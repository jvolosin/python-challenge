import os

import csv

csvpath = os.path.join(r'C:\Users\jvolo\python-challenge\PyBank\Resources\budget_data.csv')

# Set the Variables 
total_months = 0 
net_total = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Don't count the header
    header = next(csvreader) 

    for row in csvreader: 

         # Count the number of months
        total_months +=1

print(f"Total Months: {total_months}")

