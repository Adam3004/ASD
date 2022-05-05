def lcs(A, B):
    n = len(A)
    F = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        if B[0] == A[i]:
            F[i][0] = 1
    for j in range(n):
        if B[j] == A[0]:
            F[0][j] = 1

    for i in range(1, n):
        for j in range(1, n):
            if A[i] == B[j]:
                F[i][j] = F[i - 1][j - 1] + 1
            else:
                F[i][j] = max(F[i][j - 1], F[i - 1][j])
    # for i in range(n):
    #     print(F[i])
    return F[n - 1][n - 1]


if __name__ == '__main__':
    A = [1, 5, 2, 5, 3]
    B = [2, 7, 5, 4, 3]
    print(lcs(A, B))
