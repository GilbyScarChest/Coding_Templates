# Import Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

# initiate browser
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:\\Users\\tdgso\\Desktop\\chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

browser = init_browser()

# URL of page to be scraped
url = 'https://webscraping_url.com'

# initiate web scrape 
browser.visit(url)

# allow the site to compile html
time.sleep(2)

# define html
html = browser.html

# parse the html using BeautifulSoup
soup = bs(html, "html.parser")

# print out the html from the scraped site
print(soup.body.prettify()) 

# finding target text
Scraped_comments = []
for item in soup.body.find_all("div", class_="js-tweet-text-container"):
    Scraped_comments.append(item.p.text)
    print(item.p.text)

# Print it out nicely
for i in Scraped_comments:
    print(f"Comment: {i}")

print(f"Total Comments: {len(Scraped_comments)}")

### See "Soup" for more scraping options ###