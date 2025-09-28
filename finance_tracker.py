#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os

# File to store the spending data
DATA_FILE = "spending.csv"

# Check if the file exists; if not, create it with columns
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["Date", "Category", "Description", "Amount"])
    df.to_csv(DATA_FILE, index=False)

# Load existing data
df = pd.read_csv(DATA_FILE)

def log_spending():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Transport, Bills): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    new_entry = pd.DataFrame({
        "Date": [date],
        "Category": [category],
        "Description": [description],
        "Amount": [amount]
    })

    global df
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)
    print("Spending logged successfully!")

def monthly_summary():
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")

    monthly_totals = df.groupby(["Month", "Category"])["Amount"].sum().unstack(fill_value=0)
    print("\nMonthly Summary:")
    print(monthly_totals)

    # Plot the summary
    monthly_totals.plot(kind="bar", stacked=True, figsize=(10,6))
    plt.title("Monthly Spending by Category")
    plt.ylabel("Amount")
    plt.xlabel("Month")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Log Spending")
        print("2. View Monthly Summary")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            log_spending()
        elif choice == "2":
            monthly_summary()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()