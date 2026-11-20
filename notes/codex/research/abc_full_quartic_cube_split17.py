"""Split-prime certificate for the cube-denominator quartic. Standard Python."""
from itertools import product

from abc_congruent_six_smooth_odd_support import add, multiple


def main():
    p = 17
    lifted = {t % p: t for t in range(p*p) if (t**3-3*t-1) % (p*p) == 0}
    roots = sorted(lifted)
    assert roots == [3, 4, 10]
    squares = {v*v % p: v for v in range(p)}
    local = []
    directions = []
    for theta in roots:
        th = lifted[theta]
        modulus = p*p
        k = -3*pow(2*th+1, -1, modulus) % modulus
        a4 = -36*th*th
        d = (12, -12*th*k % modulus)
        reduced = tuple(v % p for v in d)
        points = [None]
        point = reduced
        while point is not None:
            points.append(point)
            point = add(point, reduced, 0, a4, p)
        torsion = [None, (0, 0), (6*th % p, 0), (-6*th % p, 0)]
        order = len(points)
        assert order % 2 == 0 and 20 % order == 0
        size = 1 + sum(1 for x, y in product(range(p), repeat=2) if (y*y-x**3-a4*x) % p == 0)
        # Half the reduction order takes D to a nonzero point of order two.
        # There dy/(3x²+a4) is the integral invariant differential.
        x, y = multiple(order//2, d, 0, a4, modulus)
        assert y % p == 0
        tangent = 2*y*pow(3*x*x+a4, -1, modulus) % modulus
        direction = -theta*(20//order)*(tangent//p) % p
        directions.append(direction)
        print('root, lift, group order, order of D, normalized slope:', theta, th, size, order, direction)
        images = {0: {None, reduced}, None: {torsion[1], add(reduced, torsion[1], 0, a4, p)}}
        for u in range(1, p):
            f = (1+4*k*u-18*u**2-12*k*u**3+9*u**4) % p
            images[u] = set()
            if f not in squares:
                continue
            for w in {squares[f], -squares[f] % p}:
                xx = ((2*(w+1)+4*k*u) * pow(u*u, -1, p)) % p
                yy = (((xx*xx-36)*u-4*k*xx+24*k) * pow(2, -1, p)) % p
                X = (xx-6)*th*th*pow(4, -1, p) % p
                Y = yy*th**3*pow(8, -1, p) % p
                assert (Y**2-X**3-a4*X) % p == 0
                images[u].add((X, Y))
        local.append((a4, points, torsion, images))

    possible = {u: set() for u in [*range(p), None]}
    for j, torsion_index in product(range(20), range(4)):
        triple = tuple(add(points[j % len(points)], torsion[torsion_index], 0, a4, p)
                       for a4, points, torsion, _ in local)
        for u in possible:
            if all(triple[i] in entry[3][u] for i, entry in enumerate(local)):
                possible[u].add(triple)
    O = (None,)*3
    D = tuple(entry[1][1] for entry in local)
    T = ((0, 0),)*3
    DT = tuple(add(point, (0, 0), 0, entry[0], p) for point, entry in zip(D, local))
    assert {u: cells for u, cells in possible.items() if cells} == {0: {O, D}, None: {T, DT}}
    assert directions == [11, 13, 7]
    print('Only the two known points at slope zero and the two at infinity survive.')


if __name__ == '__main__':
    main()
