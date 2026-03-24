"""
Sales_Analyzer
Author: Aniket M. Warghat

"""

import os
import pandas as pd
import openpyxl
import random as rd
from datetime import datetime, timedelta

# --- Step 1: Configuration & Variables ---
region = ["North", "South", "East", "West"]
product = ["Laptop", "Tablet", "Phone"]
data_list = []

# --- Step 2: Data Generation ---
# Generate 500 random sales transactions
for i in range(500):
    # Create a random date within the last 60 days
    random_day = rd.randint(0, 60)
    txn_date = datetime.now() - timedelta(days=random_day)

    # Build a dictionary for the current row
    row = {
        "Transaction ID": 500 + i,
        "Date": txn_date.strftime("%d-%m-%Y"),
        "Region": rd.choice(region),
        "Product": rd.choice(product),
        "Amount": round(rd.uniform(10000, 50000), 3) # Random price between 10k and 50k
    }

    data_list.append(row)

# --- Step 3: File System Management ---
# Get the absolute path of the directory where this script is saved
py_dict = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(py_dict, "Sample_Report")

# Create the output folder if it doesn't already exist
if not os.path.exists(folder):
    os.mkdir(folder)

filename = "sample_report.csv"
full_path = os.path.join(folder, filename)

# --- Step 4: Export Raw Data to CSV ---
# Convert the list of dictionaries into a Pandas DataFrame
df = pd.DataFrame(data_list)
df.to_csv(full_path, index=False)
print(f"{filename} is Ready for Analysis")

# --- Step 5: Data Analysis (Pivot Table) ---
# Read the CSV back into a DataFrame for processing
df = pd.read_csv(full_path)

# Create a Pivot Table to summarize 'Amount' by 'Region' (Rows) and 'Product' (Columns)
# It calculates the Total Sum, Average (Mean), and Transaction Count for each intersection
pivot_df = pd.pivot_table(df, values="Amount", index="Region", columns="Product", aggfunc=['sum', 'mean', 'count'])

# Round the financial figures to 3 decimal places for readability
pivot_df = pivot_df.round({"sum": 3, "mean": 3})

# --- Step 6: Multi-Sheet Excel Export ---
# Define the path for the final Excel report
excel_path = os.path.join(folder, "Final_Report.xlsx")

# Use ExcelWriter to save multiple DataFrames into a single workbook with different tabs
with pd.ExcelWriter(excel_path) as writer:
    # Save the original 500 rows to the first sheet
    df.to_excel(writer, sheet_name="Raw_Data", index=False)
    # Save the summarized Pivot Table to the second sheet
    pivot_df.to_excel(writer, sheet_name="Summary")

print(f"Final Excel Report generated at: {excel_path}")