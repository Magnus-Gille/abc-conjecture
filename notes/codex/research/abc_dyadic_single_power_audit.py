"""Independent local and full-cusp-space check for the dyadic Q-curve argument."""

try:
    from cypari import pari
except ImportError:
    from cypari2 import Pari
    pari = Pari()


def double(x, y, p):
    slope = (3*x*x + 32*x + 32) * pow(2*y, -1, p) % p
    u = (slope*slope - 16 - 2*x) % p
    return u, (slope*(x-u) - y) % p


def trace(s, coefficient, p):
    squares = {k*k % p for k in range(1, p)}
    total = 0
    for x in range(p):
        value = x*(x*x + 2*s*x + 1 + coefficient*s) % p
        if value:
            total += 1 if value in squares else -1
    return -total


def check():
    p = 47
    point = double(*double(-8, 16, p), p)
    assert point == (32, 11)
    assert double(*point, p) == (32, 36)
    assert double(32, 36, p) == point
    for x, y in [(32, 11), (32, 36)]:
        coefficient = 8 * (x*pow(y, -1, p))**2 % p
        assert coefficient == 4
        for s in (7, 40):
            assert s*s % p == 2
            assert (1+4*s) % p and (1-4*s) % p
            assert trace(s, coefficient, p) == -2

    pari.allocatemem(96_000_000, silent=True)
    pari('M=mfinit([512,2,8],1); H=mfheckemat(M,47)')
    assert int(pari('mfdim(M)')) == 48
    assert bool(pari('charpoly(H)==x^36*(x-8)^4*(x+8)^4*(x^2-128)^2'))
    expected = 2**48*3**4*5**4*31**2
    assert abs(int(pari('matdet(H-2)'))) == expected
    assert abs(int(pari('matdet(H+2)'))) == expected
    print('Full S_2(512,chi_8), dimension 48 and both determinants verified.')


if __name__ == '__main__':
    check()
