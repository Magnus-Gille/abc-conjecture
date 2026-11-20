"""Standard-library two-isogeny descent bound over Q(theta), theta^3=3 theta+1."""
from itertools import product

ONE = (1, 0, 0)
THETA = (0, 1, 0)
CONJUGATE = (2, 0, -1)
PI = (-1, 1, 0)
PI_INVERSE_TIMES_3 = (-2, 1, 1)


def scale(a, scalar):
    return tuple(scalar*x for x in a)


def multiply(a, b):
    i, j, k = a
    x, y, z = b
    cubic, quartic = j*z + k*y, k*z
    return (i*x+cubic, i*y+j*x+3*cubic+quartic, i*z+j*y+k*x+3*quartic)


def unit_inverse(u):
    x, y, z = multiply(u, u)
    return (x-3, y, z)


def descent_pair(scalar, classes):
    sign, t, conjugate, two, pi = classes
    d = scale(ONE, (-1)**sign * 2**two)
    other = scale(multiply(THETA, THETA), (-1)**sign * scalar // (2**two * 3**pi))
    for exponent, base, inverse in [
            (t, THETA, unit_inverse(THETA)),
            (conjugate, CONJUGATE, unit_inverse(CONJUGATE)),
            (pi, PI, PI_INVERSE_TIMES_3)]:
        if exponent:
            d = multiply(d, base)
            other = multiply(other, inverse)
    assert multiply(d,other) == scale(multiply(THETA,THETA),scalar)
    return d,other


def residue(v, modulus):
    return tuple(x % modulus for x in v)


def residue_tables(modulus):
    elements = product(range(modulus), repeat=3)
    squares = {residue(multiply(v,v),modulus) for v in elements}
    fourths = {residue(multiply(s,s),modulus) for s in squares}
    return squares, fourths


def soluble_at(pair, modulus, tables):
    d, other = pair
    squares, fourths = tables
    for first, second in [(d,other), (other,d)]:
        for fourth in fourths:
            value = tuple(x+y for x,y in zip(first,multiply(second,fourth)))
            if residue(value,modulus) in squares:
                return True
    return False


def main():
    assert multiply(THETA,unit_inverse(THETA)) == ONE
    assert multiply(CONJUGATE,unit_inverse(CONJUGATE)) == ONE
    assert multiply(PI,PI_INVERSE_TIMES_3) == scale(ONE,3)
    for scalar in (-36,144):
        initial = []
        for cls in product(range(2),repeat=5):
            sign, t, conjugate, two, pi = cls
            if scalar < 0 or (sign == 0 and conjugate == 0 and t == pi):
                initial.append(cls)
        for m in (16, 9):
            table = residue_tables(m)
            initial = [c for c in initial if soluble_at(descent_pair(scalar,c),m,table)]
            print(f'A={scalar} theta^2, modulus={m}, classes={len(initial)}: {initial}')
        assert len(initial) == (8 if scalar == -36 else 1)
    print('rank <= log2(8*1/4) = 1')


if __name__ == '__main__':
    main()
