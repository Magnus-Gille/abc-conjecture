"""Finite Mordell-Weil sieve for w^4=m^4+4m^3n+10m²n²−4mn³+n^4."""
from math import isqrt
import sys


def allowed(p):
    """Residues of k mod ord_p(G) giving a square in either torsion coset."""
    squares = {y*y % p for y in range(p)}

    def add(left,right):
        if left is None:
            return right
        if right is None:
            return left
        x,y = left
        u,v = right
        if x == u:
            if (y+v) % p == 0:
                return None
            slope = (3*x*x+32*x+32)*pow(2*y,-1,p) % p
        else:
            slope = (v-y)*pow(u-x,-1,p) % p
        new_x = (slope*slope-16-x-u) % p
        return new_x,(slope*(x-new_x)-y) % p

    def lifts(point):
        if point is None:
            return True  # y/x² -> 1 at this infinity
        u,v = point
        if (u+8) % p == 0:
            # The quartic y²=g(x) has x=-1/2, y=-9/4 at v=-16,
            # and y/x² -> -1 at the other point with u=-8.
            return ((-9 if (v+16) % p == 0 else -1) % p) in squares
        x = (v-2*u)*pow(2*(u+8),-1,p) % p
        y = ((u+8)*pow(2,-1,p)-x*x-2*x-3) % p
        return y in squares

    generator, torsion = (-4 % p,8 % p),(0,0)
    point = None
    residues = [[],[]]
    while True:
        residues[0].append(lifts(point))
        residues[1].append(lifts(add(point,torsion)))
        point = add(point,generator)
        if point is None:
            return residues


def main():
    bound = int(sys.argv[1]) if len(sys.argv)>1 else 10**6
    primes = [p for p in range(3,201,2) if all(p%d for d in range(2,isqrt(p)+1))]
    tables = [allowed(p) for p in primes]
    for e in (0,1):
        indices = range(-bound,bound+1)
        for p,data in zip(primes,tables):
            row = data[e]
            indices = [k for k in indices if row[k % len(row)]]
            if indices == [-2,0]:
                break
        print(f'torsion coset {e}, last test prime {p}, surviving indices {indices}')
        if bound == 10**6:
            assert indices == [-2,0]


if __name__ == '__main__':
    main()
