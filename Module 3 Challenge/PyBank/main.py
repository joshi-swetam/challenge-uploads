#read csv file
import os
import csv

date = 0
profit_loss = 0

total_month = 0
total_profit_loss = 0

#assign  a path for csv file
file_path = os.path.join("Resources","budget_data.csv")


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

        #print(total_profit_loss)

        #calculate  average of  "Profit/Losses"
        #calculate greatest increase in profits (date and amount)
        #calculate greatest decrease in profits (date and amount)

print(f'```text')
print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total Months: {total_month}')
print(f'Total: ${total_profit_loss}') 