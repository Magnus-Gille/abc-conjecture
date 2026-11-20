# Rational square values of the ninth and eighteenth cyclotomic forms

The rational projective slopes \([A:B]\) for which
\(\Phi_9(A,B)=A^6+A^3B^3+B^6\) is a square are exactly
\([0:1],[-1:1],[1:0]\). For \(\Phi_{18}(A,B)=\Phi_9(A,-B)\) the list is
\([0:1],[1:1],[1:0]\). Each slope gives two points on the smooth projective
genus-two curve. In particular neither form is a square for coprime
integers \(A>B>0\). Scaling \(A,B\) by a nonzero rational multiplies the
form by a sixth power, so the condition on a projective slope is well-defined.

## The elliptic quotient

Take \(A+B\ne0\), put \(s=(A-B)/(A+B)\), and suppose \(z^2=\Phi_9(A,B)\).
Then \(u=s^2\) and \(v=8z/(A+B)^3\) satisfy
\[
                 v^2=u^3+33u^2+27u+3 .
\]
The change \(X=(u+11)/4,\ Y=v/8\) gives
\[
                   E\colon Y^2=X^3-21X+37 .
\]
We prove below that \(E(\mathbf Q)=\{O,(3,1),(3,-1)\}\). Thus \(u=1\),
so \(A=0\) or \(B=0\). The missing slope \(A+B=0\) gives \(\Phi_9=A^6\).
Each of the three listed slopes attains a nonzero square.

## An explicit descent on \(E\)

Let \(\theta^3-3\theta+1=0\), \(K=\mathbf Q(\theta)\), and
\(\lambda=2+2\theta-\theta^2\). The defining cubic for \(\theta\) is
irreducible by the rational root test. Its discriminant is \(81\), so
\(K\) is Galois and totally real. Direct substitution gives the minimal
polynomial \(f(T)=T^3-21T+37\) of \(\lambda\), again of discriminant \(81\).
For example, the change from \(1,\theta,\theta^2\) to \(1,\lambda,\lambda^2\)
has determinant of absolute value one. Minkowski's discriminant bound gives
\(\sqrt{|D_K|}\ge 27/6\). A proper index for \(\mathbf Z[\theta]\) would
give discriminant \(9\) or \(1\), so \(\mathcal O_K=\mathbf Z[\theta]=
\mathbf Z[\lambda]\). Each ideal class has an integral representative of
norm at most \((6/27)\sqrt{81}=2\). The cubic for \(\theta\) is irreducible
modulo \(2\), so \(2\) is inert and there is no ideal of norm \(2\).
Thus \(K\) has class number one.

Write a finite rational point as \(X=a/d^2,\ Y=b/d^3\), with \(d>0\) and
\(\gcd(a,d)=1\). These denominator exponents follow directly from the monic
Weierstrass equation at every prime where \(X\) has negative valuation. The
element \(\alpha=a-\lambda d^2\) has norm \(b^2\). It is nonzero because
\(f\) is irreducible. If a prime ideal above \(\ell\) divides \(\alpha\),
then \(\ell\nmid d\) and \(\lambda\) reduces to \(a/d^2\in\mathbf F_\ell\).
Since \(\mathcal O_K=\mathbf Z[\lambda]\), there is just one prime above
\(\ell\) with that reduction, and its residue degree is one. This argument
also applies at the ramified prime \(3\). The valuation of \(\alpha\)
therefore equals the valuation of its norm at \(\ell\), which is even.
The class number calculation gives \(\alpha=\epsilon h^2\) with
\(h\in\mathcal O_K\) and \(\epsilon\) a unit.

The three conjugates of the unit \(\theta\) each have one negative and
two positive embeddings, with distinct negative positions. They realize
independent sign vectors. Dirichlet's unit theorem gives
\(\#(\mathcal O_K^\times/\mathcal O_K^{\times2})=8\), so the signatures
determine the unit squareclasses. The negative conjugate of \(\theta\)
lies between \(-2\) and \(-1\), and its conjugate of \(\lambda\) is negative.
The other two conjugates of \(\theta\) lie in \((0,2)\), where
\(2+2\theta-\theta^2>0\). Since \(f(X)=Y^2>0\), the conjugates of
\(X-\lambda\) are either all positive or positive only at the negative
conjugate of \(\theta\). It follows that \(\epsilon\) represents \(1\)
or \(-\theta\) modulo squares.

To exclude \(-\theta\), reduce in the basis \(1,\theta,\theta^2\) modulo
\(4\). The square of \(h\) depends only on \(h\bmod 2\). For the eight
choices \(h=i+j\theta+k\theta^2\), \(i,j,k\in\{0,1\}\), the coefficient
triples of \(-\theta h^2\) form the set
\[
 \{(0,0,0),(0,2,3),(0,3,0),(1,0,1),
    (1,0,2),(1,1,0),(2,3,1),(3,3,1)\}.
\]
These follow by replacing \(\theta^3\) by \(3\theta-1\). For even \(d\),
\(a-\lambda d^2\) has triple \((1,0,0)\) or \((3,0,0)\). For odd \(d\)
it has triple \((a-2,2,1)\). Neither case occurs in the displayed set.
Thus \(X-\lambda\) is a square in \(K\) for every rational point.

For completeness this last condition makes the point a rational double.
Choose \(r\in K\) with \(r^2=X-\lambda\). Choose its sign so that its
three conjugates have product \(-Y\), and write \(s_1,s_2\) for their
first and second elementary symmetric functions. These are rational.
The line \(L(T)=-Y-s_1(T-X)\) satisfies
\[
                   f(T)-L(T)^2=(T-X)(T-X-s_2)^2 .
\]
This identity follows by expanding
\(f(T)=\prod_i(T-X+r_i^2)\). The line passes through \((X,-Y)\)
and is tangent at the rational point of abscissa \(X+s_2\). The group
law makes the latter point a half of \((X,Y)\), including when the
intersections coincide. Hence multiplication by two is surjective on
\(E(\mathbf Q)\). Finite generation gives rank zero.

The curve has good reduction at \(5\) and \(7\). Counting the solutions of
its displayed equation gives \(\#E(\mathbf F_5)=3\) and
\(\#E(\mathbf F_7)=9\), including infinity. Prime-to-residue-characteristic
torsion injects under good reduction, so \(\#E(\mathbf Q)\) divides three.
Both \((3,1)\) and \((3,-1)\) lie on the curve, finishing the computation.

## The cofactor three

For coprime $A>B>0$, neither $\Phi_9(A,B)$ nor $\Phi_{18}(A,B)$ is three times a square. For $\Phi_9$ on the rational projective line the only slope giving three times a square is $[1:1]$. For $\Phi_{18}$ it is $[-1:1]$.

Indeed, suppose $\Phi_9(A,B)=3z^2$ and both $A+B$ and $A-B$ are nonzero. With $s=(A-B)/(A+B)$ and $v=8z/(A+B)^3$ one obtains
$$
           3v^2=s^6+33s^4+27s^2+3 .
$$
Put $q=1/s^2$, $w=v/s^3$. Then $3w^2=3q^3+27q^2+33q+1$. The substitution $x=9q$, $y=27w$ gives $y^2=x^3+81x^2+891x+243$. With $X=(x+27)/4$, $Y=y/8$ this is
$$
                 E'\colon Y^2=X^3-81X+243 .
$$
We show that $E'(\mathbf Q)$ has only the point at infinity. The excluded slopes $A=B$ and $A=-B$ give $\Phi_9=3A^6$ and $\Phi_9=A^6$, respectively, completing the assertion. Replacing $B$ by $-B$ gives the result for $\Phi_{18}$.

Use the same cubic field and the same descent as above, now with $\lambda'=3(2+\theta-\theta^2)$. Its minimal polynomial is $f'(X)=X^3-81X+243$ (the prime here labels the second curve). This polynomial has discriminant $3^{12}$. Thus $\mathbf Z[\lambda']$ has index a power of $3$ in $\mathcal O_K$. Away from $3$, evaluation at $\lambda'=a/d^2\bmod\ell$ selects at most one prime ideal, of degree one, just as in the first descent. Above $3$ there is only one prime of degree one, since $\mathcal O_K/(3)=\mathbf F_3[\theta]/((\theta+1)^3)$. The square norm again forces every ideal valuation of $a-\lambda'd^2$ to be even.

The embedding where $\theta<-1$ makes $\lambda'=3(2-\theta)(1+\theta)$ negative and the other two embeddings make it positive. Thus the only unit squareclasses to consider are again $1$ and $-\theta$. For even $d$ the same mod-4 obstruction applies as before. For odd $d$ the coefficient triple of $a-\lambda'd^2$ is $(a-2,1,3)\bmod4$, absent from the same eight-entry table. The tangent-line halving calculation above applies to this cubic as well. It proves that $E'(\mathbf Q)$ has rank zero. Counting points at the two good primes gives $\#E'(\mathbf F_5)=3$ and $\#E'(\mathbf F_7)=7$. Prime-to-characteristic torsion injects at each, so the torsion is trivial.

## The other critical sextics and the large-prime cube condition

For \(\Phi_7\), the same \(s,u,v\) give
\(v^2=u^3+21u^2+35u+7\). More generally, if the right side is
\(u^3+bu^2+cu+d\), the second quotient has coordinates
\(X=d/s^2,\ Y=dv/s^3\) and equation
\(Y^2=X^3+cX^2+bdX+d^2\). PARI/GP's \(\mathrm{ellrank}\) and
\(\mathrm{elltors}\) give the following ranks and torsion orders.

| Index | Quotient coefficients \((a_2,a_4,a_6)\) | Rank interval | Torsion order |
|---|---|---|---|
| 7 | \((21,35,7)\) | \([1,1]\) | 1 |
| 7 | \((35,147,49)\) | \([1,1]\) | 1 |
| 9 | \((33,27,3)\) | \([0,0]\) | 3 |
| 9 | \((27,99,9)\) | \([1,1]\) | 3 |

These rows can be reproduced with
\(\mathrm{ellinit}([0,a_2,0,a_4,a_6])\). At index \(7\) both quotients
have positive rank. Passing to a real cubic field and applying elliptic
Chabauty gives exactly \([0:1],[-1:1],[1:0]\), and substitution
\(B\mapsto-B\) gives the index-\(14\) list.
[Seventh-index proof and verifier](abc_cyclotomic_seventh_square_points.md)

For \(A>B>0\) coprime and prime \(p>A^2\), divisibility of \(\Phi_n(A,B)\)
by \(p^3\) forces \(\Phi_n(A,B)=p^3\) for \(n=7,9\). Indeed the positive
integer multiplier is strictly less than \(7\) or \(3\), respectively, by
the coefficient sums and \(p^3>A^6\). Both values are odd. At index \(7\)
neither \(3\) nor \(5\) can divide: a prime \(\ell\ne7\) dividing the form
must give \(A/B\) exact multiplicative order \(7\bmod\ell\), by separability
of \(T^7-1\). This removes all possible multipliers other than \(1\).
For \(n=14,18\) the positive form is strictly less than \(A^6\), by
\(\Phi_{14}=(A^7+B^7)/(A+B)\) and
\(\Phi_{18}=A^6-A^3B^3+B^6\). A cube \(p^3\) with \(p>A^2\) cannot
divide either. At \(7,9\), deciding whether the remaining exact prime
cubes occur requires a separate argument for the cubic covers.

A standard-library script checks both cubic equations, the mod-four obstructions, the point counts at the two good primes, and sample substitutions used in the order theorem. [Arithmetic verifier](abc_cyclotomic_ninth_descent_check.py)
