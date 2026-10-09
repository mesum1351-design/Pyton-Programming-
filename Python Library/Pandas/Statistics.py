import pandas as pd

df = pd.DataFrame({ "Items " : ['Apple','Orange','Banana'],
                   "Quantity" : [12,10,100],
                    "Price" : [1.0,2.0,0.5]
})
print(df)
# Adding new column
df["Total"] = df["Quantity"] * df["Price"]
# Sum
print(df.sum())
#Maximum
print(df["Total"].max())

#Minimum
print(df["Total"].min())

#MEAN
print(df["Total"].mean())

# Median
print(df["Total"].median())

# Standard Deviation
print(df["Total"].std())

#Variance
print(df["Total"].var())

#Quantile
print(df["Total"].quantile(0.25))

#Describe
print(df.describe())
