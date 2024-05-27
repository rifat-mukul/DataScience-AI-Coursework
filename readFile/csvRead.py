import pandas as pd

url ='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv'

print("========================================")
print("Without header")
df = pd.read_csv(url)
print(df)
print("========================================")
print("With Header")
df.columns = ["First Name", "Last Name", "Location", "City", "State", "Area COde"]
print(df)
print("========================================")
print("Single Column")
print(df["First Name"])
print("========================================")
print("Selecting Multiple Column")
print(df[["First Name", "State"]])
print("========================================")
# To select the first row
print(df.loc[0])
print("========================================")
# To select the 0th,1st and 2nd row of "First Name" column only
print(df.loc[[0,1,2], "First Name" ])
print("========================================")
# iloc() : iloc() is a indexed based selecting method which means that we have to pass integer index in the method to select specific row/column.
# To select the 0th,1st and 2nd row of "First Name" column only
print(df.iloc[[0,1,2], 0])
print("========================================")
print("========================================")
print("========================================")
print("========================================")
print("========================================")