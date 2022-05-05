# Adam Misztal
# Dopisek:
# w moim wykonaniu zadania korzystałem z algorytmu podobnego do tego opisanego, w książce poleconej do tych zajęć
# "Wprowadzenie do algorytmów" Cormena w rozdziale poświęconemu heap sortowi i kolejce, oraz wspomagałem się kodem
# pokazanym na zajęciach.
# Działanie algorytmu:
# gdy k = 0 nie ma zmian więc zwracam p
# w przypadku gdy k=1 wykorzystuje bubble sorta w uproszczonej wersji (wykonuje się raz) dzięki temu dla tego przypadku
# udało mi się wykonywać to zadanie liniowo
# w każdym innym przypadku kożystam z algorytmu działającego na zasadzie kolejki
# uzupełniam tablice k+1 pierwszymi elementami, tworzę z niej kopiec (min na górze), zamieniam element pierwszy z ostatnim
# i wyciągam z tej listy najmniejszy wyraz i zmieniam wartość odpowiedzniego elementu listy odsyłaczowej (nie było sensu
# robić drugiej, gdy mam już gotową), potem wstawiam kolejny wyraz z linked listy do mojej tablicy i próbuje "wypchnąć"
# go na swoje miejsce, po czym naprawiam kopiec poprzez metode heapify. Ten prodes wykonuje n - k - 1 razy. Potem
# Dalej wykonuję pierwszą część, ale już nie dodaje kolejnych elementów, bo już ich nie ma. Na koniec wstawiam ostatni
# element i zwracam wskaźnik na początek listy odsyłaczowej.
# Dla k=0 algorym działa w złożoności Θ(1), bo tylko zwraca wskaźnik
# Dla k=1 algorym działa w złożoności Θ(n), bo to jednorazowy bubble sort, który dla 1chatoycznych list działa liniowo
# Dla pozostałych k algorym działa w złożoności Θ(c*n*log(k)) (gdzie c jest jakąś liczbą), bo wykonuje instrukcje
# zajmujące log(k), n razy. Wydaje mi się, że początkowe sprawdzenie liczby elementów poprzez przebiegnięcie po liście
# zwiększa tę złożoność do 0(n*(log(k)+1)) a w przypadku gdy k=n-1, wstawianie do listy również trwa n więc najgorsza
# złożoność to jeżeli się nie mylę 0(n*(log(k)+2))
# Bubble sort działa dobrze (wiadomo), kolejka działa dobrze, bo można przesunąć elemen maksymalnie o k pól, żeby był
# posortowny, więc w tablicy k+1 elementów znajdzie się element który jest najmniejszy idąc od lewej. W kolejnym ruchu
# 2 najmniejszy też znajdzie się na pierwszym miejscu tej listy itd. aż do końca. Wyżej opisałem, jak dzieje się to, że
# one się na owych miejscach znajdują

from zad1testy import Node, runtests


def SortH(p, k):
    # 0-chaotyczna jest już posortowana
    if k == 0:
        return p
    elif k == 1:
        # 1-chaotyczna jest sortowana przez bubble sorta w czasie liniowym
        first = bubbleSort(p)
    else:
        # w innym wypadku korzystam z kolejki
        first = heap_sort(p, k)
    return first


# bubble sort
# użyłem go, bo działa liniowo dla k=1 i korzystam z niego tylko dla tego przypadku, więc jest on trochę uproszczony
# żeby wykonał się tylko raz, bo więcej nie ma potrzeby
def bubbleSort(p):
    first = p  # zmienna wskazująca pierwszy element
    # zamaiana pierwszego elementu z drugim jeśli jest taka potrzeba
    if p.next.val < p.val:
        prev = p.next
        tmp = prev.next
        prev.next = p
        first = prev
        prev = prev.next
        prev.next = tmp
        p = first.next
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
        else:
            connector = p
            p = p.next
    # ustawiamy p na first i jeśli jakieś zmiany były wykonane, to rozpoczynamy kolejne wykonanie pętli
    p = first

    return first


# heap heap hurra (kolejka)

def left(i): return 2 * i + 1


def right(i): return 2 * i + 2


def parent(i): return (i - 1) // 2


# sprawdza długość linked listy
def len_of_linked_list(p):
    counter = 0
    while p is not None:
        counter += 1
        p = p.next
    return counter


# buduje kupiec
def build_heap(tab, k):
    for i in range(parent(k), - 1, -1):
        heapify(tab, i, k)


# naprawia kopiec
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


# zamienia elementy i naprawia kopiec
def changer(tab, k):
    max = tab[0]
    tab[0] = tab[k]
    heapify(tab, 0, k)
    return max


# dodaje do kopca element i wypycha go na jak najwyższe miejsce
def increase(tab, i, val):
    tab[i] = val
    while i > 0 and tab[parent(i)] > tab[i]:
        tab[parent(i)], tab[i] = tab[i], tab[parent(i)]
        i = parent(i)


# zamienia n elementów linked listy na tablice
def chnager_to_table(p, tab, n):
    for i in range(n):
        tab[i] = p.val
        p = p.next
        i += 1

    return tab, p


# główna funkcja
def heap_sort(p, k):
    n = len_of_linked_list(p)  # długość linked listy
    first = p  # wskaźnik na 1 element
    q = p  # wskaźnik na pierwszy element, będe zmieniał wartości przesuwając właśnie q
    if k >= n:  # warunek konieczny bo k nie może być wieksze niż n-1
        k = n - 1
    tmp_tab = [None for _ in range(k + 1)]  # tablica z której korzystam
    tmp_tab, p = chnager_to_table(p, tmp_tab, k + 1)  # uzupełnienie tej tablicy
    build_heap(tmp_tab, k)
    for i in range(n - k - 1):
        q.val = changer(tmp_tab, k)
        q = q.next
        increase(tmp_tab, k, p.val)
        p = p.next
    for i in range(k, 0, -1):
        tmp_tab[i], tmp_tab[0] = tmp_tab[0], tmp_tab[i]
        q.val = tmp_tab[i]
        q = q.next
        heapify(tmp_tab, 0, i - 1)
    q.val = tmp_tab[0]
    return first


runtests(SortH)
