"""Exact mixed-orbit slopes and least valuation-two primes for the inert indices.

Run without options for the arithmetic certificates. Pass --slopes to emit CSV
with the complete reduced numerators and denominators. Add --extended for index 53.
"""
import csv
from fractions import Fraction
from math import isqrt
import sys

EXAMPLES = {5: 131, 7: 617, 13: 2939, 23: 57593, 31: 11657}


def add(left, right, prime=None):
    """Affine addition on v²=u³−8u²+8u over Q or F_p."""
    if left is None:
        return right
    if right is None:
        return left
    x,y = left
    u,v = right
    if x == u:
        if (y == -v if prime is None else (y+v) % prime == 0):
            return None
        num, den = 3*x*x-16*x+8, 2*y
    else:
        num, den = v-y, u-x
    if prime is None:
        slope = Fraction(num, den)
    else:
        slope = num*pow(den, -1, prime) % prime
    z = slope*slope+8-x-u
    w = slope*(x-z)-y
    return (z,w) if prime is None else (z % prime,w % prime)


def multiple(k, prime=None):
    result, point = None, (1,1)
    while k:
        if k & 1:
            result = add(result,point,prime)
        k //= 2
        if k:
            point = add(point,point,prime)
    return result


def roots(m):
    u,v = multiple((3*m+1)//2)
    s,t = ((v+u)/(2*(u-1))).as_integer_ratio()
    root_y = isqrt(s*s+2*t*t)
    root_u = isqrt((s-t)**2+t*t)
    assert root_y**2 == s*s+2*t*t
    assert root_u**2 == (s-t)**2+t*t
    return s,t,root_y,root_u


def primes_through(n):
    sieve = bytearray(b'\x01')*(n+1)
    for p in range(2,n+1):
        if sieve[p]:
            yield p
            for j in range(p*p,n+1,p):
                sieve[j] = 0


def exponent(value,p):
    count = 0
    while value % p == 0:
        value //= p
        count += 1
    return count


def point_count(p):
    squares = bytearray(p)
    for y in range((p+1)//2):
        squares[y*y % p] = 1
    total = 1
    for x in range(p):
        rhs = (x**3-8*x*x+8*x) % p
        total += 1 if rhs == 0 else 2*squares[rhs]
    return total


def main():
    slopes = '--slopes' in sys.argv[1:]
    table = csv.writer(sys.stdout, lineterminator='\n')
    table.writerow(('index','s','t') if slopes else
                   ('index','sign','digits_s','digits_t','v2_t','least_bad_Y',
                    'v_p_Y','ord_p_T','ord_p_A','curve_order','least_bad_Uminus'))
    examples = dict(EXAMPLES)
    if '--extended' in sys.argv[1:]:
        examples[53] = 9623953
    for m, expected in examples.items():
        s,t,y,u = roots(m)
        assert s % 2 and exponent(t,2) == max(exponent(3*m-1,2),exponent(3*m+1,2))
        assert 2*exponent(y,3) == 4 and 2*exponent(u,5) == 2+2*exponent(m,5)
        p = next(p for p in primes_through(expected) if exponent(y,p) == 1)
        assert p == expected
        bad_u = next(p for p in primes_through(29) if exponent(u,p) == 1)
        # Since m is prime, exact order m for T=3A follows from these two tests.
        assert multiple(3,p) is not None and multiple(3*m,p) is None
        ord_a = m if multiple(m,p) is None else 3*m
        count = point_count(p)
        assert count % (m*m) == 0 and (p-1) % m == 0
        if slopes:
            table.writerow((m,s,t))
        else:
            table.writerow((m,'+' if s>0 else '-',len(str(abs(s))),len(str(t)),
                            exponent(t,2),p,2,m,ord_a,count,bad_u))


if __name__ == '__main__':
    main()
