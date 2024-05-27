import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr1 = arr.reshape(4,3)

print(newarr1)
print("==========================")
newarr2 = arr.reshape(2,3,2)
print(newarr2)
print("============================")
print(arr.reshape(2, 4).base)
print("============================")
