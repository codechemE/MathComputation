import numpy as np


def three_by_three_method(Ca0, Cc0, Cd0, k1, k2, tau):
    x0 = (1 + k1 * tau)
    x1 = 0
    x2 = 0
    x3 = -1 * k1 * tau
    x4 = 1 + k2 * tau
    x5 = 0
    x6 = 0
    x7 = -1 * k2 * tau
    x8 = 1

    a = np.array([[x0, x1, x2],
                  [x3, x4, x5],
                  [x6, x7, x8]])
    b = [Ca0, Cc0, Cd0]
    return np.linalg.solve(a, b)


sol = three_by_three_method(2.2, 0, 0, 2.3 / 60, 4.5 / 60, 2.5 * 60)
print(f'Ca equals {sol[0]} mol / L')
print(f'Cc equals {sol[1]} mol / L')
print(f'Cd equals {sol[2]} mol / L')

