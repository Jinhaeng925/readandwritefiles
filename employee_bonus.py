# program that reads the EmployeePay.csv file and prints out details of each employee

import csv

# open the csv file in read mode
employeePay = open("EmployeePay.csv", "r")
# using the csv library, create a csv object the delimiter ',' tells the program how the columns are seperated
employeePay_file = csv.reader(employeePay, delimiter=",")
# skip the first line in the csv file
next(employeePay_file)

# using a for loop you can step through the file, one line at a time
for record in employeePay_file:
    employeeID = record[0]
    employeeFullName = record[1] + " " + record[2]
    salary = float(record[3])
    bonus = 1 + float(record[4])
    totalSalary = format(round((salary * bonus), 2), ",")

    # Ask for input for each employee
    input()
    print(
        f"Employee ID: {employeeID} \n   Full Name: {employeeFullName} \n   Total Salary ($): {totalSalary}"
    )
