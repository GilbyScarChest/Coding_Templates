names = []
for _ in range(10):
    name = input("Please enter the name of someone you know. ")
    names.append(name)
    if name == "q":
    	break

# @TODO: Use a list comprehension to create a list of lowercased names
lowercased = [name.lower() for name in names]

# @TODO: Use a list comprehension to create a list of titlecased names
# https://www.tutorialspoint.com/python/string_title.htm
titlecased = [name.upper() for name in names]

invitations = [
    f"Dear {name}, please come to the wedding this Saturday!" for name in titlecased]

for invitation in invitations:
    print(invitation)
