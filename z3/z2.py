def NodePrinter(first):
    L = []
    while first is not None:
        L.append(first.val)
        first = first.next
    print(L)


# sortowanie dla P
def findMax(L):
    max = 0
    for elem in L:
        dl = len(str(elem[2]))
        if dl > max:
            max = dl
    return max


def countingSort(L, n, max_len, size):
    B = [0 for _ in range(n)]
    C = [0 for _ in range(10)]
    for i in range(max_len + size, -1, -1):
        if i == size:
            continue
        for j in range(n):
            C[int(L[j][2][i])] += 1
        for j in range(1, 10):
            C[j] += C[j - 1]
        for j in range(n - 1, -1, -1):
            B[C[int(L[j][2][i])] - 1] = L[j]
            C[int(L[j][2][i])] -= 1
        if i > 0:
            for j in range(n):
                L[j] = B[j]
        else:
            for j in range(n):
                L[n - j - 1] = B[j]
        C = [0 for _ in range(10)]
    return L


def RadixSort(L, size):
    # preparing numbers to sort
    n = len(L)
    max_len = findMax(L) - size - 1
    our_format = "." + str(max_len) + "f"
    L = [(elem[0], elem[1], str(format(elem[2], our_format))) for elem in L]
    L = countingSort(L, n, max_len, size)
    L = [(elem[0], elem[1], float(elem[2])) for elem in L]
    return L


def SortP(P):
    MoreThanNine = []
    LessThanNine = []
    if len(P) > 1:
        for elem in P:
            if elem[2] // 10 >= 1:
                MoreThanNine.append(elem)
            else:
                LessThanNine.append(elem)
    else:
        return P
    n_max = len(MoreThanNine)
    n_min = len(LessThanNine)
    if n_max > 1:
        MoreThanNine = RadixSort(MoreThanNine, 2)
    if n_min > 1:
        LessThanNine = RadixSort(LessThanNine, 1)
    tmp = 0
    for i in range(n_max):
        P[i] = MoreThanNine[i]
        tmp = i + 1
    for j in range(n_min):
        P[j + tmp] = LessThanNine[j]
    return P


# def SortP(P):
#     n = len(P)
#     for i in range(1, n):
#         x = P[i]
#         j = i - 1
#         while j >= 0 and P[j][2] < x[2]:
#             P[j + 1] = P[j]
#             j -= 1
#         else:
#             P[j + 1] = x
#     return P
# def SortP(P):
#     def moving(P, l, r):
#         x = P[r][2]
#         i = l - 1
#         for j in range(l, r):
#             if P[j][2] <= x:
#                 i += 1
#                 P[i], P[j] = P[j], P[i]
#         P[i + 1], P[r] = P[r], P[i + 1]
#         return i + 1
#
#     def quickSort(P, l, r):
#         while l < r:
#             q = moving(P, l, r)
#             quickSort(P, l, q - 1)
#             l = q + 1
#         return P
#
#     return quickSort(P, 0, len(P) - 1)


def SortBucket(Bucket):
    quickSort(Bucket, 0, len(Bucket) - 1)
    return Bucket


def moving(L, l, r):
    x = L[r]
    i = l - 1
    for j in range(l, r):
        if L[j] <= x:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i + 1], L[r] = L[r], L[i + 1]
    return i + 1


def quickSort(L, l, r):
    if l < r:
        q = moving(L, l, r)
        quickSort(L, l, q - 1)
        quickSort(L, q + 1, r)


def BucketCreator(probability, n):
    size = int((probability * n) // 1 + 1)
    ListOfBuckets = [[] for _ in range(size)]
    return ListOfBuckets, size


def InsertValToList(ListOfBuckets, size, Output, out_end, number_of_elems):
    n = len(Output)
    if number_of_elems > 0:
        lowest_val = 0
        highest_val = 10000000
        for i in range(size):
            if len(ListOfBuckets[i]) > 0:
                lowest_val = ListOfBuckets[i][0]
                break
        for i in range(size - 1, -1, -1):
            if len(ListOfBuckets[i]) > 0:
                highest_val = ListOfBuckets[i][-1]
                break
        out_low_val = Output[0]
        out_high_val = Output[out_end - 1]
        if lowest_val >= out_high_val:
            for i in range(size):
                for elem in ListOfBuckets[i]:
                    if out_end < n:
                        Output[out_end] = elem
                        out_end += 1
                    # print(Output)
        elif highest_val <= out_low_val:
            for i in range(out_end - 1, -1, -1):
                Output[i + number_of_elems] = Output[i]
            j = 0
            for i in range(size):
                for elem in ListOfBuckets[i]:
                    Output[j] = elem
                    j += 1
            out_end += number_of_elems
        else:
            for i in range(size):
                for elem in ListOfBuckets[i]:
                    j = out_end - 1
                    while j >= 0 and Output[j] > elem:
                        Output[j + 1] = Output[j]
                        j -= 1
                    out_end += 1
                    Output[j + 1] = elem
    return Output, out_end


def BucketSort(P, index, n, T, end, Output, out_end):
    actual_P = P[index]
    adding_elems_counter = 0
    ListOfBuckets, size = BucketCreator(actual_P[2], n)
    bottom = actual_P[0]
    upper = actual_P[1]
    step = (upper - bottom) / size
    i = 0
    while i <= end:
        actual_elem = T[i]
        if bottom <= actual_elem < upper:
            a = int((actual_elem - bottom) // step)
            ListOfBuckets[a].append(actual_elem)
            T[i], T[end] = T[end], T[i]
            end -= 1
            adding_elems_counter += 1
        elif actual_elem == upper:
            a = int((actual_elem - bottom) // step) - 1
            ListOfBuckets[a].append(actual_elem)
            T[i], T[end] = T[end], T[i]
            end -= 1
            adding_elems_counter += 1
        else:
            i += 1
    for i in range(len(ListOfBuckets)):
        if len(ListOfBuckets[i]) > 1:
            ListOfBuckets[i] = SortBucket(ListOfBuckets[i])
    Output, out_end = InsertValToList(ListOfBuckets, size, Output, out_end, adding_elems_counter)
    return end, Output, out_end


def SortTab(T, P):
    P = SortP(P)
    n = len(T)
    Output = [0 for _ in range(n)]
    out_end = 0
    end = n - 1
    for i in range(len(P)):
        end, Output, out_end = BucketSort(P, i, n, T, end, Output, out_end)
    T = Output
    return T


# LL method
#
# class Node:
#     def __init__(self, val: None):
#         self.val = val
#         self.next = None
#
# def BucketSort(P, index, n, T, end, first):
#     actual_P = P[index]
#     ListOfBuckets, size = BucketCreator(actual_P[2], n)
#     bottom = actual_P[0]
#     upper = actual_P[1]
#     step = (upper - bottom) / size
#     i = 0
#     while i <= end:
#         actual_elem = T[i]
#         if bottom <= actual_elem < upper:
#             a = int((actual_elem - bottom) // step)
#             ListOfBuckets[a].append(actual_elem)
#             T[i], T[end] = T[end], T[i]
#             end -= 1
#         elif actual_elem == upper:
#             a = int((actual_elem - bottom) // step) - 1
#             ListOfBuckets[a].append(actual_elem)
#             T[i], T[end] = T[end], T[i]
#             end -= 1
#         else:
#             i += 1
#     for i in range(len(ListOfBuckets)):
#         if len(ListOfBuckets[i]) > 1:
#             ListOfBuckets[i] = SortBucket(ListOfBuckets[i])
#     first = AddValuesToLL(first, ListOfBuckets)
#     return end, ListOfBuckets, first


# def AddValuesToLL(first, ListOfBuckets):
#     if first.next is not None:
#         first_val = first.next
#         p = first
#         while p.next is not None:
#             p = p.next
#         last_val = p
#         for Bucket in ListOfBuckets:
#             for elem in Bucket:
#                 if elem <= first_val.val:
#                     first.next = Node(elem)
#                     p = first
#                     p = p.next
#                     p.next = first_val
#                     first_val = p
#                 elif elem >= last_val.val:
#                     last_val.next = Node(elem)
#                     p = last_val
#                     p = p.next
#                     last_val = p
#                 else:
#                     p = first_val
#                     q = first
#                     while elem >= p.val:
#                         q = p
#                         p = p.next
#                     q.next = Node(elem)
#                     q = q.next
#                     q.next = p
#     else:
#         first_val = None
#         last_val = None
#         for Bucket in ListOfBuckets:
#             for elem in Bucket:
#                 if first_val is not None:
#                     if elem <= first_val.val:
#                         first.next = Node(elem)
#                         p = first
#                         p = p.next
#                         p.next = first_val
#                         first_val = p
#                     else:
#                         last_val.next = Node(elem)
#                         p = last_val
#                         p = p.next
#                         last_val = p
#                 else:
#                     first.next = Node(elem)
#                     p = first
#                     p = p.next
#                     first_val = p
#                     last_val = p
#     return first

#
# def ConvertLLToTable(first, T, n):
#     first = first.next
#     for i in range(n):
#         T[i] = first.val
#         first = first.next
#     return T


# def SortTab(T, P):
#     first = Node(None)
#     P = SortP(P)
#     n = len(T)
#     end = n - 1
#     for i in range(len(P)):
#         end, ListOfBuckets, first = BucketSort(P, i, n, T, end, first)
#     T = ConvertLLToTable(first, T, n)
#     return T

# rozwiazania pozosstałe
# # Adam Misztal
# import time
#
# from zad3testy import runtests
#
# #
# #
# #
# # class Node:
# #     def __init__(self, val: None):
# #         self.val = val
# #         self.next = None
# #
# #
# # def NodePrinter(first):
# #     L = []
# #     while first is not None:
# #         L.append(first.val)
# #         first = first.next
# #     print(L)
# #
# #
# # def SortP(P):
# #     n = len(P)
# #     for i in range(1, n):
# #         x = P[i]
# #         j = i - 1
# #         while j >= 0 and P[j][2] < x[2]:
# #             P[j + 1] = P[j]
# #             j -= 1
# #         else:
# #             P[j + 1] = x
# #     return P
# #
# #
# # def SortBucket(Bucket: list):
# #     for i in range(1, len(Bucket)):
# #         x = Bucket[i]
# #         j = i - 1
# #         while j >= 0 and Bucket[j] > x:
# #             Bucket[j + 1] = Bucket[j]
# #             j -= 1
# #         Bucket[j + 1] = x
# #     return Bucket
# #
# #
# # def BucketCreator(probability, n):
# #     size = int((probability * n) // 1 + 1)
# #     ListOfBuckets = [[] for _ in range(size)]
# #     return ListOfBuckets, size
# #
# #
# # def BucketSort(P, index, n, T, end, first):
# #     actual_P = P[index]
# #     ListOfBuckets, size = BucketCreator(actual_P[2], n)
# #     bottom = actual_P[0]
# #     upper = actual_P[1]
# #     step = (upper - bottom) / size
# #     i = 0
# #     while i <= end:
# #         actual_elem = T[i]
# #         if bottom <= actual_elem < upper:
# #             a = int((actual_elem - bottom) // step)
# #             ListOfBuckets[a].append(actual_elem)
# #             T[i], T[end] = T[end], T[i]
# #             end -= 1
# #         elif actual_elem == upper:
# #             a = int((actual_elem - bottom) // step) -1
# #             ListOfBuckets[a].append(actual_elem)
# #             T[i], T[end] = T[end], T[i]
# #             end -= 1
# #         else:
# #             i += 1
# #     for i in range(len(ListOfBuckets)):
# #         if len(ListOfBuckets[i]) > 1:
# #             ListOfBuckets[i] = SortBucket(ListOfBuckets[i])
# #     first = AddValuesToLL(first, ListOfBuckets)
# #     return end, ListOfBuckets, first
# #
# #
# # def AddValuesToLL(first, ListOfBuckets):
# #     if first.next is not None:
# #         first_val = first.next
# #         p = first
# #         while p.next is not None:
# #             p = p.next
# #         last_val = p
# #         for Bucket in ListOfBuckets:
# #             for elem in Bucket:
# #                 if elem <= first_val.val:
# #                     first.next = Node(elem)
# #                     p = first
# #                     p = p.next
# #                     p.next = first_val
# #                     first_val = p
# #                 elif elem >= last_val.val:
# #                     last_val.next = Node(elem)
# #                     p = last_val
# #                     p = p.next
# #                     last_val = p
# #                 else:
# #                     p = first_val
# #                     q = first
# #                     while elem >= p.val:
# #                         q = p
# #                         p = p.next
# #                     q.next = Node(elem)
# #                     q = q.next
# #                     q.next = p
# #     else:
# #         first_val = None
# #         last_val = None
# #         for Bucket in ListOfBuckets:
# #             for elem in Bucket:
# #                 if first_val is not None:
# #                     if elem <= first_val.val:
# #                         first.next = Node(elem)
# #                         p = first
# #                         p = p.next
# #                         p.next = first_val
# #                         first_val = p
# #                     else:
# #                         last_val.next = Node(elem)
# #                         p = last_val
# #                         p = p.next
# #                         last_val = p
# #                 else:
# #                     first.next = Node(elem)
# #                     p = first
# #                     p = p.next
# #                     first_val = p
# #                     last_val = p
# #     return first
# #
# #
# # def ConvertLLToTable(first, T, n):
# #     first = first.next
# #     for i in range(n):
# #         T[i] = first.val
# #         first = first.next
# #     return T
# #
# #
# # def SortTab(T, P):
# #     first = Node(None)
# #     # P = SortP(P)
# #     n = len(T)
# #     end = n - 1
# #     for i in range(len(P)):
# #         end, ListOfBuckets, first = BucketSort(P, i, n, T, end, first)
# #     T = ConvertLLToTable(first, T, n)
# #     return T
#
#
# # sposób 2
#
# #
# # def SortBucket(Bucket):
# #     quickSort(Bucket, 0, len(Bucket) - 1)
# #     return Bucket
# #
# #
# # def moving(L, l, r):
# #     x = L[r]
# #     i = l - 1
# #     for j in range(l, r):
# #         if L[j] <= x:
# #             i += 1
# #             L[i], L[j] = L[j], L[i]
# #     L[i + 1], L[r] = L[r], L[i + 1]
# #     return i + 1
# #
# #
# # def quickSort(L, l, r):
# #     while l < r:
# #         q = moving(L, l, r)
# #         quickSort(L, l, q - 1)
# #         l = q + 1
# #
# #
# # def BucketCreator(probability, n):
# #     size = int((probability * n) // 1 + 1)
# #     ListOfBuckets = [[] for _ in range(size)]
# #     return ListOfBuckets, size
# #
# #
# # def InsertValToList(ListOfBuckets, size, Output, out_end, number_of_elems):
# #     n = len(Output)
# #     if number_of_elems > 0:
# #         lowest_val = 0
# #         highest_val = 10000000
# #         for i in range(size):
# #             if len(ListOfBuckets[i]) > 0:
# #                 lowest_val = ListOfBuckets[i][0]
# #                 break
# #         for i in range(size - 1, -1, -1):
# #             if len(ListOfBuckets[i]) > 0:
# #                 highest_val = ListOfBuckets[i][-1]
# #                 break
# #         out_low_val = Output[0]
# #         out_high_val = Output[out_end - 1]
# #         if lowest_val >= out_high_val:
# #             for i in range(size):
# #                 for elem in ListOfBuckets[i]:
# #                     if out_end < n:
# #                         Output[out_end] = elem
# #                         out_end += 1
# #                     # print(Output)
# #         elif highest_val <= out_low_val:
# #             for i in range(out_end - 1, -1, -1):
# #                 Output[i + number_of_elems] = Output[i]
# #             j = 0
# #             for i in range(size):
# #                 for elem in ListOfBuckets[i]:
# #                     Output[j] = elem
# #                     j += 1
# #             out_end += number_of_elems
# #         else:
# #             for i in range(size):
# #                 for elem in ListOfBuckets[i]:
# #                     j = out_end - 1
# #                     while j >= 0 and Output[j] > elem:
# #                         Output[j + 1] = Output[j]
# #                         j -= 1
# #                     out_end += 1
# #                     Output[j + 1] = elem
# #     return Output, out_end
# #
# #
# # def BucketSort(P, index, n, T, end, Output, out_end):
# #     actual_P = P[index]
# #     adding_elems_counter = 0
# #     ListOfBuckets, size = BucketCreator(actual_P[2], n)
# #     bottom = actual_P[0]
# #     upper = actual_P[1]
# #     step = (upper - bottom) / size
# #     i = 0
# #     while i <= end:
# #         actual_elem = T[i]
# #         if bottom <= actual_elem < upper:
# #             a = int((actual_elem - bottom) // step)
# #             ListOfBuckets[a].append(actual_elem)
# #             T[i], T[end] = T[end], T[i]
# #             end -= 1
# #             adding_elems_counter += 1
# #         elif actual_elem == upper:
# #             a = int((actual_elem - bottom) // step) - 1
# #             ListOfBuckets[a].append(actual_elem)
# #             T[i], T[end] = T[end], T[i]
# #             end -= 1
# #             adding_elems_counter += 1
# #         else:
# #             i += 1
# #     for i in range(len(ListOfBuckets)):
# #         if len(ListOfBuckets[i]) > 1:
# #             ListOfBuckets[i] = SortBucket(ListOfBuckets[i])
# #     Output, out_end = InsertValToList(ListOfBuckets, size, Output, out_end, adding_elems_counter)
# #     return end, Output, out_end
# #
# #
# # # sortowanie dla P
# # def findMax(L):
# #     max = 0
# #     for elem in L:
# #         dl = len(str(elem[2]))
# #         if dl > max:
# #             max = dl
# #     return max
# #
# #
# # def countingSort(L, n, max_len, size):
# #     B = [0 for _ in range(n)]
# #     C = [0 for _ in range(10)]
# #     for i in range(max_len + size, -1, -1):
# #         if i == size:
# #             continue
# #         for j in range(n):
# #             C[int(L[j][2][i])] += 1
# #         for j in range(1, 10):
# #             C[j] += C[j - 1]
# #         for j in range(n - 1, -1, -1):
# #             B[C[int(L[j][2][i])] - 1] = L[j]
# #             C[int(L[j][2][i])] -= 1
# #         if i > 0:
# #             for j in range(n):
# #                 L[j] = B[j]
# #         else:
# #             for j in range(n):
# #                 L[n - j - 1] = B[j]
# #         C = [0 for _ in range(10)]
# #     return L
# #
# #
# # def RadixSort(L, size):
# #     # preparing numbers to sort
# #     n = len(L)
# #     max_len = findMax(L) - size - 1
# #     our_format = "." + str(max_len) + "f"
# #     L = [(elem[0], elem[1], str(format(elem[2], our_format))) for elem in L]
# #     L = countingSort(L, n, max_len, size)
# #     L = [(elem[0], elem[1], float(elem[2])) for elem in L]
# #     return L
# #
# #
# # def SortP(P):
# #     MoreThanNine = []
# #     LessThanNine = []
# #     if len(P) > 1:
# #         for elem in P:
# #             if elem[2] // 10 >= 1:
# #                 MoreThanNine.append(elem)
# #             else:
# #                 LessThanNine.append(elem)
# #     else:
# #         return P
# #     n_max = len(MoreThanNine)
# #     n_min = len(LessThanNine)
# #     if n_max > 1:
# #         MoreThanNine = RadixSort(MoreThanNine, 2)
# #     if n_min > 1:
# #         LessThanNine = RadixSort(LessThanNine, 1)
# #     tmp = 0
# #     for i in range(n_max):
# #         P[i] = MoreThanNine[i]
# #         tmp = i + 1
# #     for j in range(n_min):
# #         P[j + tmp] = LessThanNine[j]
# #     return P
# #
# #
# # def SortTab(T, P):
# #     # P = SortP(P)
# #     n = len(T)
# #     # revers_P(P)
# #     Output = [0 for _ in range(n)]
# #     out_end = 0
# #     end = n - 1
# #     for i in range(len(P)):
# #         end, Output, out_end = BucketSort(P, i, n, T, end, Output, out_end)
# #     T = Output
# #     return T
#
#
# # sposob 3 (działa dobrze)
#
# # Adam Misztal
# # W procesię tworzenia kodu podpierałem się wiedzą z wykładu, a także z Cormena.
# # Sposób rozwiązania: najpierw znajduję największą i najmniejszą wartość jakie są w przedziałach w talbicy P, następnie
# # bucket sortem sortuje listę. Tworzę n//15 kubełków, ponieważ tak moim zdaniem jest najoptymalniej, bo testowałem różne
# # liczby, a lepiej przedzieć n przez jakąś liczbe, bo przy n kubełkach jest dość sporo pustych. Sam algorytm działa
# # poprawnie, ponieważ to zwykły bucket sort.
# # Złożoność tego algorytmu średnio jest liniowa, a w najgorszym wypadku nlogn gdy mamy tylko 1 kubełek. find_ends ma
# # złożonośc n/2, a bucketsort c*n gdzie c to stała. Co prawda, buckety są sortowane quciksortem który jest nlogn, ale
# # przy tych liczbach jest on dość optymalny, bo nawet jeśli w przedziałach będzie sporo liczb to będzie się on lepiej
# # zachowywał niż jakiś kwadratowy algorytm sortowania, a żaden liniowy algorytm przy na tyle różnych danych nie byłby
# # sensowny. Jedyna sytuacja która może spowodować, że algorytm jest liniowy to taka, gdy n<30 i mamy tylko jeden kubełek
# # wtedy algorytm ma złożoność quicksorta, czyli nlogn, ale są to nieduże liczby więc nie jest to problem. Dla większych
# # n problem znika bo quicksort działa w złożoności klogk gdzie k to liczba elementów w danym kubełku, a zazwyczaj k jest
# # znacznie mniejsze niż n, więc w średnim przypadku algorytm działa liniowo.
#
# from zad3testy import runtests
#
#
# # algorytm szukania min max, ma złożoność n/2, bo porównujemy na bieżąco wyraz i-ty z i+1-wszym, więc pętla wykona się
# # n/2 razy. Przypisujemy na początku do startu i endu wartości ostatniej krotki z tablicy, bo dzięki temu unikamy ifa
# # po pętli który sprawdzałby ostatni wyraz w przypadku gdy n parzyste.
# # Napisałem podobny algorytm do tego jaki kojarzyłem z ćwiczeń.
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
#
#
# # quicksort
# def moving(L, l, r):
#     x = L[r]
#     i = l - 1
#     for j in range(l, r):
#         if L[j] <= x:
#             i += 1
#             L[i], L[j] = L[j], L[i]
#     L[i + 1], L[r] = L[r], L[i + 1]
#     return i + 1
#
#
# def quickSort(L, l, r):
#     while l < r:
#         q = moving(L, l, r)
#         quickSort(L, l, q - 1)
#         l = q + 1
#
#
# # quickSort end
#
# # bucketSort
# def bucketSort(n, T, start, end):
#     size = n // 15
#     if size == 0:
#         size = 1
#     bottom = start
#     upper = end
#     step = (upper - bottom) / size
#     ListOfBuckets = [[] for _ in range(size)]
#     for i in range(n):
#         actual_elem = T[i]
#         ListOfBuckets[int((actual_elem - bottom) // step)].append(actual_elem)
#     for i in range(len(ListOfBuckets)):
#         if len(ListOfBuckets[i]) > 1:
#             quickSort(ListOfBuckets[i], 0, len(ListOfBuckets[i]) - 1)
#     j = 0
#     for i in range(len(ListOfBuckets)):
#         for elem in ListOfBuckets[i]:
#             T[j] = elem
#             j += 1
#     return T
#
#
# # główna funkcja sortująca
# def SortTab(T, P):
#     n = len(T)
#     start, end = find_ends(P)
#     T = bucketSort(n, T, start, end)
#     return T
#
#
# # sposób 4
# #
# # def findMax(L):
# #     max = 0
# #     for elem in L:
# #         dl = len(str(elem[0]))
# #         if dl > max:
# #             max = dl
# #     return max
# #
# #
# # def countingSort(L, n, max_len, size):
# #     B = [0 for _ in range(n)]
# #     C = [0 for _ in range(10)]
# #     for i in range(max_len + size, -1, -1):
# #         if i == size:
# #             continue
# #         for j in range(n):
# #             C[int(L[j][0][i])] += 1
# #         for j in range(1, 10):
# #             C[j] += C[j - 1]
# #         for j in range(n - 1, -1, -1):
# #             B[C[int(L[j][0][i])] - 1] = L[j]
# #             C[int(L[j][0][i])] -= 1
# #         for j in range(n):
# #             L[j] = B[j]
# #         C = [0 for _ in range(10)]
# #     return L
# #
# #
# # def RadixSort(L, size):
# #     # preparing numbers to sort
# #     n = len(L)
# #     max_len = findMax(L) - size - 1
# #     our_format = "." + str(max_len) + "f"
# #     L = [(str(format(elem[0], our_format)), str(format(elem[1], our_format)), elem[2]) for elem in L]
# #     L = countingSort(L, n, max_len, size)
# #     L = [(float(elem[0]), float(elem[1]), elem[2]) for elem in L]
# #     return L
# #
# #
# # def CountBoxes(L):
# #     number = max(L)[0]
# #     counter = 0
# #     while number > 0:
# #         number //= 10
# #         counter += 1
# #
# #     return counter
# #
# #
# # def SortP(L):
# #     L = [(float(elem[0]), float(elem[1]), elem[2]) for elem in L]
# #     n_of_boxes = CountBoxes(L)
# #     ListOfLists = [[] for _ in range(n_of_boxes)]
# #     if len(L) > 1:
# #         for elem in L:
# #             check = elem[0]
# #             counter = 0
# #             x = check // 10
# #             while x > 0:
# #                 x //= 10
# #                 counter += 1
# #             ListOfLists[counter].append(elem)
# #     else:
# #         return L
# #     for i in range(n_of_boxes):
# #         checking = ListOfLists[i]
# #         if len(checking) > 1:
# #             ListOfLists[i] = RadixSort(checking, i + 1)
# #     tmp = 0
# #     for i in range(n_of_boxes):
# #         checking = ListOfLists[i]
# #         tmp_2 = tmp
# #         for j in range(len(checking)):
# #             L[j + tmp_2] = checking[j]
# #             tmp += 1
# #
# #     return L
# #
# #
# # def SortTab(T, P):
# #     n = len(T)
# #     P = SortP(P)
# #     Output = []
# #     end = n - 1
# #     for i in range(len(P)):
# #         Output, end = BucketSort(P, i, n, T, end, Output)
# #         if end < 0:
# #             break
# #     return Output
# #
# #
# # def BucketCreator(probability, n):
# #     size = int((probability * n) // 1 + 1)
# #     ListOfBuckets = [[] for _ in range(size)]
# #     return ListOfBuckets, size
# #
# #
# # def moving(L, l, r):
# #     x = L[r]
# #     i = l - 1
# #     for j in range(l, r):
# #         if L[j] <= x:
# #             i += 1
# #             L[i], L[j] = L[j], L[i]
# #     L[i + 1], L[r] = L[r], L[i + 1]
# #     return i + 1
# #
# #
# # def quickSort(L, l, r):
# #     while l < r:
# #         q = moving(L, l, r)
# #         quickSort(L, l, q - 1)
# #         l = q + 1
# #
# #
# # def BucketSort(P, index, n, T, end, Output):
# #     actual_P = P[index]
# #     ListOfBuckets, size = BucketCreator(actual_P[2], n)
# #     if size == 0:
# #         size = 1
# #     bottom = actual_P[0]
# #     upper = actual_P[1]
# #     step = (upper - bottom) / size
# #     i = 0
# #     changed = False
# #     while i <= end:
# #         actual_elem = T[i]
# #         if bottom <= actual_elem < upper:
# #             a = int((actual_elem - bottom) // step)
# #             ListOfBuckets[a].append(actual_elem)
# #             T[i], T[end] = T[end], T[i]
# #             end -= 1
# #             changed = True
# #         elif actual_elem == upper:
# #             a = int((actual_elem - bottom) // step) - 1
# #             ListOfBuckets[a].append(actual_elem)
# #             T[i], T[end] = T[end], T[i]
# #             end -= 1
# #             changed = True
# #         else:
# #             i += 1
# #     if changed:
# #         for i in range(len(ListOfBuckets)):
# #             checking = ListOfBuckets[i]
# #             if len(checking) > 1:
# #                 quickSort(ListOfBuckets[i], 0, len(checking) - 1)
# #             for j in range(len(checking)):
# #                 Output.append(checking[j])
# #
# #     return Output, end
#
#
# runtests(SortTab)

if __name__ == '__main__':
    T = [6.1, 1.2, 1.5, 3.5, 4.5, 9.2, 2.5, 3.9, 7.8, 15, 12.3, 3, 5, 7, 2.5]
    # T =[15.0]
    P = [(1, 5, 0.60), (4, 8, 0.20), (10, 15, 0.05), (1, 20, 0.05), (4, 7, 0.1)]

    print(SortTab(T, P))
