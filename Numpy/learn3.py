import numpy as np

"""You can create a new array by combining existing arrays. This you can do in two ways:

Either combine the arrays vertically (i.e. along the rows) using the vstack() method, thereby increasing the number of rows in the resulting array
Or combine the arrays in a horizontal fashion (i.e. along the columns) using the hstack(), thereby increasing the number of columns in the resultant array

Another interesting way to combine arrays is using the dstack() method. It combines array elements index by index and stacks them along the depth axis:"""

#Better way to do it is using numpy.stack

a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
b = np.flip(a,axis=0)

#stacking using the stack along prefered axis
print(np.stack([a,b], axis = 3).shape) #giving axis stacks along that dimension. increasing the dimension

"""Concatenating the arrays means to merge the arrays along the desired axis
if concatenate along rows means to add by rows means axis = 0 for 2d array to 
concatenate along the rows the no. of columns has to be same. Concatenating array
doesn't increase dimension
The number of that increase along which axis the concatenation is done
ex, 2,3,3 con... 2,3,3 will give 2,6,3 along axis=1"""

print(np.concatenate((a,b), axis=2).shape)
"""append adds only at end of an array, if axis is not specified the array is flattenn
before appending"""

print(np.append(a,b, axis=0).shape)