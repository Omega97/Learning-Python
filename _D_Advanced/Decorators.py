"""
A decorator is a function that takes another function
and extends the behavior of the latter function
without explicitly modifying it
"""
from utils import title
from time import time
from random import random


@title
def example_1():
    """ example 1 """
    def a(f):
        # simple decorator
        def wrapper():
            # wrapping method
            print("pre-Whee")
            f()
            print("post-Whee")
        return wrapper

    @a
    def say_whee():
        # dummy method
        print("Whee!")

    say_whee()


@title
def example_2():
    """ example 2 """
    def a(f):
        # decorator with arguments
        def wrapper(*args, **kwargs):
            print('before')
            f(*args, **kwargs)
            print('after')

        return wrapper

    @a
    def fun(s):
        print(s)

    fun('fun')


@title
def example_3():
    """ example 3 """
    def do_twice(f):
        # repeat attributes twice
        def wrapper():
            f()
            f()
        return wrapper

    @do_twice
    def greet(name='Bosa'):
        print(f"Hello {name}")

    greet()


@title
def example_4():
    """ example 4 """
    def a(f):
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper

    @a
    def fun(name):
        print("fun call")
        return f"Hi {name}"

    print(fun('Omar'))


@title
def take_time_decorator():
    """ example 5 """
    def take_time(f):
        # take the time it takes to execute a method
        def wrapper():
            t0 = time()
            f()
            print('t = %.5f s' % (time()-t0))
        return wrapper

    @take_time
    def foo():
        for _ in range(10**5):
            pass

    foo()


@title
def example_6():
    """ example 6 """
    def dec(f):
        print('init dec')

        def w(*ar, **kw):
            print('w', ar, kw)
            return f(*ar, *kw)
        return w

    @dec
    def fun(*args, **kwargs):
        print('fun', args, kwargs)
        return 'output', args, kwargs

    print()
    print(fun, '\n')
    print(fun(1, k=2), '\n')


@title
def decorator_with_variables():
    """ decorator with variables """

    def repeat(n=2):
        def wrapper(fun):
            def wrapper2(*args, **kwargs):
                for _ in range(n):
                    fun(*args, **kwargs)

            return wrapper2

        return wrapper

    @repeat(n=3)
    def f(x):
        print(x)

    f('again')


@title
def take_time_n_times():    # todo fix
    """ decorator with variables """
    def repeat(n=2):
        t = time()

        def wrapper(fun):
            def wrapper2(*args, **kwargs):
                for _ in range(n):
                    fun(*args, **kwargs)
            return wrapper2
        print((time() - t) / n)
        return wrapper

    @repeat(n=5)
    def test():
        return sorted([random() for _ in range(10000)])

    control = time()

    test()

    print(time() - control)


if __name__ == "__main__":
    example_1()
    example_2()
    example_3()
    example_4()
    take_time_decorator()
    example_6()
    decorator_with_variables()
    take_time_n_times()
