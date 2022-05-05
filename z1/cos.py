def left(i): return 2 * i + 1


def right(i): return 2 * i + 2


def parent(i): return (i - 1) // 2


def heapify(tab, n, i, k):
    l = left(i)
    r = right(i)
    max_val = i
    if n > l and tab[l] > tab[max_val]:
        max_val = l
    if n > r and tab[r] > tab[max_val]:
        max_val = r
    if max_val != i:
        tab[max_val], tab[i] = tab[i], tab[max_val]
        heapify(tab, n, max_val, k)


def build_heap(tab, n, k):
    for i in range(parent(n - 1), -1, -1):
        heapify(tab, n, i, k)


def chnager_to_table(p, tab):
    counter = 0
    first = p
    while p is not None:
        p = p.next
        counter += 1
    tab = [None for _ in range(counter)]
    for i in range(counter):
        tab[i] = first.val
        first = first.next

    return tab, counter


def changer_to_linked_list(tab, n, p):
    first = p
    for i in range(n):
        p.val = tab[i]
        p = p.next
    return first


def heap_sort(k):
    tab = [1, 0, 3, 2, 4, 6, 5]
    n = 7
    # tab, n = chnager_to_table(p, tab)
    build_heap(tab, n, k)
    for i in range(n - 1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        heapify(tab, i, 0, k)
    print(tab)
    # p = changer_to_linked_list(tab, n, p)
    # return p


l = [0, 1, 2, 3, 4, 5, 6]
print(l[2:5])
