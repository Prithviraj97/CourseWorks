class myMatrix:

 #Matrix Constructor
 def __init__(self, m, n):

 # initialization condition
  if (m <= 0 or n <= 0 or m > 500000 or n > 500000):
   print("Error! Martix size cannot be less than 0 or more than 500000")
   return None


  else: 
   self.data = []
   
   for i in range(m):
    z=[]
    for j in range(n):
        z.append((i+1)*(j+1))
    self.data.append(z)
     

 def __mul__(self, other):
  if isinstance(other, (int, float)):
      result = myMatrix(m = len(self.data), n = len(self.data[0]))
      result.data = [[self.data[i][j] * other for j in range(len(self.data[0]))] for i in range(len(self.data))]
      return result.data
  elif isinstance(other,myMatrix):
   result = myMatrix(m = len(self.data), n = len(other.data[0]))
   for i in range(len(result.data)):
    for j in range(len(result.data[0])):
        result.data[i][j]=0
        for k in range(len(result.data)):
          result.data[i][j] += self.data[i][k] * other.data[k][j]
   return result.data

 def __pow__(self, other):
     if isinstance(other, (int, float)):
          result = myMatrix(m = len(self.data), n = len(self.data[0]))
          result.data = [[self.data[i][j] ** other for j in range(len(self.data[i]))] for i in range(len(self.data))]
          return result.data

 def __truediv__(self, other): 
  if (other == 0):
      return "Error: Divisor can't be zero"
   #divide by zero condition
  elif isinstance(other, (int, float)):
      result = myMatrix(m = len(self.data), n = len(self.data[0]))
      result.data = [[self.data[i][j] / other for j in range(len(self.data[i]))] for i in range(len(self.data))]
      return result.data

 def sum(self): 
     total = 0
     for i in range(len(self.data)):
         for j in range(len(self.data[0])):
              total +=(self.data[i][j])
     return print(total)

import time
initial= time.time()
a=myMatrix(5,5)
a*a
print("%s" %(time.time() - initial))

#for 10x10 matrix
initial= time.time()
c=myMatrix(10,10)
c*c
print("%s" %(time.time() - initial))

#for 20x20 matrix
initial = time.time()
d=myMatrix(20,20)
d*d
print("%s" %(time.time() - initial))

#for 50x50 matrix
initial = time.time()
e=myMatrix(50, 50)
e*e
print("%s" %(time.time() - initial))

#for 100x100 matrix
initial = time.time()
f=myMatrix(100,100)
f*f
print("%s" %(time.time() - initial))

#for 250x250 matrix
intial = time.time()
b=myMatrix(250,250)
b*b
print("%s" %(time.time() - initial))










