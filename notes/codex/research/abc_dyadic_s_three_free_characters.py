"""Whole-orbit congruences for the 3-free part of s_n = u_n^2 + 8v_n^2."""

from math import isqrt


# exponent, auxiliary prime, transient length, cycle length
CASES = [
    (2, 23, 0, 1),
    (3, 109279, 0, 11),
    (5, 1477631, 5, 18),
    (7, 51479, 0, 15),
    (11, 2690689, 3, 5),
    (17, 21319, 0, 20),
    (23, 39508481, 5, 33),
    (31, 1079297, 5, 5),
    (47, 482546369, 1, 200),
]


def check(q, prime, transient, period):
    assert prime != 3 and (prime-1) % q == 0
    assert all(prime % d for d in range(2, isqrt(prime)+1))
    power = (prime-1)//q
    assert pow(3, power, prime) == 1

    # V=v^2 is the scale off infinity; at infinity the scale is U=u^2.
    U, V = 961 % prime, 196 % prime
    x = U*pow(V, -1, prime) % prime if V else None
    h = pow(V or U, power, prime)
    seen = {}
    while (x,h) not in seen:
        seen[x,h] = len(seen)
        if x is None:
            assert h not in (0,1)
            h = pow(h, 4, prime)
            continue
        observed = h*pow((x+8) % prime, power, prime) % prime
        assert observed not in (0,1)
        numerator = (x*x-32)**2 % prime
        denominator = 4*x*(x*x+16*x+32) % prime
        h = pow(h,4,prime)*pow(denominator or numerator, power, prime) % prime
        x = numerator*pow(denominator,-1,prime) % prime if denominator else None
    assert seen[x,h] == transient
    assert len(seen)-transient == period


if __name__ == '__main__':
    for case in CASES:
        check(*case)
        print(*case)
