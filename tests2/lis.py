# longest consistent substring
import random

r = 15
n = 10
A = [random.randint(1, 15) for _ in range(n)]


def printer(A, P, maxi):
    if maxi == -1:
        return
    printer(A, P, P[maxi])
    print(A[maxi])


def lis(A):
    n = len(A)
    F = [1 for _ in range(n)]
    P = [-1 for _ in range(n)]
    maxi = 0
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
        if F[i] > F[maxi]:
            maxi = i
    print(f'Najdluzszy podciag ma {F[maxi]} wyrazow i sa to:')
    printer(A, P, maxi)


print(A)
lis(A)
