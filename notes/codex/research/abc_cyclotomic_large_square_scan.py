"""Census of prime squares p² | Phi_n(A,B) with p > A² for four degree-six rows."""

import argparse
from bisect import bisect_right
from math import gcd, isqrt

from abc_average_order_check import prime_divisors
from abc_mersenne_quadratic_prime_scan import is_prime, primes_through


# For 0 < B < A, Phi_n(A,B) < K*A^6 with these values of K.
BOUNDS = {7: 7, 9: 3, 14: 1, 18: 1}


def cyclotomic(n, a, b):
    if n == 7:
        return (a**7 - b**7) // (a-b)
    if n == 14:
        return (a**7 + b**7) // (a+b)
    x, y = a**3, b**3
    return x*x + y*y + (x*y if n == 9 else -x*y)


def large_squares(value, a, cutoff, prime_product):
    # The squarefree product contains every eligible prime through K*A^2.
    radical = gcd(value, prime_product)
    rest = value // radical
    repeated = gcd(radical, rest)
    hits = [p for p in prime_divisors(repeated) if p > a*a]
    while repeated > 1:
        rest //= repeated
        repeated = gcd(radical, rest)

    # If p > K*A^2 occurs twice, its complementary factor is < K*A^2,
    # so removing all the small primes leaves exactly p².
    root = isqrt(rest)
    if rest > 1 and root*root == rest:
        assert root > cutoff
        hits.append(root)
    return hits


def scan(height):
    # The extra range supplies the independent brute check for small boxes.
    primes = primes_through(max(7*height**2, isqrt(7*min(height, 20)**6)))
    all_hits = []
    for n, k in BOUNDS.items():
        # Coprimality makes B a unit at any prime dividing Phi. For p not
        # dividing n, separability of T^n-1 forces ord_p(A/B)=n.
        eligible = [p for p in primes if p <= k*height**2 and (n % p == 0 or (p-1) % n == 0)]
        index = 0
        product = 1
        rows = 0
        hits = []
        for a in range(2, height + 1):
            cutoff = k*a*a
            while index < len(eligible) and eligible[index] <= cutoff:
                product *= eligible[index]
                index += 1
            for b in range(1, a):
                if gcd(a, b) != 1:
                    continue
                rows += 1
                value = cyclotomic(n, a, b)
                assert 1 < value < k*a**6
                found = large_squares(value, a, cutoff, product)
                if a <= 20:
                    candidates = primes[bisect_right(primes, a*a):bisect_right(primes, isqrt(value))]
                    assert found == [p for p in candidates if value % (p*p) == 0]
                for p in found:
                    assert is_prime(p, primes) and p > a*a and value % (p*p) == 0
                    cofactor = value // (p*p)
                    exponent = 2
                    while cofactor % p == 0:
                        cofactor //= p
                        exponent += 1
                    assert value == p**exponent * cofactor
                    hits.append((n, a, b, p, exponent, cofactor))
        print(f'n={n}: {len(hits)} hits among {rows} coprime pairs.')
        all_hits.extend(hits)
    return all_hits


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--height', type=int, default=500)
    args = parser.parse_args()
    if args.height < 2:
        parser.error('height must be at least 2')
    hits = scan(args.height)
    print('n,A,B,p,valuation,remaining_cofactor')
    for row in hits:
        print(*row, sep=',')


if __name__ == '__main__':
    main()
