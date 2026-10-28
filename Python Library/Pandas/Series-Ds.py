#  Series Data Structure 1-Dimensional
# In series we add index name for manupulation
import pandas as pd
print(pd.__version__)
s= pd.Series([1,2,3,4],
             index = ['first','second','third','fourth'],
             name = 'name')
print(s)
print(s.index)
print(s.values)
print(s.dtypes)

#Data Access:
print(s['first'])
print(s['first': 'second'])  # values and index
print(s.first)     # only values
print(s.first,s.second)
print(s.array)

#Missing data Handling
import numpy as np
s = pd.Series([1,np.nan,3,4],
              index = ['first','second','third','fourth'],)
print(s)
s.second= 2   # when the value is known
print(s)

#Automatic Data Alignment
term1 = pd.Series([40, 45,50], index=['Ali', 'Zahra','Haseeb'])
term2 = pd.Series([50, 42, 38], index=['Ali', 'Zahra', 'Saqib'])
# Add
total = term1 + term2

print("Total Marks:")
print(total)

# Series from Dicitionary
import pandas as pd

# Series from Python Dictionary
data1 = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
print(data1)

obj = pd.Series(data1)
# Result check karein
print(obj)
  # override the index
state = ["california","Texas","Islamabad","Ohio"]
obj2 = pd.Series(data1, index=state)

print(obj2)