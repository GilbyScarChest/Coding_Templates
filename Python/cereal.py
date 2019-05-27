import os
import csv

csvpath = os.path.join("..", "Resources", "cereal.csv")

with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')


	csv_header = next(csvreader, None)
	print(f"CSV Header: {csv_header}")


	for row in csvreader:
		if float(row[7]) >= 5:
			print(row)

