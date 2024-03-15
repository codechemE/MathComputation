import numpy as np
from numpy import linalg

a = np.array([[0, 2, 1],
              [1, 1, 2],
              [2, 1, 1]])
b = np.array([4, 6, 7])
sol = np.linalg.solve(a, b)
print(sol)

c = np.array([[1, -1, 1, 3], [2, 1, 8, 18], [4, 2, -3, -2]])


def RowSwap(A, k, z):
    n = A.shape[1]

    B = np.copy(A).astype('float64')

    for j in range(n):
        temp = B[k][j]
        B[k][j] = B[z][j]
        B[z][j] = temp

    return B


def RowScale(A, k, scale):
    n = A.shape[1]

    A = np.copy(A).astype('float64')

    for j in range(n):
        B[k][j] *= scale
    return A


def RowAdd(A, k, z, scale):
    n = A.shape[1]

    A = np.copy(A).astype('float64')

    for j in range(n):
        A[z][j] += A[k][j] * scale

    return A

# print(c)
# print(RowSwap(a, 0, 2))
# print(c)
# print(RowScale(a, 2, .5))


a_b = np.array([[0, 2, 1, 4],
                [1, 1, 2, 6],
                [2, 1, 1, 7]])

# step_1 = RowScale(a_b, 2, -1)
step_1 = RowAdd(a_b, 2, 1, -1)
step_2 = RowAdd(step_1, 2, 1, .5)


print(step_2)
# step 1 = scale row 1 by -2

# step_1 = RowScale(a_b, 0, -2)
# print(step_1)
# row 2 = row 2 + row 1
# step_2 = RowAdd(step_1, 0, 1, 1)
# print(step_2)

# swap row 1 with row 3
# step_3 = RowSwap(step_2, 0, 2)
# print(step_3)

# row 2 = row 2 - .5 * row 1

# step_4 = RowAdd(step_3, 0, 1, -.5)
# print(step_4)

# step_5 = RowScale(step_4, 2, -1)
# print(step_5)

# row 2 = row 2 + 1/4 row 3

# step_six = RowAdd(step_5, 2, 1, .25)

# print(step_six)
