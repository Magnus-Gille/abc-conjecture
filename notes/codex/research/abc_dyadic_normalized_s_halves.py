"""All-index power exclusions on each half of the 3-free shifted dyadic factor."""

from functools import cache
from math import gcd, isqrt


# Each row has the ordered lists of auxiliary primes for h=0,...,q-1.
WITNESSES = {
    (2, -1): [(113, 353), (5,)],
    (2, 1): [(233, 353), (5,)],
    (3, -1): [(1279,), (7,), (1759, 1663)],
    (3, 1): [(79,), (7,), (283, 1279)],
    (5, -1): [(71,), (271,), (31,), (71,), (31,)],
    (5, 1): [(71,), (271,), (31,), (71,), (31,)],
    (7, -1): [(113,), (113,), (3361,), (127,), (113,), (29,), (71,)],
    (7, 1): [(113,), (113,), (127,), (5839,), (29,), (29,), (29,)],
}


@cache
def orbit(q, p):
    assert p > 3 and all(p % d for d in range(2, isqrt(p) + 1))
    assert (p - 1) % q == 0
    assert q % 2 or p % 4 == 1  # both signs of a denominator have the same character
    inverse_four = pow(4, -1, p)

    def recurrence(i, term):
        j = i // 2
        if i % 2:
            return (term(j+2)*term(j)**3 - term(j-1)*term(j+1)**3) % p
        return (inverse_four*term(j)*(term(j+2)*term(j-1)**2 -
                                      term(j-2)*term(j+1)**2)) % p

    @cache
    def psi(i):
        if i <= 4:
            return (0, 1, 4, -36, -448)[i] % p
        return recurrence(i, psi)

    # Indices m+offset, offset=-3,...,3; the initial centre m=8 gives n=16.
    block = tuple(psi(i) for i in range(5, 12))
    half = 4 % (p - 1)
    exponent = (p - 1) // q
    inverse_two = pow(2, -exponent, p)
    seen = {}
    values = []
    while (block, half) not in seen:
        seen[block, half] = len(values)
        characters = []
        for sign in (-1, 1):
            scale = half*half + sign*half
            characters.append(pow(block[3+sign], exponent, p) *
                              pow(inverse_two, scale % (p-1), p) % p)
        values.append(tuple(characters))
        block = tuple(recurrence(i, lambda t: block[t+3]) for i in range(-3, 4))
        half = 2*half % (p-1)
    return values, seen[block, half]


def allowed(q, sign, h, p):
    values, split = orbit(q, p)
    target = pow(3, h*((p-1)//q), p)
    index = (1 + sign) // 2
    mask = [v[index] in (0, target) for v in values]
    tail = mask[split:]
    for period in range(1, len(tail) + 1):
        if len(tail) % period == 0 and all(v == tail[i % period] for i, v in enumerate(tail)):
            break
    residues = {(split+i) % period for i in range(period) if tail[i]}
    return mask[:split], period, residues


def verify():
    for (q, sign), by_h in WITNESSES.items():
        assert len(by_h) == q
        for h, primes in enumerate(by_h):
            rows = [allowed(q, sign, h, p) for p in primes]
            upto = max(len(prefix) for prefix, _, _ in rows)
            for i in range(upto):
                assert not all(prefix[i] if i < len(prefix) else i % period in residues
                               for prefix, period, residues in rows)
            if len(primes) == 1:
                assert not rows[0][2]
            else:
                assert len(primes) == 2
                (_, d, first), (_, e, second) = rows
                common = gcd(d, e)
                assert not any((x-y) % common == 0 for x in first for y in second)
    print("Every coefficient class at q=2,3,5,7 excluded on each 3-free denominator half.")


if __name__ == "__main__":
    verify()
