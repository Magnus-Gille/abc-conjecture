"""Independent exact rational verification of the exceptional first denominator."""
from fractions import Fraction
from functools import cache
from math import isqrt
from abc_eisenstein_twelfth_slice_check import add

P=(Fraction(-2),Fraction(8))

@cache
def point(n):
    if n==0:return None
    h=point(n//2)
    d=add(h,h)
    return add(d,P) if n%2 else d

@cache
def psi(n):
    if n<0:return -psi(-n)
    if n<5:return (0,1,16,-1536,3670016)[n]
    k=n//2
    if n%2:return psi(k+2)*psi(k)**3-psi(k-1)*psi(k+1)**3
    numerator=psi(k)*(psi(k+2)*psi(k-1)**2-psi(k-2)*psi(k+1)**2)
    assert numerator%16==0
    return numerator//16

p=211
Q=point(53)
B=isqrt(Q[0].denominator)
assert B*B==Q[0].denominator and B%(p*p)==0 and B//(p*p)%p==149
assert psi(53)%(p*p)==0 and psi(53)//(p*p)%p==117
print('B_53',B)
print('B_53/211^2 mod 211',149,'psi_53/211^2 mod 211',117)
for n in [105,107]:
    t=-point(n)[0]/2
    x,y=isqrt(t.numerator),isqrt(t.denominator)
    assert x*x==t.numerator and y*y==t.denominator
    delta=x*x-y*y
    assert delta%(p*p)==0 and delta//(p*p)%p
    print('n, digits of x and y, (x^2-y^2)/211^2 mod 211',n,len(str(x)),len(str(y)),delta//(p*p)%p)
