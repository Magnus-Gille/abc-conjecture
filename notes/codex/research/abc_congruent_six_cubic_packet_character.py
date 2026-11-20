"""Verify the Gaussian denominator character at 193 for G=(-3,9)."""


def add(left, right, prime):
    if left is None:
        return right
    if right is None:
        return left
    x, y = left
    u, v = right
    if x == u and (y + v) % prime == 0:
        return None
    if left == right:
        slope = (3 * x * x - 36) * pow(2 * y, -1, prime)
    else:
        slope = (v - y) * pow(u - x, -1, prime)
    new_x = (slope * slope - x - u) % prime
    return new_x, (slope * (x - new_x) - y) % prime


def main():
    prime = 193
    generator = (-3 % prime, 9)
    multiples = [None]
    point = generator
    while point is not None:
        multiples.append(point)
        point = add(point, generator, prime)
    assert len(multiples) == 26

    cubic_index = {pow(2, j, 13): j % 3 for j in range(12)}
    assert len(cubic_index) == 12
    signs = (1, -1, 1)
    counts = [[0] * 3 for _ in range(3)]
    for a in range(1, 26, 2):
        for b in range(0, 26, 2):
            if (a * a + b * b) % 13 == 0:
                continue
            x_index = cubic_index[(a + 5 * b) % 13]
            y_index = cubic_index[(a - 5 * b) % 13]
            counts[x_index][y_index] += 1

            if multiples[b] is None:
                character = 1
            else:
                x_sum = (multiples[a][0] + multiples[b][0]) % prime
                character = pow(x_sum, (prime - 1) // 2, prime)
            assert character == signs[x_index] * signs[y_index] % prime

    assert counts == [[16, 16, 16]] * 3
    assert (cubic_index[11], cubic_index[4]) == (1, 2)  # 1+2i
    print("ord_193(G) = 26. All 144 unit pairs passed, 16 in each cell.")
    for left_sign in signs:
        print(" ".join("+" if left_sign * right_sign == 1 else "-"
                       for right_sign in signs))
    print("32 of 144 residue pairs have opposite nonzero cubic indices.")


if __name__ == "__main__":
    main()
