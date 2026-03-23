import os
import shutil

folder = os.path.join(os.path.dirname(__file__))
target_path = os.path.join(folder, "..", "Project_06", "Expense Report")

list_dir = os.listdir(target_path)

for i in list_dir:
    name, extension = os.path.splitext(i)
    if extension == ".csv":
        subfolder_path = os.path.join(target_path, "Spreadsheet")
        if not os.path.exists(subfolder_path):
            os.mkdir(subfolder_path)
        source = os.path.join(target_path, i)
        destination = os.path.join(subfolder_path, i)
        shutil.move(source, destination)
        print(f"Moved {i}")

print(subfolder_path)