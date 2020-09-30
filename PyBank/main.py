import os
import csv

profit_losses = []

csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

month_total = 0
net_total = 0
profit_change = 0
prev_profit = 0

with open(csvpath) as budget_file:
    csv_reader = csv.reader(budget_file, delimiter = ',')
    
    csv_header = next(budget_file)

    for row in csv_reader:
        month_total = (month_total + 1)
        net_total = (net_total + int(row[1]))
        if prev_profit != 0:
            profit_change = int(row[1]) - prev_profit
            profit_losses.append(profit_change)
            prev_profit = int(row[1])
        else: 
            prev_profit = int(row[1])

    average_change = round((sum(profit_losses) / len(profit_losses)), 2)

print(
    f"Financial Analysis\n"
    f"------------------------------------------\n"
    f"Total Months: {month_total}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change}\n"
)