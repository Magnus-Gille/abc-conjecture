"""Enumerate rational tame Belyi passports in degrees 3–7 on the two forms of j=8000.

The two-prime certificate uses only Python's standard library. A partition is
printed as its decreasing list of multiplicities. Target fibers are unordered.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations


class QuadraticField:
    """Elements a+bt of F_p[t]/(t²-n) are encoded by a+p*b."""
    def __init__(self, p):
        self.p = p
        self.order = p*p
        self.nonsquare = next(n for n in range(2, p) if pow(n, (p-1)//2, p) != 1)
        coords = [(i % p, i // p) for i in range(self.order)]
        self.mul = [[(a*c + self.nonsquare*b*d) % p + p*((a*d+b*c) % p)
                     for c, d in coords] for a, b in coords]
        self.inverse = [0] + [row.index(1) for row in self.mul[1:]]

    def add(self, x, y):
        p = self.p
        return (x % p + y % p) % p + p*((x // p + y // p) % p)

    def neg(self, x):
        p = self.p
        return -x % p + p*(-(x // p) % p)

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def div(self, x, y):
        assert y != 0
        return self.mul[x][self.inverse[y]]

    def frobenius(self, x):
        p = self.p
        return x % p + p*(-(x // p) % p)


class Curve:
    """Monic y²=x³+a*x²+b*x. The point at infinity is represented by None."""
    def __init__(self, field, twist):
        self.field = field
        p = field.p
        self.a, self.b = 16*twist % p, 32*twist**2 % p
        mul, add = field.mul, field.add
        square_roots = {}
        for y in range(field.order):
            square_roots.setdefault(mul[y][y], []).append(y)
        points = [(x, y) for x in range(field.order)
                  for y in square_roots.get(mul[x][add(self.b, mul[x][add(x, self.a)])], [])]
        self.rational = [None] + [q for q in points if max(q) < p]
        self.nonrational_pairs = [(q, self.frobenius(q)) for q in points if q < self.frobenius(q)]

    def frobenius(self, q):
        return tuple(self.field.frobenius(z) for z in q)

    def neg(self, q):
        return None if q is None else (q[0], self.field.neg(q[1]))

    @lru_cache(None)
    def add(self, q, r):
        if q is None:
            return r
        if r is None:
            return q
        field = self.field
        add, sub, mul = field.add, field.sub, field.mul
        x, y = q
        u, v = r
        if x == u:
            if add(y, v) == 0:
                return None
            derivative = add(self.b, mul[x][add(2*self.a % field.p, mul[3][x])])
            slope = field.div(derivative, mul[2][y])
        else:
            slope = field.div(sub(y, v), sub(x, u))
        z = sub(sub(sub(mul[slope][slope], self.a), x), u)
        return z, sub(mul[slope][sub(x, z)], y)

    @lru_cache(None)
    def times(self, n, q):
        return self.add(q, self.times(n-1, q)) if n else None

    @lru_cache(None)
    def jets(self, q, m):
        """Evaluation of the first seven local coefficients of each basis section."""
        powers = (0, 2, 3, 4, 5, 6, 7, 8)
        if q is None:
            # The coordinate flags give precisely the vanishing conditions at O.
            return [[int(t == m-k) for t in powers[:m]] for k in range(7)]
        field = self.field
        add, sub, mul = field.add, field.sub, field.mul

        def product(left, right):
            result = []
            for k in range(7):
                coeff = 0
                for i in range(k+1):
                    coeff = add(coeff, mul[left[i]][right[k-i]])
                result.append(coeff)
            return result

        u, v = q
        x, y = [u]+[0]*6, [v]+[0]*6
        if v:
            x[1] = 1
            series = y
            derivative = mul[2][v]
        else:
            y[1] = 1
            series = x
            derivative = field.neg(add(self.b, mul[u][add(2*self.a % field.p, mul[3][u])]))
        for k in range(1, 7):
            xx = product(x, x)
            error = sub(sub(sub(product(y, y)[k], product(xx, x)[k]), mul[self.a][xx[k]]),
                        mul[self.b][x[k]])
            series[k] = field.div(field.neg(error), derivative)
        xx = product(x, x)
        basis = [[1]+[0]*6, x, y, xx, product(x, y), product(xx, x), product(xx, y), product(xx, xx)]
        return list(zip(*basis[:m]))

    def section(self, divisor, total, degree):
        """Cut out D+B in |mO|, with B=-sum(D) if sum(D) differs from O."""
        data = Counter(dict(divisor))
        if total is not None:
            data[self.neg(total)] += 1
        m = degree + int(total is not None)
        p = self.field.p
        rows = []
        for q, multiplicity in data.items():
            if q is not None and max(q) >= p and q > self.frobenius(q):
                continue
            for row in self.jets(q, m)[:multiplicity]:
                rows.append([a % p for a in row])
                if any(a >= p for a in row):
                    rows.append([a // p for a in row])
        pivots = []
        for col in range(m):
            i = len(pivots)
            j = next((k for k in range(i, len(rows)) if rows[k][col]), None)
            if j is None:
                continue
            pivots.append(col)
            rows[i], rows[j] = rows[j], rows[i]
            rows[i] = [x*pow(rows[i][col], -1, p) % p for x in rows[i]]
            for k, row in enumerate(rows):
                if k != i and row[col]:
                    rows[k] = [(x-row[col]*y) % p for x, y in zip(row, rows[i])]
        assert len(pivots) == m-1
        free, = set(range(m))-set(pivots)
        vector = [0]*m
        vector[free] = 1
        for k, col in enumerate(pivots):
            vector[col] = -rows[k][free] % p
        return vector


class PolynomialRing:
    """Coefficients are listed from lowest to highest degree, with [] for zero."""
    def __init__(self, p):
        self.p = p

    @staticmethod
    def trim(poly):
        while poly and not poly[-1]:
            poly.pop()
        return poly

    def divmod(self, a, b):
        a = a[:]
        quotient = [0]*max(0, len(a)-len(b)+1)
        inverse = pow(b[-1], -1, self.p)
        while len(a) >= len(b):
            i = len(a)-len(b)
            quotient[i] = factor = a[-1]*inverse % self.p
            for j, value in enumerate(b):
                a[i+j] = (a[i+j]-factor*value) % self.p
            self.trim(a)
        return quotient, a

    def gcd(self, a, b):
        while b:
            a, b = b, self.divmod(a, b)[1]
        return a

    def repeated_part(self, a):
        derivative = self.trim([i*a[i] % self.p for i in range(1, len(a))])
        return self.gcd(a, derivative)

    def radical_degree(self, a):
        return 0 if len(a) < 2 else len(a)-len(self.repeated_part(a))

    def multiplicity_classes(self, a):
        """Yield (e, squarefree polynomial with roots of multiplicity exactly e)."""
        e = 1
        while len(a) > 1:
            repeated = self.repeated_part(a)
            radical, rem = self.divmod(a, repeated)
            assert not rem
            still_repeated = self.gcd(radical, repeated)
            exact, rem = self.divmod(radical, still_repeated)
            assert not rem
            if len(exact) > 1:
                yield e, exact
            e, a = e+1, repeated

    def mul(self, a, b):
        result = [0]*(len(a)+len(b)-1) if a and b else []
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                result[i+j] = (result[i+j]+x*y) % self.p
        return result


def sections(curve, d):
    """Enumerate sections of support size 1, 2, and the required size-3 sections."""
    multiples = {curve.times(d, q) for q in curve.rational}
    remaining = set(curve.rational)-multiples
    representatives = [None]
    while remaining:
        q = min(remaining)
        representatives.append(q)
        remaining -= {curve.add(q, r) for r in multiples}
    groups = {s: {1: [], 2: [], 3: []} for s in representatives}

    def record(divisor, total):
        if total in groups:
            support = frozenset(q for q, k in divisor)
            shape = tuple(sorted((k for q, k in divisor), reverse=True))
            groups[total][len(support)].append((support, shape, curve.section(divisor, total, d)))

    for q in curve.rational:
        record([(q, d)], curve.times(d, q))
    for i in range(1, 1+d//2):
        for qi, q in enumerate(curve.rational):
            for r in curve.rational[(qi+1 if i == d-i else 0):]:
                if q != r:
                    record([(q, i), (r, d-i)], curve.add(curve.times(i, q), curve.times(d-i, r)))
        if 2*i == d:
            for q, r in curve.nonrational_pairs:
                record([(q, i), (r, i)], curve.times(i, curve.add(q, r)))
    if d == 7:
        # Three-point second fibers are needed only for fiber sizes 1,3,3.
        for i, j, k in [(1, 1, 5), (1, 2, 4), (1, 3, 3), (2, 2, 3)]:
            for qi, q in enumerate(curve.rational):
                for ri, r in enumerate(curve.rational):
                    if q == r or (i == j and qi >= ri):
                        continue
                    for vi, v in enumerate(curve.rational):
                        if v in (q, r) or (j == k and ri >= vi):
                            continue
                        total = curve.add(curve.times(i, q), curve.add(curve.times(j, r), curve.times(k, v)))
                        if total is None:
                            record([(q, i), (r, j), (v, k)], None)
            if i == j or j == k:
                h = i if i == j else j
                for q, r in curve.nonrational_pairs:
                    subtotal = curve.times(h, curve.add(q, r))
                    for v in curve.rational:
                        if curve.add(subtotal, curve.times(7-2*h, v)) is None:
                            record([(q, h), (r, h), (v, 7-2*h)], None)
    return groups


def divisor_data(curve, ring, vector, total):
    """Count distinct geometric zeros of the section A+yB, including infinity."""
    p, m = ring.p, len(vector)
    v = vector + [0]*(8-m)
    a = ring.trim([v[0], v[1], v[3], v[5], v[7]])
    b = ring.trim([v[2], v[4], v[6]])
    cubic = [0, curve.b, curve.a, 1]
    h = ring.gcd(a, b)
    aa, cbb = ring.mul(a, a), ring.mul(cubic, ring.mul(b, b))
    norm = ring.trim([((aa[i] if i < len(aa) else 0) - (cbb[i] if i < len(cbb) else 0)) % p
                      for i in range(max(len(aa), len(cbb)))])
    at_infinity = m - (len(norm)-1)
    size = (ring.radical_degree(norm) + ring.radical_degree(h)
            - ring.radical_degree(ring.gcd(h, cubic)) + int(at_infinity > 0))
    base_order = 0
    if total is not None:
        for row in curve.jets(curve.neg(total), m):
            if sum(x*y for x, y in zip(row, vector)) % p:
                break
            base_order += 1
        assert base_order > 0
        size -= int(base_order == 1)
    return size, (norm, h, cubic, at_infinity, base_order)


def partition(ring, data):
    norm, h, cubic, at_infinity, base_order = data
    counts = Counter()
    if at_infinity:
        counts[at_infinity] += 1
    for e, roots in ring.multiplicity_classes(norm):
        branch = ring.gcd(roots, cubic)
        counts[e] += len(branch)-1
        unramified, rem = ring.divmod(roots, branch)
        assert not rem
        leftover = len(unramified)-1
        for j, common_roots in ring.multiplicity_classes(h):
            number = len(ring.gcd(unramified, common_roots))-1
            if number:
                assert e >= 2*j
                counts[j] += number
                counts[e-j] += number
                leftover -= number
        counts[e] += leftover
    if base_order:
        counts[base_order] -= 1
        if base_order > 1:
            counts[base_order-1] += 1
    return tuple(sorted(counts.elements(), reverse=True))


def passports(curve):
    ring = PolynomialRing(curve.field.p)
    result = set()
    for d in range(3, 8):
        for total, group in sections(curve, d).items():
            for fibers in group.values():
                for _, shape, section in fibers:
                    size, data = divisor_data(curve, ring, section, total)
                    assert size == len(shape) and partition(ring, data) == shape

            def check_line(first, second):
                support1, shape1, left = first
                support2, shape2, right = second
                needed = d-len(shape1)-len(shape2)
                if support1 & support2 or needed < len(shape2):
                    return
                for c in range(1, ring.p):
                    vector = [(a+c*b) % ring.p for a, b in zip(left, right)]
                    size, data = divisor_data(curve, ring, vector, total)
                    if size == needed:
                        shape3 = partition(ring, data)
                        assert len(shape3) == size and sum(shape3) == d
                        result.add(tuple(sorted((shape1, shape2, shape3))))

            if total is None:
                origin = next(s for s in group[1] if s[0] == frozenset([None]))
                for size in range(1, 1+(d-1)//2):
                    for second in group[size]:
                        check_line(origin, second)
            if d >= 6:
                for first, second in combinations(group[2], 2):
                    check_line(first, second)
    return result


if __name__ == '__main__':
    results = []
    for p in (11, 19):
        field = QuadraticField(p)
        local = set()
        for twist in (1, field.nonsquare):
            curve = Curve(field, twist)
            found = passports(curve)
            print(p, twist, len(curve.rational), sorted(found), flush=True)
            local |= found
        results.append(local)
    assert results[0].isdisjoint(results[1])
    print("The sets of possible passports at 11 and 19 are disjoint.")
