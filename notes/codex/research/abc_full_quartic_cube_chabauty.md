# Cubes in the odd denominator of the full quartic signature

The only positive primitive solution of \(a^4+3b^2=4v^{12}\) is \((a,b,v)=(1,1,1)\). Equivalently, \(w_n=B(n(-3,9))\) on \(Y^2=X^3-36X\) is a cube at positive odd index \(n\) precisely when \(n=1\). Together with the square classification, this excludes every nontrivial perfect power whose exponent has a factor 2 or 3. [Full parametrization](abc_full_quartic_signature.md) · [Square classification](abc_full_quartic_square_chabauty.md) · [Standard-library verifier](abc_full_quartic_cube_chabauty.py)

## One quartic over the real cyclotomic cubic

The parametrization supplies coprime odd positive \(x,y\), with \(3\nmid x\), such that \(x^4-18x^2y^2+9y^4=-8a^2\), \(w_n=(x^2+3y^2)/4\), and \(3\nmid a\). Write \(j=\sqrt{-3}=1+2\omega\), where \(\omega\) is a primitive cubic root of unity. In the Eisenstein integers, \(\beta=(x+yj)/2\) satisfies
\[
 N\beta=w_n,\qquad \beta^4+\bar\beta^4=-a^2 .
\]
The ideals of \(\beta,\bar\beta\) are coprime: their sum and difference exclude every common odd prime away from 3 by \((x,y)=1\), while \((w_n,6)=1\). If \(w_n=v^3\), unique factorization gives \(\beta=\eta\gamma^3\) with \(\eta\) a unit. Modulo 2, \(\beta=(x+y)/2+y\omega\) is in \(\mathbf F_4\setminus\mathbf F_2\), whereas nonzero cubes reduce to one. Absorbing a sign in \(\gamma\) and conjugating if necessary, we obtain \(\eta=\omega\). Thus
\[
                \omega\gamma^{12}+\bar\omega\bar\gamma^{12}=-a^2.
\]
Allowing this conjugation preserves the absolute value of the original slope \(x/y\).

Take \(\xi^3=\omega\) with \(\xi\) a primitive ninth root of unity, and put \(L=\mathbf Q(\theta)\) with \(\theta=\xi+\xi^{-1}\), \(\theta^3-3\theta+1=0\). This cyclic cubic field has ring of integers \(\mathbf Z[\theta]\), discriminant 81, inert prime 2 and totally ramified prime 3. These follow from the real cyclotomic field of conductor 9. Its Minkowski class bound is 2, and there is no ideal of norm 2, so its class number is one. The signs of \(-1,\theta,\theta-1\) at the three real places are independent, as the three roots lie in \((-2,-1),(0,1),(1,2)\). All three are units. Dirichlet's unit theorem now shows that they form a basis of the units modulo squares. In particular every totally positive unit is a square.

The three conjugates of \(\alpha=\xi\gamma^4+\xi^{-1}\bar\gamma^4\) have sum zero and product \(-a^2\). They are pairwise coprime away from 3. Indeed in \(\mathbf Q(\xi)\) any two simultaneous divisibilities force both \(\gamma^4\) and \(\bar\gamma^4\) to vanish, since the determinant of the corresponding two linear forms is a unit away from 3. This contradicts coprimality of \(\gamma,\bar\gamma\). The conjugates are also units at 3 because \(3\nmid a\). Consequently \(\alpha\) has square ideal. Its sign pattern has exactly one negative entry. Replacing \(\gamma\) by \(\omega\gamma\) preserves \(\beta\) and cycles these three signs, so we may align them with the signs of \(\theta\). It follows that \(\alpha/\theta\) is a square in \(L\).

Write \(\gamma=s+uj\) with \(s,u\in\mathbf Q\), let \(r=s/u\) on the finite chart, and set
\[
 \kappa=j(\xi-\xi^{-1})=4-2\theta^2-\theta,\qquad k=\kappa/\theta .
\]
Then \(k^2+3=12/\theta^2\), and every prospective solution lifts to the single quartic
\[
 W^2=f(r)=r^4+4kr^3-18r^2-12kr+9,\qquad r\in\mathbf P^1(\mathbf Q).
\]
Scaling \(s,u\) to this chart only divides a square by \(u^4\).

## The elliptic group has rank one

Put \(S=k^2+3\), \(b=-9-2k^2\), \(h=8kS\), and
\[
 U=2(W+r^2+2kr+b),\quad V=2Ur+2kU+h,\quad
 X=\theta^2(U+4S)/4,\quad Y=\theta^3 V/8.
\]
Indeed \(f=(r^2+2kr+b)^2+hr+9-b^2\). Completing the square in \(r\) gives a birational transformation to
\[
 E:Y^2=X^3-36\theta^2X,\qquad
 r=\frac{Y-\kappa X}{\theta(X-12)} .
\]
The two points at infinity of the quartic give \(O,D\), where \(D=(12,-12\kappa)\). The two points at \(r=0\) give \(T_0,D+T_0\), where \(T_0=(0,0)\). The involution \(W\mapsto-W\) is \(Q\mapsto D-Q\) by the constant group sum of each fiber of the degree-two function \(r\). Translation by \(T_0\) sends \(r\mapsto-3/r\); substituting the standard translation formulas uses \(Y^2-\kappa^2X^2=X(X-12)(X+3\theta^2)\).

Perform two-isogeny descent on \(E\), with coefficient \(B=-36\theta^2\), and on the dual with \(B'=144\theta^2\). An abscissa squareclass has even valuations outside 2,3. The five possible squareclass generators are
\[
           -1,\quad\theta,\quad\theta-1,\quad 2,\quad\theta+1.
\]
Here \(N(\theta+1)=-3\). For the primal image class \(e\), the normalized quartic gives \(e z^2=e^2 u^4+Bv^4\), where \(u,v\) are dyadic integers with one a unit; \(z\) is integral since \(B/e\) is locally integral. If \(v\) is a unit set it to one; otherwise set \(u=1\) with \(v\) a nonunit. Exhausting both charts in \(\mathbf Z[\theta]/32\), the only generator masks which pass are
\[
 00000,\ 00011,\ 01001,\ 01010,\ 10000,\ 10011,\ 11001,\ 11010 .
\]
The accompanying verifier uses precisely the sets of squares, fourth powers and fourth powers of nonunits of this ring. Thus the primal image has size at most 8.

The dual image is trivial. At 2 its coefficient has valuation four, so odd abscissa valuation would force odd ordinate-square valuation. At 3 the sum \(X^2+(12\theta)^2\) always has even valuation, since \(-1\) is a nonsquare in the residue field \(\mathbf F_3\). Consequently all abscissa valuations are even, and \(B'\) is itself a square. The abscissa is totally positive at every real place because \(B'\) is totally positive. The unit signature result therefore makes its squareclass trivial. The usual rank formula gives \(2^{\mathrm{rank}E(L)}\le8\cdot1/4=2\).

At a place above 19 the reduced group has order 20; at the inert prime 7 it has order 344, since the residue field has cardinality \(343\equiv3\bmod4\) and the odd cubic character sum vanishes under \(X\mapsto-X\). Together with full rational two-torsion this proves \(E(L)_{\mathrm{tors}}=E[2]\). The point \(D\) has abscissa class \(3\), outside the torsion classes \(1,-1,\pm6\theta\), as is seen at the primes above 2 and 3. Thus \(D\) has infinite order, the rank is one, and \([E(L):\langle D,E[2]\rangle]\) is odd.

## The three places above 19

The three roots of the cubic modulo 19 are \(3,7,9\). At each, \(E(\mathbf F_{19})\) has cardinality 20 and \(D\) has order 10. The index of \(\langle D,E[2]\rangle\) is also prime to 5: a putative relation \(D=5Q+T\) would have trivial 5-primary part after reduction. Hence this subgroup generates the full simultaneous reduction of \(E(L)\) at 19.

At its 40 possible cells \(mD+T\) for \(m\bmod10\), \(T\in E[2]\), evaluate \(r\) at the three embeddings. At \(-D\), where the displayed ratio is removable, its value is \((12+3\theta^2)/(2\kappa\theta)\) by the tangent slope. The only cells giving the same point of \(\mathbf P^1(\mathbf F_{19})\) at all three embeddings are precisely \(O,D,T_0,D+T_0\). Their slopes are \(\infty,\infty,0,0\). The two involutions above take every one of these residue disks to the disk at \(O\), while preserving rationality of the slope.

For the formal parameter \(z=-X/Y\) of \(R=10D\), the three Hensel lifts of \(\theta\) and reductions are

| \(\theta\bmod19^2\) | \(z(R)/19\bmod19\) | \(-\theta z(R)/19\bmod19\) |
|---:|---:|---:|
|288|9|11|
|273|12|11|
|161|14|7|

The verifier checks all 40 cells and computes \(10D\) directly in projective coordinates modulo \(19^2\). Any global point in the three formal disks has simultaneous formal logarithms proportional over \(\mathbf Q\) to those of \(R\), by rank one. A nonzero proportionality factor gives common positive valuation. At \(O\), \(1/r=-\theta z+O(z^2)\) with integral higher coefficients, and the formal logarithm and its inverse preserve leading terms. The leading residues of \(1/r\) would therefore be a common nonzero scalar times \((11,11,7)\), impossible for a rational value. Only \(O\) remains in that disk. Undoing the involutions proves that the only rational slopes of the quartic are \(0,\infty\).

At \(r=\infty\), \(\gamma\) is rational and \(\beta=\omega\gamma^3\) gives original absolute slope \(|x/y|=1\). At \(r=0\), \(\gamma\) is a rational multiple of \(j\), giving \(|x/y|=3\), excluded by \(3\nmid x\). The first case gives \(x=y=1\) and \(w_n=1\). This proves the stated classification.
