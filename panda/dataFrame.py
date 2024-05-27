import pandas as pd

data = {
    "color" : ["black", "blue","Gray"],
    "duration" : [120, 240, 249]
}

myvar = pd.DataFrame(data)

print(myvar)
print("=================================")
data2 = {
    "categories": [420,380,390],
    "duration": [50,40,45]
}

df = pd.DataFrame(data2)

print(df)
print("=================================")
print(df.loc[0])
print("=================================")
print(df.loc[[0,1]])
print("=================================")