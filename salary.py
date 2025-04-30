import pandas as pd
from datetime import datetime, timedelta

# Load paychecks from Excel
excel_file = "paychecks.xlsx"
try:
    df = pd.read_excel(excel_file, engine="openpyxl")
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Gross Salary"] = pd.to_numeric(df["Gross Salary"], errors="coerce")
    df["Filing Status"] = df["Filing Status"].str.lower().fillna("single")
    df.dropna(subset=["Date", "Gross Salary"], inplace=True)
    print(f"Loaded {len(df)} valid paychecks from {excel_file}.")
except FileNotFoundError:
    print(f"Error: '{excel_file}' not found.")
    exit()

if df.empty:
    print("Error: No valid paychecks found.")
    exit()

# Tax brackets for single and married filers
TAX_BRACKETS = {
    "single": [
        (626350, 0.37), (250525, 0.35), (197300, 0.32),
        (103350, 0.24), (48475, 0.22), (11925, 0.12), (0, 0.10)
    ],
    "married": [
        (751600, 0.37), (501050, 0.35), (394600, 0.32),
        (206700, 0.24), (96950, 0.22), (23850, 0.12), (0, 0.10)
    ],
}

# Calculate net salary after taxes
def calculate_net_salary(gross_salary, filing_status):
    tax_brackets = TAX_BRACKETS[filing_status]
    remaining_income = gross_salary
    net_income = 0

    for threshold, rate in tax_brackets:
        if remaining_income > threshold:
            taxable_amount = remaining_income - threshold
            tax = taxable_amount * rate
            net_income += taxable_amount - tax
            remaining_income = threshold

    return net_income

# Determine pay frequency based on date intervals
df.sort_values(by="Date", inplace=True)
pay_interval = int(df["Date"].diff().dropna().mean().days)  # FIXED
average_gross = df["Gross Salary"].mean()

if pay_interval <= 7:
    pay_frequency = "weekly"
    periods_per_year = 52
elif pay_interval <= 14:
    pay_frequency = "biweekly"
    periods_per_year = 26
else:
    pay_frequency = "monthly"
    periods_per_year = 12

print(f"Pay Frequency: {pay_frequency} ({periods_per_year} periods/year)")
print(f"Average Gross Paycheck: ${average_gross:.2f}")


# Generate projections based on filing status
projections = {"1-Month": 4, "6-Month": 26, "12-Month": periods_per_year}
results = []

for label, periods in projections.items():
    total_gross = 0
    total_net = 0

    # Calculate based on individual filing status
    for _, row in df.iterrows():
        filing_status = row["Filing Status"]
        gross = row["Gross Salary"]
        net = calculate_net_salary(gross, filing_status)

        total_gross += gross * periods / len(df)
        total_net += net * periods / len(df)

    results.append({
        "Projection": label,
        "Gross Income": round(total_gross, 2),
        "Net Income": round(total_net, 2)
    })

# Save projections to Excel
projection_df = pd.DataFrame(results)
with pd.ExcelWriter("salary_projections.xlsx") as writer:
    projection_df.to_excel(writer, index=False, sheet_name="Projections")

print(f"Projections saved to 'salary_projections.xlsx'.")
