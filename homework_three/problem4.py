import numpy as np
from numpy import linalg

a = np.array([[0, 8, -2, 5, 6], [1, 3, 0, 1, 7], [6, 0, 0, 2, -1],
              [2, 1, 2, 0, 2], [8, 4, 1, -2, 1]])
b = np.array([5, 20, 2, 3, 4])

sol = np.linalg.solve(a, b)
print(sol)
