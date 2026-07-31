#!/usr/bin/env python3
"""Verification for notes/claude/quadratic-realization.md (Theorem Q17).

Covers the four check items of mailbox/0083:
  1. Prop Q15 root criterion at index 2^{n+2}: counts, simplicity, signs,
     and no-root incompatible cases, for n = 0..3 across several primes.
  2. Multi-prescription realization D = {(17,0,3,+1),(7,1,2,-1),(31,2,1,-1)}
     on three distinct seeds: exact valuations, cross-level avoidance
     through level 3.
  3. 2-adic CRT modulus M = 2 * prod p^{h+1} with parity conditions.
  4. Primitivity, positivity, seed-prime avoidance, distinctness.

Standard library only; independent of chebyshev_abc.py / chebyshev_research.py.
"""
from math import gcd

ok = fail = 0
def check(name, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1
        print("FAIL:", name)

def t2(a, b):
    return 4*a*b, (b-a)**2

def G_poly_values(n, p):
    """G_n(x,1) mod p for all x, via direct orbit iteration."""
    vals = []
    for x in range(p):
        a, b = x % p, 1
        for _ in range(n):
            a, b = (4*a*b) % p, (b-a)**2 % p
        vals.append((b - a) % p)
    return vals

def legendre(a, p):
    a %= p
    if a == 0: return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1

def v(x, p):
    n = 0; x = abs(x)
    while x and x % p == 0: x //= p; n += 1
    return n

# ---- 1. Prop Q15 root classification ----
compat_cases = [
    (0, 5, 1), (0, 7, -1), (0, 13, 1), (0, 11, -1),   # m=4
    (1, 17, 1), (1, 7, -1), (1, 23, -1), (1, 41, 1),  # m=8
    (2, 17, 1), (2, 31, -1), (2, 97, 1), (2, 47, -1), # m=16
    (3, 97, 1), (3, 31, -1), (3, 191, -1),            # m=32
]
for n, p, chi in compat_cases:
    m = 2**(n+2)
    check(f"Q15 compat n={n} p={p}", (p - chi) % m == 0)
    vals = G_poly_values(n, p)
    roots = [x for x in range(p) if vals[x] == 0]
    check(f"Q15 count n={n} p={p}: {len(roots)} vs 2^{n}", len(roots) == 2**n)
    for r in roots:
        check(f"Q15 sign n={n} p={p} rho={r}", legendre(-r, p) == chi)
        check(f"Q15 rho!=0,-1 n={n} p={p}", r not in (0, p-1))
incompat_cases = [(1, 3), (1, 5), (1, 13), (2, 7), (2, 11), (2, 19), (3, 17)]
for n, p in incompat_cases:
    m = 2**(n+2)
    if (p-1) % m and (p+1) % m:
        vals = G_poly_values(n, p)
        check(f"Q15 no roots n={n} p={p}", all(x != 0 for x in vals))

# ---- 2-4. Theorem Q17 realization ----
def hensel_root(n, p, h, chi):
    """A root of G_n(X,1) mod p with sign chi, lifted mod p^{h+1}."""
    vals = G_poly_values(n, p)
    roots = [x for x in range(p) if vals[x] == 0 and legendre(-x, p) == chi]
    assert roots, (n, p, chi)
    r = roots[0]
    # Newton-lift on exact integer orbit values: G_n at (x,1) via bigints
    def G(x, mod):
        a, b = x % mod, 1
        for _ in range(n):
            a, b = (4*a*b) % mod, (b-a)**2 % mod
        return (b - a) % mod
    for k in range(1, h+1):
        mod = p**(k+1)
        # derivative numerically: (G(r+p^k*t)-G(r))/p^k has unit coefficient;
        # solve G(r + p^k * t) = 0 mod p^{k+1} by scanning t in 0..p-1
        found = None
        for t in range(p):
            if G(r + p**k * t, mod) % mod == 0:
                found = r + p**k * t
                break
        assert found is not None, (n, p, k)
        r = found
    return r  # root mod p^{h+1}

def crt(r1, m1, r2, m2):
    assert gcd(m1, m2) == 1
    return (r1 + m1 * ((r2 - r1) * pow(m1, -1, m2) % m2)) % (m1*m2)

D = [(17, 0, 3, 1), (7, 1, 2, -1), (31, 2, 1, -1)]
for p, n, h, chi in D:
    check(f"Q17 compat ({p},{n},{h},{chi})", (p - chi) % 2**(n+2) == 0)

# build congruence classes
M = 2
abar, bbar = 0, 1                        # a even, b odd
for p, n, h, chi in D:
    rho = hensel_root(n, p, h, chi)
    a_t = (rho + p**h) % p**(h+1)
    abar = crt(abar, M, a_t, p**(h+1))
    bbar = crt(bbar, M, 1, p**(h+1))
    M *= p**(h+1)

seeds = []
t = 0
while len(seeds) < 3:
    t += 1
    b0 = bbar + M * t
    # a0 = abar mod M and a0 = 1 mod b0 (second CRT); positive rep
    a0 = crt(abar, M, 1 % b0, b0)
    if a0 <= 0: a0 += M * b0
    seeds.append((a0, b0))

seen = set()
for idx, (a0, b0) in enumerate(seeds):
    check(f"Q17 seed{idx} positive", a0 > 0 and b0 > 0)
    check(f"Q17 seed{idx} parity", a0 % 2 == 0 and b0 % 2 == 1)
    check(f"Q17 seed{idx} primitive", gcd(a0, b0) == 1)
    check(f"Q17 seed{idx} distinct", (a0, b0) not in seen)
    seen.add((a0, b0))
    # orbit through level 3
    a, b = a0, b0
    E = []
    for j in range(4):
        E.append(abs(b - a))
        a, b = t2(a, b)
    for p, n, h, chi in D:
        check(f"Q17 seed{idx} v_{p}(E_{n})={h} (got {v(E[n],p)})",
              v(E[n], p) == h)
        for j in range(4):
            if j != n:
                check(f"Q17 seed{idx} {p} absent E_{j}", E[j] % p != 0)
        check(f"Q17 seed{idx} {p} absent seed",
              (a0 * b0 * (a0 + b0)) % p != 0)
        check(f"Q17 seed{idx} chi({p})", legendre(-a0*b0, p) == chi)
    check(f"Q17 seed{idx} E odd", all(e % 2 == 1 for e in E))

print(f"\n{ok} checks passed, {fail} failed")
