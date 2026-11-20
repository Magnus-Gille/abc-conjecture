"""Scan every possible p <= 10r² of odd prime order r=3 mod 4 for G=(-3,9)."""
import argparse,csv,hashlib,json
from math import isqrt
from pathlib import Path
from abc_gaussian_order_witness import division_value,modular_point

def prime_flags(limit):
    flags=bytearray([1])*(limit+1)
    flags[:2]=bytes(2)
    for p in range(2,isqrt(limit)+1):
        if flags[p]:flags[p*p::p]=bytes((limit-p*p)//p+1)
    return flags

def prime64(n):
    # The seven bases below are deterministic for all 0<n<2^64.
    assert 0<n<1<<64
    if n==1:return False
    for q in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n%q==0:return n==q
    odd=n-1;s=0
    while odd%2==0:
        odd//=2;s+=1
    for a in (2,325,9375,28178,450775,9780504,1795265022):
        if a%n==0:continue
        v=pow(a,odd,n)
        if v in (1,n-1):continue
        for _ in range(s-1):
            v=v*v%n
            if v==n-1:break
        else:return False
    return True

def candidates(r,factor):
    # b=0 is a rational square; b>0 represents the two conjugates once.
    cap=factor*r*r
    result={}
    for b in range(1,isqrt(factor)+1):
        bound=isqrt(cap-(b*r)**2)
        for a in range(-((bound+1)//r),(bound-1)//r+1):
            p=(1+a*r)**2+(b*r)**2
            if p%12==1:result.setdefault(p,[]).append((a,b))
    return result

def check_abscissa(n,p,e):
    # Projective x-only ladder on y²=x³-36x, with consecutive multiples
    # and fixed difference G. Z measures twice the denominator depth.
    mod=p**(2*e+1)
    def double(P):
        x,z=P
        return pow(x*x+36*z*z,2,mod),4*x*z*(x*x-36*z*z)%mod
    def consecutive(P,Q):
        x,z=P;u,w=Q
        return pow(x*u+36*z*w,2,mod),-3*pow(x*w-u*z,2,mod)%mod
    P=(-3%mod,1);Q=double(P)
    for bit in bin(n)[3:]:
        mid=consecutive(P,Q)
        if bit=='1':P,Q=mid,double(Q)
        else:P,Q=double(P),mid
    x,z=P
    assert x%p and z%p**(2*e)==0 and z

def scan(limit,factor,orders_path):
    flags=prime_flags(limit)
    counts={k:0 for k in ['ranks','norm_candidates','prime_candidates','even_coefficient_prime_candidates',
                           'exact_orders','first_squares','ranks_with_prime']}
    histogram={};hits=[];samplers=[]
    with orders_path.open('w') as out:
        writer=csv.writer(out,lineterminator='\n')
        writer.writerow(['r','p','a','b','e','psi_r_div_p_mod_p'])
        for r in range(3,limit+1,4):
            if not flags[r]:continue
            counts['ranks']+=1
            found=0
            for p,reps in sorted(candidates(r,factor).items()):
                counts['norm_candidates']+=1
                if not prime64(p):continue
                counts['prime_candidates']+=1
                primary=[(a,b) for a,b in reps if not (a%2 or b%2)]
                counts['even_coefficient_prime_candidates']+=bool(primary)
                P=modular_point(r,p)
                # Confirm both field computations at every candidate.
                if P is not None:
                    assert division_value(r,p)
                    continue
                assert primary
                a,b=primary[0]
                value=division_value(r,p*p)
                assert value%p==0
                e=1
                if value==0:
                    e=2
                    while division_value(r,p**(e+1))==0:e+=1
                    hits.append((r,p,e));counts['first_squares']+=1
                check_abscissa(r,p,e)
                writer.writerow([r,p,a,b,e,value//p])
                found+=1;counts['exact_orders']+=1
                if len(samplers)<12:samplers.append((r,p,e))
            counts['ranks_with_prime']+=bool(found)
            histogram[found]=histogram.get(found,0)+1
    assert modular_point(106,211) is None
    assert modular_point(53,211)==(6,0) and modular_point(2,211) is not None
    assert division_value(106,211**3)==2*211**2
    check_abscissa(106,211,2)
    return dict(limit=limit,window=factor,counts=counts,order_count_per_rank=histogram,squares=hits,sample=samplers,
                exact_orders_sha256=hashlib.sha256(orders_path.read_bytes()).hexdigest())

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('bound',type=int,nargs='?',default=10**6)
    ap.add_argument('--orders',type=Path,required=True)
    ap.add_argument('--window',type=int,default=10)
    args=ap.parse_args()
    print(json.dumps(scan(args.bound,args.window,args.orders),indent=2))
