"""Find all squares in the first p index residues and test first appearances."""

import argparse
from fractions import Fraction
from math import gcd

from hall_pell_crt import fib_pair, primes_through


def square_root_mod_prime(a, p):
    """One square root modulo the odd prime p, or None for a nonsquare."""
    a %= p
    if not a:
        return 0
    if p % 4 == 3:
        x = pow(a, (p + 1) // 4, p)
        return x if x * x % p == a else None
    if pow(a, (p - 1) // 2, p) != 1:
        return None
    odd = p - 1
    depth = 0
    while odd % 2 == 0:
        odd //= 2
        depth += 1
    nonresidue = 2
    while pow(nonresidue, (p - 1) // 2, p) == 1:
        nonresidue += 1
    c, t, x = pow(nonresidue, odd, p), pow(a, odd, p), pow(a, (odd + 1) // 2, p)
    while t != 1:
        level, power = 1, t * t % p
        while power != 1:
            power = power * power % p
            level += 1
        b = pow(c, 1 << (depth - level - 1), p)
        c, x, depth = b * b % p, x * b % p, level
        t = t * c % p
    return x


def lift_root(a, p):
    x = square_root_mod_prime(a, p)
    if x is None:
        return None
    assert x != 0  # The discriminants in this family have prime divisors only 2,3,5.
    return x + p * (((a - x * x) // p) * pow(2 * x, -1, p) % p)


def first_divisibility(p, last_j):
    u, v, f, g = 29 % p, 9349 % p, 13 % p, 4181 % p
    for j in range(last_j + 1):
        if u == 11 % p or f == 0 or ((u - 6)**2 - 20) % p == 0 or ((u - 9)**2 - 5) % p == 0:
            return j
        u, v = v, (322 * v - u) % p
        f, g = g, (322 * g - f) % p
    return None


def squared_labels(p, j):
    modulus = p * p
    f, g = fib_pair(7 + 12 * j, modulus)
    u = (2 * g - f) % modulus
    return [label for label, value in [('A', (u - 6)**2 - 20), ('B', (u - 9)**2 - 5)]
            if value % modulus == 0]


def initial_squares(p):
    """All (p,n,label) with p^2 dividing the quadratic and 0 <= j < p."""
    if p % 5 not in (1, 4):
        return [], False
    modulus = p * p
    half = (modulus + 1) // 2
    s = lift_root(5, p)
    alpha = (1 + s) * half % modulus
    alpha_quotient = (pow(alpha, p - 1, modulus) - 1) // p
    if alpha_quotient == 0:
        u, v = 29 % modulus, 9349 % modulus
        hits = []
        for j in range(p):
            for label, value in [('A', (u-6)**2-20), ('B', (u-9)**2-5)]:
                if value % modulus == 0:
                    hits.append((p, 7 + 12*j, label))
            u, v = v, (322*v-u) % modulus
        return hits, True

    inverse = pow(12 * alpha_quotient, -1, p)
    hits = set()
    for label, u in [('A', 6+2*s), ('A', 6-2*s), ('B', 9+s), ('B', 9-s)]:
        root = lift_root(u * u + 4, p)
        if root is None:
            continue
        beta = (u + root) * half % modulus
        quotient = (pow(beta, p - 1, modulus) - 1) // p
        # The second root is -1/beta, whose Fermat quotient has opposite sign.
        for target, q in [(beta, quotient), ((u - root) * half % modulus, -quotient)]:
            j = (q - 7 * alpha_quotient) * inverse % p
            if pow(alpha, 7 + 12*j, p) == target % p:
                assert pow(alpha, 7 + 12*j, modulus) == target
                assert label in squared_labels(p, j)
                hits.add((p, 7 + 12*j, label))
    return sorted(hits), False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prime-limit', type=int, default=100_000_000)
    parser.add_argument('--direct-check-through', type=int, default=2000)
    args = parser.parse_args()
    hits, first_hits, exceptional = [], [], []
    for p in primes_through(args.prime_limit):
        if p < 7:
            continue
        found, singular = initial_squares(p)
        hits.extend(found)
        if found:
            earliest = min((n-7)//12 for _, n, _ in found)
            period_bound = (p-1)//gcd(12, p-1)
            if earliest < period_bound and first_divisibility(p, earliest) == earliest:
                first_hits.extend(row for row in found if row[1] == 7 + 12*earliest)
        if singular:
            exceptional.append(p)
        if p <= args.direct_check_through and p % 5 in (1, 4):
            u, v = 29 % (p*p), 9349 % (p*p)
            expected = []
            for j in range(p):
                for label, value in [('A', (u-6)**2-20), ('B', (u-9)**2-5)]:
                    if value % (p*p) == 0:
                        expected.append((p, 7+12*j, label))
                u, v = v, (322*v-u) % (p*p)
            assert sorted(expected) == sorted(found)
    print("Hits with 0 <= j < p:", hits)
    if hits:
        print("Largest p/n in these hits:", max(Fraction(p,n) for p,n,_ in hits))
    print("First appearances already squared in a quadratic:", first_hits)
    print("Split primes with zero Fermat quotient for alpha:", exceptional)


if __name__ == '__main__':
    main()
