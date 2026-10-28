#DataFrame
import pandas as pd

#dictionary data lists
data = {

    'Student': ['Ali', 'Zahra', 'Saqib', 'Mesum'],
    'Degree': ['BSAI', 'BSAI', 'BSIT', 'BSAI'],
    'Semester': [3, 3, 4, 3],
    'CGPA': [3.4, 3.8, 3.2, 3.9]
}
#  convert Dictionary to DataFrame
df = pd.DataFrame(data)
print(df)
print(df.describe())
print(df.dtypes)
print(df.shape)
print(df.columns)
print(df.index)
print(df.size)

#Data Access
print(df.Student,df.CGPA)
print(df.Degree)


df = pd.DataFrame(data=[
    ['NJ', 'Towaco', 'Square'],
    ['CA', 'San Francisco', 'Oval'],
    ['TX', 'Austin', 'Triangle'],
    ['MD', 'Baltimore', 'Square']
], columns=['State', 'City', 'Shape'])

print("Original DataFrame:")
print(df)

# Selection data by column
print("Data By Column")
print(df["State"])

# loc (Selection By Location)
print("By Location")
print(df.loc[0])    #
print(df.loc[1:3])  # Range

#iloc (Number/Position)
print(df.iloc[1:3])