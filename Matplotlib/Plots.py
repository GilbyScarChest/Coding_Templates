# Import Numpy for calculations and matplotlib for charting
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Creates a list from 0 to 5 with each step being 0.1 higher than the last
x_axis = np.arange(0, 5, 0.1)
x_axis

# Creates an exponential series of values which we can then chart
e_x = [np.exp(x) for x in x_axis]
e_x


# Give our graph axis labels
plt.xlabel("Time With MatPlotLib")
plt.ylabel("How Cool MatPlotLib Seems")

# Create a graph based upon the two lists we have created
plt.plot(x_axis, e_x)
plt.show()

# Adds a legend and sets its location to the lower right
plt.legend(loc="lower right")

# Bar Charts
# Tell matplotlib that we will be making a bar chart
# Users is our y axis and x_axis is, of course, our x axis
# We apply align="edge" to ensure our bars line up with our tick marks
plt.bar(x_axis, users, color='r', alpha=0.5, align="center")
# Tell matplotlib where we would like to place each of our x axis headers
tick_locations = list(x_axis)
plt.xticks(tick_locations, ["Java", "C++", "Python", "Ruby", "Clojure"])


# Pie Charts
# Creates the pie chart based upon the values above
# Automatically finds the percentages of each part of the pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=140)
# Tells matplotlib that we want a pie chart with equal axes
plt.axis("equal")


# Scatter Plots
# Tells matplotlib that we want to make a scatter plot
# The size of each point on our plot is determined by their x value
plt.scatter(x_axis, data, marker="o", facecolors="red", edgecolors="black",
            s=x_axis, alpha=0.75)


# Box Plot
# Create box plot
arr = np.array([2.3, 10.2,11.2, 12.3, 14.5, 14.6, 15.0, 15.1, 19.0, 24.0])
plt.boxplot(arr, showmeans=True, vert=False)
plt.grid()
#Standard Deviation amount
STD = np.std(arr)
STD


# Sub Plots (Multiple Plots)
# Set data
x_axis = np.arange(0, 10, 1)
fake = [1, 2.5, 2.75, 4.25, 5.5, 6, 7.25, 8, 8.75, 9.8]
# Plot data
fig, ax = plt.subplots(nrows=2, ncols=2)

fig.suptitle("Fake Banana Data!", fontsize=16, fontweight="bold")

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

ax.set_xlabel("Fake Banana Ages (in days)")
ax.set_ylabel("Fake Banana Weights (in Hundres of Kilograms)")

ax.plot(x_axis, fake, linewidth=0, marker='o')
ax.plot(x_axis, fit, 'b--')

plt.show()


# Create Trend Line
# Set line
(slope, intercept, _, _, _) = linregress(x_axis, fake)
fit = slope * x_axis + intercept