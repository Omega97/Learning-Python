"""

                                                Generators


- function that returns an object (iterator) which we can iterate over (one value at a time)
- code routine that allows interleaving between user code and library code

It is fairly simple to create a generator in Python.
It is as easy as defining a normal function with yield statement instead of a return statement

The difference is that, while a return statement terminates a function entirely,
yield statement pauses the function saving all its states and later continues from there on successive calls.
"""
from utils import title


@title
def example_1():
    """ generator from a string """

    def gen(string):
        # A simple generator function
        for i in string:
            yield i

    for c in gen("hello"):
        print(c)


@title
def example_2():
    """ powers of 2 """

    def pow_2(max_=0):
        """ 2**n """
        n = 0
        while n < max_:
            yield 2 ** n
            n += 1

    for c in pow_2(5):
        print(c)


@title
def example_3():
    """ type """
    def gen(iterable):
        for i in iterable:
            yield i

    print(type(gen))
    print(gen('abx'))


@title
def example_4():
    """example_4"""
    def gen():
        for j in range(4):
            yield j

    for i in gen():
        print(i)
        print(' do other stuff')


if __name__ == "__main__":

    example_1()
    example_2()
    example_3()
    example_4()
