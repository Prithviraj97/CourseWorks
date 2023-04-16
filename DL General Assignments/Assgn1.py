'''
Name: Prithvi Raj Singh
Program: Projecting a point to a line.
Description: This is an another way i tried to do the program in PyCharm IDE. This basically does the same thing but have 
no x-axis and y-axis labeled as asked by Dr. Maida. 
Use other python file (DLASgn2.py) for evalution. I think it will be better.
'''

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero
x = np.array((1.5,2))
u = np.array((.866,.5))
print(x)
print(u)

V = np.transpose(x)
alpha = np.dot(V, u)
alphamu= np.dot(alpha, u)

fig = plt.figure()
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)
for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)
for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>")
    ax.axis[direction].set_visible(True)
ax.axis["yzero"].invert_ticklabel_direction()
ax.set_yticks([-4,-3,-2,-1,1, 2,3,4])
ax.set_xticks([-4,-3,-2,-1,1,2,3,4])
params = {'mathtext.default':'regular'}
#ax.set_ylabel('$x_{1}$')
#ax.set_xlabel('$x_{2}$')
#plt.xlabel('X1')
x_coord = 1.5
y_coord = 2
x1 = np.linspace(-4.5,4.5,80)
m = np.tan(np.radians(30))*x1
#ax.plot(x_coord, y_coord)
plt.gca().set_box_aspect(1)
#plt.scatter(x_coord,y_coord)
plt.plot(x1, m)
plt.scatter(x_coord,y_coord, label='x')
plt.scatter(1.990934, 1.1495, label='alpha_u')
plt.scatter(0.866, 0.5, color='red', label='u')
#plt.annotate('x', (x_coord, y_coord))
ax.annotate('x', xy=(x_coord,y_coord), xycoords='data', xytext=(0.75,0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.03))

plt.grid()
plt.arrow(x=0,y=0,dx=0.866, dy=0.5, width = 0.07)
ax.legend(loc='upper left', frameon= True)
plt.show()