"""Exhaustive new p² | sqrt(Y_l) scan for inert prime ranks l and p <= bound."""
from functools import lru_cache
from math import isqrt
import sys

from abc_octic_mixed_prime_indices import multiple


def prime_sieve(n):
    flags = bytearray(b'\x01')*(n+1)
    flags[:2] = b'\x00\x00'
    for d in range(2,isqrt(n)+1):
        if flags[d]:
            start = d*d
            flags[start:n+1:d] = b'\x00'*((n-start)//d+1)
    return flags


def division_value(n, modulus):
    """psi_n evaluated at A=(1,1), on v²=u³−8u²+8u."""
    initial = (0,1,2,-45,868)
    inv2 = (modulus+1)//2

    @lru_cache(None)
    def psi(i):
        if i < 5:
            return initial[i] % modulus
        k = i//2
        if i & 1:
            value = psi(k+2)*psi(k)**3 - psi(k-1)*psi(k+1)**3
        else:
            value = psi(k)*inv2*(psi(k+2)*psi(k-1)**2-psi(k-2)*psi(k+1)**2)
        return value % modulus

    return psi(n)


def candidates(bound, flags):
    limit = isqrt(bound//2)
    for l in range(5,limit+1):
        if not flags[l] or l % 8 not in (5,7):
            continue
        for v in range(l,limit+1,l):
            xmax = isqrt(bound-2*v*v)
            amin = -((xmax+1)//l)
            amax = (xmax-1)//l
            for a in range(amin,amax+1):
                u = 1+a*l
                p = u*u+2*v*v
                if flags[p] and p > 5:
                    yield l,p


def main():
    bound = int(sys.argv[1]) if len(sys.argv)>1 else 10**7
    flags = prime_sieve(bound)
    total, hits_y, hits_u = 0,0,0
    exceptional_y, exceptional_u = [],[]
    y_rows, u_rows = [],[]
    for l,p in candidates(bound, flags):
        total += 1
        value = division_value(3*l,p*p)
        if value % p:
            continue
        u,v = multiple((3*l+1)//2,p)
        x = (v+u)*pow(2*(u-1),-1,p) % p
        hit_y = (x*x+2) % p == 0
        hit_u = ((x-1)**2+1) % p == 0
        assert hit_y != hit_u
        # Independent direct check of the designated integer norm mod p³.
        modulus = p**3
        deep_u,deep_v = multiple((3*l+1)//2,modulus)
        slope = (deep_v+deep_u)*pow(2*(deep_u-1),-1,modulus) % modulus
        norm = slope*slope+2 if hit_y else (slope-1)**2+1
        assert norm % (p*p) == 0
        assert (norm % modulus == 0) == (value == 0)
        (y_rows if hit_y else u_rows).append((l,p))
        if hit_y:
            hits_y += 1
        else:
            hits_u += 1
        if value == 0:
            triple = division_value(3*l,p**3)
            (exceptional_y if hit_y else exceptional_u).append((l,p,triple))
    print(f'p <= {bound}; {total} norm-representation pairs')
    print(f'Y ranked primes ({len(set(l for l,p in y_rows))} distinct ranks): {sorted(y_rows)}')
    print(f'U- ranked primes in the candidate set: {sorted(u_rows)}')
    print(f'Y: {hits_y} first-appearance pairs, exceptional {exceptional_y}')
    print(f'U-: {hits_u} first-appearance pairs in the candidate set, exceptional {exceptional_u}')


if __name__ == '__main__':
    main()
