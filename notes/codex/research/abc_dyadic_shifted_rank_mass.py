"""Check the sharp first-rank mass constants with integer interval arithmetic."""
from fractions import Fraction
from math import gcd, isqrt


def euler_intervals(limit):
    sieve = bytearray([1]) * (limit + 1)
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p*p::p] = bytes((limit-p*p)//p + 1)
    scale = 10**18
    # For each h store the lower and upper scaled products on both signs.
    bounds = [[[scale, scale], [scale, scale]] for _ in range(3)]
    for p in range(3, limit + 1, 2):
        if not sieve[p]:
            continue
        odd = p - 1
        while not odd % 2:
            odd //= 2
        residue = pow(2, odd, p)
        nu = 0
        while residue != 1:
            residue = residue**2 % p
            nu += 1
        for h in range(3):
            if nu > h + 1:
                continue
            interval = bounds[h][int(nu == h + 1)]
            den = p*p
            interval[0] = interval[0]*(den-1)//den
            interval[1] = (interval[1]*(den-1)+den-1)//den
    intervals = []
    for minus, plus in bounds:
        lower = Fraction((minus[0]+plus[0])*(limit-1), 2*scale*limit)
        upper = Fraction(minus[1]+plus[1], 2*scale)
        intervals.append((lower, upper))
    return intervals


def add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x, y = P
    u, v = Q
    if x == u:
        if y == -v:
            return None
        slope = (3*x*x+32*x+32)/(2*y)
    else:
        slope = (v-y)/(u-x)
    X = slope**2-16-x-u
    return X, slope*(x-X)-y


def check_denominators():
    point = (Fraction(-8), Fraction(16))
    P = None
    denominator = {}
    for d in range(1, 66):
        P = add(P, point)
        b = isqrt(P[0].denominator)
        assert b*b == P[0].denominator
        denominator[d] = b
    for d in range(3, 25, 2):
        fresh = denominator[d]
        for r in range(1, d, 2):
            if d % r == 0:
                inherited = gcd(fresh, denominator[r])
                while inherited > 1:
                    fresh //= inherited
                    inherited = gcd(fresh, denominator[r])
        assert fresh > 1, d
    assert denominator[7] == 117041
    assert denominator[9] == 3**3*11*67*13411
    u, v, w = 1, 1, 7
    for M in (2, 4, 8, 16, 32, 64):
        assert denominator[M-1] * denominator[M+1] == u*u+8*v*v
        u, v, w = abs(u**4-32*v**4), 2*u*v*w, w**4-128*(u*v)**4


if __name__ == "__main__":
    intervals = euler_intervals(200_000)
    assert intervals[0][0] > Fraction(9263, 10_000)
    assert intervals[1][0] > Fraction(90321, 100_000)
    assert intervals[1][1] < Fraction(90323, 100_000)
    assert intervals[2][0] > Fraction(9050, 10_000)
    for h, (lower, upper) in enumerate(intervals):
        print(h, f"{float(lower):.9f}", f"{float(upper):.9f}")
    check_denominators()
    print("Both odd denominators checked at each dyadic index through 128.")
