"""Check every possible squarefree kernel through the attained value at index three."""
import csv
import itertools
import json
from collections import defaultdict
from functools import lru_cache
from math import gcd, isqrt, prod
from pathlib import Path

from sympy import factorint, primerange

from abc_eisenstein_slice_tunnell import real_and_legendre

HERE = Path(__file__).resolve().parent
LIMIT = 2591 * 1031


def add(P,Q,p):
    if P is None:
        return Q
    if Q is None:
        return P
    x,y=P
    u,v=Q
    if x==u:
        if (y+v)%p==0:
            return None
        slope=(3*x*x-576)*pow((2*y)%p,-1,p)%p
    else:
        slope=(v-y)*pow((u-x)%p,-1,p)%p
    t=(slope*slope-x-u)%p
    return t,(slope*(x-t)-y)%p


def odd_visits(p):
    Q=(-8%p,-64%p)
    step=add(Q,Q,p)
    P=Q
    hits=[]
    h=1
    while True:
        if P is not None:
            u=P[0]
            if (u*u+336*u+576)%p==0:
                hits.append(h)
        P=add(P,step,p)
        h+=2
        if P==Q:
            return (h-1,hits)


@lru_cache(maxsize=None)
def pair_count(m, coeff):
    """Binary norm count on odd m for Q(sqrt(-2)) and Q(i), respectively."""
    result=2
    for p,e in factorint(m).items():
        split = (p%8 in (1,3)) if coeff==2 else p%4==1
        if split:
            result*=e+1
        elif e%2:
            return 0
    return result


@lru_cache(maxsize=None)
def delta(d, coeff):
    m=3*d
    value=-pair_count(m,coeff)
    for z in range(1,isqrt(m//8)+1):
        value+=(2 if z%2 else -2)*pair_count(m-8*z*z,coeff)
    return value


def quartics(x,y):
    f=x**4-18*x*x*y*y+9*y**4
    h=12*x*y*(x*x-3*y*y)
    return f,f+h,f-h


@lru_cache(maxsize=None)
def local_cover(p, k_residue, l_residue):
    squares={t*t%p for t in range(p)}
    A={-8*t%p for t in squares}
    B={16*k_residue*t%p for t in squares}
    C={32*l_residue*t%p for t in squares}
    for x,y in [(1,0)]+[(x,1) for x in range(p)]:
        a,b,c=quartics(x,y)
        if a%p in A and b%p in B and c%p in C:
            return True
    return False


def first_local_failure(d4,d5):
    k=d4 if d4%3==1 else -d4
    l=-d5 if d5%3==1 else d5
    return next((p for p in primerange(5,54) if not local_cover(p,k%p,l%p)),0)


def main():
    start = next(p for p in primerange(5,1000) if odd_visits(p)[1])
    maxp=LIMIT//start
    visits={p:(period,hits) for p in primerange(5,maxp+1)
            for period,hits in [odd_visits(p)] if hits}
    archive=defaultdict(list)
    archive_path=HERE/'abc_eisenstein_slice_paired_quartic_1m.csv'
    with archive_path.open() as handle:
        for row in csv.DictReader(handle):
            p=int(row['p'])
            if p<=maxp:
                archive[p].append((int(row['odd_period']),int(row['h'])))
    assert {p:[(t,h) for h in hs] for p,(t,hs) in visits.items()} == dict(archive)
    primes=sorted(visits)
    assert prod(primes[:3])>LIMIT
    rows=[]
    for p,q in itertools.combinations(primes,2):
        b=p*q
        if b>LIMIT:
            continue
        T,hs=visits[p]
        U,ks=visits[q]
        crt=any((h-k)%gcd(T,U)==0 for h,k in itertools.product(hs,ks))
        for d4,d5 in ((p,q),(q,p)):
            real,symbols=real_and_legendre(d4,d5,[p,q])
            rows.append(dict(b=b,d4=d4,d5=d5,crt=int(crt),real=int(real),symbols=int(symbols),
                             first_local_failure=first_local_failure(d4,d5),
                             delta_3b=delta(b,2),delta_6d4=delta(d4,4),delta_3d5=delta(d5,2)))
    rows.sort(key=lambda r:(r['b'],r['d4']))
    with (HERE/'abc_eisenstein_slice_minimum_kernel.tsv').open('w') as output:
        writer=csv.DictWriter(output,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    def counts(pred):
        selected=[r for r in rows if pred(r)]
        return dict(orientations=len(selected),kernels=len({r['b'] for r in selected}))
    def three(r):
        return r['delta_3b']==r['delta_6d4']==r['delta_3d5']==0
    def full(r):
        return three(r) and r['symbols'] and r['crt']
    out=dict(limit=LIMIT,prime_bound=maxp,all_primes_scanned=len(list(primerange(5,maxp+1))),
             visiting_primes=len(primes),three_smallest=primes[:3],
             visited=counts(lambda r:True),visited_crt=counts(lambda r:r['crt']),
             visited_3tun=counts(three),visited_3tun_real_symbols=counts(lambda r:three(r) and r['symbols']),
             full=counts(full),full_orientations=[r for r in rows if full(r)])
    out["local_counts_only"]={str(p):counts(lambda r:r['first_local_failure']==0 or r['first_local_failure']>p)
                              for p in primerange(5,54)}
    out["local_only_survivors"]=[r for r in rows if not r['first_local_failure']]
    f,fp,fm=quartics(11,3)
    assert (f,fp,fm)==(-8*23**2,32*1031,-16*2591)
    assert [(r["d4"],r["d5"]) for r in out["local_only_survivors"]]==[(2591,1031)]
    (HERE/'abc_eisenstein_slice_minimum_kernel.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))


if __name__=='__main__':
    main()
