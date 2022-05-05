L = [5, 9999, 123123, 1251, 123312, 32, 132, 1, 0, 15, 19, 2456]


#
# def tupleCreator(tuple):
#     rest = tuple[1] % 10
#     next_num = tuple[1] // 10
#     return tuple[0], next_num, rest


def radixSort(L):
    n = len(L)
    L = [(L[i], 0, L[i]) for i in range(n)]
    zeros_counter = 0
    while zeros_counter < n:
        L = [(L[i][0], L[i][2] % 10, L[i][2] // 10) for i in range(n)]
        zeros_counter = 0
        for i in range(n):
            if L[i][1] == 0:
                zeros_counter += 1
        L = countingSort(L)
    L = [L[i][0] for i in range(n)]
    return L


def countingSort(L):
    n = len(L)
    B = [None for _ in range(n)]
    C = [0 for _ in range(10)]
    for i in range(n): C[L[i][1]] += 1
    for i in range(1, 10): C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        B[C[L[i][1]] - 1] = (L[i][0], L[i][1], L[i][2])
        C[L[i][1]] -= 1
    for i in range(n):
        L[i] = B[i]
    return L


print(radixSort(L))
