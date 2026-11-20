"""Exact checks for the primitive packet discriminant note (standard library)."""

from functools import cache
from math import gcd, isqrt, prod


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def division_value(n, modulus, x=1, y=1):
    """Value of psi_n on y²=x³−8x²+8x at a point with 2y invertible."""
    assert (y * y - x**3 + 8 * x**2 - 8 * x) % modulus == 0
    initial = (
        0,
        1,
        2 * y,
        3 * x**4 - 32 * x**3 + 48 * x**2 - 64,
        2 * y * (2 * x**6 - 32 * x**5 + 80 * x**4 - 640 * x**2 + 2048 * x - 1024),
    )
    inverse = pow(2 * y, -1, modulus)

    @cache
    def psi(i):
        if i < len(initial):
            return initial[i] % modulus
        k = i // 2
        if i % 2:
            value = psi(k + 2) * psi(k)**3 - psi(k - 1) * psi(k + 1)**3
        else:
            value = inverse * psi(k) * (
                psi(k + 2) * psi(k - 1)**2 - psi(k - 2) * psi(k + 1)**2
            )
        return value % modulus

    return psi(n)


def fixed_point():
    p = 205883
    r = 34387
    assert prime(p) and p % 8 == 3
    assert prime(137) and prime(251) and r == 137 * 251
    v137 = division_value(137, p)
    v251 = division_value(251, p)
    assert (v137, v251) == (48637, 126586)
    value = division_value(r, p**3)
    assert value == 34977 * p**2
    shifted_y = (1 - 5 * p * pow(2, -1, p**2)) % p**2
    shifted = division_value(r, p**2, 1 + p, shifted_y)
    derivative = (shifted - value) // p % p
    assert shifted % p == 0 and derivative == 132358
    invert_proper = pow(v137 * v251, -1, p)
    assert value // p**2 * invert_proper % p == 100540
    assert derivative * invert_proper % p == 96176
    root_digit = -(value // p**2) * pow(derivative, -1, p) % p
    assert root_digit == 106494
    lifted_x = 1 + root_digit * p**2
    lifted_y = (1 - 5 * (lifted_x - 1) * pow(2, -1, p**3)) % p**3
    assert division_value(r, p**3, lifted_x, lifted_y) == 0


def jacobi(a, m):
    sign = 1
    a %= m
    while a:
        while a % 2 == 0:
            a //= 2
            if m % 8 in (3, 5):
                sign = -sign
        if a % 4 == m % 4 == 3:
            sign = -sign
        a, m = m % a, a
    return sign if m == 1 else 0


def finite_field_frequency(m):
    """First nonzero Jacobi sum frequency, using a primitive m-th root modulo q."""
    q = m + 1
    while not prime(q):
        q += m
    for base in range(2, q):
        root = pow(base, (q - 1) // m, q)
        if all(pow(root, j, q) != 1 for j in range(1, m)):
            break
    else:
        raise AssertionError("No primitive root of the required order")
    assert pow(root, m, q) == 1
    coefficients = [jacobi(a, m) for a in range(m)]
    for k in range(1, m + 1):
        total = sum(v * pow(root, k * a, q) for a, v in enumerate(coefficients))
        if total % q:
            return k
    raise AssertionError("All frequencies vanished")


def cube_radical(m):
    """Batched small-prime removal and an exact square test on the residual."""
    bound = 0
    while (bound + 1)**3 <= m:
        bound += 1
    small_product = prod(p for p in range(2, bound + 1) if prime(p)) % m
    small_radical = gcd(m, small_product)
    remaining = m
    while (common := gcd(remaining, small_product)) > 1:
        remaining //= common
    root = isqrt(remaining)
    return small_radical * (root if root * root == remaining else remaining)


if __name__ == "__main__":
    fixed_point()
    samples = {3: 3, 9: 3, 15: 15, 25: 5, 27: 3, 45: 15, 49: 7,
               75: 15, 105: 105, 121: 11, 125: 5, 225: 15}
    for m, radical in samples.items():
        assert finite_field_frequency(m) == m // radical
    for m in range(1, 2500):
        expected = prod(p for p in range(2, m + 1) if m % p == 0 and prime(p))
        assert cube_radical(m) == expected
    print("Fixed point, twelve finite-field Fourier cases, and 2499 cube-root sieves verified.")
