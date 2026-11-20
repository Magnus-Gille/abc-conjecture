"""Arithmetic checks for the all-index total squarefree-kernel censuses."""

import json
import subprocess
import sys
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import gcd,isqrt,prod
from pathlib import Path

from abc_full_quartic_largest_prime_census import (
    denominator, first_contradiction, prime_list, source_characters,
)


BOUND = 80_217_359


def add(P,Q,p=None):
    if P is None:
        return Q
    if Q is None:
        return P
    x,y = P
    u,v = Q
    if x==u and (y==-v if p is None else (y+v)%p==0):
        return None
    numerator,divisor = (3*x*x-36,2*y) if x==u else (v-y,u-x)
    if p is None:
        slope = numerator/divisor
        xx = slope*slope-x-u
        return xx,slope*(x-xx)-y
    slope = numerator*pow(divisor,-1,p)%p
    xx = (slope*slope-x-u)%p
    return xx,(slope*(x-xx)-y)%p


def multiple(n,P):
    Q = None
    while n:
        if n%2:
            Q = add(Q,P)
        n //= 2
        if n:
            P = add(P,P)
    return Q


def mod(q,p):
    return q.numerator*pow(q.denominator,-1,p)%p


def order(P,p):
    P = tuple(x%p for x in P)
    Q = P
    n = 1
    while Q is not None:
        n += 1
        Q = add(Q,P,p)
    return n


def check_small_arithmetic():
    tables = json.loads(Path(__file__).with_name('abc_congruent_six_initial_quality_factors.json').read_text())
    coords = {'w':(-3,9),'a':(12,36),'c':(18,-72),'d':(-2,-8)}
    totals = {}
    largest = {}
    for n in (1,3,5,7,9):
        bases = []
        for key,P in coords.items():
            x,_ = multiple(n,tuple(map(Fraction,P)))
            den = isqrt(x.denominator)
            factors = tables[str(n)][key]
            assert den**2 == x.denominator
            assert prod(int(p)**e for p,e,_ in factors) == den
            for text,e,kind in factors:
                p = int(text)
                assert kind=='p' and all(p%j for j in range(2,isqrt(p)+1))
                if e%2:
                    bases.append(p)
        assert len(bases)==len(set(bases))
        totals[n] = prod(bases)
        largest[n] = max(bases,default=1)
    assert [totals[n] for n in (1,3,5)] == [1,1319901,2216541307731009701]
    assert largest == {1:1,3:47,5:3121,7:2802064609,9:80217359}
    for p,orders in {23:(3,6),47:(6,3),73:(5,10),97:(10,5),239:(10,5),719:(5,10)}.items():
        assert tuple(order(coords[k],p) for k in ('a','c'))==orders
    x,_ = multiple(25,tuple(map(Fraction,coords['a'])))
    assert x.denominator % 2017**2 == 0 and x.denominator % 2017**3
    G = tuple(map(Fraction,coords['w']))
    S = tuple(map(Fraction,coords['d']))
    assert [mod(multiple(n,G)[1],8) for n in (1,3,5,7)] == [1,3,5,7]
    x,y = multiple(8,G)
    assert mod(-x/y,8)==0
    x,y = multiple(3,S)
    assert -x/y == Fraction(1551,3404)
    print('Total kernels through index 9:',totals)
    print('Largest prime factors through index 9:',largest)


def smooth_scan(scanner):
    text = subprocess.check_output([scanner,str(BOUND)],text=True)
    candidates = defaultdict(list)
    for line in text.splitlines():
        q,p = map(int,line.split())
        candidates[q].append(p)
    assert len(text.splitlines())==91558 and len(candidates)==86731
    tests = [(l,source_characters(l)) for l in prime_list(71) if l>3]
    winners = []
    count = 0
    for q,ps in candidates.items():
        for size in range(1,len(ps)+1):
            for subset in combinations(ps,size):
                count += 1
                if first_contradiction(q,prod(subset),tests) is None:
                    winners.append((q,tuple(sorted(subset))))
    assert count==97977 and sorted(winners)==[(3,(37,)),(5,(13,3121)),(7,(14281,140449))]
    print('Prime-index denominator candidates:',sorted(winners))
    sieve = bytearray(b'\x01')*(BOUND+1)
    sieve[:2] = bytes(2)
    for p in range(2,isqrt(BOUND)+1):
        if sieve[p]:
            sieve[p*p::p] = bytes((BOUND-p*p)//p+1)
    residuals = {n:denominator(n) for n in (15,21,25,27,35,49)}
    for p in range(13,BOUND+1,12):
        if sieve[p]:
            for n,value in residuals.items():
                while value%p==0:
                    value //= p
                residuals[n] = value
    assert all(isqrt(v)**2!=v for v in residuals.values())
    print('Composite-divisor residual bit lengths:',{n:v.bit_length() for n,v in residuals.items()})


if __name__=='__main__':
    check_small_arithmetic()
    if len(sys.argv)==2:
        smooth_scan(sys.argv[1])
