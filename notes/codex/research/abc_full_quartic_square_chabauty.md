# The only square denominator on the full quartic signature

The only primitive solution in positive integers of
\[
                         a^4+3b^2=4v^8
\]
is \((a,b,v)=(1,1,1)\). Equivalently, on \(E_6:Y^2=X^3-36X\), the square-root denominator \(w_n=B(n(-3,9))\) at a positive odd index is a square precisely at \(n=1\). Allowing signed coordinates introduces the corresponding sign choices. The argument below uses a unique elliptic cover over \(\mathbf Q(\sqrt3)\) with rank one. [Full parametrization](abc_full_quartic_signature.md)

## A single quadratic-field cover

On \(E_0:Y^2=X^3+36X^2+36X\) with \(P=(-2,8)\), the full parametrization gives \(X(nP)=-2x^2/y^2\) with \(x,y>0\) coprime odd and \(3\nmid x\), and
\[
   x^4-18x^2y^2+9y^4=-8a^2,\qquad
   w_n=(x^2+3y^2)/4 .
\]
Suppose \(w_n=v^2\). Write \(r=x/y\), so \(r^2+3=(2v/y)^2\). Over \(K=\mathbf Q(t)\), \(t=\sqrt3>0\), put \(\delta=1+t\), \(\epsilon=2+t\). Its integer ring is \(\mathbf Z[t]\), its class number is one by the Minkowski bound \(\sqrt{12}/2<2\), and its units are \(\pm\epsilon^{\mathbf Z}\) by the elementary Pell equation for 3. Both 2 and 3 ramify, generated as prime ideals by \(\delta\) and \(t\), respectively.

The two conjugates of \(H=x^2+2txy-3y^2\) have product \(-8a^2\). A common odd prime ideal would divide \(4txy\). Primitivity and \(3\nmid x\) exclude this. Thus \(H\) has even valuation at every odd place and valuation three at the unique dyadic place, using \(a\) odd. At the chosen embedding \(H>\bar H\) and \(H\bar H<0\), so its signs agree with those of \(\delta\). It follows that \(H=\delta\epsilon^j A^2\) with \(A\in K\). At the prime \((t)\), \(H\equiv x^2\equiv1\), \(\delta\equiv1\) and \(\epsilon\equiv-1\), so \(j\) is even. Consequently every prospective solution lifts to
\[
  \mathcal C:\quad \delta W^2=(r^2+3)(r^2+2tr-3),\qquad r\in\mathbf Q_{>0}.
\]
The points at \(r=1\) have \(W=\pm2(t-1)\).

## The elliptic curve and rank

Use the positive-sign point at \(r=1\) as origin. Put \(b=2(t-1)\), \(u=1/(r-1)\), \(z=Wu^2/b\). Define
\[
 \beta=t/2+5/4,\quad \gamma=-t/4-13/32,\quad
 h=45t/32+153/64,\quad j=-9t/64-297/1024,\quad c=3t/4+21/16.
\]
Expansion gives \(z^2=(u^2+\beta u+\gamma)^2+hu+j\). Take
\[
 U=2(z+u^2+\beta u+\gamma),\quad V=2Uu+\beta U+h,\quad
 X=4(U+c),\quad Y=8V .
\]
Completing the square in \(u\) gives
\[
                      E:Y^2=X^3+9\epsilon X .
\]
The inverse parameter and the two points above \(r=1\) are
\[
 r=1+\frac{2U}{V-\beta U-h},\qquad
 O,\quad D=(4c,-8h)=\left(\frac{21+12t}{4},-\frac{153+90t}{8}\right).
\]
These birational formulas extend on the smooth projective models. The involution \(W\mapsto-W\) on \(\mathcal C\) becomes \(S\mapsto D-S\): the sum of the two points of each fiber of the degree-two function \(r\) is constant in the elliptic group, and the fiber at 1 is \(O+D\).

For the rational two-isogeny on \(E\), its dual curve has the same form with \(B'=-36\epsilon\) in place of \(B=9\epsilon\). At every finite place \(v(B)\) and \(v(B')\) are multiples of four, by ramification at 2 and 3. If \(v(X)\) is odd, the valuations of \(X^2\) and the coefficient are different, forcing \(v(X^3+BX)\) odd, a contradiction. The same reasoning applies on the dual. Thus all classes in both abscissa descent images are represented by units, including the class of the abscissa at \((0,0)\), which is the coefficient. The units modulo squares are \(\{1,-1,\epsilon,-\epsilon\}\). On \(E\) the coefficient is totally positive, so the abscissa image is contained in \(\{1,\epsilon\}\). The usual two-isogeny rank formula now gives
\[
             2^{\mathrm{rank}E(K)}\le 2\cdot4/4=2 .
\]
At the two places of \(K\) above 13 the reduced groups have respective orders 10 and 18. In particular global rational 3-torsion is trivial. At the split prime 47 both reductions of \(D\) have order divisible by 3, so \(D\) is nontorsion and \(E(K)\) has rank one.

## Two residue classes and a formal logarithm

At a good rational prime \(p\) for \(E_0\), define a sign on the finite residue of \(nP\) by the Legendre symbol of \(8(6-X(nP))\); at the identity use one. Indeed at finite reduction, \(p\nmid y\) and \(w_n=y^2(6-X(nP))/8\). At the identity \(p\mid y\) and \(w_n\equiv x^2/4\bmod p\). A negative sign rules out a square. Taking successive multiples of \(P\) gives

| Prime | Order of \(P\) | Excluded odd residues modulo 24 |
|---:|---:|---|
| 5 | 8 | 3, 5, 11, 13, 19, 21 |
| 577 | 24 | 3, 5, 7, 9, 15, 17, 19, 21 |

It follows that \(n\equiv\pm1\bmod24\). The order of \(P\bmod47\) is 12, hence \(X(nP)\equiv-2\bmod47\) and \(r\equiv\pm1\bmod47\). At \(r=-1\) the value of \(W^2\) on \(\mathcal C\) is \(-8\), a quadratic nonresidue modulo 47. Thus \(r\equiv1\) at both split places. Its two possible reductions there correspond to \(O,D\). Indeed the quartic is smooth at these two affine points and both changes of integral local parameter have unit leading coefficient at 47.

At the two roots \(t=12,-12\bmod47\), the respective cardinalities of \(E(\mathbf F_{47})\) are 48 and 48, and the orders of \(D\) are 3 and 12. The 3-primary subgroup at each place has order three. The 3-primary projection of the simultaneous reduction of \(E(K)\) is cyclic, since the global group has rank one and no 3-torsion. Its generator can be taken to be the projection of \(D\), nonzero at both places. Thus neither mixed residue pair \((O,D)\) nor \((D,O)\) occurs globally. The deck involution reduces the remaining two equal-sign pairs to \((O,O)\), while preserving \(r\).

For the point \(R=12D\) use the formal parameter \(s=-X/Y\). The two Hensel lifts of \(t\) to modulus \(47^2\) and the resulting formal parameters are

| \(t\bmod47^2\) | \(s(R)\bmod47^2\) |
|---:|---:|
| 1939 | \(47\cdot26\) |
| 270 | \(47\cdot24\) |

[Independent standard-library verification of the formal parameters](abc_full_quartic_square_chabauty47.py)

The formal logarithm has the same leading terms at these depths. For a global point \(S\) reducing to \(O\) at both places, its pair of formal logarithms is a rational scalar multiple of that of \(R\), by rank one and torsion-freeness of the good formal groups at 47. If the scalar is nonzero, both logarithms have the same positive valuation \(k\), and after division by \(47^k\) their residue pair is a nonzero multiple of \((26,24)\). The formal inverse to the logarithm also preserves leading terms. On the quartic, the inverse function gives \(r-1=-4s+O(s^2)\) with integral higher coefficients, by the standard Laurent expansions \(X=s^{-2}+O(1),Y=-s^{-3}+O(s^{-1})\). Since \(26\ne24\bmod47\), the resulting two values of \(r\) differ already at depth \(k\), impossible for rational \(r\). The scalar must be zero and \(S=O\). Before using the deck involution the solutions are exactly \(O,D\), both with \(r=1\).

Finally \(r=1\) forces \(x=y=1\) by primitivity. Hence \(w_n=1\), \(a=1\) and \(|b|=1\). In the full parametrization this gives the two signed indices \(\pm1\). Together with the independent cofactor census and its largest-index-prime argument, the same result shows that the four least squarefree parts of the positive odd denominator are each attained at precisely one positive index. [Cofactor census](abc_full_quartic_square_denominators.md)

## All rational points on the genus-two quotient

The curve
\[
             Z^2=-2(r^2+3)(r^4-18r^2+9)
\]
has exactly the four rational points \((r,Z)=(\pm1,\pm8)\). Its leading coefficient \(-2\) excludes rational points at infinity. Write a finite rational parameter as \(x/y\) in lowest terms. Opposite parity makes the right side of the homogenized equation have 2-adic valuation one. If \(3\mid x\), its 3-adic valuation is three. Thus \(x,y\) are both odd and \(3\nmid x\). Outside 2 and 3 the two forms \(H=x^2+3y^2\) and \(F=x^4-18x^2y^2+9y^4\) have no common prime, since \(x^2\equiv-3y^2\) would give \(F\equiv72y^4\). At 2 their respective valuations are exactly two and three; at 3 they are both units. Therefore \(H=h^2\) and \(F=-8a^2\) for integers \(h,a\).

Taking the norm of \(((x+y\sqrt{-3})/2)^4\) now gives the primitive signature with \(w=H/4=(h/2)^2\), \(b=xy(x^2-3y^2)/2\), and the indicated \(a\). If a prime divides \(a,w\), the two coprime odd normalized forms would share that prime, which the preceding calculation excludes. This suffices for primitivity. The theorem forces \(w=1\), so \(|x|=|y|=1\), giving exactly the four listed points. On the degree-four fiber product \(s^2=-2(r^4-18r^2+9),\ h^2=r^2+3\), the finite rational points are exactly \((r,s,h)=(\pm1,\pm4,\pm2)\), with signs independent. Above infinity, the leading coefficient \(-2\) of the first equation excludes rational points.

## Multiple odd-exponent primes at one index

For each odd prime \(q\mid n\), choose a prime \(p(q)\) of odd exponent in \(w_q\). The theorem guarantees such a prime. Its reduction order for \(G\) is exactly \(q\). Hence the chosen primes are distinct, they are \(1\bmod12\), and \(p(q)\ge(2\sqrt q-1)^2>2q\). If \(q\equiv3\bmod4\) and \(q\ge7\), the Gaussian lower bound improves to \(p(q)\ge8q^2-4q+1\). [Gaussian prime bounds](abc_full_quartic_square_denominators.md)

Join one index prime \(q\) to the index prime \(p(q)\) precisely when \(v_{p(q)}(n)\) is odd. These edges are injective and increasing. The resulting components on the index primes are chains. At the last vertex \(q'\) of a chain, formal lifting gives \(v_{p(q')}(w_n)=v_{p(q')}(w_{q'})+v_{p(q')}(n/q')\), an odd number. Distinct chains yield distinct terminal primes in \(d_n=\operatorname{sf}(w_n)\). Every \(q\mid n\) which is outside \(1\bmod12\), or occurs to even exponent in \(n\), is a chain source. Thus \(\omega(d_n)\) is at least the number of such primes, and also at least one for \(n>1\).

Writing \(S\) for the actual chain sources, the product of the distinct terminal primes is exactly \(\prod_{q\in S}q\prod_{q\mid n}p(q)/q\) by cancellation along each chain. In particular
\[
 d_n\ \ge\ 2^{\omega(n)}
   \prod_{\substack{q\mid n:\ q\not\equiv1\ (12)\;\text{or}\;2\mid v_q(n)}}q .
\]
One may retain each stronger individual bound in the product of ratios. All these estimates hold at every positive odd index.
