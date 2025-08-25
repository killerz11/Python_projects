import numpy as np
"""slicing the array means to get a particular values from the array by telling
the starting and ending points, also can mention step size"""

"""To get the particular part of an array we 1st specify the row(0:1) and then 
select the column(0:2)"""
a = np.array([[1,2,3,4],[5,6,7,8]])
print(a[:,1:2])

#Slicing in 3d array
"""Slicing in 3d array is same as 2d but you have to select the array from stac and it is the 
1st number, we can also use the negative slicing, -1 means selecting from ending"""

b = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
print(b[0:2,:,-1])
#reversing the array, use ::-1 at a axis you want to reverse
print(b[::-1,::-1,::-1])

#also can use flip(), to reverse
print(np.flip(b, axis=0)) #along z axis equivalent to ([::-1,:,:])

