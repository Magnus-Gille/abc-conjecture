"""Independent scalar certificates for the Pell square census, early factors and target histogram."""
from collections import Counter
from csv import DictReader
from math import gcd, prod
from pathlib import Path
from flint import fmpz

from abc_cm_pell_whole_triple import evaluate, pell
from abc_pell11_early_squares import compatible_primes, full_form, pell_values
from abc_pell11_square_periods import parameter_coefficients


def scalar_denominator(n, modulus):
    # x-coordinate multiplication by 11 on y²=x³+16x²+32x, shared by all twists.
    b,a=pell(abs(n),modulus)
    if n<0:
        a=-a
    s=(b*b+2*a*a)%modulus
    base=(-8*(s+2*a*b)%modulus,s)

    def double(P):
        x,z=P
        xx,zz,xz=x*x%modulus,z*z%modulus,x*z%modulus
        return (pow(xx-32*zz,2,modulus),4*xz*(xx+16*xz+32*zz)%modulus)

    def add_consecutive(P,Q):
        x,z=P
        y,w=Q
        return (base[1]*pow(x*y-32*z*w,2,modulus)%modulus,
                base[0]*pow(x*w-y*z,2,modulus)%modulus)

    P,Q=base,double(base)
    for bit in bin(11)[3:]:
        addition=add_consecutive(P,Q)
        if bit=='1':
            P,Q=addition,double(Q)
        else:
            P,Q=double(P),addition
    return P


def exact_square(p,n):
    x,z=scalar_denominator(n,p**5)
    assert x%p and z % p**4 == 0 and z != 0


def verify_small_factors():
    # The last factor in each row is the quotient by the listed factors.
    rules={
        0:[82633],
        1:[2179,18371],
        2:[268643,132679547527986097],
        4:[4027,772040897],
        5:[26203],
        -1:[9241,519853819],
        -2:[79856463754211,627829452273211],
        -4:[2179,1172777],
    }
    for sign in (1,-1):
        for i,f in enumerate(pell_values(5,sign)):
            n=sign*i
            if n==3:
                ds=[2179,4349753,21116393]
                rest,rem=divmod(f,prod(ds))
                assert not rem and len(str(rest))==100 and not rest.is_prime()
                assert all(fmpz(p).is_prime() and rest%p for p in ds)
            if n not in rules:
                continue
            ps=list(map(fmpz,rules[n]))
            last, rem=divmod(f,prod(ps))
            ps.append(last)
            assert not rem and len(ps)==len(set(ps)) and all(p.is_prime() for p in ps)
    coeff,content=full_form()
    form=parameter_coefficients(coeff,content)
    for p,period,expected in [(2,2,1),(11,24,10)]:
        b,a=1,0
        for n in range(period):
            assert sum(c*pow(a,j,p)*pow(b,100-j,p) for j,c in enumerate(form))%p==expected
            b,a=(b+2*a)%p,(b+a)%p
            assert (b,a)!=(1,0) or n+1==period
        assert (b,a)==(1,0)


def main():
    verify_small_factors()
    rows=[]
    with Path(__file__).with_name('abc_pell11_square_periods.csv').open() as handle:
        for line in DictReader(handle):
            rows.append(tuple(map(int,line.values())))
    assert [p for p,*rest in rows]==compatible_primes(10**7)
    coeff,_=full_form()
    coeff=list(map(int,coeff))
    histogram=Counter()
    total=0
    for p,m,r,n,residue,least_root in rows:
        assert 0<=r<=100 and r%gcd(m,2)==0
        histogram[r//gcd(m,2)]+=1
        if p<=10000:
            s,t=1,0
            roots=[]
            for j in range(m):
                if s and evaluate(coeff,-8*(s+t)*pow(s,-1,p)%p,p)==0:
                    roots.append(j)
                s,t=(3*s+4*t)%p,(2*s+3*t)%p
            assert len(roots)==r and min(roots,default=0)==least_root
        total+=r
        if r:
            assert n>0 and residue%p
            exact_square(p,n)
        else:
            assert n==residue==0
    assert len(rows)==6607 and total==356138 and histogram[0]==229
    assert sum(k*v for k,v in histogram.items())==180203
    assert [(p,n) for p,m,r,n,_,__ in rows if 0<n<p]==[(65099,13707)]
    for p,n in [(683,-3031),(683,4196890),(1409,4196890)]:
        exact_square(p,n)
    assert 10**(9*1213)<683**3900
    print('scalar checks',len(rows)-histogram[0]+3,'parameter roots',total)
    print('Laurent target histogram',sorted(histogram.items()))


if __name__=='__main__':
    main()
