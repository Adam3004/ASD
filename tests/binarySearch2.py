def binarySearch(L, x):
    l = 0
    p = len(L) - 1
    while l <= p:
        s = (l + p) // 2
        if L[s] == x:
            return s
        elif L[s] > x:
            p = s - 1
        else:
            l = s + 1
    return -1


print(binarySearch([1, 2, 3, 4, 5, 6, 7], 5))
