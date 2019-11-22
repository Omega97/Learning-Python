"""
filter iterables
"""
from utils import title


@title
def simple_dict():
    """ simple dict """
    dic = {'a': 1,
           'b': 2,
           'c': 3,
           'd': 4}

    print(dic['c'])
    print(dic['b'])


@title
def search_a_key():
    """ search a key """

    def search_key(dic_, index):
        return dic_[index] if index in dic_ else None

    dic = {'a': 1}
    print(search_key(dic, 'a'))
    print(search_key(dic, 'x'))


@title
def update_keys():
    """ update_keys """
    dic = {}
    dic.update({'e': 5})
    print(dic)
    dic.clear()
    print(dic)


@title
def join_dicts():
    """ join_dicts """
    a = {'a': 1, 'b': 2}
    b = {'c': 3, 'd': 4}
    c = {**a, **b}
    print(c)


@title
def build_dict():
    """ 2 ways to construct a dict """

    def f(x):
        return x * 10

    # 1) list to dict
    v = [i for i in range(1, 4)]
    word_index = {a: f(a) for a in v}

    print(word_index)

    # 2) list of lists to dict
    v = [[i, f(i)] for i in range(1, 4)]
    word_index = {a: b for a, b in v}

    print(word_index)


@title
def double_index():
    """ double index + loop """
    v = [[str(i), i * 10] for i in range(1, 5)]
    dic = {i: j for i, j in v}
    print(dic)


@title
def dict_items():
    """ double index + loop """
    dic = {'x': 1, 'y': 2, 'z':3}
    print(type(dic.items()))
    print(dic.items())


if __name__ == "__main__":
    simple_dict()
    search_a_key()
    update_keys()
    join_dicts()
    build_dict()
    double_index()
    dict_items()
