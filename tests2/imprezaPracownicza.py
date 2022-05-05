import random


class Employee:
    def __init__(self, fun):
        self.fun = fun
        self.emp = []
        self.f = -1
        self.g = -1





def create_empolyers():
    r=5
    emp0 = Employee(random.randint(0, r))
    emp1 = Employee(random.randint(0, r))
    emp2 = Employee(random.randint(0, r))
    emp3 = Employee(random.randint(0, r))
    emp11 = Employee(random.randint(0, r))
    emp12 = Employee(random.randint(0, r))
    empG = Employee(random.randint(0, r))
    emp1.emp.append(emp0)
    emp11.emp.append(emp1)
    emp11.emp.append(emp2)
    emp12.emp.append(emp3)
    empG.emp.append(emp12)
    empG.emp.append(emp11)
    print(empG.fun)
    print(f'{emp11.fun} | {emp12.fun}')
    print(f'{emp1.fun}, {emp2.fun} | {emp3.fun}')
    print(emp0.fun)
    return empG


def g(v: Employee):
    if v.g != -1:
        return v.g
    v.g = 0
    for u in v.emp:
        v.g += f(u)
    return v.g


def f(v: Employee):
    if v.f != -1:
        return v.f
    v.f = v.fun
    for u in v.emp:
        v.f += g(u)
    v.f = max(g(v), v.f)
    return v.f


if __name__ == '__main__':
    emp = create_empolyers()

    print(f(emp))
