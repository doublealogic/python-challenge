import os
import csv

candidates = {}

elec_csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

vote_total = 0
winning_votes = 0
winner = None

with open(elec_csvpath) as election_file:
    elec_csvreader = csv.reader(election_file, delimiter = ',')

    elec_csvheader = next(election_file)

    for row in elec_csvreader:
        vote_total += 1
        if row[2] not in candidates:
            candidates[row[2]] = 0
        candidates[row[2]] += 1

print(
    f'Election Results\n'
    f'-----------------------------------\n'
    f'Total Votes: {vote_total}\n'
    f'-----------------------------------'
)

for candidate,total_can_votes in candidates.items():
    vote_percentage = ('{:.3f}'.format((total_can_votes/vote_total) * 100))
    if total_can_votes >= winning_votes:
        winning_votes = total_can_votes
        winner = candidate
    print(
        f'{candidate}: {vote_percentage}% ({total_can_votes})'
    )

print(
    f'Winner: {winner}\n'
    f'-----------------------------------'
)