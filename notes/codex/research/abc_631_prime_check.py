"""Test every possible later prime through 10^10 in the 631 lifting family."""

from math import isqrt

from sympy import sieve


def later_prime_check(x, y, bound):
    p = 631
    last = (bound - 1) // p
    possible = bytearray([1]) * (last + 1)
    possible[0] = 0
    for ell in sieve.primerange(2, isqrt(bound) + 1):
        if ell == p:
            continue
        # Strike ell-divisors of p*t+1 beginning where p*t+1 >= ell^2.
        start = max(1, (ell * ell - 1 + p - 1) // p)
        start += (-pow(p, -1, ell) - start) % ell
        if start <= last:
            count = (last - start) // ell + 1
            possible[start::ell] = bytes(count)

    seed = y**5 - x**5
    primes = 0
    dividing = []
    repeated = []
    for t in range(1, last + 1):
        if not possible[t]:
            continue
        q = p * t + 1
        primes += 1
        if seed % q == 0:
            continue
        exponent = 5 * p
        part = t
        while part % p == 0:
            exponent *= p
            part //= p
        if pow(y, exponent, q) == pow(x, exponent, q):
            dividing.append(q)
            if pow(y, exponent, q*q) == pow(x, exponent, q*q):
                repeated.append(q)
    return primes, dividing, repeated


if __name__ == "__main__":
    x = 188501707118483312662842033434214073534
    y = 14106104618039134064040525112584509829903089804413987905
    primes, dividing, repeated = later_prime_check(x, y, 10**10)
    assert primes == 722563
    assert dividing == [
        2025511, 1007347331, 1055139271, 1867375091, 4447458371, 8807321321
    ]
    assert repeated == []
    print(f"{primes} eligible primes, {len(dividing)} new divisors, {len(repeated)} repeated")
