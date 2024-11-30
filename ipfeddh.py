from charm.toolbox.integergroup import IntegerGroup
from charm.core.math.integer import getMod, toInt
from ipfehelpers import (
    MPK,
    MSK,
    CT,
    SKy,
)


class IPFEDDH:
    group = None
    p = None
    g = None

    def __init__(self, sec_bits):
        self.group = IntegerGroup()
        self.group.paramgen(sec_bits)
        self.g = self.group.randomGen()
        self.p = int(getMod(self.g))

    def random_vector(self, l, p):
        vector = [self.group.random() % p for _ in range(l)]
        return [int(toInt(vector[i])) for i in range(l)]


    def setup(self, l):
        s = self.random_vector(l, self.p)
        h = [self.g ** s[i] for i in range(l)]

        return MPK(h), MSK(s)

    def encrypt(self, mpk, x, l):
        r = int(toInt(self.group.random()))
        c0 = self.g**r
        ci = [(mpk.h[i] ** r) * (self.g ** x[i]) for i in range(l)]

        return CT(c0, ci)

    def keyder(self, msk, y, l):
        inner = sum(y[i] * msk.s[i] for i in range(l))
        return SKy(inner)

    def decrypt(self, mpk, ct, sk, y, l):
        tmp = [int(toInt(ct.cti[i] ** y[i])) for i in range(l)]
        res = 1
        for i in range(len(tmp)):
            res *= tmp[i]

        res /= ct.ct0**sk.key

        return res
