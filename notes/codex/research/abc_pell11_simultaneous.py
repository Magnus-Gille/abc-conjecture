"""Enumerate two simultaneous exact square primes using the archived first indices."""
from argparse import ArgumentParser
from csv import DictReader
from pathlib import Path

from abc_pell11_early_squares import full_form
from abc_pell11_square_periods import factor_at, parameter_coefficients, root_indices


def collisions(bound):
    archive=Path(__file__).with_name('abc_pell11_square_periods.csv')
    coeff,content=full_form()
    params=parameter_coefficients(coeff,content)
    coeff=list(map(int,coeff))
    seen={}
    hits={}
    eligible=0
    with archive.open() as handle:
        for row in DictReader(handle):
            first=int(row['first_exact_square'])
            if not 0<first<=bound:
                continue
            eligible+=1
            p,m=int(row['p']),int(row['projective_period'])
            for r in root_indices(params,p,m):
                u=factor_at(r,coeff,p*p)
                v=factor_at(r+m,coeff,p*p)
                j=(-u//p)*pow((v-u)//p,-1,p)%p
                residue=r+m*j
                period=p*m
                for n in range(residue or period,bound+1,period):
                    previous=seen.setdefault(n,p)
                    if previous!=p:
                        hits.setdefault(n,{previous}).add(p)
    exact=[]
    for n,ps in hits.items():
        ps=[p for p in sorted(ps) if factor_at(n,coeff,p**3)!=0]
        if len(ps)>=2:
            exact.append((n,ps))
    print('index bound, eligible primes, distinct candidate indices, exact collisions',
          bound,eligible,len(seen),len(exact))
    for n,ps in sorted(exact)[:10]:
        print(n,ps,[factor_at(n,coeff,p**3)//(p*p) for p in ps])


if __name__=='__main__':
    parser=ArgumentParser(description=__doc__)
    parser.add_argument('bound',type=int,nargs='?',default=200000000)
    collisions(parser.parse_args().bound)
