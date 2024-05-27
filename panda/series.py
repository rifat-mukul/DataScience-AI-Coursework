import pandas as pd

a = [1,2,3,4]

myvar = pd.Series(a)

print(myvar)
print(f"2nd data is {myvar[2]}")
print("==========================")

myvar2 = pd.Series(a, index=["x", "y","z","k"])
print(myvar2)

print("==========================")
color = {"day1":420, "day2": 360, "day3": 370}
myvar3 = pd.Series(color)
print(myvar3)
print("==========================")
myvar4 = pd.Series(color, index=["day1", "day2"])
print(myvar4)
print("==========================")