P = [1231, 312, 31, 4, 235, 32, 352, 1241421.414, 141, 4.14124142, 1.4, 1.4124124, 1412.4124124, 124124124124124.1,
     24124, 1.241]


# P = [15, 150, 333, 213, 1543]

# szuka najdłuższego wyrazu, żeby pozostałe wyrównać
def findMax(L):
    max = 0
    for elem in L:
        dl = len(str(elem))
        if dl > max:
            max = dl
    return max


# w zasadzie właściwy radix z countem w środku
def countingSort(L, n, max_len, size):
    B = [0 for _ in range(n)]
    C = [0 for _ in range(10)]
    # lecimy po wyrazach od ostatniego i count soretm sortujemy
    for i in range(max_len + size, -1, -1):
        if i == size:
            continue
        for j in range(n):
            C[int(L[j][i])] += 1
        for j in range(1, 10):
            C[j] += C[j - 1]
        for j in range(n - 1, -1, -1):
            B[C[int(L[j][i])] - 1] = L[j]
            C[int(L[j][i])] -= 1
        for j in range(n):
            L[j] = B[j]
        C = [0 for _ in range(10)]
    return L


def RadixSort(L, size):
    # preparing numbers to sort
    n = len(L)
    max_len = findMax(L) - size - 1
    our_format = "." + str(max_len) + "f"
    # wyrównanie wyrazów i zmiana ich na stringi
    L = [str(format(elem, our_format)) for elem in L]
    L = countingSort(L, n, max_len, size)
    # powrót na floaty
    L = [float(elem) for elem in L]
    return L


def CountBoxes(L):
    number = max(L)
    counter = 0
    while number > 0:
        number //= 10
        counter += 1

    return counter


def SortP(L):
    L = [float(elem) for elem in L]
    n_of_boxes = CountBoxes(L)
    # buckety
    ListOfLists = [[] for _ in range(n_of_boxes)]
    # przydzielanie do bucketów po długości
    if len(L) > 1:
        for elem in L:
            counter = 0
            x = elem // 10
            while x > 0:
                x //= 10
                counter += 1
            ListOfLists[counter].append(elem)
    else:
        return L
    # jeśli bucket ma coś w sobie to sortujemy
    for i in range(n_of_boxes):
        checking = ListOfLists[i]
        if len(checking) > 1:
            ListOfLists[i] = RadixSort(checking, i + 1)
    tmp = 0
    # wpierdalnie do listy
    for i in range(n_of_boxes):
        checking = ListOfLists[i]
        tmp_2 = tmp
        for j in range(len(checking)):
            L[j + tmp_2] = checking[j]
            tmp += 1

    return L


# print(CountBoxes(P))
# print(SortP(P))
print(SortP(P))


# /////////////////////////////////

# def find_ends(L):
#     start = L[-1][0]
#     end = L[-1][1]
#     for i in range(0, len(L), 2):
#         checking1 = L[i]
#         checking2 = L[i + 1]
#         if checking1[0] > checking2[0]:
#             if checking2[0] < start:
#                 start = checking2[0]
#         else:
#             if checking1[0] < start:
#                 start = checking1[0]
#         if checking1[1] > checking2[1]:
#             if checking1[1] > end:
#                 end = checking1[1]
#         else:
#             if checking2[1] > end:
#                 end = checking2[1]
#     return start, end
