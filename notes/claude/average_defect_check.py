#!/usr/bin/env python3
"""Empirical validation of the exact local densities behind the average-defect
theorem (Phase 5, step 2; claude).

Predictions being tested, for ell=3, over primitive admissible seeds:
  P(p | E_j)          = 2 d_j / (p+1)          (p compatible at level j)
  P(p^2 | E_j)        = 2 d_j / (p(p+1))
  E[(v_p(E_j)-1)^+]   = 2 d_j / (p^2-1)
  mean truncated defect at level j
                      = 2 d_j * sum_{p<=y compat} log p/(p^2-1)
with d_j = 3^j (3-1)/2 = 3^j.  Compatibility at level j: p = +-1 mod 3^{j+1},
p odd, p != 3.  (For j=0 that is every prime p >= 5, plus p=2 excluded since
E_j is odd.)

Deterministic sampling (no RNG): seeds enumerated on a fixed grid.
Standard library only.
"""
import math
from math import gcd, log

L = 3
X = 10**5          # seed box
NMAX = 2           # levels 0..1
PMAX = 3000        # truncation for defect
D = {0: 1, 1: 3}   # d_j for ell=3


def S3(a, b):
    return 3*b - a


def C3(a, b):
    return b - 3*a


def v(x, p):
    n = 0
    x = abs(x)
    while x % p == 0 and x:
        x //= p
        n += 1
    return n


def admissible(a, b):
    if gcd(a, b) != 1 or (a + b) % 2 == 0:
        return False
    if a % 3 != 0:
        return False
    return v(S3(a, b), 3) == 1


def primes_upto(n):
    sieve = bytearray([1]) * (n+1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
    return [i for i in range(2, n+1) if sieve[i]]

PRIMES = primes_upto(PMAX)


def compatible(p, j):
    if p in (2, 3):
        return False
    return (p - 1) % 3**(j+1) == 0 or (p + 1) % 3**(j+1) == 0


def main():
    # Unbiased deterministic sampling: full product grid with strides coprime
    # to every tested prime, and NO first-hit selection (that biased residues
    # mod small p in v1 of this script).
    seeds = []
    stride_a, stride_b = 138, 89     # 138 = 2*3*23, 89 prime; both coprime to
                                     # {5,7,13,17,19,31,37,53}
    for a in range(6, X, stride_a):
        for b in range(1, X, stride_b):
            if admissible(a, b):
                seeds.append((a, b))

    print(f"seeds sampled: {len(seeds)} (box {X}, unbiased product grid)")

    hits1 = {}   # (j,p) -> count p | E_j
    hits2 = {}   # (j,p) -> count p^2 | E_j
    defect = {0: 0.0, 1: 0.0}
    for (a0, b0) in seeds:
        a, b = a0, b0
        for j in range(NMAX):
            s, c = S3(a, b), C3(a, b)
            E = abs(s * c) // 3
            for p in PRIMES:
                if not compatible(p, j):
                    continue
                w = v(E, p)
                if w >= 1:
                    hits1[(j, p)] = hits1.get((j, p), 0) + 1
                if w >= 2:
                    hits2[(j, p)] = hits2.get((j, p), 0) + 1
                if w >= 2:
                    defect[j] += (w - 1) * log(p)
            a, b = a*s*s, b*c*c

    N = len(seeds)
    print("\nlevel j, prime p: empirical vs predicted   P(p|E_j)   P(p^2|E_j)")
    for (j, plist) in ((0, [5, 7, 13, 31]), (1, [17, 19, 37, 53])):
        for p in plist:
            e1 = hits1.get((j, p), 0)/N
            e2 = hits2.get((j, p), 0)/N
            t1 = 2*D[j]/(p+1)
            t2 = 2*D[j]/(p*(p+1))
            print(f"  j={j} p={p:4d}:  {e1:.4f} vs {t1:.4f}    {e2:.5f} vs {t2:.5f}")

    print("\ntruncated mean defect per level (empirical vs theory):")
    for j in range(NMAX):
        theory = 2*D[j]*sum(log(p)/(p*p-1) for p in PRIMES if compatible(p, j))
        print(f"  j={j}: {defect[j]/N:.4f} vs {theory:.4f}")

    # the corrected constant: c_ell(n) partial sums and the majorant bound
    print("\nc_3(n) partial sums (primes up to 10^6 per level):")
    BIG = primes_upto(10**6)
    tot = 0.0
    for j in range(0, 6):
        q = 3**(j+1)
        term = 2*(3**j)*sum(log(p)/(p*p-1) for p in BIG
                            if p > 3 and ((p-1) % q == 0 or (p+1) % q == 0))
        tot += term
        print(f"  level {j}: term {term:.5f}  cumulative c_3({j+1}) ~ {tot:.5f}")
    print("  (geometric decay of the per-level term is the corrected finding;")
    print("   the old O(n^2) heuristic came from a majorant slip, see note)")


if __name__ == "__main__":
    main()
