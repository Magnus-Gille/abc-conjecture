"""Check the cubic Belyi example for reduced inputs with denominator at most 250."""

from itertools import combinations
from math import gcd

FORMS = ((1, 0), (-1, 1), (0, 1), (3, -2), (3, 1))


def prime_support(value):
    primes = set()
    p = 2
    while p * p <= value:
        if value % p == 0:
            primes.add(p)
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        primes.add(value)
    return primes


def det(left, right):
    return left[0] * right[1] - left[1] * right[0]


def check(limit=250):
    # The only possible good primes in an image come from these five forms.
    small_support = [prime_support(i) for i in range(4 * limit + 1)]
    relations = []
    for i, j, k in combinations(range(len(FORMS)), 3):
        scales = (det(FORMS[j], FORMS[k]), det(FORMS[k], FORMS[i]), det(FORMS[i], FORMS[j]))
        relations.append(tuple(zip((i, j, k), scales)))

    checked = 0
    for z in range(2, limit + 1):
        for x in range(1, z):
            if gcd(x, z) != 1 or 3 * x == 2 * z:
                continue
            values = [a * x + b * z for a, b in FORMS]
            left = 27 * x**2 * (z - x)
            right = (3 * x - 2 * z)**2 * (3 * x + z)
            total = 4 * z**3
            assert left + right == total
            common = gcd(left, right)
            assert 108 % common == 0
            output = (left // common, right // common, total // common)
            marked = [small_support[abs(value)] - {2, 3} for value in values]
            counts = {p: 0 for part in marked for p in part}
            assert len(counts) == sum(map(len, marked))
            assert all(any(coord % p == 0 for coord in output) for p in counts)
            for relation in relations:
                terms = [values[i] * scale for i, scale in relation]
                assert sum(terms) == 0
                for p in set().union(*(marked[i] for i, _ in relation)):
                    counts[p] += 1
            assert all(multiplicity == 6 for multiplicity in counts.values())
            checked += 1
    print(f"Verified the cubic and its ten relations at {checked} reduced inputs through denominator {limit}.")


if __name__ == "__main__":
    check()
