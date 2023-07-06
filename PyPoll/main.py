#PyPoll

import os
import csv

folder_path = os.path.dirname(os.path.realpath(__file__))
election_data_csv = os.path.join(folder_path, "Resources", "election_data.csv")

with open(election_data_csv, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    candidates = set() # https://www.w3resource.com/python-exercises/sets/python-sets-exercise-1.php, referenced for declaring empty set
    results = {}
    total_ballots = 0

    for row in csvreader:
        
        candidate = str(row[2])
        total_ballots += 1

        candidates.add(candidate)

        if candidate in results:
            vote_count = results[candidate][0] + 1 # https://www.geeksforgeeks.org/python-accessing-items-in-lists-within-dictionary/, referenced for accesing items in list in dictionary
            results[candidate][0] = vote_count
        else:
            results[candidate] = [1]
    
    for votes in results:
        
        candidate_votes = results[votes][0]
        vote_percentage = round((candidate_votes / total_ballots) * 100, 3)
        results[votes] += [vote_percentage] # https://www.geeksforgeeks.org/appending-to-list-in-python-dictionary/, referenced for appending to list in dictionary
        
    print("Election Results")
    print("---------------------")
    print(f"Total Votes: {total_ballots}")
    print("---------------------")
    for name in candidates:
        print(f"{name}: {results[name][1]}% ({results[name][0]})")
    winner = max(zip(results.values(), results.keys()))[1] # https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/#, referenced for code for max() function
    print("---------------------")
    print(f"Winner: {winner}")

output_file = os.path.join(folder_path, "analysis", "polls_summary.txt")

with open(output_file, "w") as datafile: # https://www.pythontutorial.net/python-basics/python-write-text-file/, referenced for how to write to txt file
    datafile.write("Election Results")
    datafile.write("\n")
    datafile.write("---------------------")
    datafile.write("\n")
    datafile.write(f"Total Votes: {total_ballots}")
    datafile.write("\n")
    datafile.write("---------------------")
    datafile.write("\n") 
    for names in candidates:
        datafile.write(f"{names}: {results[names][1]}% ({results[names][0]})")
        datafile.write("\n")
    datafile.write("---------------------")
    datafile.write("\n")
    datafile.write(f"Winner: {winner}")



