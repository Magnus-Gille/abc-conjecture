#!/usr/bin/env python3
"""Q1 (Reyssat case): exact minimal nondegenerate certificate height H*.

Triple: a = 2, b = 3^10 * 109 = 6436341, c = 23^5 = 6436343 (Reyssat, q ~ 1.6299).
Primes (order): 2, 3, 109, 23. Variables x = (x2, x3, x109, x23).

Constraint (1)  D_x(a) + D_x(b) = D_x(c):
    e2*x2 + e3*x3 + e109*x109 + e23*x23 = 0
with e2 = v2(a)*(a/2) = 1, e3 = 10*(b/3) = 21454470, e109 = b/109 = 59049,
     e23 = -5*(c/23) = -1399205.

Nondegenerate iff W != 0 iff L_a != L_b iff 327*x2 != 2*(1090*x3 + 3*x109)
(L_a = x2/2, L_b = (1090*x3 + 3*x109)/327; under (1), L_a=L_b forces L_a=L_c).

Method: brute force over (x3, x23) in [-H,H]^2; then e109*x109 must land within
+-H of -(e3*x3 + e23*x23), so x109 has <= 3 candidates; x2 is then determined.
Exhaustive for the max-norm ball, H = 721 (the height of the certificate
exhibited in firsttryabc.md SS6, known to be nondegenerate with W = abc/R).
"""
from math import log2

a, b, c = 2, 3**10 * 109, 23**5
R = 2 * 3 * 109 * 23
e2, e3, e109, e23 = 1, 10 * (b // 3), b // 109, -5 * (c // 23)
H = 721

best = None
count_nondeg = 0
for x3 in range(-H, H + 1):
    A = e3 * x3
    for x23 in range(-H, H + 1):
        T = A + e23 * x23
        q0 = round(-T / e109)
        for x109 in (q0 - 1, q0, q0 + 1):
            if abs(x109) > H:
                continue
            x2 = -(T + e109 * x109)
            if abs(x2) > H:
                continue
            if 327 * x2 == 2 * (1090 * x3 + 3 * x109):
                continue  # degenerate (W = 0)
            count_nondeg += 1
            m = max(abs(x2), abs(x3), abs(x109), abs(x23))
            if best is None or m < best[0]:
                best = (m, x2, x3, x109, x23)

m, x2, x3, x109, x23 = best
assert e2 * x2 + e3 * x3 + e109 * x109 + e23 * x23 == 0
# W = ab*(L_b - L_a) = (ab/654)*(2*(1090*x3+3*x109) - 327*x2)   [654 = 2*327]
W = (a * b // 654) * (2 * (1090 * x3 + 3 * x109) - 327 * x2)
assert W % (a * b * c // R) == 0 and W != 0

print(f"c/R                    = {c / R:.2f}")
print(f"Prop-1 lower bound     = c/(R*log2 c) = {c / (R * log2(c)):.2f}")
print(f"H* (exact, ball H<=721)= {m}")
print(f"argmin x = (x2,x3,x109,x23) = ({x2}, {x3}, {x109}, {x23})")
print(f"W(x)/(abc/R)           = {W // (a * b * c // R)}")
print(f"nondegenerate solutions in ball: {count_nondeg}")

# Degenerate minimum for contrast: x2=10u, x23=23u, x3=3w, x109=545u-1090w
dbest = None
for u in range(-60, 61):
    for w in range(-60, 61):
        if u == 0 and w == 0:
            continue
        mm = max(abs(10 * u), abs(23 * u), abs(3 * w), abs(545 * u - 1090 * w))
        if dbest is None or mm < dbest[0]:
            dbest = (mm, u, w)
print(f"min degenerate height (nonzero): {dbest[0]}  (u={dbest[1]}, w={dbest[2]})")
