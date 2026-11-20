"""Check the prime-index trace obstruction for prime exponents through 10^9."""

from functools import cache
from math import gcd,isqrt
from abc_congruent_six_perfect_power_trace import add,prime


SMALL_BOUND = 251
EXPONENT_BOUND = 10**9
FINAL = {
    99426071:503, 114643751:1249, 131968489:719, 345399071:769,
    381837431:349, 424674311:457, 487420391:313, 597818471:443,
    632591951:457, 885554569:367,
}


def lucas_trace(t,j,l):
    # a,b are traces at two successive exponents.
    a,b = 2,t
    for bit in bin(j)[2:]:
        odd = (a*b-t)%l
        if bit == '1':
            a,b = odd,(b*b-2)%l
        else:
            a,b = (a*a-2)%l,odd
    return a


@cache
def local_data(l):
    assert prime(l) and l>3
    generator = (-3%l,9%l)
    point = generator
    xs = [None]
    while point is not None:
        xs.append(-point[0]*pow(3,-1,l)%l)
        point = add(point,generator,l)
    rank = len(xs)
    slopes = {xs[n] for n in range(1,rank) if gcd(n,rank)==1}
    squares = {x*x%l for x in range(1,l)}
    torus_order = l-(1 if (-3)%l in squares else -1)
    return torus_order,squares,slopes


def forces_square(l,residue):
    h,squares,slopes = local_data(l)
    j = pow(residue,-1,h)
    return all(lucas_trace(t,j,l) in squares for t in slopes)


def residue_wheel():
    modulus = 24
    allowed = [1]
    for l in (5,7,11,13,23):
        _,squares,_ = local_data(l)
        allowed = [v for r in allowed for v in range(r,r+modulus*l,modulus)
                   if v%l in squares]
        modulus *= l
    return modulus,allowed


def main():
    tests = []
    absolute = []
    for l in range(5,SMALL_BOUND+1):
        if not prime(l):
            continue
        h,squares,_ = local_data(l)
        units = [i for i in range(1,h) if gcd(i,h)==1]
        stable = {i for i in units if forces_square(l,i)}
        tests.append((len(stable)/len(units),l,h,stable,squares))
        if len(stable)==len(units):
            absolute.append(l)
    assert absolute == [5,7,11,13,23,37,47,73]
    tests.sort(reverse=True)

    modulus,allowed = residue_wheel()
    survivors = []
    for block in range(0,EXPONENT_BOUND+modulus,modulus):
        for residue in allowed:
            for p,sign in ((block+residue,1),(block-residue,-1)):
                if p<27431 or p>EXPONENT_BOUND:
                    continue
                if all(p%h not in stable or sign*p%l in squares
                       for _,l,h,stable,squares in tests):
                    if prime(p):
                        survivors.append(p)
    assert sorted(survivors)==sorted(FINAL)
    for p,l in FINAL.items():
        h,squares,_ = local_data(l)
        signed = p if p%4==1 else -p
        assert signed%l not in squares and forces_square(l,p%h)
    print('Universal residue primes:',absolute)
    print('Additional single-prime obstructions:',sorted(FINAL.items()))
    print('Excluded every prime exponent from 5 through',EXPONENT_BOUND)


if __name__=='__main__':
    main()
