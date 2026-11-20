"""Verify a two-generator parameter with prescribed exact depths at two primes."""

from math import prod

from abc_cm_twist_depth_example import degree_eleven_factors, residue
from abc_cm_pell_whole_triple import pell


def multiply(z, w, modulus):
    b, a = z
    d, c = w
    return (b*d+2*a*c) % modulus, (a*d+b*c) % modulus


def power(z, exponent, modulus):
    if exponent < 0:
        # Conjugation is inversion in the projective group of units.
        z = z[0], -z[1]
        exponent = -exponent
    result = (1, 0)
    while exponent:
        if exponent % 2:
            result = multiply(result, z, modulus)
        z = multiply(z, z, modulus)
        exponent //= 2
    return result


def crt(values, moduli):
    result, period = 0, 1
    for value, modulus in zip(values, moduli):
        result += period*((value-result)*pow(period, -1, modulus) % modulus)
        period *= modulus
    return result


def digit_lift(function, p, depth):
    exponent, step = 0, 1
    for j in range(1, depth+1):
        size = p**j
        value = function(exponent, p*size)
        moved = function(exponent+step, p*size)
        assert value % size == moved % size == 0
        exponent += step*(-(value//size)*pow((moved-value)//size, -1, p) % p)
        assert function(exponent, p*size) == 0
        step *= p
    return exponent


def nearest(num, den):
    if den < 0:
        return nearest(-num, -den)
    return (2*num+den)//(2*den)


def determinant(z, w):
    return z[0]*w[1]-z[1]*w[0]


def shorten(target, slope, modulus):
    # The kernel is x+slope*y = 0 mod modulus.
    u, v = (modulus, 0), (-slope, 1)
    def squared(z):
        return z[0]**2+z[1]**2
    while True:
        if squared(v) < squared(u):
            u, v = v, u
        if 2*abs(u[0]*v[0]+u[1]*v[1]) <= squared(u):
            break
        t = nearest(u[0]*v[0]+u[1]*v[1], squared(u))
        v = v[0]-t*u[0], v[1]-t*u[1]
    base = (target, 0)
    den = determinant(u, v)
    assert abs(den) == modulus
    i = nearest(determinant(base, v), den)
    j = nearest(determinant(u, base), den)
    x, y = target-i*u[0]-j*v[0], -i*u[1]-j*v[1]
    assert (x+slope*y-target) % modulus == 0
    return x, y


def main():
    primes, locations = [683, 1409], [1213, 3706]
    D = prod(primes)
    slopes = []
    for p, n in zip(primes, locations):
        b, a = pell(n, p)
        slopes.append(a*pow(b, -1, p) % p)
    seed = 1, crt(slopes, primes)
    first, second = (1, D), (1, 2*D)
    _, full = degree_eleven_factors()
    print("D and seed", D, seed)
    for k in (2, 4, 8, 12):
        coefficients, targets = [], []
        for p in primes:
            def relation(n, modulus):
                z = power(first, n, modulus)
                return determinant(z, second) % modulus
            def target(n, modulus):
                b, a = multiply(seed, power(first, n, modulus), modulus)
                return residue(full, a*pow(b, -1, modulus) % modulus, modulus)
            coefficients.append(digit_lift(relation, p, k))
            root = digit_lift(target, p, k)
            targets.append((root+p**(k-1)) % p**k)
        moduli = [p**k for p in primes]
        x, y = shorten(crt(targets, moduli), crt(coefficients, moduli), prod(moduli))
        witnesses = []
        for p in primes:
            modulus = p**(k+1)
            z = multiply(power(first, x, modulus), power(second, y, modulus), modulus)
            b, a = multiply(seed, z, modulus)
            value = residue(full, a*pow(b, -1, modulus) % modulus, modulus)
            assert value % p**k == 0 and value != 0
            witnesses.append(value//p**k)
        print("k, exponents, nonzero residues", k, (x, y), witnesses)


if __name__ == "__main__":
    main()
