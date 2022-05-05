import math

C = [(1, 1), (3, 2), (2, 5), (0, 3), (5, 10), (7, -2)]
# C = [(1, 0), (2, 0), (7, 12), (12, 0)]
# C = [(1, 1), (2, 1), (3, 18), (6, 1)]
C.sort()


def d(miasto_x, miasto_y):
    return math.sqrt((miasto_x[0] - miasto_y[0]) ** 2 + (miasto_x[1] - miasto_y[1]) ** 2)


def f(S, t):
    if len(S) == 1 and t == S[0]:
        return 0
    min_val = math.inf
    Tmp = S.copy()
    Tmp.remove(t)
    for r in Tmp:
        min_val = min(min_val, f(Tmp, r) + d(r, t))

    return min_val


min_val = math.inf
for t in C:
    min_val = min(min_val, f(C.copy(), t))
print(min_val)
