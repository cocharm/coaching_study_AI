import numpy as np

arr1 = np.array([[5,7], [9,11]], float)
arr2 = np.array([[2,4], [6,8]], float)

concat_1 = np.concatenate((arr1, arr2), axis=0) 
concat_2 = np.concatenate((arr1, arr2), axis=1)

print(concat_1, concat_2, sep = '\n')