def exch(M, C):
    n = len(M)
    F = [[1000 for _ in range(C + 1)] for _ in range(n)]
    # for i in range(n):
    #     if C % M[i] == 0:
    #         F[i][0] = C // M[i]
    for i in range(n):
        F[i][0] = 0
    for j in range(int(C / M[0]) + 1):
        F[0][j * M[0]] = j
    for i in range(n):
        print(F[i])
    print(20 * "-")
    for i in range(1, n):
        for c in range(C + 1):
            F[i][c] = F[i - 1][c]
            if M[i] <= c:
                F[i][c] = min(F[i - 1][c], F[i][c - M[i]] + 1)
        for i in range(n):
            print(F[i])
        print(20 * "-")
    for i in range(n):
        print(F[i])
    return F[n - 1][C]


if __name__ == '__main__':
    M = [3, 7, 1, 5, 4]
    C = 12
    print(exch(M, C))
