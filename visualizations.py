import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import mplcursors

# Load projections from Excel
try:
    df = pd.read_excel("salary_projections.xlsx", sheet_name="Projections")
except FileNotFoundError:
    print("Error: 'salary_projections.xlsx' not found. Run 'salary.py' first.")
    exit()

# Function to create the Bar Chart window (With Data Labels)
def show_bar_chart():
    bar_root = tk.Toplevel()
    bar_root.title("Salary Projection - Bar Chart")
    bar_root.geometry("1000x700")

    fig, ax = plt.subplots(figsize=(12, 7))

    # Bar positions
    x = np.arange(len(df["Projection"]))
    width = 0.35

    # Plot separate bars for Gross and Net Income
    bars1 = ax.bar(x - width/2, df["Gross Income"], width, color="skyblue", label="Gross Income")
    bars2 = ax.bar(x + width/2, df["Net Income"], width, color="orange", label="Net Income")

    # Add data labels above each bar
    for bar in bars1:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"${bar.get_height():,.0f}", ha='center', va='bottom', fontsize=10)
    for bar in bars2:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"${bar.get_height():,.0f}", ha='center', va='bottom', fontsize=10)

    ax.set_title("Salary Projection - Gross vs. Net Income")
    ax.set_ylabel("Salary ($)")
    ax.set_xticks(x)
    ax.set_xticklabels(df["Projection"])
    ax.legend()

    # Embed plot into Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=bar_root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    bar_root.mainloop()

# Function to create the Line Chart window (Hover Tooltips Only)
def show_line_chart():
    line_root = tk.Toplevel()
    line_root.title("Salary Projection - Line Chart (52 Weeks)")
    line_root.geometry("1000x700")

    fig, ax = plt.subplots(figsize=(14, 8))

    # Generate weekly data points based on average gross/net income
    weeks = np.arange(1, 53)
    average_gross_weekly = df[df["Projection"] == "12-Month"]["Gross Income"].values[0] / 52
    average_net_weekly = df[df["Projection"] == "12-Month"]["Net Income"].values[0] / 52

    gross_income_weekly = [average_gross_weekly * week for week in weeks]
    net_income_weekly = [average_net_weekly * week for week in weeks]

    # Plot weekly projections with smaller markers
    gross_line, = ax.plot(weeks, gross_income_weekly, marker="o", markersize=4, label="Gross Income", color="green")
    net_line, = ax.plot(weeks, net_income_weekly, marker="o", markersize=4, label="Net Income", color="red")

    # Add hover tooltips for each data point (Line Chart Only)
    mplcursors.cursor([gross_line, net_line], hover=True).connect(
        "add", lambda sel: sel.annotation.set_text(f"Week {int(sel.target[0])}\n${sel.target[1]:,.0f}")
    )

    ax.set_title("Weekly Salary Projection (52 Weeks)")
    ax.set_xlabel("Week Number")
    ax.set_ylabel("Cumulative Salary ($)")
    ax.legend()
    ax.grid(True)

    # Embed plot into Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=line_root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    line_root.mainloop()

# Main Tkinter window with buttons to open each chart
def main():
    main_root = tk.Tk()
    main_root.title("Salary Projection Dashboard")
    main_root.geometry("400x300")

    label = tk.Label(main_root, text="Choose a visualization to view:", font=("Arial", 14))
    label.pack(pady=10)

    bar_button = tk.Button(main_root, text="View Bar Chart", command=show_bar_chart, width=20, height=2)
    bar_button.pack(pady=5)

    line_button = tk.Button(main_root, text="View Line Chart (52 Weeks)", command=show_line_chart, width=20, height=2)
    line_button.pack(pady=5)

    exit_button = tk.Button(main_root, text="Exit", command=main_root.destroy, width=20, height=2)
    exit_button.pack(pady=5)

    main_root.mainloop()

# Ensure this runs only when executed directly, not during import
if __name__ == "__main__":
    main()
