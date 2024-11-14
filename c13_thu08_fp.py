"""
c13 assignment
group id: c13_thu00
file submission: c13_thu00_fp.py
submission deadline: Sun 17 Nov 2024 before midnight (23:59)

1. create a class named Employee with the following fields:
_eid, _name, _salary
with a constructor (__init__), all getter/setter methods
and __str__ method

2. create a list of at list 6 employees

3. create the following functions to
3.1 filter a list of Employees who has salary > 1000
3.2 map a list of Employees to a list of Employee's name
3.3 compute an average salary of all Employees on a list
*** 
a) write 3.1-3.3 using functional programming style
b) generalize 3.1-3.3 so that the functions can receive
other functions for filtering, mapping, or reduction
"""

from typing import Callable
from functools import reduce

def imperative():
    print(5)
    x = 3.8
    print(x)


def functional():
    x: int = 5
    print(x)

    # store a function in a variable
    def f(p: int) -> int: return 10 * p
    y: Callable[[int],int] = f
    print(y(6))

    # pass a function as a parameter to another function
    # that "another" function is called "higher-order function"
    def g(h: Callable[[int],int], v: int) -> int:
        return h(v + 3)
    print(g(f, 5))

    # anonymous function
    z: Callable[[int], int] = lambda i : i ** 2
    print(z(25))
    print(g(z,5))
    print(g(lambda i: i / 2, 9))

    # return a function as a return value from another function
    # that "another" function is called "higher-order function"
    def k() -> Callable[[int],int]:
        return lambda j: j % 5
    print(k()(17))
    a:Callable[[int],int] = k()
    print(a(23))

class T:
    _cls_data: int = None
    _cls_func: Callable = NotImplemented

    @classmethod
    def get_cls_data(cls) -> int: return cls._cls_data
    @classmethod
    def get_cls_func(cls) -> Callable: return cls._cls_func
    @classmethod
    def set_cls_data(cls, data): cls._cls_data = data
    @classmethod
    def set_cls_func(cls, func): cls._cls_func = func
    @classmethod
    def cls_run(cls): return cls._cls_func(cls._cls_data)

    def __init__(self, data: int, func: Callable):
        self._data = data
        self._func = func

    def get_data(self): return self._data
    def get_func(self): return self._func
    def set_data(self, data): self._data = data
    def set_func(self, func): self._func = func

def oop_fp():
    T.set_cls_data(5)
    T.set_cls_func(lambda i: i * 100)
    print(T.cls_run())
    T.set_cls_func(lambda i: i ** 2)
    print(T.cls_run())
    print(T.get_cls_func()(12))
    t = T(13, lambda j: j % 10)
    print(t.get_func()(t.get_data()))

def higher():
    # common higher-order functions
    # map, filter, reduce, ...
    # lisp = list processing
    data = ["Peter","Michael","Smith","Johnson","Albert"]

    # map
    print(list(map(len,data)))

    result = []
    for i in data: result.append(len(i))
    print(result)

    def initial(s): return s[0]
    x = map(initial,data)
    print(list(x))
    print(list(map(lambda s: s[0], data)))

    # filter
    print(list(filter(lambda s: len(s)==5,data)))

    print(list(map(lambda s: s[0], filter(lambda s: len(s) >=6, data))))

    # reduce
    print(reduce(lambda x, y: x + ", " + y, data))
    print(reduce(lambda x, y: x + ", " + y, data, "START"))


def main():
    #imperative()
    #functional()
    #oop_fp()
    higher()


if __name__ == "__main__":
    main()