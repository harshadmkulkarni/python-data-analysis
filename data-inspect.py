# Data analysis & inspection with Python Pandas

import pandas as pd
# df for DataFrame
df = pd.read_csv('intel.csv')
#print df to make sure it works
#print(df)

#check df datatype which is <class 'pandas.core.frame.DataFrame'>
# print(type(df))

#check df shape
#print(df.shape)

#view column names
#print(df.columns)

#inspect first rows of data auto set to 5
#print(df.head)
#inspect first 10 rows of data
print(df.head(10))


#inspect last 5 rows of data auto set to 5
#print(df.tail)
#inspect last 10 rows of data
#print(df.tail(10))

#inspect Open and Close Columns first 5 entries of column-data
#print(df[['Open','Close']].head())

#describe the dataset
#print (df.describe())
