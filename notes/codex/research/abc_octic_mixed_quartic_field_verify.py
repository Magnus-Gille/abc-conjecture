"""Verify the dyadic full-2-descent exclusions in the quartic field."""

from itertools import product


def reduce_coefficients(values):
    values = list(values) + [0] * 4
    for j in range(len(values) - 1, 3, -1):
        values[j - 4] += values[j]
        values[j - 2] += 2 * values[j]
    return tuple(c % 8 for c in values[:4])


def subtract(a, b):
    return reduce_coefficients(x - y for x, y in zip(a, b))


def multiply(a, b):
    coefficients = [0] * 7
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            coefficients[i + j] += x * y
    return reduce_coefficients(coefficients)


def is_unit(a):
    # The residue field is F_2 and t reduces to 1.
    return sum(a) % 2 == 1


def reduction(q, t):
    """The two points, two-torsion, and affine addition at a degree-one place."""
    assert (t**4 - 2 * t**2 - 1) % q == 0
    a = (1 + pow(t, -1, q)) % q
    b = a * t**2 % q
    squares = {i * i % q for i in range(1, q)}

    def cubic(x):
        return x * (x - a) * (x - b) % q

    order = q + 1 + sum(0 if value == 0 else (1 if value in squares else -1) for value in map(cubic, range(q)))
    p_inf = ((1 + t)**2 * pow(4, -1, q) % q, (-3*t**3 - t**2 + 7*t + 1) * pow(8, -1, q) % q)
    half_seed = ((t**2 - 1) % q, (t**3 - 3*t) % q)
    seed = ((2*t**3 + 5*t**2 + 2*t + 2) * pow(4, -1, q) % q,
            (-5*t**3 - 11*t**2 - 8*t - 5) * pow(8, -1, q) % q)

    def add(p, r):
        if p is None:
            return r
        if r is None:
            return p
        x, y = p
        u, v = r
        if x == u and (y + v) % q == 0:
            return None
        if x == u:
            slope = (3*x*x - 2*(a+b)*x + a*b) * pow(2*y, -1, q) % q
        else:
            slope = (v-y) * pow(u-x, -1, q) % q
        xx = (slope*slope + a+b-x-u) % q
        return xx, (slope*(x-xx) - y) % q

    def times(n, point):
        total = None
        while n:
            if n & 1:
                total = add(total, point)
            point = add(point, point)
            n //= 2
        return total

    assert all(y*y % q == cubic(x) for x, y in (p_inf, half_seed, seed))
    assert add(half_seed, half_seed) == seed
    return a, b, order, p_inf, half_seed, seed, times


def check_saturation():
    assert reduction(7, 2)[2] == 8 and reduction(41, 5)[2] == 36
    expected = [[0,1,0,1], [1,1,0,0], [0,1,0,0], [1,1,1,0]]
    rows = []
    for t in (2, 5):
        a, b, _, p_inf, half_seed, _, _ = reduction(7, t)
        roots = (0, a, b)
        for e in roots[:2]:
            row = []
            for x, _ in [p_inf, half_seed, (0, 0), (a, 0)]:
                val = x - e
                if not val:
                    f, g = [r for r in roots if r != e]
                    val = (e-f)*(e-g)
                row.append(int(pow(val % 7, 3, 7) == 6))
            rows.append(row)
    assert rows == expected
    assert all(any(sum(x*y for x,y in zip(v,row)) % 2 for row in rows)
               for v in product(range(2), repeat=4) if any(v))
    # Each row is (q,t,c) for [order/l]Q=c[order/l]P, where Q=2H.
    # c=None denotes zero for the projection of P, nonzero for that of Q.
    certificates = {
        3: [(41, 5, 1), (41, 36, None)],
        5: [(31, 3, None), (31, 28, 2)],
        7: [(47, 14, 4), (47, 33, 5)],
        11: [(313, 302, 0), (599, 261, 6)],
        13: [(41, 10, 5), (257, 224, 12)],
        17: [(127, 12, 3), (127, 115, 7)],
        19: [(313, 173, 11), (577, 261, 1)],
        23: [(199, 141, 16), (569, 246, 19)],
        29: [(113, 17, 18), (113, 96, 19)],
        31: [(271, 110, 4), (271, 161, 23)],
    }
    for l, pair in certificates.items():
        assert pair[0][2] != pair[1][2]
        for q, t, c in pair:
            _, _, n, p_inf, _, seed, times = reduction(q, t)
            assert q != l and n % l == 0
            u, v = times(n//l, p_inf), times(n//l, seed)
            if c is None:
                assert u is None and v is not None and times(l, v) is None
            else:
                assert u is not None and times(l, u) is None and times(c, u) == v
    print("Two independent projections checked for every odd prime from 3 through 31; 2-saturation also checked.")


if __name__ == "__main__":
    one = (1, 0, 0, 0)
    t = (0, 1, 0, 0)
    h = (7, 1, 1, 0)  # t^2+t-1
    a = (1, 6, 0, 1)  # 1+1/t = 1-2t+t^3
    b = multiply(a, multiply(t, t))
    squares = {multiply(v, v) for v in product(range(8), repeat=4)}
    squares_of_nonunits = {v for v in squares if not is_unit(v)}
    assert len(squares) == 96 and len(squares_of_nonunits) == 32
    print(f"Squares modulo 8: {len(squares)}, from nonunits: {len(squares_of_nonunits)}")
    for name, d in [("t", t), ("h", h), ("t*h", multiply(t, h))]:
        d_squares = {multiply(d, v) for v in squares}
        # If z0 is a unit, scale z0=1 and enumerate z1^2.
        first_chart = sum(subtract(v, a) in d_squares and subtract(v, b) in d_squares for v in squares)
        # If z0 is a nonunit, z1 must be a unit by primitivity. Scale z1=1.
        second_chart = sum(
            subtract(one, multiply(a, v)) in d_squares and subtract(one, multiply(b, v)) in d_squares
            for v in squares_of_nonunits
        )
        assert first_chart == second_chart == 0
        print(f"d={name}: {first_chart} possibilities with z0 a unit, {second_chart} otherwise")
    check_saturation()
