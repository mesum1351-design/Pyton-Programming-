import pandas as pd

# Ek dummy DataFrame banate hain
data = {
    'Name': ['Ali', 'Zahra', 'Saqib', 'Mesum'],
    'Gender': ['Male', 'Female', 'Male', 'Male'],
    'Salary': [95000, 130000, 110000, 150000]
}
df = pd.DataFrame(data)

print("Original Data:")
print(df)
#one df filter true and false and another df only True
fd = df[df['Gender'] == 'Male']
fd = fd[fd['Salary'] > 120000]
print(fd)