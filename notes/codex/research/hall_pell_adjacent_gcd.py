"""Verify the exact neighboring gcd for the two Lucas quadratics."""

from math import gcd, prod

from sympy import factorint, resultant, symbols


def quadratics(x):
    return (x - 6) ** 2 - 20, (x - 9) ** 2 - 5


def resultant_factors():
    x, y = symbols("x y")
    invariant = 29**2 + 9349**2 - 322 * 29 * 9349
    conic = x**2 + y**2 - 322 * x * y - invariant
    expected = [
        {2: 24, 3: 4, 5: 5, 29: 1, 61: 1, 151: 2},
        {2: 8, 3: 4, 59: 1, 61: 1, 197699: 1, 14119141: 1},
        {2: 8, 3: 4, 59: 1, 61: 1, 197699: 1, 14119141: 1},
        {2: 20, 3: 8, 5: 5, 79: 2, 2081: 1},
    ]
    factorizations = [
        factorint(abs(resultant(h, resultant(g, conic, x), y)))
        for g in quadratics(x) for h in quadratics(y)
    ]
    assert factorizations == expected
    return factorizations


def adjacent_hits(modulus):
    initial = 29 % modulus, 9349 % modulus
    u, v = initial
    j = 0
    hits = []
    while True:
        a, b = quadratics(u)
        if a * b % modulus == 0:
            a, b = quadratics(v)
            if a * b % modulus == 0:
                hits.append(j)
        u, v = v, (322 * v - u) % modulus
        j += 1
        if (u, v) == initial:
            return j, hits


def main():
    factors = resultant_factors()
    candidates = {int(p) for row in factors for p in row if p > 5}
    expected = {
        59: (29, [14]),
        79: (13, [12]),
        197699: (98849, [44283]),
        14119141: (1176595, [222004]),
    }
    for prime in sorted(candidates):
        period, hits = adjacent_hits(prime)
        if prime in expected:
            assert (period, hits) == expected[prime]
            if any(row.get(prime, 0) > 1 for row in factors):
                assert adjacent_hits(prime**2)[1] == []
        else:
            assert not hits

    common_period = 1
    first_maximum = 30165452234189
    for period, hits in expected.values():
        assert gcd(common_period, period) == 1
        common_period *= period
        assert first_maximum % period == hits[0]
    assert first_maximum < common_period
    print("Maximum neighboring gcd:", 5 * prod(expected))
    print("First attaining j:", first_maximum, "with period", common_period)


if __name__ == "__main__":
    main()
