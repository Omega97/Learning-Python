""" useful methods for the demos """


def title(fun):
    """ Add a title from the first line of the docstring to the console output
    if no docstring is given, then rakes the name of the method"""
    def wrapper(*args, **kwargs):
        if fun.__doc__:
            print('\n\t', fun.__doc__.split('\n')[0])
        else:
            print('\n\t', fun.__qualname__.replace('_', ' '))
        print()
        fun(*args, **kwargs)
        print()
    return wrapper


if __name__ == '__main__':

    @title
    def f_1():
        print('first function')

    f_1()


    @title
    def f_2():
        """The title
        Not the title"""
        print('second function')

    f_2()
