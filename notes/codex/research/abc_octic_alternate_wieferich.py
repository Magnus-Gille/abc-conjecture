"""Check exact first-rank fourth powers for alternate seeds on the d=65 curve."""
from abc_octic_forced_index_verify import is_prime, orbit_slope


def good_multiple(k, seed, p):
    s,t,z = seed
    q = (-4*s*s*t*t*pow(z*z, -1, p) % p,
         2*s*t*(s**4-4*t**4)*pow(z**3, -1, p) % p)

    def add(a,b):
        if a is None:
            return b
        if b is None:
            return a
        x,y = a
        u,v = b
        if x == u:
            if (y+v) % p == 0:
                return None
            slope = (3*x*x-4225)*pow(2*y, -1, p) % p
        else:
            slope = (v-y)*pow(u-x, -1, p) % p
        w = (slope*slope-x-u) % p
        return w,(slope*(x-w)-y) % p

    a = None
    while k:
        if k & 1:
            a = add(a,q)
        q = add(q,q)
        k //= 2
    return a


small_seed = (7,8,17)
witnesses = [(small_seed, 41, 13, 149), (small_seed, 173, 37, 691),
             (small_seed, 257, 65, 1093), ((73,28,689), 298897, 24855, None)]
for seed,p,r,l in witnesses:
    assert is_prime(p) and r % 2 == 1
    assert good_multiple(r,seed,p) is None
    for d in range(2,r+1):
        if r % d == 0 and is_prime(d):
            assert good_multiple(r//d,seed,p) is not None
    slope = orbit_slope(r,p**5,seed)
    value = (slope-1)**2+1
    assert value % p**4 == 0 and value % p**5 != 0
    print(f'{seed[:2]}: p={p}, rank {r}, signed minus valuation 4.')
    if l is not None:
        assert is_prime(l)
        group_order = 1
        for x in range(l):
            rhs = (x**3-4225*x) % l
            group_order += 1 if rhs == 0 else 2*(pow(rhs,(l-1)//2,l) == 1)
        assert group_order == 4*p
        assert good_multiple(4,seed,l) is not None
        print(f'Q is indivisible by {p} modulo {l}, hence over Q.')
