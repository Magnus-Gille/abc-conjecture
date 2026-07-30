#!/usr/bin/env python3
"""Claude's independent spot-checks of the prime-genealogy draft.

Written from the manuscript statements alone; does NOT import chebyshev_abc.py.
Checks fresh data not present in Codex's regression suite.
"""
import math
from math import gcd, comb, isclose

def S(l, a, b):
    m = (l - 1) // 2
    return sum((-1)**r * comb(l, 2*r+1) * a**r * b**(m-r) for r in range(m+1))

def C(l, a, b):
    m = (l - 1) // 2
    return sum((-1)**r * comb(l, 2*r) * a**r * b**(m-r) for r in range(m+1))

def vp(x, p):
    if x == 0:
        return None
    v = 0
    while x % p == 0:
        x //= p
        v += 1
    return v

def orbit(l, a0, b0, steps):
    a, b = a0, b0
    out = []
    for _ in range(steps):
        s, c = S(l, a, b), C(l, a, b)
        out.append((a, b, a+b, s, c))
        a, b = a*s*s, b*c*c
    out.append((a, b, a+b, None, None))
    return out

def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    t = pow(a, (p-1)//2, p)
    return 1 if t == 1 else -1

ok = fail = 0
def check(name, cond):
    global ok, fail
    if cond:
        ok += 1
    else:
        fail += 1
        print(f"FAIL: {name}")

# 1. Transfer identity for many (l, a, b)
for l in (3, 5, 7, 11, 13):
    for a, b in ((1, 2), (4, 9), (7, 12), (25, 6), (123, 458)):
        check(f"identity l={l} a={a} b={b}",
              a*S(l, a, b)**2 + b*C(l, a, b)**2 == (a+b)**l)

# 2. Prop 15 root classification, brute force over F_p, fresh cases.
#    F_{n,A} = S_n/l, F_{n,B} = C_n, computed on dehomogenized orbit polys mod p.
def branch_poly_values(l, n, branch, p):
    """Return list of F_{n,branch}(x,1) mod p for x in 0..p-1."""
    vals = []
    linv = pow(l, -1, p)
    for x in range(p):
        a, b = x % p, 1
        for _ in range(n):
            s, c = S(l, a, b) % p, C(l, a, b) % p
            a, b = (a*s*s) % p, (b*c*c) % p
        s, c = S(l, a, b) % p, C(l, a, b) % p
        vals.append((s * linv) % p if branch == 'A' else c % p)
    return vals

cases = [
    # (l, n, branch, p) compatible: m | p-1 or m | p+1, m = l^{n+1} (A) or 2 l^{n+1} (B)
    (3, 0, 'A', 31),   # m=3  | 30
    (3, 1, 'A', 19),   # m=9  | 18
    (3, 1, 'B', 37),   # m=18 | 36
    (3, 1, 'A', 17),   # m=9  | 18 = p+1 (inert)
    (5, 0, 'B', 29),   # m=10 | 30 = p+1
    (5, 1, 'A', 101),  # m=25 | 100
    (7, 0, 'A', 29),   # m=7  | 28
    (7, 0, 'B', 41),   # m=14 | 42 = p+1
]
for l, n, br, p in cases:
    m = l**(n+1) * (2 if br == 'B' else 1)
    chi = 1 if (p-1) % m == 0 else (-1 if (p+1) % m == 0 else 0)
    check(f"compat l={l} n={n} {br} p={p}", chi != 0)
    dn = l**n * (l-1) // 2
    vals = branch_poly_values(l, n, br, p)
    roots = [x for x in range(p) if vals[x] == 0]
    check(f"rootcount l={l} n={n} {br} p={p}: {len(roots)} vs d_n={dn}",
          len(roots) == dn)
    for r in roots:
        check(f"legendre sign l={l} n={n} {br} p={p} rho={r}",
              legendre(-r, p) == chi)
        check(f"rho not 0/-1 l={l} n={n} {br} p={p}", r % p not in (0, (p-1)))
    # converse: incompatible prime has no roots
for l, n, br, p in [(3, 1, 'A', 23), (5, 0, 'A', 13), (7, 0, 'B', 23)]:
    m = l**(n+1)
    if (p-1) % m and (p+1) % m:
        vals = branch_poly_values(l, n, br, p)
        check(f"no-roots l={l} n={n} {br} p={p}",
              all(v != 0 for v in vals))

# 3. Remark 18 seed, recomputed from scratch
a0, b0 = 304260006, 39305
check("R18 gcd", gcd(a0, b0) == 1)
check("R18 parity", (a0 + b0) % 2 == 1)
check("R18 3|a0", a0 % 3 == 0)
check("R18 v3(3b0-a0)=1", vp(3*b0 - a0, 3) == 1)
orb = orbit(3, a0, b0, 2)
_, _, _, s0, c0_ = orb[0]
E0 = abs(s0 * c0_) // 3
check("R18 17 excluded at level 0", E0 % 17 != 0)
_, _, _, s1, c1 = orb[1]
A1 = abs(s1) // 3
check("R18 v17(A1)=2", vp(A1, 17) == 2)
check("R18 chi=-1", legendre(-a0 * b0, 17) == -1)

# 4. My own fresh Theorem 17 instance, built with my own CRT (not in test suite):
#    l=3, prescribe (p,n,eps,h,chi)=(13,0,B,2,+1): m=6 | 13-1, root of C3(X,1)=1-3X
#    Hensel lift mod 13^3: rho_hat = 1/3 mod 2197 = 1465. Impose a0 = 1465+169 mod 2197,
#    b0 = 1 mod 2197, a0 even, b0 odd, a0=3 mod 9, b0=2 mod 9.
from itertools import count
def crt(r1, m1, r2, m2):
    g = gcd(m1, m2)
    assert g == 1
    return (r1 + m1 * ((r2 - r1) * pow(m1, -1, m2) % m2)) % (m1 * m2)

p, h = 13, 2
rho_hat = pow(3, -1, p**(h+1))          # root of 1-3X mod p^{h+1}
a_target = (rho_hat + p**h) % p**(h+1)
M = 2 * 9 * p**(h+1)
abar = crt(crt(a_target, p**(h+1), 0, 2), 2 * p**(h+1), 3, 9)
bbar = crt(crt(1, p**(h+1), 1, 2), 2 * p**(h+1), 2, 9)
found = 0
for t in count(0):
    b0x = bbar + M * t
    if b0x <= 0:
        continue
    a0x = abar
    while a0x <= 0 or gcd(a0x, b0x) != 1:
        a0x += M
    # admissible seed
    check("T17 v3", vp(3*b0x - a0x, 3) == 1)
    orbx = orbit(3, a0x, b0x, 2)
    _, _, _, s0x, c0x = orbx[0]
    B0 = abs(c0x)
    A0 = abs(s0x) // 3
    check(f"T17 seed#{t} v13(B0)=2 (got {vp(B0, 13)})", vp(B0, 13) == 2)
    check(f"T17 seed#{t} 13 not in A0", A0 % 13 != 0)
    check(f"T17 seed#{t} 13 not in seed", (a0x * b0x * (a0x + b0x)) % 13 != 0)
    check(f"T17 seed#{t} chi=+1", legendre(-a0x * b0x, 13) == 1)
    _, _, _, s1x, c1x = orbx[1]
    E1x = abs(s1x * c1x) // 3
    check(f"T17 seed#{t} 13 never reborn at level 1", E1x % 13 != 0)
    found += 1
    if found == 3:
        break

# 5. Theorem 5 radical identity, numeric check on cubic orbit (3,2,5)
a0, b0 = 3, 2
c0 = a0 + b0
theta = math.acos((b0 - a0) / c0)
orb = orbit(3, a0, b0, 2)
def rad(x):
    r, d, y = 1, 2, x
    while d * d <= y:
        if y % d == 0:
            r *= d
            while y % d == 0:
                y //= d
        d += 1
    return r * (y if y > 1 else 1)
for n in (1, 2):
    an, bn, cn = orb[n][0], orb[n][1], orb[n][2]
    Rn = rad(an * bn * cn)
    W = 1
    for j in range(n):
        Ej = abs(orb[j][3] * orb[j][4]) // 3
        W *= Ej // rad(Ej)
    lhs = Rn / cn
    rhs = (rad(a0*b0*c0) / c0) * abs(math.sin(3**n * theta)) / (3**n * math.sin(theta) * W)
    check(f"Thm5 n={n}: {lhs:.6f} vs {rhs:.6f}", isclose(lhs, rhs, rel_tol=1e-9))

# 6. Theorem 13 congruence on quintic orbit E1 primes
for p in (199, 11549, 892254749):
    chi = legendre(-10, p)   # seed (5,2): -a0*b0 = -10
    check(f"Thm13 quintic p={p}: 25 | p-chi", (p - chi) % 25 == 0)

print(f"\n{ok} checks passed, {fail} failed")
