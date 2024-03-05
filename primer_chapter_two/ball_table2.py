import numpy as np

vo = 1
g = 9.81
n = 11
t = np.linspace(0, 2*vo/g, n)
y = np.zeros(11)

for i in range(0,len(t)):
    y[i] = vo*t[i] - 0.5*g*t[i]**2

z = zip(t,y)

print(list(z))
