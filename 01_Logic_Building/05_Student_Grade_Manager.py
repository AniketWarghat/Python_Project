"""
Student Grade Manager
Author: Aniket M. Warghat
Description: A simple CLI Student Grade Manager Where User Can add student grade and 
the grade get stored in .csv file and st the end the total Score of student is printed. 
"""


import os
import csv

print("Welcome to Student Score Manager! \n")

# --- Setup File Path ---
py_dir = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(py_dir, "05_Reports")
filename = "Student_grade.csv"
full_path = os.path.join(folder, filename)

# Create the target directory if it doesn't already exist
if not os.path.exists(folder):
    os.mkdir(folder)

# List to store student dictionaries
students = []

# --- Data Entry Loop ---
while True:
    
    try:
        # Prompt user to continue or exit
        option = str(input("Add Student ? (y/n) : "))
    except ValueError:
        print("Not a Valid input! Try again")
    
    # Check if user wants to add a new student
    if option == "y" or option == "yes":
        data = {}
        
        # Collect Student Name
        key = "name"
        name = input("Enter Student Name : ")
        data[key] = name
        
        # Collect Math Score and store in dictionary
        key1 = "math"
        math = int(input("Enter Math Score : "))
        data[key1] = math
        
        # Collect Science Score and store in dictionary
        key2 = "science"
        sci = int(input("Enter Science Score : "))
        data[key2] = sci
        
        # Append the individual student dictionary to the list
        students.append(data)
        
    elif option == "n" or option == "no":
        # Exit the loop if user is finished
        print("\n Good Bye! Have a grate Day. \n")
        break
    else:
        # Handle unexpected inputs
        print("Enter Y (yes) or n (no)")

# --- Writing to CSV ---
# Open the file in write mode ('w') and define headers
with open(full_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "math", "science"])
    writer.writeheader()   # Write the header row
    writer.writerows(students) # Write all student data rows

# --- Reading and Processing CSV ---
# Re-open the file in read mode ('r') to display results
with open(full_path, 'r', newline="") as csv_file:
    print ("Student Total Score ->")
    csv_reader = csv.DictReader(csv_file)
    count = 0
    
    # Iterate through each row in the CSV
    for i in csv_reader:
        count += 1
        # Calculate the sum of math and science scores
        score = int(i["math"]) + int(i["science"])
        # Print the formatted result for each student
        print(f"{count}.{i['name']} | Total Score : {score}")

print(f"\n Task Complete! check {folder} for {filename}")