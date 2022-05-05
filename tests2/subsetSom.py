def selectSum(T, A):
    n = len(A)
    F = [[False for _ in range(T + 1)] for _ in range(n)]
    # v1
    # for t in range(T + 1):
    #     F[0][t] = False
    #     if A[0] == T:
    #         F[0][t] = True
    # for t in range(T + 1):
    #     for i in range(n):
    #         F[i][t] = F[i - 1][t]
    #         if A[i] < t:
    #             F[i][t] = F[i - 1][t] | F[i - 1][t - A[i]]
    #         elif A[i] == t:
    #             F[i][t] = True
    # v2
    for i in range(n):
        F[i][0] = True
    F[0][A[0]] = True
    for t in range(T + 1):
        for i in range(1, n):
            F[i][t] = F[i - 1][t]
            if A[i] <= t:
                F[i][t] = F[i - 1][t] | F[i - 1][t - A[i]]
    # for i in range(n):
    #     print(F[i])
    return F[n - 1][T]


if __name__ == '__main__':
    A = [0, 7, 3, 5, 6]
    T = 8
    print(selectSum(T, A))
