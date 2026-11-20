"""Verify the two-isogeny sieve at 2 and elliptic Chabauty arithmetic at 19."""
from itertools import product

def dyadic_descent():
    m = 32
    def enc(a, b=0, c=0):
        return a % m + m * (b % m + m * (c % m))
    coeff = [(z % m, z // m % m, z // (m*m)) for z in range(m**3)]
    def add(x, y):
        a,b,c = coeff[x]; A,B,C = coeff[y]
        return enc(a+A,b+B,c+C)
    def mul(x, y):
        a,b,c = coeff[x]; A,B,C = coeff[y]
        u = b*C + c*B
        v = c*C
        return enc(a*A-u, a*B+b*A+3*u-v, a*C+b*B+c*A+3*v)
    squares = {mul(z,z) for z in range(m**3)}
    fourths = {mul(z,z) for z in squares}
    nonunit_fourths = {mul(z,z) for z in squares if all(a % 2 == 0 for a in coeff[z])}
    B = enc(0,0,-36)
    generators = [enc(-1),enc(0,1),enc(-1,1),enc(2),enc(1,1)]
    classes = []
    for bits in product((0,1),repeat=5):
        e = enc(1)
        for bit,gen in zip(bits,generators):
            if bit: e=mul(e,gen)
        e2=mul(e,e)
        lhs={mul(e,z) for z in squares}
        if (any(add(mul(e2,z),B) in lhs for z in fourths)
                or any(add(e2,mul(B,z)) in lhs for z in nonunit_fourths)):
            classes.append(''.join(map(str,bits)))
    assert classes == ['00000','00011','01001','01010','10000','10011','11001','11010']
    print("Dyadic candidate classes",classes)


def add_affine(P,Q,b,p):
    if P is None: return Q
    if Q is None: return P
    x,y=P; u,v=Q
    if x==u:
        if (y+v)%p==0: return None
        m=(3*x*x+b)*pow(2*y,-1,p)
    else:
        m=(y-v)*pow(x-u,-1,p)
    xx=(m*m-x-u)%p
    return xx,(m*(x-xx)-y)%p


def jac_double(point,b,m):
    x,y,z=point
    h=4*x*y*y; s=3*x*x+b*z**4
    xx=s*s-2*h
    return xx%m, (s*(h-xx)-8*y**4)%m, 2*y*z%m


def jac_add_affine(point,Q,m):
    x,y,z=point; u,v=Q
    h=u*z*z-x;k=v*z**3-y
    xx=k*k-h**3-2*x*h*h
    return xx%m,(k*(x*h*h-xx)-y*h**3)%m,z*h%m


def split_local():
    p=19; m=p*p
    roots=[t for t in range(m) if (t**3-3*t+1)%m==0]
    roots.sort(key=lambda t:t%p)
    assert roots==[288,273,161]
    tables=[];leading=[]
    for t in roots:
        k=(4-2*t*t-t)%m; b=-36*t*t%m
        d=(12,-12*k%m)
        assert (d[1]**2-d[0]**3-b*d[0])%m==0
        two=jac_double((*d,1),b,m)
        four=jac_double(two,b,m)
        five=jac_add_affine(four,d,m)
        x,y,z=jac_double(five,b,m)
        assert (y*y-x**3-b*x*z**4)%m==0 and y%p!=0 and z%p==0
        parameter=-x*z*pow(y,-1,m)%m
        leading.append((parameter//p,(-t*parameter//p)%p))
        t%=p;k%=p;b%=p;D=(12,d[1]%p)
        points=[None]
        while True:
            Q=add_affine(points[-1],D,b,p)
            if Q is None: break
            points.append(Q)
        assert len(points)==10
        assert 1+sum((y*y-x**3-b*x)%p==0 for x in range(p) for y in range(p))==20
        def slope(Q):
            if Q is None or Q==D: return p
            x,y=Q
            if x==12: return (12+3*t*t)*pow(2*k*t,-1,p)%p
            return (y-k*x)*pow(t*(x-12),-1,p)%p
        tors=[None,(0,0),(6*t%p,0),(-6*t%p,0)]
        tables.append([[slope(add_affine(Q,T,b,p)) for Q in points] for T in tors])
    assert leading==[(9,11),(12,11),(14,7)]
    hits=[]
    for j in range(4):
        for n in range(10):
            r=[table[j][n] for table in tables]
            if len(set(r))==1: hits.append((j,n,r[0]))
    assert hits==[(0,0,p),(0,1,p),(1,0,0),(1,1,0)]
    print("Common-slope cells (torsion, multiplier, slope; 19 represents infinity)",hits)
    print("Formal parameters and reciprocal-slope leading terms modulo 19",leading)

if __name__=='__main__':
    dyadic_descent()
    split_local()
