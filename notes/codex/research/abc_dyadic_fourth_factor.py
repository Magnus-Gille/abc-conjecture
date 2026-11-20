"""Verify the finite calculations for s_n = u_n² + 8v_n²."""
from math import isqrt

try:
    from cypari import pari
except ImportError:
    from cypari2 import Pari
    pari = Pari()


def inert_trace(p):
    # In F_{p²} = F_p[t]/(t²+2), the quadratic character of an
    # element is the quadratic character of its norm in F_p.
    assert pow((-2) % p, (p - 1) // 2, p) == p - 1
    squares = {x*x % p for x in range(1, p)}
    total = 0
    for x in range(p):
        for y in range(p):
            # Evaluate X*(X²+4X+2+8t) at X=x+y*t.
            real = x*x - 2*y*y + 4*x + 2
            imag = 2*x*y + 4*y + 8
            product_real = x*real - 2*y*imag
            product_imag = x*imag + y*real
            norm = (product_real**2 + 2*product_imag**2) % p
            if norm:
                total += 1 if norm in squares else -1
    return -total


def period(q, p):
    assert p > 2 and all(p % d for d in range(2, isqrt(p) + 1))
    assert (p-1) % q == 0
    state = (31 % p, 14 % p, 2273 % p)
    seen = set()
    while state not in seen:
        seen.add(state)
        u, v, w = state
        value = (u*u + 8*v*v) % p
        assert value and pow(value, (p-1)//q, p) != 1
        state = ((u**4 - 32*v**4) % p, 2*u*v*w % p,
                 (w**4 - 128*(u*v)**4) % p)
    return len(seen)


if __name__ == "__main__":
    assert inert_trace(47) == 4
    pari.allocatemem(100_000_000, silent=True)
    space = pari.mfinit([1024, 2], 1)
    assert int(pari.mfdim(space)) == 105
    characteristic = pari.charpoly(pari.mfheckemat(space, 47))
    value = int(pari.polresultant(characteristic, pari("x^2-98")))
    assert abs(value) == 2**105 * 3**8 * 5**8 * 7**114 * 17**24 * 31**8
    tests = [(2, 23, 11), (3, 7, 2), (5, 31, 4), (7, 113, 3),
             (17, 2687, 41), (31, 311, 61), (47, 473479, 100)]
    for q, p, expected in tests:
        assert period(q, p) == expected
    print("Trace 4, full Hecke resultant, and seven all-index power tests verified.")
