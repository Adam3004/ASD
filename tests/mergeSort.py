L = [1, 7, 3, 4, 2, 5, 6, 0]
L1 = [1, 2, 5, 17]
L2 = [3, 4, 5, 6]


# nieporządki T[i]>T[j] i<j
def mergeLists(L1, L2, n1, n2, counter):
    n = n1 + n2
    L0 = [None for _ in range(n)]
    i1 = 0
    i2 = 0
    i0 = 0
    while i1 < n1 and i2 < n2:
        checking1 = L1[i1]
        checking2 = L2[i2]
        if checking1 >= checking2:
            L0[i0] = checking2
            i2 += 1
            counter += n1 - i1
        else:
            L0[i0] = checking1
            i1 += 1
        i0 += 1
    if i1 < n1:
        while i1 < n1:
            L0[i0] = L1[i1]
            i1 += 1
            i0 += 1
    else:
        while i2 < n2:
            L0[i0] = L2[i2]
            i2 += 1
            i0 += 1
    return L0, counter


def mergeSort(L, counter):
    n = len(L)
    if n <= 1:
        return L, counter
    L1, counter = mergeSort(L[:n // 2], counter)
    L2, counter = mergeSort(L[n // 2:], counter)
    return mergeLists(L1, L2, n // 2, n - (n // 2), counter)


l, n = mergeSort(L, 0)
print(f'Lista: {L} ma {n} nieporządków i po posortowaniu wyglada tak: {l}\n')
