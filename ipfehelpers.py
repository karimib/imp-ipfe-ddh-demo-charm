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


def inner_product_mod(vector1, vector2, p):
    """
    Computes the inner product (dot product) of two vectors modulo p.

    Args:
        vector1 (list[int or float]): The first vector.
        vector2 (list[int or float]): The second vector.
        p (int): The modulus.

    Returns:
        int: The inner product of the two vectors modulo p.

    Raises:
        ValueError: If the vectors are not of the same length.
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same length")

    # Compute the inner product modulo p
    return sum(vector1[i] * vector2[i] for i in range(len(vector1))) % p


def random_vector(low, high, n):
    """
    Generates a random vector with elements from range [a, b].

    Args:
        a (int): The lower bound (inclusive).
        b (int): The upper bound (inclusive).
        n (int): The size of the vector.

    Returns:
        list[int]: A vector (list) of random integers.
    """
    return [random.randint(low, high - 1) for _ in range(n)]
