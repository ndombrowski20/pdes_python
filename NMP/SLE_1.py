# Linear Systems of Equations
from numpy import array, zeros
import numpy as np

paranoid = True
fancy = False

# gauss elimination method

a = [
    [0, 7, -1, 3, 1],
    [2, 3, 4, 1, 7],
    [6, 2, 0, 2, -1],
    [2, 1, 2, 0, 2],
    [3, 4, 1, -2, 1]
]
b = [5, 7, 2, 3, 4]


def gauss_elim(A, B):
    n = len(A)
    for k in range(n-1):
        if A[k][k] == 0:
            A[k], A[k+1] = A[k+1], A[k]
            B[k], B[k+1] = B[k+1], B[k]
        for i in range(k+1, n):
            if A[i][k] ==0:
                continue
            factor = (A[k][k]) / (A[i][k])
            B[i] = B[k] - factor*B[i]
            for j in range(k, n):
                A[i][j] = A[k][j] - factor*A[i][j]
    x = zeros(n, float)
    x[n-1] = B[n-1] / A[n-1][n-1]
    for m in range(n-2, -1, -1):
        terms = 0
        for l in range(m+1, n):
            terms += A[m][l]*x[l]

        x[m] = (B[m] - terms)/A[m][m]

    return x


# print(gauss_elim(a, b))

# Jacobi's Method

c = array([[4, 1, 2, -1],
           [3, 6, -1, 2],
           [2, -1, 5, -3],
           [4, 1, -3, -8]], float)
d = array([2, -1, 3, 2], float)

guess_x = np.full(len(d), 1.0, float)


def jacobi_elim(A, B, x):
    n = len(B)
    x_new = np.empty(n, float)

    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += A[i][j] * x[j]
        x_new[i] = -1/A[i][i] * (s - B[i])

    if abs(x - x_new).any() > .0001:
        return jacobi_elim(A, B, x_new)
    else:
        return x


q = jacobi_elim(c, d, guess_x)
print(q)


