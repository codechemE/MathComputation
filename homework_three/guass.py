import numpy as np


def guass_elimination(a, b):
    def RowScale(A, k, scale):
        z = A.shape[1]

        A = np.copy(A).astype('float64')

        for j in range(z):
            A[k][j] *= scale
        return A

    n = len(b)
    m = n - 1
    i = 0
    j = i - 1
    x = np.zeros(n)
