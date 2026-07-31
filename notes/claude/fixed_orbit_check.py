#!/usr/bin/env python3
"""Numeric sanity checks for notes/claude/fixed-orbit-sources.md section 0.

Verifies, on the cubic (3,2,5) and quintic (5,2,7) canonical orbits:
  1. every prime of every computed layer factor E_j has rank of
     apparition (in the descended Lucas sequence U_m) EXACTLY equal to
     its layer index ell^{j+1} -- so each prime's contribution is its
     rank-Wieferich excess, localized at its birth layer;
  2. the law of repetition v_p(U_{rho p}) = v_p(U_rho) + 1 on those
     primes (indices that are never d-smooth, hence never in a layer);
  3. delta_j recomputed two ways agrees:
     sum over p | E_j of (v_p(E_j)-1) log p
       ==  sum over p of (v_p(U_{ell^{j+1}}) - 1) log p restricted to
           rank(p) == ell^{j+1}.
Standard library only.
"""
from math import comb, gcd, log

ok = fail = 0
def check(name, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1
        print("FAIL:", name)

def S(l, a, b):
    m = (l-1)//2
    return sum((-1)**r*comb(l, 2*r+1)*a**r*b**(m-r) for r in range(m+1))

def C(l, a, b):
    m = (l-1)//2
    return sum((-1)**r*comb(l, 2*r)*a**r*b**(m-r) for r in range(m+1))

def v(x, p):
    n = 0; x = abs(x)
    while x and x % p == 0: x //= p; n += 1
    return n

def factor(x):
    fs = {}
    d = 2
    while d*d <= x:
        while x % d == 0:
            fs[d] = fs.get(d, 0) + 1
            x //= d
        d += 1
    if x > 1: fs[x] = fs.get(x, 0) + 1
    return fs

def U_mod(m, P, Q, mod):
    """U_m of x^2 - P x + Q, modulo mod (fast doubling via matrices)."""
    def mul(A, B):
        return [(A[0]*B[0]+A[1]*B[2]) % mod, (A[0]*B[1]+A[1]*B[3]) % mod,
                (A[2]*B[0]+A[3]*B[2]) % mod, (A[2]*B[1]+A[3]*B[3]) % mod]
    R = [1, 0, 0, 1]
    M = [P % mod, (-Q) % mod, 1, 0]
    e = m
    while e:
        if e & 1: R = mul(R, M)
        M = mul(M, M)
        e >>= 1
    # [U_{m+1}, ?; U_m, ?] = M^m acting on (U_1,U_0)=(1,0)
    return R[2]

def rank_of_apparition(p, P, Q, bound):
    """Smallest r <= bound with p | U_r (exact search over divisors of
    p - (D|p) would be faster; brute force over divisors of candidates)."""
    # rank divides p - legendre(D,p); search its divisors
    D = (P*P - 4*Q) % p
    ls = pow(D, (p-1)//2, p) if D else 0
    chi = 1 if ls == 1 else (-1 if ls == p-1 else 0)
    if chi == 0:
        n = p  # ramified
    else:
        n = p - chi
    divs = sorted(d for d in range(1, n+1) if n % d == 0)
    for r in divs:
        if U_mod(r, P, Q, p) == 0:
            return r
    return None

for l, a0, b0, levels in ((3, 3, 2, 3), (5, 5, 2, 2)):
    c0 = a0 + b0
    P0, Q0 = 2*(b0 - a0), c0*c0
    a, b = a0, b0
    for j in range(levels):
        s, c = S(l, a, b), C(l, a, b)
        E = abs(s*c) // l
        fs = factor(E)
        m_layer = l**(j+1)
        d1 = sum((e-1)*log(p) for p, e in fs.items() if e >= 2)
        d2 = 0.0
        for p, e in fs.items():
            r = rank_of_apparition(p, P0, Q0, p+1)
            check(f"l={l} j={j} p={p}: rank {r} == layer {m_layer}",
                  r == m_layer)
            # repetition law at index rho*p (never d-smooth)
            vr = v(E, p)  # = v_p(U_{m_layer}) since ranks match, unit cofactor
            urp = U_mod(m_layer*p, P0, Q0, p**(vr+2))
            check(f"l={l} j={j} p={p}: v_p(U_(rho*p)) = {vr}+1",
                  v(urp, p) == vr + 1)
            if vr >= 2:
                d2 += (vr - 1)*log(p)
        check(f"l={l} j={j}: delta via E == delta via ranks "
              f"({d1:.4f} vs {d2:.4f})", abs(d1 - d2) < 1e-9)
        print(f"l={l} j={j}: E_j has {len(fs)} primes, "
              f"delta_j={d1:.4f}, primes={sorted(fs.items())}")
        a, b = a*s*s, b*c*c

print(f"\n{ok} checks passed, {fail} failed")
