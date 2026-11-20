"""Enumerate single-prime certificates for the 7th and 9th power triples.

For each n in {7,9}, prime p <= --max-prime and 2 <= e <= --max-exponent,
enumerate positive coprime B < A with ord_p(B/A) = n, p^e | A^n-B^n and
p^(21(e-1)) > A^(42+n). No independent height cutoff is imposed. Since the
radical of B^n + (A^n-B^n) = A^n is at most AB(A^n-B^n)/p^(e-1), a hit
has quality greater than n/(n+2-(e-1) log(p)/log(A)) > 21/20.

Put Q=p^e and M=floor(sqrt(p^(e-1))). The strict height test implies
A^2 < p^(42(e-1)/(42+n)) < p^(e-1), hence B < A <= M and 2M^2 < Q.
All eligible residues r=B/A modulo Q are the unique Hensel lifts of the
primitive n-th roots modulo p; necessarily n | p-1.

Rational reconstruction uses the Euclidean remainders of Q,r and their
signed coefficients of r. For either orientation u/v of the pair, an eligible
residue satisfies r*v-u=k*Q with gcd(k,v)=1 and 2uv <= 2M^2 < Q. The error
|r/Q-k/v|=u/(vQ) is less than 1/(2v^2), so k/v is a convergent. In the
Euclidean algorithm its numerator error u is a remainder, with signed
coefficient v. Take the first remainder at most M. If a later
remainder had denominator at most M, the adjacent determinant identity
Q = r_i |a_(i+1)| + r_(i+1) |a_i| would give Q <= 2M^2. Thus this first
remainder is the only possible candidate. Two reduced fractions in the
height box also have determinant smaller than Q, giving uniqueness directly.
Reciprocal residue roots exchange numerator and denominator. One representative
of each inverse pair therefore suffices when both positive orientations are tested.

Default bounds are inclusive. Each printed record is one (n,p,e,A,B);
a seed can appear at several e. The small direct check is independent of
Hensel lifting and of rational reconstruction. All membership tests are exact.

Each of these argument pairs gives exactly the tuples (7,71,4,150,43),
(7,71,5,150,43) and (9,19,3,11,6):
    --max-prime 2000 --max-exponent 300
    --max-prime 200000 --max-exponent 120
    --max-prime 2000000 --max-exponent 12
The targeted run --prime 71 --index 7 --max-exponent 500 gives the first two.
"""

import argparse
from collections import Counter
from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction
from math import gcd, isqrt


INDICES = (7, 9)


@dataclass(frozen=True, order=True)
class Hit:
    n: int
    p: int
    e: int
    A: int
    B: int


def primes_through(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start::p] = b"\x00" * ((limit - start) // p + 1)
    return (p for p in range(2, limit + 1) if sieve[p])


def proper_index(n):
    """Maximal proper divisor of one of the two prime-power indices."""
    return 1 if n == 7 else 3


def primitive_roots(n, p):
    """Return all residues of exact order n, assuming n divides p-1."""
    for base in range(2, p):
        generator = pow(base, (p - 1) // n, p)
        if pow(generator, proper_index(n), p) != 1:
            return [pow(generator, j, p) for j in range(1, n) if gcd(j, n) == 1]
    raise ArithmeticError("no generator found for the residue subgroup")


def reconstruct(root, modulus, bound):
    previous, remainder = modulus, root
    old_coeff, coefficient = 0, 1
    while remainder > bound:
        quotient, next_remainder = divmod(previous, remainder)
        previous, remainder = remainder, next_remainder
        old_coeff, coefficient = coefficient, old_coeff - quotient * coefficient
    if 0 < coefficient <= bound and remainder != coefficient and gcd(remainder, coefficient) == 1:
        return remainder, coefficient
    return None


def search(max_prime, max_exponent, only_prime=None, indices=INDICES):
    hits = []
    primes = (only_prime,) if only_prime is not None else primes_through(max_prime)
    for p in primes:
        for n in indices:
            if (p - 1) % n:
                continue
            for root_mod_p in primitive_roots(n, p):
                if root_mod_p > pow(root_mod_p, -1, p):
                    continue
                root = root_mod_p
                modulus = p
                derivative_inverse = pow(n * pow(root, n - 1, p), -1, p)
                for e in range(2, max_exponent + 1):
                    next_modulus = modulus * p
                    error_digit = (pow(root, n, next_modulus) - 1) // modulus
                    root += (-error_digit * derivative_inverse % p) * modulus
                    bound = isqrt(modulus)
                    modulus = next_modulus
                    pair = reconstruct(root, modulus, bound)
                    if pair is None:
                        continue
                    numerator, denominator = pair
                    A, B = max(pair), min(pair)
                    if p ** (21 * (e - 1)) > A ** (42 + n):
                        # Independently verify every reported lift and its order.
                        assert A % p and (denominator * root - numerator) % modulus == 0
                        assert (pow(A, n, modulus) - pow(B, n, modulus)) % modulus == 0
                        ratio = B * pow(A, -1, p) % p
                        assert pow(ratio, n, p) == 1 and pow(ratio, proper_index(n), p) != 1
                        hits.append(Hit(n, p, e, A, B))
    return sorted(hits)


def direct_check(max_prime=73, max_exponent=5):
    """Visit every height allowed by the certificate at these test bounds."""
    expected = []
    for p in primes_through(max_prime):
        for n in INDICES:
            if (p - 1) % n:
                continue
            for e in range(2, max_exponent + 1):
                limit = p ** (21 * (e - 1))
                max_A = 1
                while (max_A + 1) ** (42 + n) < limit:
                    max_A += 1
                modulus = p ** e
                powers = [pow(x, n, modulus) for x in range(max_A + 1)]
                for A in range(2, max_A + 1):
                    if A % p == 0:
                        continue
                    for B in range(1, A):
                        if powers[B] == powers[A] and gcd(A, B) == 1:
                            ratio = B * pow(A, -1, p) % p
                            if pow(ratio, proper_index(n), p) != 1:
                                expected.append(Hit(n, p, e, A, B))
    actual = search(max_prime, max_exponent)
    if sorted(expected) != actual:
        raise ArithmeticError("small direct enumeration disagrees with reconstruction")
    return len(actual)


def log_bounds(value):
    # Decimal.ln is correctly rounded. Its two neighbors enclose the exact log.
    with localcontext() as context:
        context.prec = 80
        center = Decimal(value).ln()
        return Fraction(center.next_minus()), Fraction(center.next_plus())


def exponent_bounds(hit):
    plo, phi = log_bounds(hit.p)
    alo, ahi = log_bounds(hit.A)
    return (hit.e - 1) * plo / ahi, (hit.e - 1) * phi / alo


def quality_score(hit):
    lo, hi = exponent_bounds(hit)
    return (lo - 2) / hit.n, (hi - 2) / hit.n


def decimal_string(value):
    with localcontext() as context:
        context.prec = 20
        return str(Decimal(value.numerator) / Decimal(value.denominator))


def report_best(hits, name, bounds):
    scores = [(bounds(hit), hit) for hit in hits]
    best_lower = max(interval[0] for interval, _ in scores)
    leaders = [hit for interval, hit in scores if interval[1] >= best_lower]
    keys = {(hit.n, hit.p, hit.e, hit.A) for hit in leaders}
    if len(keys) != 1:
        print(f"{name}: leading intervals overlap at precision 80; listing all contenders")
    for hit in leaders:
        lo, hi = exponent_bounds(hit)
        exponent = (lo + hi) / 2
        normalized = (exponent - 2) / hit.n
        quality = 1 / (1 - normalized)
        difference = hit.A ** hit.n - hit.B ** hit.n
        radical_cap = hit.A * hit.B * difference // hit.p ** (hit.e - 1)
        log_A_lo, _ = log_bounds(hit.A)
        _, log_cap_hi = log_bounds(radical_cap)
        product_quality = hit.n * log_A_lo / log_cap_hi
        print(f"{name} {hit} exponent={decimal_string(exponent)} "
              f"normalized={decimal_string(normalized)} quality_bound={decimal_string(quality)} "
              f"radical_cap={radical_cap} product_quality_bound={decimal_string(product_quality)}")


def report(hits, show_records):
    if show_records:
        print("n p e A B")
        for h in hits:
            print(h.n, h.p, h.e, h.A, h.B)
    print("qualifying tuples", len(hits))
    print("distinct (A,B) seeds", len({(h.A, h.B) for h in hits}))
    print("distinct (n,A,B) seeds", len({(h.n, h.A, h.B) for h in hits}))
    print("distinct (n,p,A,B) prime certificates", len({(h.n, h.p, h.A, h.B) for h in hits}))
    for n in INDICES:
        rows = [h for h in hits if h.n == n]
        print(f"n={n} tuples={len(rows)} seeds={len({(h.A, h.B) for h in rows})}")
    print("tuples by e", dict(sorted(Counter(h.e for h in hits).items())))
    if hits:
        max_A = max(h.A for h in hits)
        print("largest A", max_A, [h for h in hits if h.A == max_A])
        report_best(hits, "largest raw exponent", exponent_bounds)
        report_best(hits, "strongest quality certificate", quality_score)
    print("150,43 certificate at n=7,p=71,e=5", Hit(7, 71, 5, 150, 43) in hits)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    primes = parser.add_mutually_exclusive_group()
    primes.add_argument("--max-prime", type=int, default=20000)
    primes.add_argument("--prime", type=int, help="search only this prime")
    parser.add_argument("--index", type=int, choices=INDICES, help="search only this index")
    parser.add_argument("--max-exponent", type=int, default=60)
    parser.add_argument("--summary-only", action="store_true")
    args = parser.parse_args()
    if args.max_prime < 2 or args.max_exponent < 2:
        parser.error("both bounds must be at least 2")
    if args.prime is not None:
        if args.prime < 2 or any(args.prime % d == 0 for d in range(2, isqrt(args.prime) + 1)):
            parser.error("--prime must be a prime number")
    indices = INDICES if args.index is None else (args.index,)
    prime_limit = f"p<={args.max_prime}" if args.prime is None else f"p={args.prime}"
    small = direct_check()
    print(f"direct check through p=73, e=5: {small} tuples, all heights")
    print(f"complete limits n={indices}, {prime_limit}, 2<=e<={args.max_exponent}")
    report(search(args.max_prime, args.max_exponent, args.prime, indices), not args.summary_only)


if __name__ == "__main__":
    main()
