""" Sub-classes """
from utils import title


@title
def example1():
    """Animal"""
    class Animal:

        def __init__(self):
            self.name = None
            self.cute = True
            self.food = 0

        def feed(self):
            self.food += 1

    class Neko(Animal):

        def __init__(self, name):
            super().__init__()
            self.name = name

    cat = Neko('Leo')
    print(cat.name)
    print(cat.cute)
    cat.feed()
    print(cat.food)


@title
def example2():
    """Super"""
    class Super:

        def __init__(self, x=0):
            self.super_att = x

    class Sub(Super):

        def __init__(self, y=0, **kwargs):
            super(Sub, self).__init__(**kwargs)
            self.sub_att = y

    a = Sub(x=1, y=2)
    print(a.super_att)
    print(a.sub_att)


if __name__ == '__main__':

    example1()
    example2()
