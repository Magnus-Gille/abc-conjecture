"""All odd square classes of u^2+336u+576 on y^2=u^3-576u at Q=(-8,-64)."""
import argparse,csv,sys
from functools import cache
from math import gcd,isqrt,lcm
from abc_eisenstein_twelfth_first_squares import prime_data

def root_int(a,p):
    a%=p
    if a==0:return 0
    if pow(a,(p-1)//2,p)!=1:return None
    if p%4==3:return pow(a,(p+1)//4,p)
    d=p-1;s=0
    while d%2==0:d//=2;s+=1
    z=2
    while pow(z,(p-1)//2,p)==1:z+=1
    c=pow(z,d,p);x=pow(a,(d+1)//2,p);v=pow(a,d,p)
    while v!=1:
        i=1;u=v*v%p
        while u!=1:u=u*u%p;i+=1
        b=pow(c,1<<(s-i-1),p)
        x=x*b%p;c=b*b%p;v=v*c%p;s=i
    assert x*x%p==a
    return x

def ec_add(A,B,p):
    if A is None:return B
    if B is None:return A
    x,y=A
    u,v=B
    if x==u:
        if (y+v)%p==0:return None
        slope=(3*x*x-576)*pow(2*y,-1,p)%p
    else:slope=(y-v)*pow(x-u,-1,p)%p
    x1=(slope*slope-x-u)%p
    return x1,(slope*(x-x1)-y)%p

def times(n,P,p):
    R=None
    while n:
        if n&1:R=ec_add(R,P,p)
        P=ec_add(P,P,p);n//=2
    return R

def prime_factors(N):
    f=2
    while f*f<=N:
        if N%f==0:
            yield f
            while N%f==0:N//=f
        f+=1 if f==2 else 2
    if N>1:yield N

def visit(p,odd_part):
    root=root_int(3,p)
    if root is None:return None,[]
    xs=[(-168+sgn*96*root)%p for sgn in [-1,1]]
    targets=[]
    for x in xs:
        y=root_int(x*(x*x-576),p)
        if y is not None:
            assert y and (x*x+336*x+576)%p==0
            targets.append((x,y))
    if not targets:return None,[]
    N=p+1
    if p%4==1:
        chi=1 if pow(24,(p-1)//2,p)==1 else -1
        N-=2*odd_part[p]*chi
    Q=(-8%p,-64%p)
    assert times(N,Q,p) is None
    r=N
    for f in prime_factors(N):
        while r%f==0 and times(r//f,Q,p) is None:r//=f
    width=isqrt(r)+1
    baby={}
    S=None
    for j in range(width):
        baby[S]=j;S=ec_add(S,Q,p)
    step=(S[0],-S[1]%p) if S else None
    hits=set()
    for S in targets:
        for k in range((r+width-1)//width):
            if S in baby:
                n=(width*k+baby[S])%r
                for h in (n,(-n)%r):
                    if h%2:hits.add(h)
                    elif r%2:hits.add(h+r)
                break
            S=ec_add(S,step,p)
    return r,sorted(hits)

def poly_value(n,mod):
    two_y=-128
    inverse=pow(two_y,-1,mod)
    initial=(0,1,two_y,-540672,-18790481920)
    @cache
    def psi(k):
        if k<5:return initial[k]%mod
        m=k//2
        if k%2:return (psi(m+2)*pow(psi(m),3,mod)-psi(m-1)*pow(psi(m+1),3,mod))%mod
        return (psi(m)*inverse*(psi(m+2)*psi(m-1)**2-psi(m-2)*psi(m+1)**2))%mod
    u=(-8-psi(n-1)*psi(n+1)*pow(psi(n),-2,mod))%mod
    return (u*u+336*u+576)%mod

def scan(bound):
    primes,odd_part=prime_data(bound)
    writer=csv.writer(sys.stdout,lineterminator='\n')
    writer.writerow(['p','r','odd_period','h','square_index','square_period','J_over_p2_mod_p'])
    checked=roots=lifted=deep=0
    for p in range(5,bound+1,2):
        if not primes[p]:continue
        checked+=1
        r,odds=visit(p,odd_part)
        for h in odds:
            period=lcm(2,r)
            a=poly_value(h,p*p)
            b=poly_value(h+period,p*p)
            assert a%p==b%p==0
            slope=(b-a)//p%p
            roots+=1
            if not slope:
                if a:continue
                n=h;step=period;deep+=1
            else:
                k=-(a//p)*pow(slope,-1,p)%p
                n=h+k*period;step=period*p
            v=poly_value(n,p**3)
            assert v%(p*p)==0
            lifted+=1
            writer.writerow([p,r,period,h,n,step,v//(p*p)])
    print('bound,good primes,odd roots,square classes,flat square classes',
          bound,checked,roots,lifted,deep,file=sys.stderr)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('bound',type=int,nargs='?',default=100000)
    scan(parser.parse_args().bound)
