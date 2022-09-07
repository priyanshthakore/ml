#!/usr/bin/python3

import numpy as np

arr = np.arange(0,11)
print(arr[8])

# slice notation
print(arr[1:5])

# everything in array before value
print(arr[:6])

# everything in array after value
print(arr[5:])

# broadcasting numbers 
arr[0:5]=100
print(arr)

## slicing of array
arr = np.arange(0,11)
slice_of_arr = arr[0:6]
# print(slice_of_arr)
slice_of_arr[:]= 99
print(slice_of_arr)
print(arr)

# copying array
arr_copy = arr.copy()
print(arr)
arr_copy[:]=100
print(arr_copy)
print(arr)


### creating 2D array
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)
print(arr_2d[1][1])
print(arr_2d[1,2])

### 
print(arr_2d[:2,1:])

print(arr_2d[1,:])

### conditional comparison

print(arr)
bool_arr = arr > 5
print(bool_arr)


####
new_2d_array = np.arange(50).reshape(5,10)
print(new_2d_array)
print(new_2d_array[1:3,3:5])























