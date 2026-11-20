"""Check the exact denominator products at rank 265 with integer arithmetic."""

from math import gcd, isqrt, prod

from abc_gaussian_order_witness import gaussian_product, rational_point


GAUSSIAN_PRIMES = [(1, 2), (1, -2), (7, 2), (7, -2)]


def abscissa_data(index):
    if index == 0:
        return 1, 0
    x_coordinate = rational_point(index)[0]
    denominator = isqrt(x_coordinate.denominator)
    assert denominator**2 == x_coordinate.denominator
    return x_coordinate.numerator, denominator


def conjugate_mask(mask):
    return ((mask & 5) << 1) | ((mask & 10) >> 1)


def verify():
    rank = 265
    _, denominator = abscissa_data(rank)
    old_product = abscissa_data(5)[1] * abscissa_data(53)[1]
    products = {}
    nonsquare_factors = []
    counts = [0, 0]
    for mask in range(16):
        alpha = (1, 0)
        for index, prime in enumerate(GAUSSIAN_PRIMES):
            if mask & (1 << index):
                alpha = gaussian_product(alpha, prime)
        a_num, a_den = abscissa_data(alpha[0])
        b_num, b_den = abscissa_data(alpha[1])
        raw = a_num * b_den**2 + b_num * a_den**2
        lower = prod(value for sub, value in products.items() if sub & mask == sub)
        exact, remainder = divmod(raw, lower)
        assert exact > 0 and remainder == 0
        products[mask] = exact
        if mask >= conjugate_mask(mask) or pow(exact, 96, 193) != 192:
            continue
        assert isqrt(exact)**2 != exact
        assert denominator % exact == 0 and gcd(denominator // exact, exact) == 1
        assert all(gcd(exact, previous) == 1 for previous in nonsquare_factors)
        nonsquare_factors.append(exact)
        counts[0] += 1
        if mask & 3 and mask & 12:
            assert gcd(exact, old_product) == 1
            counts[1] += 1
            print(f"Gaussian multiple {alpha}, first-order factor of {exact.bit_length()} bits")
    for mask, exact in products.items():
        assert exact == products[conjugate_mask(mask)]
    assert prod(products.values()) == denominator**2
    assert counts == [5, 3]
    print(f"{counts[0]} coprime nonsquare factors, {counts[1]} first appearing at rank {rank}")


if __name__ == "__main__":
    verify()
