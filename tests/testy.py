def longest(tab):
    n = len(tab)
    pom = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        j = i + 1
        while j < n and tab[i] >= tab[j]:
            j += 1
        if j >= n:
            if i < n - 1:
                pom[i] = pom[i + 1]
            else:
                pom[i] = 1
        else:
            pom[i] = pom[j] + 1
    print(pom)
    return pom[0]


print(longest([4, 1, 0, 3, 4]))
