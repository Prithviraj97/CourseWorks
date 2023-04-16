'''
Name: Prithvi Raj Singh
Assignment 3: Linear Regression problem. 
Drawing a line of best fit.
**Note: Please use the attached .csv file (OneVarBPdata.csv) for the program to produce desired output. 
This produces the 2d plot of the given data.
The data given by Dr. Maida was slightly reformatted for the program to read all the rows and columns of the data. 
'''


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_frame = pd.read_csv("oneVarBPdata.csv")
data_frame.head()
data_frame.tail()
data_set = data_frame.values

X = data_set[:, 1:3:1]
print("\n",X)
y = data_set[:, 3]
print("\n",y)

x_transpose = np.transpose(X)
W = np.matmul(np.matmul(np.linalg.inv(np.matmul(x_transpose,X)), x_transpose), y)
print("The optimal weight is:\n", W)

x1 = np.linspace(20, 80, 100)
y1 = W[1]*x1 + W[0]
ages = data_set[:, 2]
sbp = y

plt.scatter(ages, sbp, color='red')
plt.xlabel('Age')
plt.ylabel('SBP')

plt.plot(x1, y1)
plt.show()
