import numpy as np


f = np.arange(0, 110, 10)
c = np.zeros(11)
c_hat = np.zeros(11)

for i in range(0, 11):
    c[i] = (5/9)*(f[i]-32)
    c_hat[i] = (f[i] - 30)/2
    print(f[i], c[i], c_hat[i])
