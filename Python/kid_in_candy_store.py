candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]
allowance = 5

candyCart = []

for candy in candyList:
    print("[" + str(candyList.index(candy)) + "]" + candy)


for i in range(allowance):
	user_input = input("Which candy would you like to bring home? ")
	candyCart.append(candyList[int(user_input)])

print("You bought...")
for candy in candyCart:
	print(candy)
