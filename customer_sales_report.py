# program that reads the sales.csv file and creates a new file with the customer ID and calculated total (as shown in salesreport.csv)
import csv

# open the csv file in read mode
sales = open("sales.csv", "r")
# using the csv library, create a csv object the delimiter ',' tells the program how the columns are seperated
sales_file = csv.reader(sales, delimiter=",")
# skip the first line in the csv file if it contains a header record in this file it would be "ID,FirstName,LastName,City,Country,Phone"
next(sales_file)

# Create a new file to write the customer ID and calculated total
salesreport = open("salesreport.csv", "w", newline="")

# Create a writer to write into the sales file
salesreport_writer = csv.writer(salesreport)

# Write the Header Row of sales file
salesreport_writer.writerow(["Customer ID", "Calculated Total"])

# using a for loop you can step through the file, one line at a time
for record in sales_file:
    # customerID will be retrieved from the sales file
    customerID = record[0]
    print(type(sales_file))

    """
    if customerID == sales_file[record-1][0]
    # calcTotal will be the sum of all the costs
    calcTotal = float(record[3]) + float(record[4]) + float(record[5])
    calcTotal = "%.2f" % calcTotal

    # and written in the new file: "salesreport.csv"
    salesreport_writer.writerow([customerID, calcTotal])
    """
