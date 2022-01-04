import numpy as np
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#Generate null matric
array = np.zeros((2,3))
print(array)

#Generate unit or identity matric
array = np.ones((2,3))
print(array)

#Convert a list to an array for mathematical operations

list1 = [ 1, 2, 3, 4, 5, 6]
list2 = [2, 3, 4, 5, 6, 7]
array1 = np.array(list1)
array2 = np.array(list2)
print(array1)
print(array2)
#Now you can add elements of two arrays
addMatrix = np.add(array1,array2)
print(addMatrix)
a = array1 + array2
print(a)

#You cannot add elements of two lists
b = list1 + list2
print(type(list1))
print(b)

