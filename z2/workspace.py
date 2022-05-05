import random
import time


def moving(L: list, l: int, r: int):
    x = L[r][0]
    i = l - 1
    k = i
    for j in range(l, r):
        if L[j][0] < x:
            i += 1
            k += 1
            L[k], L[j] = L[j], L[k]
            L[i], L[k] = L[k], L[i]
        elif L[j][0] == x:
            k += 1
            L[k], L[j] = L[j], L[k]

    L[k + 1], L[r] = L[r], L[k + 1]
    return i + 1, k + 1


# def sort_same_partitions(L: list, l: int, r: int):
#     anyChanges = True
#     while anyChanges:
#         anyChanges = False
#         for i in range(l, r):
#             if L[i][1] < L[i + 1][1]:
#                 L[i], L[i + 1] = L[i + 1], L[i]
#                 anyChanges = True

def sort_same_partitions(L: list, l: int, r: int):
    max_val = (L[r][1], r)
    for i in range(l, r, 2):
        checking_1 = L[i][1]
        checking_2 = L[i + 1][1]
        if checking_1 <= checking_2:
            if max_val[0] < checking_2:
                max_val = (checking_2, i + 1)
        else:
            if max_val[0] < checking_1:
                max_val = (checking_1, i)
    L[l], L[max_val[1]] = L[max_val[1]], L[l]


# def quickSort(L: list, l, r):
#     if l < r:
#         q, q2 = moving(L, l, r)
#         quickSort(L, l, q - 1)
#         sort_same_partitions(L, q, q2)
#         quickSort(L, q2 + 1, r)

def quickSort(L: list, l, r):
    while l < r:
        q, q2 = moving(L, l, r)
        quickSort(L, l, q - 1)
        sort_same_partitions(L, q, q2)
        l = q2 + 1


# to ok \/

def including(L, start):
    k = 0
    j = start + 1
    while j < len(L) and L[start][1] >= L[j][1]:
        j += 1
        k += 1
    next_move = j
    j += 1
    while j < len(L):
        if L[start][1] >= L[j][1]:
            k += 1
        j += 1
    return k, next_move


def find_level(L):
    max_k = 0
    j = 0
    while j < len(L):
        k, next_move = including(L, j)
        if k > max_k:
            max_k = k
        j = next_move
    return max_k


def executor(L):
    L = [(i[0], i[1]) for i in L]
    start = time.time()
    quickSort(L, 0, len(L) - 1)
    end = time.time()
    print(end - start)
    start = time.time()
    end = time.time()
    print(end - start)
    return find_level(L)


def creator(L: list):
    for i in range(10001):
        start = random.randint(1, 1000)
        end = random.randint(1000, 100000)
        L.append([start, end])
    return L


if __name__ == '__main__':
    # L = [(2, 2), (3, 3), (1, 4), (1, 3), (2, 5)]
    L = [[0, 2], [0, 1], [0, 3], [1, 4], [1, 5],[2,6]]
    # L = creator(L)
    # L = [elem[0] for elem in L1]
    # quickSort(L, 0, len(L) - 1)
    print(executor(L))
    # print(L)
