"""Search supports of size at most four for strong conic radical certificates."""
import heapq,json,sys
from itertools import combinations
from math import log
from abc_conic_short_kernel import parameters,cyclic_logs,lattice,vector
for arg in sys.argv[1:]:
    d=int(arg)
    data=parameters(d)
    ell,eta,D,M,k,t,exps,H=data
    logs=[cyclic_logs(p,j,eta) for p,j in exps.items()]
    shortlist=[]
    seen=set()
    for s in range(1,5):
        for I in combinations(range(d),s):
            R,det=lattice(logs,I)
            for v in R:
                if any(x==0 for x in v):continue
                if v[0]<0:v=[-x for x in v]
                approx_height=2*sum(abs(x)*log(ell[i]) for x,i in zip(v,I))
                raw=log(M)-log(D)-sum(log(ell[i]) for i in I)-1.5*log(2)
                if raw<=0:continue
                z=[0]*d
                for i,x in zip(I,v):z[i]=x
                key=tuple(z)
                if key in seen:continue
                seen.add(key)
                entry=(raw/approx_height,key)
                if len(shortlist)<20:heapq.heappush(shortlist,entry)
                elif entry>shortlist[0]:heapq.heapreplace(shortlist,entry)
    rows=[vector(data,list(z)) for _,z in shortlist]
    print(json.dumps(dict(d=d,best_M=max(rows,key=lambda r:r['gain_M_over_height']),best_attained=max(rows,key=lambda r:r['gain_over_height']))),flush=True)
