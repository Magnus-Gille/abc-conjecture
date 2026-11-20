"""Exact prime and order certificates for the two moving marks."""

from math import gcd, isqrt, prod

from abc_octic_mixed_prime_indices import multiple


CERTIFICATES = {
    22151840117633: (3, {2: 7, 59: 1, 14321: 1, 204821: 1}),
    7393900643053507997: (2, {2: 2, 7: 1, 347: 1, 15461: 1, 49220783671: 1}),
    49220783671: (3, {2: 1, 3: 1, 5: 1, 83: 1, 149: 1, 132667: 1}),
}


def prove_prime(p):
    if p not in CERTIFICATES:
        assert 2 <= p < 210000
        assert all(p % i for i in range(2, isqrt(p) + 1))
        return
    generator, factors = CERTIFICATES[p]
    assert prod(q ** e for q, e in factors.items()) == p - 1
    assert pow(generator, p - 1, p) == 1
    for q in factors:
        prove_prime(q)
        assert gcd(pow(generator, (p - 1) // q, p) - 1, p) == 1


def verify():
    p16, p19 = 22151840117633, 7393900643053507997
    prove_prime(p16)
    prove_prime(p19)
    assert multiple(19, p19) is None  # The finite integral A has order 19.
    u, v = 31, 14
    w8 = isqrt(u ** 4 + 16 * u ** 2 * v ** 2 + 32 * v ** 4)
    assert w8 == 2273
    u, v = abs(u ** 4 - 32 * v ** 4), 2 * u * v * w8
    assert u ** 4 + 16 * u ** 2 * v ** 2 + 32 * v ** 4 == p16 ** 2
    assert (4 * 8443 + 615) % 34387 == 0
    assert (57 * 8443 + 167) % 34387 == 0
    print('Verified the two prime collisions and both short congruences.')


if __name__ == '__main__':
    verify()
