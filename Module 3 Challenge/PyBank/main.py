# Import Dependencies
import os
import csv

# create variable 
date = 0
profit_loss = 0
previous_profit_loss = 0

total_month = 0
total_profit_loss = 0
change = []

max_change_period = ""
max_change = 0

min_change_period = ""
min_change = 0

#assign path for csv file
file_path = os.path.join("Resources","budget_data.csv")

# read csv file 
with open(file_path) as csv_file:
    budeget_reader = csv.reader(csv_file, delimiter=',')
    next(budeget_reader)

    for row in budeget_reader:
        date = row[0]
        profit_loss = int(row[1])

        #calculate total months
        total_month += 1

        #calculate total profit/loss amount
        total_profit_loss += profit_loss

        #calculate  average of  "Profit/Losses"
        if len(change) == 0:
            change.append(0)
            previous_profit_loss = profit_loss
        else:
            change.append(profit_loss - previous_profit_loss)
            previous_profit_loss = profit_loss

        #calculate greatest increase-decrease in profits (date and amount)
        if change[-1] < 0 and change[-1] < min_change:
            min_change_period = date
            min_change = change[-1]
        elif change[-1] >= 0 and change[-1] > max_change:
            max_change_period = date
            max_change = change[-1]
        

print(f'```text')
print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total Months: {total_month}')
print(f'Total: ${total_profit_loss}')
print(f"Average Change: ${sum(change)/(len(change)-1):.2f}")
print(f"Greatest Increase in Profits: {max_change_period} (${max(change)})")
print(f"Greatest Decrease in Profits: {min_change_period} (${min(change)})")
print(f"```")

with open('pybank_anlaysis.txt','w') as file:
    file.write(f"  ```text\n")
    file.write(f"  Financial Analysis\n")
    file.write(f"  ----------------------------\n")
    file.write(f"  Total Months: {total_month}\n")
    file.write(f"  Total: ${total_profit_loss}\n")
    file.write(f"  Average Change: ${sum(change)/(len(change)-1):.2f}\n")
    file.write(f"  Greatest Increase in Profits: {max_change_period} (${max_change})\n")
    file.write(f"  Greatest Decrease in Profits: {min_change_period} (${min_change})\n")
    file.write(f"  ```")