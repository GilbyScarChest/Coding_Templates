import random

mylist = ["rock", "paper", "scissors"]

computer1 = random.choice(mylist)

user_input = input("Rock, Paper, Scissors! Please input r, p, or r: ")


user_input
print(computer1)

if computer1 == "rock":
	if user_input == "r":
		print("Tie! Try again!")
		user_input
	elif user_input == "p":
		print("You Win!")
	elif user_input == "s":
		print("You Lose!")
	else:
		print("Please make a valid entry")
		user_input

elif computer1 == "paper":
	if user_input == "r":
		print("You Lose!")
		user_input
	elif user_input == "p":
		print("Tie! Try again!")
	elif user_input == "s":
		print("You Win!")
	else:
		print("Please make a valid entry")
		user_input

elif computer1 == "scissors":
	if user_input == "r":
		print("You Win!")
		user_input
	elif user_input == "p":
		print("You Lose!")
	elif user_input == "s":
		print("Tie! Try again!")
	else:
		print("Please make a valid entry")
		user_input

