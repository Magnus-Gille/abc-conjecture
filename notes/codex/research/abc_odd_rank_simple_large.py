"""Verify large, simple prime divisors, using only the Python standard library."""
import json
from functools import cache
from math import gcd, isqrt, prod
from pathlib import Path

from abc_octic_mixed_simple_density import division_at_r0
from abc_odd_rank_quartic_cutoff import (
    denominator, full_packet, norm_denominator, prime_divisors, split_generator,
)


def verify():
    data = json.loads(Path(__file__).with_name('abc_odd_rank_simple_large_cert.json').read_text())

    @cache
    def prove_prime(p):
        if p <= 10000:
            assert p > 1 and all(p % i for i in range(2, isqrt(p)+1))
            return
        g, factors = data['primality'][str(p)]
        assert prod(q**e for q, e in factors) == p-1
        assert all(e > 0 for _, e in factors)
        assert pow(g, p-1, p) == 1
        for q, _ in factors:
            prove_prime(q)
            assert gcd(pow(g, (p-1)//q, p)-1, p) == 1

    rows = data['witnesses']
    for n, p, r, full in rows:
        prove_prime(p)
        assert p > n**4 and n % r == 0
        w = division_at_r0(p*p)
        assert w(n) % p == 0 and w(n) != 0
        assert w(r) % p == 0
        assert all(w(r//q) % p for q in prime_divisors(r))
        if n <= 75:
            B = denominator(n)
            assert B % p == 0 and B % (p*p) != 0
            assert full == int(full_packet(n) % p == 0)
        else:
            assert prime_divisors(n) == (n,) and full == 0
            assert norm_denominator(*split_generator(n)) % p == 0
    small = {n for n, _, _, _ in rows if n <= 75}
    assert len(rows) == len({row[0] for row in rows})
    print('Certified odd indices 7–75:', len(small), 'of 35')
    print('Gaps:', sorted(set(range(7, 76, 2))-small))
    print('Additional certified prime indices:', [r[0] for r in rows if r[0] > 75])
    print('Exact scalar order n among the 7–75 examples:', sum(n == r for n, _, r, _ in rows if n <= 75))


if __name__ == '__main__':
    verify()
