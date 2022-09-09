import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101) ## random seed is used to get same datapoint 
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)
print(df['W'])
print(type(df))
print(df[['W','Z']])
df['new'] = df['W'] + df['Y']

## dropping rows and columns in dataframe

print(df)
print(df.drop('new',axis=1))
print(df)
print(df.drop('new',axis=1,inplace=True))
print(df)
print(df.drop('E',axis=0))
print(df)


## checking the shape of the dataframe
print(df.shape)
print(df[['Z','X']])

## rows based on names 
print(df.loc['A'])

## rows based on index location
print(df.iloc[2])

## getting value from a particular location
print(df.loc['B','Y'])

print(df)
print(df.loc[['A','B'],['W','Y']])