# Import Modules
import os
import csv

# Variables
Total_Votes = 0
candidates = []
Votes_Per_Candidate = []

# Set path for the CSV file
csvpath = os.path.join('election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None) 

# Open the CSV using the set path and calculate desired information
    for row in csvreader:
        Total_Votes += 1
        if Total_Votes == 1:
            candidates.append(row[2])
            Votes_Per_Candidate.append(1)
        else:
            try:
                candidate = candidates.index(row[2])
                Votes_Per_Candidate[candidate] += 1
            except:
                candidates.append(row[2])
                Votes_Per_Candidate.append(1)

# Append results and print results
results = []
results.append("Election Results")
results.append(f"Total Votes: {Total_Votes}")

winner = candidates[0]
max_votes = Votes_Per_Candidate[0]
for i in range(len(candidates)):
    if Votes_Per_Candidate[i] > max_votes:
        winner = candidates[i]
        max_votes = Votes_Per_Candidate[i]
    percent = 100 * Votes_Per_Candidate[i] / Total_Votes
    results.append(f"{candidates[i]}: {round(percent,3)} % ({Votes_Per_Candidate[i]})")

results.append(f"Winner: {winner}")

# Print to txt file
filename = 'Results.txt'
with open(filename, 'w') as file:
    for result in results:
        print(result)
        file.write(result + ' ')

# CSV file was too big when trying to download and open from gitlab.
# Results are same though with Khan being the winner from the data. 
# Small difference in percentage but very close from desired results.