"""Enumerate abc triples with a specified share of repeated factors from a seed.

The threshold is eta=1/10. Give the two positive coprime seed addends for a
one-step enumeration, or --through H for the closure of all starting triples
of height at most H. Requires sympy.
"""

import argparse
from collections import deque
from functools import lru_cache
from itertools import product
from math import gcd, prod

from sympy import factorint, integer_nthroot


@lru_cache(maxsize=None)
def radical(value):
    return prod(factorint(value))


def convergents(numerator, denominator):
    prev_num, num = 0, 1
    prev_den, den = 1, 0
    while denominator:
        quotient, remainder = divmod(numerator, denominator)
        prev_num, num = num, quotient * num + prev_num
        prev_den, den = den, quotient * den + prev_den
        yield num, den
        numerator, denominator = denominator, remainder


def prime_assignments(prime, exponent):
    yield 1, 1, 1, 1
    for place in range(3):
        power = 1
        for _ in range(exponent):
            power *= prime
            parts = [1, 1, 1]
            parts[place] = power
            yield (*parts, prime)


def profiles(seed_product):
    choices = [list(prime_assignments(p, e)) for p, e in factorint(seed_product).items()]
    for allocation in product(*choices):
        yield tuple(prod(column) for column in zip(*allocation))


def enumerate_triples(seed_product):
    results = []
    for da, db, dc, support in profiles(seed_product):
        if support <= 2 or dc < support:
            continue
        common = da * db * dc
        residue = -da * pow(db, -1, dc) % dc
        for k, x in convergents(residue, dc):
            y = residue * x - k * dc
            if y <= 0 or x * y * support > dc:
                continue
            a, b = da * x, db * y
            c = a + b
            if a > b or gcd(a, b) != 1:
                continue
            if (gcd(a, seed_product), gcd(b, seed_product), gcd(c, seed_product)) != (da, db, dc):
                continue
            rad = radical(a) * radical(b) * radical(c)
            excess = a * b * c // rad
            fresh = excess // (common // support)
            if rad**10 <= c**9 and fresh**10 <= c:
                results.append((a, b, c, rad, fresh))
    return sorted(results, key=lambda row: (row[2], row[0]))


def small_exceptions(limit):
    radicals = [1] * (limit + 1)
    for p in range(2, limit + 1):
        if radicals[p] == 1:
            for i in range(p, limit + 1, p):
                radicals[i] *= p
    for c in range(2, limit + 1):
        bound = integer_nthroot(c**9, 10)[0] // radicals[c]
        for a in range(1, c // 2 + 1):
            b = c - a
            if radicals[a] * radicals[b] <= bound and gcd(a, b) == 1:
                yield a, b, c


def closure(initial):
    seen = set(initial)
    queue = deque(seen)
    edges = 0
    while queue:
        a, b, c = queue.popleft()
        descendants = enumerate_triples(a * b * c)
        edges += len(descendants)
        for x, y, z, _, _ in descendants:
            triple = x, y, z
            if triple not in seen:
                seen.add(triple)
                queue.append(triple)
    return seen, edges


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("addends", type=int, nargs="*")
    parser.add_argument("--through", type=int, metavar="H")
    args = parser.parse_args()
    if args.through is not None:
        if args.addends or args.through < 2:
            parser.error("--through takes a height of at least two and no seed addends")
        starts = set(small_exceptions(args.through))
        reached, edges = closure(starts)
        print(f"{len(starts)} starts, {len(reached)} reachable triples, {edges} directed edges")
        print("Additional triples in increasing height order")
        for row in sorted(reached - starts, key=lambda t: (t[2], t[0])):
            print(*row)
    else:
        if len(args.addends) != 2:
            parser.error("give two seed addends or --through H")
        a, b = args.addends
        if min(a, b) < 1 or gcd(a, b) != 1:
            parser.error("seed addends must be positive and coprime")
        rows = enumerate_triples(a * b * (a + b))
        print("a b c rad(abc) fresh")
        for row in rows:
            print(*row)
        print(f"{len(rows)} triples")
