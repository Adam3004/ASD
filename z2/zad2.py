# Adam Misztal
# Dopisek:
# W moim kodzie użyłem algorytmów, które były pokazane na ćwiczeniach oraz wykładach, lub podobnych, które lekko
# zmodyfikowałem. Pozostała, część jest napisana przeze mnie.
# Opis algorytmu:
# Zacznę od wyjaśnienia odnośnie zmiany listy list na listę krotek. Gdzieś kiedyś czytałem, że krotki dużo szybciej
# zwracają wartości niż listy, a samo comprehension w pythonie jest również szybkie, więc ta zmaiana przynosi korzystne
# rezultaty w przypadku szybkości wykonywania się mojego algorytmu.
# Algorym składa się z 2 głownych etapów: 1 posortwanie listy niemalejąco po początkach przedziałów, a dla wartości
# sobie równych ustawnienie najpierw największego końca przedziału (tylko to ma znaczenie reszta nie musi być
# posortowana) 2. sprawdzenie poziomów tych przedziałów które nie są jeszcze w niczym zawarte.
# Sortowanie wykonuje quicksortem, który dzieli talbicę na 3 (na wykładzie chyba było powiedziane, że nazywa się to
# quicker sort, ale nie jestem pewny, bo sam wymyślałem ten algorym), więc działanie dla większych i mniejszych
# oczywiste. Dla równych za to używam algorymtu który pojawił się na ćwiczeniach. Wyszukuje on wartość największego
# końca przedziału w czasie 0.5 N, bo sprawdzamy 2 wyrazy sąsiednie i większy przyrównujemy do naszego aktualnego
# maksimum. Później zamieniam element pierwszy spośród tych które mają ten sam początek przedziału, z tym który ma
# największą wartość końca przedziału. Zamysł jest taki, że jeśli będę sprawdzał co zawiera w sobie jakiś przedział, to
# zacznę od pierwszego, a jeśli pierwszy jest największy to automatycznie zawiera wszystkie pozostałe przedziały,
# które rozpoczynają się tą samą wartością, pozwoli mi to uniknąć jednego warunku w ifie w kodzie i ułatwi całe zadanie.
# W samym quicksorcie używam while, ponieważ dzięki temu używam mniej pamięci jak i cały kod wykonuje się szybciej
# Etap drugi działa w sposób następujący, rozpoczynam zliczanie wartości k (k=poziom danego przedziału), przy czym,
# zwracam też pierwszy przedział, który nie jest zawarty w sprawdzanym (ten będę sprawdzał następnie). Dzięki temu
# ukniknę sprawdzania k dla przedziałów które są w czymś zarate, bo ich k jest na pewno mniejsze od k przedziału w
# którym są zawarte, a nas interesuje tylko największe spośród k. Wykonujemy ten krok dopóki istnieje przedział który
# nie jest zawarty w poprzednim. Sprawdzamy oczywiście tylko dalsze przedziały, po to są posortwane, np przedział
# [2,5] (zakładamy, że to jednyny który zaczyna się od 2 na potrzeby przykładu), nie będzie zawierał żadnego który jest
# w posortowanej liście przed nim, bo 2 < od czegkolwiek mniejszego (oczywsite). Dlatego algorym dla każdego kolejnego
# przedziału dla którego szukamy k wykonuje się coraz mniej razy.
# Złożoność:
# Złożonośc optymistyczyna tego algorymtu to n(logn + 1), ponieważ quicksort działa w złożoności nlogn, a jeżeli lista
# zawiera przedział który zawiera w sobie wszystkie pozostałe to będzie on pierwszym elementem posortwanej listy, więc
# dalsza część algorymu ograniczy się do wyliczenia k dla pierszego elementu i pętla while nie będzie się dalej
# wykonywać.
# Złożoność średnia tego algorymtu to c2n(logn) (c to jakaś stała), bo w drugiej części algorytmu pętla while wykonuje
# się log n razy a zawarte w niej instrukcje przynajmniej raz (dla pierwszego elementu ta długość wynosi n, dla
# kolejnego n-1 itd), więc skoro wykona się tylko kilka razy i za każdym razem krócej to będzie to więcej niż n ale
# mniej niż n^2
# Złożoność pesymistyczna: quickosrt wykona się w n^2 i druga część algorymu w n*(n+1)/2. Wtedy otrzymujemy łączną
# złożoność 1.5*n^2 + 0.5*n, jednak szanse na taki przypadek są minimalne, a sama stałą przy n^2 jest nieduża.
# n*(n+1)/2 ponieważ n razy wykonanmy pętle o długości (n, n-1, n-2, ..., 1) z sumy ciągu arytmetycznego otrzymujemy
# taki wynik. Taki przypadek może zdażyć się dla listy gdzie wszystkie przedziały nie zawierają się w sobie nawzajem
# W rzeczywistości najczęstrzym przypadkiem jest przypadek średni. Szanse na optymistyczny i pesymistyczny są niewielkie
# dlatego wnioskuje, że sam algorym jest optymalny.
# Postanowiłem zrezygnować z optymalizacji quicksorta, poprzez randomizacje, czy medianę, ponieważ kosztowało to zawsze
# trochę czasu, a w przypadku zadania domowego wydaję się to bardziej istotne niż prawdopodobieństwo przypadku
# pesymistycznego. Rozważałem też rekurencje w drugiej części zamiast iteracji, ale myślę, że dzięki iteracji
# zaoszczędzę pamięć.


from zad2testy import runtests


# funkcja odpowiadająca, za ułożenie listy na zasadzie [   <x   ,   =x   ,   >x   ] gdzie i wskazauje na pierwszy
# element =x, a k na ostatni element =x (to k nie ma połącznie z k o którym pisałem w opisie oznaczającym poziom,
# tutaj to zwykła zmienna, zbierzność nazw)
def moving(L, l, r):
    x = L[r][0]
    i = l - 1
    k = i
    for j in range(l, r):
        if L[j][0] < x:
            i += 1
            k += 1
            L[k], L[j] = L[j], L[k]
            L[i], L[k] = L[k], L[i]
        elif L[j][0] == x:
            k += 1
            L[k], L[j] = L[j], L[k]

    L[k + 1], L[r] = L[r], L[k + 1]
    return i + 1, k + 1


# szukanie maksymalnego końca przedziału
# algorym sprawdza co drugie elementy i większy porównuje z aktualnym max
# ustawiam max wal na ostatnią bo w niektórych przypadkach ostatnia wartość nie byłaby sprawdzona w pętli
def sort_same_partitions(L, l, r):
    max_val = (L[r][1], r)
    for i in range(l, r, 2):
        checking_1 = L[i][1]
        checking_2 = L[i + 1][1]
        if checking_1 <= checking_2:
            if max_val[0] < checking_2:
                max_val = (checking_2, i + 1)
        else:
            if max_val[0] < checking_1:
                max_val = (checking_1, i)
    L[l], L[max_val[1]] = L[max_val[1]], L[l]


# lekko zmodyfikowany quicksort z wykładu
def quickSort(L, l, r):
    while l < r:
        q, q2 = moving(L, l, r)
        quickSort(L, l, q - 1)
        sort_same_partitions(L, q, q2)
        l = q2 + 1


# # funckja znajdująca nasze k(poziom przedziału). Pierwszy while szuka przedziału który jako kolejny sprawdzimy. Jest
# # to pierwszy przedział który nie jest zawarty w aktualnym. Dzięki temu nie ominiemy, żadnego, ale i nie będziemy
# # sprawdzać niepotrzebnych. Potem dokańczam liczenie k forem bo jest to szybsze
def including(L, start, length):
    k = 0
    j = start + 1
    starting_val = L[start][1]
    while j < length and starting_val >= L[j][1]:
        j += 1
        k += 1
    next_move = j
    j += 1
    for i in range(j, length):
        if starting_val >= L[i][1]:
            k += 1
    return k, next_move


# # funkcja znajduje największy poziom w liście przedziałów
# # while wykonuje się dla next_move zwracanych przez funckje including, dzięki temu wynokuje się dużo mniej razy
# # i nie sprawdza też niepotrzebnie jakichś warunków
def find_level(L, length):
    max_k = 0
    j = 0
    while j < length:
        k, j = including(L, j, length)
        if k > max_k:
            max_k = k
    return max_k


# comprehension zamieniające liste list na liste korotek. Powód tej optymalizacji kodu opisałem na początku
# wywołanie quicksorta (etap 1 sortowanie)
# zwrócenie wyniku z etapu 2 który wykonuje się w find_level
def depth(L):
    length = len(L)
    L = [(i[0], i[1]) for i in L]
    quickSort(L, 0, length - 1)
    return find_level(L, length)


runtests(depth)
