"""Local certificates for u_n^2 + 8v_n^2 and u_n^2 + 16v_n^2 at n=2^k, k≥3.

Run with standard-library Python. No term of the integer orbit is factored.
"""

from fractions import Fraction
from math import gcd, isqrt, lcm


S_WITNESSES = {
    2: 23,
    3: 7,
    5: 31,
    7: 113,
    11: 353,
    13: 8191,
    17: 2687,
    19: 191,
    23: 47,
    29: 18503,
    31: 311,
    37: 1777,
    41: 1231,
    43: 20641,
    47: 473479,
    53: 892097,
    59: 50033,
    61: 977,
    67: 180097,
    71: 1279,
    73: 3359,
    79: 2687,
    83: 167,
    89: 5519,
    97: 4657,
    101: 1360673,
    103: 756433,
    107: 75329,
    109: 2399,
    113: 1583,
    127: 13463,
    131: 263,
    137: 823,
    139: 5839,
    149: 1537681,
    151: 1511,
    157: 15073,
    163: 15649,
    167: 1082161,
    173: 496511,
    179: 1328897,
    181: 1087,
    191: 73727,
    193: 3089,
    197: 7487,
    199: 643567,
    211: 2111,
    223: 18287,
    227: 6711937,
    229: 5039,
    233: 1399,
    239: 7649,
    241: 5303,
    251: 168673,
    257: 1543,
    263: 71537,
    269: 21521,
    271: 5962001,
    277: 1663,
    281: 8431,
    283: 36791,
    293: 1759,
    307: 29473,
    311: 15551,
    313: 260417,
    317: 6695041,
    331: 5297,
    337: 5393,
    347: 31231,
    349: 49559,
}

T_WITNESSES = {2: 3, 3: 7, 5: 71, 47: 419429}


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def add_rational(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x, y = P
    u, v = Q
    if x == u and y == -v:
        return None
    if P == Q:
        slope = (3*x*x + 32*x + 32) / (2*y)
    else:
        slope = (v - y) / (u - x)
    z = slope*slope - 16 - x - u
    return z, slope*(x-z) - y


def check_reduction_orders():
    R = Fraction(-8), Fraction(16)
    P = None
    coordinates = {}
    for m in range(1, 8):
        P = add_rational(P, R)
        coordinates[m] = P[0]
    assert coordinates[3] == Fraction(-200, 81)
    p = 117041
    assert is_prime(p)
    assert coordinates[7] == Fraction(-61290606728, p**2)
    order = 14630
    divisors = [2, 5, 7, 11, 19]
    assert order == 2*5*7*11*19 and pow(2, order, p) == 1
    assert all(pow(2, order//l, p) != 1 for l in divisors)


def next_state(state, p):
    u, v, w = state
    u4, v4 = pow(u, 4, p), pow(v, 4, p)
    return (u4 - 32*v4) % p, (2*u*v*w) % p, (pow(w, 4, p) - 128*u4*v4) % p


def check_witness(q, p, c, modulus):
    assert is_prime(q) and is_prime(p) and (p-1) % q == 0
    state = (31 % p, 14 % p, 2273 % p)
    first = {}
    bad_indices = []
    k = 3
    while state not in first:
        first[state] = k
        u, v, _ = state
        z = (u*u + c*v*v) % p
        if not z or pow(z, (p-1)//q, p) == 1:
            bad_indices.append(k)
        state = next_state(state, p)
        k += 1
    start = first[state]
    period = k - start
    for j in bad_indices:
        if j < start:
            assert (j-1) % modulus != 0, (q, p, c, j)
        else:
            assert (j-1) % gcd(modulus, period) != 0, (q, p, c, j, period)
    return k - 3, bool(bad_indices)


if __name__ == "__main__":
    check_reduction_orders()
    assert set(S_WITNESSES) == {q for q in range(2, 350) if is_prime(q)}
    raw, conditional, largest = 0, 0, 0
    for q, p in S_WITNESSES.items():
        modulus = lcm(14630, 3**(q-2)) if q >= 5 else 1
        length, needs_progression = check_witness(q, p, 8, modulus)
        raw += int(not needs_progression)
        conditional += int(needs_progression)
        largest = max(largest, length)
    print(f"s: {raw} raw and {conditional} progression certificates; {largest} states at most.")
    for q, p in T_WITNESSES.items():
        length, _ = check_witness(q, p, 16, 1)
        print(f"t: q={q}, p={p}, {length} states.")
