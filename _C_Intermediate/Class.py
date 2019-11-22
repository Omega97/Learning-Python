from utils import title


@title
def example_1():
    """initialization"""
    class C:

        def __init__(self, n=0):
            self.n = n

    a = C(1)
    print(a.n)


@title
def example_2():
    """representation"""
    class C:

        def __init__(self, n=0):
            self.n = n

        def __repr__(self):
            return f'C({self.n})'

    a = C(1)
    print(a)


@title
def example_3():
    """addition & subtraction"""
    class C:

        def __init__(self, n=0):
            self.n = n

        def __repr__(self):
            return f'C({self.n})'

        def __add__(self, other):
            self.n += other
            return self

        def __sub__(self, other):
            self.n -= other
            return self

    a = C(1)
    a += 3
    print(a)
    a -= 2
    print(a)


@title
def example_4():
    """call"""
    class C:

        def __init__(self, n=0):
            self.n = n

        def __repr__(self):
            return f'C({self.n})'

        def __add__(self, other):
            self.n += other
            return self

        def __sub__(self, other):
            self.n -= other
            return self

        def __call__(self, *args, **kwargs):
            return self.n

    a = C(1)
    print(a())


@title
def example_5():
    """call"""
    class C:

        def __init__(self, v: list):
            self.v = v

        def __repr__(self):
            return f'C({self.v})'

        def __add__(self, other):
            self.v += other
            return self

        def __sub__(self, other):
            self.v -= other
            return self

        def __call__(self, *args, **kwargs):
            return self.v

        def __getitem__(self, item):
            return self.v[item]

        def __setitem__(self, key, value):
            self.v[key] = value

    a = C(['a', 'b', 'c'])
    print(a[0])
    a[1] = 'new'
    print(a)


if __name__ == '__main__':
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()
