import os, csv
from pathlib import Path 

# importing the file
df_csv = Path("python-challenge", "PyBank", "budget_data.csv")

# Defining the specific variables
total_profit = []
total_months = []
monthly_profit_change = []
 
# Open csv
with open(df_csv,newline="", encoding="utf-8") as budgetcsv:
     # storing in a variable
    fileread = csv.reader(budgetcsv,delimiter=",") 
    # ignoring header
    header = next(fileread)  
    # iterating
    for row in fileread: 
        # Append lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    # iterating for monthly change in profits
    for i in range(len(total_profit)-1): 
        # difference and monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])        
# max and min of the the montly profit change
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)
# match the month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print data
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Output
output_file = Path("python-challenge", "PyBank", "Financial_Analysis_Summary.txt")

with open(output_file,"w") as file:    
# print to summary
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
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


