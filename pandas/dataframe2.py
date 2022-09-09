#!/usr/bin/python3

## conditional selection in pandas

import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)
booldf = df > 0
# print(df[booldf])
# print(df[df>0])

## checking conditional in rows or columns
# print(df[df['W']>0])
# print(df[df['Z']<0])

resultdf = df[df['W']>0]
# print(resultdf['X'])

# print(df[df['W']>0]['X'])
# print(df[df['W']>0][['Y','X']])

boolser = df['W']>0
result = df[boolser]
mycols = ['Y','X']
# print(result[mycols])

## using multiple conditions
print(df[(df['W']>0) & (df['Y']>1)])
print(df[(df['W']>0) | (df['Y']>1)])

print(df.reset_index())

newind = 'CA NY WY OR CO'.split()
print(newind)
df['States'] = newind
print(df)

print(df.set_index('States',inplace=True))
print(df)