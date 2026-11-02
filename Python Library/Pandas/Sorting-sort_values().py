
import pandas as pd
import numpy as np

data = {'Student': ['Ali', 'Zahra', 'Saqib'],
        'Marks': [75, 92, 85]}
df = pd.DataFrame(data)
print("before Sorting data")
print(df)
print("After Sorting data")
print("Ascending Order:")
print(df.sort_values(by = 'Marks'))
print("Decending order:")
print(df.sort_values(by = 'Marks', ascending = False))

