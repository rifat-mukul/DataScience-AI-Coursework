import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'London', 'Sydney']
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print()
print("==================================")
df2 = df.loc[1,"Name"]
print(df2)
print("==================================")
df3 = df["Name"]
print(df3)
print("==================================")
