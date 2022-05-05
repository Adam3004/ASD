# L = [[(1, 2), (3, 4)], [(1, 1), (5, 5)], [(2, 3), (7, 4)], [(5, 1), (6, 7)]]
L = [[(1, 2), (3, 4)], [(2, 3), (3, 4)], [(3, 4), (4, 5)], [(1, 1), (2, 6)]]


def capacity(container):
    len_x = container[1][0] - container[0][0]
    len_y = container[1][1] - container[0][1]
    return container[0][1], container[1][1], len_x * len_y


def creator(L, a):
    n = len(L)
    Capacities = [(10000000, 1000000000, 0) for _ in range(n)]
    end = 0
    for elem in L:
        heights = capacity(elem)
        last = end
        while last > 0 and Capacities[last - 1][1] > heights[1]:
            Capacities[last] = Capacities[last - 1]
            last -= 1
        if last > 0 and Capacities[last - 1][0] == heights[0]:
            while last > 0 and Capacities[last - 1][1] > heights[1] and Capacities[last - 1][0] >= heights[0]:
                Capacities[last] = Capacities[last - 1]
                last -= 1
        Capacities[last] = heights
        end += 1
    end = 0
    last = 0
    Boxes_Done = [(1000000, 1000000) for _ in range(n)]
    i = 0
    j = 0
    while j < n - 1:
        if j > 0:
            height = Capacities[j][1]
            while height == Capacities[j + 1][1]:
                needed_water += Capacities[j][2]
                j += 1
            j2 = j
            while j2 < n:
                checking = Capacities[j2]
                if checking[0] < height and checking[0] <= prev_h:
                    needed_water += (checking[2] * ((height - prev_h) / (checking[1] - checking[0])))
                elif height > checking[0] > prev_h:
                    needed_water += (checking[2] * ((height - checking[0]) / (checking[1] - checking[0])))
                j2 += 1
            Boxes_Done[i] = (height, needed_water)
            i += 1
            prev_h = height
            j += 1
        else:
            needed_water = 0
            height = Capacities[j][1]
            while height == Capacities[j + 1][1]:
                needed_water += Capacities[j][2]
                j += 1
            j2 = j
            while j2 < n:
                checking = Capacities[j2]
                if checking[0] < height:
                    needed_water += (checking[2] * ((height - checking[0]) / (checking[1] - checking[0])))
                j2 += 1
            Boxes_Done[i] = (height, needed_water)
            i += 1
            prev_h = height
            j += 1
    height = Capacities[j][1]
    j2 = j
    checking = Capacities[j2]
    if checking[0] < height and checking[0] < prev_h:
        needed_water += (checking[2] * ((height - prev_h) / (checking[1] - checking[0])))
    elif height > checking[0] > prev_h:
        needed_water += (checking[2] * ((height - checking[0]) / (checking[1] - checking[0])))

    Boxes_Done[i] = (height, needed_water)
    # while end < n - 1:
    #     while Capacities[end + 1][1] == Capacities[end][1]:
    #         for i in range(last, n):
    #             Boxes_Done[i] += Capacities[end][2]
    #         end += 1
    #     else:
    #         for i in range(last, n):
    #             Boxes_Done[i] += Capacities[end][2]
    #         end += 1
    #     if end < n - 1 and Capacities[end + 1][1] != Capacities[end][1]:
    #         Boxes_Done[end] += Capacities[end][2]
    #         end += 1
    #     last = end
    # Boxes_Done[end] += Capacities[last][2]
    print(Capacities)
    print(Boxes_Done)
    i = 0
    while i < len(Boxes_Done) and Boxes_Done[i][1] <= a:
        i += 1
    if i == 0:
        return 0
    else:
        return i


print(creator(L, 10.5))
