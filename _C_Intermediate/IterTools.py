from itertools import *
from utils import title


@title
def permutations_():
    """ permutations """
    v = [1, 2, 3]
    w = permutations(v)
    for i in w:
        print(i)


@title
def combinations_():
    """ combinations """
    v = [1, 2, 3]
    w = combinations(v, 2)
    for i in w:
        print(i)


@title
def combinations_2():
    """ combinations 2 """
    v = [1, 2, 3]
    w = combinations(v, 2)
    for i in w:
        print([1 if j+1 in i else 0 for j in range(len(v))])


@title
def all_comb():
    """ all combinations """
    def wombo_combo(s):
        out = []
        for j in range(len(s)):
            out += [''.join(i) for i in product(s, repeat=j+1)]
        return out

    print(wombo_combo('ab'))
    print(wombo_combo('abc'))


if __name__ == "__main__":

    permutations_()
    combinations_()
    combinations_2()
    all_comb()
