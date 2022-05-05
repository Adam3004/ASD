A = [[1, 2, 3],
     [0, 4, 5],
     [11, 23, 43]]
B = [[5, 14, 13, 12],
     [11, 10, 9, 8],
     [7, 6, 15, 4],
     [3, 2, 1, 0]]

C = [[23, 24, 22, 21, 20],
     [19, 18, 13, 16, 15],
     [14, 17, 12, 11, 10],
     [9, 8, 7, 6, 5],
     [4, 3, 2, 1, 0]]
D = [[10, 12, 13, 16, 17, 11],
     [9, 8, 7, 6, 5, 4],
     [23, 24, 25, 27, 21, 29],
     [33, 34, 38, 32, 31, 39],
     [41, 42, 43, 44, 45, 46],
     [0, 1, 2, 3, 15, 18]]
E = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28],
     [29, 30, 31, 32, 33, 34, 35], [36, 37, 38, 39, 40, 41, 42], [43, 44, 45, 46, 47, 48, 49]]
'''
[5, 23, 11]
[0, 4, 43]
[2, 1, 3]


[15, 14, 13, 12]
[11, 10, 9, 8]
[7, 6, 5, 4]
[3, 2, 1, 0]


[24, 23, 22, 21, 20]
[19, 18, 17, 16, 15]
[14, 13, 12, 11, 10]
[ 9,  8,  7,  6,  5]
[ 4,  3,  2,  1,  0]
'''


def printer(L):
    for i in range(len(L)):
        print(L[i])


def findMaxMin(L):
    n = len(L)
    max = L[0][0]
    min = L[0][0]
    for i in range(n):
        for j in range(n):
            checking = L[i][j]
            if checking > max:
                max = checking
            elif checking < min:
                min = checking
    return min, max


def findMaxP(L):
    max = L[0][0]
    for i in range(1, len(L)):
        if L[i][i] > max:
            max += 1
    return max


def countSort(L):
    n = len(L)
    min, max = findMaxMin(L)
    Numbers = [0 for _ in range(max - min + 1)]
    for i in range(n):
        for j in range(n):
            Numbers[L[i][j] - min] += 1
    w = 0
    k = 0
    for i in range(len(Numbers) - 1, -1, -1):
        if Numbers[i] > 0:
            L[w][k] = min + i
            k += 1
            if k == n:
                k = 0
                w += 1
    if n % 2 == 0:
        # start = n * n // 2 - n / 2
        start = n // 2
        for i in range(n):
            if i < n // 2:
                L[i][i], L[(n // 2) - 1][start] = L[(n // 2) - 1][start], L[i][i]
                start += 1
                if start == n:
                    start = 0
            else:
                L[i][i], L[(n // 2)][start] = L[(n // 2)][start], L[i][i]
                start += 1
        max_p = findMaxP(L)
        for i in range(n):
            j = 0
            while j < i:
                checking = L[i][j]
                if checking > max_p:
                    L[i][j], L[n - i - 1][n - j - 1] = L[n - i - 1][n - j - 1], L[i][j]
                j += 1
    else:
        start = 0
        max_p = L[n // 2][0]
        for i in range((n // 2) + 1):
            L[i][i], L[n // 2][start] = L[n // 2][start], L[i][i]
            L[n - i - 1][n - i - 1], L[n // 2][n - start - 1] = L[n // 2][n - start - 1], L[n - i - 1][n - i - 1]
            L[n // 2][start], L[n // 2][n - start - 1] = L[n // 2][n - start - 1], L[n // 2][start]
            start += 1
        for i in range(n):
            j = 0
            while j < i:
                checking = L[i][j]
                if checking > max_p:
                    L[i][j], L[n - i - 1][n - j - 1] = L[n - i - 1][n - j - 1], L[i][j]
                j += 1

    return L


L = countSort(E)
printer(L)
