import os
import csv

elec_csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

vote_total = 0

with open(elec_csvpath) as election_file:
    elec_csvreader = csv.reader(election_file, delimiter = ',')

    elec_csvheader = next(election_file)

    for row in elec_csvreader:
        vote_total = (vote_total + 1)

print(
    f'Election Results\n'
    f'-----------------------------------\n'
    f'Total Votes: {vote_total}\n'
    f'-----------------------------------\n'
)