"""Exhaustively certify the minimum coefficient 1-norm in the small conic lattices."""
import json
from collections import Counter
from math import gcd,prod
from flint import arb,fmpz
from abc_conic_short_kernel import parameters,cyclic_logs,vector

def half_ball(logs,indices,bound):
    mod=[n for n,_ in logs]
    def walk(i,left,z,tags):
        if i==len(indices):
            yield tuple(tags),tuple(z),bound-left
            return
        coeff=[L[indices[i]] for _,L in logs]
        for a in range(-left,left+1):
            yield from walk(i+1,left-abs(a),z+[a],
                            [(x+a*l)%n for x,l,n in zip(tags,coeff,mod)])
    yield from walk(0,bound,[],[0]*len(logs))

def exact_min(data,upper):
    ell,eta,D,M,k,t,exps,H=data
    logs=[cyclic_logs(p,j,eta) for p,j in exps.items()]
    d=len(ell)
    table={}
    counts=[0,0]
    for tag,z,n in half_ball(logs,list(range(d//2)),upper):
        # Separate zero and nonzero halves with the identity tag.
        key=(tag,any(z))
        if key not in table or table[key][0]>n:table[key]=(n,[z])
        elif table[key][0]==n:table[key][1].append(z)
        counts[0]+=1
    best=upper
    vectors=set()
    for tag,z,n in half_ball(logs,list(range(d//2,d)),upper):
        counts[1]+=1
        opposite=tuple((-x)%m for x,(m,_) in zip(tag,logs))
        for active in (True,False):
            found=table.get((opposite,active))
            if not found or (not active and n==0):continue
            total=n+found[0]
            if total>best:continue
            if total<best:vectors.clear();best=total
            for v in found[1]:
                x=v+z
                vectors.add(x if next(i for i in x if i)>0 else tuple(-i for i in x))
    return best,sorted(vectors),counts

def integer_triple(data,z):
    ell,eta,D,M,k,t,exps,H=data
    def mult(v,w):
        b,a=v;c,f=w
        return b*c+2*a*f,b*f+a*c
    h=(1,0)
    for (b,a),v in zip(eta,z):
        power=(b,a if v>0 else -a)
        e=abs(v)
        while e:
            if e&1:h=mult(h,power)
            power=mult(power,power)
            e//=2
    b,a=h
    assert gcd(b,a)==1 and a%M==0
    S=b*b+2*a*a
    J=abs(b*b-2*a*a)
    w,u,v=S,J,2*abs(a*b)
    A,B,C=u*u,2*v*v,w*w
    assert A+B==C and gcd(A,B)==1
    fac={}
    for value in (2,J,abs(a),abs(b),S):
        fs=fmpz(value).factor()
        assert prod(p**e for p,e in fs)==value and all(p.is_prime() for p,_ in fs)
        for p,e in fs:fac[int(p)]=1
    rad=prod(fac)
    return dict(b=b,a=a,J=J,S=S,C=C,rad_ABC=rad,actual_gain=float((arb(C)/rad).log()),
                quality=float(arb(C).log()/arb(rad).log()))

if __name__=='__main__':
    for d,upper in [(4,4),(5,8),(6,16),(7,15),(8,21)]:
        data=parameters(d)
        best,zs,counts=exact_min(data,upper)
        assert zs and best<=upper
        reports=[]
        for z in zs:
            r=vector(data,list(z))
            r.update(integer_triple(data,z))
            reports.append(r)
        print(json.dumps(dict(d=d,upper=upper,best=best,visits=counts,reports=reports)),flush=True)
