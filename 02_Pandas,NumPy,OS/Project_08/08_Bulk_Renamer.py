"""
Bulk_Renamer
Author: Aniket M. Warghat

"""

import os

# --- Step 1: Define Path Hierarchy ---
# Get the absolute path of the directory where this script is currently located
current_path = os.path.join(os.path.dirname(__file__))

# Navigate to the 'Expense Report' folder located in a sibling project directory ('Project_06')
source_folder = os.path.join(current_path, "..", "Project_06", "Expense Report")

# Define the final target directory containing the files to be renamed
target_path = os.path.join(source_folder, "Spreadsheet")

# --- Step 2: List Target Files ---
# Retrieve a list of all files and folders inside the 'Spreadsheet' directory
list_files = os.listdir(target_path)

# --- Step 3: Batch Rename Logic ---
for i in list_files:
    # Define the standardized prefix for the files
    prefix = "2026_Project_"
    new_name = prefix + i

    # Construct the full absolute paths for the current file and the intended new name
    old_path = os.path.join(target_path, i)
    new_path = os.path.join(target_path, new_name)
    
    # Check if the file already has the prefix to avoid redundant renaming (e.g., 2026_Project_2026_Project_...)
    if not i.startswith(prefix):
        # Execute the rename operation on the file system
        os.rename(old_path, new_path)

# Print confirmation to indicate the loop has finished
print(f"Renaming complete in: {target_path}")