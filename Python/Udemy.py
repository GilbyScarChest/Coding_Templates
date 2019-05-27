import os
import csv


title = []
price = []
subscriber_count = []
number_of_reviews = []
course_length = []


csvpath = os.path.join("..", "Resources", "web_starter.csv")

with open(csvpath, newline='') as csvfile:
	
	csvreader = csv.reader(csvfile, delimiter=',')

	print(csvreader)

	csv_header = next(csvreader)
	#print(f"CSV Header: {csv_header}")


	for row in csvreader:
		
		title.append(row[1])
		price.append(row[4])
		subscriber_count.append(row[5])
		number_of_reviews.append(row[6])
		course_length.append(row[-2])

		

# Specify the file to write to
output_path = os.path.join("..", "output", "Udemy.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Title', 'Price', 'Subscriber Count', 'Number Of Reviews', 'Course Length'])

    # Write the second row
    csvwriter.writerows(zip(title, price, subscriber_count, number_of_reviews, course_length))

