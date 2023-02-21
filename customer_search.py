import csv

infile = open("customers.csv", "r")
csvfile = csv.reader(infile)

searchname = input("\nPlease enter the name to search for: ")

foundName = False

next(csvfile)  # skip the first line which is the header

for record in csvfile:
    if searchname.lower() == record[1].lower():
        print("\nMatch Found!\n")
        print(f"First Name: {record[1]}")
        print(f"Last Name: {record[2]}")
        print(f"City: {record[3]}")
        print(f"Country: {record[4]}")
        print(f"Phone: {record[5]}\n")
        foundName = True

if not foundName:
    print("Match Not Found\n")
