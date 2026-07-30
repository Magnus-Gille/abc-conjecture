#!/usr/bin/env python3
"""Verify the change-of-variables bridge between the prime-genealogy branch
polynomials F_{n,eps}(X,1) and the fibotomic atoms Psi_m of
Byer-Dvorachek-Eckard-Harrington-Wise-Wong (Adv. Appl. Math. 138 (2022),
arXiv:2009.03345).

Claim (mailbox/0071-claude.md): for m = m_{n,eps}, odd p != ell, the roots
rho of F_{n,eps}(X,1) in F_p and the x^2-roots of the (even) polynomial
Psi_m(x) = G_m(x^2) in F_p correspond bijectively under

    x^2 = -4/(rho+1),   equivalently   rho = -1 - 4/x^2,

each fiber {x,-x} giving a linear pair (x^2 a residue) or an irreducible
quadratic factor (x^2 a nonresidue) of Psi_m mod p. Derivation: with
zeta = -omega^2 and x = omega - omega^{-1}, the Cayley parameter satisfies
s = (zeta-1)/(zeta+1) = (omega+omega^{-1})/(omega-omega^{-1}), hence
rho = -s^2 = -(x^2+4)/x^2.

Standard library only. Independent of chebyshev_abc.py.
"""
from math import comb


def S(l, a, b):
    m = (l - 1) // 2
    return sum((-1)**r * comb(l, 2*r+1) * a**r * b**(m-r) for r in range(m+1))


def C(l, a, b):
    m = (l - 1) // 2
    return sum((-1)**r * comb(l, 2*r) * a**r * b**(m-r) for r in range(m+1))


def our_roots(l, n, branch, p):
    """Roots of F_{n,branch}(X,1) in F_p by brute force on the orbit."""
    inv_l = pow(l, -1, p)
    roots = []
    for x in range(p):
        a, b = x % p, 1
        for _ in range(n):
            a, b = (a * S(l, a, b)**2) % p, (b * C(l, a, b)**2) % p
        val = (S(l, a, b) * inv_l) % p if branch == 'A' else C(l, a, b) % p
        if val == 0:
            roots.append(x)
    return roots


def fibotomic_atoms(limit):
    """Psi_d over Z for 2 <= d <= limit, via F_n = prod_{d|n, d>1} Psi_d."""
    F = {1: [1], 2: [0, 1]}
    for k in range(3, limit + 1):
        xf = [0] + F[k-1]
        F[k] = [(xf[i] if i < len(xf) else 0) +
                (F[k-2][i] if i < len(F[k-2]) else 0)
                for i in range(max(len(xf), len(F[k-2])))]

    def polydiv_exact(A, B):
        A = A[:]
        q = [0] * (len(A) - len(B) + 1)
        for i in range(len(A) - len(B), -1, -1):
            c = A[i + len(B) - 1] // B[-1]
            q[i] = c
            for j, bj in enumerate(B):
                A[i + j] -= c * bj
        assert all(v == 0 for v in A), "non-exact division"
        return q

    Psi = {}
    for d in range(2, limit + 1):
        num = F[d][:]
        for e in range(2, d):
            if d % e == 0:
                num = polydiv_exact(num, Psi[e])
        Psi[d] = num
    return Psi


def peval(P, x, p):
    return sum(c * pow(x, i, p) for i, c in enumerate(P)) % p


def compare(l, n, branch, p, Psi):
    m = (l**(n+1)) * (2 if branch == 'B' else 1)
    ours = our_roots(l, n, branch, p)
    x2_ours = sorted(((-4) * pow(r + 1, -1, p)) % p for r in ours)
    even = all(c == 0 for i, c in enumerate(Psi[m]) if i % 2 == 1)
    G = [c for i, c in enumerate(Psi[m]) if i % 2 == 0]
    x2_theirs = sorted(y for y in range(p) if peval(G, y, p) == 0)
    ok = even and x2_ours == x2_theirs
    shapes = ['linear-pair' if pow(y, (p-1)//2, p) == 1 else 'irred-quadratic'
              for y in x2_ours]
    print(f"l={l} n={n} {branch} p={p} m={m}: rho-roots={ours} -> "
          f"x2={x2_ours} vs Psi_{m} x2-roots={x2_theirs} "
          f"{'OK' if ok else 'FAIL'} shapes={shapes}")
    return ok


def main():
    Psi = fibotomic_atoms(19)
    cases = [
        (3, 1, 'A', 19),   # 9 | p-1, p=3 mod 4: BDEHWW delta=2 stratum
        (3, 1, 'A', 37),   # 2m | p-1, p=1 mod 4: delta=1 full split
        (3, 1, 'B', 17),   # m=18 | p+1: inert side
        (5, 0, 'B', 29),   # m=10 | p+1
        (3, 0, 'A', 7),    # m=3 | p-1
        (3, 0, 'B', 11),   # m=6 | p+1
    ]
    ok = all(compare(*c, Psi) for c in cases)
    print("ALL OK" if ok else "SOME FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
