import numpy as np

arr1 = np.array([1,2,2,3])

arr2 = np.array([4,5,6,7])

arr = np.concatenate((arr1, arr2))

print(arr)

print("==================================")

arr3 = np.array([[1, 2], [3, 4]])

arr4 = np.array([[5, 6], [7, 8]])

arrx = np.concatenate((arr3, arr4), axis=1)

print(arrx)