"""
The difference between assignation, shallow copy and deep copy
"""
from utils import title


@title
def no_copy():
    """ no copy """
    a = [['a', 'a'], ['a', 'a']]
    print('old a =', a)
    b = a
    b[0] = ['b']
    b[1][0] = 'b'
    b[1][1] = 'b'
    print('new a =', a)
    print('    b =', b)
    print('\n', "Same Id" if id(a) == id(b) else "Different Id")
    # conclusion: a and b are the same object


@title
def do_copy():
    """ copy """
    a = [['a', 'a'], ['a', 'a']]
    print('old a =', a)
    b = copy(a)
    b[0] = ['b']
    b[1][0] = 'b'
    b[1][1] = 'b'
    print('new a =', a)
    print('    b =', b)
    print('\n', "Same Id" if id(a) == id(b) else "Different Id")
    # conclusion: a and b are different objects, but the child objects are the same


@title
def do_deepcopy_copy():
    """ deepcopy """
    a = [['a', 'a'], ['a', 'a']]
    print('old a =', a)
    b = deepcopy(a)
    b[0] = ['b']
    b[1][0] = 'b'
    b[1][1] = 'b'
    print('new a =', a)
    print('    b =', b)
    print('\n', "Same Id" if id(a) == id(b) else "Different Id")
    # conclusion: a and b are completely different objects


if __name__ == "__main__":

    no_copy()
    do_copy()
    do_deepcopy_copy()
