
#Imports
import csv
from pathlib import Path

#read file data
csvpath = Path('..\Resources\budget_data.csv')

#read cvs file in dictionary format
with open(Path, newline="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    data = list(csvreader)
    
#Calculate the total number of months included in the dataset
total_months = len(data)


# The greatest increase in profits (date and amount) over the entire period
greatest_increase = 0

for i in range(1, len(data)):
    if int(data[i]["Profit/Losses"]) - int(data[i-1]["Profit/Losses"]) > greatest_increase:
        greatest_increase = int(data[i]["Profit/Losses"]) - int(data[i-1]["Profit/Losses"])
        greatest_increase_date = data[i]["Date"]


# The average of the changes in Profit/Losses over the entire period
change = 0
for i in range(1, len(data)):
    change += int(data[i]["Profit/Losses"]) - int(data[i-1]["Profit/Losses"])
average_change = change / (len(data) - 1)

#round to 2 decimal places
average_change = round(average_change, 2)


# The greatest increase in profits (date and amount) over the entire period
greatest_increase = 0
for i in range(1, len(data)):
    if int(data[i]["Profit/Losses"]) - int(data[i-1]["Profit/Losses"]) > greatest_increase:
        greatest_increase = int(data[i]["Profit/Losses"]) - int(data[i-1]["Profit/Losses"])
        greatest_increase_date = data[i]["Date"]

# The greatest decrease in losses (date and amount) over the entire period
greatest_decrease = 0
for i in range(1, len(data)):
    if int(data[i]["Profit/Losses"]) - int(data[i-1]["Profit/Losses"]) < greatest_decrease:
        greatest_decrease = int(data[i]["Profit/Losses"]) - int(data[i-1]["Profit/Losses"])
        greatest_decrease_date = data[i]["Date"]


#Print the financial analysis 
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
