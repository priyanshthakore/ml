import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
print(df)

## drop data na
print(df.dropna())
print(df.dropna(axis=1))

print(df.dropna(thresh=2))

## filling na 
print(df.fillna(value = 'FILL VALUE'))
print(df['A'].fillna(value=df['A'].mean()))