import pandas as pd

#DataFrame
data = {
    'Name': ['Ali', 'Zahra', 'Saqib'],
    'Marks': [85, 92, 78]
}
df = pd.DataFrame(data)

# column 'ID'
df['ID'] = ['AS1', 'AS2', 'AS3']

print("Original Data (0, 1, 2 index ke sath):")
print(df)

# 'ID'new Index
df_with_new_index = df.set_index('ID')

print("\nNaya Index Set Karne Ke Baad:")
print(df_with_new_index)

# Reset
# Wapas purani halat mein lana
df_reset = df_with_new_index.reset_index()

print("\nIndex Reset Karne Ke Baad:")
print(df_reset)