"""Check the local square and prescribed-cylinder data in the Pell index sieve."""

from abc_cm_twist_depth_example import degree_eleven_factors


def multiply(left, right, modulus):
    b, a = left
    d, c = right
    return (b*d + 2*a*c) % modulus, (a*d + b*c) % modulus


def unit_power(n, modulus):
    result = (1, 0)
    base = (1, 1)
    while n:
        if n % 2:
            result = multiply(result, base, modulus)
        base = multiply(base, base, modulus)
        n //= 2
    return result


def value(coefficients, n, modulus):
    b, a = unit_power(n, modulus)
    s = (b*b + 2*a*a) % modulus
    x = -8*(s + 2*a*b) % modulus
    total = 0
    s_power = 1
    for coefficient in coefficients:
        total = (total*x + coefficient*s_power) % modulus
        s_power = s_power*s % modulus
    return -total*pow(2, -125, modulus) % modulus


def check():
    coefficients = degree_eleven_factors()[1]
    p = 683
    period = 114
    assert unit_power(4*period, p) == (1, 0)
    for prime in (2, 3, 19):
        assert unit_power(4*(period//prime), p) != (1, 0)
    assert unit_power(4*period, p*p) != (1, 0)
    hits = [n for n in range(period) if value(coefficients, n, p) == 0]
    assert hits == [9, 15, 21, 23, 25, 30, 36, 47, 58, 73, 74, 94, 105, 106]
    for n in hits:
        # The first local period step gives the linear slope modulo p squared.
        first = value(coefficients, n, p*p)//p
        next_value = value(coefficients, n + period, p*p)//p
        slope = (next_value - first) % p
        assert slope != 0
        lift = -first*pow(slope, -1, p) % p
        assert value(coefficients, n + period*lift, p*p) == 0
        # At most one root among all p residues, checked directly.
        assert sum(value(coefficients, n + period*j, p*p) == 0 for j in range(p)) == 1
    test = value(coefficients, 1213, p**3)
    assert test % (p*p) == 0 and test != 0
    assert value(coefficients, 1213 + period*p*p, p**3) == test
    print("683 has order 114 and 14 simple hit classes; index 1213 has exact depth 2")


if __name__ == "__main__":
    check()
