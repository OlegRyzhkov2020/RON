import os
import csv
import sys

# Description of output messages
MSG_1 = "\nElection Results\n{}\nTotal Votes: {}\n{}\n"
MSG_2 = "Candidate {}: {}% Number of voters: {}"
MSG_3 = "\n{}\nWinner: {}\n{}\n"

def load_data(path, file_name):
    """Load a data set.
    Args:
        path (str): The location of a CSV file
        file_name (str): The name of a CSV file.
    Returns:
        data_dict: (dict of rows from CSV file)
    """
    data_csv = os.path.join(path, file_name)
    with open(data_csv, 'r') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=',')
        # Removing header
        next(data_reader, None)
        # Convert CSV file into a nested list
        data_list = []
        for row in data_reader:
            data_list.append(row)
    return data_list

def print_plus(print_list, candidate_dict, output_file = "None"):
    """Printing data to the terminal or text file
    Args:
        data_list   (tuple):            The total number of voters, name of the winner
        candidate_dict (dict):          The dictionary with candidate summary
        output_file (string, optional): The name of a txt file.
    """
    if output_file != "None":
        sys.stdout = open(output_file, "w")
    border = '#' * 51
    print(MSG_1.format(border, print_list[0], border))
    for key in candidate_dict:
        print(MSG_2.format(key, candidate_dict[key][1], candidate_dict[key][0]))
    print(MSG_3.format(border, print_list[1], border))
    if output_file != "None":
        sys.stdout.close()

#Call function load_data for PyBank
pypoll_data = load_data("Resources", "election_data.csv")
total_voters = format(len(pypoll_data),',d')
#Creating list of candidates
cand_name_list = [pypoll_data[0][2]]
for i in range(len(pypoll_data)):
    if pypoll_data[i][2] not in cand_name_list:
        cand_name_list.append(pypoll_data[i][2])
#Data Analysis
cand_values_list = []
cand_votes = 0
win_num = 0
for name in range(len(cand_name_list)):
    for i in range(len(pypoll_data)):
        if pypoll_data[i][2] == cand_name_list[name]:
            cand_votes += 1
    cand_votes_percent = round(cand_votes/len(pypoll_data)*100,1)
    cand_values_list.append([format(cand_votes, ',d'), format(cand_votes_percent,'.2f')])
    if cand_votes > win_num:
        win_num = cand_votes
        winner = cand_name_list[name]
    cand_votes = 0
#Conversion of two list into an output dictionary
cand_dict = dict(zip(cand_name_list, cand_values_list))
print_data = (total_voters, winner)

#Call function to print summary to the terminal
print_plus(print_data, cand_dict)
#Call function to print summary to the text file
print_plus(print_data, cand_dict, 'summary_analysis.txt')
