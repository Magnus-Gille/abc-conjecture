"""Verify exclusions for every prime perfect-power exponent through 31,904,497.

Pass the path to the C++17 executable built from abc_full_quartic_prime_rank_scan.cpp.
Certification uses an order calculation in a residue ring and requires no
primality oracle for the auxiliary moduli.
"""
from hashlib import sha256
from math import gcd
import subprocess
import sys

from abc_congruent_six_quotient_local_covers import psi_odd
from abc_congruent_six_smooth_odd_support import prime_list


def normalized_denominator(q, modulus):
    return psi_odd((-3, 9), q, modulus) * pow(3, -((q*q-1)//2), modulus) % modulus


def exclude(q, exponent, trial_primes):
    for k in range(2, exponent + 1, 2):
        h = k*exponent + 1
        if any(h % p == 0 and h != p for p in trial_primes):
            continue
        if pow(2, h-1, h) != 1 or h % 3 == 0:
            continue
        # At odd q the absolute value of the normalized division polynomial is B_q.
        signed = normalized_denominator(q, h)
        c = pow(signed, k, h)
        if gcd(c-1, h) == 1 and pow(c, exponent, h) == 1:
            # Each prime divisor of h is 1 modulo exponent by the order of c.
            # Their product could not be below (exponent+1)^2 unless h is prime.
            # In F_h every nonzero exponent-th power has k-th power 1.
            assert h < (exponent+1)**2
            return k
    raise ValueError(f'no verified auxiliary integer for q={q}, exponent={exponent}')


def main():
    if len(sys.argv) != 2:
        sys.exit('Pass the path to the compiled rank scanner.')
    cutoff = 31_904_497
    rows = subprocess.check_output([sys.argv[1], str(cutoff), '--power-exponents'])
    expected_digest = '83917e8c564853dd46af78905ee4d0b95696aaa01fa77021522b6a85e884f312'
    if sha256(rows).hexdigest() != expected_digest:
        raise ValueError('Candidate list differs from the independently verified prime-order census.')
    trial_primes = prime_list(101)
    count, largest_k = 0, 0
    last_exponent = 0
    for row in rows.splitlines():
        q, exponent = map(int, row.split())
        assert last_exponent < exponent <= cutoff
        last_exponent = exponent
        modulus = exponent*exponent
        value = normalized_denominator(q, modulus)
        assert value % exponent != 0
        if pow(value, exponent-1, modulus) == 1:
            raise ValueError(f'unresolved at the exponent squared: q={q}, exponent={exponent}')
        largest_k = max(largest_k, exclude(q, exponent, trial_primes))
        count += 1
    print('Candidate pairs excluded:', count, 'largest auxiliary multiplier:', largest_k)
    print('Largest candidate exponent tested:', last_exponent)
    print('All candidate pairs also fail the necessary test modulo the square of the exponent.')


if __name__ == '__main__':
    main()
