"""Census of all potential w_n primes <= 10^12 at dyadic n >= 16384."""

from functools import cache
from math import isqrt
import sys


def primes_up_to(bound):
    flags = bytearray([1]) * (bound + 1)
    flags[:2] = bytes(2)
    for p in range(2, isqrt(bound) + 1):
        if flags[p]:
            flags[p*p::p] = bytes((bound - p*p)//p + 1)
    return [p for p in range(2, bound + 1) if flags[p]]


def signed_packet(n, modulus):
    u, v, w = 31, 14, 2273
    for _ in range(n.bit_length() - 4):
        u4, v4 = pow(u, 4, modulus), pow(v, 4, modulus)
        u, v, w = ((u4 - 32*v4) % modulus, 2*u*v*w % modulus,
                   (pow(w, 4, modulus) - 128*u4*v4) % modulus)
    return w % modulus


def packet_square(n, modulus):
    X, Y = 961 % modulus, 196 % modulus
    for _ in range(n.bit_length() - 4):
        F = (X*X + 16*X*Y + 32*Y*Y) % modulus
        X, Y = (X*X - 32*Y*Y)**2 % modulus, 4*X*Y*F % modulus
    return (X*X + 16*X*Y + 32*Y*Y) % modulus


def census(bound):
    trial_primes = primes_up_to(isqrt(bound))

    @cache
    def prime(value):
        for ell in trial_primes:
            if ell*ell > value:
                break
            if value % ell == 0:
                return False
        return True

    n = 16384
    rows = []
    details = []
    while 8*n*n + 1 <= bound:
        pairs = 0
        candidates = set()
        for b in range(1, isqrt(bound//(8*n*n)) + 1):
            vertical = 8*n*n*b*b
            width = isqrt(bound - vertical)
            low = -((width + 1)//(2*n))
            high = (width - 1)//(2*n)
            for a in range(low, high + 1):
                pairs += 1
                value = (1 + 2*n*a)**2 + vertical
                if not prime(value):
                    continue
                candidates.add(value)
                residue = signed_packet(n, value)
                residue2 = signed_packet(n, value**2)
                assert residue2 % value == residue
                assert packet_square(n, value**2) == residue2**2 % (value**2)
                assert residue != 0
                details.append((n, a, b, value, residue, residue2))
        rows.append((n, pairs, len(candidates)))
        n *= 2
    return rows, details


if __name__ == '__main__':
    expected = {
        10**11: [(16384,92,6),(32768,21,1),(65536,3,0)],
        10**12: [(16384,1005,59),(32768,242,17),(65536,59,4),
                 (131072,12,1),(262144,3,0)]
    }
    for bound, answer in expected.items():
        rows, details = census(bound)
        assert rows == answer
        if '--csv' in sys.argv:
            if bound == 10**12:
                print('n,a,b,p,w_mod_p,w_mod_p_squared')
                for record in details:
                    print(*record, sep=',')
        else:
            print(bound, rows, len({r[3] for r in details}), 'distinct candidates, no hits')
