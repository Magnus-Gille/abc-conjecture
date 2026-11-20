"""Check finite arithmetic for both elliptic descents at orders nine and eighteen."""

from itertools import product
from math import gcd


def multiply(left, right):
    # Coefficients in Z[t]/(t^3-3t+1), in ascending order.
    result = [0] * 5
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    for degree in (4, 3):
        result[degree - 2] += 3 * result[degree]
        result[degree - 3] -= result[degree]
    return tuple(result[:3])


def curve_order(linear, constant, prime):
    return 1 + sum(
        (y * y - x**3 - linear * x - constant) % prime == 0
        for x, y in product(range(prime), repeat=2)
    )


def homogeneous_factor(x, y, n, cache):
    if n not in cache:
        value = x**n - y**n
        for d in range(1, n):
            if n % d == 0:
                value, rem = divmod(value, homogeneous_factor(x, y, d, cache))
                assert rem == 0
        cache[n] = value
    return cache[n]


def main():
    residues = {
        tuple(c % 4 for c in multiply((0, -1, 0), multiply(h, h)))
        for h in product(range(2), repeat=3)
    }
    assert residues == {
        (0, 0, 0), (0, 2, 3), (0, 3, 0), (1, 0, 1),
        (1, 0, 2), (1, 1, 0), (2, 3, 1), (3, 3, 1),
    }
    for root, linear, constant, orders in [
        ((2, 2, -1), -21, 37, (3, 9)),
        ((6, 3, -3), -81, 243, (3, 7)),
    ]:
        cube = multiply(root, multiply(root, root))
        assert tuple(c + linear * t for c, t in zip(cube, root)) == (-constant, 0, 0)
        assert tuple(curve_order(linear, constant, p) for p in (5, 7)) == orders
        for a, d in product(range(4), repeat=2):
            if gcd(gcd(a, d), 2) == 1:
                target = tuple((b - d*d*t) % 4 for b, t in zip((a, 0, 0), root))
                assert target not in residues

    for a, b in [(2, 1), (5, 2), (7, 4)]:
        cache = {}
        for i, j in product(range(4), range(2, 5)):
            m = 2**i * 3**j
            base, u = (9, m // 9) if i == 0 else (18, m // 18)
            x, y = a**u, b**u
            sign = 1 if base == 9 else -1
            assert homogeneous_factor(a, b, m, cache) == x**6 + sign*x**3*y**3 + y**6
    print("Both cubic descents and 36 cyclotomic substitutions checked.")


if __name__ == "__main__":
    main()
