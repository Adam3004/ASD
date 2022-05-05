import random
import time

L = [random.randint(1, 20) for _ in range(20)]
# L = [1, 2, 1, 1, 1]


def moving_modified(L: list, l: int, r: int):
    x = L[r]
    i = l - 1
    counter = 0
    for j in range(l, r):
        if L[j] < x:
            i += 1
            L[i], L[j] = L[j], L[i]
        elif L[j] == x:
            counter += 1
            i += 1
            L[i], L[j] = L[j], L[i]
    if counter == r - l:
        return (l + r) // 2
    else:
        L[i + 1], L[r] = L[r], L[i + 1]
        return i + 1


def moving(L: list, l: int, r: int):
    x = L[r]
    i = l - 1
    for j in range(l, r):
        if L[j] <= x:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i + 1], L[r] = L[r], L[i + 1]
    return i + 1


def quickSort(L: list, l, r):
    if l < r:
        q = moving(L, l, r)
        quickSort(L, l, q - 1)
        quickSort(L, q + 1, r)


if __name__ == "__main__":
    s = time.time()
    quickSort(L, 0, len(L) - 1)
    print(L)
    e = time.time()
    print(e - s)
