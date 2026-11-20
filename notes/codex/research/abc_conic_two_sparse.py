"""Certify the shortest conic relation supported on at most two generators."""
import json,sys
from itertools import combinations
from abc_conic_short_kernel import cyclic_logs,lattice,parameters

def length(v):return abs(v[0])+abs(v[1])
def sq(v):return v[0]**2+v[1]**2
def min_l1(B):
    a,b=B
    while True:
        if sq(b)<sq(a):a,b=b,a
        dot=sum(i*j for i,j in zip(a,b))
        if 2*abs(dot)<=sq(a):break
        k=(2*dot+sq(a))//(2*sq(a))
        b=[x-k*y for x,y in zip(b,a)]
    # Gauss reduction gives distance between the a-lines at least sqrt(3)|a|/2.
    # Since ||a||_1 <= sqrt(2)|a|, a shortest vector is on line 0 or +/-1.
    choices=[a]
    for x,y in zip(a,b):
        if x:
            t=(-y)//x
            for k in [t,t+1]:
                choices.append([j+k*i for i,j in zip(a,b)])
    return min(choices,key=length)

if __name__=='__main__':
    for arg in sys.argv[1:]:
        d=int(arg)
        data=parameters(d)
        ell,eta,D,M,k,t,exps,H=data
        logs=[cyclic_logs(p,j,eta) for p,j in exps.items()]
        best=None
        for i,j in combinations(range(d),2):
            B,det=lattice(logs,[i,j])
            v=min_l1(B)
            if best is None or length(v)<best[0]:
                best=length(v),i,j,v
        size,i,j,v=best
        assert all((v[0]*L[i]+v[1]*L[j])%N==0 for N,L in logs)
        print(json.dumps(dict(d=d,minimum=size,split_primes=[ell[i],ell[j]],coefficients=v)),flush=True)
