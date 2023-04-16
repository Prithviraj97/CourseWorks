'''
Name: Prithvi Raj Singh
Assignment 3: Linear Regression problem Part2. 
Printing the optimal weight of 3 variable datas using formula7 .
**Note: Please use the attached .csv file (twoVarBPdata.csv) for the program to produce desired output. 
This produces the 3d plot of the given data which is optional and not optimized.
The data given by Dr. Maida was slightly reformatted for the program to read all the rows and columns of the data 
'''



import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits import mplot3d

data_frame = pd.read_csv("twoVarBPdata.csv", skiprows=None)
data_frame.head()
data_frame.tail()
data_set2 = data_frame.values
data_set2 = np.insert(data_set2, 1, 1, axis=1)

x = data_set2[0:17, 1:4]
print("\nThe value of x is the collection of matrix of Age and Weight. It is used for optimal value calculation")
print(x)
y = data_set2[:, 4]
print("\n This will print out y, the matrix value of SBP")
print(y)
x_transpose = np.transpose(x)
W = np.matmul(np.matmul(np.linalg.inv(np.matmul(x_transpose,x)), x_transpose), y)
print("The optimal weight is:\n", W)


'''
The below code for the plotting is optional for this part of assignment3. Dr. Maida asked us to just print out the optimal
weight for this. 
'''
fig = plt.figure()
ax= plt.axes(projection='3d')
zline = np.linspace(30,120,100)
xline = np.linspace(20,80,100)
yline = W[1]*xline + W[0]+W[2]*zline
ax.plot3D(xline, yline, zline, 'red')
ax.plot(xline,yline,zline, 'red')