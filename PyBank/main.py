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
        
for i in range(len(Profloss)- 1):
    change = Profloss[i + 1] - Profloss[i]
    change_list.append(change)

sum_profitloss = sum(Profloss) 
average_change = sum(change_list)/len(change_list)
Total_Months = len(Date)
max_change = max(change_list)
min_change = min(change_list)
max_change_index = change_list.index(max_change)
min_change_index = change_list.index(min_change)
max_change_date = Date[max_change_index + 1]
min_change_date = Date[min_change_index + 1]

print(Total_Months)
print(sum_profitloss)
print(max_change_date)
print(min_change_date)

# Your task is to create a Python script that analyzes the records to 
# calculate each of the following:
# - skip header(x)

#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period(x)
# - append rows for date and profloss(x)

# - once net total is found, average can be calculated(x)

#The average of the changes in "Profit/Losses" over the entire period (x)

#The greatest increase in profits (date and amount) over the entire period
# - find max()

#The greatest decrease in losses (date and amount) over the entire period
# - find min()

#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# - output readme()