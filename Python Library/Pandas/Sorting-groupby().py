
import pandas as pd

# Animals ki Max Speed ka data
df = pd.DataFrame({
    'Animal': ['Falcon', 'Falcon', 'Parrot', 'Parrot'],
    'Max Speed': [380.0, 370.0, 24.0, 26.0]
})

# Count the values
count = df.groupby(['Animal']).count()
mean  = df.groupby(['Animal']).mean()
print("Group By ka Result (Count):")
print(count)
print(mean)