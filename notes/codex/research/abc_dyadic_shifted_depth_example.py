"""Certify the reduction order, depth and multiplicative orders at p=205883."""
from functools import cache
from math import isqrt

p = 205883
rank = 137 * 251
modulus = p**3
x = -8
b2, b4, b8 = 64, 64, -1024
initial = [
    0, 1, 32, 3*x**4 + b2*x**3 + 3*b4*x**2 + b8,
    32*(2*x**6 + b2*x**5 + 5*b4*x**4 + 10*b8*x**2 + b2*b8*x+b4*b8),
]


@cache
def division_polynomial(n):
    if n < 5:
        return initial[n] % modulus
    k = n // 2
    f = division_polynomial
    if n % 2:
        return (f(k+2)*f(k)**3 - f(k-1)*f(k+1)**3) % modulus
    return (f(k)*pow(32, -1, modulus)*(f(k+2)*f(k-1)**2-f(k-2)*f(k+1)**2)) % modulus


if __name__ == "__main__":
    for prime in (p, 137, 251, 2, 5, 17, 311, 331):
        assert all(prime % d for d in range(2, isqrt(prime) + 1))
    assert rank == 34387
    assert division_polynomial(rank) == 69702*p**2
    assert division_polynomial(137) % p == 86204
    assert division_polynomial(251) % p == 86237
    assert 1700 == 2**2*5**2*17
    assert pow(2, 1700, rank) == 1
    assert all(pow(2, 1700//q, rank) != 1 for q in (2,5,17))
    assert pow(2, 850, rank) == 3013
    assert p-1 == 2*311*331
    assert all(pow(2, (p-1)//q, p) != 1 for q in (2,311,331))
    assert pow(2, p-1, p*p) == 1 + 103791*p
    print("205883 has first depth two at rank 34387; both order certificates verified.")
