"""
An iterator is an object:
  - that contains a countable number of values.
  - that can be iterated upon
  - which implements the iterator protocol, which consist of the methods __iter__() and __next__().

Examples:
    - list
    - tuple
    - any class with consist of the methods __iter__() and __next__()
"""
from utils import title


@title
def build_list():
    """ build a list
    range is an object doesn't produce numbers immediately;
    it is a smart sequence object that produces numbers on demand
    """
    v = [i ** 2 for i in range(4)]
    print(v)
    for i in v:
        print(i)


@title
def recursive_list():
    """ recursive list """
    a = 1
    for i in range(3):
        a = [a, a]
        print(a)


@title
def double_index():
    """ double_index """
    w = [[+i, -i] for i in range(5)]
    for i, j in w:
        print(i, j)


@title
def range_iterator():
    """ range """
    r = range(2, 6)
    print(r)
    print(type(r))


if __name__ == "__main__":

    build_list()
    recursive_list()
    double_index()
    range_iterator()
