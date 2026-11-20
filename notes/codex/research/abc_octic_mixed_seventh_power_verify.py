"""Local two-descent and torsion checks for Y^2=X^7+6^7, in Python 3."""

from functools import lru_cache
from itertools import product
from math import gcd


# In the chosen unramified cubic, z is a seventh root of unity. The sum
# t=z+z^2+z^4 is the even 2-adic root of t^2+t+2=0.
MOD = 2**15
t, = [u for u in range(0, MOD, 2) if (u*u+u+2) % MOD == 0]
one = (1, 0, 0)
z = (0, 1, 0)


def add(a, b):
    return tuple((x+y) % MOD for x, y in zip(a, b))


def scale(a, c):
    return tuple((c*x) % MOD for x in a)


def mul(a, b):
    w = [0]*5
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            w[i+j] += x*y
    for i in (4, 3):
        w[i-1] += t*w[i]
        w[i-2] += (1+t)*w[i]
        w[i-3] += w[i]
    return tuple(v % MOD for v in w[:3])


def power(a, n):
    result = one
    while n:
        if n & 1:
            result = mul(result, a)
        n //= 2
        a = mul(a, a)
    return result


def frobenius(a):
    return add((a[0], 0, 0), add(scale(power(z, 2), a[1]), scale(power(z, 4), a[2])))


def mod8(a):
    return tuple(x % 8 for x in a)


unit_squares = {mod8(mul(a, a)) for a in product(range(8), repeat=3)
                if any(x % 2 for x in a)}


@lru_cache(None)
def unit_class(a):
    return min(mod8(mul(a, s)) for s in unit_squares)


def squareclass(a):
    assert any(a)
    v = min((x & -x).bit_length()-1 for x in a if x)
    assert v <= 12  # Three digits of the normalized unit remain available.
    return v % 2, unit_class(mod8(tuple(x // 2**v for x in a)))


def class_mul(a, b):
    return a[0] ^ b[0], unit_class(mod8(mul(a[1], b[1])))


def pair_mul(a, b):
    return class_mul(a[0], b[0]), class_mul(a[1], b[1])


def check_local():
    assert power(z, 7) == one and frobenius(z) == power(z, 2)
    assert len(unit_squares) == 28
    embeddings = (z, power(z, 6))
    trivial = squareclass(one)
    identity = trivial, trivial
    T = tuple(squareclass(scale(add(v, scale(one, -1)), 6)) for v in embeddings)
    gens = [T]
    for degree, x in [(1, (1, 0, 0)), (1, (14, 0, 0)),
                      (3, (0, 0, 14)), (3, (0, 6, 2))]:
        assert squareclass(add(power(x, 7), scale(one, 6**7))) == trivial
        orbit = [x] if degree == 1 else [x, frobenius(x), frobenius(frobenius(x))]
        images = []
        for v in embeddings:
            value = one
            for xx in orbit:
                value = mul(value, add(xx, scale(v, 6)))
            images.append(squareclass(value))
        gens.append(tuple(images))
    local = {identity}
    for g in gens:
        local |= {pair_mul(g, w) for w in local}
    assert len(local) == 32
    print("Five dyadic generators:")
    for g in gens:
        print(g)

    # The surviving odd-place basis is e_1,e_2,2,-3,1-z.
    def globals_at(v):
        return [add(v, power(v, 6)), add(power(v, 2), power(v, 5)),
                scale(one, 2), scale(one, -3), add(one, scale(v, -1))]
    basis = list(zip(*(map(squareclass, globals_at(v)) for v in embeddings)))
    accepted = []
    for bits in product(range(2), repeat=5):
        val = identity
        for b, y in zip(bits, basis):
            if b:
                val = pair_mul(val, y)
        if val in local:
            accepted.append(bits)
    assert accepted == [(0, 0, 0, 0, 0), (0, 0, 1, 1, 1)]
    print("Surviving global classes:", accepted)


def counts_11():
    # Both x^7 maps are permutations in degrees one and two.
    # In F_11^3 use t^3+t+4, irreducible by checking its 11 values.
    p = 11
    assert all((i**3+i+4) % p for i in range(p))
    def prod(a, b):
        w = [0]*5
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                w[i+j] += x*y
        for i in (4, 3):
            w[i-2] -= w[i]
            w[i-3] -= 4*w[i]
        return tuple(v % p for v in w[:3])
    elems = list(product(range(p), repeat=3))
    squares = {prod(a, a) for a in elems}
    n3 = 1
    for x in elems:
        x2 = prod(x, x)
        x7 = prod(prod(x2, x2), prod(x2, x))
        y2 = (x7[0]+6**7) % p, x7[1], x7[2]
        n3 += 1 if y2 == (0, 0, 0) else 2*int(y2 in squares)
    return p+1, p*p+1, n3


if __name__ == "__main__":
    check_local()
    # p=5 has order 6 mod 7, p=11 order 3. Newton identities and
    # reciprocity give T^6 + (N3-p^3-1)/3 T^3 + p^3 at either prime.
    assert all(gcd(7, 5**i-1) == 1 for i in (1, 2, 3))
    assert all(gcd(7, 11**i-1) == 1 for i in (1, 2))
    n1, n2, n3 = counts_11()
    assert (n1, n2, n3) == (12, 122, 1464)
    j5 = 1+5**3
    j11 = 1+(n3-11**3-1)//3+11**3
    assert (j5, j11, gcd(j5, j11)) == (126, 1376, 2)
    print("Counts at 11:", n1, n2, n3, "Jacobian orders:", j5, j11)
