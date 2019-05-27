import os
import csv

# Path to collect data from the Resources folder




# Define the function and have it accept the 'wrestlerData' as its sole parameter

# Find the total number of matches wrestled
# Total matches can be found by adding wins, losses, and draws together


# Find the percentage of matches won
# Win percent can be found by dividing the the total wins by the total matches and multiplying by 100


# Find the percentage of matches lost
# Loss percent can be found by dividing the total losses by the total matches and multiplying by 100


# Find the percentage of matches drawn



# Print out the wrestler's name and their percentage stats

# Read in the CSV file
with open(wrestlingCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    nameToCheck = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'getPercentages()' function
        if(nameToCheck == row[0]):
            getPercentages(row)
