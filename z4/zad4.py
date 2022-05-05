# Adam Misztal
from zad4testy import runtests

'''
Algorytm rozwiązujący zadany problem
class Building - oznacza dany akademik (wygodniej było mi robić to zadanie z obiektem)
class BuildingsListClass - to klasa w której mam wszystkie potrzebne metody (analogiczny powód)
initialize - zmienia listę krotek w liste obiektów Building
rebuild - analogicznie jak wyżej, ale na odwrót
find_indexes_T - znajduje indexy elementów które zostały wybrane w tablicy T

1. funckja f(i,p) znajduje największą liczbę studentów, których można zmieścić w nienachodzących na siebie akademikach 
od 0 do i, nie przekraczających łącznej wartości p
2. f(i,p)={ max(f(i-1, p), f(i-1, p - waga budynku i) + ilość studentów których można zmieścić w itym budynku), jeśli 
            p - waga budynku i >=0 oraz budynek ity nie nachodzi na poprzednio wybrany budynek
            f(i-1, p), w przeciwnym razie }
    f(-1,p)=0
3. implementacja poniżej 

ta funkcja pozwala na znalezienie największej liczby studentów, których można zmieścić w nienachodzących na siebie 
akademikach, nie przekraczających łącznej wartości p, ponieważ rozważamy wszystkie podproblemy które są nam potrzebne
i pozwolą nam znaleźć odpowiedni wynik

Złożoność czasowa: O((n^2)*p + nlogn)
Złożoność pamięciowa: O(n*p)
'''


# klasa opisana w opisie
class Building:
    def __init__(self, h, a, b, w):
        self.h = h
        self.a = a
        self.b = b
        self.w = w

    # zwraca ilość studentów których pomieśći dany obiek Building (akademik)
    def get_value(self):
        return int((self.b - self.a) * self.h)

    def __str__(self):
        out = str((self.h, self.a, self.b, self.w))
        return out


# klasa opisana w opisie
class BuildingsListClass:
    def __init__(self, T):
        self.ListOfBuildings = T.copy()
        self.T = T

    def initialize(self):
        self.ListOfBuildings.sort(key=lambda x: (x[2], x[1]))
        self.ListOfBuildings = [Building(elem[0], elem[1], elem[2], elem[3]) for elem in self.ListOfBuildings]

    def rebuild(self):
        self.ListOfBuildings = [(elem.h, elem.a, elem.b, elem.w) for elem in self.ListOfBuildings]

    # tworze krotkę ((h,a,b,w), index) i ją sortuję, po czym zamieniam wartości z otrzymanej wcześniej tablicy na te
    # które dane elementy miały przed posortowaniem
    def find_indexes_T(self, OutputList):
        n = len(self.T)
        sorted_T = [(self.T[i], i) for i in range(n)]
        sorted_T.sort(key=lambda x: (x[0][2], x[0][1]))
        for i in range(len(OutputList)):
            OutputList[i] = sorted_T[OutputList[i]][1]
        return sorted(OutputList)


# funkcja opisana w opisie
def f(ListOfBuildings, i, ListOfValues, prev_a, p):
    if i < 0:
        return 0
    # jeśli wartość już była liczona to wykorzystujemy ją i nie liczymy ponownie
    if ListOfValues[i][p] != 0:
        return ListOfValues[i][p]
    taken = 0  # opcja kiedy bierzemy ity element (akademik)
    if p - ListOfBuildings[i].w >= 0:
        tmp_i = i - 1
        # poszukiwanie następnego akademika który nie będzie nachodził na mój obecnie wybrany akademik
        while tmp_i >= 0 and ListOfBuildings[tmp_i].b >= ListOfBuildings[i].a:
            tmp_i -= 1
        taken = f(ListOfBuildings, tmp_i, ListOfValues, ListOfBuildings[i].a, p - ListOfBuildings[i].w) + \
                ListOfBuildings[i].get_value()
    notTaken = f(ListOfBuildings, i - 1, ListOfValues, prev_a, p)  # opcja kiedy nie bierzemy itego elementu
    ListOfValues[i][p] = max(notTaken, taken)
    return ListOfValues[i][p]


# zwraca ilość studentów których pomieści dany akademik
def get_value(Building):
    return (Building[2] - Building[1]) * Building[0]


def find_answer(ListOfBuildings, ListOfValues, n, p):  # (posortowana tablica T, wypełniona lista wartości, len(T), p)
    i = n - 1
    val = ListOfValues[n - 1][p]
    Out = []  # lista przetrzymująca wynik (indexy elementów w talicy ListOfBuildings, które chcemy wybrać, aby uzyskać
    # najlepszy możliwy wynik

    # szukamy pierwszej innej wartości niż najlepsza
    while i > 0 and ListOfValues[i][p] == ListOfValues[i - 1][p]:
        i -= 1
    # dodajemy pierwszy element, który nas interesuje
    Out.append(i)
    # zmniejszamy poszukiwaną wartość o ilość studentów, których pomieśći ity akademik
    val -= get_value(ListOfBuildings[i])
    # jeżeli wartość == 0 (sytuacja kiedy bieżemy tylko jeden akademik) to funkcja kończy swoje działanie zwracając Out
    if val == 0:
        return Out
    # odejmujemy od p wartość jaką kosztuje nas ity akademik
    p -= ListOfBuildings[i][3]
    # ustawiamy prev_a na a itego akademika
    prev_a = ListOfBuildings[i][1]
    i -= 1
    while i >= 0:
        # szukamy domku który nie będzie nachodził na ostatni który wzięliśmy, dzięki posortowaniu, każdy następny
        # też będzie możliwy do wzięcia
        while i > 0 and (prev_a <= ListOfBuildings[i][2]):
            i -= 1
        # szukamy pierwszej innej wartości niż ostatnia
        while i > 0 and ListOfValues[i][p] == val:
            i -= 1
        # upewniamy się czy nasza wartość jest inna od tej którą mieliśmy w zmiennej val
        if ListOfValues[i][p] != val:
            # dodajemy index do tablicy Out i wykonujemy potrzebne zmiany w zmiennych
            i += 1
            Out.append(i)
            val -= get_value(ListOfBuildings[i])
            if val == 0:
                return Out
            p -= ListOfBuildings[i][3]
            prev_a = ListOfBuildings[i][1]
            i -= 2
        else:
            i -= 1
    else:
        if i < 0:
            i = 0
        if i == 0 and ListOfValues[0][p] == val:
            Out.append(i)
    return Out


def select_buildings(T, p):
    classOfBuildings = BuildingsListClass(T)
    classOfBuildings.initialize()
    n = len(classOfBuildings.ListOfBuildings)
    ListOfValues = [[0 for _ in range(p + 1)] for _ in range(n)]  # wartości funkcji f(i,p) opisanej wyżej (wypełnione
    # będą tylko te pola które były potrzebne, pozostałe zostają wypełnione zerami)

    f(classOfBuildings.ListOfBuildings, n - 1, ListOfValues, classOfBuildings.ListOfBuildings[n - 1].b + 1, p)
    classOfBuildings.rebuild()
    return classOfBuildings.find_indexes_T(find_answer(classOfBuildings.ListOfBuildings, ListOfValues, n, p))


runtests(select_buildings)
