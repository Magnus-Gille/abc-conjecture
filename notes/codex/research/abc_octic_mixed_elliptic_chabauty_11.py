"""Exact local elliptic Chabauty certificate in the unramified quartic at 11.

Elements of (Z/nZ)[t]/(t^4-2t^2-1) use the coefficient basis 1,t,t²,t³.
Only n=11 and n=121 are needed. Row vectors are coefficients in this basis.
"""
from functools import lru_cache
from itertools import product
P = 11
GROUP = 14596

class R:
 __slots__=('c','n')
 def __init__(self,c,n):
  self.n=n
  self.c=tuple(x%n for x in ((c,0,0,0) if type(c)==int else c))
 def __add__(self,b):
  if type(b)==int:b=R(b,self.n)
  return R(tuple(x+y for x,y in zip(self.c,b.c)),self.n)
 __radd__=__add__
 def __neg__(self):return R(tuple(-x for x in self.c),self.n)
 def __sub__(self,b):return self+(-b)
 def __rsub__(self,b):return b+(-self)
 def __mul__(self,b):
  if type(b)==int:return R(tuple(b*x for x in self.c),self.n)
  a0,a1,a2,a3=self.c;b0,b1,b2,b3=b.c
  w4=a1*b3+a2*b2+a3*b1;w5=a2*b3+a3*b2;w6=a3*b3
  return R((a0*b0+w4+2*w6,a0*b1+a1*b0+w5,a0*b2+a1*b1+a2*b0+2*w4+5*w6,a0*b3+a1*b2+a2*b1+a3*b0+2*w5),self.n)
 __rmul__=__mul__
 def __pow__(self,k):
  if k<0:return self.inv()**(-k)
  b=self;a=R(1,self.n)
  while k:
   if k&1:a=a*b
   k//=2
   if k:b=b*b
  return a
 def inv(self):
  if not any(x%P for x in self.c):raise ValueError(('nonunit',self.c))
  if not any(self.c[1:]):return R(pow(self.c[0],-1,self.n),self.n)
  v=(self.red(P)**(P**4-2)).red(self.n);j=P
  while j<self.n:
   v=v*(2-self*v);j*=j
  return v
 def __truediv__(self,b):
  return self*(b.inv() if isinstance(b,R) else pow(b,-1,self.n))
 def __rtruediv__(self,b):return b*self.inv()
 def __eq__(self,b):
  if type(b)==int:return self.c==(b%self.n,0,0,0)
  return self.c==b.c if isinstance(b,R) else False
 def red(self,n):return R(self.c,n)
 def __repr__(self):return str(self.c)

def pars(n):
 t=R((0,1,0,0),n)
 b=-2*(1+t);g=4*t**3+2*t**2-8*t+2;h=-12*t**3-4*t**2+28*t+4;a=1+t**3-2*t # t^{-1}=t^3-2t
 return t,b,g,h,a,-a*(1+t*t),a*a*t*t

def sqrtff(x):
 n=x.n;assert n==P
 if x==0:return x
 L=P**4-1
 if x**(L//2)!=1:return None
 odd=L;v=0
 while odd%2==0:odd//=2;v+=1
 for i in range(P):
  for j in range(1,P):
   ns=R((i,j,0,0),P)
   if ns**(L//2)==-1:break
  else:continue
  break
 else:raise ValueError('nonsquare')
 a=ns**odd;b=x**odd;y=x**((odd+1)//2);m=v
 while b!=1:
  i=1;v0=b*b
  while v0!=1:i+=1;v0=v0*v0
  f=a**(2**(m-i-1));y=y*f;a=f*f;b=b*a;m=i
 assert y*y==x
 return y

def sqrtlift(x):
 y=sqrtff(x.red(P))
 if y is None:return None
 if y==0:raise ValueError('zero root')
 y=y.red(x.n);j=P
 while j<x.n:y=(y+x/y)/2;j=j*j
 assert y*y==x
 return y

def affadd(A,B,c2,c4):
 if A is None:return B
 if B is None:return A
 x,y=A;u,v=B
 if x==u:
  if y==-v:return None
  h=(3*x*x+2*c2*x+c4)/(2*y)
 else:h=(v-y)/(u-x)
 z=h*h-c2-x-u
 return z,h*(x-z)-y

def amul(k,A,c2,c4):
 a=None;b=A
 while k:
  if k&1:a=affadd(a,b,c2,c4)
  k//=2
  if k:b=affadd(b,b,c2,c4)
 return a

@lru_cache(None)
def order(x,y):
 q=(R(x,P),R(y,P))
 c2,c4=pars(P)[-2:]
 ds=GROUP;r=GROUP;f=2
 while ds>1:
  if f*f>ds:f=ds
  while ds%f==0:
   ds//=f
   if r%f==0 and amul(r//f,q,c2,c4) is None:r//=f
  f+=1
 assert amul(r,q,c2,c4) is None
 return r

def logvec(Q):
 bx,by=Q;n=bx.n;c2,c4=pars(n)[-2:]
 assert by*by==bx**3+c2*bx*bx+c4*bx,('offcurve',Q)
 r=order(bx.red(P).c,by.red(P).c)
 x,y,z=bx,by,R(1,n)
 for bit in bin(r)[3:]:
  zz=z*z;yy=y*y
  s=4*x*yy;m=3*x*x+2*c2*x*zz+c4*zz*zz
  nz=2*y*z
  nx=m*m-2*s-c2*nz*nz
  x,y,z=nx,m*(s-nx)-8*yy*yy,nz
  if bit=='1':
   zz=z*z;h=bx*zz-x;k=by*z*zz-y
   hh=h*h;hhh=h*hh;v=x*hh;nz=z*h
   nx=k*k-hhh-2*v-c2*nz*nz
   x,y,z=nx,k*(v-nx)-y*hhh,nz
 assert not any(c%P for c in z.c)
 param=-x*z/y
 # Here log_formal(z) = z modulo 121 for z in the formal subgroup.
 assert P>=5
 return (param*(GROUP//r))

def quartic(z,W):
 t,b,g,h,a,c2,c4=pars(z.n);U=2*(W+z*z+b*z+g);V=2*U*z+b*U-2*h
 return (U+4*(1+t)**2)/16,V/64

def Bpoly(z):
 t=pars(z.n)[0]
 return z*z-4*(1+t)*z+8*(t**3+t*t-t)

def rowspace(rows,p):
 a=[list(x) for x in rows];z=0
 for c in range(4):
  y=next((i for i in range(z,len(a)) if a[i][c]%p),None)
  if y is None:continue
  a[z],a[y]=a[y],a[z];v=pow(a[z][c],-1,p);a[z]=[x*v%p for x in a[z]]
  for i in range(len(a)):
   if i!=z:a[i]=[(u-a[i][c]*v)%p for u,v in zip(a[i],a[z])]
  z+=1
 return tuple(tuple(r) for r in a if any(r))

def run():
 p=P
 # t^(11^4)=t rules out repeated factors and irreducible degrees other
 # than 1,2,4. The next check then rules out a decomposition in degrees 1,2.
 tf=R((0,1,0,0),P)
 assert tf**(P**4)==tf and tf**(P**2)!=tf
 ff=[R(c,P) for c in product(range(P),repeat=4)]
 squares={(v*v).c for v in ff}
 c2,c4=pars(P)[-2:]
 cardinality=1
 for x in ff:
  rhs=x*(x*x+c2*x+c4)
  cardinality+=1 if rhs==0 else 2*int(rhs.c in squares)
 assert cardinality==GROUP
 print('finite residue group order',cardinality)
 n=P**2;t,b,g,h,a,c2,c4=pars(n)
 Pinf=((1+t)**2/4,h/32)
 Pm=((2*t**3+5*t**2+2*t+2)/4,(-5*t**3-11*t*t-8*t-5)/8)
 rows=lambda q:tuple(z//P for z in logvec(q).c)
 span=rowspace([rows(Pinf),rows(Pm)],P)
 print('span',p,span,flush=True)
 assert span==((1,0,0,9),(0,1,7,10))
 def test(Q):return len(rowspace(list(span)+[rows(Q)],P))==2
 def F(z):return (z*z-4*z-8)**2+16*z*z
 squares={j*j%P for j in range(P)}
 # For z near infinity use r=1/z and the nonsingular negative branch:
 # W=z²*(-sqrt(1+...) ); rationalize U so no division by r.
 results={}
 for z0 in list(range(P))+[None]:
  survivors=[]
  rrlist=[]
  if z0 is None:
   for k in range(P):
    rr=R(P*k,n)
    ww=sqrtlift((1+8*rr*rr)*(1-4*(1+t)*rr+8*(t**3+t*t-t)*rr*rr))
    if ww.red(P)!=1:ww=-ww
    # (z²+bz+g)^2 − H(z) = 2h z + g² − H(0).
    H0=64*(t**3+t*t-t)
    den=(1+b*rr+g*rr*rr)+ww
    U_over_r=2*(2*h+(g*g-H0)*rr)/den
    U=rr*U_over_r;V=2*U_over_r+b*U-2*h
    Q=(U+4*(1+t)**2)/16,V/64
    rrlist.append(rows(Q))
    if test(Q):survivors.append(k)
  elif (z0*z0+8)%P==0:
   if F(z0)%P not in squares:continue
   for k in range(P):
    vs=R(P*k,n)
    z=sqrtlift(vs*vs-8)
    if z.red(P)!=z0:z=-z
    B=sqrtlift(Bpoly(z))
    if B is None:continue
    rrlist.append(rows(quartic(z,vs*B)))
    if test(quartic(z,vs*B)):survivors.append(k)
  else:
   if (z0*z0+8)%P not in squares or F(z0)%P not in squares:continue
   for k in range(P):
    z=R(z0+P*k,n)
    W=sqrtlift((z*z+8)*Bpoly(z))
    if W is None:continue
    rrlist.append(rows(quartic(z,W)))
    if test(quartic(z,W)):survivors.append(k)
  if rrlist:
   a,c=rrlist[:2];d=[(j-i)%p for i,j in zip(a,c)]
   project=lambda v:((v[2]-7*v[1])%p,(v[3]-9*v[0]-10*v[1])%p)
   for k,vector in enumerate(rrlist):
    assert project(vector)==tuple((i+k*j)%p for i,j in zip(project(a),project(d)))
   print('disc',z0,'projected constant',project(a),'linear',project(d),'survivors',survivors)
   results[z0]=(project(a),project(d),survivors)
 assert results=={1:((6,8),(2,5),[]),6:((0,0),(3,9),[0]),
                  9:((6,10),(3,2),[]),10:((8,9),(8,9),[10]),
                  None:((0,0),(0,7),[0])}
if __name__=='__main__':
 run()
