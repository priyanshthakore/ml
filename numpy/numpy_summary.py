#!/usr/bin/python3

import numpy as np

# create an array of 10 zeros
print(np.zeros(10))

# create an array of 10 ones
print(np.ones(10))

# create an array of 10 5s
print(np.ones(10)*5)

# create an array integers 10 to 50 
print(np.arange(10,51))

# create an arra of all the even integers from 10 to 50
print(np.arange(10,51,2))

# create a 3x3 matrix with values ranging from 0 to 8
print(np.arange(9).reshape(3,3))

# create a 3x3 matrix
print(np.eye(3))

# use numpy to generate random number between 0 to 1
print(np.random.rand(1))

# use numpy to create a array of 25 random number sampled
print(np.random.randn(25))

# creating matrix
print(np.arange(1,101).reshape(10,10)/100)

print(np.linspace(0.01,1,100).reshape(10,10))
print(np.linspace(0,1,20))

## indexing 
mat = np.arange(1,26).reshape(5,5)
print(mat)
print(mat[2:,1:])

# grabbing 20
print(mat[3,4])

print(mat[:3,1:2])
print(mat[4:,])
print(mat[3:5,])

# summing all the values
print(mat.sum())

# std deviation
print(mat.std())

# sum of all the columns
print(mat.sum(axis=0))



































