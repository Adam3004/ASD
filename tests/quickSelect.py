def partition(L, l, p):
    x = L[p]
    first_b = l
    for i in range(l, p):
        if L[i] <= x:
            L[i], L[first_b] = L[first_b], L[i]
            first_b += 1
    L[p], L[first_b] = L[first_b], L[p]
    return first_b


def quickSelect(L, l, k, p):
    if l == p:
        return L[l]
    if l < p:
        q = partition(L, l, p)
        if q == k:
            return L[q]
        elif q > k:
            return quickSelect(L, l, k, q - 1)
        else:
            return quickSelect(L, q + 1, k, p)


L = [123, 63, 2, 5, 7, 1, 7, 12, 7, 1, 8, 9, 41, 23, 67, 2]
k = 12
print(quickSelect(L, 0, k, len(L) - 1))
L.sort()
print(L[k])
