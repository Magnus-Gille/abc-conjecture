"""All full mixed-orbit support classes for 4871 and 205883."""

from math import gcd, lcm

from abc_octic_mixed_prime_indices import add
from abc_octic_mixed_wieferich import division_value


def projective_slope(point, p):
    if point is None or point == (1, 1):
        return 1, 0
    if point == (1, p - 1):
        # The other point of this slope fiber is 2A, with slope 7/4.
        return 7, 4
    u, v = point
    return (u + v) % p, 2 * (u - 1) % p


def support(point, p):
    s, t = projective_slope(point, p)
    assert s % p or t % p
    factors = {'s': s, 't': t, 'D': s*s - 2*t*t, 'U': (s+t)**2 + t*t,
               'Y': s*s + 2*t*t, 'V': (s-t)**2 + t*t}
    return [name for name, value in factors.items() if value % p == 0]


def classes(p, r):
    point = None
    result = {}
    for n in range(r):
        labels = support(point, p)
        assert len(labels) <= 1
        if labels:
            result[(2*n - 1) % (2*r)] = labels[0]
        point = add(point, (1, 1), p)
        assert (point is None) == (n+1 == r)
    return result


def crt(a, b, r, s):
    g = gcd(r, s)
    assert (b-a) % g == 0
    return (a + r * ((b-a)//g) * pow(r//g, -1, s//g)) % lcm(r, s)


def normalized_residue(p, e, index, factor):
    modulus = p**(e + 1)
    n = (index + 1)//2

    def w(k):
        return division_value(k, modulus)

    inv = pow(w(n), -1, modulus)
    u = (1 - w(n-1)*w(n+1)*inv**2) % modulus
    v = w(2*n)*pow(2, -1, modulus)*pow(inv, 4, modulus) % modulus
    assert (v*v - u**3 + 8*u*u - 8*u) % modulus == 0
    slope = (u+v)*pow(2*(u-1), -1, modulus) % modulus
    value = slope if factor == 's' else (slope*slope+2) % modulus
    assert value % (p**e) == 0
    return value//(p**e)


def run():
    a = classes(4871, 2436)
    b = classes(205883, 34387)
    assert a == {1: 't', 2435: 's', 2437: 's', 4871: 't'}
    assert b == {1: 't', 34387: 'Y', 68773: 't'}
    combined = sorted((crt(i, j, 4872, 68774), v, w)
                      for i, v in a.items() for j, w in b.items())
    assert lcm(4872, 68774) == 167533464
    assert combined[0] == (1, 't', 't')  # Degenerate full index.
    assert combined[1] == (15095893, 's', 'Y')
    assert [n for n, _, _ in combined] == [
        1, 15095893, 30191785, 53574947, 68670839, 83766731,
        83766733, 98862625, 113958517, 137341679, 152437571, 167533463,
    ]
    assert normalized_residue(4871, 2, 2435, 's') == 1717
    assert normalized_residue(205883, 4, 34387, 'Y') == 99897
    assert normalized_residue(4871, 2, 15095893, 's') == 2886
    assert normalized_residue(205883, 4, 15095893, 'Y') == 130407
    print('Verified both support periods, the 12 CRT classes, and the first simultaneous valuations.')


if __name__ == '__main__':
    run()
