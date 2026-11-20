"""Exhaust the primes below a bound in every dyadic packet. Standard Python only."""

import argparse
import itertools
import math


SMALL = {
    4: (7,),
    8: (2273,),
    16: (22151840117633,),
    32: (2401379840999699201, 100264636730315412574143047918721793),
}

# Lucas certificates: one witness of order p-1 followed by the complete factorization of p-1.
CERT = {
    22151840117633: (3, [(2,7),(59,1),(14321,1),(204821,1)]),
    2401379840999699201: (3, [(2,8),(5,2),(859,1),(4211,1),(6521,1),(15907,1)]),
    100264636730315412574143047918721793: (7, [(2,8),(3,2),(113159,1),(3758230277,1),(102327607955369761,1)]),
    102327607955369761: (11, [(2,5),(3,1),(5,1),(61,1),(20333,1),(171877999,1)]),
    3758230277: (2, [(2,2),(5431,1),(172999,1)]),
}


# n, prime, exact valuation in w_n, and w_n/p^e modulo p.
EXPECTED = [
    (4, 7, 1, 1),
    (8, 2273, 1, 1),
    (64, 242636033, 1, 64047156),
    (128, 67649537, 1, 7276566),
    (512, 339767297, 1, 181919147),
    (8192, 65229783041, 1, 16173440797),
]


def prime(p):
    if p not in CERT:
        return p >= 2 and (p == 2 or p % 2 and all(p % q for q in range(3,math.isqrt(p)+1,2)))
    a, factors = CERT[p]
    return (math.prod(q**e for q,e in factors) == p-1 and pow(a,p-1,p) == 1
            and all(prime(q) and math.gcd(pow(a,(p-1)//q,p)-1,p)==1 for q,e in factors))


def packet(n, modulus=None):
    """Evaluate w_n by homogeneous doubling, without modular division."""
    if n == 4:
        return 7 if modulus is None else 7 % modulus
    a = b = 1  # squared numerator and denominator at n=4
    j = 4
    while True:
        aa, ab, bb = a*a, a*b, b*b
        if modulus:
            aa, ab, bb = aa % modulus, ab % modulus, bb % modulus
        if 2*j == n:
            w = aa*(aa+32*ab+192*bb) + 1024*bb*(ab+bb)
            return w if modulus is None else w % modulus
        a, b = (aa-32*bb)**2, 4*ab*(aa+16*ab+32*bb)
        if modulus:
            a, b = a % modulus, b % modulus
        j *= 2


def screen(n):
    roots = []
    for ell in range(3,300,2):
        if not prime(ell): continue
        sqrt = next((r for r in range(ell) if (r*r+2)%ell == 0), None)
        roots.append((ell,sqrt,pow(2*n,-1,ell)))
    return roots


def candidates(n, bound):
    """Enumerate positive b and both signs of a; sieve only certified composites."""
    screening = screen(n)
    step = 2*n
    for b in range(1,math.isqrt(bound//(8*n*n))+1):
        vertical = 8*n*n*b*b
        width = math.isqrt(bound-vertical)
        low, high = -((width+1)//step), (width-1)//step
        count = high-low+1
        if not count: continue
        marks = bytearray([1])*count
        for ell,root,inv in screening:
            if root is None:
                if b%ell: continue
                residues = (-inv,)
            else:
                residues = (root*b-inv,-root*b-inv)
            for res in residues:
                start = (res-low)%ell
                if start<count:
                    marks[start::ell] = bytes(1+(count-start-1)//ell)
        yield count, [(1+step*a)**2+vertical for a in itertools.compress(range(low,high+1),marks)]


def detect(n,bound):
    exact = packet(n) if n <= 1024 else None
    hits = set()
    count = screened = 0
    for size, row in candidates(n,bound):
        count += size
        screened += len(row)
        if exact is None:
            for p in row:
                if packet(n,p) == 0 and prime(p): hits.add(p)
        else:
            # The gcd first skips batches whose represented integers are all coprime to w_n.
            for i in range(0,len(row),64):
                batch = row[i:i+64]
                d = math.gcd(exact,math.prod(batch))
                if d>1:
                    hits.update(p for p in batch if d%p==0 and prime(p))
    return count,screened,sorted(hits)


def scan(bound):
    for n, factors in SMALL.items():
        assert all(prime(p) for p in factors)
        assert math.prod(factors) == packet(n)
    rows = {n:[p for p in factors if p<=bound] for n,factors in SMALL.items()}
    total_pairs = total_screened = 0
    n=64
    while 8*n*n+1 <= bound:
        pairs,screened,rows[n] = detect(n,bound)
        total_pairs += pairs
        total_screened += screened
        print(f'n={n} norm_pairs={pairs} screened={screened} support={rows[n]}',flush=True)
        n *= 2
    first_excluded_index = n
    hits = []
    for n, factors in sorted(rows.items()):
        for p in factors:
            assert packet(n,p)==0
            e=1
            while packet(n,p**(e+1))==0:e+=1
            x = packet(n,p**(e+1))
            hits.append((n,p,e,x//p**e))
    if bound <= 10**12:
        assert hits == [row for row in EXPECTED if row[1] <= bound]
    if bound == 10**12:
        assert (total_pairs,total_screened,first_excluded_index) == (90375083,15840691,524288)
    print('All (n, p, valuation, normalized residue modulo p):', hits,flush=True)
    return hits


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('bound',nargs='?',type=int,default=10**12)
    scan(parser.parse_args().bound)
