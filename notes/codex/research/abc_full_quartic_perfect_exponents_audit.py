"""Recheck the full perfect-power exponent census using PARI and an adjacent-point ladder.

Run: python3 abc_full_quartic_perfect_exponents_audit.py /path/to/rank_scan
The C++ scanner takes roughly one minute including the independent PARI enumeration.
"""
from hashlib import sha256
from math import isqrt
import subprocess
import sys

try:
    from cypari import pari
except ImportError:
    from cypari2 import Pari
    pari = Pari()
from abc_full_quartic_perfect_exponents import normalized_denominator

CUTOFF = 31_904_497
EXPECTED_DIGEST = '83917e8c564853dd46af78905ee4d0b95696aaa01fa77021522b6a85e884f312'


def enumeration():
    # The reduction of G+(0,0) is (12,36). Its odd prime order q is equivalent
    # to qG=(0,0) for odd prime q at the primes in this census.
    values = pari(f'''my(v=List());forprime(p=5,{CUTOFF},
        if(p%24==1 || p%24==23,
           my(s=ellorder(ellinit([0,0,0,-36,0],p),[12,36]));
           if(s%2 && isprime(s),listput(v,[s,p]))));Vec(v)'''.replace('\n',' '))
    return [(int(row[0]),int(row[1])) for row in values]


def double(point,modulus):
    x,y=point
    slope=(3*x*x-36)*pow(2*y,-1,modulus)%modulus
    u=(slope*slope-2*x)%modulus
    return u,(slope*(x-u)-y)%modulus


def plus(left,right,modulus):
    x,y=left
    u,v=right
    slope=(v-y)*pow(u-x,-1,modulus)%modulus
    xx=(slope*slope-x-u)%modulus
    return xx,(slope*(x-xx)-y)%modulus


def division_value(q,modulus):
    # Maintain consecutive division values and consecutive group points at j,j+1.
    a,b=1,18
    Q=(-3,9)
    R=double(Q,modulus)
    for digit in bin(q)[3:]:
        # psi_(2j+1)=(x_j-x_(j+1)) psi_j^2 psi_(j+1)^2,
        # psi_(2j)=2 y_j psi_j^4.  Here ord_p(G)=2q, so intermediate division
        # is always by a unit, even while performing the final step at q.
        w=(Q[0]-R[0])*(a*b)**2%modulus
        if digit=='0':
            a,b=2*Q[1]*a**4%modulus,w
            Q,R=double(Q,modulus),plus(Q,R,modulus)
        else:
            a,b=w,2*R[1]*b**4%modulus
            Q,R=plus(Q,R,modulus),double(R,modulus)
    return a


def exact_prefix():
    curve=pari.ellinit([0,0,0,-36,0])
    for n in range(1,102,2):
        x=pari.ellmul(curve,[-3,9],n)[0]
        denominator=int(pari.denominator(x))
        b=isqrt(denominator)
        assert b*b==denominator
        for m in (2**127-1,1009*1013,97**2,25):
            assert normalized_denominator(n,m)==(-1)**((n-1)//2)*b%m
    print('Exact rational abscissas verified at all 51 positive odd indices through 101, four moduli.')


def main(executable):
    rows=enumeration()
    expected=''.join(f'{q} {p}\n' for q,p in rows).encode('ascii')
    actual=subprocess.check_output([executable,str(CUTOFF),'--power-exponents'])
    assert actual==expected
    digest=sha256(actual).hexdigest()
    assert len(rows)==23883 and rows[-1]==(1993633,31903633) and digest==EXPECTED_DIGEST
    print(f'Full PARI order enumeration matched all {len(rows)} C++ pairs; final pair {rows[-1]}; SHA-256 {digest}',flush=True)
    for q,p in rows:
        m=p*p
        s=division_value(q,m)*pow(3,-((q*q-1)//2),m)%m
        assert s==normalized_denominator(q,m)
        assert s%p and pow(s,p-1,m)!=1
    print(f'Independent adjacent-point division ladder matched all {len(rows)} normalized residues modulo the exponent squared; every pair fails the power test.')
    exact_prefix()


if __name__=='__main__':
    if len(sys.argv)!=2:
        sys.exit('Pass the executable built from abc_full_quartic_prime_rank_scan.cpp.')
    main(sys.argv[1])
