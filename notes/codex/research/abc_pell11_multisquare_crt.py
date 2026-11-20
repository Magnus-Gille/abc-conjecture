"""Compute primitive square-support periods and extend a single Pell CRT branch."""
from argparse import ArgumentParser
from collections import defaultdict
from math import gcd, lcm, prod

from abc_cm_pell_whole_triple import pell
from abc_pell11_early_squares import full_form
from abc_pell11_square_periods import factor_at

def primitive(modulus, residues):
    # The order of a translational stabilizer divides both modulus and support size.
    common=gcd(modulus,len(residues))
    pool=set(residues)
    for order in range(common,0,-1):
        if common%order: continue
        step=modulus//order
        if all((a+step)%modulus in pool for a in pool):
            return step,sorted({a%step for a in pool})
    raise AssertionError

def merge(first,second):
    m,ra=first
    n,rb=second
    d=gcd(m,n)
    inv=pow(m//d,-1,n//d)
    by=defaultdict(list)
    for b in rb: by[b%d].append(b)
    return m*(n//d),[a+m*(((b-a)//d*inv)%(n//d)) for a in ra for b in by[a%d]]

def at(index,p,coeff,content):
    q=p**3
    b,a=pell(index,q)
    s=(b*b+2*a*a)%q
    value=factor_at(index,coeff,q)
    absolute=-value*pow(s,50,q)*pow(content,-1,q)%q
    assert value%(p*p)==absolute%(p*p)==0
    return value//(p*p),absolute//(p*p)

def report(rows,abscissa_periods,primes,coeff,content):
    combined=(1,[0])
    for p in primes:
        print('local',p,rows[p][0],len(rows[p][1]))
        combined=merge(combined,rows[p])
    period,reps=primitive(*combined)
    first=min(x or period for x in reps)
    print('square support',period,len(reps),'first three',sorted(x or period for x in reps)[:3])
    if all(period%abscissa_periods[p]==0 and (period//abscissa_periods[p])%p for p in primes):
        print('exact support period',period*prod(primes))
    print('first',[(p,at(first,p,coeff,content)) for p in primes])
    return first,period

def extend(index,period,marked,rows,coeff,content):
    # Every p in marked already divides F_index to exact exponent 2.
    best=None
    for p,local in rows.items():
        if p in marked: continue
        modulus,candidates=merge((period,[index%period]),local)
        for n in candidates:
            if not n: n=modulus
            if best and n>=best[0]: continue
            # Choose a witness among least representatives of square-support classes.
            if all(at(n,q,coeff,content)[0] for q in [*marked,p]):
                best=n,modulus,p
    return best

if __name__=='__main__':
    parser=ArgumentParser(description=__doc__)
    parser.add_argument('classes')
    parser.add_argument('--primes',type=int,nargs='+',default=[683,1409,2707])
    parser.add_argument('--extend',type=int,default=0)
    args=parser.parse_args()
    rows={}
    abscissa_periods={}
    with open(args.classes) as f:
        for line in f:
            p,m,*R=map(int,line.split())
            rows[p]=primitive(p*m,R)
            abscissa_periods[p]=p*m//gcd(m,2)
    coeff,content=full_form()
    coeff=list(map(int,coeff))
    marked=args.primes.copy()
    index,period=report(rows,abscissa_periods,marked,coeff,int(content))
    for _ in range(args.extend):
        index,period,new=extend(index,period,marked,rows,coeff,int(content))
        marked.append(new)
        print('extended',index,'step',period,'primes',marked,'residues',
              [at(index,p,coeff,int(content))[1] for p in marked],flush=True)
