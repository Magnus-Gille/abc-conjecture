# Higher first-order arithmetic Wronskians do not amplify the bound

Author: codex  
Date: 2026-07-25

This addresses agenda branch B without repeating the field-status work assigned
to Claude.

Let `T(a,b)` be the lattice of derivations satisfying the chosen additivity
condition for `a+b=c`, and let

    W_x = a D_x(b) - b D_x(a).

The map `x -> W_x` is an integer linear functional on `T(a,b)`. Its kernel is
the degenerate lattice `T°(a,b)`. As already verified,

    rank T(a,b)  = omega(abc)-1,
    rank T°(a,b) = omega(abc)-2.

Therefore the quotient carrying all Wronskian information,

    T(a,b) / T°(a,b),

has rank one.

## Consequence 1: every alternating higher determinant vanishes

Take two derivations `x,y in T(a,b)`. The natural logarithmic-differential row
for a derivation is

    (D_x(a)/a - D_x(c)/c,
     D_x(b)/b - D_x(c)/c).

Using `D_x(c)=D_x(a)+D_x(b)` and `a+b=c`, this row equals

    (-W_x/(ac), W_x/(bc)).

It is a scalar multiple of the fixed vector `(-1/(ac),1/(bc))`. Hence the
2-by-2 determinant formed from the rows for `x` and `y` is identically zero.
Equivalently, the exterior square of the rank-one quotient is zero. The same
argument kills every alternating `k`-derivation determinant for `k >= 2`.

The even more direct 3-by-3 candidate

    det [[a,      b,      c],
         [D_x(a),D_x(b),D_x(c)],
         [D_y(a),D_y(b),D_y(c)]]

also vanishes, because its third column is the sum of its first two columns.

## Consequence 2: multiplying ordinary Wronskians gives no gain

For nondegenerate `x_1,...,x_k`, each ordinary Wronskian satisfies

    abc/R <= |W_(x_i)| <= ab H(x_i) log_2 c.

Multiplying and taking the `k`-th root gives only

    c <= R (product_i H(x_i))^(1/k) log_2 c,

the original estimate with `H` replaced by its geometric mean. Divisibility
gain and coefficient cost scale by exactly the same factor.

## Scope of the negative result

This closes amplification *within the inherited first-order framework*. A
nonzero higher construction would have to add genuinely new data: different
additive equations, or iterated arithmetic derivatives. The latter are not a
free extension: applying one arithmetic derivative creates prime factors
outside `abc`, and the next derivative no longer has the support/additivity
properties used in the divisibility proof. No such controlled higher theory is
present in the inherited argument.

