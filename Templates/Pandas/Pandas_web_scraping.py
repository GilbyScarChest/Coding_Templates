# Dependancies
import pandas as pd

# We can use the read_html function in Pandas 
# to automatically scrape any tabular data from a page.

# URL of website to scrape
url = 'https://en.wikipedia.org/wiki/List_of_capitals_in_the_United_States'

# Read HTML
tables = pd.read_html(url)
tables

# What we get in return is a list of dataframes for any tabular data that Pandas found.
# We can slice off any of those dataframes that we want using normal indexing.

# Select first table as df
df = tables[0]

# Establish columns
df.columns = ['State', 'Abr.', 'State-hood Rank', 'Capital', 
              'Capital Since', 'Area (sq-mi)', 'Municipal Population', 'Metropolitan', 
              'Metropolitan Population', 'Population Rank', 'Notes']
# Display
df.head()

# Cleanup of extra rows
df = df.iloc[2:]
df.head()

# Set the index to the State column
df.set_index('State', inplace=True)
df.head()

# That way we can display all info about a row
df.loc['Alabama']


# Pandas also had a to_html method that we can use to generate HTML tables from DataFrames.
html_table = df.to_html()
html_table

# You may have to strip unwanted newlines to clean up the table.
html_table.replace('\n', '')

# You can also save the table directly to a file.
df.to_html('table.html')