"""Finite arithmetic for the congruent-six square-denominator proof."""


class QuadraticRing:
    """Pairs represent a+b*sqrt(3) modulo the indicated rational modulus."""

    def __init__(self, modulus):
        self.modulus = modulus
        self.zero = (0, 0)
        self.epsilon = (2, 1)
        self.coefficient = self.multiply(self.integer(-4), self.epsilon)

    def integer(self, value):
        return value % self.modulus, 0

    def add(self, left, right):
        return tuple((a + b) % self.modulus for a, b in zip(left, right))

    def negative(self, value):
        return tuple(-a % self.modulus for a in value)

    def subtract(self, left, right):
        return self.add(left, self.negative(right))

    def multiply(self, left, right):
        a, b = left
        c, d = right
        return (a*c + 3*b*d) % self.modulus, (a*d + b*c) % self.modulus

    def square(self, value):
        return self.multiply(value, value)

    def divide(self, left, right):
        a, b = right
        scale = pow(a*a - 3*b*b, -1, self.modulus)
        return self.multiply(left, self.multiply((a, -b), self.integer(scale)))

    def elliptic_add(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        x, y = left
        u, v = right
        if x == u and y == self.negative(v):
            return None
        if left == right:
            numerator = self.add(self.multiply(self.integer(3), self.square(x)), self.coefficient)
            slope = self.divide(numerator, self.add(y, y))
        else:
            slope = self.divide(self.subtract(y, v), self.subtract(x, u))
        new_x = self.subtract(self.subtract(self.square(slope), x), u)
        new_y = self.subtract(self.multiply(slope, self.subtract(x, new_x)), y)
        return new_x, new_y

    def points(self):
        elements = [(a, b) for a in range(self.modulus) for b in range(self.modulus)]
        squares = {}
        for y in elements:
            squares.setdefault(self.square(y), []).append(y)
        result = [None]
        for x in elements:
            value = self.multiply(x, self.add(self.square(x), self.coefficient))
            result.extend((x, y) for y in squares.get(value, []))
        return result


def quartic_residues():
    result = []
    for u, v in [(u, 1) for u in range(7)] + [(1, 0)]:
        value = u**4 + 6*u**3*v + 18*u*u*v*v + 18*u*v**3 + 9*v**4
        result.extend((u, v, z) for z in range(7) if (z**4 - value) % 7 == 0)
    return result


def main():
    assert len(QuadraticRing(5).points()) == 32
    field = QuadraticRing(7)
    curve_points = field.points()
    assert len(curve_points) == 36
    for point in curve_points:
        triple = field.elliptic_add(field.elliptic_add(point, point), point)
        assert field.elliptic_add(triple, triple) is None

    p = (field.integer(-1), field.epsilon)
    subgroup = [None]
    point = p
    while point is not None:
        subgroup.append(point)
        point = field.elliptic_add(point, p)
    assert len(subgroup) == 6 and subgroup[3] == (field.zero, field.zero)

    residues = quartic_residues()
    assert len(residues) == 8
    survivors = []
    for u, v, z in residues:
        assert z != 0
        x = field.divide((u, v), field.integer(z))
        y = field.divide((u, -v), field.integer(z))
        image = (field.negative(field.square(y)),
                 field.multiply(field.epsilon, field.multiply(field.square(x), y)))
        if image in subgroup:
            survivors.append((u, v, z))
    assert survivors == [(1, 0, 1), (1, 0, 6)]

    ring = QuadraticRing(49)
    p = (ring.integer(-1), ring.epsilon)
    triple = ring.elliptic_add(ring.elliptic_add(p, p), p)
    assert triple == ((0, 0), (0, 35))
    first_log = ring.divide(ring.add(triple[1], triple[1]), ring.coefficient)
    assert first_log == (28, 14)
    print("Reduced group orders at 5,7 are 32,36. The group at 7 has exponent 6.")
    print("The two surviving quartic reductions are", survivors)
    print("The coefficients of log(6P)/7 modulo 7 are (4,2).")


if __name__ == "__main__":
    main()
