import math

# C = [(1, 1), (3, 2), (2, 5), (0, 3), (5, 10), (7, -2)]
# C = [(1, 1), (2, 1), (3, 18), (6, 1)]
C = [(1, 0), (2, 0), (5, 3)]
n = len(C)


def d(miasto_x, miasto_y):
    return math.sqrt((miasto_x[0] - miasto_y[0]) ** 2 + (miasto_x[1] - miasto_y[1]) ** 2)


D = [[d(C[i], C[j]) for i in range(n)] for j in range(n)]
F = [[math.inf for i in range(n)] for j in range(n)]


def tspf(i, j, D, F, C):
    if F[i][j] != math.inf:
        return F[i][j]
    if i == 0 and j == 1:
        return D[i][j]
    if i == j - 1:
        best = math.inf
        for k in range(j - 1):
            best = min(best, tspf(k, j - 1, D, F, C) + D[k][j])
        F[j - 1][j] = best
    else:
        F[i][j] = tspf(i, j - 1, D, F, C) + D[j - 1][j]

    return F[i][j]


tspf(n - 2, n - 1, D, F, C)
print(F[n - 2][n - 1])
print(F)
