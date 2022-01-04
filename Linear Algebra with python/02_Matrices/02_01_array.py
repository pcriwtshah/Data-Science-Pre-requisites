import numpy as np
import random
#create an array from 5 to 15
arr1 = np.arange(5, 15)
print(arr1)

arr2  =np.linspace(5,100,10)
print(arr2)
arr3 = np.log10(arr2)
print(arr3)

#Let's createa an array of numbers with 2 rows and 4 columns
A = [[1, 2, 3, 4], 
        [5, 6, 7, 8]]

#An array with 3 rows and 3 columns
B = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

#Find the shape of an array using numpy
a = np.shape(A)
b = np.shape(B)

print(f"The shape of A is {a} and the shape of B is {b}")

#Use len() function with matrix
print(f"{len(A)} \t {A[0]} \t {A[1]}")
'''
So, we see that len(A) gives number of rows;
 A[0] gives all elements of row 1 and
A[1] gives all elements of row 2'''
'''
Let's us define a function that returns the shape of A and B'''
def shape(A):
    n_row = len(A) #here len(A) will give you number of rows or number of elements in a column
    n_column = len(A[0]) if A else 0 #A[0] is the first row, A[1] is the second row
    return n_row, n_column

print(shape(A))
print(shape(B))
'''
# Generate a matrix
#not working now
def make_matrix(row, column):
    x = np.array[]
    for i in range(row):
        for j in range(column):
            x[i][j] = random.randint(0, 9)
            x.append(x[i][j])
    return x

print(make_matrix(3, 3))
'''

