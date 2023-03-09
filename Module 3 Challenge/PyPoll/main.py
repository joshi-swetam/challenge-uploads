# Import Dependencies
import os
import csv

# create variable
candidate = ""
total_Votes = 0
candidate_votes = {}

#assign path for csv file
file_path = os.path.join("Resources","election_data.csv")

# read csv file 
with open(file_path) as csv_file:
    election_data_reader = csv.reader(csv_file, delimiter=',')
    next(election_data_reader)
    for row in election_data_reader:
        candidate = str(row[2])

# total number of votes cast
        total_Votes += 1

#total number of votes and percentage each candidate won        
        if len(candidate_votes) == 0 or candidate not in candidate_votes:
            candidate_votes[candidate] = 1
        else:
            candidate_votes[candidate] += 1

# winner of the election based on maximum vote
winner = max(candidate_votes, key=candidate_votes.get)


print(f"  ```text\n")
print(f"  Election Results\n")
print(f"  -------------------------\n")
print(f"  Total Votes: {total_Votes}\n")
print(f"  -------------------------\n")
for candidate_name, vote_count in candidate_votes.items():
    print(f"  {candidate_name}: {vote_count*100/total_Votes:.3f}% ({vote_count})\n")
print(f"  -------------------------\n")
print(f"  Winner: {winner}\n")
print(f"  -------------------------\n")
print(f"  ```\n") 
   
with open('pypoll_anlaysis.txt','w') as file:
    file.write(f"  ```text\n")
    file.write(f"  Election Results\n")
    file.write(f"  -------------------------\n")
    file.write(f"  Total Votes: {total_Votes}\n")
    file.write(f"  -------------------------\n")
    for candidate_name, vote_count in candidate_votes.items():
        file.write(f"  {candidate_name}: {vote_count*100/total_Votes:.3f}% ({vote_count})\n")
    file.write(f"  -------------------------\n")
    file.write(f"  Winner: {winner}\n")
    file.write(f"  -------------------------\n")
    file.write(f"  ```\n")