"""Certify the level-256 newspace and the small exponents for adjacent w terms."""
try:
    from cypari import pari
except ImportError:
    from cypari2 import Pari
    pari = Pari()


def verify_newforms():
    forms = list(pari.mfeigenbasis(pari.mfinit([256, 2], 0)))
    assert len(forms) == 5
    rational = []
    irrational = []
    for f in forms:
        if int(pari.mfparams(f)[3].poldegree()) == 1:
            rational.append(tuple(map(int, pari.mfcoefs(f, 64))))
        else:
            irrational.append(f)
    expected = []
    for a, b in [(0, 2), (0, -2), (4, 2), (-4, 2)]:
        e = pari.ellinit([0, a, 0, b, 0])
        assert int(pari.ellglobalred(e)[0]) == 256
        expected.append((0, *map(int, pari.ellan(e, 64))))
    assert sorted(rational) == sorted(expected)
    assert len(irrational) == 1
    f = irrational[0]
    assert int(pari.mfparams(f)[3].poldegree()) == 2
    trace = pari.mfcoefs(f, 3)[3]
    assert trace**2 == 8
    assert [int((trace - t).norm()) for t in [-2, 0, 2]] == [-4, -8, -4]
    print('Level 256: four rational CM forms through the Sturm bound 64, '
          'and one quadratic orbit with a_3^2=8.')


def double(point, p):
    if point is None:
        return None
    x, y = point
    if y == 0:
        return None
    m = (3*x*x + 32*x + 32) * pow(2*y, -1, p) % p
    new_x = (m*m - 16 - 2*x) % p
    return new_x, (m*(x-new_x) - y) % p


def check_ratio(q, p, same_rank=False):
    assert int(pari(p).isprime()) and (p-1) % q == 0
    point = (-8 % p, 16 % p)
    for _ in range(2):
        point = double(point, p)
    # Every n >= 8 starts at or after the point 4R on this orbit.
    seen = set()
    while point not in seen:
        seen.add(point)
        assert point is not None
        x, y = point
        assert y % p
        if same_rank:
            assert x % p
            inv_x = pow(x, -1, p)
            residue = (1 + 16*inv_x + 32*inv_x**2) % p
        else:
            r = x * pow(y, -1, p) % p
            residue = (1 - 128 * r**4) % p
        assert residue and pow(residue, (p-1)//q, p) != 1, (q, p, point)
        point = double(point, p)
    return len(seen)


if __name__ == '__main__':
    verify_newforms()
    tests = [(2, 3), (3, 13), (5, 11), (7, 29), (11, 23), (13, 53),
             (17, 103), (19, 571), (23, 47), (29, 59), (31, 311), (37, 149)]
    assert [q for q, _ in tests] == list(map(int, pari.primes([2, 37])))
    for q, p in tests:
        print(f'q={q}, p={p}, doubling points={check_ratio(q, p)}')

    same_rank_tests = [(3, 67), (5, 71), (7, 113), (11, 23), (13, 79), (17, 103),
                       (19, 419), (23, 47), (29, 59), (31, 5209), (37, 223)]
    assert [q for q, _ in same_rank_tests] == list(map(int, pari.primes([3, 37])))
    for q, p in same_rank_tests:
        print(f'Same rank, q={q}, p={p}, doubling points={check_ratio(q, p, True)}')
