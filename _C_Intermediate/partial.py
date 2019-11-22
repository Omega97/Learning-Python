"""Return a new partial object which when called will behave like func called
with the positional arguments args and keyword arguments keywords"""
from utils import title
from functools import partial


@title
def example_1():
    """demo"""
    def f(*args):
        print(args)

    partial(f, 1)(2, 3, 4)


@title
def example_2():
    """base converter"""
    base_2 = partial(int, base=2)
    print(base_2('10010'))  # print(int('10010', base=2))


if __name__ == '__main__':
    example_1()
    example_2()
