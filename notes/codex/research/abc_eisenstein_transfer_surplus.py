"""Exact radical surplus for the degree-96 Eisenstein transfer, using proven prime factors."""
import argparse,json
from collections import Counter
from functools import lru_cache
from itertools import chain
from math import gcd,log,prod
from flint import fmpz

@lru_cache(maxsize=None)
def factor(n):
    n=abs(n)
    assert n
    fac=tuple((int(p),int(e)) for p,e in fmpz(n).factor())
    assert prod(p**e for p,e in fac)==n
    assert all(fmpz(p).is_prime() for p,e in fac)
    return fac

def factor_list(parts,halved=False):
    fac=Counter()
    for base,e in parts:
        for p,v in factor(base):
            fac[p]+=e*v
    if halved:
        fac[2]-=1
        if fac[2]==0:del fac[2]
    assert all(e>0 for e in fac.values())
    return fac

def product_fac(fac):return prod(p**e for p,e in fac.items())
def excess(fac):return prod(p**(e-1) for p,e in fac.items())

@lru_cache(maxsize=None)
def mapped(x,y):
    assert x%2 and y%2==0 and gcd(x,y)==1
    s,t=x**4,y**4
    def mult(P,Q):
        a,b=P;c,d=Q
        return a*c-3*b*d,a*d+b*c
    alpha=(s-t//2,t//2)
    square=mult(alpha,alpha)
    fourth=mult(square,square)
    U,V=map(abs,mult(fourth,mult(fourth,fourth)))
    W=s*s-s*t+t*t
    assert U*U+3*V*V==W**12 and gcd(U,3*V)==1 and gcd(U*V,W)==1
    A=s**4-8*s**3*t+6*s*s*t*t+4*s*t**3-2*t**4
    B=s**4+4*s**3*t-12*s*s*t*t+4*s*t**3+t**4
    C=2*s**4-4*s**3*t-6*s*s*t*t+8*s*t**3-t**4
    fsU=factor_list([(A,1),(B,1),(C,1)],True)
    parts=[3,x-y,x+y,x*x+y*y,s-2*t,s+t,2*s-t,s*s-4*s*t+t*t,s*s+2*s*t-2*t*t,2*s*s-2*s*t-t*t]
    fsV=factor_list([(x,4),(y,4)]+[(v,1) for v in parts],True)
    fsW=Counter(dict(factor(W)))
    assert (U,V,W)==tuple(map(product_fac,(fsU,fsV,fsW)))
    assert all(p%24 in (1,23) for p in fsU) and all(p%24==1 for p in fsW)
    return U,V,W,fsU,fsV,fsW

def compare(src,x):
    y=next(v for v in src if v%2==0)
    U,V,W,fu,fv,fw=mapped(x,y)
    src_rad=prod(set(p for v in src for p,e in factor(v)))
    out_rad=prod(set(chain(fu,fv,fw,[3])))
    assert 3 in fv
    c=max(src)
    marked={p for a in src for p,e in factor(a)}
    from_src=prod(p**(e-1) for p,e in fv.items() if p in marked)
    from_extra=prod(p**(e-1) for p,e in fv.items() if p not in marked)
    assert set(marked)<=set(fv)
    z=prod(src)//(x*y)
    for p in marked:
        def valuation(n):
            e=0
            while n%p==0:n//=p;e+=1
            return e
        if (x*y)%p==0:assert fv[p]==4*valuation(x*y)+valuation(6)
        else:assert fv[p]==valuation(z)+valuation(3)
    assert from_src*src_rad==2*(3 if 3 in marked else 1)*(x*y)**4*z
    archived=dict(src=src,x=x,y=y,source_rad=src_rad,out_rad=out_rad,
        U=U,V=V,W=W,U_factors=sorted(fu.items()),V_factors=sorted(fv.items()),W_factors=sorted(fw.items()),
        source_log_gain=log(c)-log(src_rad),out_log_gain=12*log(W)-log(out_rad),
        source_quality=log(c)/log(src_rad),out_quality=12*log(W)/log(out_rad),
        base_log=11*log(W)-log(U)-log(V),v_source_excess=from_src,v_extra_excess=from_extra,
        u_excess=excess(fu),w_excess=excess(fw))
    ds=archived
    assert W**11*ds['u_excess']*ds['w_excess']*from_src*from_extra*out_rad==W**12*U*V
    return ds

def odd_choices(src):
    return sorted(set(t for t in src if t%2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bound',type=int,default=0)
    parser.add_argument('--triple',type=int,nargs=3,action='append',default=[])
    args=parser.parse_args()
    triples=args.triple
    for c in range(3,args.bound+1):
        for a in range(1,c//2+1):
            if gcd(a,c)==1:triples.append((a,c-a,c))
    for src in triples:
        a,b,c=src
        assert a+b==c and gcd(a,b)==1
        for x in odd_choices(src):
            print(json.dumps(compare(src,x)),flush=True)
