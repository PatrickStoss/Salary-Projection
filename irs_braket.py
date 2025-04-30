import pandas as pd

# Define the 2025 tax brackets
tax_brackets = [
    {"Tax Rate": "37%", "Single Income Over": "$626,350", "Married Income Over": "$751,600"},
    {"Tax Rate": "35%", "Single Income Over": "$250,525", "Married Income Over": "$501,050"},
    {"Tax Rate": "32%", "Single Income Over": "$197,300", "Married Income Over": "$394,600"},
    {"Tax Rate": "24%", "Single Income Over": "$103,350", "Married Income Over": "$206,700"},
    {"Tax Rate": "22%", "Single Income Over": "$48,475", "Married Income Over": "$96,950"},
    {"Tax Rate": "12%", "Single Income Over": "$11,925", "Married Income Over": "$23,850"},
    {"Tax Rate": "10%", "Single Income Over": "$11,925 or less", "Married Income Over": "$23,850 or less"},
]

# Convert to DataFrame
df = pd.DataFrame(tax_brackets)

# Display tax brackets
print("2025 IRS Tax Brackets:")
print(df)
