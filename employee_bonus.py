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
    # prints out details of each employee
    print(record)
