"""Verify sharp individual squarefree kernels using the original elliptic point orbit."""
from math import lcm
from pathlib import Path
import json

from sympy import primerange
from abc_eisenstein_slice_minimum_kernel import odd_visits, quartics, delta


def add(P,Q,p):
    if P is None:
        return Q
    if Q is None:
        return P
    x,y=P
    u,v=Q
    if x==u:
        if (y+v)%p==0:
            return None
        slope=(3*x*x+72*x+36)*pow(2*y%p,-1,p)%p
    else:
        slope=(v-y)*pow((u-x)%p,-1,p)%p
    t=(slope*slope-36-x-u)%p
    return t,(slope*(x-t)-y)%p


def allowed(p,i,d):
    Q=(-2%p,8%p)
    step=add(Q,Q,p)
    squares={s*s%p:s for s in range(p)}
    k=(1 if d%3==1 else -1)*(1 if i==4 else -1)*d
    values={(1<<i)*k*s%p for s in squares}
    P=Q
    hs=[]
    h=1
    while True:
        if P is None:
            x,y=1,0
        else:
            x,y=squares[-P[0]*pow(2,-1,p)%p],1
        _,plus,minus=quartics(x,y)
        if plus%p in values or minus%p in values:
            hs.append(h)
        P=add(P,step,p)
        h+=2
        if P==Q:
            return h-1,hs


def main():
    visited=[p for p in primerange(5,2592) if odd_visits(p)[1]]
    assert visited[0]*visited[1]>2591
    out={"primes_scanned":len(list(primerange(5,2592))),"visited":visited,"bounds":{}}
    for i,cap in ((4,2591),(5,1031)):
        tests=[(d,delta(d,4 if i==4 else 2)) for d in visited if d<=cap]
        witnesses={}
        for d,diff in tests:
            if d==cap:
                continue
            if d in (191,311,983,1367):
                places=[11]
            elif (i,d) in ((5,167),(4,263)):
                places=[17,19]
            elif (i,d)==(4,1031):
                places=[71,251]
            else:
                places=[13,73]
            restrictions=[(p,*allowed(p,i,d)) for p in places]
            period=lcm(*(r for p,r,hs in restrictions))
            assert not any(all(n%r in hs for p,r,hs in restrictions) for n in range(1,period,2))
            witnesses[str(d)]=restrictions
        assert [d for d,diff in tests if str(d) not in witnesses]==[cap]
        out["bounds"][str(i)]={"minimum":cap,"tunnell_deltas":tests,"individual_local_obstructions":witnesses}
    assert quartics(11,3)==(-8*23**2,32*1031,-16*2591)
    path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))


if __name__=='__main__':
    main()
