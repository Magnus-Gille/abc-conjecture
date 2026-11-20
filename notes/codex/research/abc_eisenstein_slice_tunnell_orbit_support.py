"""Split the all-prime Tunnell census by the three-primary restrictions on visiting classes."""
import csv
import gzip
import json
from collections import Counter, defaultdict
from pathlib import Path

HERE=Path(__file__).resolve().parent
LIMIT=10**6


def squarefree_products(primes):
    vals=[1]
    for p in primes:
        vals.extend([p*b for b in vals if p*b<=LIMIT])
    return set(vals)


def main():
    visits=defaultdict(list)
    with (HERE/'abc_eisenstein_slice_paired_quartic_1m.csv').open() as f:
        for row in csv.DictReader(f):
            visits[int(row['p'])].append((int(row['r']),int(row['h'])))
    prime_groups={
        'visited':set(visits),
        'visited_index_prime_to_3':{p for p,hs in visits.items() if any(r%3 or h%3 for r,h in hs)},
        'visited_index_divisible_by_3':{p for p,hs in visits.items() if any(r%3 or h%3==0 for r,h in hs)},
        'visited_reduction_order_prime_to_3':{p for p,hs in visits.items() if hs[0][0]%3}
    }
    square_groups={key:squarefree_products(sorted(primes)) for key,primes in prime_groups.items()}
    counts=defaultdict(Counter)
    table=HERE/'abc_eisenstein_slice_tunnell.tsv.gz'
    with gzip.open(table,'rt') as f:
        for row in csv.DictReader(f,delimiter='\t'):
            b=int(row['b'])
            for name,values in square_groups.items():
                if b not in values:
                    continue
                for label in ([name+'_all',name+'_primes'] if int(row['omega'])==1 else [name+'_all']):
                    s=counts[label]
                    s['number']+=1
                    s['3b']+=int(row['delta_3b'])==0
                    s['6b']+=int(row['delta_6b'])==0
                    s['both']+=int(row['delta_3b'])==int(row['delta_6b'])==0
                    s['nontrivial_split']+=int(row['nontrivial'])>0
                    s['three_way']+=int(row['three_way'])>0
                    s['three_way_real_symbols']+=int(row['three_way_real_symbols'])>0
    out={'limit':LIMIT,'counts':counts}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out))


if __name__=='__main__':
    main()
