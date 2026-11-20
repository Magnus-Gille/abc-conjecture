"""Exact indexed squareclass sieve for the paired quartic on the fixed orbit."""
from functools import cache
from itertools import combinations,product
from math import gcd,isqrt,lcm

LIMIT=1031*2591
AUXILIARIES=(5,7,23,37,43,47)

def prime_flags(limit):
    flags=bytearray([1])*(limit+1)
    flags[:2]=b"\x00\x00"
    for p in range(2,limit+1):
        if flags[p] and p*p<=limit:
            flags[p*p::p]=bytes((limit-p*p)//p+1)
    return flags

def ec_add(A,B,p):
    if A is None:return B
    if B is None:return A
    x,y=A;u,v=B
    if x==u:
        if (y+v)%p==0:return None
        slope=(3*x*x-576)*pow(2*y,-1,p)%p
    else:slope=(y-v)*pow(x-u,-1,p)%p
    X=(slope*slope-x-u)%p
    return X,(slope*(x-X)-y)%p

def crt(h,M,k,N):
    g=gcd(M,N)
    if (k-h)%g:return None
    step=N//g
    return (h+M*((k-h)//g*pow(M//g,-1,step)%step),M*step)

def sign(c,ell):
    v=pow(c%ell,(ell-1)//2,ell)
    return -1 if v==ell-1 else v

@cache
def symbols(ell):
    Q=(-8%ell,-64%ell)
    S=Q
    sequence=[1] # At O the quotient of J by a fourth-order pole is a square unit.
    while S is not None:
        u,v=S
        sequence.append(sign(u*u+336*u+576,ell))
        S=ec_add(S,Q,ell)
        assert len(sequence)<=ell+2+2*isqrt(ell)
    return sequence

def visited_primes(bound):
    """Independent direct field enumeration over a bound of only 15995."""
    flags=prime_flags(bound)
    out={}
    for p in range(5,bound+1,2):
        if not flags[p]:continue
        seq=symbols(p)
        T=lcm(len(seq),2)
        roots=[i for i in range(1,T,2) if seq[i%len(seq)]==0]
        if roots:out[p]=(T,roots)
    return out

def seed_classes():
    # Even without using the first nontrivial orbit prime, there are two
    # distinct odd factors >=5. Probe to recover the true least orbit prime.
    small=visited_primes(300)
    least=min(small)
    assert sorted(small)==[167,191,263]
    table=visited_primes(LIMIT//least)
    primes=sorted(table)
    assert primes[:3]==[167,191,263] and 167*191*263>LIMIT
    result={}
    for p,q in combinations(primes,2):
        if p*q>LIMIT:continue
        M,A=table[p]
        N,B=table[q]
        initial=sorted({v for a,b in product(A,B) if (v:=crt(a,M,b,N)) is not None})
        result[(p,q)]=initial
    return result

@cache
def allowed(ell,g,s):
    return frozenset(i%g for i,v in enumerate(symbols(ell)) if v in (0,s))

def project_filter(h,M,ell,s):
    g=gcd(len(symbols(ell)),M)
    return h%g in allowed(ell,g,s)

def presieve(baseline,aux):
    output={}
    for (p,q),roots in baseline.items():
        if not roots:continue
        c=(2 if (p*q)%3==2 else -2)*p*q
        items=list(roots)
        for ell in aux:
            if ell in (p,q):continue
            s=sign(c,ell)
            items=[(h,M) for h,M in items if project_filter(h,M,ell,s)]
            if not items:break
        if items:output[(p,q)]=items
    return output

def verify():
    # The signed rational J squareclass is +/-2*d. Both dyadic factors
    # have total valuation 9, as this exhaustive odd-ratio check shows.
    def quartics(x,y):
        f=x**4-18*x*x*y*y+9*y**4
        t=12*x*y*(x*x-3*y*y)
        return f+t,f-t
    for x in range(1,1024,2):
        a,b=quartics(x,1)
        assert (a*b)%1024==512
    assert quartics(11,3)==(32*1031,-16*2591)
    B=seed_classes()
    print("bound",LIMIT,"number of prime pairs",len(B))
    stages=[]
    def counts(B):
        lower=[c for k,c in B.items() if k[0]*k[1]<LIMIT and c]
        return len(lower),sum(map(len,lower))
    stages.append(counts(B))
    for ell in AUXILIARIES:
        B=presieve(B,[ell])
        stages.append(counts(B))
        print("auxiliary, order, fewer-than-bound pairs and classes",ell,len(symbols(ell)),stages[-1])
    assert stages==[(119,440),(60,222),(28,104),(7,20),(4,14),(3,10),(0,0)]
    assert B=={(1031,2591):[(3,13932),(1293,13932),(12639,13932),(13929,13932)]}
    print("equality candidate and necessary CRT classes",B)

# For each multiplier K, the auxiliary primes below suffice to eliminate
# all nonzero j in n=3+69660*j modulo 69660*K.
REFINEMENTS=(
    (32,[6911, 5503, 6143]),
    (25,[1499, 2999, 199, 1999]),
    (49,[9941, 2351, 2939]),
    (11,[5939, 659]),
    (169,[457, 257, 6653, 8111]),
    (289,[5653, 5779, 1097, 2381, 9433]),
    (23,[7727, 827, 4139]),
    (29,[6263, 1777, 137]),
    (31,[619, 4463, 1487, 3347]),
    (37,[739, 6659, 6073]),
    (41,[181, 491, 1709]),
    (47,[5639, 563, 751, 1879, 9587]),
    (53,[6359, 2069, 3361]),
    (61,[937, 2927, 1193, 1237]),
    (73,[1409, 2377, 5857, 5953, 281]),
    (89,[4271, 3559, 1789, 701, 3533]),
    (97,[373, 353, 7753, 9781]),
    (101,[8017, 1609, 8233, 9901]),
    (109,[397, 1307, 449, 3433, 2273, 4493]),
    (113,[2297, 1753, 4637, 421, 1873]),
    (137,[593, 2753, 2161, 547, 2281]),
)

def verify_equality_index():
    c=-2*LIMIT
    base=13932
    seeds=(3,1293,12639,13929)
    eligible={h+base*j for h in seeds for j in range(5)}
    base*=5
    flags=prime_flags(10000)
    def restrict(residues,mod,primes):
        for ell in primes:
            assert flags[ell] and c%ell
            residues={h for h in residues if project_filter(h,mod,ell,sign(c,ell))}
        return residues
    assert restrict(eligible,base,(179,859))=={3,base-3}
    combined=base
    for K,primes in REFINEMENTS:
        M=base*K
        assert restrict({3+base*j for j in range(K)},M,primes)=={3}
        combined=lcm(combined,M)
    assert combined==751025916841423597521007417808841718128000
    print("equality requires n congruent to ±3 modulo",combined)

if __name__=='__main__':
    verify()
    verify_equality_index()
