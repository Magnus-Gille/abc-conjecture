"""Verify the modular and residue calculations for the 3-free part of s_n."""

from math import gcd, isqrt

from abc_dyadic_fourth_factor import inert_trace, pari


WITNESSES = {
    2: (23,),
    3: (7, 223),
    5: (31, 191),
    7: (71, 113),
}


def excluded_classes(q, p):
    assert p > 3 and all(p % d for d in range(2, isqrt(p) + 1))
    assert (p - 1) % q == 0
    exponent = (p - 1) // q
    state = (31 % p, 14 % p, 2273 % p)
    seen = set()
    values = set()
    while state not in seen:
        seen.add(state)
        u, v, w = state
        values.add(pow((u*u + 8*v*v) % p, exponent, p))
        state = ((u**4 - 32*v**4) % p, 2*u*v*w % p, (w**4 - 128*(u*v)**4) % p)
    assert 0 not in values
    return {a for a in range(q) if pow(3, a * exponent, p) not in values}


def finite_field_traces():
    def rational_trace(prime, coefficient):
        squares = {x*x % prime for x in range(1, prime)}
        total = 0
        for x in range(prime):
            value = x*(x*x + 4*x + coefficient) % prime
            if value:
                total += 1 if value in squares else -1
        return -total

    for prime, expected_x, expected_ratio in [(17, 1, 13), (47, 32, 4)]:
        x = 31**2 * pow(14**2, -1, prime) % prime
        form = (x*x + 16*x + 32) % prime
        assert x == expected_x
        assert (x*x - 32)**2 * pow(4*x*form, -1, prime) % prime == x
        assert 8*x * pow(form, -1, prime) % prime == expected_ratio
    assert rational_trace(7, 2) == 0
    for tau in (7, 10):
        assert tau*tau % 17 == 15
        assert rational_trace(17, 2*(1 + 13*tau) % 17) == 4
    assert inert_trace(47) == 4


def common_determinant(left, right):
    return gcd(int(pari.matdet(left)), int(pari.matdet(left + right)),
               int(pari.matdet(left - right)))


def hecke_support():
    pari.allocatemem(350_000_000, silent=True)
    aggregate = set()
    for odd_part in (1, 3):
        for k in range(11):
            level = odd_part * 2**k
            space = pari.mfinit([level, 2], 0)
            if int(pari.mfdim(space)) == 0:
                continue
            h7 = pari.mfheckemat(space, 7)**2
            h17 = pari.mfheckemat(space, 17)**2 - 16
            h47 = pari.mfheckemat(space, 47)**2 - 98
            value = common_determinant(h47, h17)
            assert value > 0
            for p in (2, 3, 5, 7):
                if value % p == 0:
                    aggregate.add(p)
                while value % p == 0:
                    value //= p
            assert value == 1, level
            assert common_determinant(h47, h7) % 17, level
            assert common_determinant(h17, h7) % 47, level
    assert aggregate == {2, 3, 5, 7}


if __name__ == "__main__":
    finite_field_traces()
    for q, primes in WITNESSES.items():
        covered = set().union(*(excluded_classes(q, p) for p in primes))
        assert covered == set(range(q))
    hecke_support()
    print("Three traces, all exact-level determinant tests and all seven residue witnesses passed.")
