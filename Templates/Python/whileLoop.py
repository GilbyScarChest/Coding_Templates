run = "y"
last_number = 0

while run == "y":

	numbers = input("How many numbers do you want to print out? ")

	for i in range(last_number, last_number + int(numbers) + 1):
		print(i)
		last_number = last_number + int(numbers)

	run = input("Would you like to continue? y or n: ")

