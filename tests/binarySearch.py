# znajdz pierwszą liczę której nie ma
# ciąg n elementowy, o elementach z przedziału 0-m
# n<m
import random

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 11]


def search(L):
    l = L[0]
    p = L[-1]
    min = L[-1] + 1
    x = min
    while p - l > 1:
        if (l + p) // 2 not in L:
            min = (l + p) // 2
        p = p - 1
    if min != x:
        return min
    else:
        l = L[-2]
        p = L[-1]
        while l > 0:
            if (l + p) // 2 not in L:
                min = (l + p) // 2
            l = l - 1
    return min


def search_test(L):
    l = L[0]
    p = L[-1]
    min = L[-1] + 1
    x = min
    while p - l > 1:
        if (l + p) // 2 not in L:
            min = (l + p) // 2
        p = p - 1
    if min != x:
        return False
    else:
        return True


def creator():
    L = [random.randint(0, 1000) for _ in range(100)]
    return L
    # if
    # L = [elem if elem in L else random.randint(0,1000) for elem in L]


def tester():
    counter_main = 0
    t = False
    for j in range(100):
        counter = 0
        for i in range(1000):
            L = creator()
            if search_test(L):
                counter += 1
        if counter / 10 > 50:
            counter_main += 1
        elif counter / 10 == 50:
            if t:
                counter_main += 1
                t = False
            else:
                t = True

    print(counter_main)


if __name__ == "__main__":
    tester()
# moim zdaniem
# przypadek optymistyczny   n
# przypadek pesymistyczny   n/n^2 (48%/52%)
# przypadek średni          n^2
