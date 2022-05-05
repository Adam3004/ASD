import random


def printer(F, B):
    n = len(F)
    for i in range(n - 1, 0, -1):
        if F[i][B] != F[i - 1][B]:
            b2 = B
            while b2 > 0 and F[i - 1][b2] == F[i - 1][b2 - 1]:
                b2 -= 1
            B = b2
            print(i + 1)
    if F[0][B] > 0:
        print(1)


def f(W, P, n, B):
    F = [[0 for _ in range(B + 1)] for _ in range(n)]
    for b in range(W[0], B + 1):
        F[0][b] = P[0]
    for b in range(B + 1):
        for i in range(1, n):
            F[i][b] = F[i - 1][b]
            if b - W[i] >= 0:
                F[i][b] = max(F[i][b], F[i - 1][b - W[i]] + P[i])
    # for i in range(n):
    #     print(F[i])
    printer(F, B)
    return F[n - 1][B]


if __name__ == '__main__':
    n = 5
    r = 10
    W = [random.randint(0, r) for _ in range(n)]
    P = [random.randint(0, r) for _ in range(n)]
    # W, P = [5, 10, 0, 7, 1], [9, 5, 2, 5, 1]
    print(W, P)
    print(f'wynik: {f(W, P, n, 10)}')
