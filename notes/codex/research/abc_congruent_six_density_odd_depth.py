"""Eight quadratic-character values certify the density-one bound."""

from math import isqrt


def prime_factors(n):
    factors = []
    for d in range(2, isqrt(n) + 1):
        if n % d:
            continue
        factors.append(d)
        while n % d == 0:
            n //= d
    if n > 1:
        factors.append(n)
    return factors


def gaussian_product(left, right, prime):
    a, b = left
    c, d = right
    return (a * c - b * d) % prime, (a * d + b * c) % prime


def gaussian_power(base, exponent, prime):
    result = (1, 0)
    while exponent:
        if exponent % 2:
            result = gaussian_product(result, base, prime)
        base = gaussian_product(base, base, prime)
        exponent //= 2
    return result


def elliptic_add(left, right, prime):
    if left is None:
        return right
    if right is None:
        return left
    x, y = left
    u, v = right
    if x == u and (y + v) % prime == 0:
        return None
    if left == right:
        slope = (3 * x * x - 36) * pow(2 * y, -1, prime)
    else:
        slope = (v - y) * pow(u - x, -1, prime)
    new_x = (slope * slope - x - u) % prime
    return new_x, (slope * (x - new_x) - y) % prime


def main():
    modulus = 503
    auxiliary = 2011
    generator = (1, 6)
    for prime in (modulus, auxiliary):
        assert prime_factors(prime) == [prime]
    order = modulus * modulus - 1
    assert gaussian_power(generator, order, modulus) == (1, 0)
    for prime in prime_factors(order):
        assert gaussian_power(generator, order // prime, modulus) != (1, 0)

    point = (-3 % auxiliary, 9)
    multiples = [None]
    running = point
    while running is not None:
        multiples.append(running)
        running = elliptic_add(running, point, auxiliary)
    assert len(multiples) == 2 * modulus

    period = order // 2
    odd_part = period
    while odd_part % 2 == 0:
        odd_part //= 2
    primes = prime_factors(odd_part)
    print("mask  exponent   a   b   abscissa sum   sign")
    signs = []
    for mask in range(1 << len(primes)):
        exponent = 1 + sum(period // p for j, p in enumerate(primes)
                           if mask & (1 << j))
        a, b = gaussian_power(generator, exponent, modulus)
        a += (1 - a % 2) * modulus
        b += (b % 2) * modulus
        value = 1 if multiples[b] is None else (
            multiples[a][0] + multiples[b][0]) % auxiliary
        assert value
        symbol = pow(value, (auxiliary - 1) // 2, auxiliary)
        sign = 1 if symbol == 1 else -1
        signs.append(sign)
        print(f"{mask:4} {exponent:9} {a:3} {b:3} {value:14} {sign:6}")
    assert signs == [-1, -1, 1, 1, 1, 1, 1, -1]
    print("The product is -1.")


if __name__ == "__main__":
    main()
