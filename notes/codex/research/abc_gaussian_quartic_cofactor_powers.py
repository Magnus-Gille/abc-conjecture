"""Certify powers and odd support of the exact above-r^4 denominator cofactors."""
import argparse,csv,hashlib,json
from pathlib import Path
from math import gcd
from flint import fmpz
from abc_gaussian_quartic_prime_scan import denominator
from abc_gaussian_scalar_prime_scan import prime_flags

def verify(input_path,output_path):
    maxq=1000000
    flags=prime_flags(maxq)
    q_primes=[q for q in range(2,maxq+1) if flags[q]]
    folds=[];proof_count=0;fallback=0;cols=[0,0,0]
    proof_digest=hashlib.sha256()
    with input_path.open() as archive,output_path.open('w') as out:
        writer=csv.writer(out,lineterminator='\n')
        writer.writerow(['r','cofactor_bits','cofactor_mod8','smallest_square_nonresidue_prime','max_exponent_checked','prime_exponents','prime_powers'])
        for row in csv.DictReader(archive):
            r=int(row['r']);S=int(row['small_product']);B=denominator(r);C=B//S
            assert C*S==B and C.bit_length()==int(row['remaining_cofactor_bits'])
            if C==1:
                writer.writerow([r,1,1,'',0,0,'unit']);continue
            h=(r**4).bit_length()-1
            maximum=(C.bit_length()-1)//h
            powers=[];w_square=0;count=0
            for ell in q_primes:
                if ell>maximum:break
                witness=None
                for q in range(ell+1,maxq+1,ell):
                    if flags[q]:
                        res=int(C%q)
                        if res and pow(res,(q-1)//ell,q)!=1:
                            witness=q;break
                    if q>200*ell+200:break
                if witness is None:
                    z=C.root(ell)
                    if z**ell==C:powers.append(ell)
                    fallback+=1
                if ell==2:w_square=witness or 0
                proof_count+=1;count+=1
                proof_digest.update(f'{r} {ell} {witness or 0}\n'.encode())
            assert C.is_square()==(2 in powers)
            if powers:folds.append((r,powers))
            cols[0]+=1;cols[1]+=int(C%8==5);cols[2]=max(cols[2],w_square)
            writer.writerow([r,C.bit_length(),int(C%8),w_square,maximum,count,' '.join(map(str,powers))])
    return dict(nonunits=cols[0],cofactors_5_mod8=cols[1],max_square_nonresidue_prime=cols[2],
                successful_powers=folds,prime_exponent_tests=proof_count,exact_root_fallbacks=fallback,witness_digest=proof_digest.hexdigest())

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    here=Path(__file__).resolve().parent
    ap.add_argument('--input',type=Path,default=here/'abc_gaussian_quartic_prime_scan.csv')
    ap.add_argument('--rows',type=Path,default=here/'abc_gaussian_quartic_cofactor_powers.csv')
    args=ap.parse_args()
    print(json.dumps(verify(args.input,args.rows),indent=2))
