"""Inert-prime elliptic Chabauty tangent at r=1 over Q(sqrt(3))."""

def tangent(p):
    m=p*p
    def elt(a,b=0):
        return a%m,b%m
    def add(u,v):
        return elt(u[0]+v[0],u[1]+v[1])
    def neg(u):
        return elt(-u[0],-u[1])
    def sub(u,v):
        return add(u,neg(v))
    def mul(u,v):
        return elt(u[0]*v[0]+3*u[1]*v[1],u[0]*v[1]+u[1]*v[0])
    def div(u,v):
        norm=v[0]**2-3*v[1]**2
        return mul(mul(u,elt(v[0],-v[1])),elt(pow(norm,-1,m)))
    def zero(u):
        return all(a%p==0 for a in u)
    A=elt(288,144)
    D=(elt(21,12),elt(-153,-90))
    xd,yd=D
    assert mul(yd,yd)==mul(xd,add(mul(xd,xd),A))
    if zero(yd):
        return
    x,y=D
    for k in range(1,(p+1)**2+1):
        if k==1:
            slope=div(add(mul(elt(3),mul(x,x)),A),mul(elt(2),y))
        else:
            h=sub(x,xd)
            u=sub(y,yd)
            if zero(h):
                assert not zero(u)
                t=div(h,u)
                assert zero(t)
                return k+1,(x,y),t,tuple(a//p for a in t)
            slope=div(u,h)
        xnew=sub(sub(mul(slope,slope),x),xd)
        ynew=sub(mul(slope,sub(x,xnew)),y)
        x,y=xnew,ynew
    raise ValueError('exceeded the Hasse bound')

if __name__=='__main__':
    witness=tangent(5)
    assert witness==(4,((21,17),(18,0)),(0,5),(0,1))
    print("inert prime 5:",witness)
