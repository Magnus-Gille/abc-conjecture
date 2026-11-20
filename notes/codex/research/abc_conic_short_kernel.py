"""Certified conic moduli, projective discrete logarithms and short relation witnesses."""
import argparse
import json
from itertools import combinations
from math import gcd,isqrt,prod
from pathlib import Path
from sympy import primerange,nextprime,factorint
from flint import arb,ctx,fmpz_mat
ctx.prec=256

def parameters(d):
    small=list(map(int,primerange(2,d+1)))
    ell=[]
    p=d
    while len(ell)<d:
        p=int(nextprime(p))
        if p%8 in (1,7):ell.append(p)
    eta=[]
    for p in ell:
        pairs=[]
        for a in range(1,isqrt(3*p//2)+1):
            for z in (2*a*a+p,2*a*a-p):
                if z<=0:continue
                b=isqrt(z)
                if b*b==z and b*b+2*a*a<=3*p:
                    pairs.append((b*b+2*a*a,b,a))
        _,b,a=min(pairs)
        eta.append((b,a))
    D=prod(small)
    ld=arb(d).log()
    epsilon=1+arb(2).sqrt()
    H=2*(arb(1).exp()/arb.pi()).sqrt()*d*d*ld**2
    log_L=(2*d/arb.pi()).log()/2+(arb(d)/2+2).gamma().log()/d
    log_U=d*(H.log()-log_L)-sum((arb(p).log()+2*epsilon.log()).log() for p in ell)
    log_bound=log_U-arb(2).log()-sum((1+1/arb(p)).log() for p in small)
    k=int((log_bound/arb(D).log()).floor().unique_fmpz())
    t=int(((log_bound-k*arb(D).log())/arb(3).log()).floor().unique_fmpz())
    assert k>=1 and t>=0
    M=D**k*3**t
    assert arb(M).log()<=log_bound<arb(3*M).log()
    exps={p:k+(t if p==3 else 0) for p in small}
    return ell,eta,D,M,k,t,exps,H

def mul(x,y,q):
    b,a=x
    c,e=y
    return ((b*c+2*a*e)%q,(b*e+a*c)%q)

def power(x,e,q):
    y=(1,0)
    while e:
        if e&1:y=mul(y,x,q)
        x=mul(x,x,q)
        e//=2
    return y

def normalize(x,p,q):
    b,a=x
    if b%p:return (1,a*pow(b,-1,q)%q)
    return (b*pow(a,-1,q)%q,1)

def cyclic_logs(p,j,eta):
    q=p**j
    N=q if p==2 else (q//p)*(p-(1 if p%8 in (1,7) else -1))
    fs={int(l):int(e) for l,e in factorint(N).items()}
    i=0
    while True:
        i+=1
        g=(1,i)
        if (1-2*i*i)%p and all(power(g,N//l,q)[1] for l in fs):break
    assert power(g,N,q)[1]==0
    tables={}
    for l,e in fs.items():
        base=power(g,N//l,q)
        tables[l]={normalize(power(base,z,q),p,q):z for z in range(l)}
    logs=[]
    for h in eta:
        x=0
        for l,e in fs.items():
            curr=h
            inv_g=(g[0],-g[1])
            v=0
            for r in range(e):
                digit=tables[l][normalize(power(curr,N//l**(r+1),q),p,q)]
                v+=digit*l**r
                curr=mul(curr,power(inv_g,digit,q),q)
                inv_g=power(inv_g,l,q)
            n=l**e
            x+=v*(N//n)*pow(N//n,-1,n)
        x%=N
        assert normalize(power(g,x,q),p,q)==normalize(h,p,q)
        logs.append(x)
    return N,logs

def lattice(logs,subset):
    n=len(subset)
    B=[[int(i==j) for j in range(n)] for i in range(n)]
    det=1
    for N,full_row in logs:
        row=[full_row[i] for i in subset]
        for p,e in factorint(N).items():
            q=int(p**e)
            residues=[sum(a*b for a,b in zip(v,row))%q for v in B]
            i=min(range(n),key=lambda j:gcd(q,residues[j]))
            g=gcd(q,residues[i])
            size=q//g
            if size==1:continue
            inv=pow(residues[i]//g,-1,size)
            pivot=B[i]
            for j in range(n):
                if j==i:continue
                c=-(residues[j]//g)*inv%size
                if 2*c>size:c-=size
                if c:B[j]=[x+c*y for x,y in zip(B[j],pivot)]
            B[i]=[size*x for x in pivot]
            det*=size
    R=fmpz_mat(B).lll()
    assert abs(R.det())==det
    return [[int(x) for x in v] for v in R.tolist()],det

def vector(data,z):
    ell,etas,D,M,k,t,exps,H=data
    support=[i for i,x in enumerate(z) if x]
    rj=prod(ell[i] for i in support)
    log_j=sum(abs(z[i])*arb(ell[i]).log() for i in support)
    v=sum(z[i]*((etas[i][0]+etas[i][1]*arb(2).sqrt())/arb(ell[i]).sqrt()).log() for i in support)
    log_C=2*(log_j+(2*v).cosh().log())
    gain_M=arb(M).log()-arb(D).log()-arb(rj).log()+(arb(2).sqrt()/4).log()
    extra=0
    vals={}
    for p,j in exps.items():
        while True:
            q=p**(j+1)
            h=(1,0)
            for i in support:
                b,a=etas[i]
                h=mul(h,power((b,a if z[i]>0 else -a),abs(z[i]),q),q)
            assert h[0]%p!=0 and h[1]%(q//p)==0
            if h[1]:break
            j+=1
        vals[p]=j
        extra+=(j-1)*arb(p).log()
    gain=extra-arb(rj).log()+(2*arb(2).sqrt()/abs((2*v).tanh())).log()
    weighted=sum(abs(z[i])*(arb(ell[i]).log()+2*(1+arb(2).sqrt()).log()) for i in support)
    def num(x):return float(x)
    return dict(weighted_l1=num(weighted),H=num(H),within_packing_ball=bool(weighted<=H),z=z,l1=sum(map(abs,z)),s=len(support),v_a=vals,log_C=num(log_C),
        log_gain_M=num(gain_M),log_gain_attained=num(gain),gain_over_height=num(gain/log_C),
        gain_M_over_height=num(gain_M/log_C),height_digits=int((log_C/arb(10).log()).floor().unique_fmpz())+1)

def scan(d,fractions):
    data=parameters(d)
    ell,eta,D,M,k,t,exps,H=data
    logs=[cyclic_logs(p,j,eta) for p,j in exps.items()]
    result=dict(d=d,D=str(D),M=str(M),k=k,t=t,primes=ell,generators=eta,search=[])
    for size in sorted({max(2,(d*n)//100) for n in fractions},reverse=True):
        subset=list(range(size))
        reduced,det=lattice(logs,subset)
        # Minimize low norm and improve support using two close reduced rows.
        pool=list(reduced)
        if size<=24:
            for a,b in combinations(reduced,2):
                pool.extend([[x+s*y for x,y in zip(a,b)] for s in [-1,1]])
        ordered=sorted(pool,key=lambda v:(sum(map(abs,v)),sum(x!=0 for x in v)))
        candidates=ordered[:4]
        # Include particularly sparse basis vectors and the best theorem certificate ratio.
        candidates.extend(sorted(pool,key=lambda v:(sum(x!=0 for x in v),sum(map(abs,v))))[:4])
        log_M=float(arb(M).log()-arb(D).log()+(arb(2).sqrt()/4).log())
        logell=[float(arb(p).log()) for p in ell]
        def estimate(v):
            return (log_M-sum(l for x,l in zip(v,logell) if x))/(2*sum(abs(x)*l for x,l in zip(v,logell)))
        candidates.extend(sorted(pool,key=estimate,reverse=True)[:8])
        rows=[]
        seen=set()
        for v in candidates:
            v=v+[0]*(d-size)
            if next(x for x in v if x)<0:v=[-x for x in v]
            if tuple(v) in seen:continue
            seen.add(tuple(v))
            assert all(sum(a*b for a,b in zip(v,l))%N==0 for N,l in logs)
            rows.append(vector(data,v))
        best=max(rows,key=lambda r:r['gain_over_height'])
        shortest=min(rows,key=lambda r:(r['l1'],r['s']))
        best_M=max(rows,key=lambda r:r['gain_M_over_height'])
        result['search'].append(dict(size=size,det=str(det),shortest=shortest,best=best,best_M=best_M))
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('dimensions',nargs='+',type=int)
    ap.add_argument('--percentages',nargs='+',default=[100,75,50],type=int)
    args=ap.parse_args()
    for d in args.dimensions:
        print(json.dumps(scan(d,args.percentages)),flush=True)
