import numpy as np


f = np.arange(0, 110, 10)
c = np.zeros(11)
c_approx = np.zeros(11)

for i in range(0, 11):
    c[i] = (5/9)*(f[i]-32)
    c_approx[i] = (f[i] - 30)/2
    #  print(f[i], c[i], c_approx[i])

conversion = [f, c, c_approx]

#  print(conversion)

q = [r ** 2 for r in [10 ** i for i in range(5)]]
print(q)