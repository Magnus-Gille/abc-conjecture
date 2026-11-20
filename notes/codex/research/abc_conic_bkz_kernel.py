"""Block lattice reduction on selected supports of the exact conic kernel."""
import argparse,json
from math import log
from fpylll import BKZ,FPLLL,IntegerMatrix
from abc_conic_short_kernel import cyclic_logs,lattice,parameters,vector

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('rank',type=int)
    ap.add_argument('sizes',type=int,nargs='+')
    ap.add_argument('--block',type=int,default=24)
    ap.add_argument('--loops',type=int,default=4)
    args=ap.parse_args()
    FPLLL.set_random_seed(901)
    data=parameters(args.rank)
    ell,eta,D,M,k,t,exps,H=data
    logs=[cyclic_logs(p,j,eta) for p,j in exps.items()]
    for size in args.sizes:
        subset=list(range(size))
        B,det=lattice(logs,subset)
        R=IntegerMatrix.from_matrix(B)
        BKZ.reduction(R,BKZ.Param(block_size=min(args.block,size),max_loops=args.loops))
        rows=[list(R[i])+[0]*(args.rank-size) for i in range(size)]
        def score(v):
            h=2*sum(abs(x)*log(p) for x,p in zip(v,ell))
            g=log(M)-log(D)-1.5*log(2)-sum(log(p) for p,x in zip(ell,v) if x)
            return g/h
        def weight(v):return sum(abs(x)*(log(p)+2*log(1+2**.5)) for x,p in zip(v,ell))
        selected=sorted(rows,key=score,reverse=True)[:4]+sorted(rows,key=weight)[:4]
        reports=[]
        for v in selected:
            if next(x for x in v if x)<0:v=[-x for x in v]
            assert all(sum(a*b for a,b in zip(v,l))%N==0 for N,l in logs)
            reports.append(vector(data,v))
        print(json.dumps(dict(d=args.rank,size=size,block=args.block,loops=args.loops,
              min_weight=min(reports,key=lambda x:x['weighted_l1']),
              best_M=max(reports,key=lambda x:x['gain_M_over_height']))),flush=True)
