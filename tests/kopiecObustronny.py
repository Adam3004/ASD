def left(x): return 2 * x + 1


def right(x): return 2 * x + 2


def parent(x): return (x - 1) // 2


def buildHeapMin(L, n):
    for i in range(parent(n - 1), -1, -1):
        heapify_min(L, n, i)


def buildHeapMax(L, n):
    for i in range(parent(n - 1), -1, -1):
        heapify_max(L, n, i)


def heapify_min(L, n, i):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and L[max_ind] < L[l]:
        max_ind = l
    if r < n and L[max_ind] < L[r]:
        max_ind = r
    if max_ind != i:
        L[i], L[max_ind] = L[max_ind], L[i]
        heapify_min(L, n, max_ind)


def heapify_max(L, n, i):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and L[max_ind] > L[l]:
        max_ind = l
    if r < n and L[max_ind] > L[r]:
        max_ind = r
    if max_ind != i:
        L[i], L[max_ind] = L[max_ind], L[i]
        heapify_max(L, n, max_ind)


def heapSortMin(L):
    n = len(L)
    buildHeapMin(L, n)
    for i in range(n - 1, 0, -1):
        L[i], L[0] = L[0], L[i]
        heapify_min(L, i, 0)
    return L


def heapSortMax(L):
    n = len(L)
    buildHeapMax(L, n)
    for i in range(n - 1, 0, -1):
        L[i], L[0] = L[0], L[i]
        heapify_max(L, i, 0)
    return L


def findIndexInHeap(L, val, Pom, n):
    for i in range(n - 1, -1, -1):
        if L[i] == val and not Pom[i]:
            Pom[i] = True
            return i


def createHeapClassMin(L_min, L_max):
    n = len(L_min)
    L = [None for _ in range(n)]
    Pom = [False for _ in range(n)]
    for i in range(n):
        L[i] = (L_min[i], findIndexInHeap(L_max, L_min[i], Pom, n))
    return L


def createHeapClassMax(L_min, L_max):
    n = len(L_max)
    L = [None for _ in range(n)]
    Pom = [False for _ in range(n)]
    for i in range(n):
        L[i] = (L_max[i], findIndexInHeap(L_min, L_max[i], Pom, n))
    return L


def findIndexInHeapRep(L, val, Pom, n):
    for i in range(n - 1, -1, -1):
        if L[i][0] == val and not Pom[i]:
            Pom[i] = True
            return i


def createHeapClassMinRepair(L_min, L_max):
    n = len(L_min)
    L = [None for _ in range(n)]
    Pom = [False for _ in range(n)]
    for i in range(n):
        L[i] = (L_min[i][0], findIndexInHeapRep(L_max, L_min[i][0], Pom, n))
    return L


def createHeapClassMaxRepair(L_min, L_max):
    n = len(L_max)
    L = [None for _ in range(n)]
    Pom = [False for _ in range(n)]
    for i in range(n):
        L[i] = (L_max[i][0], findIndexInHeapRep(L_min, L_max[i][0], Pom, n))
    return L


def repairHeapMin(L, i, L_max):
    p = parent(i)
    while p >= 0 and L[p] > L[i]:
        L[p], L[i] = L[i], L[p]
        L_max[i] = (L_max[i][0], p)
        L_max[p] = (L_max[p][0], i)
        i = p
        p = parent(i)
    L[i] = (L[i][0], len(L) - i - 1)


def repairHeapMax(L, i, L_min):
    p = parent(i)
    while p >= 0 and L[p][0] < L[i][0]:
        L_min[L[i][1]] = (L_min[L[i][1]][0], p)
        L_min[L[p][1]] = (L_min[L[p][1]][0], i)
        L[p], L[i] = L[i], L[p]
        i = p
        p = parent(i)
    L[i] = (L[i][0], len(L) - i - 1)

def poperMin(L_min, i):
    L_min[i], L_min[-1] = L_min[-1], L_min[i]
    L.pop()
    heapify_min(L_min,len(L_min))

class Heaps:

    def __init__(self, L):
        P = L.copy()
        self.leng = len(L)
        self.L_min = heapSortMin(P)
        self.L_max = heapSortMax(L.copy())
        self.heap_min = createHeapClassMin(self.L_min, self.L_max)
        self.heap_max = createHeapClassMax(self.L_min, self.L_max)

    def add_elem(self, val):
        self.leng += 1
        self.heap_min.append((val, -1))
        repairHeapMin(self.heap_min, self.leng - 1, self.heap_max)
        self.heap_max.append((val, -1))
        repairHeapMax(self.heap_max, self.leng - 1, self.heap_min)

    def return_min(self):
        return self.heap_min[0]

    def return_max(self):
        return self.heap_max[0]

    def pop_max(self):
        pass



if __name__ == '__main__':
    L = [6, 5, 1, 4, 3, 2, 7, 0]
    heap = Heaps(L)
    print(heap.heap_max)
    heap.add_elem(8)
    print(heap.heap_min)
    print(heap.heap_max)
