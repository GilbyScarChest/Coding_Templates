# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Build Random Dataset for Regression
from sklearn.datasets import make_regression

X, y = make_regression(n_samples=20, n_features=1, random_state=0, noise=4, bias=100.0)



# Use sklearn's `train_test_split` to split the data into training and testing in this case: 80% Training, 20% Test
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.20, train_size=.80)


# Build LinearRegression model
from sklearn.linear_model import LinearRegression
model = LinearRegression()


#Fit the model to our data using the fit method
model.fit(X, y)


#We can view the coefficients and intercept of the line from the coef_ and intercept_ attributes. 
#Note that the _ suffix indicates that the attribute is available after model is fit to the data (trained).
print('Weight coefficients: ', model.coef_)
print('y-axis intercept: ', model.intercept_) 

#We can use our model to make predictions.
predictions = model.predict(X)

print(f"True output: {y[0]}")
print(f"Predicted output: {predictions[0]}")
print(f"Prediction Error: {predictions[0]-y[0]}") # Mean Square Error (MSE)

# Visualize the differences in a Dataframe
pd.DataFrame({"Predicted": predictions, "Actual": y, "Error": predictions - y})[["Predicted", "Actual", "Error"]]

# score the training data
model.score(X_train, y_train)

# score the test data
model.score(X_test, y_test)