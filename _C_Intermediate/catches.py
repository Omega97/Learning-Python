"""
Python catches
"""
from copy import copy
from utils import title


@title
def list_catch():
    """ List catch """
    v = [0 for _ in range(3)]
    v = [v for _ in range(3)]
    v[0][0] = 1

    print('expected:\t', [[1, 0, 0], [0, 0, 0], [0, 0, 0]])
    print('returned:\t', v)
    # conclusion: v is a list of the same elements, repeated several times


@title
def method_catch():
    """ Method catch """
    def join_sets(s1, s2):
        s1.update(s2)
        return s1

    a, b = {1}, {2}
    print('previous args:\t', a, b)
    _ = join_sets(a, b)
    print('altered args:\t', a, b)
    # conclusion: a has been altered when join_sets was called


@title
def method_catch_2():
    """ Method catch 2 """

    def f(x):
        a_ = 0
        for i in range(len(x)):
            a_ = x
            print(id(a_) - id(x))
            a_[i] += 1
        return a_

    v = [0, 0, 0]
    print(f(v))
    print(v)
    # conclusion: v has been modified as well


@title
def class_catch():
    """ Class catch """
    class C:
        def __init__(self):
            self.x = 0

    a = C()
    b = a
    b.x = 1
    print('expected:\t', 0, ',', 1)
    print('returned:\t', a.x, ',',  b.x)


@title
def id_catch():
    """ Id catch """
    a = 1
    b = copy(a)
    print('\n', "Same Id" if id(a) == id(b) else "Different Id")


if __name__ == "__main__":

    list_catch()
    method_catch()
    method_catch_2()
    class_catch()
    id_catch()
