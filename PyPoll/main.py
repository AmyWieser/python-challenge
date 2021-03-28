# Import Modules
import os
import csv
import sys

#create variables
total_votes = 0
candidate_listing = []
candidate_name = []
candidate_votes = []
percent_vote = []

# Define csv file
election_data = os.path.join("Resources", "election_data.csv")

# open csvfile:
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# store the header row so it won't be included in calculations
    csv_header = next(csvreader)

# Loop through the file
    for row in csvreader:
        # Add total votes
        total_votes = total_votes + 1

        # Create listing for each candidate
        candidate_listing.append(row[2])

    # Sum votes for each candidate, 
    # i is the reference to the position in set, 
    # v is the count of votes per each candidate name, 
    # p is the percentage of votes per each candidate name
    for i in set(candidate_listing):
            candidate_name.append(i) 
            v = candidate_listing.count(i)
            candidate_votes.append(v) 
            p = round((v/total_votes)*100,4)
            percent_vote.append(p)

    # find winner of the election
    top_candidate_counts = max(candidate_votes)
    winning_candidate_name = candidate_name[candidate_votes.index(top_candidate_counts)]
    

# print election results
print(f"Election Results")
print("--------------------------------------------")
print(f"Total Voles: {total_votes}")
print("--------------------------------------------")
print(str(candidate_name[0])+" "+str(percent_vote[0])+"% "+"(" +str(candidate_votes[0])+")")
print(str(candidate_name[1])+" "+str(percent_vote[1])+"% "+"(" +str(candidate_votes[1])+")")
print(str(candidate_name[2])+" "+str(percent_vote[2])+"% "+"(" +str(candidate_votes[2])+")")
print(str(candidate_name[3])+" "+str(percent_vote[3])+"% "+"(" +str(candidate_votes[3])+")")
print("--------------------------------------------")
print(f"Winner: {winning_candidate_name}") 
print("--------------------------------------------")

# print to text file
sys.stdout = open('log.txt', 'w')
print(f"Election Results")
print("--------------------------------------------")
print(f"Total Voles: {total_votes}")
print("--------------------------------------------")
print(str(candidate_name[0])+" "+str(percent_vote[0])+"% "+"(" +str(candidate_votes[0])+")")
print(str(candidate_name[1])+" "+str(percent_vote[1])+"% "+"(" +str(candidate_votes[1])+")")
print(str(candidate_name[2])+" "+str(percent_vote[2])+"% "+"(" +str(candidate_votes[2])+")")
print(str(candidate_name[3])+" "+str(percent_vote[3])+"% "+"(" +str(candidate_votes[3])+")")
print("--------------------------------------------")
print(f"Winner: {winning_candidate_name}") 
print("--------------------------------------------")