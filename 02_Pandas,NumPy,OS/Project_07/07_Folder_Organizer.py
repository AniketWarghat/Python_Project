"""
Folder_Organizer
Author: Aniket M. Warghat

"""
import os
import shutil

# --- Step 1: Define Path Hierarchy ---
# Get the absolute path of the directory where this script is currently located
folder = os.path.join(os.path.dirname(__file__))

# Navigate to the 'Expense Report' folder located in a sibling project directory ('Project_06')
target_path = os.path.join(folder, "..", "Project_06", "Expense Report")

# Retrieve a list of all items (files and folders) inside the target directory
list_dir = os.listdir(target_path)

# --- Step 2: Filter and Organize Files ---
for i in list_dir:
    # Split the filename into its name and extension (e.g., 'Report' and '.csv')
    name, extension = os.path.splitext(i)
    
    # Check if the file is a CSV spreadsheet
    if extension == ".csv":
        # Define the destination path for spreadsheets
        subfolder_path = os.path.join(target_path, "Spreadsheet")
        
        # Create the 'Spreadsheet' subfolder if it does not already exist
        if not os.path.exists(subfolder_path):
            os.mkdir(subfolder_path)
        
        # Define the full source path and the full destination path
        source = os.path.join(target_path, i)
        destination = os.path.join(subfolder_path, i)
        
        # Move the file from the root 'Expense Report' folder into the 'Spreadsheet' folder
        shutil.move(source, destination)
        print(f"Moved {i}")

# Print the final location of the organized files
print(subfolder_path)