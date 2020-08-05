import numpy as np

# This program demonstrates a matrix operation with numpy

A = np.array([  [3, 6, 7], 
                [5, -3, 0]])

B = np.array([  [1, 1],
                [2, 1],
                [3, -3]])

result = A.dot(B)

print(result)
