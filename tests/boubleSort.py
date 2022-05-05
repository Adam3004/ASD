L = [1, 5, 7, 3, 2, 12, 4, 15, 6, 26, 0, 54, 17, 23, 32, 41, 14, 81, 63, 22, 0, 16, 16, 5, 3, 23, 25, 100, 12]


def bouble(L):
    n = len(L)
    chages = 1
    while chages > 0:
        chages = 0
        for i in range(n - 1):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                chages += 1


if __name__ == "__main__":
    P = sorted(L)
    bouble(L)
    print(L)
    print(P)

# przypadek optymistyczny   n
# przypadek pesymistyczny   n^2
# przypadek średni          n^2
