import numpy as np
import pandas as pd
from numpy.random import randn

# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
heir_index = list(zip(outside,inside))
heir_index = pd.MultiIndex.from_tuples(heir_index)
df = pd.DataFrame(randn(6,2),heir_index,['A','B'])
print(df)
print(df.loc['G1'])
print(df.loc['G1'].loc[1])  
print(df.index.names)
df.index.names = ['Groups','Num']
print(df.index.names)
print(df.loc['G2'].loc[2]['B'])
print(df.xs(1,level='Num'))