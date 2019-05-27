import os
import csv

# video_title = row[0]
# video_rating = row[1]
# user_rating = row[5]

video = input("What video are you looking for? Please Enter Title: ")

csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")

found = True

with open(csvpath, newline='') as csvfile:
	
	csvreader = csv.reader(csvfile, delimiter=',')


	#csv_header = next(csvreader)
	#print(f"CSV Header: {csv_header}")


	for row in csvreader:
		if row[0] == video:
			print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])
			found = False
			break
		
			
	if found:
		print("Video Not Found")




# if video in netflix_ratings:
# 	#get the video
# 	print(f"{video_title} is rated {video_rating} with a rating of {int(user_rating)}")
# else:
# 	print("Video Not Found") 