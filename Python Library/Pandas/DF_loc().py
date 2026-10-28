#
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns =
['A', 'B', 'C', 'D'])
#select all rows for a specific column
#df.loc[index , Column]
print (df.loc[:,'A'])
print (df.loc[:,['A','C']])
print (df.loc[['a','b','f','h'],['A','C']])
print (df.loc[['a'],['A']])

# Select range of rows for all column
print(df.loc['a':'h'])

# for getting values with a boolean array
print (df.loc['a']>0)