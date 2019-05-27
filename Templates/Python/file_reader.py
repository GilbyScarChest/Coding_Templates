path = "/Users/tdgsoundtracks/desktop/LearnPython/assignment1/my_first_text_file.txt"

with open(path, 'r') as handler:

	lines = handler.read()

	print(lines)