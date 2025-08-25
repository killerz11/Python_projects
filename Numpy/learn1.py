import numpy as np

a = np.array([[30,40,60,20],[40,30,44,20]])
# print(np.shape(a))

# print(len(a))

# print(np.random.rand(3,3))

# print(np.full((4,4), 1)) #fills the array with desired number

"""here we get the identity matrix, k=1, means 1 along the upper diagonal of main diagonal
#k=-1, means 1 in the lower diagonal"""
#print(np.eye(3,k=1, dtype=int))

"""here 1d array is given, start included, end excluded, step size specified """
#print(np.arange(1,11,2))
"""here start and stop is included,but here it is not step size but number of elements
to be given in the given range"""
#print(np.linspace(2,10,5, dtype=int))







