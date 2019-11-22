""" Lists ... """
from utils import title


@title
def simple_list():
    """ simple list """
    v = [0, 1, 2]
    print(v)


@title
def iteration():
    """ iteration """
    v = [i for i in range(4)]
    print(v)


@title
def join_lists():
    """ join lists """
    v = [1, 2] + [3, 4]
    print(v)


@title
def append_to_list():
    """ append to lists """
    v = list([0, 1])
    v.append(2)
    print(v)


@title
def multiply_lists():
    """ multiply lists """
    v = [1, 2] * 4
    print(v)


@title
def iterate_over_range():
    """iterate over a range"""
    v = [i * 2 for i in range(4)]
    print(v)


@title
def iterate_over_string():
    """inter over a string """
    v = [i for i in '1234']
    print(v)


@title
def conditional():
    """  conditional """
    v = [i for i in range(1, 10) if i % 3 == 0]
    print(v)


# ----------------------------------------------------------------


if __name__ == "__main__":

    simple_list()
    iteration()
    join_lists()
    append_to_list()
    multiply_lists()
    iterate_over_range()
    iterate_over_string()
    conditional()
