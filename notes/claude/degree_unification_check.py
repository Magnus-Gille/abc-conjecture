#!/usr/bin/env python3
"""Numerical verification for the degree-unification note (Phase 5, step 3).

Checks:
  A. ell=2 quadratic transfer (a,b) -> (4ab, (b-a)^2):
     A1. T_2 semiconjugacy and the SAME radical telescope identity
         R_n/c_n = (R_0/c_0)|sin(2^n t)|/(2^n sin t W_n) on (1,8,9).
     A2. Unified atom normalization  2*E_n = |Phi_{2^{n+1}}(alpha,beta)|
         (exactly the odd-prime formula ell*E_n = |Phi_{ell^{n+1}}(alpha,beta)|
         continued to ell=2), with E_n = |b_n - a_n|.
     A3. NEW programmed-square realization at ell=2: level-1 atom
         X^2-6XY+Y^2, prescription (p,n,h,chi)=(7,1,2,-1): three seeds
         with v_7(E_1)=2 exactly, 7 absent from seed and E_0, chi=-1.
  B. Composite odd degree:
     B1. Chain identities S_15 = S_3(a,b)*S_5(a3,b3) = S_5(a,b)*S_3(a5,b5)
         and the C-analogues (exact, with signs).
     B2. ell=9 = 3^2: S_9 = S_3(a,b)*S_3(a3,b3), hence
         v_3(S_9) = v_3(S_3(a,b)) + v_3(S_3(a3,b3)); generic value 2,
         degenerate seeds give 3 (the corrected normalization condition).
     B3. Atom rationality spot check: Phi_3(w,wbar)=S_3, Phi_5(w,wbar)=S_5.

Standard library only; written independently of chebyshev_abc.py.
"""
import math
from math import comb, gcd

ok = fail = 0
def check(name, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1
        print("FAIL:", name)

def S(l, a, b):
    m = (l - 1)//2
    return sum((-1)**r*comb(l, 2*r+1)*a**r*b**(m-r) for r in range(m+1))

def C(l, a, b):
    m = (l - 1)//2
    return sum((-1)**r*comb(l, 2*r)*a**r*b**(m-r) for r in range(m+1))

def v(x, p):
    n = 0; x = abs(x)
    while x and x % p == 0: x //= p; n += 1
    return n

def rad(x):
    r, d = 1, 2
    while d*d <= x:
        if x % d == 0:
            r *= d
            while x % d == 0: x //= d
        d += 1
    return r*(x if x > 1 else 1)

# ---------- A. ell = 2 ----------
def t2(a, b):
    return 4*a*b, (b-a)**2

# A1: telescope on (1,8,9)
a0, b0 = 1, 8
c0 = a0 + b0
theta = math.acos((b0-a0)/c0)
a, b = a0, b0
W = 1
R0 = rad(a0*b0*c0)
for n in range(1, 5):
    E = abs(b - a)
    W *= E // rad(E)
    a, b = t2(a, b)
    cn = a + b
    check(f"A1 c_{n} = c0^(2^n)", cn == c0**(2**n))
    Rn = rad(a*b*cn)
    lhs = Rn/cn
    rhs = (R0/c0)*abs(math.sin(2**n*theta))/(2**n*math.sin(theta)*W)
    check(f"A1 telescope n={n}: {lhs:.6g} vs {rhs:.6g}",
          math.isclose(lhs, rhs, rel_tol=1e-9))

# A2: unified atom normalization 2 E_n = |Phi_{2^{n+1}}(alpha,beta)|
# alpha,beta = (b0-a0) +- 2 sqrt(-a0 b0);  alpha^k + beta^k computed by the
# integer Lucas recursion  L_k = P L_{k-1} - Q L_{k-2},  P = 2(b0-a0),
# Q = alpha*beta = (b0-a0)^2 + 4 a0 b0 = c0^2.
def lucas_L(k, P, Q):
    x, y = 2, P          # L_0, L_1
    for _ in range(k-1):
        x, y = y, P*y - Q*x
    return y if k >= 1 else x

for (sa, sb) in ((1, 8), (3, 4), (7, 2), (5, 12)):
    if gcd(sa, sb) != 1 or (sa+sb) % 2 == 0: continue
    P, Q = 2*(sb-sa), (sa+sb)**2
    a, b = sa, sb
    for n in range(0, 4):
        E = abs(b-a)
        # Phi_{2^{n+1}}(alpha,beta) = alpha^{2^n} + beta^{2^n}  (n>=1);
        # for n=0 it is alpha+beta = P.
        val = P if n == 0 else lucas_L(2**n, P, Q)
        check(f"A2 seed({sa},{sb}) n={n}: 2E_n=|Phi|", 2*E == abs(val))
        a, b = t2(a, b)

# A3: programmed square for ell=2, prescription (p,n,h,chi)=(7,1,2,-1)
# level-1 atom in seed coordinates: b1-a1 = (Y-X)^2-4XY = X^2-6XY+Y^2
p, h = 7, 2
f = lambda x: x*x - 6*x + 1
# Hensel-lift the root 2 of f mod 7 to mod 7^{h+1}
r = 2
for k in range(1, h+1):
    mod = p**(k+1)
    fp = (2*r - 6) % mod
    r = (r - f(r)*pow(fp, -1, mod)) % mod
check("A3 lift valid", f(r) % p**(h+1) == 0 and r % p == 2)
M = 2*p**(h+1)
a_target = (r + p**h) % p**(h+1)
found = 0
t = 0
while found < 3:
    t += 1
    b0x = 1 + p**(h+1)*(2*t)          # odd, = 1 mod 7^3
    a0x = a_target if a_target % 2 == 0 else a_target + p**(h+1)
    while gcd(a0x, b0x) != 1:
        a0x += 2*p**(h+1)
    check(f"A3 seed{t} parity/prim", (a0x+b0x) % 2 == 1 and gcd(a0x, b0x) == 1)
    E0 = abs(b0x - a0x)
    check(f"A3 seed{t} 7 not in E0", E0 % 7 != 0)
    check(f"A3 seed{t} 7 not in seed", (a0x*b0x*(a0x+b0x)) % 7 != 0)
    a1, b1 = t2(a0x, b0x)
    E1 = abs(b1 - a1)
    check(f"A3 seed{t} v7(E1)=2 (got {v(E1,7)})", v(E1, 7) == 2)
    leg = pow((-a0x*b0x) % 7, 3, 7)
    check(f"A3 seed{t} chi=-1", leg == 7-1)
    found += 1

# ---------- B. composite odd degree ----------
def step(l, a, b):
    return a*S(l, a, b)**2, b*C(l, a, b)**2

# B1: chain identities for ell = 15
for (sa, sb) in ((2, 5), (4, 9), (14, 3), (8, 21)):
    a3, b3 = step(3, sa, sb)
    a5, b5 = step(5, sa, sb)
    check(f"B1 S15 chain-3 ({sa},{sb})",
          S(15, sa, sb) == S(3, sa, sb)*S(5, a3, b3))
    check(f"B1 S15 chain-5 ({sa},{sb})",
          S(15, sa, sb) == S(5, sa, sb)*S(3, a5, b5))
    check(f"B1 C15 chain-3 ({sa},{sb})",
          C(15, sa, sb) == C(3, sa, sb)*C(5, a3, b3))
    check(f"B1 C15 chain-5 ({sa},{sb})",
          C(15, sa, sb) == C(5, sa, sb)*C(3, a5, b5))
    # the transferred triples agree along both chains (commuting semigroup)
    check(f"B1 orbit commutes ({sa},{sb})",
          step(5, *step(3, sa, sb)) == step(3, *step(5, sa, sb))
          == step(15, sa, sb))

# B2: ell = 9 valuation additivity and the corrected normalization
for (sa, sb) in ((3, 2), (6, 1), (3, 8), (12, 1), (21, 2), (30, 1)):
    a3, b3 = step(3, sa, sb)
    check(f"B2 S9 chain ({sa},{sb})",
          S(9, sa, sb) == S(3, sa, sb)*S(3, a3, b3))
    lhs = v(S(9, sa, sb), 3)
    rhs = v(S(3, sa, sb), 3) + v(S(3, a3, b3), 3)
    check(f"B2 v3 additivity ({sa},{sb}): {lhs}", lhs == rhs)
# generic admissible-for-3 seed: v3(S3)=1 and second step automatic 1 -> total 2
check("B2 generic v3(S9)=2", v(S(9, 3, 2), 3) == 2)
# degenerate: v3(3b-a)=2 at the seed, e.g. (a,b)=(12,1): 3b-a=-9
check("B2 degenerate v3(S9)=3", v(S(9, 12, 1), 3) == 3)

# B3: atom rationality identities
for (sa, sb) in ((2, 5), (4, 9), (1, 8)):
    bma, c = sb - sa, sa + sb
    phi3 = 2*bma + c
    phi5 = 2*(bma*bma - 4*sa*sb) + 2*c*bma + c*c
    check(f"B3 Phi3=S3 ({sa},{sb})", phi3 == S(3, sa, sb))
    check(f"B3 Phi5=S5 ({sa},{sb})", phi5 == S(5, sa, sb))

print(f"\n{ok} checks passed, {fail} failed")
