# program that reads the file customers.csv and produces a new file containing the customer name and country they are from

import csv

# open the csv file in read mode
customers = open("customers.csv", "r")
# using the csv library, create a csv object the delimiter ',' tells the program how the columns are seperated
customer_file = csv.reader(customers, delimiter=",")
# skip the first line in the csv file if it contains a header record in this file it would be "ID,FirstName,LastName,City,Country,Phone"
next(customer_file)

# Create a new file to write the customer name and country to
customer_country = open("customer_country.csv", "w", newline="")

# Create a writer to write into the customer_country file
customer_country_writer = csv.writer(customer_country)

# Write the Header Row of customer_country file
header = ["Name", "Country"]
customer_country_writer.writerow(header)

# using a for loop you can step through the file, one line at a time
for record in customer_file:
    # For every row in the customer file, the first and last name will be concatenated to be name
    name = record[1] + " " + record[2].rstrip("\n")
    # country will be country
    country = record[4].rstrip("\n")
    # and written in the new file: "customer_country.csv"
    customer_country_writer.writerow([name, country.rstrip("\n")])
