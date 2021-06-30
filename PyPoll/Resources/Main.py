import csv
import os

#Path to collect data from the Resources folder - had to determine absolute path
This_File = os.path.dirname(os.path.abspath(__file__))

election_data = os.path.join(This_File, "election_data.csv")

#Open and read csv
with open(election_data, 'r') as csvfile:

    #Establishing file parameters to be read
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Read the header row first and ignore
    header = next(csvfile)

    #Setting up lists and setting votes to null before count, CandidatePool is all of the candidates
    VotesPerCandidate = []
    CandidatePool = []
    NumberOfVotes = 0

    #Extracting data from csv file
    for row in csvreader:
        
        #Tallying the votes for each candidate in each row
        NumberOfVotes = NumberOfVotes + 1

        #Identifying that the candidate name is in index column 2 that was voted for
        Candidate = row[2]

        #Counting the votes for each candidate and adding to the list
        if Candidate in CandidatePool:

            CandidateLoc = CandidatePool.index(Candidate)

            VotesPerCandidate[CandidateLoc] = VotesPerCandidate[CandidateLoc] + 1

        else:

            CandidatePool.append(Candidate)

            VotesPerCandidate.append(1)

MaxVotes = VotesPerCandidate[0]

#Creating a new list to determine which candidate has the highest number of counts and percentage
PercentageOfVotes = []

Max = 0

#Counting the number of Candidates in the list
for count in range(len(CandidatePool)):

    #Calculating the percentage of votes for candidates
    Percentage =  (VotesPerCandidate[count]/NumberOfVotes * 100)

    PercentageOfVotes.append(Percentage)

    #Checking who has the most votes
    if VotesPerCandidate[count] > MaxVotes:

        MaxVotes = VotesPerCandidate[count]

        Max = count

#Establishing the winner of the election
ElectionWinner = CandidatePool[Max] 

#Display Final Voting Summary on Terminal
print(" \n") #adding additional blank lines -purley asthetic

print("Election Results Summary")

print("------------------------")

print(f"Total Votes: {NumberOfVotes}")

print("------------------------")

for count in range(len(CandidatePool)):

   print(f"{CandidatePool[count]}: {PercentageOfVotes[count]}% ({VotesPerCandidate[count]})")

print("------------------------")

print(f"Winner: {ElectionWinner}")


#Export text file of Final vote count summary
OutFile = os.path.dirname(os.path.abspath(__file__))

SummaryFileExport = os.path.join(OutFile, "election_summary.txt")

with open(SummaryFileExport, 'w') as TextFile:
     TextFile.write(" \n\n\n")
     TextFile.write("Election Results Summary\n")
     TextFile.write("--------------------------------\n")
     TextFile.write(f"Total Votes: {NumberOfVotes}\n")
     TextFile.write("--------------------------------\n")
     
     for count in range(len(CandidatePool)):
        TextFile.write(f"{CandidatePool[count]}: {PercentageOfVotes[count]}% ({VotesPerCandidate[count]})\n")
     
     TextFile.write("--------------------------------\n")
     TextFile.write(f"Winner: {ElectionWinner}\n")
     
