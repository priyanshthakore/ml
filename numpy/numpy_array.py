#!/usr/bin/python3

# creating numpy array from list 

import numpy as np 

my_list = [1,2,3]
arr = np.array(my_list)
print(arr)
print(type(arr))

## 2D array 

my_mat = [[1,2,3],[4,5,6],[7,8,9]]
new_arr = np.array(my_mat)
print(new_arr)
print(type(new_arr))

## creating array using numpy itself by built in arange function

new_arr_1 = np.arange(0,10)
print(new_arr_1)

# with step size

new_arr_2 = np.arange(0,10,2) ## here 2 is the step size we want between the numbers
print(new_arr_2)
print(type(new_arr_2))

# zeros 
print(np.zeros(3))
print(np.zeros((2,3)))

# ones
print(np.ones(3))
print(np.ones((2,3)))

# linspace
print(np.linspace(0,5,100)) ## here 100 is the number of points you want between the range of 0-5

# identity matrix
print(np.eye(4))

## This will give uniform distribution of values ranging from 0 - 1
#  1D random
print(np.random.rand(5))

# 2D random 
print(np.random.rand(5,5))

## normal distribution 1D
print(np.random.randn(4))

# normal distribution 2D
print(np.random.randn(4,4))

# getting a random number between range of number
print(np.random.randint(0,60))

# getting a random numbers between range of number (inclusive of low end and exclusive of high end)
print(np.random.randint(0,60,10))

## reshaping a numpy array
nuarray = np.arange(25)
print(nuarray)

reshaped = nuarray.reshape(5,5) # make sure this is same as 1D array 
print(reshaped)

# max value of array
print(nuarray.max())

# min value of array
print(nuarray.min())

# to know the index value 
print(nuarray.argmax())

# to know the min value 
print(nuarray.argmin())

# to know the shape of vector
print(nuarray.shape)

# to reshape and printing the shape of vector
new_reshape = nuarray.reshape(5,5)
print(new_reshape)
print(new_reshape.shape)

# printing the datatype of array
print(nuarray.dtype)
