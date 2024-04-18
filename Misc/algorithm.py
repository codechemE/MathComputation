# Author: Jefim Naljotov


Ft0 = 1
fract_SO2 = .28
fract_air = .72
pressure_0 = 1485
R = 8.314
temperature_0 = 500

air_fract_O2 = .21
air_fract_N2 = .79

fa0 = fract_SO2*Ft0
fb0 = fract_air*air_fract_O2
fi = fract_air*air_fract_N2

theta_A = 1
theta_B = fb0/fa0
theta_I = fi/fa0

print(theta_B, theta_I)
a = 1
b = 1/2
c = 1

delta = a - b - 1
epsilon = fract_SO2*delta
print(epsilon)



