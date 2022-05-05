def findLeader(tab, n):
    do_pary = 1
    lider = tab[0]
    for i in range(n):
        if do_pary > 0:
            if tab[i] == lider:
                do_pary += 1
            else:
                do_pary -= 1
        else:
            do_pary += 1
            lider = tab[i]
        if do_pary == 0: return -1
        ile = 0
        for i in range(n):
            if tab[i] == lider:
                ile += 1

        if ile > n / 2: return lider

    return -1


tab = [1, 2, 3, 1, 1, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
print(findLeader(tab, len(tab)))
