import pandas as pd

pd.read_csv('example')

df = pd.read_csv('example')
# print(df)
# df.to_csv('My_output')
df.to_csv('My_output',index=False)
# print(pd.read_csv('My_output'))

## install pip3 install xlrd 
## reading from excel files
# print(pd.read_excel('Excel_Sample.xlsx',sheet_name='Sheet1'))

## writing from excel files
df.to_excel('Excel_Sample2.xlsx',sheet_name='NewSheet')
data = pd.read_html('https://www.fdic.gov/bank/individual/part335/')
print(type(data))
print(data)
print(data[0])

## reading from sql

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
df.to_sql('my_table',engine)
sqldf = pd.read_sql('my_table',con=engine)
print(sqldf)