"""Independent no-CRT audit for primes from 5 through 10^9.

In the scratch directory run
  g++ -O3 -std=c++17 abc_congruent_six_exponent_trace_audit.cpp -o /tmp/abc_trace_audit
  python3 abc_congruent_six_exponent_trace_audit.py /tmp/abc_trace_audit
The low interval uses the six necessary signed characters from the trace descent,
with p=23 and 47 checked separately by the order of (12,36).
"""
from math import gcd
import subprocess
import sys
try:
    from cypari import pari
except ImportError:
    from cypari2 import Pari
    pari = Pari()

FINAL = {
    99426071:503, 114643751:1249, 131968489:719, 345399071:769,
    381837431:349, 424674311:457, 487420391:313, 597818471:443,
    632591951:457, 885554569:367,
}


def character(n,l):
    return int(pari.kronecker(n,l))


def local_data(l,just_exponent=None):
    assert l>3 and pari.isprime(l)
    E=pari.ellinit([0,0,0,-36,0],l)
    G=[-3,9]
    order=int(pari.ellorder(E,G))
    h=l-character(-3,l)
    slopes={-int(pari.lift(pari.ellmul(E,G,i)[0]))*pow(3,-1,l)%l
            for i in range(1,order) if gcd(i,order)==1}
    traces=[]
    for slope in slopes:
        values=[2,slope]
        while len(values)<h:
            values.append((slope*values[-1]-values[-2])%l)
        traces.append(values)

    def forces_square(i):
        if gcd(i,h)!=1:
            return False
        j=pow(i,-1,h)
        return all(character(row[j],l)==1 for row in traces)

    if just_exponent is not None:
        assert forces_square(just_exponent%h)
        return order,h,pow(just_exponent,-1,h),len(slopes)
    squares=''.join(str(int(character(i,l)==1)) for i in range(l))
    forced=''.join(str(int(forces_square(i))) for i in range(h))
    unit_count=sum(gcd(i,h)==1 for i in range(h))
    return (-forced.count('1')/unit_count,l,h,squares,forced)


def low_interval():
    auxiliary=(5,7,11,13,23,47)
    for l,r in [(23,3),(47,6)]:
        E=pari.ellinit([0,0,0,-36,0],l)
        assert int(pari.ellorder(E,[12,36]))==r
    for pp in pari.primes([5,27430]):
        p=int(pp)
        if p in (23,47) or p%24 not in (1,23):
            continue
        signed=p if p%24==1 else -p
        assert any(l!=p and character(signed,l)==-1 for l in auxiliary)
    print('Low interval through 27,430 verified with six signed characters and the orders 3,6 at 23,47.')


def main(executable):
    low_interval()
    tests=sorted(local_data(int(l)) for l in pari.primes([5,251]))
    rows=''.join(f'{l} {h} {squares} {forced}\n' for _,l,h,squares,forced in tests)
    candidates=list(map(int,subprocess.check_output([executable],input=rows,text=True).split()))
    assert candidates==list(FINAL)
    print(f'Direct sweep of both 24k+1 and 24k-1 through one billion leaves {len(candidates)} primes.')
    for p in candidates:
        l=FINAL[p]
        signed=p if p%24==1 else -p
        assert pari.isprime(p) and character(signed,l)==-1
        order,h,j,num=local_data(l,p)
        print(f'p={p}, l={l}, ord(G)={order}, torus size={h}, inverse exponent={j}, checked slopes={num}')


if __name__=='__main__':
    if len(sys.argv)!=2:
        sys.exit('Pass the executable built from abc_congruent_six_exponent_trace_audit.cpp.')
    main(sys.argv[1])
