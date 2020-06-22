import os
import csv
import sys
from datetime import datetime

# Description of output messages
MSG_1 = "\nFinacial Analysis\n{}\nTotal Months: {}\nTotal: {}"
MSG_2 = "\nAverage Change: ${}"
MSG_3 = "Greatest Increase in Profits (${})  Date(YYYY-MM):{}-{}"
MSG_4 = "Greatest Decrease in Profits (${}) Date(YYYY-MM):{}-{}\n{}"

def load_data(path, file_name):
    """Load a data set.
    Args:
        path (str): The location of a CSV file
        file_name (str): The name of a CSV file.
    Returns:
        data_list: (list of rows from CSV file)
    """
    # Path to collect data
    data_csv = os.path.join(path, file_name)
    # Opening CSV file
    with open(data_csv, 'r') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=',')
        # Removing header
        next(data_reader, None)
        # Convert CSV file into a nested list
        data_list = []
        for row in data_reader:
            data_list.append(row)
    # Returning list with uploaded dataset
    return data_list

def conversion_data(data_list):
    """Converts string data to date and integer types,
    adds list element with the changes of "Profit/Losses".
    Args:
        data_list (list): The data list for conversion.
    Returns:
        conversion_dict:
            key - list (type date) with 1 element date
            values - list (type integer) with 2 elements (profit, change)
    """

    # Conversion string into data type
    date_list = [datetime.strptime(data_str[0], '%b-%Y') for data_str in data_list]
    # Conversion string into integer type
    profit_list = [int(data_str[1]) for data_str in data_list]
    # Merging 2 lists into a dictionary
    conversion_dict = dict(zip(date_list, profit_list))
    # Appending changes element to a value for each key of a dictionary
    changes_list = []
    for i in range(len(profit_list)):
        if i == 0 : changes_list.append(0)
        else:
            changes_list.append(profit_list[i] - profit_list[i-1])
        conversion_dict[date_list[i]] = [conversion_dict[date_list[i]], changes_list[i]]
    # Returning dictionary with conversed and added data
    return conversion_dict

def print_plus(print_list, output_file = "None"):
    """Printing data to the terminal.
    Args:
        data_list (tuple):              The data list for printing
        output_file (string, optional): The name of a txt file.
    """
    #Printing the analysis result to the terminal
    if output_file != "None":
        sys.stdout = open(output_file, "w")
    border = '#' * 63
    print(MSG_1.format(border, print_list[0], print_list[1]))
    print(MSG_2.format(print_list[2]))
    print(MSG_3.format(print_list[3], print_list[4].year, print_list[4].month))
    print(MSG_4.format(print_list[5], print_list[6].year, print_list[6].month, border))
    if output_file != "None":
        sys.stdout.close()

#Call function load_data for PyBank
pybank_data = load_data("Resources", "budget_data.csv")
#Call function conversion_data for PyBank uploaded data into paybank_data
pybank_conversion = conversion_data(pybank_data)

#Dictionary records analysis
total_profit = 0
total_change = 0
max_change = 0
min_change = 0
for key in pybank_conversion:
    total_profit += pybank_conversion[key][0]
    total_change += pybank_conversion[key][1]
    if pybank_conversion[key][1] > max_change:
        max_change = pybank_conversion[key][1]
        max_date = key
    if pybank_conversion[key][1] < min_change:
        min_change = pybank_conversion[key][1]
        min_date = key
total_months = len(pybank_conversion)
avg_change = format(total_change/total_months,'.2f')

#Creating tuple for output data
print_data = (total_months, format(total_profit, ',d'), avg_change, format(max_change,',d'), max_date, format(min_change,',d'), min_date)

#Call function to print summary to the terminal
print_plus(print_data)
#Call function to print summary to the text file
print_plus(print_data, 'summary_analysis.txt')
