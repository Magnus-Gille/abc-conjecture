"""Verify the marked rational abc triple locally at p = 205883."""

from abc_octic_mixed_prime_indices import multiple
from abc_octic_mixed_wieferich import division_value


def verify():
    prime = 205883
    order = 34387
    index = 8443
    assert order == 137 * 251 and multiple(order, prime) is None
    assert all(multiple(order // q, prime) is not None for q in (137, 251))
    assert (index * index + 2) == 2073 * order
    assert 0 < index < order // 2

    modulus = prime ** 3
    def has_depth_two(value):
        return value % (prime ** 2) == 0 and value % modulus != 0

    assert has_depth_two(division_value(order, modulus))
    u, _ = multiple(index, modulus)
    assert has_depth_two(2 * u + 1)
    ratio = (u - 3) * pow(u + 4, -1, modulus) % modulus
    z = 8 * ratio ** 2 % modulus
    assert has_depth_two(z - 8)
    numerator = 7 ** 7 * z ** 2 * (6 * z + 1)
    denominator = (z - 1) ** 3 * (5 * z + 9) * (50 * z ** 2 - 345 * z - 48) ** 2
    image = numerator * pow(denominator, -1, modulus) % modulus
    assert has_depth_two(1 - image)

    u, v = multiple((index + 1) // 2, modulus)
    slope = (u + v) * pow(2 * (u - 1), -1, modulus) % modulus
    assert (slope ** 2 + 2 * slope + 2) % prime != 0
    assert has_depth_two(3 * slope ** 2 - 8 * slope + 6)
    print('Order 34387, least marked index 8443, exact depth two in the new triple.')


if __name__ == '__main__':
    verify()
