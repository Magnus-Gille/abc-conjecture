"""Exact early-index search for p² dividing the primitive full Pell form at q=11."""
from argparse import ArgumentParser
from itertools import compress
from math import gcd, isqrt, log

from flint import fmpz, fmpz_poly
from abc_cm_twist_depth_example import degree_eleven_factors


def primes_to(bound):
    flags = bytearray([1])*(bound+1)
    flags[:2]=bytes(2)
    for p in range(2,isqrt(bound)+1):
        if flags[p]:
            flags[p*p::p]=bytes(1+(bound-p*p)//p)
    return list(compress(range(bound+1),flags))


def compatible_primes(bound):
    # A prime norm in the required CM class has p=1+22k.
    last=(bound-1)//22
    flags=bytearray([1])*(last+1)
    for ell in primes_to(isqrt(bound)):
        if ell in (2,11):
            continue
        k=-pow(22, -1, ell) % ell
        low=(ell*ell+20)//22
        start=low + (k-low)%ell
        if start<=last:
            flags[start::ell]=bytes(1+(last-start)//ell)
    primes=[]
    for b in range(1,isqrt(bound//242)+1):
        other=242*b*b
        width=isqrt(bound-other)
        for h in range(-((width+1)//22),(width-1)//22+1):
            p=(1+22*h)**2+other
            if flags[(p-1)//22]:
                primes.append(p)
    assert len(set(primes))==len(primes)
    return sorted(primes)


def product(numbers):
    if not numbers:
        return fmpz(1)
    while len(numbers)>1:
        numbers=[numbers[i]*numbers[i+1] for i in range(0,len(numbers)-1,2)] + (
            numbers[-1:] if len(numbers)%2 else [])
    return numbers[0]


def full_form():
    _, coefficients=degree_eleven_factors()
    s=fmpz_poly([1,0,2])
    x=-8*fmpz_poly([1,2,2])
    form=fmpz_poly([coefficients[0]])
    power=fmpz_poly([1])
    for c in coefficients[1:]:
        power*=s
        form=form*x+c*power
    content=form.content()
    assert content==2**125
    return [fmpz(c) for c in coefficients],content


def homogeneous(coeffs,x,s):
    # Balanced binary evaluation of G(x,s), with shared powers of x and s.
    powers_x={0:fmpz(1),1:x}
    powers_s={0:fmpz(1),1:s}
    def power(i,table):
        if i not in table:
            part=power(i//2,table)
            table[i]=part*part
            if i%2: table[i]*=table[1]
        return table[i]
    def evaluate(start,end):
        if end==start+1:
            return coeffs[start]
        mid=(start+end)//2
        return (evaluate(start,mid)*power(end-mid,powers_x)
                +evaluate(mid,end)*power(mid-start,powers_s))
    return evaluate(0,len(coeffs))


def pell_values(limit, sign=1):
    coefficients,content=full_form()
    # s + a sqrt(2) = epsilon^(2n), so s=S(a_n,b_n) and s+a=H(a_n,b_n).
    s,a=fmpz(1),fmpz(0)
    for n in range(limit+1):
        form=homogeneous(coefficients,-8*(s+sign*a),s)
        assert form%content==0
        yield abs(form//content)
        s,a=3*s+4*a,2*s+3*a


def batch_search(primes, limit, block, sign=1):
    sieve=product([fmpz(p) for p in primes])
    print('compatible primes, product bits',len(primes),sieve.bit_length(),flush=True)
    values=[]
    for n,value in enumerate(pell_values(limit,sign)):
        values.append(value)
        if len(values)<block and n<limit:
            continue
        g=sieve.gcd(product(values.copy()))
        for j,f in enumerate(values,n-len(values)+1):
            support=g.gcd(f)
            deep=support.gcd(f//support)
            if deep==1:
                continue
            for p, _ in deep.factor():
                assert p.is_prime() and int(p) in primes
                e=1
                while f%p**(e+1)==0:
                    e+=1
                print('square',sign*j,p,e,'quotient',f//p**e%p,flush=True)
        values=[]
        if n%512==511:
            print('through index',n,flush=True)
    print('finished signed index',sign*limit)


if __name__=='__main__':
    parser=ArgumentParser(description=__doc__)
    parser.add_argument('--prime-bound',type=int,default=10**8)
    parser.add_argument('--index-bound',type=int,default=4000)
    parser.add_argument('--block',type=int,default=32)
    parser.add_argument('--negative',action='store_true')
    args=parser.parse_args()
    batch_search(compatible_primes(args.prime_bound),args.index_bound,args.block,-1 if args.negative else 1)
