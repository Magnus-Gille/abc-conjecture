"""Finite certificate for the dyadic single-packet perfect-power theorem.

Requires PARI via cypari or cypari2. No large packet is factored.
"""
from math import prod

try:
    from cypari import pari
except ImportError:
    from cypari2 import Pari
    pari = Pari()


def double(point, p):
    x, y = point
    slope = (3*x*x + 32*x + 32) * pow(2*y, -1, p) % p
    new_x = (slope*slope - 16 - 2*x) % p
    return new_x, (slope*(x-new_x) - y) % p


def check_trace():
    p, s = 47, 7
    assert (s*s - 2) % p == 0
    r = (-8 % p, 16)
    p0 = double(double(r, p), p)
    p1 = double(p0, p)
    assert (p0, p1) == ((32, 11), (32, 36))
    assert double(p1, p) == p0
    for x, y in [p0, p1]:
        ratios = [8*(x*pow(y, -1, p))**2 % p, 4*pow(x, -1, p) % p]
        assert ratios == [4, 6]
        for ratio, trace in zip(ratios, [-2, 12]):
            for root in [s, -s]:
                a2, a4 = 2*root, 1 + ratio*root
                points = 1 + sum((j*j-i*(i*i+a2*i+a4)) % p == 0
                                 for i in range(p) for j in range(p))
                assert p+1-points == trace
    print('At 47 the normalized traces are -2 for w and 12 for u, at both places.')


def check_newforms():
    expected_counts = [0, 0, 0, 1, 2, 3, 5]
    norm_primes = {2: set(), 12: set()}
    for k, expected_count in zip(range(3, 10), expected_counts):
        level = 2**k
        space = pari.mfinit([level, 2, 8], 0)
        forms = list(pari.mfeigenbasis(space))
        assert len(forms) == expected_count
        degrees = sum(int(pari.mfparams(f)[3].poldegree()) for f in forms)
        assert degrees == int(pari.mfdim(space))
        norms = {2: set(), 12: set()}
        for f in forms:
            trace = pari.mfcoefs(f, 47)[47]
            for t in [-12, -2, 2, 12]:
                difference = trace - t
                norm = abs(int(difference.norm()))
                assert norm
                factors = pari(norm).factor()
                powers = [(int(p), int(e)) for p, e in zip(factors[0], factors[1])]
                assert prod(p**e for p, e in powers) == norm
                assert all(int(pari(p).isprime()) == 1 for p, _ in powers)
                norm_primes[abs(t)].update(p for p, _ in powers)
                norms[abs(t)].add(norm)
        print(f'Level {level}, {len(forms)} orbits, w norms {sorted(norms[2])}, '
              f'u norms {sorted(norms[12])}')
    assert norm_primes == {2: {2, 3, 5, 31}, 12: {2, 3, 5}}


def check_small_exponents(packet, primes):
    for q, p, orbit_size in primes:
        assert int(pari(p).isprime()) == 1 and (p-1) % q == 0
        state = (31 % p, 14 % p, 2273 % p)
        seen = set()
        while state not in seen:
            seen.add(state)
            u, v, w = state
            values = {'w': w, 'u': u, 't': (u*u + 16*v*v) % p}
            value = values[packet]
            if packet == 'u':
                assert pow(-1, (p-1)//q, p) == 1
            assert value != 0 and pow(value, (p-1)//q, p) != 1
            u4, v4 = pow(u, 4, p), pow(v, 4, p)
            state = ((u4 - 32*v4) % p, 2*u*v*w % p,
                     (pow(w, 4, p) - 128*u4*v4) % p)
        assert len(seen) == orbit_size
        print(f'{packet}: q={q}, auxiliary prime {p}, {orbit_size} states')


def check_third_packet():
    p = 47
    for point in [(32, 11), (32, 36)]:
        x, y = point
        ratio = (y*pow(2*x, -1, p))**2 % p
        assert ratio == 24
        for root in [7, -7]:
            a2, a4 = 4*root, root*(ratio + 4 + 2*root)
            points = 1 + sum((j*j-i*(i*i+a2*i+a4)) % p == 0
                             for i in range(p) for j in range(p))
            assert p+1-points == 12
    space = pari.mfinit([1024, 2, 8], 1)
    assert int(pari.mfdim(space)) == 104
    hecke = pari.mfheckemat(space, 47)
    charpoly = hecke.charpoly()
    expected = pari('x^60*(x^2-64)^10*(x^2-128)^4*(x^2-96)^4*'
                    '(x^4-64*x^2+512)^2')
    assert charpoly == expected
    for trace in [-12, 12]:
        assert abs(int(charpoly.subst('x', trace))) == 2**208 * 3**64 * 5**10 * 47**2
    print('t: trace 12 at both places. Full level-1024 characteristic polynomial verified.')
    assert int(pari(17).isprime()) == 1
    check_small_exponents('t', [(2, 3, 3), (3, 7, 2), (5, 71, 7),
                                (47, 419429, 1321)])


if __name__ == '__main__':
    pari.allocatemem(160000000, silent=True)
    assert int(pari(7).isprime()) == int(pari(2273).isprime()) == 1
    check_trace()
    check_newforms()
    check_small_exponents('w', [(2, 3, 3), (3, 7, 2), (5, 31, 4), (23, 47, 22),
                                (31, 6449, 31), (47, 636287, 1936)])
    assert int(pari(31).isprime()) == 1
    check_small_exponents('u', [(2, 17, 3), (3, 7, 2), (5, 71, 7),
                                (47, 473479, 100)])
    check_third_packet()
