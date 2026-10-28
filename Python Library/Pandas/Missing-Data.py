# Original Data With Missing Values
#  dropna()   Fillna()
import pandas as pd
import numpy as np

#DataFrame having  missing values (np.nan)
dt = {'a': [1, np.nan, 3], 'b': [10, np.nan, 2], 'c': [0, 5, 2]}
df = pd.DataFrame(dt)

print("Original Data (Missing values ke sath):")
print(df)

#dropna() (Delete Missing Data)
print("After Deleting Null Rows")
df1 = pd.DataFrame(df.dropna(axis =0))  # Delete Row
print(df1)
print("After Deleting Null column")
df2 = pd.DataFrame(df.dropna(axis =1))  # Delete Column
print(df2)

# fillna()  (Fill Missing Value)
print("After Deleting  Fill Values")
df3 = pd.DataFrame(df.fillna(100))
print(df3)

df['a'] = df['a'].fillna(df['a'].mean())
df['b'] = df['b'].fillna(df['b'].mean())
df['c'] = df['c'].fillna(df['c'].mean())
print("\n Fill with Mean of Column")
print(df)