"""Exact least Pell indices of full exponent two by projective periods and Hensel lifting."""
from argparse import ArgumentParser
from math import isqrt, log
from flint import fmpz_poly, nmod_poly
from abc_cm_pell_whole_triple import evaluate, pell
from abc_pell11_early_squares import compatible_primes, full_form


def parameter_coefficients(coeff, content):
    s=fmpz_poly([1,0,2])
    x=-8*fmpz_poly([1,2,2])
    form=fmpz_poly([coeff[0]])
    power=fmpz_poly([1])
    for c in coeff[1:]:
        power*=s
        form=form*x+c*power
    assert form.content()==content
    return [int(c) for c in form//content]


def prime_factors(n):
    i=2
    while i*i<=n:
        if n%i==0:
            yield i
            while n%i==0:
                n//=i
        i+=1
    if n>1:
        yield n


def projective_order(p):
    # The split or nonsplit projective torus has order p-(2/p).
    m=p-(1 if p%8 in (1,7) else -1)
    for ell in list(prime_factors(m)):
        while m%ell==0 and pell(m//ell,p)[1]==0:
            m//=ell
    assert pell(m,p)[1]==0
    return m


def root_indices(coefficients,p,m):
    param=nmod_poly(coefficients,p)
    roots=param.roots()
    assert all(e==1 for k,e in roots)
    zs=[]
    for k,e in roots:
        k=int(k)
        v=pow(1-2*k*k,-1,p)
        zs.append(((1+2*k*k)*v%p,2*k*v%p))
    if param.degree()<100:
        zs.append((p-1,0))
    assert len(zs)==100
    # Projectivization as z=(b+a*sqrt(2))/(b-a*sqrt(2)). At epsilon, z=-3-2*sqrt(2).
    width=isqrt(m)+1
    table={}
    B,A=1,0
    for j in range(width):
        table[B*p+A]=j
        B,A=(-3*B-4*A)%p,(-2*B-3*A)%p
    V,W=B,-A
    indices=[]
    for B,A in zs:
        for j in range((m+width-1)//width):
            i=table.get(B*p+A)
            if i is not None:
                indices.append((j*width+i)%m)
                break
            B,A=(V*B+2*W*A)%p,(W*B+V*A)%p
    assert len(set(indices))==len(indices)
    return sorted(indices)


def factor_at(n,coeff,power):
    b,a=pell(n,power)
    s=(b*b+2*a*a)%power
    x=-8*(s+2*a*b)*pow(s,-1,power)%power
    return evaluate(coeff,x,power)


def least_square(p,coeff,params):
    m=projective_order(p)
    roots=root_indices(params,p,m)
    if not roots:
        return m,0,0,0,0
    # Nontrivial first lift of epsilon has been checked for every prime in the census.
    assert pell(m,p*p)[1]%p**2!=0,(p,'Pell-Wieferich')
    best=None
    for r in roots:
        first=factor_at(r,coeff,p*p)
        second=factor_at(r+m,coeff,p*p)
        assert first%p==second%p==0
        j=(-first//p)*pow((second-first)//p,-1,p)%p
        n=r+j*m
        if not n:
            n+=m*p
        if best is not None and n>=best:
            continue
        deep=factor_at(n,coeff,p**3)
        assert deep%p**2==0
        if not deep:
            n+=m*p
            deep=factor_at(n,coeff,p**3)
            assert deep and deep%p**2==0
        if best is None or n<best:
            best=n
            residue=deep//(p*p)
    return m,len(roots),best,residue, min(roots)


if __name__=='__main__':
    parser=ArgumentParser(description=__doc__)
    parser.add_argument('bound',type=int,nargs='?',default=100000)
    args=parser.parse_args()
    coeff,content=full_form()
    params=parameter_coefficients(coeff,content)
    coeff=list(map(int,coeff))
    print('p,projective_period,root_classes,first_exact_square,quotient_mod_p,least_root')
    for p in compatible_primes(args.bound):
        row=least_square(p,coeff,params)
        print(','.join(map(str,(p,)+row)),flush=True)
