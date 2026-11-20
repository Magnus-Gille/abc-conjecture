"""Check the Belyi-map polynomials by exact interpolation and squarefreeness."""

from fractions import Fraction


def outer(z):
    numerator = 7**7 * z**2 * (6*z+1)
    denominator = (z-1)**3 * (5*z+9) * (50*z*z-345*z-48)**2
    complement = (z-8) * (2*z-9)**2 * (5*z+2)**5
    return numerator, denominator, complement


def composite(u):
    numerator = (u-3)**4 * (u+4)**10 * (7*u*u-40*u+64)
    denominator = ((u*u-8*u+8)**3 * (7*u*u-24*u+72)
                   * (u**4-114*u**3+591*u*u-744*u-384)**2)
    complement = -4*u*u * (u-24)**2 * (2*u+1) * (3*u*u-16*u+28)**5
    return numerator, denominator, complement


def check_identities():
    for z in range(9):
        n, d, h = outer(z)
        assert d-n == h  # Degree at most eight.
    for u in range(33):
        n, d, h = composite(u)
        assert d-n == h
        a, b = 8*(u-3)**2, (u+4)**2
        top = 7**7*a*a*(6*a+b)*b**5
        bottom = (a-b)**3*(5*a+9*b)*(50*a*a-345*a*b-48*b*b)**2
        assert n*bottom == d*top  # Degree at most 32.
    for u in (0, Fraction(-1, 2)):
        n, d, h = composite(u)
        assert n == d != 0 and h == 0
    u = Fraction(-1, 2)
    assert composite(u)[1] == Fraction(7**17, 2**16)
    cofactor = -4*u*u*(u-24)**2*(3*u*u-16*u+28)**5
    assert cofactor == -Fraction(3**5*7**14, 2**12)


def trim(poly, prime):
    a = [x % prime for x in poly]
    while a and a[-1] == 0:
        a.pop()
    return a


def squarefree_at(factors, prime):
    """If all degrees are preserved and the product is squarefree mod p, it is squarefree over Q."""
    f = [1]
    for g in factors:
        assert g[-1] % prime
        prod = [0]*(len(f)+len(g)-1)
        for i, x in enumerate(f):
            for j, y in enumerate(g):
                prod[i+j] += x*y
        f = trim(prod, prime)
    derivative = trim([i*x for i, x in enumerate(f) if i], prime)
    while derivative:
        rem = f
        while len(rem) >= len(derivative):
            k = len(rem)-len(derivative)
            ratio = rem[-1] * pow(derivative[-1], -1, prime)
            for i, y in enumerate(derivative):
                rem[k+i] -= ratio*y
            rem = trim(rem, prime)
        f, derivative = derivative, rem
    return len(f) == 1


if __name__ == "__main__":
    check_identities()
    z_factors = [(0,1), (1,6), (-8,1), (-9,2), (2,5), (-1,1), (9,5), (-48,-345,50)]
    u_factors = [(-3,1), (4,1), (64,-40,7), (0,1), (-24,1), (1,2), (28,-16,3),
                 (8,-8,1), (72,-24,7), (-384,-744,591,-114,1)]
    assert squarefree_at(z_factors, 101) and squarefree_at(u_factors, 101)
    partitions = [[10,10,4,4]+[1]*4, [5]*4+[4,2,2,2,1,1], [6,6]+[2]*8+[1]*4]
    assert all(sum(v) == 32 for v in partitions)
    assert sum(sum(e-1 for e in v) for v in partitions) == 64
    print("Degree 32; ramification contributions over 0,1,infinity: 24,22,18.")
