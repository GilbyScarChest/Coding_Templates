# @TODO: Write a function that returns the arithmetic average for a list of numbers



def average(list_of_numbers):
	list_of_numbers = sum(list_of_numbers) / len(list_of_numbers)
	return list_of_numbers



# Test your function with the following:
print(average([1, 5, 9]))
print(average(range(11)))
