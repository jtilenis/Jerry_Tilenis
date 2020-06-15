# Dependencies
import os
import csv

# Specify the file to write to
output_path = os.path.join("..","Homework", "new.csv")
print("output path:" + output_path)

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Emp ID','First Name', 'Last Name', 'DOB', 'SSN', 'State'])

    # Write the second row
    csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])
