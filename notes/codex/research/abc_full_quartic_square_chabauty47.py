"""Finite arithmetic for the split-prime argument on the rank-one sqrt(3) cover."""

P = 47
M = P * P


def add(left, right, a2, a4, prime=P):
    if left is None:
        return right
    if right is None:
        return left
    x, y = left
    u, v = right
    if x == u:
        if (y + v) % prime == 0:
            return None
        slope = (3*x*x + 2*a2*x + a4) * pow(2*y, -1, prime)
    else:
        slope = (v-y) * pow(u-x, -1, prime)
    xx = (slope*slope - a2 - x - u) % prime
    return xx, (slope*(x-xx)-y) % prime


def order(point, a2, a4):
    point = tuple(v % P for v in point)
    cur = point
    for k in range(1, 65):
        if cur is None:
            return k
        cur = add(cur, point, a2, a4)
    raise AssertionError('order exceeds the Hasse bound')


def jac_double(point, A):
    x, y, z = point
    s = 4*x*y*y
    m = 3*x*x + A*z**4
    xx = m*m-2*s
    return xx % M, (m*(s-xx)-8*y**4) % M, 2*y*z % M


def jac_add_affine(point, affine):
    x, y, z = point
    u, v = affine
    h = u*z*z - x
    k = v*z**3 - y
    xx = k*k-h**3-2*x*h*h
    return xx % M, (k*(x*h*h-xx)-y*h**3) % M, z*h % M


def main():
    ell = 577
    point = (-2 % ell, 8)
    cur = point
    admissible = []
    for n in range(1,25):
        if n < 24:
            assert cur is not None
        else:
            assert cur is None
        if n % 2 and pow(8*(6-cur[0]),(ell-1)//2,ell) != ell-1:
            admissible.append(n)
        cur = add(cur,point,36,36,ell)
    assert admissible == [1,11,13,23]
    print('admissible original indices modulo 24:', admissible)
    assert order((-2, 8), 36, 36) == 12
    squares = {i*i % P for i in range(P)}
    assert (-8) % P not in squares
    results = {}
    for t in range(M):
        if (t*t-3) % M:
            continue
        A = 9*(2+t) % M
        d = ((3*t+21*pow(4,-1,M)) % M,
             (-45*t*pow(4,-1,M)-153*pow(8,-1,M)) % M)
        x, y = d
        assert (y*y-x**3-A*x) % M == 0
        size = 1 + sum((y*y-x**3-A*x) % P == 0
                       for x in range(P) for y in range(P))
        triple = jac_add_affine(jac_double((x,y,1),A),d)
        X,Y,Z = jac_double(jac_double(triple,A),A)
        assert (Y*Y-X**3-A*X*Z**4) % M == 0
        assert Y % P and Z % P == 0
        formal = -X*Z*pow(Y,-1,M) % M
        assert formal % P == 0
        results[t%P] = (t,d,size,order(d,0,A),formal//P)
    assert results == {12:(1939,(852,2190),48,3,26),
                       35:(270,(263,533),48,12,24)}
    for residue, values in sorted(results.items()):
        print(residue, *values)


if __name__ == '__main__':
    main()
