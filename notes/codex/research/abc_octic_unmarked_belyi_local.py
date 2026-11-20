"""Exclude the exceptional degree-seven rational Belyi passport at a good prime."""
from itertools import combinations
from math import gcd


def kernel(rows, prime):
    """Return the normalized kernel vector of a rank-six matrix with seven columns."""
    matrix = [[a % prime for a in row] for row in rows]
    pivots = []
    for col in range(7):
        row = len(pivots)
        pivot = next((k for k in range(row, len(matrix)) if matrix[k][col]), None)
        if pivot is None:
            continue
        pivots.append(col)
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        inverse = pow(matrix[row][col], -1, prime)
        matrix[row] = [a * inverse % prime for a in matrix[row]]
        for k in range(len(matrix)):
            if k != row:
                coeff = matrix[k][col]
                matrix[k] = [(a - coeff*b) % prime for a, b in zip(matrix[k], matrix[row])]
    assert len(pivots) == 6
    free, = set(range(7)).difference(pivots)
    vector = [0] * 7
    vector[free] = 1
    for k, col in enumerate(pivots):
        vector[col] = -matrix[k][free] % prime
    return normalize(vector, prime)


def normalize(vector, prime):
    first = next(a % prime for a in vector if a % prime)
    return tuple((a * pow(first, -1, prime)) % prime for a in vector)


def jets(point, prime):
    """First six coefficients of 1,x,y,x²,xy,x³,x²y in a local trivialization."""
    if point is None:
        # Pole orders are 0,2,3,4,5,6,7. The flags at O are coordinate flags.
        return [[int(col == index) for col in range(7)] for index in (6, 5, 4, 3, 2, 1)]

    def multiply(a, b):
        return [sum(a[j] * b[k-j] for j in range(k+1)) % prime for k in range(6)]

    x0, y0 = point
    x, y = [x0, 0, 0, 0, 0, 0], [y0, 0, 0, 0, 0, 0]
    if y0:
        x[1] = 1
        current = y
        derivative = 2*y0
    else:
        y[1] = 1
        current = x
        derivative = -(3*x0*x0 + 32*x0 + 32)
    for k in range(1, 6):
        xx = multiply(x, x)
        eq = multiply(y, y)[k] - multiply(xx, x)[k] - 16*xx[k] - 32*x[k]
        current[k] = -eq * pow(derivative, -1, prime) % prime
    xx = multiply(x, x)
    return list(zip([1, 0, 0, 0, 0, 0], x, y, xx, multiply(x, y), multiply(xx, x), multiply(xx, y)))


def count(prime):
    points = [None] + [(x, y) for x in range(prime) for y in range(prime)
                       if (y*y - x**3 - 16*x*x - 32*x) % prime == 0]
    assert gcd(len(points), 7) == 1 and prime > 7
    flags = {point: jets(point, prime) for point in points}
    six = [(point, kernel(flag, prime)) for point, flag in flags.items() if point is not None]
    # Seven times a nonzero rational point is nonzero, so the residual simple point differs.
    def support(vector):
        return {point for point in points if sum(a*b for a,b in zip(flags[point][0], vector)) % prime == 0}
    six = [(v, support(v)) for _, v in six]
    assert all(len(s) == 2 for _, s in six)
    four_two = set()
    for u in points:
        for v in points:
            if u != v:
                vector = kernel(flags[u][:4] + flags[v][:2], prime)
                if len(support(vector)) == 3:
                    four_two.add(vector)

    pencils = hits = 0
    for (s, s_points), (t, t_points) in combinations(six, 2):
        if s_points.isdisjoint(t_points):
            pencils += 1
            for coeff in range(1, prime):
                combo = normalize([a + coeff*b for a,b in zip(s,t)], prime)
                hits += combo in four_two
    return len(points), len(six), len(four_two), pencils, hits


if __name__ == "__main__":
    for prime in (11, 17, 19):
        print(prime, *count(prime))
