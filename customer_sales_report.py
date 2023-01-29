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

prevCustomerID = -1
prevCustomerTotal = 0
firstRow = True

while True:
    try:
        # using a for loop you can step through the file, one line at a time
        for record in sales_file:
            # customerID will be retrieved from the sales file
            customerID = record[0]

            # calcTotal will be the sum of all the costs
            calcTotal = float(record[3]) + float(record[4]) + float(record[5])

            # If this is the very first row we will set up the variables for comparison
            if firstRow == True:
                prevCustomerID = customerID
                prevCustomerTotal = calcTotal
                firstRow = False
            # Once the setup is complete we will check to add the total value for each customer
            else:
                if prevCustomerID == customerID:
                    prevCustomerTotal += calcTotal
                else:
                    salesreport_writer.writerow(
                        [prevCustomerID, round(prevCustomerTotal, 2)]
                    )
                    prevCustomerID = customerID
                    prevCustomerTotal = calcTotal
        # If this is the end of the file, there will be an exception
        next(sales_file)
    except StopIteration:
        # Since, the loop has completed without inserting the final customer info, we will insert before exiting the program.
        salesreport_writer.writerow([prevCustomerID, round(prevCustomerTotal, 2)])
        # Close write file
        salesreport.close()
        break
