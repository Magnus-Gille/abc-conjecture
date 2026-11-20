"""Count first-depth-one primes for A=(1,1) on y²=x³−8x²+8x."""

from sys import argv

from abc_octic_mixed_wieferich import division_value

try:
    from cypari import pari
except ImportError:
    from cypari2 import Pari
    pari = Pari()


def verify_exception(p):
    finite_curve = pari.ellinit([0, -8, 0, 8, 0], p)
    order = int(pari.ellorder(finite_curve, [1, 1]))
    depth = 2
    while division_value(order, p ** (depth + 1)) == 0:
        depth += 1
    one = pari(f'1+O({p}^{2 * depth + 8})')
    local_curve = pari.ellinit([0, -8, 0, 8 * one, 0 * one])
    multiple = pari.ellmul(local_curve, [one, one], order)
    assert int(pari.valuation(multiple[0], p)) == -2 * depth
    if p in (4871, 205883):
        index = 4873 if p == 4871 else 34387
        u, v = pari.ellmul(local_curve, [one, one], (index + 1) // 2)
        slope = (v + u) / (2 * (u - 1))
        if p == 4871:
            assert int(pari.valuation(slope, p)) == -2
        else:
            assert int(pari.valuation(slope ** 2 + 2, p)) == 4
    return p, order, depth


def count_primes(limit):
    curve = pari.ellinit([0, -8, 0, 8, 0])
    exceptions = []
    tested = 0
    for entry in pari.primes([7, limit]):
        p = int(entry)
        group_order = int(pari.ellcard(curve, p))
        assert group_order % p
        value = division_value(group_order, p * p)
        assert value % p == 0
        tested += 1
        if value == 0:
            exceptions.append(verify_exception(p))
    return tested, exceptions


if __name__ == '__main__':
    bound = int(argv[1]) if len(argv) > 1 else 100000
    tested, exceptions = count_primes(bound)
    print(f'7 ≤ p ≤ {bound}: {tested} primes, {tested-len(exceptions)} of first depth one')
    print('Exceptional (prime, order, depth):', exceptions)
