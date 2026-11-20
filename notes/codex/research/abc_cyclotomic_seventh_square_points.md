# Rational square values of the seventh and fourteenth cyclotomic forms

The rational projective slopes \([A:B]\) on \(Z^2=\Phi_7(A,B)\) are exactly
\([0:1],[-1:1],[1:0]\), each with two signs for \(Z\). Substitution
\(B\mapsto-B\) gives \([0:1],[1:1],[1:0]\) at index \(14\).
For \(\Phi_7(A,B)=7Z^2\) the only slope is \([1:1]\), and for
\(\Phi_{14}(A,B)=7Z^2\) the only slope is \([-1:1]\). In particular
neither form has squarefree kernel \(1\) or \(7\) for coprime integers
\(A>B>0\).
The proof uses full two-descent over a real cubic field and one residue
prime for elliptic Chabauty. All finite computations below are reproduced
by a standard-library Python program. [Verifier](abc_cyclotomic_seventh_square_points.py)

## The cubic-field cover

Let \(a=2\cos(2\pi/7)\), \(b=a^2-2\), \(c=-1-a-b\). These are the
conjugate roots of \(g(T)=T^3+T^2-2T-1\). The field \(K=\mathbf Q(a)\)
is cyclic cubic, with \(\mathcal O_K=\mathbf Z[a]\) and discriminant \(49\).
Indeed \(g\) is irreducible and has discriminant \(49\), and a proper
index for \(\mathbf Z[a]\) would give field discriminant \(1\), impossible
by Minkowski. The ideal class bound \(6\sqrt{49}/27<2\) gives class
number one. The unit generators \(-1,a,b\) have independent signature
vectors, since \(a,b\) have distinct positive positions and are negative
at their other two embeddings. By Dirichlet's theorem their classes
generate \(\mathcal O_K^\times/\mathcal O_K^{\times2}\).

Take \(A,B\) primitive. The three factors \(A^2-iAB+B^2\) for
\(i\in\{a,b,c\}\) multiply to \(\Phi_7(A,B)\). They are totally positive
because \(|i|<2\). A common prime ideal of two factors cannot divide
\(AB\), so it divides a difference of conjugates and consequently lies
above \(7\). Modulo \(7\) the form equals \((A-B)^6\). When \(7\mid A-B\)
its \(7\)-adic valuation is one, by expanding
\(((B+(A-B))^7-B^7)/(A-B)\), with the same value \(7B^6\) when \(A=B\).
Thus a square value is prime to \(7\). The three principal ideals are
then pairwise coprime with square product, so each has even valuations.
Class number one and the unit signatures make each individual factor a
square in \(K\).

Assume \(AB\ne0\). Put \(t=A/B,\ S=t+t^{-1}\). From the two factors for
\(b,c\), \((S-b)(S-c)\) is a square in \(K\), and \(S^2-4=(t-t^{-1})^2\).
Hence \(V^2=(S-2)(S+2)(S-b)(S-c)\) for some \(V\in K\). Set
\[
 h=4(2-b)(2-c),\qquad (D_1,D_2,D_3)=(h/4,h/(2-b),h/(2-c)).
\]
For \(S\ne2\) the change \(X=h/(S-2),\ Y=hV/(S-2)^2\) gives
\[
                  E\colon Y^2=\prod_{i=1}^3(X+D_i).
\]
In the basis \(1,a,a^2\) the \(D_i\) are \((4,3,1),(4,4,4),(16,0,-4)\).
The rational function on \(E\) recovering the target is \(S=2+h/X\).
It is \(2\) at \(O\), has poles at \(\pm P=(0,\pm h)\), and equals \(-2\)
at \(T=(-D_1,0)\). The slope \(t=1\) giving \(S=2\) has \(\Phi_7(1,1)=7\).

## Full two-descent over the cubic field

The full two-descent map uses the squareclasses of \(X+D_1,X+D_2\) in
\(K^\times/K^{\times2}\). At a two-torsion point, replace the vanishing
factor by the product of the other two. Send \(O\) to the identity pair.
This is the standard Kummer injection of \(E(K)/2E(K)\) for three
rational roots. Multiplicativity follows by intersecting a line with the
cubic and evaluating at each root. Trivial squareclasses give a rational
half by the tangent construction in the [ninth-index proof](abc_cyclotomic_sextic_square_points.md).
The same descriptions apply over each completion.

The norms of \(D_1-D_2,D_1-D_3,D_2-D_3\) are \(-7,-7,-448\).
At any prime away from \(2,7\), integral \(X\) makes at most one
\(X+D_i\) a nonunit, hence its valuation is even. For nonintegral \(X\)
all three valuations equal \(v(X)\), which is even by the equation.
The torsion formulas give the same even valuations. The prime \(2\) is
inert by \(g\bmod2\), and \(7\) is totally ramified with uniformizer
\(\pi=2-a\), since \(\pi^3=7(a-1)^2\) and \(N(\pi)=7\).
Each global coordinate is therefore a product of a subset of
\(\{-1,a,b,2,\pi\}\), modulo squares. This gives \(32^2=1024\) pairs.

Order the embeddings by the images \(2\cos(2\pi/7),2\cos(4\pi/7),
2\cos(6\pi/7)\) of \(a\). At each embedding \(D_1\) is the smallest
of the three. The inequality \(D_2<D_3\) holds only at the middle
embedding. For a real point the first two coordinate signs are either
\((+,+)\) or \((-,+),(-,-),(-,+)\), respectively, at the three
embeddings. This follows directly from the intervals where the cubic
is nonnegative, also taking the limits at its roots.

For the primes above \(7\) and \(2\), the local images have orders \(4\)
and \(32\). To see this, take a sufficiently small open subgroup \(U\)
identified with an additive lattice by the formal logarithm. Then
\([E(K_v):2E(K_v)]=\#E[2](K_v)[U:2U]\), by comparing indices above
\(2U\). Here the first factor is four and the second is one or eight.
The following local abscissae generate subgroups of those exact sizes.

| Place | Generating abscissae |
|---|---|
| Above \(7\) | \(-D_1,-D_2\) |
| Above \(2\) | \(-D_1,-D_2,-2a^2,2a^2,1-a\) |

The verifier checks that the product of the three factors at each
nontorsion abscissa is a local square, so the required local points
exist. At \(7\) a class is its valuation parity and the Legendre sign
of its unit part in \(\mathbf F_7\), with \(a\equiv2\bmod\pi\).
At \(2\) one uses valuation parity and the class of the unit part
modulo squares in \((\mathcal O_K/8)^\times\). This suffices because
every unit congruent to one modulo eight is a square by Hensel's lemma.
Enumerating the generated local subgroups and filtering the global pairs
gives the following counts.

| Conditions imposed cumulatively | Pairs |
|---|---:|
| Global support | 1024 |
| Three real signatures | 128 |
| Local image at \(7\) | 32 |
| Local image at \(2\) | 8 |

Thus \(\#E(K)/2E(K)\le8\). The three nonzero rational two-torsion points
give \(\dim_{\mathbf F_2} E(K)[2]=2\), so \(\operatorname{rank}E(K)\le1\).
The formal computation below exhibits the infinite-order point \(P\),
giving equality.

## The four residue disks at \(3\)

The polynomial \(g\) is irreducible modulo \(3\), and the roots
\(-D_i\) are distinct there. The completion is unramified, with residue
field \(k=\mathbf F_{27}=\mathbf F_3[\bar a]\), and \(E\) has good
reduction. If \(t\in\mathbf Q^\times\), the reduction of \(S=t+t^{-1}\)
is \(\infty\) when \(v_3(t)\ne0\), and otherwise it is \(2\) or \(-2\).
It follows from \(X=h/(S-2)\) and the reduced equation that a candidate
on \(E(K)\) reduces to one of \(\pm P,O,T\) defined above.

For \(R\) in the kernel of reduction use \(\tau(R)=-X(R)/Y(R)\).
Direct doubling gives \(4P\equiv T\bmod3\), and \(8P\) has
\[
          v_3(\tau(8P))=1,\qquad \tau(8P)/3\bmod3
                   =w=1+2\bar a+\bar a^2 .
\]
For an explicit modulo-nine computation, double \(P\) twice using
integral unit denominators. At \(4P=(x_4,y_4)\), \(y_4\equiv0\bmod3\)
and \(f'(x_4)\) is a unit for \(f(X)=\prod_i(X+D_i)\). The tangent
slope for doubling \(4P\) is \(m=f'(x_4)/(2y_4)\), so
\(\tau(8P)\equiv 1/m\bmod9\) when \(v_3(y_4)=1\).
The verifier computes \(2(y_4/3)/f'(x_4)\bmod3=w\).

On this unramified \(3\)-adic formal group the logarithm is injective
on the kernel of reduction and has the same leading coefficient as its
parameter. Indeed integration of the invariant differential gives a
coefficient in \(j^{-1}\mathcal O_{K_3}\) in degree \(j\), and for
\(v_3(\tau)\ge1,\ j\ge2\), \(jv_3(\tau)-v_3(j)>v_3(\tau)\).
Thus \(8P\) has nonzero logarithm. If \(R\ne O\) is any global point in
that kernel, rank one gives a nontrivial rational linear dependence of
\(R,8P\) modulo torsion. The kernel has no torsion, so their logarithms
are rational multiples of each other. In particular, writing
\(j=v_3(\tau(R))\), the initial residue
\(\tau(R)/3^j\bmod3\) is an \(\mathbf F_3^\times\)-multiple of \(w\).
This argument works with the given point \(P\) regardless of its index
in the free part of \(E(K)\).

Translate a proposed point by its disk center and write the difference
as \(R\). For \(R\ne O\), the following are the first terms in \(\tau=\tau(R)\)
of functions which must have rational values. The last column evaluates
the coefficient times the indicated power of \(w\), up to sign.

| Center | First term | Residue after removing the power of \(3\), up to \(\mathbf F_3^\times\) |
|---|---|---|
| \(O\) | \(S-2=h\tau^2+O(\tau^3)\) | \(1+\bar a+\bar a^2\) |
| \(P\) or \(-P\) | \(1/S=\pm2\tau+O(\tau^2)\) | \(2+\bar a+2\bar a^2\) |
| \(T\) | \(S+2=-h(D_2-D_1)(D_3-D_1)\tau^2/D_1^2+O(\tau^3)\) | \(2+\bar a^2\) |

All error terms have integral coefficients at \(3\). At \(O\) use
\(1/X(R)=\tau^2+\cdots\). At \(\pm P\), invariance of \(dX/(2Y)\)
gives \(X(\pm P+R)=\pm2h\tau+\cdots\) and \(1/S=X/(2X+h)\).
At \(T\) the two-torsion translation formula gives
\[
 X(T+R)=-D_1+(D_2-D_1)(D_3-D_1)/(X(R)+D_1).
\]
None of the displayed initial residues is in \(\mathbf F_3\).
A nonzero rational number has initial residue in \(\mathbf F_3^\times\),
so each disk contains only its center among points with the required
rational value of \(S\). The centers \(\pm P\) give a pole. For finite
nonzero \(t\) the remaining values are \(S=\pm2\), giving \(t=\pm1\).
The value at \(t=-1\) is one and the value at \(t=1\) is seven.
The omitted slopes with \(AB=0\) also give one in primitive coordinates.

## Squarefree kernel seven

Suppose \(\Phi_7(A,B)=7Z^2\) with primitive \(A,B\). Then \(7\mid A-B\)
and \(7\nmid AB\). For each \(i=a,b,c\), the element \(2-i\) generates the
unique prime above \(7\). The factor
\[
            A^2-iAB+B^2=(A-B)^2+(2-i)AB
\]
has valuation one there. Its valuations away from \(7\) are even by
pairwise coprimality. Dividing by \(2-i\) leaves a totally positive
element with even valuations, hence a square in \(K\). Multiplying the
results for \(i=b,c\) again makes \((S-b)(S-c)\) a square, since
\[
          (2-b)(2-c)=\frac{7}{2-a}
                    =\left(\frac{2-a}{a-1}\right)^2 .
\]
Thus the same elliptic curve and the same residue disks restrict the
slopes to \([0:1],[-1:1],[1:1],[1:0]\). Exactly \([1:1]\) has squarefree
kernel seven. Substitution \(B\mapsto-B\) gives the result at \(14\).
