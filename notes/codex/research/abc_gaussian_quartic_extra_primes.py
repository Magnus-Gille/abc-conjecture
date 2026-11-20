"""Test an additional annulus above r^4 for explicit odd-exponent primes."""
import argparse,csv,json
from functools import cache
from math import isqrt,prod
from pathlib import Path
from flint import fmpz
from abc_gaussian_quartic_prime_scan import denominator,prime_product
from abc_gaussian_order_witness import modular_point,division_value

def extra_prime_candidates(r,multiple):
    lower=r**4
    upper=multiple*lower
    out=set()
    for b in range(2,isqrt(upper)//r+1,2):
        m=isqrt(upper-(b*r)**2)
        low=-((m+1)//r)
        for a in range(low+(-low)%4,(m-1)//r+1,4):
            p=(1+a*r)**2+(b*r)**2
            if lower<p and p%12==1 and fmpz(p).is_prime():out.add(p)
    return out

def check(path,multiple):
    out=[]
    for row in csv.DictReader(open(path)):
        r=int(row['r']);S=int(row['small_product']);C=denominator(r)//S
        if C==1:continue
        primes=extra_prime_candidates(r,multiple)
        support=prime_product(primes).gcd(C)
        explicit=[p for p in sorted(primes) if support%p==0]
        # Modest smooth factoring at the first few ranks only.
        if r<=47:
            fs=C.factor_smooth(35,1)
            explicit=sorted(set(explicit+[int(p) for p,e in fs if p.is_prime()]))
        rem=C;factors=[]
        for p in explicit:
            assert p>r**4 and fmpz(p).is_prime() and modular_point(r,p) is None
            e=0
            while rem%p==0:rem//=p;e+=1
            assert e and division_value(r,p**(e+1))%p**e==0 and division_value(r,p**(e+1))!=0
            factors.append((p,e))
        if factors:
            qsign=None
            if rem>1 and not rem.is_square():
                for q in range(3,1000,2):
                    if fmpz(q).is_prime() and pow(int(rem%q),(q-1)//2,q)==q-1:
                        qsign=q;break
                assert qsign
            out.append(dict(r=r,explicit=factors,remaining_cofactor_bits=rem.bit_length(),
                extra_nonresidue=qsign,lower_odd_primes=sum(e%2 for p,e in factors)+bool(qsign)))
    return out

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--multiple',type=int,default=16)
    ap.add_argument('--input',type=Path,default=Path(__file__).with_name('abc_gaussian_quartic_prime_scan.csv'))
    args=ap.parse_args()
    print(json.dumps(dict(annulus_max_multiple=args.multiple,rows=check(args.input,args.multiple)),indent=2))
