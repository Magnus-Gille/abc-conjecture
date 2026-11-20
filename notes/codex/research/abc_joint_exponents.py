"""Search for certified abc hits using 35th roots modulo prime powers."""

from math import gcd

from sympy import primerange, primitive_root


def candidate_bases(residue, modulus, prime):
    """Yield x and h for two coprime bases x and x+h from convergents."""
    previous, remainder = modulus, residue
    previous_denominator, denominator = 0, 1
    sign = 1
    while remainder:
        # The signed remainder is denominator*residue - numerator*modulus.
        signed = sign * remainder
        if denominator % prime and (signed > 0 or signed + denominator < 0):
            yield min(abs(signed), abs(signed + denominator)), denominator
        quotient, next_remainder = divmod(previous, remainder)
        previous, remainder = remainder, next_remainder
        previous_denominator, denominator = (
            denominator,
            previous_denominator + quotient * denominator,
        )
        sign = -sign


def search(limit=100_000):
    exponent = 35
    eligible = residues = direct_hits = 0
    hits = set()
    for prime in primerange(2, limit + 1):
        order = gcd(prime - 1, exponent)
        if exponent % prime == 0 or order == 1:
            continue
        eligible += 1
        modulus = prime**exponent
        threshold = modulus // prime
        generator = int(primitive_root(prime))
        root = pow(generator, (prime - 1) // order * threshold, modulus)
        power = 1
        for _ in range(1, order):
            power = power * root % modulus
            residue = pow(power - 1, -1, modulus)
            residues += 1
            direct_hits += threshold > exponent * residue
            if residue > modulus // 2:
                continue
            for x, h in candidate_bases(residue, modulus, prime):
                if threshold > exponent * x * h:
                    y = x + h
                    assert gcd(x, y) == 1
                    assert pow(x, exponent, modulus) == pow(y, exponent, modulus)
                    hits.add((prime, x, y))
    return eligible, residues, direct_hits, sorted(hits)


if __name__ == "__main__":
    eligible, residues, direct_hits, hits = search()
    print(f"{eligible} primes, {residues} residues, {direct_hits} direct hits")
    for prime, x, y in hits:
        print(f"p={prime} x={x} y={y}")
    assert (eligible, residues, direct_hits) == (3588, 28514, 0)
    assert len(hits) == len({prime for prime, x, y in hits}) == 8
