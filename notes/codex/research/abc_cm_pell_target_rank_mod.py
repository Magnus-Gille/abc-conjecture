"""Exact multiplicative-rank certificate for the fifty full CM Pell targets."""

from math import isqrt

P = 9241
SQRT_TWO = 2863
TAU = 3220
BASE = (2122, 2151)
INDICES = [(j,k) for j in range(10) for k in range(5)]


def add(left, right):
    if left is None:
        return right
    if right is None:
        return left
    x, y = left
    u, v = right
    if x == u and (y+v) % P == 0:
        return None
    if left == right:
        slope = (3*x*x + 32*x + 32)*pow(2*y,-1,P) % P
    else:
        slope = (v-y)*pow(u-x,-1,P) % P
    X = (slope*slope - 16 - x - u) % P
    return X, (slope*(x-X)-y) % P


def multiply(point, n):
    result = None
    while n:
        if n % 2:
            result = add(result,point)
        point = add(point,point)
        n //= 2
    return result


def scalar_product(i, j):
    a, b = (i[0]+j[0]) % 10, (i[1]+j[1]) % 10
    return ((a+5) % 10, b-5) if b >= 5 else (a,b)


def determinant_mod_five(M):
    rows = [row.copy() for row in M]
    result = 1
    for j in range(len(rows)):
        pivot = next((i for i in range(j,len(rows)) if rows[i][j] % 5),None)
        if pivot is None:
            return 0
        if pivot != j:
            rows[j],rows[pivot] = rows[pivot],rows[j]
            result = -result
        result = result*rows[j][j] % 5
        inverse = pow(rows[j][j],-1,5)
        for i in range(j+1,len(rows)):
            scalar = rows[i][j]*inverse % 5
            for k in range(j,len(rows)):
                rows[i][k] = (rows[i][k] - scalar*rows[j][k]) % 5
    return result % 5


def main():
    assert all(P % n for n in range(2,isqrt(P)+1))
    assert SQRT_TWO**2 % P == 2 and TAU**2 % P == P-2
    x, y = BASE
    assert y*y % P == (x**3+16*x*x+32*x) % P
    assert multiply(BASE,11) is None
    tau_point = (-(x+16+32*pow(x,-1,P))*pow(2,-1,P) % P,
                 TAU*y*(1-32*pow(x,-2,P))*pow(4,-1,P) % P)
    assert tau_point == (1091,4736)
    assert add(multiply(BASE,3),tau_point) is not None
    assert add(multiply(BASE,3),(tau_point[0],-tau_point[1] % P)) is not None
    character_base = pow(13,(P-1)//5,P)
    lookup = {pow(character_base,i,P): i for i in range(5)}
    assert len(lookup) == 5
    characters = {}
    targets = set()
    for j,k in INDICES:
        s,t = pow(2,j,11),pow(2,k,11)
        a,b = (s+t)*6 % 11,(s-t)*2 % 11
        u,_ = add(multiply(BASE,a),multiply(tau_point,b))
        target = (-8+4*SQRT_TWO-u)*pow(u+8+4*SQRT_TWO,-1,P) % P
        targets.add(target)
        characters[j,k] = lookup[pow(target,(P-1)//5,P)]
    assert len(targets) == 50
    matrix = [[characters[scalar_product(i,j)] for j in INDICES] for i in INDICES]
    determinant = determinant_mod_five(matrix)
    assert determinant != 0
    print(f"At {P} all 50 targets are distinct and the character determinant is {determinant} modulo 5.")


if __name__ == "__main__":
    main()
