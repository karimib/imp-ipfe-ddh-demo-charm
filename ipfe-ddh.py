import random
from charm.toolbox.pairinggroup import PairingGroup, G1
from ipfehelpers import random_vector, MPK, MSK, CT, inner_product_mod, SKy


group = PairingGroup("SS512")
g = group.random(G1)
p = group.order()

l = 5


def setup(l):
    s = random_vector(0, p, l)
    h = [g ** s[i] for i in range(l)]

    return MPK(h), MSK(s)


def encrypt(mpk, x):
    r = random.randint(0, p)
    c = []
    c.append(g**r)
    for i in range(l):
        c.append((mpk.h[i] ** r) * (g ** x[i]))

    return CT(c[0], c[1:])


def keyder(msk, y):
    return SKy(inner_product_mod(y, msk.s, p))


def decrypt(mpk, ct, sk, y):
    res = 1
    for i in range(l):
        res *= ct.cti[i] ** y[i]

    divisor = ct.ct0**sk.key
    res /= divisor

    return res


def main():
    mpk, msk = setup(l)
    x = random_vector(0, p, l)
    ct = encrypt(mpk, x)
    y = random_vector(0, p, l)
    sk = keyder(msk, y)
    res = decrypt(mpk, ct, sk, y)

    expected = inner_product_mod(x, y, p)
    print("<x,y> ", expected)
    print("g^<x,y>: ", g**expected)
    print("Decrypted result: ", res)


main()
