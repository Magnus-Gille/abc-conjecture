#!/usr/bin/env python3
"""Phase 7: verification for the Lucas-Wieferich window reduction (claude).

Key identity being tested (Proposition W1): for a squared layer prime p
of a fixed orbit, with chi = (Delta|p) and p - chi = r * (rank multiple),
p not dividing r:
    v_p(U_{p-chi}) = v_p(U_{q_j}) = v_p(E_j)  (>= 2),
i.e. every squared layer prime is a Lucas-Wieferich prime of the pair.
Since beta is a p-adic unit and (alpha-beta)^2 = -16ab is prime to p,
v_p(u^m - 1) = v_p(U_m), so everything is integer arithmetic.

Tests:
  A. Programmed squares: Q17 quadratic seeds with v_7(E_1)=2 exactly
     -> verify v_7(U_8) = 2 (p=7, chi=-1, p-chi=8).
     Remark 18 cubic seed with v_17(E_1)=2 -> verify v_17(U_18) = 2.
  B. LTE stability: for assorted (pair, q, p | U_q, r coprime to p):
     v_p(U_{q r}) = v_p(U_q).
  C. Empirical LW search: for the three canonical pairs, count p <= X
     with U_{p-chi} == 0 mod p^2  (LW primes). Report hits.

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

def v(x, p):
    n = 0; x = abs(x)
    while x and x % p == 0: x //= p; n += 1
    return n

def U_mod(m, P, Q, mod):
    """U_m for x^2 - P x + Q, modulo mod, by fast matrix power."""
    def mul(A, B):
        return ((A[0]*B[0]+A[1]*B[2]) % mod, (A[0]*B[1]+A[1]*B[3]) % mod,
                (A[2]*B[0]+A[3]*B[2]) % mod, (A[2]*B[1]+A[3]*B[3]) % mod)
    R = (1, 0, 0, 1)
    M = (P % mod, (-Q) % mod, 1, 0)
    e = m
    while e:
        if e & 1: R = mul(R, M)
        M = mul(M, M)
        e >>= 1
    return R[2]

def legendre(a, p):
    a %= p
    if a == 0: return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1

# ---------- A. programmed squares ----------
def t2(a, b): return 4*a*b, (b-a)**2

def S3(a, b): return 3*b - a
def C3(a, b): return b - 3*a

# A1: quadratic Q17 seeds (reconstruct as in quadratic_realization_check)
def hensel_root_quadratic(n, p, h, chi):
    def Gv(x, mod):
        a, b = x % mod, 1
        for _ in range(n):
            a, b = (4*a*b) % mod, (b-a)**2 % mod
        return (b - a) % mod
    roots = [x for x in range(p)
             if Gv(x, p) == 0 and legendre(-x, p) == chi]
    r = roots[0]
    for k in range(1, h+1):
        mod = p**(k+1)
        for t in range(p):
            if Gv(r + p**k*t, mod) % mod == 0:
                r += p**k*t
                break
    return r

def crt(r1, m1, r2, m2):
    return (r1 + m1*((r2-r1)*pow(m1, -1, m2) % m2)) % (m1*m2)

p, n, h, chi = 7, 1, 2, -1
rho = hensel_root_quadratic(n, p, h, chi)
a_t = (rho + p**h) % p**(h+1)
M = 2*p**(h+1)
abar = crt(crt(a_t, p**(h+1), 0, 2), 2*p**(h+1) // 2, 0, 2)  # a even
abar = crt(a_t, p**(h+1), 0, 2)
bbar = crt(1, p**(h+1), 1, 2)
for t in range(1, 4):
    b0 = bbar + M*t
    a0 = crt(abar, M, 1 % b0, b0)
    if a0 <= 0: a0 += M*b0
    if gcd(a0, b0) != 1: continue
    a1, b1 = t2(a0, b0)
    E1 = abs(b1 - a1)
    check(f"A1 seed{t} v7(E1)=2", v(E1, 7) == 2)
    # Lucas pair of the seed
    P0, Q0 = 2*(b0 - a0), (a0 + b0)**2
    D = P0*P0 - 4*Q0
    check(f"A1 seed{t} chi(-a0b0)=-1", legendre(D, 7) == -1)
    u8 = U_mod(8, P0, Q0, 7**4)
    check(f"A1 seed{t} v7(U_8)={v(u8,7)} == 2 (LW characterization)",
          v(u8, 7) == 2)
    # and the rank-side value agrees: v7(U_4) = v7(E_1)
    u4 = U_mod(4, P0, Q0, 7**4)
    check(f"A1 seed{t} v7(U_4)=2", v(u4, 7) == 2)

# A2: Remark 18 cubic seed, 17^2 at level 1
a0, b0 = 304260006, 39305
a, b = a0, b0
s, c = S3(a, b), C3(a, b)
a, b = a*s*s, b*c*c
s1, c1 = S3(a, b), C3(a, b)
E1 = abs(s1*c1)//3
check("A2 v17(E1)=2", v(E1, 17) == 2)
P0, Q0 = 2*(b0-a0), (a0+b0)**2
D = P0*P0 - 4*Q0
check("A2 chi=-1", legendre(D, 17) == -1)
u18 = U_mod(18, P0, Q0, 17**4)
check(f"A2 v17(U_18)={v(u18,17)} == 2 (LW characterization)", v(u18, 17) == 2)
u9 = U_mod(9, P0, Q0, 17**4)
check("A2 v17(U_9)=2 (rank side)", v(u9, 17) == 2)

# ---------- B. LTE stability v_p(U_{q r}) = v_p(U_q), p not dividing r ----------
for (P0, Q0, q, p) in ((14, 81, 4, 17), (-2, 25, 9, 17), (-2, 25, 9, 89),
                       (-6, 49, 5, 11), (-6, 49, 5, 29), (14, 81, 8, 31)):
    base = v(U_mod(q, P0, Q0, p**5), p)
    if base == 0:
        check(f"B skip p={p} (not a divisor)", True)
        continue
    for r in (2, 3, 5, 6):
        if r % p == 0: continue
        val = v(U_mod(q*r, P0, Q0, p**6), p)
        check(f"B pair({P0},{Q0}) q={q} p={p} r={r}: {val}=={base}",
              val == base)

# ---------- C. empirical LW search ----------
def sieve(n):
    s = bytearray([1])*(n+1); s[0:2] = b"\x00\x00"
    for i in range(2, int(n**.5)+1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(2, n+1) if s[i]]

X = 10**5
PRIMES = sieve(X)
for name, (P0, Q0) in (("quadratic(1,8,9)", (14, 81)),
                       ("cubic(3,2,5)", (-2, 25)),
                       ("quintic(5,2,7)", (-6, 49))):
    D = P0*P0 - 4*Q0
    hits = []
    for p in PRIMES:
        if p == 2 or Q0 % p == 0 or D % p == 0: continue
        chi = legendre(D, p)
        m = p - chi
        if U_mod(m, P0, Q0, p*p) == 0:
            hits.append(p)
    print(f"C {name}: LW primes p <= {X}: {hits if hits else 'none'}")
    check(f"C {name} sparsity (<= 3 hits expected heuristically)",
          len(hits) <= 3)
    # rank of each LW hit, and whether it is d-smooth (i.e. could ever
    # appear in a layer of THIS orbit's tower)
    d_of = {"quadratic(1,8,9)": 2, "cubic(3,2,5)": 3, "quintic(5,2,7)": 5}
    d = d_of[name]
    for p in hits:
        chi = legendre(D, p)
        m = p - chi
        divs = sorted(k for k in range(1, m+1) if m % k == 0)
        rank = next(k for k in divs if U_mod(k, P0, Q0, p) == 0)
        x = rank
        while x % d == 0: x //= d
        print(f"    p={p}: rank={rank}, pure-{d}-power={'yes' if x==1 else 'no'}")
        check(f"C {name} p={p} rank not a pure d-power (never a layer prime)",
              x != 1)

print(f"\n{ok} checks passed, {fail} failed")
