import os
import csv

voter_id_list = []
county_list = []
candidate_list = []
khan_vote = 0
correy_vote = 0
li_vote = 0
otooley_vote = 0

election_file = os.path.join('resources', 'election_data.csv')

with open(election_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        voter_id_list.append(row[0])
        county_list.append(row[1])
        candidate_list.append(row[2])

for x in candidate_list: # to calculate total number of votes, I needed to append and count the votes.
    if x == "Khan":
        khan_vote += 1
    elif x == "Correy":
        correy_vote += 1
    elif x == "Li":
        li_vote += 1
    elif x == "O'Tooley":
        otooley_vote += 1

def popular_candidate(candidate_list):  # used key to return the candidate with most votes.
    return max(set(candidate_list), key = candidate_list.count)

total_votes_cast = len(voter_id_list)

khan_value = round(int(khan_vote)/int(total_votes_cast), 2) # calculated average of % of votes as well as total vote count for each candidate. 
khan_percent = "{:.0%}".format(khan_value)

correy_value = round(int(correy_vote)/int(total_votes_cast), 2)
correy_percent = "{:.0%}".format(correy_value)

li_value = round(int(li_vote)/int(total_votes_cast), 2)
li_percent = "{:.0%}".format(li_value)

otooley_value = round(int(otooley_vote)/int(total_votes_cast), 2)
otooley_percent = "{:.0%}".format(otooley_value)

print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes_cast}")
print("-----------------------")
print(f"Khan: {khan_percent} ({khan_vote})")
print(f"Li: {li_percent} ({li_vote})")
print(f"Correy: {correy_percent} ({correy_vote})")
print(f"O'Tooley: {otooley_percent} ({otooley_vote})")
print("-----------------------")
print("Winner: " + popular_candidate(candidate_list)) 
print("-----------------------")

pypoll_analysis_file = os.path.join("analysis", "pypoll_analysis_file.txt")
file = open(pypoll_analysis_file, 'w')

file.write("Election Results" + '\n')
file.write("-----------------------" + '\n')
file.write(f"Total Votes: {total_votes_cast}" + '\n')
file.write("-----------------------" + '\n')
file.write(f"Khan: {khan_percent} ({khan_vote})" + '\n')
file.write(f"Li: {li_percent} ({li_vote})" + '\n')
file.write(f"Correy: {correy_percent} ({correy_vote})" + '\n')
file.write(f"O'Tooley: {otooley_percent} ({otooley_vote})" + '\n')
file.write("-----------------------" + '\n')
file.write("Winner: " + popular_candidate(candidate_list) + '\n') 
file.write("-----------------------" + '\n')
