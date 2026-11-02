import pandas as pd

#DataFrame
data = {
    'Student': ['Ali', 'Zahra', 'Saqib', 'Mesum'],
    'Marks': [75, 92, 60, 95]
}
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# agg() ka istemal karke ek hi waqt mein Min, Mean (Average), aur Max nikalna
# Note: Double brackets [['Marks']] lagana zaroori hai taake output DataFrame (Table) ki shakal mein aaye
summary = df[['Marks']].agg(['mean', 'std', 'min', 'max'])

print("\nAggregation ka Result:")
print(summary)

import pandas as pd

df = pd.DataFrame({'Marks': [85, 90, 78]})

# Single Bracket -> Output ek Series hoga
print(type(df['Marks']))
# Output: <class 'pandas.core.series.Series'>

# Double Bracket -> Output ek DataFrame (Table) hoga
print(type(df[['Marks']]))
# Output: <class 'pandas.core.frame.DataFrame'>