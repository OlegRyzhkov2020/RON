import os
import csv

# Path to collect data from the Resources folder
pybank_csv = os.path.join("Resources", "budget_data.csv")

# Convert CSV file into a nested dictionary
with open(pybank_csv, 'r') as csvfile:
