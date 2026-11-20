"""Independent newform-orbit check for the 3-free dyadic factor s_n."""
from math import gcd

try:
    from cypari import pari
except ImportError:
    from cypari2 import Pari
    pari = Pari()


def supports(odd_part):
    all_primes = set()
    orbits = 0
    for exponent in range(11):
        level = odd_part * 2**exponent
        space = pari.mfinit([level, 2], 0)
        forms = list(pari.mfeigenbasis(space))
        assert sum(int(pari.mfparams(f)[3].poldegree()) for f in forms) == int(pari.mfdim(space))
        for form in forms:
            traces = pari.mfcoefs(form, 47)
            at_47 = int((traces[47]**2-98).norm())
            at_31 = int(traces[31].norm())
            obstruction = gcd(at_31, at_47)
            assert obstruction > 0, (level, 'characteristic-zero survivor')
            factors = pari(obstruction).factor()
            all_primes.update(map(int, factors[0]))
        orbits += len(forms)
    return orbits, all_primes


if __name__ == '__main__':
    pari.allocatemem(320000000, silent=True)
    assert supports(1) == (28, {2, 7, 17})
    assert supports(3) == (62, {2, 3, 5})
    print('All 90 orbits checked. No exact survivor; supports {2,7,17} and {2,3,5}.')
