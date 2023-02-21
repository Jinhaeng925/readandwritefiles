import csv

infile = open("customers.csv", "r")

csvfile = csv.reader(infile)

outfile = open("customer_country.csv", "w")

next(csvfile)  # skip the first line which is the header

outfile.write("Full Name, Country\n")

for record in csvfile:
    fullname = record[1] + " " + record[2]
    country = record[4]
    outfile.write(fullname + ", " + country + "\n")

outfile.close()
