import numpy as np


m = 0
s = 2
x = 1

innerPart = (x - m) / s
innerPart = -.5 * (innerPart ** 2)

f = 1/(np.sqrt(2*np.pi)*s) * np.exp(innerPart)

print(f)
