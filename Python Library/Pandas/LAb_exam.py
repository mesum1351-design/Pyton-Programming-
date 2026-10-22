#Question 4
import pandas as pd

# Create a dictionary containing student data
data = {
    'Student Name': [
        'Leonard', 'Penny', 'Howard', 'Bernadette',
        'Sheldon', 'Raj', 'Amy'
    ],
    'Class': ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
    'Section': ['B', 'C', 'A', 'D', 'A', 'B', 'B'],
    'Percentage': [91.2, 63.5, 90.23, 92.7, 98.2, 88.1, 95.0]
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Display the complete table
print("Complete Student Table:")
print(df.to_string(index=False))

# i) Print only the students belonging to Section A
print("\nStudents belonging to Section A:")
section_A = df[df['Section'] == 'A']
print(section_A.to_string(index=False))

# ii) Calculate section-wise mean percentage
print("\nSection-wise Mean Percentage:")
mean_percentage = df.groupby('Section')['Percentage'].mean()
print(mean_percentage)
