"""Summarize the small-height transfer census using exact rational comparisons."""
import json,sys
from fractions import Fraction
from flint import arb,ctx
ctx.prec=160
R=list(map(json.loads,open(sys.argv[1])))
def ratio(r):return Fraction(r['W']**12,r['out_rad'])
def src(r):return Fraction(max(r['src']),r['source_rad'])
def gain(r):return ratio(r)/src(r)
print('inputs, transfers, parameters',len(set(tuple(r['src']) for r in R)),len(R),len(set((r['x'],r['y']) for r in R)))
print('positive output, positive source to negative, output improved',
      sum(ratio(r)>1 for r in R),sum(src(r)>1>ratio(r) for r in R),sum(gain(r)>1 for r in R))
for title,fn in [('output',ratio),('improvement',gain),('loss',lambda r:1/gain(r))]:
    r=max(R,key=fn)
    print(title,r['src'],r['x'],float((arb(fn(r).numerator)/fn(r).denominator).log()))
def quality(r):return 12*arb(r['W']).log()/arb(r['out_rad']).log()
best=max(R,key=lambda r:float(quality(r)))
assert all((r['x'],r['y'])==(best['x'],best['y']) or quality(r)<quality(best) for r in R)
print('best quality',best['src'],best['x'],quality(best))
