import csv
import time
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from numba import jit

X = []
y = []

def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader) # skipping column names
        for row in csvFileReader:
            date_str = str(row[0])
            pattern = '%Y-%m-%d'
            epoch = int(time.mktime(time.strptime(date_str, pattern)))
            X.append(epoch)
            y.append(float(row[4]))

    return


get_data('SENSEX2.csv')
X = np.reshape(X, (len(X), 1)) # converting to matrix of n X 1
y = np.reshape(y, (len(y), 1))

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/6, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_X = sc_X.fit(X_train)
X_train = sc_X.transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)


scorer = regressor.score(X_test,y_test) *100
# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Date vs Price (Training set)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()



# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Date vs Price (Test set)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()