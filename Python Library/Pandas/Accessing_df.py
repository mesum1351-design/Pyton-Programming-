
import pandas as pd

df = pd.DataFrame ({"Name": ['Ali','Hassan','Haseeb'],
                  "Age" : [16,13,15],
                  "marks" : [67,75,87]})

print(df)
print(df["Name"])
print(df["Name"][2])
print(df["Age"][1])

print(df.loc[2])
# Check the condition
result = df["Age"] > 15
print(result)
# Print the sepacfic one
search = df[df["Age"] > 15]
print(search)

