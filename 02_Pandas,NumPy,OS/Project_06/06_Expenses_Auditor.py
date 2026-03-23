"""
Expenses_Auditor
Author: Aniket M. Warghat

"""


import pandas as pd
import numpy as np
import random as rd
from datetime import datetime, timedelta
import os

# Define the categories for the expense transactions
categories = ["Home","Travel","Shopping","Food","Subscriptions"]
Data_list = []

# --- Step 1: Data Generation ---
# Generate 1,000 random transaction records
for i in range(1000):
    # Create a random date within the last 60 days
    random_days = rd.randint(0,60)
    txn_date = datetime.now() - timedelta(days=random_days)

    # Construct a dictionary for each row
    row = {
        "Transaction ID": 1000 + i,
        "Date": txn_date.strftime("%d-%m-%Y"),
        "Category": rd.choice(categories),
        "Amount": round(rd.uniform(50, 2500), 3) # Random float between 50 and 2500
    }
    Data_list.append(row)

# --- Step 2: Directory & Path Management ---
# Get the absolute path of the current script to ensure correct folder creation
py_dict = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(py_dict, "Expense Report")

# Create the 'Expense Report' folder if it doesn't exist
if not os.path.exists(folder):
    os.mkdir(folder)

filename = "Expense_Report.csv"
full_path = os.path.join(folder, filename)

# --- Step 3: Export Raw Data ---
# Convert the list of dictionaries into a Pandas DataFrame and save to CSV
df = pd.DataFrame(Data_list)
df.to_csv(full_path, index=False)
print("'Expense_Report.csv' is Ready for Analysis")

# --- Step 4: Data Analysis & Summary ---
# Reload the CSV to simulate a data processing pipeline
df = pd.read_csv(full_path)

# Filter for "High Value" transactions (optional variable, not exported)
high_value = df[df["Amount"] > 1500]

# Group data by 'Category' and calculate Sum, Mean, and Count for each
summary = df.groupby("Category")["Amount"].agg(["sum","mean","count"]).reset_index()

# Clean up formatting by rounding the calculated values
summary = summary.round({"sum": 3, "mean": 3})

# --- Step 5: Export Summary Report ---
summary_path = os.path.join(folder, "Summary_Expense_Report.csv")
summary.to_csv(summary_path, index=False)

# Re-read the summary for confirmation or further printing
df = pd.read_csv(summary_path)

print(f"file 1: Raw data -> {full_path} \nfile 2: Audit Summary -> {summary_path}")