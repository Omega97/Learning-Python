from functools import partial
from utils import title


@title
def example_1():
    """basic custom operator"""
    class Infix:

        def __init__(self, func):
            print('> init ', func)
            self.func = func

        def __or__(self, other):
            print('> or ', other)
            return self.func(other)

        def __ror__(self, other):
            print('> ror ', other)
            return Infix(partial(self.func, other))

    @Infix
    def add(x, y):
        return x + y

    print(5 | add | 6)


@title
def example_2():
    """test operator assert 5 == 5 WHILE using 5 to do 1 + 5"""
    class Infix:

        def __init__(self, func):
            print('> init ', func)
            self.func = func

        def __or__(self, other):
            print('> or ', other)
            return self.func(other)

        def __ror__(self, other):
            print('> ror ', other)
            return Infix(partial(self.func, other))

    @Infix
    def test(x, y):
        assert x == y
        return x

    print(1 + (5 | test | 5))


@title
def example_3():
    """ custom """
    class Infix:

        def __init__(self, func):
            print('> init ', func)
            self.func = func

        def __or__(self, other):
            print('> or ', other)
            return self.func(other)

        def __ror__(self, other):
            print('> ror ', other)
            return self.func(other)

        def __call__(self, x):
            print('> call ', x)
            return self.func(x)

    @Infix
    def test(x):
        assert round(x) == x
        return x

    print(5 | test)


if __name__ == '__main__':
    example_1()
    example_2()
    # example_3()
