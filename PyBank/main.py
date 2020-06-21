import os
import csv
from datetime import datetime

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
    """Converts string data to data and integer types,
    adds column with the changes of "Profit/Losses".
    Args:
        data_list (list): data list for conversion.
    Returns:
        conversion_list: (updated list after conversion)
    """

    date_list = [datetime.strptime(data_str[0], '%b-%Y') for data_str in data_list]
    profit_list = [int(data_str[1]) for data_str in data_list]
    conversion_list = dict(zip(date_list, profit_list))

    return conversion_list

#Call function load_data for PyBank
pybank_data = load_data("Resources", "budget_data.csv")

border = '#' * 50
# print('{}\n{}'.format(border, pybank_data))

pybank_conversion = conversion_data(pybank_data)
print('{}\n{}'.format(border, pybank_conversion))
