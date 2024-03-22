import numpy as np
from numpy import linalg

A = np.array([[0, 8, -2, 5, 6],
              [1, 3, 0, 1, 7],
              [6, 0, 0, 2, -1],
              [2, 1, 2, 0, 2],
              [8, 4, 1, -2, 1]], float)

b = np.array([5, 20, 2, 3, 4], float)

# specify the length of the loop
n = len(b)
# create solution vector x
x = np.zeros(n, float)

for k in range(0, n - 1):  # loop for pivot eq.
    if A[k, k] == 0:  # check if the diagonal element is 0
        for j in range(n):  # if so then for all the columns
            A[k, j], A[k + 1, j] = A[k + 1, j], A[k, j]  # swap the elements for the row below
        b[k], b[k + 1] = b[k + 1], b[k]  # swap vector b but outside the column loop
    for i in range(k + 1, n):  # loop for equations below pivot eq
        lam = A[i, k] / A[k, k]
        b[i] = b[i] - lam * b[k]
        # print("b vector",b[i])
        for j in range(k, n):
            A[i, j] = A[i, j] - lam * A[k, j]
        # print("A matrix",A[i,j])

# Stage 2 back substitution
x[n - 1] = b[n - 1] / A[n - 1, n - 1]
for i in range(n - 2, -1, -1):
    # print(i)
    terms = 0
    for j in range(i + 1, n):
        terms += A[i, j] * x[j]
    x[i] = (b[i] - terms) / A[i, i]
print(x)
