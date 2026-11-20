"""Verify first-depth-one primes and exact coverage among odd mixed-orbit multipliers."""
from fractions import Fraction
from functools import cache
from math import gcd, isqrt, log, prod

# Each row gives the source prime q, witness prime p, and order of R0 modulo p.
ROWS = """
3 13411 9
5 294241 15
7 117041 7
11 82633 11
13 50441 39
17 57667 51
19 6427 57
23 203873 69
29 4931 87
31 11657 93
37 418027 37
41 322097 123
43 169667 129
47 449321 47
59 76819 59
61 201667 183
67 241603 201
71 271363 213
73 116881 73
79 75209 79
83 455339 83
89 158227 267
97 168433 291
103 64067 309
107 206939 107
113 164051 339
127 194057 381
131 171491 393
137 355777 411
139 427579 417
149 132611 149
163 150379 163
179 154753 537
193 406673 579
199 476009 597
211 263723 633
227 404699 681
233 172603 699
241 257657 723
251 229499 753
257 149027 257
281 472643 843
283 481667 849
307 386219 921
313 441697 313
331 49211 331
337 103387 1011
347 18859 1041
353 140521 1059
379 231017 1137
401 194963 401
409 7499 1227
419 498937 1257
433 7867 1299
443 169409 443
449 73019 1347
457 140587 1371
467 76147 1401
491 423457 1473
499 129347 1497
521 103699 1563
523 460531 1569
547 19417 1641
563 193163 1689
569 92779 1707
571 165041 1713
577 114883 1731
587 455579 587
593 32323 1779
601 10891 1803
617 245209 1851
619 121883 1857
641 371179 641
643 208489 1929
659 130987 1977
673 206651 2019
683 131779 683
691 37483 2073
739 424849 739
761 300761 2283
769 13627 2307
787 3049 787
809 465841 2427
811 29033 2433
827 5099 827
857 338297 2571
859 444473 859
881 94777 2643
883 5387 883
907 32713 2721
929 184627 2787
937 101833 2811
953 275393 953
971 1987 971
977 104953 2931
"""

# Additional pairs of exact ambient rank q, for ambient indices prime to 3.
EXTRA = ((19, 2243), (23, 57593), (41, 29137), (43, 36187), (67, 13291), (89, 143291), (113, 152777), (127, 97283), (131, 4273), (137, 343769), (139, 232409), (179, 29251), (233, 89057), (307, 5651), (467, 15121), (499, 32579), (547, 2281), (563, 161521), (571, 30491), (577, 3347), (617, 62483), (619, 10979), (643, 187513), (691, 4091), (809, 43411), (929, 119233), (977, 1867), (5, 281), (17, 83))

# Fill every remaining prime source below the first current gap.
SMOOTH_EXTRA = ((53, 9623953, 53), (101, 1102921, 303), (109, 3064427, 327), (151, 8186774249, 151), (157, 18925409, 471), (167, 4522027, 501), (173, 1976699, 519), (181, 3147953, 543))


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def division_at_r0(modulus):
    x, y = -8, 16
    b2, b4, b8 = 64, 64, -1024
    w2 = 2*y
    w3 = (3*x**4 + b2*x**3 + 3*b4*x*x + b8) % modulus
    w4 = (w2 * (2*x**6 + b2*x**5 + 5*b4*x**4
                + 10*b8*x*x + b2*b8*x + b4*b8)) % modulus
    inverse = pow(w2, -1, modulus)

    @cache
    def w(n):
        if n <= 4:
            return (0, 1, w2, w3, w4)[n]
        k = n//2
        if n % 2:
            return (w(k+2)*w(k)**3 - w(k-1)*w(k+1)**3) % modulus
        return w(k)*inverse*(w(k+2)*w(k-1)**2 - w(k-2)*w(k+1)**2) % modulus

    return w


def check():
    rows = [tuple(map(int, row.split())) for row in ROWS.splitlines() if row.strip()]
    qs = {q for q, _, _ in rows}
    ps = {p for _, p, _ in rows}
    assert len(rows) == len(qs) == len(ps) == 95 and qs.isdisjoint(ps)
    uncovered = Fraction(1)
    average_log_mass = 0
    for q, p, r in rows:
        assert is_prime(q) and is_prime(p) and 3 <= q <= 1000 < p
        assert r // gcd(r, 3) == q
        w = division_at_r0(p*p)
        assert w(r) % p == 0 and w(r) != 0
        for d in (3, q):
            if r % d == 0:
                assert w(r//d) % p != 0
        hit = Fraction(p-1, p*q)
        uncovered *= 1 - hit
        average_log_mass += float(hit)*log(p)
    assert 1 - uncovered > Fraction(4, 5)
    assert division_at_r0(11**2)(9) == 110 and division_at_r0(11)(3) != 0
    smooth = {q: (p, r) for q, p, r in rows if q < 191}
    for q, p, r in SMOOTH_EXTRA:
        assert is_prime(p) and p > q and r//gcd(r, 3) == q
        w = division_at_r0(p*p)
        assert w(r) % p == 0 and w(r) != 0
        for d in (3, q):
            if r % d == 0:
                assert w(r//d) % p != 0
        smooth[q] = p, r
    assert set(smooth) == {q for q in range(3, 191, 2) if is_prime(q)}
    ambient = [(q, p) for q, p, r in rows if q == r and q not in (83, 281)]
    for q, p in EXTRA:
        assert is_prime(q) and is_prime(p)
        w = division_at_r0(p*p)
        assert w(q) % p == 0 and w(q) != 0
        ambient.append((q, p))
    assert len({q for q, _ in ambient}) == len({p for _, p in ambient}) == len(ambient)
    assert {q for q, _ in ambient}.isdisjoint(p for _, p in ambient)
    miss_outside_three = prod(1 - Fraction(p - 1, p*q) for q, p in ambient)
    full_density = 1 - (uncovered + 2*miss_outside_three) / 3
    assert full_density > Fraction(2, 3)
    print(f"All odd ambient indices, certified relative density {float(full_density):.12f}")
    print(f"{len(rows)} witnesses, relative density {float(1-uncovered):.12f}, "
          f"mean log mass {average_log_mass:.9f}, "
          f"{len(str(prod(ps)))} digits in their product")


if __name__ == "__main__":
    check()
