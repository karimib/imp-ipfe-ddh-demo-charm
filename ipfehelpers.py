import random


class MPK:
    h = None

    def __init__(self, h):
        self.h = h


class MSK:
    s = None

    def __init__(self, s):
        self.s = s


class CT:
    ct0 = None
    cti = None

    def __init__(self, ct0, cti):
        self.ct0 = ct0
        self.cti = cti


class SKy:
    key = None

    def __init__(self, key):
        self.key = key


def inner_product(a, b):
    """
    Calculates inner product of group element vector and integer vector
    Args:
        a: group elements vector
        b: integer vector

    Returns: inner product of the vectors

    """
    n = len(a)
    inner = 0
    for i in range(n):
        inner += a[i] * b[i]
    return inner

