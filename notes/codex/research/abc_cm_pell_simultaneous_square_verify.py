"""Verify a single Pell-index progression with 1,716 simultaneous exact squares."""

from csv import DictReader
from hashlib import sha256
from math import gcd, isqrt, lcm
from pathlib import Path

from abc_cm_pell_index_square_sieve import degree_eleven_factors, unit_power, value


def prime_divisors(n):
    factors = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def crt(x, m, y, n):
    common = gcd(m, n)
    if (y-x) % common:
        return None
    step = ((y-x)//common)*pow(m//common, -1, n//common) % (n//common)
    return x + m*step, m*(n//common)


def small_first_hits(coefficients):
    earlier, period = [0], 1
    previous_primes = []
    for p, d, count, first in [
        (683, 114, 14, 1213),
        (1409, 32, 14, 4196890),
        (2179, 1090, 348, 5274743585530),
        (2267, 162, 340, 97751649103127879),
    ]:
        residues = []
        for n in range(d):
            base = value(coefficients,n,p*p)
            if base % p:
                continue
            slope = (value(coefficients,n+d,p*p)-base)//p
            j = -(base//p)*pow(slope,-1,p) % p
            residues.append(n+d*j)
        next_period = period*(p*d//gcd(period,p*d))
        combined = []
        for x in earlier:
            for y in residues:
                joint = crt(x,period,y,p*d)
                if joint is not None:
                    z, joint_period = joint
                    assert joint_period == next_period
                    combined.append(z)
        earlier, period = combined, next_period
        assert len(set(earlier)) == len(earlier) == count
        assert min(earlier) == first
        previous_primes.append(p)
        for q in previous_primes:
            residue = value(coefficients,first,q**3)
            assert residue and residue % (q*q) == 0


def close_periods(rows, x, modulus):
    # The prime-class obstruction restricts the possible extra divisors.
    selected = {int(r["p"]) for r in rows}
    pending = []
    for row in rows:
        pending.extend(prime_divisors(int(row["order"])))
    closure = {}
    while pending:
        p = pending.pop()
        if p in selected:
            raise AssertionError("A selected prime divides a retained order")
        if p in closure or p % 88 not in (1,67):
            continue
        d = p - (1 if p % 8 == 1 else -1)
        for ell in prime_divisors(d):
            while d % ell == 0 and unit_power(4*(d//ell),p) == (1,0):
                d //= ell
        closure[p] = d
        pending.extend(prime_divisors(d))
    assert len(closure) == 53
    coefficients = degree_eleven_factors()[1]
    for p, d in closure.items():
        assert value(coefficients,x % (p*d),p*p) != 0
        modulus = lcm(modulus,p*d)
    base = modulus
    for p in selected:
        assert base % (p*p) == 0
        base //= p*p
        assert base % p
    assert modulus.bit_length() == 101887
    assert base.bit_length() == 28192
    assert all(base % int(r['order']) == 0 for r in rows)
    print("closure primes",len(closure),"base modulus bits",base.bit_length())

def main():
    coefficients = degree_eleven_factors()[1]
    source = Path(__file__).with_name("abc_cm_pell_simultaneous_square_witness.csv")
    with source.open() as f:
        rows = list(DictReader(f))
    marks = []
    x, modulus = 0, 1
    support = 1
    for row in rows:
        p, d, index = (int(row[key]) for key in ("p","order","index"))
        assert p > 11 and all(p % k for k in range(2,isqrt(p)+1))
        assert (p - (1 if p % 8 in (1,7) else -1)) % d == 0
        assert unit_power(4*d,p) == (1,0)
        assert all(unit_power(4*(d//l),p) != (1,0) for l in prime_divisors(d))
        assert unit_power(4*d,p*p) != (1,0)
        assert unit_power(4*d*p*p,p**3) == (1,0)
        residue = value(coefficients,index,p**3)
        assert residue and residue % (p*p) == 0
        joint = crt(x,modulus,index,d*p*p)
        assert joint is not None
        x, modulus = joint
        marks.append(p)
        support *= p
    assert len(set(marks)) == len(marks) == 1716
    assert x.bit_length() == 101811 and modulus.bit_length() == 101812
    assert all((x-int(r['index'])) % (int(r['order'])*int(r['p'])**2) == 0 for r in rows)
    print('primes',len(marks),'range',min(marks),max(marks))
    print('marked prime product bits',support.bit_length())
    print('index and period bits',x.bit_length(),modulus.bit_length())
    print('index digest',sha256(x.to_bytes((x.bit_length()+7)//8,'big')).hexdigest())
    close_periods(rows,x,modulus)
    small_first_hits(coefficients)


if __name__ == "__main__":
    main()
