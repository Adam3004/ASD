# def binary_search(L, l, r, elem):
#     val = elem[0]
#     while l <= r:
#         mid = (l + r) // 2
#         if L[mid][0] == val:
#             L.insert(mid, elem)
#             return
#         elif L[mid][0] < val:
#             r = mid - 1
#         else:
#             l = mid + 1
#     L.insert(r + 1, elem)
#
#
# class PriorityQueue:
#     def __init__(self):
#         self.L = []
#
#     def __add__(self, elem):
#         if len(self.L) == 0:
#             self.L.append(elem)
#         elif len(self.L) == 1:
#             if self.L[0][0] > elem[0]:
#                 self.L.append(elem)
#             else:
#                 self.L.insert(0, elem)
#         else:
#             binary_search(self.L, 0, len(self.L) - 1, elem)
#
#     def __get__(self):
#         elem = self.L[0]
#         self.L.pop(0)
#         return elem
#
#     def __str__(self):
#         out = str(self.L)
#         return out
#
#
# def plan(T):
#     capacity = T[0]
#     Out = [0]
#     n = len(T)
#     actual_value = 0
#     pr_queue = PriorityQueue()
#     while actual_value + capacity < n - 1:
#         for i in range(actual_value + 1, actual_value + capacity + 1):
#             if i >= n:
#                 break
#             if T[i] != 0:
#                 pr_queue.__add__((T[i], i))
#         actual_value += capacity
#         elem = pr_queue.__get__()
#         capacity = elem[0]
#         Out.append(elem[1])
#     return sorted(Out)