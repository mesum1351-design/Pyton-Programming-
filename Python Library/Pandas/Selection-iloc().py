# iloc() integer based indexing
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(11,4),
                  columns = ["A","B","C","D"])
print(df)
print(df.iloc[0,:])
# Integer slicing
print (df.iloc[:4])
print (df.iloc[1:5, 2:4])

# Slicing through list of values
print (df.iloc[[1, 3, 5], [1, 3]])
print (df.iloc[1:3, :])
print (df.iloc[:,1:3])


#method iloc (summary)
print(df.iloc[0])# First row of a data frame
#print(df.iloc[]) #(i+1)th row
print(df.iloc[-1]) # Last row

print(df.iloc[:, 0]) # First column
print(df.iloc[:, -1]) # Last column

print(df.iloc[0:7])#First 7 rows
print(df.iloc[:, 0:2])#First 2 columns
print(df.iloc[1:3, 0:2]) #Second through third rows and first 2 columns
print(df.iloc[[0,5], [1,3]]) #1st and 6th rows and 2nd and 4th columns