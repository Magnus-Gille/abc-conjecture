"""Verify the scalar character identities and the separation of all unit residues."""
from math import gcd, isqrt, lcm, prod

MODULI = (120, 240, 264, 312, 408, 696, 984, 4440, 6360, 7560, 10680, 15960)


def primes(bound):
    possible = bytearray([1]) * (bound + 1)
    possible[:2] = bytes(2)
    for p in range(2, isqrt(bound) + 1):
        if possible[p]:
            possible[p*p::p] = bytes((bound - p*p) // p + 1)
    return [p for p in range(2, bound + 1) if possible[p]]


def local_table(p):
    """Encode negative, zero, positive as 0, 1, 2; identity is positive."""
    characters = bytearray(p)
    characters[0] = 1
    for value in range(1, p):
        characters[value * value % p] = 2
    a, b = (-2) % p, 8 % p
    x, y = a, b
    values = bytearray([2])
    while True:
        values.append(characters[8*(6-x) % p])
        if x == a and (y + b) % p == 0:
            return bytes(values)
        if x == a:
            slope = (3*a*a + 72*a + 36) * pow(2*b, -1, p)
        else:
            slope = (y-b) * pow(x-a, -1, p)
        x_new = (slope*slope - 36 - x - a) % p
        y = (slope*(x - x_new) - y) % p
        x = x_new


def jacobi(a, n):
    assert n % 2 == 1
    sign = 1
    a %= n
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                sign = -sign
        if a % 4 == n % 4 == 3:
            sign = -sign
        n, a = a, n % a
    return sign if n == 1 else 0


def main():
    tables = {p: local_table(p) for p in primes(10000) if p >= 5}
    for d, modulus, places in (
        (2, 8, (5,)), (3, 24, (577,)), (5, 10, (17,)),
        (13, 26, (41, 233)), (17, 34, (241,))
    ):
        assert all(modulus % len(tables[p]) == 0 for p in places)
        for n in range(1, modulus, 2):
            if gcd(n, modulus) != 1:
                continue
            observed = prod(tables[p][n % len(tables[p])] - 1 for p in places)
            assert observed == jacobi(d, n)
        print("Character", d, modulus, places)

    for modulus in MODULI:
        local = [row for row in tables.values() if modulus % len(row) == 0]
        signatures = set()
        for n in range(1, modulus // 2 + 1, 2):
            if gcd(n, modulus) != 1:
                continue
            key = bytes(row[n % len(row)] for row in local)
            assert 1 not in key
            assert key not in signatures
            signatures.add(key)
        print("Modulus, places, sign classes:", modulus, len(local), len(signatures))

    combined = lcm(*MODULI)
    assert combined == 144923830996024080
    support = (2, 3, 5, 7, 11, 13, 17, 19, 29, 37, 41, 53, 89)
    phi = combined
    rest = combined
    for p in support:
        assert rest % p == 0
        while rest % p == 0:
            rest //= p
        phi = phi // p * (p - 1)
    assert rest == 1 and phi // 2 == 11018538949017600
    print("Combined modulus and half totient:", combined, phi // 2)


if __name__ == "__main__":
    main()
