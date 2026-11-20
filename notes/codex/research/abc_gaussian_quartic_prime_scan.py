"""Exhaustive fourth-power cutoff for inert prime indices on y²=x³−36x."""
import argparse,csv,json
from functools import cache
from math import isqrt,prod
from pathlib import Path
from flint import fmpq,fmpz
from abc_gaussian_order_witness import add,division_value,modular_point
from abc_gaussian_scalar_prime_scan import check_abscissa,prime_flags

@cache
def term(n):
    # On y²=x³−4x at T=(-1,sqrt(3)), even psi_n is divided by 2*y.
    if n<5:return fmpz((0,1,1,-37,-70)[n])
    m=n//2
    if n%2:
        A=term(m+2)*term(m)**3
        B=term(m-1)*term(m+1)**3
        return A-144*B if m%2 else 144*A-B
    return term(m)*(term(m+2)*term(m-1)**2-term(m-2)*term(m+1)**2)

@cache
def rational_multiple(n):
    if not n:return None
    h=rational_multiple(n//2)
    P=add(h,h)
    return add(P,(fmpq(-3),fmpq(9))) if n%2 else P

def denominator(r):
    assert r%2==1
    B=abs(term(r))
    # x(rG) = -3 - 36*f_(r-1)*f_(r+1)/f_r² since x(G)=3*x(T).
    assert B.gcd(36*term(r-1)*term(r+1))==1 and B.gcd(6)==1
    return B

def norm_primes(r):
    # Full primary conditions are 4|a and 2|b. For r=3 also test all raw
    # representations so that the finite small rank rests on no shape shortcut.
    da,db=(1,1) if r==3 else (4,2)
    cap=r**4
    primes={}
    candidates=0
    for b in range(db,r+1,db):
        m=isqrt(cap-(r*b)**2)
        bottom=-((m+1)//r)
        for a in range(bottom+(-bottom)%da,(m-1)//r+1,da):
            p=(1+r*a)**2+(r*b)**2
            if p%12!=1:continue
            candidates+=1
            if fmpz(p).is_prime():primes[p]=(a,b)
    return candidates,primes

def prime_product(values):
    # A balanced product allows one gcd with the exact denominator.
    terms=[fmpz(p) for p in values]
    if not terms:return fmpz(1)
    while len(terms)>1:
        terms=[x*y for x,y in zip(terms[::2],terms[1::2])]+(terms[-1:] if len(terms)%2 else [])
    return terms[0]

def scan(limit,path):
    flags=prime_flags(limit)
    summaries=[];all_hits=[];squares=[];smooth=[];mass_exceptions=[]
    with path.open('w') as out:
        writer=csv.writer(out,lineterminator='\n')
        writer.writerow(['r','candidate_representations','prime_candidates','B_r_bits','prime_powers_below_cutoff','small_product','remaining_cofactor_bits'])
        for r in range(3,limit+1,4):
            if not flags[r]:continue
            B=denominator(r)
            if r<=400:assert rational_multiple(r)[0].denominator==B**2
            count,primes=norm_primes(r)
            supported=B.gcd(prime_product(primes))
            powers=[]
            for p in primes:
                if supported%p:continue
                assert modular_point(r,p) is None
                e=1
                while division_value(r,p**(e+1))==0:e+=1
                assert division_value(r,p)==0
                assert B%p**e==0 and B%p**(e+1)
                check_abscissa(r,p,e)
                powers.append((p,e));all_hits.append((r,p,e))
                if e>1:squares.append((r,p,e))
            assert supported==prod(p for p,e in powers)
            small=prod(p**e for p,e in powers)
            residue=B//small
            if residue==1:smooth.append(r)
            if r>3 and B**3<=fmpz(small)**500:mass_exceptions.append(r)
            writer.writerow([r,count,len(primes),B.bit_length(),' '.join(f'{p}^{e}' for p,e in sorted(powers)),small,residue.bit_length()])
            summaries.append((r,count,len(primes),B.bit_length(),len(powers),residue.bit_length()))
    result=dict(rank_bound=limit,direct_rational_crosscheck_through=min(limit,400),
        r_gt_3_with_at_most_497_over_500_log_mass_above_cutoff=mass_exceptions,ranks=len(summaries),candidate_representations=sum(s[1] for s in summaries),
        prime_candidates=sum(s[2] for s in summaries),first_primes=len(all_hits),ranks_with_small_prime=sum(s[4]>0 for s in summaries),
        squares=squares,smooth_ranks=smooth,maximum_found_per_rank=max(s[4] for s in summaries),
        largest_small_prime=max(all_hits,key=lambda entry:entry[1]))
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('bound',type=int,nargs='?',default=1000)
    ap.add_argument('--rows',type=Path,required=True)
    args=ap.parse_args()
    print(json.dumps(scan(args.bound,args.rows),indent=2))
