
"""
Stats_Engine
Author: Aniket M. Warghat

"""

import numpy as np
import random

# --- Step 1: Data Generation ---
# Create a 5x3 array (5 rows, 3 columns) of random integers between 150 and 400
# Imagine this as 5 different measurements taken at 3 different locations
soil_data = np.random.randint(150, 400, size=(5, 3))

# --- Step 2: Matrix Transposition ---
# Flip the matrix (rows become columns and columns become rows)
# The resulting 'flipped_data' will be a 3x5 array
flipped_data = soil_data.T

print("Flipped Data Matrix:")
print(flipped_data)

# --- Step 3: Statistical Analysis ---
# Calculate the mean (average) for each site
# axis=1 means we calculate across the rows of the flipped matrix
site_average = np.mean(flipped_data, axis=1)

# Calculate the Standard Deviation of the entire dataset
# This shows how much the values typically vary from the average
overall_std = np.std(flipped_data)

# Calculate the Variance (Standard Deviation squared)
# This measures the spread of the data points
variance = np.var(flipped_data)

# --- Step 4: Results Output ---
print(f"Average for each site: {site_average}")
print(f"Project Standard Deviation: {overall_std:.2f}")
print(f"Total Variance: {variance:.2f}")