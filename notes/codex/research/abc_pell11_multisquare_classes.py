"""Lift all visited Pell parameter classes to square divisibility."""
import argparse
import csv
import multiprocessing
from pathlib import Path

from abc_pell11_early_squares import full_form
from abc_pell11_square_periods import factor_at, parameter_coefficients, root_indices

def setup():
    global coeffs, params
    coeffs, content=full_form()
    params=parameter_coefficients(coeffs,content)
    coeffs=list(map(int,coeffs))

def lift(row):
    p,m,k=map(int,(row['p'],row['projective_period'],row['root_classes']))
    roots=root_indices(params,p,m)
    assert len(roots)==k
    mod=p*p
    res=[]
    for r in roots:
        u=factor_at(r,coeffs,mod)
        v=factor_at(r+m,coeffs,mod)
        assert u%p==v%p==0
        j=(-u//p)*pow((v-u)//p,-1,p)%p
        res.append(r+j*m)
    return ' '.join(map(str,[p,m]+sorted(res)))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workers',type=int,default=2)
    parser.add_argument('--bound',type=int)
    args=parser.parse_args()
    with Path(__file__).with_name('abc_pell11_square_periods.csv').open() as f:
        rows=[r for r in csv.DictReader(f) if int(r['root_classes'])>0]
    rows.sort(key=lambda r:int(r['first_exact_square']))
    if args.bound:
        rows=[r for r in rows if int(r['first_exact_square'])<=args.bound]
    with multiprocessing.Pool(args.workers,initializer=setup) as pool:
        for row in pool.imap(lift,rows,chunksize=4):
            print(row,flush=True)
