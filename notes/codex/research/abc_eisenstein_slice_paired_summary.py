"""Verify the paired-quartic census and enumerate early simultaneous indices."""
import csv,sys
from collections import Counter,defaultdict
from abc_eisenstein_slice_paired_quartic import poly_value

rows=[tuple(map(int,x.values())) for x in csv.DictReader(open(sys.argv[1]))]
sizes=Counter(p for p,*_ in rows)
print('visited primes, classes, classes per prime',len(sizes),len(rows),sorted(Counter(sizes.values()).items()))
assert all(n>h and q and 0<h<=T and 0<n<=T*p and M==T*p and (n-h)%T==0
           for p,r,T,h,n,M,q in rows)
print('first five prime/index pairs',[(p,n) for p,r,T,h,n,M,q in sorted(rows,key=lambda v:v[4])[:5]])
print('classes by prime mod 24',sorted(Counter(p%24 for p in sizes).items()))
bound=10**8
seen={};collisions=defaultdict(set)
for p,r,T,h,n,M,q in rows:
    for j in range(n,bound+1,M):
        if j in seen:collisions[j].update((p,seen[j]))
        else:seen[j]=p
print('bound, distinct indices, collisions',bound,len(seen),len(collisions))
for j,ps in sorted(collisions.items())[:5]:
    print('collision',j,[(p,poly_value(j,p**3)//p**2) for p in sorted(ps)])
