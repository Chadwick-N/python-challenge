import os
import csv

voter_id_list = []
county_list = []
candidate_list = []
khan_vote = 0
correy_vote = 0
li_vote = 0
otooley_vote = 0
khan = "Khan"
correy = "Correy"
li = "Li"
otooley = "O'Tooley"

election_file = os.path.join('resources', 'election_data.csv')

with open(election_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        voter_id_list.append(row[0])
        county_list.append(row[1])
        candidate_list.append(row[2])

for x in candidate_list:
    if x == "Khan":
        khan_vote += 1
    elif x == correy:
        correy_vote += 1
    elif x == li:
        li_vote += 1
    elif x == otooley:
        otooley_vote += 1

def popular_candidate(candidate_list): 
    return max(set(candidate_list), key = candidate_list.count)

total_votes_cast = len(voter_id_list) # total votes cast

khan_value = round(int(khan_vote)/int(total_votes_cast), 2)
khan_percent = "{:.0%}".format(khan_value)

correy_value = round(int(correy_vote)/int(total_votes_cast), 2)
correy_percent = "{:.0%}".format(correy_value)

li_value = round(int(li_vote)/int(total_votes_cast), 2)
li_percent = "{:.0%}".format(li_value)

otooley_value = round(int(khan_vote)/int(total_votes_cast), 2)
otooley_percent = "{:.0%}".format(otooley_value)

print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes_cast}")
print("-----------------------")
print(f"Khan: {khan_percent} {khan_vote}")
print(f"Li: {li_percent} {li_vote}")
print(f"Correy: {correy_percent} {correy_vote}")
print(f"O'Tooley: {otooley_percent} {otooley_vote}")
print("-----------------------")
print("Winner: " + popular_candidate(candidate_list)) 
print("-----------------------")

pypoll_analysis_file = os.path.join("analysis", "pypoll_analysis_file.txt")
file = open(pypoll_analysis_file, 'w')

file.write("Election Results" + '\n')
file.write("-----------------------" + '\n')
file.write(f"Total Votes: {total_votes_cast}" + '\n')
file.write("-----------------------" + '\n')
file.write(f"Khan: {khan_percent} {khan_vote}" + '\n')
file.write(f"Li: {li_percent} {li_vote}" + '\n')
file.write(f"Correy: {correy_percent} {correy_vote}" + '\n')
file.write(f"O'Tooley: {otooley_percent} {otooley_vote}" + '\n')
file.write("-----------------------" + '\n')
file.write("Winner: " + popular_candidate(candidate_list) + '\n') 
file.write("-----------------------" + '\n')

#Your task is to create a Python script that analyzes the votes and calculates 
# each of the following:

#  * The total number of votes cast(x)

# * A complete list of candidates who received votes(x) if stament

#  * The percentage of votes each candidate won(x) 

#  * The total number of votes each candidate won(x) if statement

#  * The winner of the election based on popular vote.() if statemnt


#* As an example, your analysis should look similar to the one below:
#
# ```text
#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------
#  ```