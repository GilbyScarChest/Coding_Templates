#pies1 = {1:'Pecan', 2:'Apple Crisp', 3:'Bean', 4:'Banoffee', 5:'Black Bun', 6:'Blueberry', 7:'Buko', 8:'Burek', 9:'Tamale', 10:'Steak'}

response = "y"

number_of_pies_ordered = 0

pies = ['Pecan', 'Apple Crisp', 'Bean', 'Banoffee', 'Black Bun', 'Blueberry', 'Buko','Burek', 'Tamale', 'Steak']

pies_counter = list(range(len(pies)))

for i in range(len(pies_counter)):
	pies_counter[i] = 0

while response == "y":

	

	print("--------------------------------------" + '\n' + "Welcome to The House Of Pies! Here are our pies:" + "\n" + "\n" + "(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee,  (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek,  (9) Tamale, (10) Steak" + "\n" + "--------------------------------------")

	
	pie_number = int(input("What Pie Would You Like To Order? Please Enter The Number "))

	print(f"Great! We will get that {pies[pie_number - 1]} pie for you!")

	pies_counter[pie_number -1] += 1
	number_of_pies_ordered += 1

	response = input("Would You Like To Make Another Order? y or n: ")

print(f"You Have Ordered {number_of_pies_ordered} Pies!")

for pie in enumerate(pies):
	print(pies_counter[pie])
