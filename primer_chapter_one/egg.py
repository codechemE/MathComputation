import numpy as np


def cookEgg(M, rho, c, K, To, Tw, Ty):
    return M ** (2 / 3) * c * rho ** (1 / 3) / (K * np.pi ** 2 * (4 * np.pi / 3) ** (2 / 3)) * np.log(
        .76 * (To - Tw) / (Ty - Tw))


print(cookEgg(67,1.038, 3.7, 5.4*10**-3, 20, 100, 70))
