"""Certify fixed-exponent obstructions for every dyadic packet starting at n=8."""

from itertools import product
from math import gcd, isqrt


AUXILIARIES = {
    2: (5,),
    3: (7,),
    5: (31,),
    7: (113,),
    11: (23,),
    13: (1249, 599),
    17: (103,),
    19: (191,),
    23: (47,),
    29: (1567, 1451),
    31: (4093, 311),
    37: (593,),
    41: (1559,),
    43: (2753,),
    47: (6863, 283),
    53: (7103, 5407),
    59: (2833, 4721),
    61: (4759, 8419),
    67: (7103, 269),
    71: (2273,),
    73: (439,),
    79: (2687,),
    83: (4483, 11953),
    89: (5519,),
    97: (1553,),
    101: (6869, 607),
    103: (2267, 16481),
    107: (12841, 7919),
    109: (5233,),
    113: (16273, 19889),
    127: (13463,),
    131: (1049, 5503),
    137: (14797, 6577),
    139: (2503, 15569),
    149: (9239, 15199),
}


def is_prime(p):
    return p > 1 and all(p % d for d in range(2, isqrt(p) + 1))


def orbit(p, q):
    """Track x=X/Y and the multiplicative character of the projective scale."""
    order = 4 if q == 2 else q
    assert is_prime(p) and (p-1) % order == 0
    def character(value):
        return pow(value % p, (p-1)//order, p)

    # (X,Y) = (31²,14²). At infinity the scale is X, elsewhere it is Y.
    X, Y = 961 % p, 196 % p
    x = X * pow(Y, -1, p) % p if Y else None
    scale = character(Y or X)
    seen = {}
    allowed = []
    while (x, scale) not in seen:
        seen[x, scale] = len(allowed)
        if x is None:
            # w² = X², and the next projective pair is (X⁴,0).
            allowed.append(scale*scale % p == 1)
            scale = pow(scale, 4, p)
            continue
        form = (x*x + 16*x + 32) % p
        allowed.append(scale*scale*character(form) % p in (0, 1))
        num = (x*x - 32)**2 % p
        den = 4*x*form % p
        scale = pow(scale, 4, p) * character(den or num) % p
        x = num * pow(den, -1, p) % p if den else None
    split = seen[x, scale]
    period = len(allowed) - split
    return allowed[:split], period, {j % period for j in range(split,len(allowed)) if allowed[j]}


def possible_in_prefix(row, j):
    prefix, period, residues = row
    return prefix[j] if j < len(prefix) else j % period in residues


def verify():
    assert sorted(AUXILIARIES) == [q for q in range(2,151) if is_prime(q)]
    for q, places in AUXILIARIES.items():
        rows = [orbit(p, q) for p in places]
        prefix_end = max(len(prefix) for prefix, _, _ in rows)
        for j in range(prefix_end):
            if all(possible_in_prefix(row, j) for row in rows):
                assert j == 0 and q == 71 and 1 < 2273 < 2**71

        # Generalized CRT checks the entire common tail using absolute phases.
        for choice in product(*(row[2] for row in rows)):
            moduli = [row[1] for row in rows]
            assert any((choice[i]-choice[j]) % gcd(moduli[i], moduli[j]) != 0
                       for i in range(len(rows)) for j in range(i))
    print('All prime exponents through 149 excluded at every dyadic n >= 8.')

    # These periods control the quadratic characters of w for n=128 and 512,
    # where the respective small factors obstruct the use of the modulus 5.
    for p, small_prime in [(17, 67649537), (13, 339767297), (5, 65229783041)]:
        prefix, _, residues = orbit(p, 2)
        assert not any(prefix) and not residues
        assert pow(small_prime, (p-1)//2, p) == 1
    print('Each tested 16 <= n <= 8192 has an odd valuation above n^4.')



# (log_2(n), digits after removing all primes <= n^4, removed factor)
# The norm-disk certificate verifies these independently.
FINITE_ROWS = [
    (4, 14, 1), (5, 54, 1), (6, 214, 1), (7, 847, 67649537),
    (8, 3417, 1), (9, 13657, 339767297), (10, 54662, 1),
    (11, 218645, 1), (12, 874580, 1), (13, 3498307, 65229783041),
]


def prime_sieve(limit):
    flags = bytearray([1]) * (limit + 1)
    flags[:2] = bytes(2)
    for i in range(2, isqrt(limit) + 1):
        if flags[i]:
            flags[i*i::i] = bytes((limit-i*i)//i + 1)
    return flags


def form_residue(k, p):
    X, Y = 961 % p, 196 % p
    for _ in range(k - 3):
        w_squared = (X*X + 16*X*Y + 32*Y*Y) % p
        X, Y = (X*X - 32*Y*Y)**2 % p, 4*X*Y*w_squared % p
    return (X*X + 16*X*Y + 32*Y*Y) % p


def verify_finite_cofactors():
    flags = prime_sieve(27_534_907)
    for k, digits, small in FINITE_ROWS:
        # An integer root z > 1 is itself supported above 2^(4k).
        # If L=z^q, then 2^(4kq) < L < 10^digits < 2^(10*digits/3).
        limit = (5*digits)//(6*k)
        total = 0
        largest_witness = 0
        for q in range(2, limit + 1):
            if not flags[q]:
                continue
            order = 4 if q == 2 else q
            step = order if order % 2 == 0 else 2*order
            for p in range(step + 1, len(flags), step):
                if not flags[p] or small % p == 0:
                    continue
                z = form_residue(k, p) * pow(small, -2, p) % p
                if z and pow(z, (p-1)//order, p) != 1:
                    total += 1
                    largest_witness = max(largest_witness, p)
                    break
            else:
                raise AssertionError((k, q))
        print(f'n={2**k}, all {total} prime exponents through {limit}, '
              f'largest auxiliary prime {largest_witness}')


if __name__ == '__main__':
    verify()
    verify_finite_cofactors()
