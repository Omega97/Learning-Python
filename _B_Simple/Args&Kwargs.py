""" Args & Kwargs """
from utils import title


@title
def demo_1():
    """ print args & kwargs """

    def f(*args, **kwargs):
        """ print args & kwargs """

        print('\nargs\t', type(args))

        for i in args:
            print(i)

        print('\nkwargs\t', type(kwargs))

        for i in kwargs:
            print(i, '=', kwargs[i])

    f(0, 1, 2, s='3', t='4')


@title
def demo_2():
    """ impose kwargs """
    def f(*args, **kwargs):
        """ print args & kwargs """
        print(args, kwargs)

    a = 1, 2
    kw = {'c': 3, 'd': 4}

    f(*a, **kw)


if __name__ == "__main__":

    demo_1()
    demo_2()
