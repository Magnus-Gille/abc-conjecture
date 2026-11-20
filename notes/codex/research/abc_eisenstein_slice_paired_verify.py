"""Direct integer early-index census for the paired quartic on the original curve."""
import argparse
from fractions import Fraction
from functools import cache
from math import isqrt
from flint import fmpz
from abc_eisenstein_twelfth_slice_check import add

P=(Fraction(-2),Fraction(8))
@cache
def point(n):
    if not n:return None
    h=point(n//2);Q=add(h,h)
    return add(Q,P) if n%2 else Q

def quartics(n):
    value=-point(n)[0]/2
    x,y=isqrt(value.numerator),isqrt(value.denominator)
    assert x*x==value.numerator and y*y==value.denominator
    f=x**4-18*x*x*y*y+9*y**4
    t=12*x*y*(x*x-3*y*y)
    return x,y,fmpz(f+t),fmpz(f-t)

def product(values):
    items=list(values)
    if not items:return fmpz(1)
    while len(items)>1:
        items=[x*y for x,y in zip(items[::2],items[1::2])]+(items[-1:] if len(items)%2 else [])
    return items[0]

def allowed_primes(limit):
    # Every odd p>3 in F+F- divides the real part of beta^12, hence p=+-1 mod 24.
    small=bytearray([1])*(isqrt(limit)+1)
    for ell in range(2,len(small)):
        if small[ell]:
            small[ell*ell::ell]=bytes(len(small[ell*ell::ell]))
    for rem in [1,23]:
        size=(limit-rem)//24+1
        sieve=bytearray([1])*size
        if rem==1:sieve[0]=0
        for ell in range(5,len(small)):
            if not small[ell]:continue
            low=max(0,(ell*ell-rem+23)//24)
            j=low+(-rem*pow(24,-1,ell)-low)%ell
            if j<size:sieve[j::ell]=bytes((size-1-j)//ell+1)
        for j,flag in enumerate(sieve):
            if flag:yield 24*j+rem

def prime_product(limit):
    chunks=[];block=[];count=0
    for p in allowed_primes(limit):
        count+=1;block.append(fmpz(p))
        if len(block)==8192:
            chunks.append(product(block));block.clear()
    chunks.append(product(block))
    return count,product(chunks)

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('prime_bound',type=int,nargs='?',default=10**8)
    ap.add_argument('index_bound',type=int,nargs='?',default=209)
    args=ap.parse_args()
    how_many,D=prime_product(args.prime_bound)
    print('prime bound, eligible primes, sieve bits',args.prime_bound,how_many,D.bit_length(),flush=True)
    values=[]
    for n in range(1,args.index_bound+1,2):
        x,y,a,b=quartics(n)
        values.append(abs(a*b))
        if n<=13:
            common=a.gcd(b)
            while common%2==0:common//=2
            while common%3==0:common//=3
            assert common==1
            for v in (a,b):
                fs=abs(v).factor()
                assert all(p.is_prime() for p,e in fs)
                assert product([p**e for p,e in fs])==abs(v)
                assert all(e==1 for p,e in fs if p>3)
        if n==209:
            assert (x%191,y%191)==(18,36)
            assert a%191**2==0 and a//191**2%191==27 and b%191==83
    active=D.gcd(product(values))
    hits=[]
    for n,v in zip(range(1,args.index_bound+1,2),values):
        h=v.gcd(active)
        repeated=h.gcd(v//h)
        if repeated>1:
            for p,_ in repeated.factor():
                assert p.is_prime()
                e=2
                while v%p**(e+1)==0:e+=1
                hits.append((n,int(p),e))
    print('index bound, all hits',args.index_bound,hits)
