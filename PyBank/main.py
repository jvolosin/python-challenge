import os

import csv

csvpath = os.path.join(r'C:\Users\jvolo\python-challenge\PyBank\Resources\budget_data.csv')

# Create lists for the following variables
total_months = []
total_profit = []
monthly_profit_change = []

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Don't count the header
    header = next(csvreader)  

    for row in csvreader: 

        # Append the total months and total profit to their corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Get the monthly change in profits
    for i in range(len(total_profit)-1):
        
        # Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
# Get the max and min of the the monthly profit change
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print the results
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Export a text file with the results
output_file = os.path.join("python-challenge", "PyBank", "Financial_Analysis.txt")

with open(output_file,"w") as file:
    
# Print to Financial_Analysis file
    file.write("Financial Analysis")
    file.write("\n")
    file.write("---------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

