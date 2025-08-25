import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],)
print(a[1, 3])
print(a.ndim)
print(a.shape) #len(a.shape) gives the dimension of an array
print(a.size)

b = np.zeros(3) #creating a array with zeroes, np.ones create array of ones
print(b)

c = np.arange(4)
print(f"using arrange : {c}")

d = np.arange(2,9,3)
print(d)

e = np.linspace(1, 13, 5, dtype=np.int64)
print(e)
