class Node:
    def __init__(self):
        self.val = None  # przechowywana liczba rzeczywista
        self.next = None  # odsyłacz do nastepnego elementu


def reversing(first):
    p = first
    while p.next is not None:
        tmp = p.next
        p.next = tmp.next
        tmp.next = first
        first = tmp
    return first


def printer(p):
    while p is not None:
        print(f'{p.val} ')
        p = p.next


if __name__ == '__main__':
    p = Node()
    p.val = 0
    q = p
    q.next = Node()
    q = q.next
    q.val = 1
    q.next = Node()
    q = q.next
    q.val = 2
    q.next = Node()
    q = q.next
    q.val = 3
    q.next = Node()
    q = q.next
    q.val = 4
    q.next = Node()
    q = q.next
    q.val = 5
    q.next = Node()
    q = q.next
    q.val = 6
    q.next = Node()
    q = q.next
    q.val = 7
    q.next = Node()
    q = q.next
    q.val = 8
    p = reversing(p)
    printer(p)
