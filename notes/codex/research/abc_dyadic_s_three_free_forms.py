"""Check the complete level 1536 determinant obstruction, including oldforms."""
from math import gcd

try:
    from cypari import pari
except ImportError:
    from cypari2 import Pari
    pari = Pari()


def check():
    pari.allocatemem(256_000_000, silent=True)
    pari('M=mfinit([1536,2],1)')
    assert int(pari('mfdim(M)')) == 225
    pari('A=mfheckemat(M,47)^2-98; U=mfheckemat(M,31)')
    det1 = int(pari('matdet(A)'))
    det2 = int(pari('matdet(A+U)'))
    assert det1 and det2
    G = 2**225*3**32*5**32*7**118*11**8*17**28*23**2*31**4
    assert gcd(det1, det2) == G
    print('Level 1536, dimension 225: both nonzero determinants and their gcd verified.')


if __name__ == '__main__':
    check()
