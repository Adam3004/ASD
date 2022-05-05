# Adam Misztal
from kol1atesty import runtests


# algorytm tworzy krotki jako wyraz i zsumowana liczba indexów ascii. Następnie sortuje po krotkach i zlicza ile jest
# takich samych wyrazów, upewniając się, że na pewno są równoważne, a nie tylko składają się z tych samych liter
# algorytm ma złożoność N +nlogn. N podczas tworzenia listy krotek i logn merge sortowanie, a na koniec sprawdzenie to
# też N
# Pamięciowo złożoność to n, bo tworze listy w merge sorcie których długość to będzie kilka n, ale nadal n


def g(T):
    return findStrongestWord(creator(T))


# dodawnienie indexów
def countLetters(word):
    counter = 0
    for elem in word:
        counter += ord(elem)
    return word, counter


# tworzenie krotek
def creator(T):
    T2 = [countLetters(T[i]) for i in range(len(T))]
    return T2


# merge 2 list
def mergeLists(L1, L2):
    i1 = 0
    i2 = 0
    n1 = len(L1)
    n2 = len(L2)
    L = [None for _ in range(n1 + n2)]
    i = 0
    while i1 < n1 and i2 < n2:
        checking1 = L1[i1]
        checking2 = L2[i2]
        if checking1[1] <= checking2[1]:
            L[i] = checking1
            i1 += 1
        else:
            i2 += 1
            L[i] = checking2
        i += 1

    if i1 == n1:
        while i2 < n2:
            L[i] = L2[i2]
            i2 += 1
            i += 1
    else:
        while i1 < n1:
            L[i] = L1[i1]
            i1 += 1
            i += 1
    return L


# merge sort
def mergeSort(T2):
    n = len(T2)
    if n <= 1:
        return T2
    L1 = mergeSort(T2[n // 2:])
    L2 = mergeSort(T2[:n // 2])
    return mergeLists(L1, L2)


def countSame(n, T2, j, i):
    counter = 1
    counter2 = 1
    nextChecking = None
    while j < n - 1 and T2[i][1] == T2[j + 1][1]:
        if T2[i][0] == T2[j + 1][0] or T2[i][0] == T2[j + 1][0][::-1]:
            counter += 1
        elif nextChecking is None:
            nextChecking = j + 1
        j += 1
    if nextChecking is not None:
        counter2 = countSame(n, T2, nextChecking, nextChecking)

    return max(counter, counter2)


# sprawdzenie i liczenie słow
def findStrongestWord(T2):
    i = 0
    n = len(T2)
    T2 = mergeSort(T2)
    max_strenght = 0
    while i < n - 1:
        # j = i
        # counter = 1
        # while j < n - 1 and T2[i][1] == T2[j + 1][1]:
        #     if T2[i][0] == T2[j + 1][0] or T2[i][0] == T2[j + 1][0][::-1]:
        #         counter += 1
        #     j += 1
        counter = countSame(n, T2, i, i)
        max_strenght = max(max_strenght, counter)

        i += counter

    return max_strenght


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests(g, all_tests=True)
