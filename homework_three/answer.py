import numpy as np
from numpy import linalg

a = [[7, 18, 15,24],
     [3, 25, 10, 65],
     [55, 41, 55, 9],
     [35, 16, 20, 2]]
b = [80*15, 80*25, 80*40, 80*20]

sol = np.linalg.solve(a, b)
print(sol)

print(linalg.cond(a))
print(linalg.det(a))