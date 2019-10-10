# Dependencies
from sklearn import tree
import pandas as pd
import os

#Load the data
df = pd.read_csv(os.path.join("..", "Resources", "diabetes.csv"))

# define your "target"(y-axis --data points)
target = df["Outcome"]
target_names = ["negative", "positive"]

# define your "data"(X-axis' --features)
data = df.drop("Outcome", axis=1)
feature_names = data.columns

# Split the data using train_test_split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=42)

# Create a Decision Tree Classifier
clf = tree.DecisionTreeClassifier()

# Fit the classifier to the data
clf.fit(X_train, y_train)

# Score the algorithm
#training
clf.score(X_train, y_train)
#test
clf.score(X_test, y_test)


### RANDOM FOREST ###
# Create, fit, and score a Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier #trying to predict the Class. 
                                                    #RandomForestRegressor tries to pick the actual number. 
                                                    #It's more difficult.

rf = RandomForestClassifier(n_estimators=200)
rf = rf.fit(X_train, y_train)
rf.score(X_test, y_test)