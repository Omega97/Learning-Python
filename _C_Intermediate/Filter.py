"""
filter iterables
"""
from utils import title


@title
def example_1():
    """ Filter out values <= 5 """
    v = [i for i in range(10)]
    print(v)
    print(list(filter(lambda x: x > 5, v)))


@title
def example_2():
    """ Filter out False elements """
    v = [0, 1, True, False, "", "a", (), [], {}, [0], None]
    print(v)
    print(list(filter(None, v)))


if __name__ == "__main__":

    example_1()
    example_2()
