# Adam Misztal

'''
Opis algorytmu:
1. Sprawdzam, czy nie mam w baku na tyle paliwa aby dojechać do końca
2. Przechodzę przez tyle pól na ile wystarczy mi paliwa w baku dodając możliwe tankowania które mijam do kolejki
3. Sprawdzam na której plamie najbardziej opłacałoby mi się zatankować (zyskam najwięcej ropy), spośród tych które
minąłem (od samego początku do pola na którym aktualnie stoję) i tankuje tam
4. Ponawiam kroki 1,2,3

Dlaczego algorym zachłanny działa?
Ponieważ mój algorym wybiera plame ropy która da mi najwięcej paliwa. Zawsze jeżeli weźmiemy więcej ropy niż mniej, to
na pewno nam to nie zaszkodzi. Np. jeżeli braknie nam ropy na 10 pól od końca, to potrzebujemy przynajmniej 10 litrów,
ale jeśli jakaś plama da nam 20, to nie zaszkodzi nam to. W każdym innym wypadku i tak wybieramy największe możliwe
jakie już minęliśmy, bo w tym wypadku więcej znaczy lepiej, bo zajedziemy się dalej, przez co ilość tankowań będzie
najkrótsza

Działanie algorytmu
Ustawiam capacity (na przejechanie ilu pól mam jeszcze wystarczającą ilość paliwa w baku) na wartość pola T[0]
Tworze listę z polami tankowań - Out
Znajduję maksymalną wartość w T
Przebiegam po tylu elementach z listy T na ile pozwala mi capacity, dodając niezerowe do kolejki priorytetowej
(Dodaje wartości max_val - T[i], ponieważ PriorityQueue na wierzch ustawia najmneiejszą wartość, więc odejmując
od maksymalnej wartości jakąś inną (na pewno mniejszą lub równą) wiem, że będzie ona pierwsza do wyjęcia. Po prostu
odwracam te wartości poprzez odejmowanie, bo w kolejce trzymam jak dużo od danej wartości brakuje mi do bycia maksymalną,
im mniej tym szybciej powinna być wyjęta. Przy dodawaniu tej wartości do capacity znów odejmuję tą trzymaną w kolejce
od max_val, przez co uzyskuję tą która była w T[i])
Jeśli stoję już na ostatnim polu na które moge dojechać, to sprawdzam z której plamy najbardziej opłacałoby się
zatankować i zakładam, że tam zatankowałem, po czym zwiększam capacity o ilość pól które mogę przejechać stojąc na
polu na którym skończyłem wcześniej sprawdzać i powtarzam proces dopóki w moim baku nie będzie wystarczająco paliwa, aby
dojechać na pole n-1.

Złożoność algorytmu:
- czasowa O(nlogn), ponieważ każde pole próbuje dodać do kolejki tylko raz (dodawanie do PriorityQueue to logn), więc
w najgorszym wypadku złożoność to nlogn, np gdy każde pole byłoby równe 1. Inne operacje mają mniejszą złożlość, np.
max(T) jest liniowe.
- pamięciowa O(n), kolejką może być zapełniona maksymalnie n-1 elementami, jeżeli np każdy byłby równy 1

'''

import queue
from zad5testy import runtests


def plan(T):
    capacity = T[0]  # pojemność naszej ciężarówki (ile pól możemy jeszcze przejechać)
    Out = [0]  # lista zawierająca indexy pól na których się zatrzymamy (lista z odpowiedzią)
    n = len(T)
    actual_value = 0
    pr_queue = queue.PriorityQueue()
    max_val = max(T)
    while actual_value + capacity < n - 1:
        for i in range(actual_value + 1, actual_value + capacity + 1):
            if i >= n:
                break
            if T[i] != 0:  # nie ma sensu dodawać 0, bo i tak nie zatankujemy 0 litrów ropy
                pr_queue.put(
                    (max_val - T[i], i))  # dodaje krotki (max_val - wartość T na którym stoje, index tego pola)
        actual_value += capacity
        elem = pr_queue.get()  # elem to pierwsza w PriorityQueue ktorka która wygląda tak jak opisałem 2 linijki wyżej
        capacity = max_val - elem[0]  # znów uzyskuje wartośc pola T[i] (wyjaśnione w opisie)
        Out.append(elem[1])
    return sorted(Out)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)
