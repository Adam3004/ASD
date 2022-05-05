# Adam Misztal
# W procesię tworzenia kodu podpierałem się wiedzą z wykładu, a także z Cormena.
# Sposób rozwiązania: najpierw znajduję największą i najmniejszą wartość jakie są w przedziałach w talbicy P, następnie
# bucket sortem sortuje listę. Tworzę n//15 kubełków, ponieważ tak moim zdaniem jest najoptymalniej, bo testowałem różne
# liczby, a lepiej przedzieć n przez jakąś liczbe, bo przy n kubełkach jest dość sporo pustych. Sam algorytm działa
# poprawnie, ponieważ to zwykły bucket sort.
# Złożoność tego algorytmu średnio jest liniowa, a w najgorszym wypadku nlogn gdy mamy tylko 1 kubełek. find_ends ma
# złożonośc n/2, a bucketsort c*n gdzie c to stała. Co prawda, buckety są sortowane quciksortem który jest nlogn, ale
# przy tych liczbach jest on dość optymalny, bo nawet jeśli w przedziałach będzie sporo liczb to będzie się on lepiej
# zachowywał niż jakiś kwadratowy algorytm sortowania, a żaden liniowy algorytm przy na tyle różnych danych nie byłby
# sensowny. Jedyna sytuacja która może spowodować, że algorytm jest liniowy to taka, gdy n<30 i mamy tylko jeden kubełek
# wtedy algorytm ma złożoność quicksorta, czyli nlogn, ale są to nieduże liczby więc nie jest to problem. Dla większych
# n problem znika bo quicksort działa w złożoności klogk gdzie k to liczba elementów w danym kubełku, a zazwyczaj k jest
# znacznie mniejsze niż n, więc w średnim przypadku algorytm działa liniowo.
# Złożoność pamięciowa to c*n, gdzie c to jakaś stała jeżeli chodzi o listę bucketów (w bucketach będzie n elementów,
# ale są to różne listy) i średnio logn w przypadku rekurencji powodwanej przez quicksorta, zatem złożoność pamięciowa
# w średnim i najgorszym wypadku to n, różniące się stałą. Quicksort jest bardziej zoptymalizowany, aby zajmował mniej
# pamięci (użycie while zamiast if).

from zad3testy import runtests


# algorytm szukania min max, ma złożoność n/2, bo porównujemy na bieżąco wyraz i-ty z i+1-wszym, więc pętla wykona się
# n/2 razy. Przypisujemy na początku do startu i endu wartości ostatniej krotki z tablicy, bo dzięki temu unikamy ifa
# po pętli który sprawdzałby ostatni wyraz w przypadku gdy n parzyste.
# Napisałem podobny algorytm do tego jaki kojarzyłem z ćwiczeń.
def find_ends(L):
    start = L[-1][0]
    end = L[-1][1]
    for i in range(0, len(L), 2):
        checking1 = L[i]
        checking2 = L[i + 1]
        if checking1[0] > checking2[0]:
            if checking2[0] < start:
                start = checking2[0]
        else:
            if checking1[0] < start:
                start = checking1[0]
        if checking1[1] > checking2[1]:
            if checking1[1] > end:
                end = checking1[1]
        else:
            if checking2[1] > end:
                end = checking2[1]
    return start, end


# quicksort
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
    while l < r:
        q = moving(L, l, r)
        quickSort(L, l, q - 1)
        l = q + 1


# quickSort end

# bucketSort
def bucketSort(n, T, start, end):
    size = n // 15
    if size == 0:
        size = 1
    bottom = start
    upper = end
    step = (upper - bottom) / size
    ListOfBuckets = [[] for _ in range(n)]
    for i in range(n):
        actual_elem = T[i]
        norm_num = actual_elem / (upper - bottom)  # normalized num
        buck_ind = int(n * norm_num)  # select bucket
        ListOfBuckets[buck_ind].append(actual_elem)
        # ListOfBuckets[int((actual_elem - bottom) // step)].append(actual_elem)
    for i in range(len(ListOfBuckets)):
        if len(ListOfBuckets[i]) > 1:
            quickSort(ListOfBuckets[i], 0, len(ListOfBuckets[i]) - 1)
    j = 0
    for i in range(len(ListOfBuckets)):
        for elem in ListOfBuckets[i]:
            T[j] = elem
            j += 1
    return T


# główna funkcja (taki main)
def SortTab(T, P):
    n = len(T)
    start, end = find_ends(P)
    # start, end = 1, n
    T = bucketSort(n, T, start, end)
    return T


runtests(SortTab)
