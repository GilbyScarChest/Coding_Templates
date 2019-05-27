# Dependencies
import os
from bs4 import BeautifulSoup as bs
import requests

# 1) HTML Source
html_string = """
<html>
	<head>
		<title>
			A Simple HTML Document
		</title>
	</head>
	<body>
		<p>This is a very simple HTML document</p>
		<p>It only has two paragraphs</p>
	</body>
</html>
"""
#
#
#
#
# OR
#
#
#
# 2) Read HTML from file
filepath = os.path.join("..", "Resources", "template.html")
with open(filepath) as file:
    html = file.read()
#
#
#
#
# OR
#
#
#
# 3) URL of page to be scraped
url = 'https://newjersey.craigslist.org/search/sss?sort=rel&query=guitar'


# 1) Create a Beautiful Soup object
soup = bs(html_string, 'html.parser')
#
#
# OR
#
#
# 2) Create a Beautiful Soup object
soup = bs(html, 'html.parser')
#
#
# OR
#
#
# 3) Retrieve page with the requests module
response = requests.get(url)
# Create BeautifulSoup object; parse with 'html.parser'
soup = bs(response.text, 'html.parser')



# Print formatted version of the soup
print(soup.prettify())

# Extract the title of the HTML document
soup.title

# Extract the text of the title
soup.title.text

# Clean up the text
soup.title.text.strip()

# Text of the first paragraph
soup.body.p.text

# Extract all paragraph elements
soup.body.find_all('p')

# Extract paragraph by index
soup.body.find_all('p')[0]

# The text of the first paragraph
soup.body.find('p').text

# More Advanced...
# Print only the headlines
headline_display = []
for item in soup.find_all('td'):
    headline_display.append(item.text.strip())
    
for item in headline_display:
    print(item)
    print('--------------------')

# Cleaning out the Null values
for item in soup.findAll('td'):
    if item.a != None:
        print(item.a.text)
        

# Scraping results from website
# results are returned as an iterable list
results = soup.find_all('li', class_="result-row")
for result in results:
    if result.span.text[0] == '$':
        print(result.span.text)

# Finding all headlines
for item in soup.find_all('div', class_="content_title"):
    print(item.a.text)

# Loop through returned results
for result in results:
    # Error handling
    try:
        # Identify and return title of listing
        title = result.find('a', class_="result-title").text
        # Identify and return price of listing
        price = result.a.span.text
        # Identify and return link to listing
        link = result.a['href']

        # Print results only if title, price, and link are available
        if (title and price and link):
            print('-------------')
            print(title)
            print(price)
            print(link)
    except AttributeError as e:
        print(e)