"""
                                                Context manager
"""
from utils import title


@title
def example_1():

    class ContextManager:
        def __init__(self, n=0):
            self.n = n

        def __repr__(self):
            return f'CM({self.n})'

        def __enter__(self):
            """setup"""
            print('__enter__')
            return self

        def __exit__(self, *args):
            """tear-down"""
            print('__exit__')

    with ContextManager(4) as cm:
        print(cm)


@title
def example_2():
    """ensure self.n is above 0 after operations"""

    class ContextManager:
        def __init__(self, n=0):
            self.n = n

        def __repr__(self):
            return f'CM({self.n})'

        def __sub__(self, other):
            self.n -= other
            return self

        def __enter__(self):
            """setup"""
            print('__enter__')
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            """tear-down"""
            self.n = max(self.n, 0)
            print('__exit__')

    with ContextManager(4) as cm:
        print(cm - 5)
    print(cm)


if __name__ == '__main__':
    example_1()
    example_2()
