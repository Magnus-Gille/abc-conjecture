"""Square divisors of A and B at n = 7 + 12j. Uses Python's standard library."""

import argparse
import csv
from dataclasses import dataclass
from math import gcd, isqrt, log, prod


def primes_through(bound):
    sieve = bytearray([1]) * (bound + 1)
    for p in range(2, isqrt(bound) + 1):
        if sieve[p]:
            sieve[p*p::p] = bytes((bound - p*p) // p + 1)
    return [p for p in range(2, bound + 1) if sieve[p]]


def prime_factors(value):
    d = 2
    while d * d <= value:
        if value % d == 0:
            yield d
            while value % d == 0:
                value //= d
        d += 1
    if value > 1:
        yield value


def fib_pair(n, mod):
    """Return F_n and F_(n+1) modulo mod by fast doubling."""
    a, b = 0, 1
    for bit in bin(n)[2:]:
        c = a * (2*b - a) % mod
        d = (a*a + b*b) % mod
        if bit == '1':
            a, b = d, (c + d) % mod
        else:
            a, b = c, d
    return a, b


def poly_value(j, label, mod):
    a, b = fib_pair(7 + 12*j, mod)
    t = (2*b - a - 11) % mod
    if label == 'A':
        return (t*t + 10*t + 5) % mod
    return (t*t + 4*t - 1) % mod


@dataclass(frozen=True)
class SquareClass:
    prime: int
    label: str
    residue: int
    modulus: int


def classes_for_prime(p):
    # Both polynomial discriminants are 5 times a square.
    if p % 5 not in (1, 4):
        return []
    # For split p the order of the 12-step Fibonacci matrix divides r.
    r = (p - 1) // gcd(12, p - 1)
    for q in prime_factors(r):
        while r % q == 0 and fib_pair(12 * (r // q), p) == (0, 1):
            r //= q
    p2 = p*p
    classes = []
    x, y = 29 % p, 9349 % p  # L_7 and L_19
    for j in range(r):
        t = x - 11
        for label, value in (('A', t*t + 10*t + 5), ('B', t*t + 4*t - 1)):
            if value % p:
                continue
            v = poly_value(j, label, p2) // p
            slope = (poly_value(j + r, label, p2) // p - v) % p
            if slope:
                k = (-v * pow(slope, -1, p)) % p
                classes.append(SquareClass(p, label, j + r*k, r*p))
            elif v == 0:
                classes.append(SquareClass(p, label, j, r))
        x, y = y, (322*y - x) % p
    assert (x, y) == (29 % p, 9349 % p)
    return classes


def combine(a, m, b, n):
    """Generalized CRT in the j variable; return the least residue and period."""
    g = gcd(m, n)
    if (b - a) % g:
        return None
    reduced = n // g
    step = ((b - a) // g * pow(m // g, -1, reduced)) % reduced
    return a + m * step, m * reduced


def verify_classes(classes):
    for c in classes:
        assert 0 <= c.residue < c.modulus
        for j in (c.residue, c.residue + c.modulus):
            assert poly_value(j, c.label, c.prime**2) == 0


def direct_check(p, classes):
    """Independent check using every consecutive Lucas index over a full period."""
    m = p*p
    x, y = 2, 1
    nmod = 0
    j = 0
    while True:
        if nmod == 7:
            t = x - 11
            for label, value in (('A', t*t + 10*t + 5), ('B', t*t + 4*t - 1)):
                predicted = any(c.label == label and j % c.modulus == c.residue for c in classes)
                assert (value % m == 0) == predicted, (p, j, label)
            j += 1
        x, y = y, (x + y) % m
        nmod = (nmod + 1) % 12
        if (x, y, nmod) == (2, 1, 0):
            break
    assert all(j % c.modulus == 0 for c in classes)


def algebraic_check(p, classes):
    """Optional independent construction using quadratic roots and discrete logs."""
    from sympy import discrete_log, n_order, sqrt_mod

    m = p*p
    expected = set()
    roots_of_five = sqrt_mod(5, m, all_roots=True)
    if roots_of_five:
        s = roots_of_five[0]
        half = pow(2, -1, m)
        alpha = (1 + s) * half % m
        step = pow(alpha, 12, m)
        period = int(n_order(step, m))
        for label, x_values in [('A', (6-2*s, 6+2*s)), ('B', (9-s, 9+s))]:
            for x in x_values:
                for root in sqrt_mod(x*x + 4, m, all_roots=True):
                    u = (x + root) * half % m
                    target = u * pow(alpha, -7, m) % m
                    if pow(target, period, m) == 1:
                        j = 0 if period == 1 else int(discrete_log(m, target, step))
                        expected.add(SquareClass(p, label, j, period))
    assert expected == set(classes), p


def print_record(title, item):
    if item is None:
        print(title, 'none')
        return
    j, m, chosen = item
    n = 7 + 12*j
    D = prod(c.prime for c in chosen)
    labels = ' '.join(f'{c.prime}{c.label}' for c in chosen)
    print(f'{title}: n={n} j={j} j_period={m} D={D} log(D)/n={log(D)/n:.10g} [{labels}]')


def compare_tuples(classes, max_size):
    """Enumerate every compatible tuple of distinct primes through max_size."""
    counts = [0] * (max_size + 1)
    first = [None] * (max_size + 1)
    best = [None] * (max_size + 1)
    scores = [-1.] * (max_size + 1)
    logp = {c.prime: log(c.prime) for c in classes}

    def visit(start, a, m, chosen, log_product):
        for i in range(start, len(classes)):
            c = classes[i]
            if chosen and c.prime == chosen[-1].prime:
                continue
            result = combine(a, m, c.residue, c.modulus)
            if result is None:
                continue
            j, period = result
            size = len(chosen) + 1
            counts[size] += 1
            new_log = log_product + logp[c.prime]
            score = new_log / (7 + 12*j)
            group = chosen + (c,)
            if first[size] is None or j < first[size][0]:
                first[size] = (j, period, group)
            if score > scores[size]:
                scores[size] = score
                best[size] = (j, period, group)
            if size < max_size:
                visit(i+1, j, period, group, new_log)

    visit(0, 0, 1, (), 0.)
    for size in range(1, max_size + 1):
        print(f'compatible class tuples of size {size}: {counts[size]}')
        print_record('earliest', first[size])
        print_record('largest log(D)/n', best[size])


def run(args):
    classes = []
    for p in primes_through(max(args.prime_limit, args.check_limit)):
        if p < 7:
            continue
        local = classes_for_prime(p)
        verify_classes(local)
        if p <= args.check_limit:
            direct_check(p, local)
        if p <= args.prime_limit:
            if args.algebraic_check:
                algebraic_check(p, local)
            classes.extend(local)
    print(f'prime bound {args.prime_limit}, active primes {len({c.prime for c in classes})}, classes {len(classes)}')
    for label in ('A', 'B'):
        hits = [c for c in classes if c.label == label]
        print(f'{label}: {len({c.prime for c in hits})} primes, {len(hits)} classes')
    print('square classes with period in j indivisible by their prime:', sum(c.modulus % c.prime != 0 for c in classes))
    if args.csv:
        with open(args.csv, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['prime','factor','j_residue','j_modulus'])
            w.writerows((c.prime,c.label,c.residue,c.modulus) for c in classes)
    compare_tuples(classes, args.tuple_size)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prime-limit', type=int, default=10000)
    parser.add_argument('--tuple-size', type=int, default=3)
    parser.add_argument('--check-limit', type=int, default=200)
    parser.add_argument('--algebraic-check', action='store_true', help='verify via SymPy')
    parser.add_argument('--csv')
    args = parser.parse_args()
    if min(args.prime_limit, args.check_limit) < 0 or args.tuple_size < 1:
        parser.error('bounds must be nonnegative and tuple size positive')
    run(args)
