# Dependencies
import pandas as pd

# Create DataFrame
new_df = pd.DataFrame({

	'column_1': ['value_1', 'value_2', 'value_3'],
	'column_2': ['value_1', 'value_2', 'value_3'],
	'column_3': ['value_1', 'value_2', 'value_3'],

	})

# Save path to data set in a variable
data_file = "Resources/dataSet.csv"

# Use Pandas to read data
data_file_pd = pd.read_csv(data_file)
# Show first 5 rows
data_file_pd.head()
# Show last 5 rows
data_file_pd.tail()

# Find how many columns and rows
data_file_pd.shape

# Display a statistical overview of the DataFrame
data_file_pd.describe()

# Reference a single column within a DataFrame
data_file_pd["Amount"].head()

# value counts
data_file_pd.Gender.value_counts()

# Reference multiple columns within a DataFrame
data_file_pd[["Amount", "Gender"]].head()

# The mean method averages the series
average = data_file_pd["Amount"].mean()
print(average)

# The sum method adds every entry in the series
total = data_file_pd["Amount"].sum()
print(total)

# The unique method shows every element of the series that appears only once
unique = data_file_pd["Last Name"].unique()
print(unique)

# Calculations can also be performed on Series and added into DataFrames as new columns
thousands_of_dollars = data_file_pd["Amount"]/1000
data_file_pd["Thousands of Dollars"] = thousands_of_dollars
data_file_pd.head()

# Using .rename(columns={}) in order to rename columns
renamed_df = organized_df.rename(columns={"Membership(Days)":"Membership in Days", "Weight":"Weight in Pounds"})
renamed_df.head()

# Export file as a CSV, without the Pandas index, but with the header
file_one_df.to_csv("Output/fileOne.csv", index=False)

# Drop all rows with missing information
df = df.dropna(how='any')

# Using GroupBy in order to separate the data into fields according to "state" values
grouped_usa_df = usa_ufo_df.groupby(['state'])

# Creating a Pivot Table from Pandas DataFrame
df.pivot(index="Column 1", columns="Name", values="Column 4")

