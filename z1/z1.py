import time


class Node:
    def __init__(self):
        self.val = None  # przechowywana liczba rzeczywista
        self.next = None  # odsyłacz do nastepnego elementu


def printer(p):
    while p is not None:
        print(f'{p.val} ')
        p = p.next


def creator():
    p = Node()
    p.val = 11
    q = p
    for i in range(1, 2):
        q.next = Node()
        q = q.next
        q.val = 8 * i
        q.next = Node()
        q = q.next
        q.val = 1 * i
        q.next = Node()
        q = q.next
        q.val = 2 * i
        q.next = Node()
        q = q.next
        q.val = 7 * i
        # q.next = Node()
        # q = q.next
        # q.val = 5 * i
    return p


def insSort(p, k):
    first = p
    q = p
    while q.next is not None and q.next.val < p.val:
        q = q.next
    tmp = q.next
    q.next = p
    first = q
    q = q.next
    q.next = tmp

    k = k - 1
    z = first
    p = first.next
    while k > 0:
        q = p
        q = q.next
        while q.next is not None and q.next.val < p.val:
            q = q.next
        tmp = q.next
        q.next = p
        z = q
        q = q.next
        q.next = tmp
        k = k - 1
        p = p.next
    return first


def insSort_v2(p):
    # działa gdy są koło sb
    first = p
    prev = p.next
    while prev is not None and prev.val > p.val:
        prev = prev.next

    if prev is not None:
        tmp = prev.next
        prev.next = p
        first = prev
        prev = prev.next
        prev.next = tmp

    p = first.next
    connector = first  # element do którego będziemy przepinać (jest to element poprzedzający p)
    while p is not None:
        prev = p.next
        while prev is not None and prev.val > p.val:
            prev = prev.next
        # gdy są koło siebie to działa
        if prev is not None:
            tmp = prev.next
            connector.next = prev
            connector = connector.next
            connector.next = p
            connector = connector.next
            connector.next = tmp
            p = connector.next
        else:
            connector = p
            p = p.next

    return first


def insSort_v3(p):
    # czasem się sypie ale w miarędziała
    first = p
    changed = True
    while changed:
        prev = p
        while prev.next is not None and prev.next.val < p.val:
            prev = prev.next

        if prev.val < p.val:
            tmp = prev.next
            prev.next = p
            first = p.next
            prev = prev.next
            prev.next = tmp
            p = first
        else:
            p = first.next
            changed = False

    connector = first  # element do którego będziemy przepinać (jest to element poprzedzający p)
    while p is not None:
        prev = p
        while prev.next is not None and prev.next.val < p.val:
            prev = prev.next

        if prev.val < p.val:
            tmp = prev.next
            connector.next = p.next
            prev.next = p
            prev = prev.next
            prev.next = tmp
            p = connector.next
        else:
            connector = p
            p = p.next

    return first


def SortH(p, k):
    # 0-chaotyczna jest już posortowana
    if k == 0:
        return p
    else:
        # 1-chaotyczna jest sortowana przez bubble sorta w czasie liniowym
        first = bubbleSort(p)
    return first


# bubble sort
def bubbleSort(p):
    first = p  # zmienna wskazująca pierwszy element
    anyChanges = True  # zmienna odpowiedzialna za sprawdzenie czy w trakcie przejscia były dokonanie jakieś zmiany
    # jeśli nie to pętla się kończy, ponieważ tablica jest wtedy już posortowana
    while anyChanges:
        anyChanges = False
        # zamaiana pierwszego elementu z drugim jeśli jest taka potrzeba
        if p.next.val < p.val:
            prev = p.next
            tmp = prev.next
            prev.next = p
            first = prev
            prev = prev.next
            prev.next = tmp
            p = first.next
            anyChanges = True
        connector = first  # element poprzedzający p, do którego będziemy podłączali element na który wskazuje prev, gdy
        # trzeba będzie je zamienić
        # pętla przepina pozostałe elementy w razię potrzeby
        while p.next is not None:
            prev = p.next
            if prev.val < p.val:
                tmp = prev.next
                connector.next = prev
                connector = connector.next
                prev.next = p
                p.next = tmp
                anyChanges = True
            else:
                connector = p
                p = p.next
        # ustawiamy p na first i jeśli jakieś zmiany były wykonane, to rozpoczynamy kolejne wykonanie pętli
        p = first

    return first


# heap heap hurra

def left(i): return 2 * i + 1


def right(i): return 2 * i + 2


def parent(i): return (i - 1) // 2


#
#
# # 4 główne opcje problemu
# # 1) ...,i,max,...
# # 2) ...,i,...,max,...
# # 3) i,max,...
# # 4) i,...,max,...
# # rozwiązanie: sprawdzamy przy pomocy if, czy nie musimy zamienić dwóch kolejnych wyrazów, jeśli tak, zamiana odbywa
# # się nieco inaczej
# # dodatkowo po wykonaniu zamiany sprawdzamy czy nie zamienialiśmy elementu który w liście jest na pozycji 0
# # możemy to stwierdzić patrząc na to jaką wartość będzie miał element 1 w krotce która w liście jest wcześniej
# # jeżli tak zwracamy nowy wskaźnik na początek listy, jeżeli nie, to zwracamy normalne p
#
# def swap(i_nodes, max_nodes, p):
#     if i_nodes[1] == max_nodes[0]:
#         tmp_max = max_nodes[1].next
#         tmp_elem = i_nodes[1]
#         i_nodes[0].next = max_nodes[1]
#         max_nodes[1].next = tmp_elem
#         tmp_elem.next = tmp_max
#         if i_nodes[0].val is not None:
#             return p
#         else:
#             return max_nodes[1]
#
#     tmp_i = i_nodes[1].next
#     tmp_max = max_nodes[1].next
#     i_nodes[0].next = max_nodes[1]
#     max_nodes[1].next = tmp_i
#     max_nodes[0].next = i_nodes[1]
#     i_nodes[1].next = tmp_max
#     if i_nodes[0].val is not None:
#         return p
#     else:
#         return max_nodes[1]
#
#
# # def jump(p, i, p2, n):
# #     if i == 0:
# #         return Node(), p
# #     if i <= n // 2:
# #         for _ in range(i - 1):
# #             p = p.next
# #         return p, p.next
# #     for _ in range((i - n // 2) - 1):
# #         p2 = p2.next
# #     return p2, p2.next
# #     # if i <= 1:
# #     #     return p, p.next
# #     # else:
# #     #     return jump(p.next, i - 1)
#
# def jump(p, i, p2, n):
#     if i == 0:
#         return Node(), p
#     for _ in range(i - 1):
#         p = p.next
#     return p, p.next
#
#
# # def heapify(tab, i, k, start, n):
# #     l = left(i)
# #     r = right(i)
# #     max_val = i
# #     if l + start < n and tab[start + l] < tab[start + max_val]:
# #         max_val = l
# #     if r + start < n and tab[start + r] < tab[start + max_val]:
# #         max_val = r
# #     if max_val != i:
# #         tab[max_val + start], tab[i + start] = tab[i + start], tab[max_val + start]
# #         heapify(tab, max_val, k, start, n)
#
#
# def build_heap(tab, k, j, n):
#     for i in range(parent(k), - 1, -1):
#         heapify(tab, i, k, j, n)
#
#
# def reversed_heapify(tab, i, k, start, n):
#     l = left(i)
#     r = right(i)
#     max_val = i
#     if l + start < n and tab[start + l] > tab[start + max_val]:
#         max_val = l
#     if r + start < n and tab[start + r] > tab[start + max_val]:
#         max_val = r
#     if max_val != i:
#         tab[max_val + start], tab[i + start] = tab[i + start], tab[max_val + start]
#         reversed_heapify(tab, max_val, k, start, n)
#
#
# #
# # def len_ods(p):
# #     counter = 0
# #     while p is not None:
# #         p = p.next
# #         counter += 1
# #     return counter
# #
# #
# # def find_middle(p, n):
# #     for i in range(n // 2):
# #         p = p.next
# #     return p
# #
# #
# # def reversing(first):
# #     p = first
# #     while p.next is not None:
# #         tmp = p.next
# #         p.next = tmp.next
# #         tmp.next = first
# #         first = tmp
# #     return first
#
#


#
def changer_to_linked_list(tab, p, start):
    while p is not None:
        p.val = tab[start]
        p = p.next
        start -= 1


def len_of_linked_list(p):
    counter = 0
    while p is not None:
        counter += 1
        p = p.next
    return counter


#
#
def pom(p):
    first = p
    while p is not None:
        p.val = -1
        p = p.next
    return first


#
#
# # def heap_sort(p, k):
#     n = len_of_linked_list(p)
#     tab = [None for _ in range(n)]
#     tab = chnager_to_table(p, tab)
#     first = pom(p)
#     # build_heap(tab, k, n - k - 1)
#     # for i in range(k, 0, -1):
#     #     tab[0], tab[i] = tab[i], tab[0]
#     #     heapify(tab, 0, i - 1, 0)
#     # tab[n - 1], tab[n - k - 1] = tab[n - k - 1], tab[n - 1]
#     build_heap(tab, k, 0, n)
#     p.val = tab[0]
#     p = p.next
#     j = 0
#     # for j in range(n - k - 2, -1, -1):
#     for j in range(1, n - k):
#         build_heap(tab, k, j, n)
#         # tab[j], tab[j - k - 1] = tab[j - k - 1], tab[j]
#         p.val = tab[j]
#         p = p.next
#     # build_heap(tab, k, j, n)
#     # p.val = tab[j]
#     # p = p.next
#     for i in range(1, k):
#         heapify(tab, 0, k - i + 1, j + i, n)
#         p.val = tab[j + i]
#         p = p.next
#     # changer_to_linked_list(tab, p, n - 2)
#
#     return first
#
# def heap_sort(p, k):
#     n = len_of_linked_list(p)
#     tab = [None for _ in range(n)]
#     tab = chnager_to_table(p, tab)
#     tmp_tab = [tab[i] for i in range(k)]
#     first = pom(p)
#     if k>=n:
#         k=k-1
#     # build_heap(tab, k, n - k - 1)
#     # for i in range(k, 0, -1):
#     #     tab[0], tab[i] = tab[i], tab[0]
#     #     heapify(tab, 0, i - 1, 0)
#     # tab[n - 1], tab[n - k - 1] = tab[n - k - 1], tab[n - 1]
#     build_heap(tmp_tab, k, 0, k)
#     print(tmp_tab)
#     p.val = tmp_tab[0]
#     p = p.next
#     tmp_tab[0] = tab[k]
#     j = 0
#     # for j in range(n - k - 2, -1, -1):
#     for j in range(1, n - k):
#         heapify(tmp_tab,0, k, 0, k)
#         # tab[j], tab[j - k - 1] = tab[j - k - 1], tab[j]
#         p.val = tmp_tab[0]
#         p = p.next
#         tmp_tab[0] = tab[k + j]
#     # build_heap(tab, k, j, n)
#     # p.val = tab[j]
#     # p = p.next
#     for i in range(1, k):
#         build_heap(tmp_tab, k - i + 1, 0, k)
#         p.val = tmp_tab[i]
#         p = p.next
#     print(tmp_tab)
#     # changer_to_linked_list(tab, p, n - 2)
#
#     return first

def build_heap(tab, k):
    for i in range(parent(k), - 1, -1):
        heapify(tab, i, k)


def heapify(tab, i, k):
    l = left(i)
    r = right(i)
    max_val = i
    if l <= k and tab[l] < tab[max_val]:
        max_val = l
    if r <= k and tab[r] < tab[max_val]:
        max_val = r
    if max_val != i:
        tab[max_val], tab[i] = tab[i], tab[max_val]
        heapify(tab, max_val, k)


def changer(tab, k):
    max = tab[0]
    tab[0] = tab[k]
    heapify(tab, 0, k)
    return max


def increase(tab, i, val):
    tab[i] = val
    while i > 0 and tab[parent(i)] > tab[i]:
        tab[parent(i)], tab[i] = tab[i], tab[parent(i)]
        i = parent(i)


def chnager_to_table(p, tab, n):
    for i in range(n):
        tab[i] = p.val
        p = p.next
        i += 1

    return tab, p


def heap_sort(p, k):
    n = len_of_linked_list(p)
    first = p
    q = p
    if k >= n:
        k = n - 1
    tmp_tab = [None for _ in range(k + 1)]
    tmp_tab, p = chnager_to_table(p, tmp_tab, k + 1)
    # first = pom(p)
    build_heap(tmp_tab, k)
    for i in range(n - k - 1):
        q.val = changer(tmp_tab, k)
        q = q.next
        increase(tmp_tab, k, p.val)
        p = p.next
    # for i in range(n - 1, n - k - 1, -1):
    #     tmp_tab[i], tmp_tab[n - k - 1] = tmp_tab[n - k - 1], tmp_tab[i]
    #     p.val = tmp_tab[i]
    #     p = p.next
    #     heapify(tmp_tab, 0, i - 1)
    for i in range(k, 0, -1):
        tmp_tab[i], tmp_tab[0] = tmp_tab[0], tmp_tab[i]
        q.val = tmp_tab[i]
        q = q.next
        heapify(tmp_tab, 0, i - 1)
    q.val = tmp_tab[0]
    return first


if __name__ == '__main__':
    # p = Node()
    # p.val = 7
    # q = p
    # q.next = Node()
    # q = q.next
    # q.val = 2
    # q.next = Node()
    # q = q.next
    # q.val = 1
    # q.next = Node()
    # q = q.next
    # q.val = 3
    # q.next = Node()
    # q = q.next
    # q.val = 4
    # q.next = Node()
    # q = q.next
    # q.val = 8
    # q.next = Node()
    # q = q.next
    # q.val = 6
    # q.next = Node()
    # q = q.next
    # q.val = 0
    # q.next = Node()
    # q = q.next
    # q.val = 5
    # p = Node()
    # p.val = 1
    # q = p
    # q.next = Node()
    # q = q.next
    # q.val = 3
    # q.next = Node()
    # q = q.next
    # q.val = 4
    # q.next = Node()
    # q = q.next
    # q.val = 2
    # q.next = Node()
    # q = q.next
    # q.val = 5
    # q.next = Node()
    # q = q.next
    # q.val = 7
    # q.next = Node()
    # q = q.next
    # q.val = 6
    # q.next = Node()
    # q = q.next
    # q.val = 8
    # q.next = Node()
    # q = q.next
    # q.val = 9
    # p = insSort_v3(p)
    # p = SortH(p, 1)
    # printer(p)
    # p = creator()
    # # printer(p)
    # print('-')
    # p = heap_sort(p, 2)
    # n = len_ods(p)
    # printer(jump(p, 5, find_middle(p, n), n)[0])
    # start = time.time()
    # bubbleSort(p)
    # end = time.time()
    # print(end-start)
    # p = bubbleSort(p)
    # p = swap(jump(p, 3), jump(p, 4), p)
    p2 = Node()
    p2.val = 897
    q = p2
    # tab = [0, 14, 0, 75, 60, 53, 101, 133, 78, 131, 78, 130, 140]
    # tab = [58, 31, 28, 47, 98, 9, 35, 8, 30, 36, 41, 10, 61, 6, 81, 53, 76, 67, 58, 81, 84, 3, 88, 27]
    tab = [262, 1657, 1881, 2064, 177, 908, 1867, 2600, 340, 1390, 767, 2296, 1931, 772, 2972, 1904, 2457, 1402, 2835,
           2720]
    for i in tab:
        z = Node()
        z.val = i
        q.next = z
        q = q.next

    # p = creator()
    print('-')
    p = heap_sort(p2, 10)
    printer(p)
    # tab = [1,4,3,2,0]
    # heapify(tab,0,5,0)
    # print(tab)



#  kolejne gorze

# # heap heap hurra
#
# def left(i): return 2 * i + 1
#
#
# def right(i): return 2 * i + 2
#
#
# def parent(i): return (i - 1) // 2
#
#
# # 4 główne opcje problemu
# # 1) ...,i,max,...
# # 2) ...,i,...,max,...
# # 3) i,max,...
# # 4) i,...,max,...
# # rozwiązanie: sprawdzamy przy pomocy if, czy nie musimy zamienić dwóch kolejnych wyrazów, jeśli tak, zamiana odbywa
# # się nieco inaczej
# # dodatkowo po wykonaniu zamiany sprawdzamy czy nie zamienialiśmy elementu który w liście jest na pozycji 0
# # możemy to stwierdzić patrząc na to jaką wartość będzie miał element 1 w krotce która w liście jest wcześniej
# # jeżli tak zwracamy nowy wskaźnik na początek listy, jeżeli nie, to zwracamy normalne p
#
# def swap(i_nodes, max_nodes, p):
#     if i_nodes[1] == max_nodes[0]:
#         tmp_max = max_nodes[1].next
#         tmp_elem = i_nodes[1]
#         i_nodes[0].next = max_nodes[1]
#         max_nodes[1].next = tmp_elem
#         tmp_elem.next = tmp_max
#         if i_nodes[0].val is not None:
#             return p
#         else:
#             return max_nodes[1]
#
#     tmp_i = i_nodes[1].next
#     tmp_max = max_nodes[1].next
#     i_nodes[0].next = max_nodes[1]
#     max_nodes[1].next = tmp_i
#     max_nodes[0].next = i_nodes[1]
#     i_nodes[1].next = tmp_max
#     if i_nodes[0].val is not None:
#         return p
#     else:
#         return max_nodes[1]
#
#
# def jump(p, i):
#     if i == 0:
#         return Node(), p
#     for _ in range(i - 1):
#         p = p.next
#     return p, p.next
#
#
# def heapify(p, n, i, k):
#     left_index = left(i)
#     right_index = right(i)
#     max_ind = i
#     max_nodes = jump(p, i)
#     i_nodes = max_nodes
#     if left_index < n:# and abs(i - left_index) <= k:  # musi być spełnione, bo skok między dwoma elementami nie jest większa niż k
#         left_nodes = jump(p, left_index)
#         if left_nodes[1].val > max_nodes[1].val:
#             max_ind = left_index
#             max_nodes = left_nodes
#     if right_index < n:# and abs(i - right_index) <= k :
#         right_nodes = jump(p, right_index)
#         if right_nodes[1].val > max_nodes[1].val:
#             max_ind = right_index
#             max_nodes = right_nodes
#     if max_ind != i:
#         # printer(p)
#         p = swap(i_nodes, max_nodes, p)
#         # printer(p)
#         heapify(p, n, max_ind, k)
#         # printer(p)
#     return p
#
#
# def build_heap(p, n, k):
#     for i in range(parent(n - 1), -1, -1):
#         p = heapify(p, n, i, k)
#     return p
#
#
# def len_ods(p):
#     counter = 0
#     while p is not None:
#         p = p.next
#         counter += 1
#     return counter
#
#
# def reversing(first):
#     p = first
#     while p.next is not None:
#         tmp = p.next
#         p.next = tmp.next
#         tmp.next = first
#         first = tmp
#     return first
#
#
# def heap_sort(p, k):
#     n = len_ods(p)
#     # p = reversing(p)
#     p = build_heap(p, n, k)
#
#     for i in range(n - 1, 0, -1):
#         p = swap((Node(), p), jump(p, i), p)
#         p = heapify(p, i, 0, k)
#     # p = reversing(p)
#     return p

# /////////////////////////

# def left(i): return 2 * i + 1
#
#
# def right(i): return 2 * i + 2
#
#
# def parent(i): return (i - 1) // 2
#
#
# def heapify(tab, n, i, k):
#     l = left(i)
#     r = right(i)
#     max_val = i
#     if n > l and tab[l] > tab[max_val]:
#         max_val = l
#     if n > r and tab[r] > tab[max_val]:
#         max_val = r
#     if max_val != i:
#         tab[max_val], tab[i] = tab[i], tab[max_val]
#         heapify(tab, n, max_val, k)
#
#
# def build_heap(tab, n, k):
#     for i in range(parent(n - 1), -1, -1):
#         heapify(tab, n, i, k)
#
#
# def chnager_to_table(p, tab):
#     counter = 0
#     first = p
#     while p is not None:
#         p = p.next
#         counter += 1
#     tab = [None for _ in range(counter)]
#     for i in range(counter):
#         tab[i] = first.val
#         first = first.next
#
#     return tab, counter
#
#
# def changer_to_linked_list(tab, n, p):
#     first = p
#     for i in range(n):
#         p.val = tab[i]
#         p = p.next
#     return first
#
#
# def heap_sort(p, k):
#     tab = [None for _ in range(1000000)]
#     tab, n = chnager_to_table(p, tab)
#     build_heap(tab, n, k)
#     for i in range(n - 1, 0, -1):
#         tab[0], tab[i] = tab[i], tab[0]
#         heapify(tab, i, 0, k)
#     p = changer_to_linked_list(tab, n, p)
#     return p

# ////
#
# def left(i): return 2 * i + 1
#
#
# def right(i): return 2 * i + 2
#
#
# def parent(i): return (i - 1) // 2
#
#
#
# def heapify(tab, i, k, j):
#     l = left(i)
#     r = right(i)
#     max_val = i
#     if k >= l and tab[j + l] > tab[j + max_val]:
#         max_val = l
#     if k >= r and tab[j + r] > tab[j + max_val]:
#         max_val = r
#     if max_val != i:
#         tab[max_val + j], tab[i + j] = tab[i + j], tab[max_val + j]
#         heapify(tab, max_val, k, j)
#
#
# def build_heap(tab, k, j):
#     for i in range(parent(k), - 1, -1):
#         heapify(tab, i, k, j)
#
#
# #
# # def len_ods(p):
# #     counter = 0
# #     while p is not None:
# #         p = p.next
# #         counter += 1
# #     return counter
# #
# #
# # def find_middle(p, n):
# #     for i in range(n // 2):
# #         p = p.next
# #     return p
# #
# #
# # def reversing(first):
# #     p = first
# #     while p.next is not None:
# #         tmp = p.next
# #         p.next = tmp.next
# #         tmp.next = first
# #         first = tmp
# #     return first
#
#
# def chnager_to_table(p, tab):
#     i = 0
#     while p is not None:
#         tab[i] = p.val
#         p = p.next
#         i += 1
#
#     return tab
#
#
# def changer_to_linked_list(tab, p, start):
#     i = start
#     while p is not None:
#         p.val = tab[i]
#         p = p.next
#         i += 1
#
#
# def len_of_linked_list(p):
#     counter = 0
#     while p is not None:
#         counter += 1
#         p = p.next
#     return counter
#
#
# def heap_sort(p, k):
#     n = len_of_linked_list(p)
#     tab = [None for _ in range(n)]
#     tab = chnager_to_table(p, tab)
#     first = p
#     for j in range(n - k):
#         build_heap(tab, k, j)
#         for i in range(k, 0, -1):
#             tab[j], tab[i + j] = tab[i + j], tab[j]
#             heapify(tab, 0, i-1, j)
#         p.val = tab[j]
#         p = p.next
#     changer_to_linked_list(tab, p, n - k)
#
#     return first
#

# ///

# # 4 główne opcje problemu
# # 1) ...,i,max,...
# # 2) ...,i,...,max,...
# # 3) i,max,...
# # 4) i,...,max,...
# # rozwiązanie: sprawdzamy przy pomocy if, czy nie musimy zamienić dwóch kolejnych wyrazów, jeśli tak, zamiana odbywa
# # się nieco inaczej
# # dodatkowo po wykonaniu zamiany sprawdzamy czy nie zamienialiśmy elementu który w liście jest na pozycji 0
# # możemy to stwierdzić patrząc na to jaką wartość będzie miał element 1 w krotce która w liście jest wcześniej
# # jeżli tak zwracamy nowy wskaźnik na początek listy, jeżeli nie, to zwracamy normalne p
#
# def swap(i_nodes, max_nodes, p):
#     if i_nodes[1] == max_nodes[0]:
#         tmp_max = max_nodes[1].next
#         tmp_elem = i_nodes[1]
#         i_nodes[0].next = max_nodes[1]
#         max_nodes[1].next = tmp_elem
#         tmp_elem.next = tmp_max
#         if i_nodes[0].val is not None:
#             return p
#         else:
#             return max_nodes[1]
#
#     tmp_i = i_nodes[1].next
#     tmp_max = max_nodes[1].next
#     i_nodes[0].next = max_nodes[1]
#     max_nodes[1].next = tmp_i
#     max_nodes[0].next = i_nodes[1]
#     i_nodes[1].next = tmp_max
#     if i_nodes[0].val is not None:
#         return p
#     else:
#         return max_nodes[1]
#
#
# # def jump(p, i, p2, n):
# #     if i == 0:
# #         return Node(), p
# #     if i <= n // 2:
# #         for _ in range(i - 1):
# #             p = p.next
# #         return p, p.next
# #     for _ in range((i - n // 2) - 1):
# #         p2 = p2.next
# #     return p2, p2.next
# #     # if i <= 1:
# #     #     return p, p.next
# #     # else:
# #     #     return jump(p.next, i - 1)
#
# def jump(p, i, p2, n):
#     if i == 0:
#         return Node(), p
#     for _ in range(i - 1):
#         p = p.next
#     return p, p.next
#
#
# # def heapify(tab, i, k, start, n):
# #     l = left(i)
# #     r = right(i)
# #     max_val = i
# #     if l + start < n and tab[start + l] < tab[start + max_val]:
# #         max_val = l
# #     if r + start < n and tab[start + r] < tab[start + max_val]:
# #         max_val = r
# #     if max_val != i:
# #         tab[max_val + start], tab[i + start] = tab[i + start], tab[max_val + start]
# #         heapify(tab, max_val, k, start, n)
#
#
# def build_heap(tab, k, j, n):
#     for i in range(parent(k), - 1, -1):
#         heapify(tab, i, k, j, n)
#
#
# def reversed_heapify(tab, i, k, start, n):
#     l = left(i)
#     r = right(i)
#     max_val = i
#     if l + start < n and tab[start + l] > tab[start + max_val]:
#         max_val = l
#     if r + start < n and tab[start + r] > tab[start + max_val]:
#         max_val = r
#     if max_val != i:
#         tab[max_val + start], tab[i + start] = tab[i + start], tab[max_val + start]
#         reversed_heapify(tab, max_val, k, start, n)
#
#
# #
# # def len_ods(p):
# #     counter = 0
# #     while p is not None:
# #         p = p.next
# #         counter += 1
# #     return counter
# #
# #
# # def find_middle(p, n):
# #     for i in range(n // 2):
# #         p = p.next
# #     return p
# #
# #
# # def reversing(first):
# #     p = first
# #     while p.next is not None:
# #         tmp = p.next
# #         p.next = tmp.next
# #         tmp.next = first
# #         first = tmp
# #     return first
#
#
# def chnager_to_table(p, tab):
#     i = 0
#     while p is not None:
#         tab[i] = p.val
#         p = p.next
#         i += 1
#
#     return tab
# def chnager_to_table(p, tab, n):
#     for i in range(n):
#         tab[i] = p.val
#         p = p.next
#         i += 1
#
#     return tab, p

# opcja tyćkę gorsza


# def left(i): return 2 * i + 1
#
#
# def right(i): return 2 * i + 2
#
#
# def parent(i): return (i - 1) // 2
#
#
# def len_of_linked_list(p):
#     counter = 0
#     while p is not None:
#         counter += 1
#         p = p.next
#     return counter
#
#
# def build_heap(tab, k):
#     for i in range(parent(k), - 1, -1):
#         heapify(tab, i, k)
#
#
# def heapify(tab, i, k):
#     l = left(i)
#     r = right(i)
#     max_val = i
#     if l <= k and tab[l] < tab[max_val]:
#         max_val = l
#     if r <= k and tab[r] < tab[max_val]:
#         max_val = r
#     if max_val != i:
#         tab[max_val], tab[i] = tab[i], tab[max_val]
#         heapify(tab, max_val, k)
#
#
# def changer(tab, k):
#     max = tab[0]
#     tab[0] = tab[k]
#     heapify(tab, 0, k)
#     return max
#
#
# def increase(tab, i, val):
#     tab[i] = val
#     while i > 0 and tab[parent(i)] > tab[i]:
#         tab[parent(i)], tab[i] = tab[i], tab[parent(i)]
#         i = parent(i)
#
#
# def chnager_to_table(p, tab, n):
#     for i in range(n):
#         tab[i] = p.val
#         p = p.next
#         i += 1
#
#     return tab, p

# def heap_sort(p, k):
#     n = len_of_linked_list(p)
#     if k >= n:
#         k = n - 1
#     tab = [None for _ in range(n)]
#     tab = chnager_to_table(p, tab)
#     tmp_tab = [tab[i] for i in range(k + 1)]
#     first = p
#     build_heap(tmp_tab, k)
#     for i in range(n - k - 1):
#         p.val = changer(tmp_tab, k)
#         p = p.next
#         increase(tmp_tab, k, tab[k + i + 1])
#
#
#     # for i in range(n - 1, n - k - 1, -1):
#     #     tmp_tab[i], tmp_tab[n - k - 1] = tmp_tab[n - k - 1], tmp_tab[i]
#     #     p.val = tmp_tab[i]
#     #     p = p.next
#     #     heapify(tmp_tab, 0, i - 1)
#     for i in range(k, 0, -1):
#         tmp_tab[i], tmp_tab[0] = tmp_tab[0], tmp_tab[i]
#         p.val = tmp_tab[i]
#         p = p.next
#         heapify(tmp_tab, 0, i - 1)
#     p.val = tmp_tab[0]
#     return first