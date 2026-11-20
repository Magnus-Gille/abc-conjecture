"""Certify simultaneous odd valuations in two CM packets at split prime indices."""
from fractions import Fraction
from functools import cache
from math import isqrt


TESTS = [
    (5, 281), (7, 117041), (11, 82633), (19, 73), (23, 57593),
    (41, 29137), (47, 449321), (53, 9623953), (73, 116881),
    (79, 75209), (113, 152777), (131, 4273), (137, 343769),
    (139, 232409), (151, 8186774249), (233, 89057), (313, 441697),
    (443, 169409), (467, 15121), (547, 2281), (563, 161521),
    (643, 187513), (739, 424849), (787, 3049), (859, 444473),
    (929, 119233), (953, 275393),
]


def prime(n):
    return n > 1 and all(n % i for i in range(2, isqrt(n)+1))


def division(h):
    # psi_1, psi_2, psi_3, psi_4 at (-8,16) on y^2=x^3+16x^2+32x.
    start = [0, 1, 32, -9216, -14680064]
    inv = pow(32, -1, h)
    @cache
    def psi(n):
        if n < 5:
            return start[n] % h
        k = n//2
        if n % 2:
            return (psi(k+2)*psi(k)**3 - psi(k-1)*psi(k+1)**3) % h
        return psi(k)*inv*(psi(k+2)*psi(k-1)**2 - psi(k-2)*psi(k+1)**2) % h
    return psi


def counts(t, h):
    assert prime(t) and prime(h) and h % 8 == 1 and t != h
    psi = division(h)
    assert psi(t) == 0 and psi(1) != 0
    chi = lambda x: pow(x % h, (h-1)//2, h)
    # Ward gives period 4t. On odd arguments these entries certify dependence on n mod t.
    scalar_chars = [chi(psi(j if j % 2 else j+t)) for j in range(t)]
    assert all(chi(psi(n)) == scalar_chars[n % t] for n in range(1, 4*t, 2))
    xs = [None] + [
        (-8-psi(k-1)*psi(k+1)*pow(psi(k), -2, h)) % h for k in range(1, 1+t//2)
    ]
    txs = [None] + [
        -(x+16+32*pow(x, -1, h))*pow(2, -1, h) % h for x in xs[1:]
    ]
    if t == 5:
        assert xs == [None, h-8, 1] and txs == [None, h-2, 116]
        assert scalar_chars[1:] == [1]*4
    if t == 7:
        assert xs == [None, h-8, 1, 44791] and txs == [None, h-2, 58496, 3352]
        assert scalar_chars[1:] == [1]*6
    totals = [0]*4
    for a, x in enumerate(xs):
        for b, tx in enumerate(txs):
            norm = (a*a+2*b*b) % t
            if norm == 0:
                continue
            # A unique pole has a square leading unit, since -1 is a square at h.
            m = 1 if x is None or tx is None else chi(x-tx)
            c = m*scalar_chars[norm] % h
            assert m in (1, h-1) and c in (1, h-1)
            if (t == 7 and norm in (5, 6)) or (t == 23 and norm in (15, 17)):
                assert m == c == h-1
            totals[(m != 1)+2*(c != 1)] += (2 if a else 1)*(2 if b else 1)
    split = pow((-2) % t, (t-1)//2, t) == 1
    assert sum(totals) == ((t-1)**2 if split else t*t-1)
    return totals


def verify():
    assert len({t for t, _ in TESTS}) == len(TESTS)
    miss_m = miss_c = miss_both = Fraction(1)
    for t, h in TESTS:
        n00, n10, n01, n11 = counts(t, h)
        total = n00+n10+n01+n11
        miss_m *= Fraction(n00+n01, total)
        miss_c *= Fraction(n00+n10, total)
        miss_both *= Fraction(n00, total)
        coverage = 1-miss_m-miss_c+miss_both
        if t == 5:
            assert coverage == Fraction(1, 2)
        if t == 7:
            assert coverage == Fraction(19, 24)
    assert Fraction(9999999747549, 10**13) < coverage < Fraction(9999999747550, 10**13)
    print(f'Certified relative density among split primes: {float(coverage):.15f}')
    print(f'Exact density: {coverage}')


if __name__ == '__main__':
    verify()
