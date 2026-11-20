"""Exact squareclass sieve for the paired Eisenstein quartic, including all factorizations."""
import argparse
import gzip
import hashlib
import json
from array import array
from collections import Counter, defaultdict
from math import isqrt
from pathlib import Path

import numpy as np


def theta_difference(maximum, coeff):
    """At odd n, return B(n)-2A(n) using y²+coeff*x²+8z², and 32z²."""
    size = (maximum+1)//2
    pair_counts = np.zeros(size, dtype=np.int64)
    odd_squares = np.arange(1, isqrt(maximum)+1, 2, dtype=np.int64)**2
    for x in range(isqrt(maximum//coeff)+1):
        rem = maximum-coeff*x*x
        selected = odd_squares[:np.searchsorted(odd_squares, rem, side="right")]
        indices = (coeff*x*x + selected-1)//2
        pair_counts[indices] += 2 if x==0 else 4
    delta = -pair_counts.copy()
    for z in range(1,isqrt(maximum//8)+1):
        shift = 4*z*z
        if shift>=size:
            break
        if z%2:
            delta[shift:] += 2*pair_counts[:-shift]
        else:
            delta[shift:] -= 2*pair_counts[:-shift]
    return delta


def direct(n, coeff, zcoeff):
    result = 0
    for z in range(-isqrt(n//zcoeff), isqrt(n//zcoeff)+1):
        remaining = n-zcoeff*z*z
        for x in range(-isqrt(remaining//coeff), isqrt(remaining//coeff)+1):
            square = remaining-coeff*x*x
            y = isqrt(square)
            if y*y==square:
                result += 1 if y==0 else 2
    return result


def smallest_factors(limit):
    table = array("I",range(limit+1))
    for p in range(2,isqrt(limit)+1):
        if table[p]!=p:
            continue
        for m in range(p*p,limit+1,p):
            if table[m]==m:
                table[m]=p
    return table


def prime_factors_if_squarefree(n, spf):
    primes = []
    while n>1:
        p=spf[n]
        n//=p
        if n%p==0:
            return None
        primes.append(p)
    return primes


def divisors(primes):
    values=[1]
    for p in primes:
        values += [d*p for d in values]
    return values


def real_and_legendre(d4, d5, primes):
    k = d4 if d4%3==1 else -d4
    l = -d5 if d5%3==1 else d5
    real = k<0 or l<0
    symbols = real and all(pow((-2*l if d4%p==0 else -k)%p, (p-1)//2, p)==1
                           for p in primes)
    return real, symbols


def calculate(limit, json_path, csv_path):
    odds=theta_difference(3*limit,2)
    evens=theta_difference(3*limit,4)
    for n in range(1,min(3*limit,550)+1,2):
        for coeff, data in ((2,odds),(4,evens)):
            assert data[(n-1)//2] == direct(n,coeff,8)-2*direct(n,coeff,32)
    # At most 8*sqrt(3*limit) * (1+2*sqrt(3*limit/8)) summands at any target.
    assert 8*(isqrt(3*limit)+1)*(1+2*isqrt(3*limit//8)) < 2**63
    spf = smallest_factors(limit)
    good3 = {d for d in range(1,limit+1,2) if d%3 and odds[(3*d-1)//2]==0}
    good6 = {d for d in range(1,limit+1,2) if d%3 and evens[(3*d-1)//2]==0}
    stats = defaultdict(Counter)
    last = defaultdict(list)
    digest=hashlib.sha256()
    def write(row,out):
        encoded=("\t".join(str(v) for v in row)+"\n").encode()
        digest.update(encoded)
        out.write(encoded)
    with open(csv_path,"wb") as raw, gzip.GzipFile(filename="",fileobj=raw,mode="wb",mtime=0) as out:
        write(["b","omega","torus","quartic","delta_3b","delta_6b",
               "nontrivial","real","real_symbols","three_way","three_way_real",
               "three_way_real_symbols","sample_d4"],out)
        for b in range(1,limit+1,2):
            if b%3==0:
                continue
            primes=prime_factors_if_squarefree(b,spf)
            if primes is None:
                continue
            torus=all(p%24 in (1,23) for p in primes)
            quartic=torus and all(p%24==23 or pow(3,(p-1)//4,p)==1 for p in primes)
            ds=[d4 for d4 in divisors(primes) if 1<d4<b]
            with_real=[]
            with_symbols=[]
            for d4 in ds:
                real,symbols=real_and_legendre(d4,b//d4,primes)
                if real:
                    with_real.append(d4)
                if symbols:
                    with_symbols.append(d4)
            three={d4 for d4 in ds if b in good3 and d4 in good6 and b//d4 in good3}
            signs=three.intersection(with_real)
            full=three.intersection(with_symbols)
            row=(b,len(primes),int(torus),int(quartic),int(odds[(3*b-1)//2]),
                 int(evens[(3*b-1)//2]),len(ds),len(with_real),len(with_symbols),
                 len(three),len(signs),len(full),min(full,default=0))
            write(row,out)
            groups=["all_squarefree_coprime_6"]
            if torus:
                groups.append("torus_squarefree")
            if quartic:
                groups.append("local_squarefree")
            if len(primes)==1:
                groups+=["all_primes_gt_3"]
                if torus:
                    groups.append("torus_primes")
                if b%24==1:
                    groups.append("primes_1_mod_24")
                if b%24==23:
                    groups.append("primes_23_mod_24")
                if quartic:
                    groups.append("local_primes")
                    if b%24==1:
                        groups.append("local_primes_1_mod_24")
            for key in groups:
                s=stats[key]
                s["b"]+=1
                s["global_3b_pass"]+=int(b in good3)
                s["single_6b_pass"]+=int(b in good6)
                s["both_single_pass"]+=int(b in good6 and b in good3)
                for label,items in (("nontrivial",ds),("real",with_real),
                                    ("real_symbols",with_symbols),("three_way",three),
                                    ("three_way_real",signs),("three_way_real_symbols",full)):
                    s[label+"_orientations"]+=len(items)
                    s["b_with_some_"+label]+=bool(items)
                if full and len(last[key])<12:
                    last[key].append([b,min(full),b//min(full)])
    result={"limit":limit,"all_rows_uncompressed_sha256":digest.hexdigest(),
            "direct_verification_through_odd_target":min(3*limit,549),
            "groups":dict(stats),"first_passing_b_d4_d5":dict(last)}
    Path(json_path).write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    return result


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--limit",type=int,default=10**6)
    here=Path(__file__).resolve().parent
    parser.add_argument("--table",default=here/"abc_eisenstein_slice_tunnell.tsv.gz")
    parser.add_argument("--json",default=here/"abc_eisenstein_slice_tunnell.json")
    args=parser.parse_args()
    r=calculate(args.limit,args.json,args.table)
    for key in ["all_primes_gt_3","local_primes_1_mod_24","primes_23_mod_24","local_squarefree"]:
        print(key,dict(r["groups"].get(key,{})))
    print(r["all_rows_uncompressed_sha256"])
