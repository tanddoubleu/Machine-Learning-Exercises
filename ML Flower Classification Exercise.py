# -*- coding: utf-8 -*-
"""Copy of Machine Learning Basics.ipynb

Automatically generated by Colaboratory.

## Pandas
Open source library providing easy to use data structures and analysis tools for Python
"""

import pandas as pd

from google.colab import files
uploaded = files.upload()

import io
iris = pd.read_csv(io.BytesIO(uploaded['Copy of iris.csv']))

"""**Series** is the datastructure for a single column of a **DataFrame**"""

iris

iris.head()

iris.tail()

iris.shape

iris.info()

iris.describe()

# Selecting 1 column
iris['sepal_length']

type(iris['sepal_length'])

iris['sepal_length'].values

iris.sepal_length

# Selecting Columns
iris[['sepal_length','sepal_width']]

# Selecting Rows
iris[1:4]

# Filtering
setosa = iris[iris['species']=='setosa']; print(setosa)

setosa = setosa[['sepal_length', 'sepal_width']]; print(setosa)

"""## Matplotlib
A plotting library for Python. It has a module named **pyplot** which makes things easy for plotting by providing feature to control line styles, font properties, formatting axes etc.
"""

from matplotlib import pyplot as plt

x = list(range(1,21)); x

setosa.head()

y = setosa.sepal_length[1:21]; y

plt.plot(x, y)
plt.show()

plt.boxplot(y)
plt.show()

y.describe()

x = setosa.sepal_width
y = setosa.sepal_length

plt.scatter(x, y)

plt.title('Setosa')
plt.xlabel('sepal length')
plt.ylabel('sepal width')

plt.show()

"""## Linear Regression with sklearn
Scikit-learn (sklearn) provides various supervised and unsupervised learning algorithms with a consistent interface in Python<br><br>
### Objective below is to find the value of **a** (gradient) and **b** (intercept) in **y = ax + b**
"""

from sklearn.linear_model import LinearRegression

# initilaise the model
regression_model = LinearRegression()

x = setosa.sepal_width.values
y = setosa.sepal_length.values

x

x = setosa.sepal_width.values.reshape(-1,1)
y = setosa.sepal_length.values.reshape(-1,1)

x

# Fit the data(train the model)
regression_model.fit(x, y)

a = regression_model.coef_; a

b = regression_model.intercept_; b

y_predicted = regression_model.predict(x); y_predicted

plt.scatter(x, y)

plt.plot(x, y_predicted, color='r')

plt.title('Setosa')
plt.xlabel('sepal length')
plt.ylabel('sepal width')

plt.show()

"""**R²** score or the *coefficient of determination* explains how much the total variance of the dependent variable can be reduced by using the least square regression."""

plt.close()

from sklearn.metrics import r2_score

r2_score(y, y_predicted)

"""## Classification with sklearn"""

! pip install seaborn

# plotting directly from iris dataframe
import seaborn as sns

sns.FacetGrid(iris, hue="species", size=5) \
   .map(plt.scatter, "sepal_length", "sepal_width") \
   .add_legend()

plt.show()

"""## Logistic Regression
It uses a logistic function (or sigmoid) to convert any real-valued input x into a predicted output value ŷ that take values between 0 and 1, as shown in the following figure:
![logistic regression image](lr.png)
Rounding ŷ to the nearest integer effectively classifies the input as belonging either to class 0 or 1.
"""

from sklearn.linear_model import LogisticRegression

# Create logistic regression instance
clf=LogisticRegression(random_state=0, multi_class='ovr', solver='liblinear')

x = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = iris.species

# Train model
model = clf.fit(x, y)

iris.tail()

x1 = [[6.7, 3.0, 5.2, 2.3]]

model.predict(x1)
