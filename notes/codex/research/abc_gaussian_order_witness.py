"""Exact Gaussian denominator witnesses for G=(-3,9) on y^2=x^3-36x."""
import json
from fractions import Fraction as F
from functools import cache
from itertools import product
from math import gcd,isqrt,lcm,prod

G=(F(-3),F(9))

def add(P,Q,mod=0):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    adjust=(lambda a:a%mod) if mod else (lambda a:a)
    if adjust(x-u)==0:
        if adjust(y+v)==0:return None
        top,bottom=3*x*x-36,2*y
    else:top,bottom=y-v,x-u
    m=adjust(top*pow(bottom,-1,mod)) if mod else top/bottom
    z=adjust(m*m-x-u)
    return z,adjust(m*(x-z)-y)

@cache
def rational_point(n):
    if not n:return None
    if n<0:
        x,y=rational_point(-n)
        return x,-y
    half=rational_point(n//2)
    P=add(half,half)
    return add(P,G) if n%2 else P

def gaussian_product(A,B):
    a,b=A;c,d=B
    return a*c-b*d,a*d+b*c

def gaussian_b(factors):
    a,b=(1,0)
    for z in factors:a,b=gaussian_product((a,b),z)
    if not b:
        re=rational_point(a)[0];im=F(0)
    elif not a:
        re=-rational_point(b)[0];im=F(0)
    else:
        x,y=rational_point(a)
        u,v=rational_point(b)
        den=(x+u)**2
        re=(y*y-v*v)/den-x+u
        im=-2*y*v/den
    D=lcm(re.denominator,im.denominator)
    # Only the odd part away from 3 is relevant.
    D=without(D,6)
    B=isqrt(D)
    assert B*B==D
    return (a,b),B

def without(val,remove):
    while (d:=gcd(val,remove))>1:val//=d
    return val

def division_value(n,m):
    # Standard division polynomials evaluated at x=-3,y=9,A=-36,B=0.
    x=-3;a=-36;y=9
    initial=[0,1,2*y,3*x**4+6*a*x*x-a*a,
        4*y*(x**6+5*a*x**4-5*a*a*x*x-a**3)]
    inv=pow(2*y,-1,m)
    @cache
    def f(k):
        if k<5:return initial[k]%m
        h=k//2
        if k%2:return (f(h+2)*pow(f(h),3,m)-f(h-1)*pow(f(h+1),3,m))%m
        return f(h)*inv*(f(h+2)*f(h-1)**2-f(h-2)*f(h+1)**2)%m
    return f(n)

def modular_point(n,p):
    if n<0:
        T=modular_point(-n,p)
        return (T[0],-T[1]%p) if T else None
    Q=(-3%p,9%p);S=None
    while n:
        if n&1:S=add(S,Q,p)
        Q=add(Q,Q,p);n//=2
    return S

CERTIFIED_FACTORS={
    (4,7):[277,23423797,189458413],
    (8,-1):[229,6661,313933,21235213],
    (9,32):[4549],
    (23,24):[4701941281],
    (33,4):[35593,39153133,45434089],
    (31,-12):[181957,1450873],
}

def check_prime(r,alpha,ls,N,p):
    assert p>3 and N%p==0 and all(p%j for j in range(2,isqrt(p)+1))
    assert modular_point(r,p) is None
    smaller=[modular_point(r//q,p) for q in ls]
    assert all(T is not None for T in smaller)
    a,b=alpha
    P,Q=modular_point(a,p),modular_point(b,p)
    i=-P[1]*pow(Q[1],-1,p)%p
    assert (i*i+1)%p==0 and (P[0]+Q[0])%p==0
    assert add(P,(-Q[0]%p,i*Q[1]%p),p) is None
    depth=1
    while N%p**(depth+1)==0:depth+=1
    return dict(p=p,sqrt_minus_one=i,order_test_x=[T[0] for T in smaller],v_N=depth)

def witnesses(fixed):
    ls=[a*a+b*b for a,b in fixed];r=prod(ls)
    records=[]
    for signs in product([1,-1],repeat=len(fixed)-1):
        factors=[(a,b*s) for (a,b),s in zip(fixed,(1,)+signs)]
        alpha,B=gaussian_b(factors)
        old=[gaussian_b(factors[:j]+factors[j+1:])[1] for j in range(len(factors))]
        N=without(B,6*r*prod(old))
        assert N>1 and division_value(r,N)==0
        assert all(gcd(N,division_value(r//q,N))==1 for q in ls)
        assert all(gcd(N,record['N'])==1 for record in records)
        prime_checks=[check_prime(r,alpha,ls,N,p) for p in CERTIFIED_FACTORS[alpha]]
        if r==65:
            assert N==prod(x['p']**x['v_N'] for x in prime_checks)
        records.append(dict(r=r,alpha=alpha,factors=factors,B=B,old=old,N=N,prime_checks=prime_checks))
    return records

if __name__=='__main__':
    for factors in ([(2,1),(3,2)],[(2,1),(3,2),(4,1)]):
        for record in witnesses(factors):
            print(json.dumps(record))
