"""Rational bounds for the density of gcd(n,b_2n)=1 on each squarefree parity."""

from fractions import Fraction
from math import isqrt, prod

BOUND = 1 << 20
CORE = 12


def small_factors(limit):
    spf = list(range(limit + 1))
    for p in range(2, isqrt(limit) + 1):
        if spf[p] == p:
            for n in range(p * p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


def factor(n, spf):
    exponents = {}
    while n > 1:
        p = spf[n]
        exponents[p] = exponents.get(p, 0) + 1
        n //= p
    return exponents


def pell_zero(n, p):
    a, b = 0, 1
    odd = False
    for bit in bin(n)[2:]:
        a, b = 2*a*b % p, (2*b*b - (-1 if odd else 1)) % p
        odd = bit == "1"
        if odd:
            a, b = (a+b) % p, (b+2*a) % p
    return a == 0


def event_weight(support):
    return Fraction(1, prod(q+1 for q in support))


def exact_avoidance(core):
    value = Fraction()
    for mask in range(1 << len(core)):
        support = set()
        for i, event in enumerate(core):
            if mask >> i & 1:
                support.update(event)
        value += (-1)**mask.bit_count() * event_weight(support)
    return value


def main():
    spf = small_factors(BOUND + 1)
    events = [{}, {}]
    for p in range(3, BOUND, 2):
        if spf[p] != p or p % 8 not in (1, 3):
            continue
        r = p-1 if p % 8 == 1 else p+1
        for q in factor(r, spf):
            while r % q == 0 and pell_zero(r//q, p):
                r //= q
        if r % 4:
            continue
        d = r//4
        f = factor(d, spf)
        if any(e > 1 for e in f.values()):
            continue
        parity = int(2 in f)
        support = frozenset((f.keys() - {2}) | {p})
        known = events[parity]
        if any(q in known and known[q] <= support for q in support):
            continue
        known[p] = support

    for parity, known in enumerate(events):
        listed = sorted(known.values(), key=lambda v: prod(q+1 for q in v))
        core, rest = listed[:CORE], listed[CORE:]
        high = exact_avoidance(core)
        # Round each remainder probability upwards before summing, to keep
        # the denominators small. The error is < len(rest) * 10^-14.
        scale = 10**14
        rest_upper = 0
        for event in rest:
            denom = prod(q+1 for q in event)
            rest_upper += (scale+denom-1)//denom
        # Tail < 2^parity * 12/(sqrt(BOUND) log BOUND);
        # use log 2 > 2/3 and BOUND = 2^20.
        tail_upper = Fraction((1 << parity)*36, 1024*40)
        low = high - Fraction(rest_upper, scale) - tail_upper
        print("parity", parity, "minimal events", len(listed),
              "conditional lower", int(low*1000000)/1000000,
              "upper", -(-high*1000000//1)/1000000)


if __name__ == "__main__":
    main()
