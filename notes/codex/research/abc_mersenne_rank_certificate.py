"""Verify first-rank and lifting factors for 2^n-1 with exact integer arithmetic."""

from math import lcm, prod


def factor(n):
    """Complete trial factorization, including factor(1) = {}."""
    factors = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        factors[n] = 1
    return factors


def order(p):
    """Order of 2 modulo the odd prime p."""
    r = p - 1
    for q in factor(r):
        while r % q == 0 and pow(2, r // q, p) == 1:
            r //= q
    return r


def check_depth(n, p, e):
    residue = pow(2, n, p ** (e + 1))
    assert (residue - 1) % p**e == 0 and residue != 1
    return (residue - 1) // p**e


def lifting_factor(n):
    return prod(p**e for p, e in factor(n).items() if p != 2 and n % order(p) == 0)


def closure(n):
    while True:
        extended = lcm(n, *(order(p) for p in factor(n) if p != 2))
        if extended == n:
            return n
        n = extended


def check_small_indices(limit):
    first_rank = {}
    for n in range(1, limit + 1):
        m = 2**n - 1
        factors = factor(m)
        # The first-rank excess at n only uses primes first appearing at n.
        first_rank[n] = prod(p**(e - 1) for p, e in factors.items() if order(p) == n)
        first_product = prod(first_rank[r] for r in range(1, n + 1) if n % r == 0)
        assert m // prod(factors) == first_product * lifting_factor(n)
    print(f'Exact excess identity verified by complete factorization for 1 <= n <= {limit}.')


def check_wieferich():
    hits = [p for p in range(3, 3512, 2)
            if factor(p) == {p: 1} and pow(2, p - 1, p*p) == 1]
    assert hits == [1093, 3511]
    print('Base-2 Wieferich primes through 3511:', *hits)
    ranks = []
    for p, r, quotient in ((1093, 364, 891), (3511, 1755, 1781)):
        assert order(p) == r
        assert check_depth(r, p, 2) == quotient
        assert lifting_factor(r) == 1
        check_depth(r * p, p, 3)
        ranks.append(r)
        print(f'p={p}: order {r}, depth 2 at {r}, depth 3 at {r*p}; '
              f'(2^{r}-1)/p^2 mod p = {quotient}.')

    n = lcm(*ranks)
    assert n == 49140 and closure(n) == n
    assert [closure(r) for r in ranks] == [1092, 7020]
    assert {p: order(p) for p in factor(n) if p != 2} == {3: 2, 5: 4, 7: 3, 13: 12}
    lift = lifting_factor(n)
    assert lift == 12285 and n // lift == 4
    for p, e in ((3, 4), (5, 2), (7, 2), (13, 2), (1093, 2), (3511, 2)):
        check_depth(n, p, e)
    print(f'n={n} is closed; ordinary lifting factor {lift}, penalty {n//lift}, '
          f'certified excess factor {lift * prod(hits)}.')


if __name__ == '__main__':
    check_small_indices(60)
    check_wieferich()
