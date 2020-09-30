import os
import csv

csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')
month_total = 0

with open(csvpath) as budget_file:
    csv_reader = csv.reader(budget_file, delimiter = ',')
    
    csv_header = next(budget_file)

    for row in csv_reader:
        month_total = (month_total + 1)

print(
    f"Financial Analysis\n"
    f"------------------------------------------\n"
    f"Total Months: {month_total}\n"
)