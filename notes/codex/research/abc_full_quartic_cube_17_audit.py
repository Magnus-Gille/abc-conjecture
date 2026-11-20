"""Independent whole-group-image and p-adic audit for the split prime 17."""
from itertools import product
try:
    from cypari import pari
except ImportError:
    from cypari2 import Pari
    pari = Pari()

p = 17
roots = [x for x in range(p) if (x**3-3*x-1)%p == 0]
curves = [pari.ellinit([0,0,0,-36*t*t,0],p) for t in roots]


def residue_point(P):
    if len(P) == 1:
        return None
    return tuple(int(pari.lift(c))%p for c in P)


def point_list(E):
    return [None] + [(x,y) for x,y in product(range(p),repeat=2) if pari.ellisoncurve(E,[x,y])]


def local_tables(E):
    points = point_list(E)
    index = {pt:i for i,pt in enumerate(points)}
    def as_pari(pt): return [0] if pt is None else list(pt)
    addition = [[index[residue_point(pari.elladd(E,as_pari(U),as_pari(V)))] for U in points] for V in points]
    return points, index, addition


def main():
    assert roots == [3,4,10]
    lists, indices, table = zip(*(local_tables(E) for E in curves))
    def add(U,V): return tuple(table[i][u][v] for i,(u,v) in enumerate(zip(U,V)))
    def encode(pts): return tuple(t[pt] for t,pt in zip(indices,pts))
    O=(0,0,0)
    torsion=[O]+[encode([((k*6*th)%p,0) for th in roots]) for k in (0,1,-1)]
    lambdas=[-3*pow(2*th+1,-1,p)%p for th in roots]
    D=encode([(12,-12*th*l%p) for th,l in zip(roots,lambdas)])
    permitted=set()
    for U in product(*(range(len(pts)) for pts in lists)):
        group=set()
        point=O
        while point not in group:
            group.update(add(point,T) for T in torsion)
            point=add(point,U)
        if D in group: permitted.update(group)
    candidates=[]
    for t in [None,*range(p)]:
        options=[]
        for i,(th,l) in enumerate(zip(roots,lambdas)):
            if t is None:
                options.append((torsion[1][i],add(D,torsion[1])[i]));continue
            if t == 0:
                options.append((O[i],D[i]));continue
            ff=(1+4*l*t-18*t*t-12*l*t**3+9*t**4)%p
            opt=[]
            for v in range(p):
                if v*v%p!=ff:continue
                x0=(2*(v+1)+4*l*t)*pow(t*t,-1,p)%p
                y0=((x0*x0-36)*t-4*l*x0+24*l)*pow(2,-1,p)%p
                pt=((x0-6)*th**2*pow(4,-1,p)%p,y0*th**3*pow(8,-1,p)%p)
                opt.append(indices[i][pt])
            options.append(opt)
        candidates.extend((t,Q) for Q in product(*options) if Q in permitted)
    assert set(candidates)=={(0,O),(0,D),(None,torsion[1]),(None,add(D,torsion[1]))}
    print('local sizes',list(map(len,lists)),'allowed group union',len(permitted),'surviving slope/point pairs',candidates)
    theta_local=pari.polrootspadic('x^3-3*x-1',p,12)
    data=[]
    for th in theta_local:
        lift=lambda x,mod: int(pari.lift(x))%mod
        theta=lift(th,p)
        l=-3/(2*th+1)
        E=pari.ellinit([0,0,0,-36*th**2,0*th]); P=[12*th**0,-12*th*l]
        r=int(pari.ellorder(curves[roots.index(theta)],[12,-12*theta*lambdas[roots.index(theta)]]))
        x,y=pari.ellmul(E,P,20)
        z=-x/y
        assert int(pari.valuation(z,p))==1
        data.append((theta,lift(th,p*p),r,lift(-th*z/p,p)))
    assert sorted(data)==[(3,207,4,11),(4,157,10,13),(10,214,4,7)]
    print('theta mod17, theta mod289, order(D), -theta*z(20D)/17 mod17:',sorted(data))


if __name__=='__main__':main()
