"""Check completely factored Pell triples and compact whole-radical certificates."""
from argparse import ArgumentParser
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import cache
from math import gcd, isqrt, prod
from pathlib import Path
import json

from abc_octic_scalar_rank_verify import ec_mul

DATA=json.loads(Path(__file__).with_name('abc_pell11_whole_quality_cert.json').read_text())


@cache
def prime(p):
    if p<=10**7:
        return p>=2 and all(p%d for d in range(2,isqrt(p)+1))
    kind,*payload=DATA['certificates'][str(p)]
    if kind=='lucas':
        a,factors=payload
        return (prod(q**e for q,e in factors)==p-1 and pow(a,p-1,p)==1
                and all(q<p and e>0 and prime(q) and gcd(pow(a,(p-1)//q,p)-1,p)==1
                        for q,e in factors))
    assert kind=='ecpp'
    n=p
    for v,t,s,a,point in payload[0]:
        assert v==n and n>3 and gcd(n,6)==1 and s>0
        q,rem=divmod(n+1-t,s)
        assert not rem and (isqrt(isqrt(n))+2)**2<q<n
        x,y=point
        b=(y*y-x**3-a*x)%n
        assert gcd(4*a**3+27*b*b,n)==1
        Q=ec_mul(s,(x%n,y%n),n,a)
        assert Q is not None and ec_mul(q,Q,n,a) is None
        n=q
    return n<p and prime(n)


def pell(n):
    b,a=1,0
    for digit in bin(abs(n))[2:]:
        b,a=b*b+2*a*a,2*a*b
        if digit=='1':
            b,a=b+2*a,b+a
    return (b,-a if n<0 else a)


def terms(n, rational):
    b,a=pell(n)
    S=b*b+2*a*a
    H=S+2*a*b
    base=rational(-8*H,S)

    def double(x):
        return (x*x-32)**2/(4*x*(x*x+16*x+32))

    def total(x,y):
        return ((x*y-32)/(x-y))**2/base

    x,y=base,double(base)
    for bit in bin(11)[3:]:
        z=total(x,y)
        x,y=(z,double(y)) if bit=='1' else (double(x),z)
    U,V=x.numerator,x.denominator
    h=U*U+16*U*V+32*V*V
    raw_a,raw_c=h*h,1024*V**4
    g=raw_a.gcd(raw_c) if hasattr(raw_a,'gcd') else gcd(raw_a,raw_c)
    assert g==1024
    A,C=raw_a//g,raw_c//g
    B=C-A
    assert A>0 and B>0 and -U*(U+16*V)*(U+8*V)**2==g*B
    return (A,B,C),(U,V,h,S*H)


def complete():
    with localcontext() as ctx:
        ctx.prec=40
        for index,entries in DATA['rows'].items():
            n=int(index)
            values,_=terms(n,Fraction)
            support=set()
            for value, factors in zip(values,entries):
                assert prod(p**e for p,e in factors)==value
                assert len(factors)==len({p for p,e in factors})
                for p,e in factors:
                    assert p not in support and e>0 and prime(p)
                    support.add(p)
            C=values[-1]
            radical=prod(support)
            print(n,len(str(C)),len(support),Decimal(C)/Decimal(radical),
                  Decimal(C).ln()/Decimal(radical).ln())
        K,rows=DATA['partial']['1']
        assert pow(2,K-1,K)!=1
        values,_=terms(1,Fraction)
        support={p for factors in rows for p,e in factors}
        assert all(prime(p) for p in support) and gcd(K,prod(support))==1
        for value,rem,factors in zip(values,(1,K,1),rows):
            assert value==rem*prod(p**e for p,e in factors)
        scale=K*prod(support)
        print(1,'coefficient of K/rad(K)',Decimal(values[-1])/Decimal(scale))


BOUNDS={
    36:(13358,{3:1,19:1,109:1},1278037652803),
    1213:(449468,{683:1},17561961147),
    -3031:(1122902,{683:1},17561961147),
    3706:(1373191,{13:1,17:1,1409:1},16013474435410),
    13707:(5078831,{3:2,11:1,65099:1},165714999654467),
}


def trace_at_three():
    from abc_pell_whole_trace import build
    from abc_pell11_early_squares import homogeneous
    from flint import fmpz

    u,trace=build()
    coeffs=list(reversed(u.coeffs()))
    plus=abs(homogeneous(coeffs,fmpz(-40),fmpz(3)))
    minus=abs(homogeneous(coeffs,fmpz(-8),fmpz(3)))
    assert abs(trace(3))==3*plus*minus
    plus//=plus & -plus
    minus//=minus & -minus
    K,plus_factors=DATA['partial']['1']
    minus_factors=DATA['rows']['-1']
    def odd_support(rows):
        return prod({p for factors in rows for p,e in factors if p!=2})
    assert 3*minus==odd_support(minus_factors) and 3*plus==K*odd_support(plus_factors)
    assert plus.gcd(minus)==65 and (plus*minus)%3 and gcd(K,int(minus))==1
    print('gcd of odd oriented evaluations at S=3',65)


def gain(n):
    from flint import fmpq,fmpz
    (_,_,C),(U,V,h,D)=terms(n,fmpq)
    l=(-2*D*U*V).isqrt()
    w=(-h//32).isqrt()
    assert l*l==-2*D*U*V and 32*w*w==-h
    T=l*w*abs(U+16*V)*abs(U+8*V)
    T=2*(T//(T & -T))
    digits,excess,expected=BOUNDS[n]
    assert fmpz(10)**(digits-1)<=C<fmpz(10)**digits
    saving=1
    for p,e in excess.items():
        assert prime(p) and T%p**(e+1)==0 and T%p**(e+2)!=0
        saving*=p**e
    assert 10**8*C*saving//T==expected
    print(n,digits,expected)


if __name__=='__main__':
    parser=ArgumentParser(description=__doc__)
    parser.add_argument('--gains',action='store_true',help='Check the large integer certificates using python-flint')
    args=parser.parse_args()
    complete()
    if args.gains:
        trace_at_three()
        for n in BOUNDS:
            gain(n)
