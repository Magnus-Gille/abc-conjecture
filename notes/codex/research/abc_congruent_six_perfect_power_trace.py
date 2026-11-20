"""Finite residue and group checks in the Eisenstein trace descent."""

from math import gcd,isqrt,prod


def prime(n):
    return n >= 2 and all(n%d for d in range(2,isqrt(n)+1))


def add(P,Q,p):
    if P is None:
        return Q
    if Q is None:
        return P
    x,y = P
    u,v = Q
    if x == u:
        if (y+v)%p == 0:
            return None
        slope = (3*x*x-36)*pow(2*y,-1,p)
    else:
        slope = (v-y)*pow(u-x,-1,p)
    xx = (slope*slope-x-u)%p
    return xx,(slope*(x-xx)-y)%p


def check_order(p,d):
    T = (12%p,36%p)
    P = T
    for _ in range(1,d):
        assert P is not None
        P = add(P,T,p)
    assert P is None


def main():
    check_order(23,3)
    check_order(47,6)
    ls = (5,7,11,13,23,47)
    orders = [l-(1 if pow(-3,(l-1)//2,l)==1 else -1) for l in ls]
    assert orders == [6,6,12,12,24,48]

    def survives(p):
        if p%24 not in (1,23):
            return False
        signed = p if p%4==1 else -p
        return all(pow(signed,(l-1)//2,l)==1 for l in ls)

    first = next(p for p in range(5,100000) if prime(p) and survives(p))
    assert first == 27431
    # CRT factors, avoiding enumeration of all 129,849,720 residues.
    numerator = 2*prod((l-1)//2 for l in ls)
    denominator = 8*prod(l-1 for l in ls)
    divisor = gcd(numerator,denominator)
    assert (numerator//divisor,denominator//divisor) == (1,256)
    print('Torus orders:',orders)
    print('First permitted prime:',first)
    print('Relative density of permitted classes: 1/256')


if __name__ == '__main__':
    main()
