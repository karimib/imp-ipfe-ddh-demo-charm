from charm.toolbox.integergroup import IntegerGroup
from charm.core.math.integer import getMod, toInt
import numpy as np
from ipfehelpers import (
    inner_product,
    MPK,
    MSK,
    CT,
    SKy,
)

l = 5
sec_bits = 512

group = IntegerGroup()
group.paramgen(sec_bits)
g = group.randomGen()
p = int(getMod(g))


def random_vector(l, p):
    vector = [group.random() % p for _ in range(l)]
    return [int(toInt(vector[i])) for i in range(l)]


def setup(l):
    s = random_vector(l, p)
    h = [g ** s[i] for i in range(l)]

    return MPK(h), MSK(s)


def encrypt(mpk, x):
    r = int(toInt(group.random()))
    c0 = g ** r
    ci = [(mpk.h[i] ** r) * (g ** x[i]) for i in range(l)]

    return CT(c0, ci)


def keyder(msk, y):
    return SKy(inner_product(msk.s, y))


def decrypt(mpk, ct, sk, y):
    res = np.prod([ct.cti[i] ** y[i] for i in range(l)])
    res /= ct.ct0**sk.key

    return res



def main():
    mpk, msk = setup(l)
    x = random_vector(l, p)
    ct = encrypt(mpk, x)
    y = random_vector(l, p)
    sk = keyder(msk, y)
    res = decrypt(mpk, ct, sk, y)

    expected = inner_product(x, y)
    print("<x,y> ", expected)
    print("g^<x,y>: ", g**expected)
    print("Decrypted result: ", res)


main()
