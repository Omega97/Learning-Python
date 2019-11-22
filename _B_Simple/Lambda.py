""" write simple functions in one line """
from utils import title


@title
def example_1():
    """ example 1 """
    x = lambda a: a + 10
    print(x(5))


@title
def example_2():
    """ example 2 """
    x = lambda a, b: a * b
    print(x(5, 6))


@title
def example_3():
    """ example 3 """
    x = lambda a, b, c: a + b + c
    print(x(5, 6, 2))


@title
def example_4():
    """ example 4 """

    def f(n):
        return lambda a: a * n

    double = f(2)
    print(double(11))


@title
def example_5():
    """ example 5 """

    def f(n):
        return lambda a: a * n

    mydoubler = f(2)
    mytripler = f(3)

    print(mydoubler(11))
    print(mytripler(11))


@title
def example_5():
    """ parabola """
    def f(a, b, c):
        return lambda x: a * x**2 + b * x + c

    par = f(1, 2, 3)

    print(par(-1))


if __name__ == "__main__":

    example_1()
    example_2()
    example_3()
    example_4()
    example_5()
