"""Verify a reported conic vector by direct integer construction of its full triple."""
import argparse,json
from math import prod
from flint import arb,fmpz
from abc_conic_short_kernel import parameters

def verify(row,dim):
    ell,eta,D,M,k,t,exps,H=parameters(dim)
    def multiply(x,y):
        b,a=x;c,f=y
        return b*c+2*a*f,b*f+a*c
    b,a=fmpz(1),fmpz(0)
    radJ=1
    absJ=fmpz(1)
    for p,(c,f),x in zip(ell,eta,row['z']):
        if x==0:continue
        radJ*=p
        absJ*=fmpz(p)**abs(x)
        z=(fmpz(c),fmpz(f if x>0 else -f))
        e=abs(x)
        while e:
            if e&1:b,a=multiply((b,a),z)
            e//=2
            if e:z=multiply(z,z)
    assert b.gcd(a)==1 and b%2 and a%M==0 and abs(b*b-2*a*a)==absJ
    S=b*b+2*a*a
    C=S*S
    assert absJ*absJ+8*a*a*b*b==C
    excess=1
    for p in exps:
        val=row['v_a'][str(p)]
        residue=a%p**(val+1)
        assert residue and residue%p**val==0
        excess*=p**(val-1)
    height=arb(C).log()
    gain=(arb(S)*excess/(radJ*abs(a*b))).log()
    assert abs(float(height)-row['log_C'])<1e-12*float(height)
    assert abs(float(gain)-row['log_gain_attained'])<1e-10
    assert int((height/arb(10).log()).floor().unique_fmpz())+1==row['height_digits']
    return dict(d=dim,support=row['s'],l1=row['l1'],bits_C=C.bit_length(),digits_C=row['height_digits'],
                log_C=float(height),log_gain=float(gain))

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('data')
    ap.add_argument('--dimension',type=int,required=True)
    ap.add_argument('--size',type=int,required=True)
    ap.add_argument('--field',default='best_M')
    args=ap.parse_args()
    for line in open(args.data):
        obj=json.loads(line)
        if obj['d']!=args.dimension:continue
        for entry in obj.get('search',[obj]):
            if entry['size']==args.size:
                print(json.dumps(verify(entry[args.field],obj['d'])))
