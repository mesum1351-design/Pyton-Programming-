import pandas as pd
import numpy as np

# Aapka Data
data = {
    'Student': ['Ali', 'Zahra', 'Saqib', 'Mesum'],
    'Subject': ['Python', 'C++', 'Python', 'AI'],
    'Marks': [85, np.nan, 78, 95]
}
df = pd.DataFrame(data)
print(df)
df = df.fillna(value=0)
print(df)
df = df.sort_values(by = 'Marks', ascending = False)
print(df)