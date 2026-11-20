"""Verify exact coordinate factors, squarefree-part bounds and abc-quality intervals."""

import csv
import json
from fractions import Fraction
from functools import cache
from math import gcd, isqrt, prod
from pathlib import Path

from flint import arb, ctx, fmpz, fmpz_mod_poly_ctx


ROOT = Path(__file__).resolve().parent
TRIAL_BOUND = 10_000_000
SCALE = 1_000_000


def add(left,right):
    if left is None:
        return right
    if right is None:
        return left
    x,y = left
    u,v = right
    if x == u:
        if y == -v:
            return None
        slope = (3*x*x-36)/(2*y)
    else:
        slope = (v-y)/(u-x)
    xx = slope*slope-x-u
    return xx,slope*(x-xx)-y


@cache
def point(n):
    if not n:
        return None
    half = point(n//2)
    value = add(half,half)
    if n % 2:
        value = add(value,(Fraction(-3),Fraction(9)))
    return value


def coordinates(n):
    x,y = point(n)
    w = isqrt(x.denominator)
    a = isqrt(-x.numerator//3)
    b = abs(y*w**3/(9*a))
    c = isqrt(2*w*w-a*a)
    d = isqrt((2*w*w+a*a)//3)
    assert x == Fraction(-3*a*a,w*w)
    assert c*c == 2*w*w-a*a and 3*d*d == 2*w*w+a*a and c*d == b
    assert a**4+3*b*b == 4*w**4 and gcd(6*w,a) == 1
    return dict(w=w,a=a,c=c,d=d)


def quality_bound(C,R,round_up):
    bound = SCALE*arb(C).log()/arb(R).log()
    rounded = bound.ceil() if round_up else bound.floor()
    certified = rounded.unique_fmpz()
    assert certified is not None
    return int(certified)


def cofactor_25_bound(v):
    # A proper Gaussian divisor of (25) divides one of (10+5i),(10-5i).
    # Its good-prime support must therefore appear in x(10G)+x(5G).
    x5 = point(5)[0]
    x10 = point(10)[0]
    raw = x5.numerator*x10.denominator+x10.numerator*x5.denominator
    assert v.gcd(raw*x5.denominator*x10.denominator) == 1
    n = int(v)
    block = 170_000
    step = 300
    ring = fmpz_mod_poly_ctx(n)
    c = pow(step,-1,n)
    factors = [ring([c+j,1]) for j in range(1,block+1)]
    while len(factors) > 1:
        products = [factors[i]*factors[i+1] for i in range(0,len(factors)-1,2)]
        if len(factors) % 2:
            products.append(factors[-1])
        factors = products
    arguments = [j*block for j in range(block)]
    residue = 1
    for value in factors[0].multipoint_evaluate(arguments):
        residue = residue*int(value) % n
    assert residue == 5074352375271660377437669864059004213688244855226498489864709439897396372
    assert gcd(residue,n) == 1
    return 1+step*block**2


def verify():
    ctx.prec = 160
    primorial = fmpz.primorial_ui(TRIAL_BOUND)
    cert = json.loads((ROOT/'abc_congruent_six_initial_quality_factors.json').read_text())
    assert list(map(int,cert)) == list(range(1,36,2))
    records = []
    for n_text,chunks in cert.items():
        n = int(n_text)
        coords = coordinates(n)
        assert set(chunks) == set(coords)
        known = {2,3}
        composites = []
        composite_radical_bound = 1
        D_lo = D_hi = 1
        for key,values in chunks.items():
            assert prod(int(z)**e for z,e,_ in values) == coords[key]
            bases = [int(z) for z,_,_ in values]
            assert all(gcd(v,prod(bases[:i])) == 1 for i,v in enumerate(bases))
            for z,e,kind in values:
                v = fmpz(z)
                assert e >= 1 and v > 1
                if kind == 'p':
                    assert v.is_prime()
                    known.add(int(v))
                    if key == 'w' and e % 2:
                        D_lo *= int(v)
                        D_hi *= int(v)
                else:
                    assert kind == 'c' and not v.is_prime()
                    assert not v.is_perfect_power() and v.gcd(primorial) == 1
                    composites.append(int(v))
                    limit = TRIAL_BOUND
                    if n == 25 and key == 'w':
                        limit = cofactor_25_bound(v)
                    composite_radical_bound *= (limit+1)**2
                    if key == 'w' and e % 2:
                        D_lo *= limit+1
                        D_hi *= int(v)
        assert all(gcd(v,prod(known)*prod(composites[:i])) == 1
                   for i,v in enumerate(composites))
        radical_lo = prod(known)*composite_radical_bound
        radical_hi = prod(known)*prod(composites)
        w = coords['w']
        C = 4*w**4
        gate = 'yes' if D_hi**2 <= w else 'no' if D_lo**2 > w else 'open'
        quality = 'above' if radical_hi<C else 'below' if radical_lo>C else 'open'
        records.append(dict(n=n,w=w,D_min=D_lo,D_max=D_hi,gate=gate,
                            unresolved_components=len(composites),
                            radical_min=radical_lo,radical_max=radical_hi,
                            quality_lower_millionths=quality_bound(C,radical_hi,False),
                            quality_upper_millionths=quality_bound(C,radical_lo,True),
                            quality_vs_one=quality))
    return records


if __name__ == '__main__':
    rows = verify()
    with (ROOT/'abc_congruent_six_initial_quality.csv').open('w') as f:
        writer = csv.DictWriter(f,fieldnames=rows[0],lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    for row in rows:
        print(row['n'],row['gate'],row['unresolved_components'],
              row['quality_lower_millionths'],row['quality_upper_millionths'])
