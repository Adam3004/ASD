# #  (h, a, b, w)
# # jeżeli p-w>0 i a>poprzednie b to bierzemy budynek lub nie
# # f(n) = max_val
# # f(i,p,val)=max(
# # opcja 1 = 0 lub f(i+1,p-building cost,value+building value), jeżeli p-w>0 i a>poprzednie b to bierzemy budynek lub nie
# # opcja 2 = f(i+1,p,value)
# # )
#
#
# # ListOfBuildings = [(2, 0, 5, 3), (5, 3, 4, 4), (4, 5, 6, 7), (1, 1, 12, 1)]
# # p = 7
# # ListOfBuildings = [(2, 1, 5, 3), (3, 7, 9, 2), (2, 8, 11, 1)]
# # p = 5
# # T = [(3, 1, 2, 7), (2, 1, 7, 19), (3, 1, 4, 3), (2, 5, 6, 11), (3, 1, 10, 3)]
# # p = 40
# T = [(2, 1, 5, 3), (3, 7, 9, 2), (2, 8, 11, 1)]
# p = 5
# ListOfBuildings = T.copy()
# ListOfBuildings.sort(key=lambda x: (x[1], x[2]))
# print(ListOfBuildings)
#
# n = len(ListOfBuildings)
#
#
# def get_value(Building):
#     return (Building[2] - Building[1]) * Building[0]
#
#
# # max value for each building
# ValuesList = [-1 for _ in range(n)]
# ChoosenBuildings = [-1 for _ in range(n)]
#
#
# def find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i, p, prev_b, value):
#     n = len(ListOfBuildings)
#     if i >= n:
#         return value
#     # if ValuesList[i] != -1:
#     #     return ValuesList[i]
#     Building = ListOfBuildings[i]
#     taken = -1
#     if p - Building[3] >= 0 and Building[1] > prev_b:
#         taken = find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i + 1, p - Building[3], Building[2],
#                           value + get_value(Building))
#     # notTaken = -1
#     # if i < n:
#     #     notTaken = ValuesList[i]
#     # if notTaken == -1:
#     #     notTaken = find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i + 1, p, prev_b, value)
#     notTaken = find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i + 1, p, prev_b, value)
#     if notTaken > taken:
#         if notTaken > ValuesList[i]:
#             ValuesList[i] = notTaken
#             ChoosenBuildings[i] = -1
#     else:
#         if taken > ValuesList[i]:
#             ValuesList[i] = taken
#             ChoosenBuildings[i] = i
#     return ValuesList[i]
#
#
# def cleaner(ChoosenBuildings, ListOfBuildings, T):
#     ChoosenBuildings = [elem for elem in ChoosenBuildings if elem != -1]
#     Tmp = []
#     for elem in ChoosenBuildings:
#         Tmp.append(T.index(ListOfBuildings[elem]))
#     return Tmp
#
#
# print(find_best(ListOfBuildings, ValuesList, ChoosenBuildings, 0, p, ListOfBuildings[0][1] - 1, 0))
# ChoosenBuildings = cleaner(ChoosenBuildings, ListOfBuildings, T)
# print(ChoosenBuildings)


# pomysł 2
# T = [(3, 1, 2, 7), (2, 1, 7, 19), (3, 1, 4, 3), (2, 5, 6, 11), (3, 1, 10, 3)]
# p = 40
# # T = [(2, 1, 5, 3), (3, 7, 9, 2), (2, 8, 11, 1)]
# # p = 5
# ListOfBuildings = T.copy()
# ListOfBuildings.sort(key=lambda x: (x[1], x[2]))
#
# print(T)
# print(ListOfBuildings)
#
#
# def get_value(Building):
#     return (Building[2] - Building[1]) * Building[0]
#
#
# # def v2(ListOfBuildings, p):
# #     n = len(ListOfBuildings)
# #     F = [[(0, -1, []) for _ in range(p + 1)] for _ in range(n)]
# #     val0 = get_value(ListOfBuildings[0])
# #     for b in range(ListOfBuildings[0][3], p + 1):
# #         F[0][b] = (val0, 0, [0])
# #     for i in range(1, n):
# #         for b in range(p + 1):
# #             F[i][b] = F[i - 1][b]
# #             Building = ListOfBuildings[i]
# #             if b - Building[3] >= 0 and Building[1] > F[i][b - Building[3]][1]:
# #                 if F[i][b][0] < F[i - 1][b - Building[3]][0] + get_value(Building):
# #                     Tmp = (F[i - 1][b - Building[3]][2]).copy()
# #                     Tmp.append(i)
# #                     F[i][b] = (F[i - 1][b - Building[3]][0] + get_value(Building), Building[2], Tmp)
# #             elif b - Building[3] >= 0 and b > 0:
# #                 if F[i][b - 1][0] > F[i][b][0]:
# #                     F[i][b] = F[i][b - 1]
# #
# #     # for i in range(n):
# #     #     print(F[i])
# #     # print(F[n - 1][p])
# #     return F[n - 1][p][2]
#
# def v3(ListOfBuildings, p):
#     n = len(ListOfBuildings)
#     F = [[(0, -1) for _ in range(p + 1)] for _ in range(n)]
#     val0 = get_value(ListOfBuildings[0])
#     for b in range(ListOfBuildings[0][3], p + 1):
#         F[0][b] = (val0, ListOfBuildings[0][2])
#     for i in range(1, n):
#         Building = ListOfBuildings[i]
#         for b in range(p + 1):
#             F[i][b] = F[i - 1][b]
#             if b - Building[3] >= 0 and Building[1] > F[i - 1][b - Building[3]][1]:
#                 if F[i][b][0] < F[i - 1][b - Building[3]][0] + get_value(Building):
#                     F[i][b] = (F[i - 1][b - Building[3]][0] + get_value(Building), Building[2])
#             # elif b - Building[3] >= 0 and b > 0:
#             #     if F[i][b - 1][0] > F[i][b][0]:
#             #         F[i][b] = F[i][b - 1]
#     #
#     # for i in range(n):
#     #     print(F[i])
#     # print(F[n - 1][p])
#     maxval = max(F[n - 1])
#     # print(maxval)
#     return maxval, F
#
#
# def finder(F, ListOfBuildings, actual_val, last_b, last_b_index, B, f_ind, p):
#     if actual_val == 0:
#         return B
#     for i in range(last_b_index, -1, -1):
#         if ListOfBuildings[i][2] == last_b:
#             B.append(i)
#             last_b_index = i
#             searching_val = actual_val - get_value(ListOfBuildings[i])
#             found = False
#             while not found:
#                 for j in range(p + 1):
#                     if F[f_ind][j][0] == searching_val:
#                         last_b = F[f_ind][j][1]
#                         found = True
#                         break
#                 f_ind -= 1
#
#             return finder(F, ListOfBuildings, searching_val, last_b, last_b_index, B, f_ind, p)
#
#
# def cleaner(OutputList, ListOfBuildings, T):
#     Tmp = []
#     for elem in OutputList:
#         Tmp.append(T.index(ListOfBuildings[elem]))
#     return sorted(Tmp)
#
#
# maxval, F = v3(ListOfBuildings, p)
# B = finder(F, ListOfBuildings, maxval[0], maxval[1], len(ListOfBuildings) - 1, [], len(ListOfBuildings) - 1, p)
# B.reverse()
# B = cleaner(B, ListOfBuildings, T)
# print(B)
#
#
# def best_find(F, p, ListOfBuildings):
#     n = len(ListOfBuildings)
#     OutputList = []
#     for i in range(n - 1, 0, -1):
#         if F[i][p] != F[i - 1][p]:
#             OutputList.append(i)
#             while p > 0 and F[i][p] == F[i][p - 1]:
#                 p -= 1
#             if p > 0:
#                 p -= 1
#     if F[i][p][0] != 0:
#         OutputList.append(0)
#     # print(sorted(OutputList))
#     return OutputList
#
#
# def cleaner(OutputList, ListOfBuildings, T):
#     Tmp = []
#     for elem in OutputList:
#         Tmp.append(T.index(ListOfBuildings[elem]))
#     return sorted(Tmp)

# #
# # F = v3(ListOfBuildings, p)
# # print()
# # Output = best_find(F, p, ListOfBuildings)
# # print(cleaner(Output, ListOfBuildings, T))
# #
# # def find_best(ListOfBuildings, p):
# #     # F = v2(ListOfBuildings, p)
# #     # n = len(ListOfBuildings)
# #     # OutputList = []
# #     # next_b = -2
# #     # i = n - 1
# #     # while next_b != -1:
# #     #     next_b = F[i][p][1]
# #     #     OutputList.append(next_b)
# #     #     if i != next_b:
# #     #         i = next_b
# #     #     while p > 0 and F[i][p] == F[i][p - 1]:
# #     #         p -= 1
# #     #     p -= 1
# #     # return OutputList
# #
# #     #     v2
# #     F = v2(ListOfBuildings, p)
# #     n = len(ListOfBuildings)
# #     OutputList = []
# #     for i in range(n - 1, 0, -1):
# #         if F[i][p] != F[i - 1][p]:
# #             OutputList.append(i)
# #             i -= 1
# #             while p > 0 and F[i][p] == F[i][p - 1]:
# #                 p -= 1
# #             if p > 0:
# #                 p -= 1
# #     if F[i][p][0] != -1:
# #         OutputList.append(0)
# #     print(sorted(OutputList))
# #     return OutputList
# #
# #
# # def cleaner(OutputList, ListOfBuildings, T):
# #     Tmp = []
# #     for elem in OutputList:
# #         Tmp.append(T.index(ListOfBuildings[elem]))
# #     return sorted(Tmp)
# #
# # n = len(ListOfBuildings)
# # print(cleaner(v2(ListOfBuildings, p), ListOfBuildings, T))
# a

# v4
# T = [(3, 1, 2, 7), (2, 1, 7, 19), (3, 1, 4, 3), (2, 5, 6, 11), (3, 1, 10, 3)]
# p = 40


# import math
#
# T = [(2, 1, 5, 3), (3, 7, 9, 2), (2, 8, 11, 1)]
# p = 5


# ListOfBuildings = T.copy()
# ListOfBuildings.sort(key=lambda x: (x[2], x[1]))
#
#
# print(T)
# print(ListOfBuildings)
#
#
# def get_value(Building):
#     return (Building[2] - Building[1]) * Building[0]
#
#
# n = len(ListOfBuildings)
# F = [[0 for _ in range(p + 1)] for _ in range(n)]  # max wartość dla danego pola
# B = [[-1 for _ in range(p + 1)] for _ in range(n)]  # prev b
# C = [[[] for _ in range(p + 1)] for _ in range(n)]
#
# val0 = get_value(ListOfBuildings[0])
# for b in range(ListOfBuildings[0][3], p + 1):
#     F[0][b] = val0
#     B[0][b] = ListOfBuildings[0][2]
#     C[0][b] = [0]
#
#
# def f(ListOfBuildings, F, B, i, b, C, prev_a):
#     if F[i][b] != 0 or i == 0:
#         if prev_a > ListOfBuildings[i][2]:
#             return F[i][b]
#         else:
#             return 0
#     taken = 0
#     if b - ListOfBuildings[i][3] >= 0 and prev_a > ListOfBuildings[i][2]:
#         taken = f(ListOfBuildings, F, B, i - 1, b - ListOfBuildings[i][3], C, ListOfBuildings[i][1]) + get_value(
#             ListOfBuildings[i])
#         if prev_a <= ListOfBuildings[i][2]:
#             taken = 0
#     notTaken = f(ListOfBuildings, F, B, i - 1, b, C, prev_a)
#     if taken > notTaken:
#         B[i][b] = ListOfBuildings[i][1]
#         F[i][b] = taken
#         Tmp = C[i - 1][b - ListOfBuildings[i][3]].copy()
#         Tmp.append(i)
#         C[i][b] = Tmp
#     elif notTaken == 0:
#         F[i][b] = notTaken
#         C[i][b] = []
#         B[i][b] = -1
#     else:
#         F[i][b] = notTaken
#         C[i][b] = C[i - 1][b]
#         B[i][b] = B[i - 1][b]
#     return F[i][b]
#
#
# f(ListOfBuildings, F, B, n - 1, p, C, math.inf)
# # for i in range(n):
# #     print(F[i])
# # print(10 * "_")
# # for i in range(n):
# #     print(B[i])
# # print(10 * "_")
# # for i in range(n):
# #     print(C[i])
#
#
# def cleaner(OutputList, ListOfBuildings, T):
#     Tmp = []
#     for elem in OutputList:
#         Tmp.append(T.index(ListOfBuildings[elem]))
#     return sorted(Tmp)
#
#
# print(cleaner(C[n - 1][p], ListOfBuildings, T))

#
# v5
#
# def get_value(Building):
#     return (Building[2] - Building[1]) * Building[0]
#
#
# def f(ListOfBuildings, F, i, b, C, prev_a):
#     if F[i][b] != 0 and prev_a > ListOfBuildings[i][2]:
#         return F[i][b]
#     if i == 0:
#         if prev_a > ListOfBuildings[i][2]:
#             return F[i][b]
#         else:
#             return 0
#     taken = 0
#     taken2 = 0
#     if b - ListOfBuildings[i][3] >= 0 and prev_a > ListOfBuildings[i][2]:
#         taken = f(ListOfBuildings, F, i - 1, b - ListOfBuildings[i][3], C, ListOfBuildings[i][1]) + get_value(
#             ListOfBuildings[i])
#         # if prev_a <= ListOfBuildings[i][2]:
#         #     taken = 0
#     if (b - ListOfBuildings[i][3] - ListOfBuildings[i][2]) >= 0:
#         taken2 = f(ListOfBuildings, F, i - 1, b - ListOfBuildings[i][3] - ListOfBuildings[i][2], C,
#                    ListOfBuildings[i][1]) + get_value(ListOfBuildings[i])
#     notTaken = f(ListOfBuildings, F, i - 1, b, C, prev_a)
#
#     if taken > notTaken:
#         if taken >= taken2:
#             F[i][b] = taken
#             Tmp = C[i - 1][b - ListOfBuildings[i][3]].copy()
#             Tmp.append(i)
#             C[i][b] = Tmp
#         else:
#             F[i][b] = taken2
#             Tmp = C[i - 1][b - ListOfBuildings[i][3] - ListOfBuildings[i][2]].copy()
#             Tmp.append(i)
#             C[i][b] = Tmp
#     elif notTaken == 0:
#         F[i][b] = notTaken
#         C[i][b] = []
#     else:
#         F[i][b] = notTaken
#         C[i][b] = C[i - 1][b]
#     return F[i][b]
#
#
# def cleaner(OutputList, ListOfBuildings, T):
#     Tmp = []
#     for elem in OutputList:
#         Tmp.append(T.index(ListOfBuildings[elem]))
#     return sorted(Tmp)
#
#
# def select_buildings(T, p):
#     ListOfBuildings = T.copy()
#     ListOfBuildings.sort(key=lambda x: (x[2], x[1]))
#     n = len(ListOfBuildings)
#     F = [[0 for _ in range(p + 1)] for _ in range(n)]  # max wartość dla danego pola
#     C = [[[] for _ in range(p + 1)] for _ in range(n)]  # wzięte budynki
#     val0 = get_value(ListOfBuildings[0])
#     for b in range(ListOfBuildings[0][3], p + 1):
#         F[0][b] = val0
#         C[0][b] = [0]
#     f(ListOfBuildings, F, n - 1, p, C, 10000000000)
#     print(ListOfBuildings)
#     print(10 * "_")
#     for i in range(n):
#         print(F[i])
#     print(10 * "_")
#     for i in range(n):
#         print(C[i])
#     return cleaner(C[n - 1][p], ListOfBuildings, T)
#
#
# print(select_buildings(T, p))
#

# v6
# class Building:
#     def __init__(self, h, a, b, w):
#         self.h = h
#         self.a = a
#         self.b = b
#         self.w = w
#
#     def get_value(self):
#         return int((self.b - self.a) * self.h)
#
#     def __str__(self):
#         out = str((self.h, self.a, self.b, self.w))
#         return out
#
#
# class BuildingsListClass:
#     def __init__(self, T):
#         self.ListOfBuildings = T.copy()
#         self.T = T
#
#     def initialize(self):
#         self.ListOfBuildings.sort(key=lambda x: (x[2], -x[1]))
#         self.ListOfBuildings = [Building(elem[0], elem[1], elem[2], elem[3]) for elem in self.ListOfBuildings]
#
#     def rebuild(self):
#         self.ListOfBuildings = [(elem.h, elem.a, elem.b, elem.w) for elem in self.ListOfBuildings]
#
#     def find_indexes_T(self, OutputList):
#         Tmp = []
#         for elem in OutputList:
#             Tmp.append(self.T.index(self.ListOfBuildings[elem]))
#         return sorted(Tmp)
#
#
# def f(ListOfBuildings, i, F, C, prev_a, b):
#     if i == 0:
#         if ListOfBuildings[i].b < prev_a:
#             return F[i][b]
#         else:
#             return 0
#     if F[i][b] != 0:
#         return F[i][b]
#     taken = 0
#     # t = 1
#     if b - ListOfBuildings[i].w > 0:
#         if ListOfBuildings[i].b < prev_a:
#             taken = f(ListOfBuildings, i - 1, F, C, ListOfBuildings[i].a, b - ListOfBuildings[i].w) + ListOfBuildings[
#                 i].get_value()
#         # else:
#         #     t = 2
#         #     while i - t > 0 and ListOfBuildings[i - t].b >= ListOfBuildings[i].a:
#         #         t += 1
#         #     if ListOfBuildings[i - t].b < ListOfBuildings[i].a:
#         #         taken = f(ListOfBuildings, i - t, F, C, ListOfBuildings[i].a, b - ListOfBuildings[i].w) + ListOfBuildings[
#         #             i].get_value()
#
#     notTaken = f(ListOfBuildings, i - 1, F, C, prev_a, b)
#     if taken > notTaken:
#         F[i][b] = taken
#         Tmp = C[i - 1][b - ListOfBuildings[i].w].copy()
#         Tmp.append(i)
#         C[i][b] = Tmp
#     elif notTaken == 0:
#         F[i][b] = notTaken
#         C[i][b] = []
#     else:
#         F[i][b] = notTaken
#         C[i][b] = C[i - 1][b]
#     return F[i][b]
#
#
# def select_buildings(T, p):
#     ListOfBuildings = BuildingsListClass(T)
#     # print(ListOfBuildings.ListOfBuildings)
#     ListOfBuildings.initialize()
#     n = len(ListOfBuildings.ListOfBuildings)
#     F = [[0 for _ in range(p + 1)] for _ in range(n)]  # max wartość dla danego pola
#     C = [[[] for _ in range(p + 1)] for _ in range(n)]  # wzięte budynki
#     val0 = ListOfBuildings.ListOfBuildings[0].get_value()
#     for b in range(ListOfBuildings.ListOfBuildings[0].w, p + 1):
#         F[0][b] = val0
#         C[0][b] = [0]
#     f(ListOfBuildings.ListOfBuildings, n - 1, F, C, 100000, p)
#     # print(10 * "_")
#     # for i in range(n):
#     #     print(F[i])
#     # print(10 * "_")
#     # for i in range(n):
#     #     print(C[i])
#     ListOfBuildings.rebuild()
#     # print(ListOfBuildings.T)
#     return ListOfBuildings.find_indexes_T(C[n - 1][p])
#
#
# # print(select_buildings(T, p))
#
# # ListOfBuildings = BuildingsListClass(T)
# # print(ListOfBuildings.ListOfBuildings)
# # ListOfBuildings.initialize()
# # ListOfBuildings.rebuild()
# # print(ListOfBuildings.ListOfBuildings)
#
# print(select_buildings(T, p))


# v7
# def get_value(Building):
#     return (Building[2] - Building[1]) * Building[0]
#
#
# # def find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i, p, prev_b, value):
# #     n = len(ListOfBuildings)
# #     if i >= n:
# #         return value
# #     # if ValuesList[i] != -1:
# #     #     return ValuesList[i]
# #     Building = ListOfBuildings[i]
# #     taken = 0
# #     if p - Building[3] >= 0 and Building[1] > prev_b:
# #         taken = find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i + 1, p - Building[3], Building[2],
# #                           value + get_value(Building))
# #     # notTaken = -1
# #     # if i < n:
# #     #     notTaken = ValuesList[i]
# #     # if notTaken == -1:
# #     #     notTaken = find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i + 1, p, prev_b, value)
# #     notTaken = find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i + 1, p, prev_b, value)
# #     if notTaken > taken:
# #         if notTaken > ValuesList[i]:
# #             ValuesList[i] = notTaken
# #             ChoosenBuildings[i] = -1
# #     else:
# #         if taken > ValuesList[i]:
# #             ValuesList[i] = taken
# #             ChoosenBuildings[i] = i
# #     return ValuesList[i]
#
# def find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i, p, prev_a):
#     if i == 0:
#         if ListOfBuildings[i][2] < prev_a:
#             return ValuesList[0][p]
#         else:
#             ValuesList[0][p] = 0
#             return 0
#
#     if ValuesList[i][p] != 0 and ListOfBuildings[i][2] < prev_a:
#         return ValuesList[i][p]
#
#     Building = ListOfBuildings[i]
#     taken = 0
#     if p - Building[3] >= 0 and Building[2] < prev_a:
#         taken = find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i - 1, p - Building[3], Building[1]) + get_value(
#             Building)
#     # notTaken = -1
#     # if i < n:
#     #     notTaken = ValuesList[i]
#     # if notTaken == -1:
#     #     notTaken = find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i + 1, p, prev_b, value)
#     notTaken = find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i - 1, p, prev_a)
#     ValuesList[i][p] = max(taken, notTaken)
#     # if notTaken == 0:
#     #     ChoosenBuildings[i] = -1
#     #
#     # elif notTaken > taken:
#     #     if notTaken > ValuesList[i][p]:
#     #         ValuesList[i][p] = notTaken
#     #         ChoosenBuildings[i] = -1
#     # else:
#     #     if taken > ValuesList[i][p]:
#     #         ValuesList[i][p] = taken
#     #         ChoosenBuildings[i] = i
#     return ValuesList[i][p]
#
#
# def find_answer(ListOfBuildings, ValuesList, n, p):
#     i = n - 1
#     Answer = []
#     while i > 0:
#         while i > 0 and ValuesList[i][p] == ValuesList[i - 1][p]:
#             i -= 1
#         if i > 0:
#             Answer.append(i)
#             p -= ListOfBuildings[i][3]
#             i -= 1
#         else:
#             if len(Answer) > 0:
#                 if ListOfBuildings[i][2] < ListOfBuildings[Answer[-1]][1]:
#                     Answer.append(0)
#             else:
#                 Answer.append(0)
#     if 0 not in Answer:
#         if len(Answer) > 0:
#             if ListOfBuildings[0][2] < ListOfBuildings[Answer[-1]][1]:
#                 Answer.append(0)
#         else:
#             Answer.append(0)
#     return Answer
#
#
# def select_buildings(T, p):
#     ListOfBuildings = T.copy()
#     ListOfBuildings.sort(key=lambda x: (x[2], x[1]))
#     n = len(ListOfBuildings)
#     ValuesList = [[0 for _ in range(p + 1)] for _ in range(n)]
#     ChoosenBuildings = [-1 for _ in range(n)]
#     val0 = get_value(ListOfBuildings[0])
#     for b in range(ListOfBuildings[0][3], p + 1):
#         ValuesList[0][b] = val0
#     # print(ListOfBuildings)
#     find_best(ListOfBuildings, ValuesList, ChoosenBuildings, n - 1, p, ListOfBuildings[n - 1][2] + 1)
#     for i in range(n):
#         print(ValuesList[i])
#     ChoosenBuildings = find_answer(ListOfBuildings, ValuesList, n, p)
#     # print(ChoosenBuildings)
#     return cleaner2(ChoosenBuildings, ListOfBuildings, T)
#
#
# def cleaner2(ChoosenBuildings, ListOfBuildings, T):
#     Tmp = []
#     for elem in ChoosenBuildings:
#         Tmp.append(T.index(ListOfBuildings[elem]))
#     return sorted(Tmp)
#
#
# def cleaner(ChoosenBuildings, ListOfBuildings, T):
#     ChoosenBuildings = [elem for elem in ChoosenBuildings if elem != -1]
#     Tmp = []
#     for elem in ChoosenBuildings:
#         Tmp.append(T.index(ListOfBuildings[elem]))
#     return Tmp

#
# v8
class Building:
    def __init__(self, h, a, b, w):
        self.h = h
        self.a = a
        self.b = b
        self.w = w

    def get_value(self):
        return int((self.b - self.a) * self.h)

    def __str__(self):
        out = str((self.h, self.a, self.b, self.w))
        return out


class BuildingsListClass:
    def __init__(self, T):
        self.BuildingsList = T.copy()
        self.T = T

    def initialize(self):
        self.BuildingsList.sort(key=lambda x: (x[2], x[1]))
        self.BuildingsList = [Building(elem[0], elem[1], elem[2], elem[3]) for elem in self.BuildingsList]

    def rebuild(self):
        self.BuildingsList = [(elem.h, elem.a, elem.b, elem.w) for elem in self.BuildingsList]

    def find_indexes_T(self, OutputList):
        Tmp = []
        for elem in OutputList:
            Tmp.append(self.T.index(self.BuildingsList[elem]))
        return sorted(Tmp)


def f(BuildingsList, i, F, C, prev_a, b):
    if i < 0:
        return 0
    # if i == 0:
    #     if ListOfBuildings[i].b < prev_a:
    #         return F[i][b]
    #     else:
    #         return 0
    if F[i][b] != 0 and BuildingsList[i].b < prev_a:
        return F[i][b]
    taken = 0
    while i >= 0 and BuildingsList[i].b >= prev_a:
        i -= 1
    if b - BuildingsList[i].w > 0 and BuildingsList[i].b < prev_a:
        taken = f(BuildingsList, i - 1, F, C, BuildingsList[i].a, b - BuildingsList[i].w) + BuildingsList[
            i].get_value()
    notTaken = f(BuildingsList, i - 1, F, C, prev_a, b)
    if taken > notTaken:
        F[i][b] = taken
        Tmp = C[i - 1][b - BuildingsList[i].w].copy()
        Tmp.append(i)
        C[i][b] = Tmp
    elif notTaken == 0:
        F[i][b] = notTaken
        C[i][b] = []
    else:
        F[i][b] = notTaken
        C[i][b] = C[i - 1][b]
    # if notTaken > taken:
    #     if notTaken > F[i][b]:
    #         F[i][b] = notTaken
    #         C[i][b] = C[i - 1][b]
    #     elif notTaken == 0:
    #         F[i][b] = notTaken
    #         C[i][b] = []
    # else:
    #     if taken > F[i][b]:
    #         F[i][b] = taken
    #         Tmp = C[i - 1][b - ListOfBuildings[i].w].copy()
    #         Tmp.append(i)
    #         C[i][b] = Tmp
    return F[i][b]


def select_buildings(T, p):
    BuildingsList = BuildingsListClass(T)
    Tmp = BuildingsList.BuildingsList
    Tmp.sort(key=lambda x: (x[2], x[1]))
    print(Tmp)
    BuildingsList.initialize()
    n = len(BuildingsList.BuildingsList)
    F = [[0 for _ in range(p + 1)] for _ in range(n)]  # max wartość dla danego pola
    C = [[[] for _ in range(p + 1)] for _ in range(n)]  # wzięte budynki
    val0 = BuildingsList.BuildingsList[0].get_value()
    for b in range(BuildingsList.BuildingsList[0].w, p + 1):
        F[0][b] = val0
        C[0][b] = [0]
    f(BuildingsList.BuildingsList, n - 1, F, C, 100000, p)
    # print(10 * "_")
    for i in range(n):
        print(F[i])
    print(10 * "_")
    print(F[n - 1][p])
    # for i in range(n):
    #     print(C[i])
    BuildingsList.rebuild()
    # print(F[n - 1][p])
    # print(ListOfBuildings.ListOfBuildings)
    # print(C[n - 1][p])
    return BuildingsList.find_indexes_T(C[n - 1][p])
    # return F[n - 1][p]


# T = [(3, 1, 2, 7), (2, 1, 7, 19), (3, 1, 4, 3), (2, 5, 6, 11), (3, 1, 10, 3)]
# p = 40

# import math
#
T = [(2, 1, 5, 3), (3, 7, 9, 2), (2, 8, 11, 1)]
p = 5
print(select_buildings(T, p))

# workspace final
# # Adam Misztal
# from zad4testy import runtests
#
#
# # pomysl 1
# # def get_value(Building):
# #     return (Building[2] - Building[1]) * Building[0]
# #
# #
# # # def find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i, p, prev_b, value):
# # #     n = len(ListOfBuildings)
# # #     if i >= n:
# # #         return value
# # #     # if ValuesList[i] != -1:
# # #     #     return ValuesList[i]
# # #     Building = ListOfBuildings[i]
# # #     taken = 0
# # #     if p - Building[3] >= 0 and Building[1] > prev_b:
# # #         taken = find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i + 1, p - Building[3], Building[2],
# # #                           value + get_value(Building))
# # #     # notTaken = -1
# # #     # if i < n:
# # #     #     notTaken = ValuesList[i]
# # #     # if notTaken == -1:
# # #     #     notTaken = find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i + 1, p, prev_b, value)
# # #     notTaken = find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i + 1, p, prev_b, value)
# # #     if notTaken > taken:
# # #         if notTaken > ValuesList[i]:
# # #             ValuesList[i] = notTaken
# # #             ChoosenBuildings[i] = -1
# # #     else:
# # #         if taken > ValuesList[i]:
# # #             ValuesList[i] = taken
# # #             ChoosenBuildings[i] = i
# # #     return ValuesList[i]
# #
# # def find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i, p, prev_a, value):
# #     n = len(ListOfBuildings)
# #     if i < 0:
# #         return value
# #     # if ValuesList[i] != -1:
# #     #     return ValuesList[i]
# #     Building = ListOfBuildings[i]
# #     taken = 0
# #     if p - Building[3] >= 0 and Building[2] < prev_a:
# #         taken = find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i - 1, p - Building[3], Building[1],
# #                           value + get_value(Building))
# #     # notTaken = -1
# #     # if i < n:
# #     #     notTaken = ValuesList[i]
# #     # if notTaken == -1:
# #     #     notTaken = find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i + 1, p, prev_b, value)
# #     notTaken = find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i - 1, p, prev_a, value)
# #     if notTaken > taken:
# #         if notTaken > ValuesList[i]:
# #             ValuesList[i] = notTaken
# #             ChoosenBuildings[i] = -1
# #     else:
# #         if taken > ValuesList[i]:
# #             ValuesList[i] = taken
# #             ChoosenBuildings[i] = i
# #     return ValuesList[i]
# #
# #
# # def select_buildings(T, p):
# #     ListOfBuildings = T.copy()
# #     ListOfBuildings.sort(key=lambda x: (x[2], x[1]))
# #     n = len(ListOfBuildings)
# #     ValuesList = [-1 for _ in range(n)]
# #     ChoosenBuildings = [-1 for _ in range(n)]
# #     find_best(ListOfBuildings, ValuesList, ChoosenBuildings, n - 1, p, ListOfBuildings[n-1][2] + 1, 0)
# #     return cleaner(ChoosenBuildings, ListOfBuildings, T)
# #
# #
# # def cleaner(ChoosenBuildings, ListOfBuildings, T):
# #     ChoosenBuildings = [elem for elem in ChoosenBuildings if elem != -1]
# #     Tmp = []
# #     for elem in ChoosenBuildings:
# #         Tmp.append(T.index(ListOfBuildings[elem]))
# #     return Tmp
# #
# #
# # # def select_buildings(T, p):
# # #     ListOfBuildings = T.copy()
# # #     ListOfBuildings.sort(key=lambda x: (x[1], x[2]))
# # #     n = len(ListOfBuildings)
# # #     ValuesList = [-1 for _ in range(n)]
# # #     ChoosenBuildings = [-1 for _ in range(n)]
# # #     find_best(ListOfBuildings, ValuesList, ChoosenBuildings, 0, p, ListOfBuildings[0][1] - 1, 0)
# # #     return cleaner(ChoosenBuildings, ListOfBuildings, T)
#
#
# # pomysl 2
# #
# # def get_value(Building):
# #     return (Building[2] - Building[1]) * Building[0]
# #
# #
# # def v2(ListOfBuildings, p):
# #     n = len(ListOfBuildings)
# #     F = [[(0, -1, []) for _ in range(p + 1)] for _ in range(n)]
# #     val0 = get_value(ListOfBuildings[0])
# #     for b in range(ListOfBuildings[0][3], p + 1):
# #         F[0][b] = (val0, 0, [0])
# #     for i in range(1, n):
# #         for b in range(p + 1):
# #             F[i][b] = F[i - 1][b]
# #             Building = ListOfBuildings[i]
# #             if b - Building[3] >= 0 and Building[1] > F[i-1][b - Building[3]][1]:
# #                 if F[i][b][0] < F[i - 1][b - Building[3]][0] + get_value(Building):
# #                     Tmp = (F[i - 1][b - Building[3]][2]).copy()
# #                     Tmp.append(i)
# #                     F[i][b] = (F[i - 1][b - Building[3]][0] + get_value(Building), Building[2], Tmp)
# #             elif b - Building[3] >= 0 and b > 0:
# #                 if F[i][b - 1][0] > F[i][b][0]:
# #                     F[i][b] = F[i][b - 1]
# #         for i in range(n):
# #             print(F[i])
# #         print(F[n - 1][p])
# #         print(10*'__')
# #     return F[n - 1][p][2]
# #
# #
# # def cleaner(OutputList, ListOfBuildings, T):
# #     Tmp = []
# #     for elem in OutputList:
# #         Tmp.append(T.index(ListOfBuildings[elem]))
# #     return sorted(Tmp)
# #
# #
# # def select_buildings(T, p):
# #     ListOfBuildings = T.copy()
# #     ListOfBuildings.sort(key=lambda x: (x[1], x[2]))
# #     return cleaner(v2(ListOfBuildings, p), ListOfBuildings, T)
#
#
# # pomysl 3
#
#
# # def get_value(Building):
# #     return (Building[2] - Building[1]) * Building[0]
# #
# #
# # def v3(ListOfBuildings, p):
# #     n = len(ListOfBuildings)
# #     F = [[(0, -1) for _ in range(p + 1)] for _ in range(n)]
# #     val0 = get_value(ListOfBuildings[0])
# #     for b in range(ListOfBuildings[0][3], p + 1):
# #         F[0][b] = (val0, ListOfBuildings[0][2])
# #     for i in range(1, n):
# #         Building = ListOfBuildings[i]
# #         for b in range(p + 1):
# #             F[i][b] = F[i - 1][b]
# #             if b - Building[3] >= 0 and Building[1] > F[i - 1][b - Building[3]][1]:
# #                 if F[i][b][0] < F[i - 1][b - Building[3]][0] + get_value(Building):
# #                     F[i][b] = (F[i - 1][b - Building[3]][0] + get_value(Building), Building[2])
# #     maxval = max(F[n - 1])
# #     return maxval, F
# #
# #
# # def finder(F, ListOfBuildings, actual_val, last_b, last_b_index, B, f_ind, p):
# #     if actual_val == 0:
# #         return B
# #     for i in range(last_b_index, -1, -1):
# #         if ListOfBuildings[i][2] == last_b:
# #             B.append(i)
# #             last_b_index = i
# #             searching_val = actual_val - get_value(ListOfBuildings[i])
# #             found = False
# #             while not found:
# #                 for j in range(p + 1):
# #                     if F[f_ind][j][0] == searching_val:
# #                         last_b = F[f_ind][j][1]
# #                         found = True
# #                         break
# #                 f_ind -= 1
# #
# #             return finder(F, ListOfBuildings, searching_val, last_b, last_b_index - 1, B, f_ind, p)
# #
# #
# # def cleaner(OutputList, ListOfBuildings, T):
# #     Tmp = []
# #     for elem in OutputList:
# #         Tmp.append(T.index(ListOfBuildings[elem]))
# #     return sorted(Tmp)
# #
# #
# # def select_buildings(T, p):
# #     ListOfBuildings = T.copy()
# #     ListOfBuildings.sort(key=lambda x: (x[1], x[2]))
# #     maxval, F = v3(ListOfBuildings, p)
# #     B = finder(F, ListOfBuildings, maxval[0], maxval[1], len(ListOfBuildings) - 1, [], len(ListOfBuildings) - 1, p)
# #     B.reverse()
# #     B = cleaner(B, ListOfBuildings, T)
# #     return B
#
# # v4
# #
# # def get_value(Building):
# #     return (Building[2] - Building[1]) * Building[0]
# #
# #
# # def f(ListOfBuildings, F, i, b, C, prev_a):
# #     if F[i][b] != 0 and prev_a > ListOfBuildings[i][2]:
# #         return F[i][b]
# #     if i == 0:
# #         if prev_a > ListOfBuildings[i][2]:
# #             return F[i][b]
# #         else:
# #             return 0
# #     taken = 0
# #     if b - ListOfBuildings[i][3] >= 0 and prev_a > ListOfBuildings[i][2]:
# #         taken = f(ListOfBuildings, F, i - 1, b - ListOfBuildings[i][3], C, ListOfBuildings[i][1]) + get_value(
# #             ListOfBuildings[i])
# #     notTaken = f(ListOfBuildings, F, i - 1, b, C, prev_a)
# #
# #     if taken > notTaken:
# #         F[i][b] = taken
# #         Tmp = C[i - 1][b - ListOfBuildings[i][3]].copy()
# #         Tmp.append(i)
# #         C[i][b] = Tmp
# #     elif notTaken == 0:
# #         F[i][b] = notTaken
# #         C[i][b] = []
# #     else:
# #         F[i][b] = notTaken
# #         C[i][b] = C[i - 1][b]
# #     return F[i][b]
# #
# #
# # def cleaner(OutputList, ListOfBuildings, T):
# #     Tmp = []
# #     for elem in OutputList:
# #         Tmp.append(T.index(ListOfBuildings[elem]))
# #     return sorted(Tmp)
# #
# #
# # def select_buildings(T, p):
# #     ListOfBuildings = T.copy()
# #     ListOfBuildings.sort(key=lambda x: (x[2], x[1]))
# #     n = len(ListOfBuildings)
# #     F = [[0 for _ in range(p + 1)] for _ in range(n)]  # max wartość dla danego pola
# #     C = [[[] for _ in range(p + 1)] for _ in range(n)]  # wzięte budynki
# #     val0 = get_value(ListOfBuildings[0])
# #     for b in range(ListOfBuildings[0][3], p + 1):
# #         F[0][b] = val0
# #         C[0][b] = [0]
# #     f(ListOfBuildings, F, n - 1, p, C, 10000000000)
# #     # print(ListOfBuildings)
# #     # print(10 * "_")
# #     # for i in range(n):
# #     #     print(F[i])
# #     # print(10 * "_")
# #     # for i in range(n):
# #     #     print(C[i])
# #     return cleaner(C[n - 1][p], ListOfBuildings, T)
# #
# # v5.1
# # class Building:
# #     def __init__(self, h, a, b, w):
# #         self.h = h
# #         self.a = a
# #         self.b = b
# #         self.w = w
# #
# #     def get_value(self):
# #         return int((self.b - self.a) * self.h)
# #
# #     def __str__(self):
# #         out = str((self.h, self.a, self.b, self.w))
# #         return out
# #
# #
# # class BuildingsListClass:
# #     def __init__(self, T):
# #         self.ListOfBuildings = T.copy()
# #         self.T = T
# #
# #     def initialize(self):
# #         self.ListOfBuildings.sort(key=lambda x: (x[2], x[1]))
# #         self.ListOfBuildings = [Building(elem[0], elem[1], elem[2], elem[3]) for elem in self.ListOfBuildings]
# #
# #     def rebuild(self):
# #         self.ListOfBuildings = [(elem.h, elem.a, elem.b, elem.w) for elem in self.ListOfBuildings]
# #
# #     def find_indexes_T(self, OutputList):
# #         Tmp = []
# #         for elem in OutputList:
# #             Tmp.append(self.T.index(self.ListOfBuildings[elem]))
# #         return sorted(Tmp)
# #
# #
# # def f(ListOfBuildings, i, F, C, prev_a, b):
# #     if i < 0:
# #         return 0
# #     # if i == 0:
# #     #     if ListOfBuildings[i].b < prev_a:
# #     #         return F[i][b]
# #     #     else:
# #     #         return 0
# #     if F[i][b] != 0 and ListOfBuildings[i].b < prev_a:
# #         return F[i][b]
# #     taken = 0
# #
# #     if b - ListOfBuildings[i].w > 0 and ListOfBuildings[i].b < prev_a:
# #         taken = f(ListOfBuildings, i - 1, F, C, ListOfBuildings[i].a, b - ListOfBuildings[i].w) + ListOfBuildings[
# #             i].get_value()
# #     notTaken = f(ListOfBuildings, i - 1, F, C, prev_a, b)
# #     if taken > notTaken:
# #         F[i][b] = taken
# #         Tmp = C[i - 1][b - ListOfBuildings[i].w].copy()
# #         Tmp.append(i)
# #         C[i][b] = Tmp
# #     elif notTaken == 0:
# #         F[i][b] = notTaken
# #         C[i][b] = []
# #     else:
# #         F[i][b] = notTaken
# #         C[i][b] = C[i - 1][b]
# #     # if notTaken > taken:
# #     #     if notTaken > F[i][b]:
# #     #         F[i][b] = notTaken
# #     #         C[i][b] = C[i - 1][b]
# #     #     elif notTaken == 0:
# #     #         F[i][b] = notTaken
# #     #         C[i][b] = []
# #     # else:
# #     #     if taken > F[i][b]:
# #     #         F[i][b] = taken
# #     #         Tmp = C[i - 1][b - ListOfBuildings[i].w].copy()
# #     #         Tmp.append(i)
# #     #         C[i][b] = Tmp
# #     return F[i][b]
# #
# #
# #
# # def select_buildings(T, p):
# #     ListOfBuildings = BuildingsListClass(T)
# #     Tmp = ListOfBuildings.ListOfBuildings
# #     Tmp.sort(key=lambda x: (x[2], x[1]))
# #     print(Tmp)
# #     ListOfBuildings.initialize()
# #     n = len(ListOfBuildings.ListOfBuildings)
# #     F = [[0 for _ in range(p + 1)] for _ in range(n)]  # max wartość dla danego pola
# #     C = [[[] for _ in range(p + 1)] for _ in range(n)]  # wzięte budynki
# #     val0 = ListOfBuildings.ListOfBuildings[0].get_value()
# #     for b in range(ListOfBuildings.ListOfBuildings[0].w, p + 1):
# #         F[0][b] = val0
# #         C[0][b] = [0]
# #     f(ListOfBuildings.ListOfBuildings, n - 1, F, C, 100000, p)
# #     # print(10 * "_")
# #     for i in range(n):
# #         print(F[i])
# #     print(10 * "_")
# #     print(F[n - 1][p])
# #     # for i in range(n):
# #     #     print(C[i])
# #     ListOfBuildings.rebuild()
# #     # print(F[n - 1][p])
# #     # print(ListOfBuildings.ListOfBuildings)
# #     # print(C[n - 1][p])
# #     return ListOfBuildings.find_indexes_T(C[n-1][p])
# #     # return ListOfBuildings.find_indexes_T(find_answer(ListOfBuildings.ListOfBuildings, F, n, p))
# #     # return F[n - 1][p]
#
# # v5
# class Building:
#     def __init__(self, h, a, b, w):
#         self.h = h
#         self.a = a
#         self.b = b
#         self.w = w
#
#     def get_value(self):
#         return int((self.b - self.a) * self.h)
#
#     def __str__(self):
#         out = str((self.h, self.a, self.b, self.w))
#         return out
#
#
# class BuildingsListClass:
#     def __init__(self, T):
#         self.ListOfBuildings = T.copy()
#         self.T = T
#
#     def initialize(self):
#         self.ListOfBuildings.sort(key=lambda x: (x[2], x[1]))
#         self.ListOfBuildings = [Building(elem[0], elem[1], elem[2], elem[3]) for elem in self.ListOfBuildings]
#
#     def rebuild(self):
#         self.ListOfBuildings = [(elem.h, elem.a, elem.b, elem.w) for elem in self.ListOfBuildings]
#
#     # def find_indexes_T(self, OutputList):
#     #     Tmp = []
#     #     for elem in OutputList:
#     #         Tmp.append(self.T.index(self.ListOfBuildings[elem]))
#     #     return sorted(Tmp)
#
#     def find_indexes_T(self, OutputList):
#         n = len(self.T)
#         sorted_T = [(self.T[i], i) for i in range(n)]
#         sorted_T.sort(key=lambda x: (x[0][2], x[0][1]))
#         for i in range(len(OutputList)):
#             OutputList[i] = sorted_T[OutputList[i]][1]
#         return sorted(OutputList)
#
#
# # def f(ListOfBuildings, i, F, C, prev_a, p):
# #     if i < 0:
# #         return 0
# #     if F[i][p] != 0 and ListOfBuildings[i].b < prev_a:
# #         return F[i][p]
# #     taken = 0
# #     while i >= 0 and ListOfBuildings[i].b >= prev_a and p - ListOfBuildings[i].w >= 0:
# #         i -= 1
# #     if p - ListOfBuildings[i].w >= 0 and ListOfBuildings[i].b < prev_a:
# #         taken = f(ListOfBuildings, i - 1, F, C, ListOfBuildings[i].a, p - ListOfBuildings[i].w) + ListOfBuildings[
# #             i].get_value()
# #     notTaken = f(ListOfBuildings, i - 1, F, C, prev_a, p)
# #     F[i][p] = max(notTaken, taken)
# #     return F[i][p]
#
# def f(ListOfBuildings, i, F, C, prev_a, p):
#     if i < 0 or p < 0:
#         return 0
#     if F[i][p] != 0 and ListOfBuildings[i].b < prev_a:
#         return F[i][p]
#     taken = 0
#     if p - ListOfBuildings[i].w >= 0 and ListOfBuildings[i].b < prev_a:
#         tmp_i = i - 1
#         while tmp_i >= 0 and ListOfBuildings[tmp_i].b >= ListOfBuildings[i].a:
#             tmp_i -= 1
#         taken = f(ListOfBuildings, tmp_i, F, C, ListOfBuildings[i].a, p - ListOfBuildings[i].w) + ListOfBuildings[
#             i].get_value()
#     notTaken = f(ListOfBuildings, i - 1, F, C, prev_a, p)
#     F[i][p] = max(notTaken, taken)
#     return F[i][p]
#
#
# def get_value(Building):
#     return (Building[2] - Building[1]) * Building[0]
#
#
# # def rek(ListOfBuildings, ValuesList, n, p, i, prev_a, val, Out):
# #     if val == 0:
# #         return True
# #     works = False
# #     while not works and i >= 0 and p >= 0:
# #         while i > 0 and (prev_a <= ListOfBuildings[i][2]):
# #             i -= 1
# #         if ValuesList[i][p] != val and (
# #                 (ValuesList[i][p] != 0 and ValuesList[i + 1][p] > ValuesList[i][p]) or (
# #                 ValuesList[i][p] == 0 and ValuesList[i + 1][p] == val)) and \
# #                 ListOfBuildings[i + 1][2] < ListOfBuildings[Out[-1]][1]:
# #             i += 1
# #             works = rek(ListOfBuildings, ValuesList, n, p - ListOfBuildings[i][3], i - 2, ListOfBuildings[i][1],
# #                         val - get_value(ListOfBuildings[i]), Out)
# #             if works:
# #                 Out.append(i)
# #                 return True
# #             i -= 2
# #         else:
# #             i -= 1
# #     else:
# #         if i < 0:
# #             i = 0
# #         if i == 0 and ValuesList[0][p] == val:
# #             Out.append(i)
# #             return True
# #         return False
# #
# #
# # def find_answer(ListOfBuildings, ValuesList, n, p):
# #     i = n - 1
# #     val = ValuesList[n - 1][p]
# #     Out = []
# #     while i > 0 and ValuesList[i][p] == ValuesList[i - 1][p]:
# #         i -= 1
# #     Out.append(i)
# #     val -= get_value(ListOfBuildings[i])
# #     if val == 0:
# #         return Out
# #     p -= ListOfBuildings[i][3]
# #     prev_a = ListOfBuildings[i][1]
# #     i -= 2
# #     rek(ListOfBuildings, ValuesList, n, p, i, prev_a, val, Out)
# #     return Out
#
#
# # def rek(ListOfBuildings, ValuesList, n, p, i, prev_a, val, Out):
# #     if val == 0:
# #         return True
# #     works = False
# #     while not works and i >= 0 and p >= 0:
# #         while i > 0 and (prev_a <= ListOfBuildings[i][2]):
# #             i -= 1
# #         if ValuesList[i][p] != val and (
# #                 (ValuesList[i][p] != 0 and ValuesList[i + 1][p] > ValuesList[i][p]) or (
# #                 ValuesList[i][p] == 0 and ValuesList[i + 1][p] == val)) and \
# #                 ListOfBuildings[i + 1][2] < ListOfBuildings[Out[-1]][1]:
# #             i += 1
# #             works = rek(ListOfBuildings, ValuesList, n, p - ListOfBuildings[i][3], i - 2, ListOfBuildings[i][1],
# #                         val - get_value(ListOfBuildings[i]), Out)
# #             if works:
# #                 Out.append(i)
# #                 return True
# #             i -= 2
# #         else:
# #             i -= 1
# #     else:
# #         if i < 0:
# #             i = 0
# #         if i == 0 and ValuesList[0][p] == val:
# #             Out.append(i)
# #             return True
# #         return False
#
#
# def find_answer(ListOfBuildings, ValuesList, n, p):
#     i = n - 1
#     val = ValuesList[n - 1][p]
#     Out = []
#     while i > 0 and ValuesList[i][p] == ValuesList[i - 1][p]:
#         i -= 1
#     Out.append(i)
#     val -= get_value(ListOfBuildings[i])
#     if val == 0:
#         return Out
#     p -= ListOfBuildings[i][3]
#     prev_a = ListOfBuildings[i][1]
#     i -= 2
#     while i >= 0 and p >= 0:
#         while i > 0 and (prev_a <= ListOfBuildings[i][2]):
#             i -= 1
#         while i > 0 and ValuesList[i][p] == val:
#             i -= 1
#         if ValuesList[i][p] != val:
#             i += 1
#             Out.append(i)
#             val -= get_value(ListOfBuildings[i])
#             if val == 0:
#                 return Out
#             p -= ListOfBuildings[i][3]
#             prev_a = ListOfBuildings[i][1]
#             i -= 2
#         else:
#             i -= 1
#     else:
#         if i < 0:
#             i = 0
#         if i == 0 and ValuesList[0][p] == val:
#             Out.append(i)
#     return Out
#
#
# # def find_answer(ListOfBuildings, ValuesList, n, p):
# #     i = n - 1
# #     Answer = []
# #     while i > 0:
# #         while i > 0 and ValuesList[i][p] == ValuesList[i - 1][p]:
# #             i -= 1
# #         if i > 0:
# #             Answer.append(i)
# #             p -= ListOfBuildings[i][3]
# #             i -= 1
# #         else:
# #             if len(Answer) > 0:
# #                 if ListOfBuildings[i][2] < ListOfBuildings[Answer[-1]][1]:
# #                     Answer.append(0)
# #             else:
# #                 Answer.append(0)
# #     if 0 not in Answer:
# #         if len(Answer) > 0:
# #             if ListOfBuildings[0][2] < ListOfBuildings[Answer[-1]][1]:
# #                 Answer.append(0)
# #         else:
# #             Answer.append(0)
# #     return Answer
#
# def select_buildings(T, p):
#     classOfBuildings = BuildingsListClass(T)
#     Tmp = classOfBuildings.ListOfBuildings
#     Tmp.sort(key=lambda x: (x[2], x[1]))
#     classOfBuildings.initialize()
#     n = len(classOfBuildings.ListOfBuildings)
#     F = [[0 for _ in range(p + 1)] for _ in range(n)]  # max wartość dla danego pola
#     C = [[[] for _ in range(p + 1)] for _ in range(n)]  # wzięte budynki
#     f(classOfBuildings.ListOfBuildings, n - 1, F, C, classOfBuildings.ListOfBuildings[n - 1].b + 1, p)
#     # for i in range(n):
#     #     print(F[i])
#     classOfBuildings.rebuild()
#     out = find_answer(classOfBuildings.ListOfBuildings, F, n, p)
#     return classOfBuildings.find_indexes_T(out)
#
#
# # v7
# # def get_value(Building):
# #     return (Building[2] - Building[1]) * Building[0]
# #
# #
# # # def find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i, p, prev_b, value):
# # #     n = len(ListOfBuildings)
# # #     if i >= n:
# # #         return value
# # #     # if ValuesList[i] != -1:
# # #     #     return ValuesList[i]
# # #     Building = ListOfBuildings[i]
# # #     taken = 0
# # #     if p - Building[3] >= 0 and Building[1] > prev_b:
# # #         taken = find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i + 1, p - Building[3], Building[2],
# # #                           value + get_value(Building))
# # #     # notTaken = -1
# # #     # if i < n:
# # #     #     notTaken = ValuesList[i]
# # #     # if notTaken == -1:
# # #     #     notTaken = find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i + 1, p, prev_b, value)
# # #     notTaken = find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i + 1, p, prev_b, value)
# # #     if notTaken > taken:
# # #         if notTaken > ValuesList[i]:
# # #             ValuesList[i] = notTaken
# # #             ChoosenBuildings[i] = -1
# # #     else:
# # #         if taken > ValuesList[i]:
# # #             ValuesList[i] = taken
# # #             ChoosenBuildings[i] = i
# # #     return ValuesList[i]
# #
# # def find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i, p, prev_a):
# #     if i == 0:
# #         if ListOfBuildings[i][2] < prev_a:
# #             return ValuesList[0][p]
# #         else:
# #             ValuesList[0][p] = 0
# #             return 0
# #
# #     if ValuesList[i][p] != 0 and ListOfBuildings[i][2] < prev_a:
# #         return ValuesList[i][p]
# #
# #     Building = ListOfBuildings[i]
# #     taken = 0
# #     if p - Building[3] >= 0 and Building[2] < prev_a:
# #         taken = find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i - 1, p - Building[3], Building[1]) + get_value(
# #             Building)
# #     # notTaken = -1
# #     # if i < n:
# #     #     notTaken = ValuesList[i]
# #     # if notTaken == -1:
# #     #     notTaken = find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i + 1, p, prev_b, value)
# #     notTaken = find_best(ListOfBuildings, ValuesList, ChoosenBuildings, i - 1, p, prev_a)
# #     ValuesList[i][p] = max(taken, notTaken)
# #     # if notTaken == 0:
# #     #     ChoosenBuildings[i] = -1
# #     #
# #     # elif notTaken > taken:
# #     #     if notTaken > ValuesList[i][p]:
# #     #         ValuesList[i][p] = notTaken
# #     #         ChoosenBuildings[i] = -1
# #     # else:
# #     #     if taken > ValuesList[i][p]:
# #     #         ValuesList[i][p] = taken
# #     #         ChoosenBuildings[i] = i
# #     return ValuesList[i][p]
# #
# #
# # def find_answer(ListOfBuildings, ValuesList, n, p):
# #     i = n - 1
# #     Answer = []
# #     while i > 0 and p >= 0:
# #         while i > 0 and ValuesList[i][p] == ValuesList[i - 1][p]:
# #             i -= 1
# #         if i > 0:
# #             Answer.append(i)
# #             p -= ListOfBuildings[i][3]
# #             i -= 1
# #         else:
# #             if len(Answer) > 0:
# #                 if ListOfBuildings[i][2] < ListOfBuildings[Answer[-1]][1]:
# #                     Answer.append(0)
# #             else:
# #                 Answer.append(0)
# #     if p>=0 and 0 not in Answer:
# #         if len(Answer) > 0:
# #             if ListOfBuildings[0][2] < ListOfBuildings[Answer[-1]][1]:
# #                 Answer.append(0)
# #         else:
# #             Answer.append(0)
# #     return Answer
# #
# #
# # def select_buildings(T, p):
# #     ListOfBuildings = T.copy()
# #     ListOfBuildings.sort(key=lambda x: (x[2], x[1]))
# #     n = len(ListOfBuildings)
# #     ValuesList = [[0 for _ in range(p + 1)] for _ in range(n)]
# #     ChoosenBuildings = [-1 for _ in range(n)]
# #     val0 = get_value(ListOfBuildings[0])
# #     for b in range(ListOfBuildings[0][3], p + 1):
# #         ValuesList[0][b] = val0
# #     # print(ListOfBuildings)
# #     find_best(ListOfBuildings, ValuesList, ChoosenBuildings, n - 1, p, ListOfBuildings[n - 1][2] + 1)
# #     # for i in range(n):
# #     #     print(ValuesList[i])
# #     print(ValuesList[n-1][p])
# #     ChoosenBuildings = find_answer(ListOfBuildings, ValuesList, n, p)
# #     # print(ChoosenBuildings)
# #     return cleaner2(ChoosenBuildings, ListOfBuildings, T)
# #
# #
# # def cleaner2(ChoosenBuildings, ListOfBuildings, T):
# #     Tmp = []
# #     for elem in ChoosenBuildings:
# #         Tmp.append(T.index(ListOfBuildings[elem]))
# #     return sorted(Tmp)
# #
# #
# # def cleaner(ChoosenBuildings, ListOfBuildings, T):
# #     ChoosenBuildings = [elem for elem in ChoosenBuildings if elem != -1]
# #     Tmp = []
# #     for elem in ChoosenBuildings:
# #         Tmp.append(T.index(ListOfBuildings[elem]))
# #     return Tmp
#
#
# runtests(select_buildings)
