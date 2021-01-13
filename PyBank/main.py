import os
import csv

Date = []
Profloss = []
change_list = []

Budgetfile = os.path.join('resources', 'budget_data.csv')

with open(Budgetfile) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        Date.append(row[0])
        Profloss.append(int(row[1]))
        
        
        
for i in range(len(Profloss) - 1):
    change = Profloss[i + 1] - Profloss[i]
    change_list.append(change)

sum_profitloss = sum(Profloss) 
average_change = round(sum(change_list)/len(change_list), 2)
Total_Months = len(Date)
max_change = max(change_list)
min_change = min(change_list)
max_change_index = change_list.index(max_change)
min_change_index = change_list.index(min_change)
max_change_date = Date[max_change_index + 1]
min_change_date = Date[min_change_index + 1]

print("Financial Analysis")
print("---------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${sum_profitloss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Incease in Profts: {max_change_date} $ {max_change}")
print("Greatest Decrease in Profits: " + str(min_change_date) + "  $" + str(min_change))

pybank_analysis_file = os.path.join("analysis", "pybank_analysis_file.txt")
file = open(pybank_analysis_file, 'w')

file.write("Financial Analysis")
file.write("---------------------")
file.write(f"Total Months: {Total_Months}" + '\n')
file.write(f"Total: ${sum_profitloss}" + '\n')
file.write(f"Average Change: ${average_change}" + '\n')
file.write(f"Greatest Incease in Profts: {max_change_date} $ {max_change}" + '\n')
file.write("Greatest Decrease in Profits: " + str(min_change_date) + "  $" + str(min_change) + '\n')

# Your task is to create a Python script that analyzes the records to 
# calculate each of the following:
# - skip header(x)

#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period(x)
# - append rows for date and profloss(x)

# - once net total is found, average can be calculated(x)

#The average of the changes in "Profit/Losses" over the entire period (x)

#The greatest increase in profits (date and amount) over the entire period
# - find max(x)

#The greatest decrease in losses (date and amount) over the entire period
# - find min(x)

#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# - output readme(x)