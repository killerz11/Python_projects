"""Broadcasting in numpy array"""
import numpy as np

a = np.arange(10,20,2)
print(a)
b = np.array([[2],[2]])
print(b)

#multiplying a scalar by a array
print(a*2)

#adding two diff array
"""Here the 2d array is formed, adding 2 to each column"""
print(a+b)

"""we can do -, *, +, /, **, %"""

"""doing mean, median and standard deviation"""

c = np.random.rand(3,3)
print(c)
print(np.mean(c))
print(np.median(c))
print(np.std(c))

"""finding the min and max, axis=1 along row,axis=0 along column, 
also can find the index of min/max by using the argmin/argmax"""
print(np.min(c, axis=1))

print(np.argmax(c, axis=0))