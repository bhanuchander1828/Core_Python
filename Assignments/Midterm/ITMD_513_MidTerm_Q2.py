'''
ITMD 513 : MidTerm- Q2 - Bhanu kureti
Summary : This program will create array and will perform some basic array operations
'''

import numpy as np

''' Create array '''
array = np.arange(1,16)

''' Reshape the array to 3 by 5'''
array = np.reshape(array, (3, 5))
print("The 3 by 5 array is :\n", array)

''' Second row of the array '''
x = array[2:3, :]
print("The second row is :\n", x)

''' fourth column of the array '''
x = array[:, 4:5]
print("The Fourth column is :\n", x)

''' 0 and 1 rows of the array '''
x = array[:2, :]
print("The rows 0 and 1 are :\n", x)

''' element in the 1 row and 4 column of the array '''
x = array[1:2,[4]]
print("The element in the 1 row and 4 column is  :\n", x)

''' Elements of rows 1 and 2 which are in 0 ,2 and 4 column of the array '''
x = array[1:3,[0,2,4]]
print(" The elements in 1 and 2 rows which are in columns 0, 2 and 4 are :\n", x)


