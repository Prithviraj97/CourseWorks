# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 22:12:25 2021
Name: Prithvi Raj Singh
Program: Projecting a point to a line.
Description: This is an another way i tried to do the program in Spyder IDE. This basically does the same thing and have 
x-axis and y-axis labeled as asked by Dr. Maida.
This can be best used for evaluation of the assignment. 
@author: PrithviCS
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero


x = (1.5,2)
u = (.866,.5)
print('This is the value of x\n',x)
print('This is the value of u=(1, pi/6)\n', u)
x_cord=1.5
y_cord =2.0
a_coord = 1.99
b_coord = 1.15

'''
K = np.tan(np.pi/6)
T = np.linspace(-4,4,100)
H = K*T + 1.15 '''
point1 = [.866,0.5]
point2 = [1.99,1.15]
point3 = [0,0]
point4 = [-3,-3]
x_vals = [point3[0],point1[0]] #This all need to go and a st line with 30 degrees to x-axis needs to made.
y_vals = [point3[1],point1[1]]

V = np.transpose(x)
alpha = np.dot(V,u)
print('The value of alpha is:\n', alpha)

alphamu = np.dot(alpha,u)
y =alphamu
print("This is the value of alpha_u = y\n",y)
#plt.xlabel('x1')
#plt.ylabel('x2')
plt.axhline(y=0, color='black')
plt.axvline(x=0, color='black')

x1 = np.linspace(-10,10,100)
y = np.tan(np.radians(30))*x1

#fig = plt.figure()
#ax = SubplotZero(fig, 111)

xyRange = np.round_([(max(abs(x[0]),abs(u[0]))),(max(abs(x[1]),abs(u[1])))])
sqrange = max(xyRange)+1
plt.xlim([-sqrange, sqrange])
plt.ylim([-sqrange, sqrange])
plt.arrow(0,0,sqrange-0.2,0,length_includes_head=False,head_length=0.2,head_width=0.2,color='black')
plt.arrow(0,0,0,sqrange-0.2,length_includes_head=False,head_length=0.2,head_width=0.2,color='black')
plt.grid()
plt.scatter(x_cord, y_cord, color='red', label='x')
plt.scatter(a_coord,b_coord, color='orange', label='alpha_u')
plt.scatter(.866,.5, color='blue', label='u')

#ax.annotate('x', xy=(x_cord,y_cord), xycoords='data', xytext=(0.75,0.95), textcoords='axes fraction',
            #arrowprops=dict(facecolor='black', shrink=0.03))
#plt.plot(x_vals,y_vals)
plt.annotate(text='x', xy=(x_cord,y_cord), xytext=(1.6,2.0))
plt.annotate(text='alpha_u', xy=(a_coord,b_coord), xytext=(2.0,1.3))
plt.annotate(text='u', xy=(a_coord,b_coord), xytext=(0.9,0.7))
plt.gca().set_box_aspect(1)
params = {'mathtext.default':'regular'}
plt.twinx().set_ylabel('$x_{1}$')
plt.twiny().set_xlabel('$x_{2}$')
plt.plot(x1,y)
#plt.plot(x_vals,y_vals)
plt.arrow(x=0, y=0, dx=0.866, dy=0.5, width=0.05)
plt.xlim([-sqrange,sqrange])
plt.ylim([-sqrange,sqrange])
plt.legend()
plt.gca().set_box_aspect(1)

#plt.plot(x, u, alphamu)



