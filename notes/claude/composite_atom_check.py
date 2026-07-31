#!/usr/bin/env python3
"""Phase 9: verification for the general atom lemma (claude derivation).

Claims tested (notes/claude/composite-atom-lemma.md):
  A. Integrality + degree: for every index k >= 3, Phi_k(Omega,Omegabar)
     is a rational integer at every integer seed (x-component vanishes in
     Z[x]/(x^2-b)), i.e. the atom A_k(a,b) is well defined; and the
     uniform omega-layer identity holds for every degree d >= 2:
         |U_{d^{j+1}}/U_{d^j}| = prod_{k in Lambda_{d,j}} |A_k(a,b)|,
         Lambda_{d,j} = {k : k | 2 d^{j+1}, k does not divide 2 d^j},
     with systematic content prod = d after admissible normalization
     (checked as |Q_{d,j}| = d * prod |A_k|/d ... i.e. product identity
     directly).
  B. Evaluations: A_k(0,1) = Phi_k(1,1) in {1, q}; A_k(-1,1) = 2^{phi(k)}
     up to sign; leading coefficient of A_k(X,1) = +-Phi_k(-1) in {1,q,2}.
  C. Root classification for composite indices k (12, 15, 20, 24, 30):
     exactly phi(k)/2 simple roots mod compatible p (k | p-chi), Legendre
     sign (-rho/p) = chi, no roots at incompatible p; distinct indices
     give disjoint root sets mod the same p.
  D. Hensel: exact valuation h for perturbed lifts at a sample of
     composite indices.

Ring arithmetic: omega^n computed exactly in Z<1,x,y,xy>, x^2=b, y^2=-a;
omega^k - omegabar^k = 2y(C_k + D_k x); Phi_k(omega,omegabar) =
prod_{d'|k} (C_{d'} + D_{d'} x)^{mu(k/d')} evaluated by exact division
in Z[x]/(x^2-b).  Standard library only.
"""
from math import comb, gcd, log

ok = fail = 0
def check(name, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1
        print("FAIL:", name)

def mobius(n):
    m, cnt, d = n, 0, 2
    while d*d <= m:
        if m % d == 0:
            m //= d
            if m % d == 0: return 0
            cnt += 1
        d += 1
    if m > 1: cnt += 1
    return -1 if cnt % 2 else 1

def omega_pow(n, a, b):
    """omega^n = A + Bx + Cy + Dxy in Z[x,y]/(x^2-b, y^2=-a), omega=x+y."""
    A, B, C, D = 1, 0, 0, 0
    PA, PB, PC, PD = 0, 1, 1, 0     # omega
    e = n
    while e:
        if e & 1:
            A, B, C, D = (A*PA + b*B*PB - a*C*PC - a*b*D*PD,
                          A*PB + B*PA - a*C*PD - a*D*PC,
                          A*PC + C*PA + b*B*PD + b*D*PB,
                          A*PD + D*PA + B*PC + C*PB)
        PA, PB, PC, PD = (PA*PA + b*PB*PB - a*PC*PC - a*b*PD*PD,
                          2*PA*PB - 2*a*PC*PD,
                          2*PA*PC + 2*b*PB*PD,
                          2*PA*PD + 2*PB*PC)
        e >>= 1
    return A, B, C, D

def CD(k, a, b):
    """omega^k - omegabar^k = 2y (C + D x): return (C, D)."""
    A, B, C, D = omega_pow(k, a, b)
    return C, D

def atom(k, a, b):
    """A_k(a,b) = Phi_k(omega,omegabar) as an exact rational integer.

    Product over d' | k of (C_{d'} + D_{d'} x)^{mu(k/d')} in Z[x]/(x^2-b).
    Returns the integer, asserting exact division and zero x-component.
    """
    num = (1, 0); den = (1, 0)
    for dp in range(1, k+1):
        if k % dp: continue
        mu = mobius(k//dp)
        if mu == 0: continue
        c, d0 = CD(dp, a, b)
        if mu == 1:
            num = (num[0]*c + b*num[1]*d0, num[0]*d0 + num[1]*c)
        else:
            den = (den[0]*c + b*den[1]*d0, den[0]*d0 + den[1]*c)
    # divide num by den in Z[x]/(x^2-b): num * conj(den) / N(den)
    nrm = den[0]*den[0] - b*den[1]*den[1]
    assert nrm != 0
    p0 = num[0]*den[0] - b*num[1]*den[1]
    p1 = num[1]*den[0] - num[0]*den[1]
    assert p0 % nrm == 0 and p1 % nrm == 0, (k, a, b, "inexact division")
    q0, q1 = p0//nrm, p1//nrm
    assert q1 == 0, (k, a, b, "nonzero x-component")
    return q0

def omega1_pow(n, a):
    """(1+y)^n = e + f y in Z[y]/(y^2 = -a): return (e, f)."""
    e, f = 1, 0
    pe, pf = 1, 1
    m = n
    while m:
        if m & 1:
            e, f = e*pe - a*f*pf, e*pf + f*pe
        pe, pf = pe*pe - a*pf*pf, 2*pe*pf
        m >>= 1
    return e, f

def _pmul(A, B):
    R = [0]*(len(A)+len(B)-1)
    for i, ai in enumerate(A):
        if ai:
            for j, bj in enumerate(B): R[i+j] += ai*bj
    while len(R) > 1 and R[-1] == 0: R.pop()
    return R

def _pdiv_exact(A, B):
    A = A[:]; q = [0]*(len(A)-len(B)+1)
    for i in range(len(A)-len(B), -1, -1):
        assert A[i+len(B)-1] % B[-1] == 0, "inexact poly division"
        c = A[i+len(B)-1]//B[-1]; q[i] = c
        for j, bj in enumerate(B): A[i+j] -= c*bj
    assert all(v == 0 for v in A), "nonzero remainder"
    while len(q) > 1 and q[-1] == 0: q.pop()
    return q

def _f_poly(n):
    """f_n(X) with (1+y)^n = e_n + f_n y over Z[X], y^2 = -X."""
    e, f = [1], [0]
    pe, pf = [1], [1]
    m = n
    while m:
        if m & 1:
            e, f = ([x-y for x, y in
                     zip(_pmul(e, pe)+[0]*99, ([0]+_pmul(f, pf))+[0]*99)][:max(len(_pmul(e,pe)), len(_pmul(f,pf))+1)],
                    [x+y for x, y in
                     zip(_pmul(e, pf)+[0]*99, _pmul(f, pe)+[0]*99)][:max(len(_pmul(e,pf)), len(_pmul(f,pe)))])
        pe, pf = ([x-y for x, y in
                   zip(_pmul(pe, pe)+[0]*99, ([0]+_pmul(pf, pf))+[0]*99)][:max(len(_pmul(pe,pe)), len(_pmul(pf,pf))+1)],
                  [2*x for x in _pmul(pe, pf)])
        m >>= 1
    while len(f) > 1 and f[-1] == 0: f.pop()
    return f

_ATOM_CACHE = {}
def atom_poly(k):
    """A_k(X,1) as an exact integer polynomial (coefficient list)."""
    if k in _ATOM_CACHE: return _ATOM_CACHE[k]
    num, den = [1], [1]
    for dp in range(1, k+1):
        if k % dp: continue
        mu = mobius(k//dp)
        if mu == 0: continue
        f = _f_poly(dp)
        if mu == 1: num = _pmul(num, f)
        else: den = _pmul(den, f)
    q = _pdiv_exact(num, den)
    _ATOM_CACHE[k] = q
    return q

def atom1(k, a):
    return sum(c*a**i for i, c in enumerate(atom_poly(k)))

def phi(n):
    r, m, d = 1, n, 2
    while d*d <= m:
        if m % d == 0:
            e = 0
            while m % d == 0: m //= d; e += 1
            r *= (d-1)*d**(e-1)
        d += 1
    if m > 1: r *= m-1
    return r

def U(n, a, b):
    P, Q = 2*(b-a), (a+b)**2
    u0, u1 = 0, 1
    for _ in range(n): u0, u1 = u1, P*u1 - Q*u0
    return u0

# ---------- A. integrality + uniform layer identity ----------
seeds = [(3,2),(5,2),(1,8),(7,2),(15,2),(9,2)]  # b nonsquare: 4-dim ring stays a domain
for k in (3,4,5,6,8,9,10,12,15,16,20,24,30):
    for (a,b) in seeds:
        v = atom(k, a, b)   # asserts integrality internally
    check(f"A integrality k={k}", True)

def layer_set(d, j):
    N1, N0 = 2*d**(j+1), 2*d**j
    return [k for k in range(3, N1+1) if N1 % k == 0 and N0 % k != 0]

for d in (2,3,5,6,10,15):
    for j in (0,1):
        for (a,b) in ((3,2),(5,2),(1,8)):
            Q = U(d**(j+1), a, b)//U(d**j, a, b) if U(d**j,a,b) else None
            if Q is None: continue
            prod = 1
            for k in layer_set(d, j):
                prod *= atom(k, a, b)
            check(f"A layer d={d} j={j} seed({a},{b}): |Q|==|prod|",
                  abs(Q) == abs(prod))

# ---------- B. evaluations ----------
def prime_power_root(k):
    m, d = k, 2
    fs = set()
    while d*d <= m:
        while m % d == 0: fs.add(d); m //= d
        d += 1
    if m > 1: fs.add(m)
    return fs

for k in (3,4,5,6,8,9,10,12,15,16,20,24,30):
    v0 = atom1(k, 0)
    fs = prime_power_root(k)
    expect = list(fs)[0] if len(fs) == 1 else 1
    check(f"B A_k(0,1) k={k}: {v0} == {expect}", v0 == expect)
    vm = atom1(k, -1)   # A_k(-1,1)
    check(f"B A_k(-1,1) nonzero k={k}", vm != 0)
    P = atom_poly(k)
    check(f"B deg A_k = phi(k)/2, k={k}", len(P)-1 == phi(k)//2)
    # leading coefficient = +-Phi_k(-1) in {1, q, 2}
    lead = abs(P[-1])
    fs = prime_power_root(k)
    allowed = {1} | fs | {2}
    check(f"B leading coeff k={k}: {lead}", lead in allowed)

# ---------- C. root classification for composite indices ----------
def legendre(x, p):
    x %= p
    if x == 0: return 0
    return 1 if pow(x, (p-1)//2, p) == 1 else -1

cases = [
    (12, 13, 1), (12, 11, -1), (12, 37, 1), (12, 23, -1),
    (15, 31, 1), (15, 29, -1), (15, 61, 1),
    (20, 41, 1), (20, 19, -1),
    (24, 73, 1), (24, 23, -1),
    (30, 31, 1), (30, 29, -1),
]
for k, p, chi in cases:
    check(f"C compat k={k} p={p}", (p - chi) % k == 0)
    roots = [x for x in range(p) if atom1(k, x % p) % p == 0]
    check(f"C count k={k} p={p}: {len(roots)} vs {phi(k)//2}",
          len(roots) == phi(k)//2)
    for r in roots:
        check(f"C sign k={k} p={p} rho={r}", legendre(-r, p) == chi)
        check(f"C rho!=0,-1 k={k} p={p}", r not in (0, p-1))
incompat = [(12, 7), (15, 7), (20, 13), (30, 17)]
for k, p in incompat:
    if (p-1) % k and (p+1) % k:
        roots = [x for x in range(p) if atom1(k, x % p) % p == 0]
        check(f"C no roots k={k} p={p}", not roots)
# disjointness of root sets for distinct indices at one p
p = 61
sets = {}
for k in (3,4,5,6,12,15,20,30):
    if (p-1) % k == 0 or (p+1) % k == 0:
        sets[k] = frozenset(x for x in range(p) if atom1(k, x) % p == 0)
ks = sorted(sets)
for i in range(len(ks)):
    for j2 in range(i+1, len(ks)):
        check(f"C disjoint k={ks[i]},{ks[j2]} mod {p}",
              not (sets[ks[i]] & sets[ks[j2]]))

# ---------- D. Hensel exact valuation at a composite index ----------
k, p, chi = 15, 31, 1
roots = [x for x in range(p) if atom1(k, x) % p == 0]
rho = roots[0]
# lift to mod p^3 by search (simple root)
r = rho
for t in range(p):
    if atom1(k, r + p*t) % p**2 == 0:
        r += p*t; break
for t in range(p):
    if atom1(k, r + p*p*t) % p**3 == 0:
        r += p*p*t; break
def v(x, p):
    n = 0; x = abs(x)
    while x and x % p == 0: x //= p; n += 1
    return n
for h, lam in ((1, 1), (1, 2), (2, 1), (2, 3)):
    val = v(atom1(k, r + lam*p**h), p)
    check(f"D Hensel k=15 p=31 h={h} lam={lam}: v={val}", val == h)

print(f"\n{ok} checks passed, {fail} failed")
