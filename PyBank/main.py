# Import Modules
import os
import csv

# Variables
months = 0
total_change = 0
max_increase = 0
max_increase_date = ""
max_decrease = 0
max_decrease_date = ""
previous = 0.0
avg_change = 0
    
# Set path for the CSV file
csvpath = os.path.join('budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None) 

# Open the CSV using the set path and calculate desired information
    for row in csvreader:
        current = float(row[1])
        if months == 0:
            max_increase = 0.0
            max_decrease = 0.0
            max_increase_date = row[0]
            max_dec_date = row[0]
        else:
            delta = current - previous
            avg_change += delta
            if delta > max_increase:
                max_increase = delta
                max_increase_date = row[0]
            elif delta < max_decrease:
                max_decrease = delta
                max_dec_date = row[0]

        previous = current
        months += 1
        total_change += float(row[1])

avg_change = avg_change / (months-1)

# Append results and print results
results = []
results.append("Financial Analysis")
results.append(f"Total Months: {months}")
results.append(f"Net Total in Profit/Losses: ${round(total_change)}")
results.append(f"Average Change in Profit/Losses: ${round(avg_change,2)}")
results.append(f"Greatest Increase in Profits: {max_increase_date} (${round(max_increase)})")
results.append(f"Greatest Decrease in Profits: {max_dec_date} (${round(max_decrease)})")

# Print to txt file
filename = 'Results.txt'
with open(filename, 'w') as file:
    for result in results:
        print(result)
        file.write(result + ' ')