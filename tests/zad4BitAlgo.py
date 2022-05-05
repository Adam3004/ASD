def counting(L, k):
    n = len(L)
    C = [0 for _ in range(k + 1)]
    for i in range(n):
        C[L[i]] += 1
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    return C


class Counter:
    def __init__(self, L, k):
        self.L = counting(L, k)

    def count_num_in_range(self, a, b):
        if a >= 1:
            return self.L[b] - self.L[a - 1]
        return self.L[b]


L = [0, 1, 5, 2, 3, 3, 2, 2, 3, 3, 3, 2, 2, 2, 1]
Counter1 = Counter(L, 5)
print(Counter1.L)
print(Counter1.count_num_in_range(2, 3))
