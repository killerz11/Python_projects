import numpy as np

a = np.array([[1,8,5,12], [4,88,44,33]])
b = np.array([3,5,7,23])

# print(a.shape[0])#no. of rows
# print(a.shape[1])#no. of columns
# print(b.shape)

b_reshaped = b.reshape(2,2)
print(f"{b_reshaped}      {b_reshaped.shape}")

print(np.concatenate((b_reshaped,a.transpose()), axis = 0))

"""The arrays being concatenated must have the same shape, except along the axis you are concatenating on.
For example, if you are concatenating along axis=0 (vertically stacking), the number of columns in each array must be the same.
If you are concatenating along axis=1 (horizontally stacking), the number of rows in each array must be the same."""

"""to make the array 1d we can use flatten or ravel method, flatten gives copy
of original array while ravel make changes in the original array"""

print(a.flatten())
c = a.ravel()
c[1] = 2

print(a) #change made in c got reflected in a

"""Taking transpose of an array using the transpose, row becomes columns and vice versa"""

print(a.transpose())
c = np.expand_dims(a,axis=0)
print(c)
"""axis=0. expands the array in row, axis =1 expands the array in column"""

"""squeeze removes the axis along which there is only one entry, cannot squeeze the axis along which
size is not equal to one """

print(np.squeeze(c, axis = 0))
