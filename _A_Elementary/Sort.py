""" sort iterables """
from utils import title


@title
def sort_example():
    """ .sort() alters the object """
    v = [3, 1, 4, 1, 5]
    print(v)

    v.sort()
    print(v)

    v.sort(reverse=True)
    print(v)


@title
def sort_by_key():
    """ sort by keys """
    v = [['a', 1, 2],
         ['b', 2, 1],
         ['c', 3, 0]]

    def key(x):
        return x[2]

    v.sort(key=key)
    for i in v:
        print(i)


@title
def alphabetical_order():
    """key + lowercase"""
    v = ['a', 'B', 'c', 'abc']
    v.sort(key=lambda x: x.split(' ')[-1].lower())
    print(v)


@title
def sorted_builtin():
    """ sorted (builtin)
    returns a list of sorted items given an iterable """
    print(sorted((3, 1, 2)))
    print(sorted("String"))


# ----------------------------------------------------------------


if __name__ == "__main__":

    sort_example()
    sort_by_key()
    alphabetical_order()
    sorted_builtin()
