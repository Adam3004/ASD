def findLeader(L):
    i1 = 0
    i2 = 1
    n = len(L)
    P = L.copy()
    if n <= 2:
        if n > 1:
            return True
        else:
            return False
    else:
        while i1 < n - 2 and i2 < n:
            if L[i1] == L[i2]:
                i2 += 1
            else:
                candidate = L[i1]
                P[i1], P[i2] = -1, -1
                i1 += 1
                i2 += 1
                while i1 < n and P[i1] == -1:
                    i1 += 1
                while i2 <= i1:
                    i2 += 1

                # if i2 < n - 1:
                #     i1 = i2 + 1
                #     i2 = i1 + 1
                # else:
                #     i2 += 1
    if i1 < n and L[i1] != -1:
        candidate = L[i1]
    counter = 0
    for elem in L:
        if elem == candidate:
            counter += 1
    if counter > n // 2:
        return True
    return False


def findLeaderV2(L):
    leader = L[0]
    counter = 1
    n = len(L)
    for i in range(1, n):
        if L[i] == leader:
            counter += 1
        else:
            counter -= 1
            if counter == 0:
                leader = L[i]
    counter = 0
    for elem in L:
        if leader == elem:
            counter += 1
    return counter > n // 2


L = [1, 1, 1, 1, 5, 3, 5, 1, 5]
print(findLeaderV2(L))
