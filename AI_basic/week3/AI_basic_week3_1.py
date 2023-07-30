import numpy as np

# 5x3 : 난수
arr1 = np.random.rand(5,3)

# 3x2 : 난수
arr2 = np.random.rand(3,2)

# 행열곱
dot = np.dot(arr1, arr2)

print(dot, dot.shape)