import os
import csv
import math
# Path to collect data from the Resources folder
csvpath = os.path.join('..', 'CSV', 'Resources', 'wrestlerCSV.csv')



# Define the function and have it accept the 'wrestlerData' as its sole parameter
def getPercentages(wrestlerData):

# Find the total number of matches wrestled
# Total matches can be found by adding wins, losses, and draws together

	total = (int(wrestlerData[1]) + int(wrestlerData[2]) + int(wrestlerData[3]))


# Find the percentage of matches won
# Win percent can be found by dividing the the total wins by the total matches and multiplying by 100

	win_perc = math.ceil(int(wrestlerData[1]) / total * 100)

# Find the percentage of matches lost
# Loss percent can be found by dividing the total losses by the total matches and multiplying by 100

	loss_perc = math.ceil(int(wrestlerData[2]) / total * 100)

# Find the percentage of matches drawn

	draw_perc = math.ceil(int(wrestlerData[3]) / total * 100)

# Print out the wrestler's name and their percentage stats

	print(f"{wrestlerData[0]}: The win percentage is: {win_perc}. The loss percentage is: {loss_perc}. The draw percentage is: {draw_perc}")

# Read in the CSV file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    nameToCheck = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'getPercentages()' function
        if(nameToCheck == row[0]):
            getPercentages(row)
