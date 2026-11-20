"""Verify separation of odd index residues by each of the four quartic arms."""

from math import gcd, isqrt, lcm


MODULI = (8, 72, 120, 312, 408, 696, 840, 984, 2520, 4440, 6360, 10680, 10920, 11640)
PERIOD_PRIMES = (2, 3, 5, 7, 13, 17, 29, 37, 41, 53, 89, 97)
PROBE_BOUND = 100_000


def primes_up_to(bound):
    prime = bytearray([1]) * (bound + 1)
    prime[:2] = bytes(2)
    for p in range(2, isqrt(bound) + 1):
        if prime[p]:
            prime[p*p::p] = bytes((bound - p*p) // p + 1)
    return [p for p in range(2, bound + 1) if prime[p]]


def add(first, second, p):
    """Addition on y^2=x^3+36x^2+36x over F_p."""
    if first is None:
        return second
    if second is None:
        return first
    x, y = first
    u, v = second
    if x == u:
        if (y + v) % p == 0:
            return None
        slope = (3*x*x + 72*x + 36) * pow(2*y, -1, p) % p
    else:
        slope = (y-v) * pow(x-u, -1, p) % p
    new_x = (slope*slope - 36 - x - u) % p
    return new_x, (slope*(x-new_x) - y) % p


def multiply(scalar, point, p):
    result = None
    while scalar:
        if scalar & 1:
            result = add(result, point, p)
        scalar >>= 1
        if scalar:
            point = add(point, point, p)
    return result


def order_if_dividing_period(point, p, period):
    if multiply(period, point, p) is not None:
        return None
    order = period
    for q in PERIOD_PRIMES:
        while order % q == 0 and multiply(order//q, point, p) is None:
            order //= q
    return order


def signs_at(point, p):
    if point is None:
        return None
    x = point[0]
    if x == 6 % p:
        return None
    w = pow(8*(6-x) % p, (p-1)//2, p)
    assert w in (1, p-1)
    x_on_target = (6 + 288*x*pow((6-x)**2, -1, p)) % p
    signs = [w]
    for target in (0, -6, 6):
        square = (x_on_target-target)*pow(-3-target, -1, p) % p
        character = pow(square, (p-1)//4, p)
        if character not in (1, p-1):
            return None
        signs.append(w*character % p)
    return tuple(1 if value == 1 else -1 for value in signs)


def probe_tables(period):
    tables = {}
    for p in primes_up_to(PROBE_BOUND):
        if p % 4 != 1:
            continue
        point = (-2 % p, 8 % p)
        order = order_if_dividing_period(point, p, period)
        if order is None or order <= 4 or all(modulus % order for modulus in MODULI):
            continue
        orbit = []
        current = None
        for _ in range(order):
            orbit.append(signs_at(current, p))
            current = add(current, point, p)
        assert current is None
        tables[p] = orbit
    return tables


def main():
    period = lcm(*MODULI)
    assert period == 11_210_216_592_196_440
    rest = phi = period
    for q in PERIOD_PRIMES:
        assert rest % q == 0
        phi = phi//q*(q-1)
        while rest % q == 0:
            rest //= q
    assert rest == 1 and phi//2 == 979_425_684_357_120
    tables = probe_tables(period)
    print("modulus, sign classes, probes, distinct words in w/a/c/d")
    for modulus in MODULI:
        residues = [m for m in range(1, modulus//2 + 1, 2) if gcd(m, modulus) == 1]
        rows = []
        for orbit in tables.values():
            if modulus % len(orbit) == 0:
                row = [orbit[m % len(orbit)] for m in residues]
                if all(value is not None for value in row):
                    rows.append(row)
        counts = []
        for arm in range(4):
            signatures = {tuple(row[i][arm] for row in rows) for i in range(len(residues))}
            counts.append(len(signatures))
        assert counts == [len(residues)]*4
        print(modulus, len(residues), len(rows), counts)

    # At a tripling step the fourth arm's known 3-adic depth increases by one.
    # Its factor of 3 has positive character at this probe.
    p = 1249
    orbit = tables[p]
    assert len(orbit) == 8 and pow(3, (p-1)//2, p) == 1
    fourth_arm = [orbit[m][3] for m in (1, 3, 5, 7)]
    assert fourth_arm == [1, -1, -1, 1]
    assert all(orbit[(3*m) % 8][3] == -orbit[m][3] for m in (1, 3, 5, 7))
    print("tripling at 1249:", fourth_arm)
    print("lcm, half totient:", period, phi//2)


if __name__ == "__main__":
    main()
