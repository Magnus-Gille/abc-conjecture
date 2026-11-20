"""Use PARI to verify all reported hits, all good primes through 10,000, and a high interval."""
from pathlib import Path
import re

try:
    from cypari import pari
except ImportError:
    from cypari2 import Pari
    pari = Pari()


curve = pari.ellinit([0,0,0,-36,0])
G = [-3,9]


def local_depth(p,r):
    one = pari(f'1+O({p}^16)')
    local = pari.ellinit([0,0,0,-36*one,0*one])
    x,y = pari.ellmul(local, [-3*one,9*one], r)
    vx,vy = int(pari.valuation(x,p)),int(pari.valuation(y,p))
    assert vx < 0 and vx % 2 == 0 and 3*vx == 2*vy
    return -vx//2


def check_interval(low,high):
    checked,odds,twice,prime_orders = 0,0,0,0
    hits=[]
    for z in pari.primes([low,high]):
        p=int(z)
        finite=pari.ellinit([0,0,0,-36,0],p)
        r=int(pari.ellorder(finite,G))
        checked+=1
        if r%4==0:
            continue
        if r%2:
            odds+=1
            prime_orders+=int(pari.isprime(r))
        else:
            twice+=1
        depth=local_depth(p,r)
        if depth>1:
            hits.append((p,r,depth))
    print(f'interval [{low},{high}]: checked {checked}, odd {odds}, twice odd {twice}, odd prime orders {prime_orders}, hits {hits}')
    return checked,odds,twice,prime_orders,hits


if __name__=='__main__':
    transcript=Path(__file__).with_name('abc_full_quartic_first_depth_scan_31904497.txt').read_text()
    hits=[(int(p),int(r)) for p,r in re.findall(r'^hit p=(\d+) r=(\d+)$',transcript,re.M)]
    assert hits == [(211,106)]
    for p,r in hits:
        finite=pari.ellinit([0,0,0,-36,0],p)
        assert int(pari.ellorder(finite,G)) == r
        local=local_depth(p,r)
        x,y=pari.ellmul(curve,G,r)
        vx,vy=int(pari.valuation(x,p)),int(pari.valuation(y,p))
        assert vx==-2*local and vy==-3*local and local==2
        translated_order=int(pari.ellorder(finite,[-2,-8]))
        assert translated_order==53
        print(f'p={p}, order={r}, exact rational x,y valuations={vx},{vy}, independent p-adic depth={local}, order of G+(6,0)={translated_order}')
    assert check_interval(5,10000)==(1227,168,686,65,[(211,106,2)])
    assert check_interval(31903497,31904497)[-1]==[]
