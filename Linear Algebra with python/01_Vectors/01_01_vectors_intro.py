'''
Vectors have magnitude and a direction. In 2D coordinate plane, 
vectors are represented by two numbers. In 3D coordinate place, 
it requires 3 numbers. Similarly, in n- dimensinal space, it 
requires n numbers. 
Vectors are added (or substracted) elementwise to form a new vectors.
Vectors are multiplied by a scalar( simply a number) to form a new vector.
We can use numpy package to work with vectors but for now we will create 
our own functions to work with vectors.
'''
''' Create a 3-dimensional vectors'''
name = ['Tom', 'Dick', 'Harry']
height = [65, 70, 63] #inches
weight = [160, 175, 180] #lbs
age = [35, 40, 45] #years

for i in range(3):
    print(f'{name[i]} is {age[i]} years old, {height[i]} inches tall and weigh {weight[i]} lbs')

vector = [name, height, weight, age]
print(vector)

#To add two vectors
def vector_add(v , w):
    '''Defining a function to add two vectors; requires two vectora as arguments'''
    assert len(v) == len(w)
    x = []
    for i in range(len(v)):
        x.append(v[i] + w[i])
        i = i + 1
    return x
exam_1 = [75, 78, 89, 90, 95, 90]
exam_2 = [85, 86, 85, 93, 98, 100]
Total_Score = vector_add(exam_1, exam_2)
print(Total_Score)

def vector_subtract(v , w):
    '''Defining a function to subtract two vectors; requires two vectora as arguments'''
    x = []
    assert len(v) == len(w)
    for i in range(len(v)):
        x.append(v[i] - w[i])
        i = i + 1
    return x

print(vector_subtract(exam_1, exam_2))

def scalar_product(v, k):
    '''Defining a function to multiply a vector by scalar; requires a vector and a scalar'''
    x = []
    for i in range(len(v)):
        x.append(k*v[i])
        i = i + 1
    return x

print(scalar_product(exam_1, 2))

def dot_product(v, w):
    '''Defining a function to multiply two vectors; requires two vectors'''
    assert len(v) == len(w)
    x = []
    for i in range(len(v)):
        x.append(v[i]*w[i])
        i = i+1
    dot_sum = sum(x) 
    return dot_sum

import math
def modulus(v):
    '''Defining a function to find the magnitude or modulus of a vector; requires 1 vector'''
    x = []
    for i in range(len(v)):
        x.append(v[i]*v[i])
        i = i+1
    magnitude = math.sqrt(sum(x))
    return magnitude
print(modulus(exam_1))

def cross_product(v, w):
    pass #This will be done later once we know about matrices and determinant

'''
Differentiation and Integration of vectors
Gradient, Divergence, Curl
Line, SUrface and Volume Integrals 
will be done if needed
'''