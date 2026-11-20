# An upper bound for primitive abc triples with two nearly powerful terms

Let \(X\le b<c\le2X\), \(a=c-b\), \((b,c)=1\). Write \(L\) for the product of primes occurring to exponent **exactly one** in \(bc\). For each fixed \(A\), \(1\le B\le X^{1/3}\), and every \(\varepsilon>0\), the number of triples with \(1\le a\le A\) and \(L\le B\) is
\[
                    \ll_{A,\varepsilon} X^{13/50+\varepsilon}B^{41/50}.       \tag{1}
\]
For two powerful terms (\(L=1\)), the following estimate holds for a growing gap:
\[
                    \ll_\varepsilon X^{13/50+\varepsilon}A^{11/10}
                       \qquad(1\le A\le X^{1/10}).                          \tag{2}
\]
These bounds also apply after imposing a radical threshold. For example, at bounded gap and \(L\le X^{1/4}\), (1) gives \(X^{93/200+\varepsilon}\). For the threshold \(\operatorname{rad}(abc)\le X^{19/20}\), the general bounded-gap argument below gives \(X^{19/40+\varepsilon}\). The exponents are 0.465 and 0.475, respectively. No distribution of powerful residues in progressions is assumed.

## General bounds by the sizes of two radicals

For \(\operatorname{rad}(abc)\le R\le X\), without restricting the singleton factors one always has
\[
  \#\{(a,b,c):1\le a\le A\}\ll_\varepsilon X^\varepsilon
              \min\{R^{2/3},\sqrt{AR}\}.                                  \tag{3}
\]
For an integer up to \(2X\), a prescribed radical has at most \(X^{o(1)}\) realizations uniformly. Indeed its \(k\) primes have \(k\ll\log X/\log\log X\) by comparison with a factorial, and the sum of exponents is at most \(\log_2(2X)\). The logarithm of the resulting binomial coefficient is \(o(\log X)\). The two smallest of the three individual radicals have product at most \(R^{2/3}\), and choosing their values, and then their entries, determines the third. Summing the divisor function up to \(R^{2/3}\) gives the first bound. At fixed \(a\), one of \(b,c\) has radical at most \(\sqrt{R/\operatorname{rad}(a)}\). Summing over \(a\le A\) and using the same multiplicity estimate gives the second, since \(\sum_{a\le A}\operatorname{rad}(a)^{-1/2}\le X^{o(1)}\sum_{d\le A}d^{-1/2}\).

There is also a useful large-singleton bound: triples with \(L\ge B\) have count \(\ll X^{o(1)}R/B\). Write \(b=k b', c=l c'\) with \(k,l\) the singleton parts of the respective terms. At fixed \(a,b',c'\), the equation \(lc'-kb'=a\) and \((b',c')=1\) give \(O(1+X/(b'c'))=O(1)\) solutions in the height window, since \(b'c'\gg X^2/L\) and \(L\le R\le X\). Also \(\operatorname{rad}(a b' c')\le R/B\); the same radical enumeration and the divisor bound count all such data in \(X^{o(1)}R/B\). For general bounded-gap triples these arguments leave an intermediate range of singleton sizes. In particular (1) does not give a global improvement of the second estimate of (3).

## Rational points close to a power function

Write the canonical powerful decompositions
\[
            b=k u^3 x^2,\qquad c=l v^3 y^2,
\]
where \(k,l\) are as above and \(u,v\) are squarefree products of primes of odd exponent at least three. Put \(L=kl\). In dyadic boxes with sizes \(U,V,M,N\) for \(u,v,x,y\), respectively, set \(D=UV\), \(E=MN\), \(Z=X/\sqrt L\). Then \(D^3E^2\asymp Z^2\). The fractions \(u/v\) and \(y/x\) are separately in lowest terms by \((b,c)=1\). Rescale each fraction by the corresponding ratio of denominator and numerator box sizes to land in \([1/2,2]\). Choose \(s\) to denote the normalized fraction with the smaller pair-size product \(J=\min(D,E)\), and \(t\) the other, with pair-size product \(K=\max(D,E)\). The height and gap conditions give
\[
           t=f(s)+O(\eta),\qquad f(s)=\kappa s^\gamma,\qquad
           \eta=A/X,
\]
where \(\gamma=3/2\) or \(2/3\), and \(\kappa\) is bounded above and below absolutely on nonempty boxes. This follows by taking the square or cube root of the exact ratio \(c/b=1+O(A/X)\). All the derivatives used below are uniformly bounded on this compact range.

Use six monomials \(1,s,s^2,t,st,s^2t\). For six candidate points a nonzero determinant of their row evaluations has absolute value \(\gg J^{-6}K^{-3}\). Indeed for the unscaled fractions multiply each row by its first denominator squared times its second denominator to make it integral. The rescaling multiplies the determinant by the first scale to the sixth power and the second to the third power. Including both numerator and denominator box sizes leaves exactly the indicated products. Further \(J^6K^3\ll Z^{18/5}\). To check, when \(D\le E\) one has \((D^2E)^5\le(D^3E^2)^3\); when \(E\le D\) one has \((DE^2)^5\le(D^3E^2)^3\).

On an interval of length \(h\le1\) in \(s\), write each row as its evaluation at \(f(s)\) plus the error \((t-f(s))(0,0,0,1,s,s^2)\). Expand the determinant in the rows. Terms choosing more than three error rows vanish. In a term with \(j\le3\) error rows, expand by the corresponding columns. For each smooth minor of order \(w\) the determinant costs \(O(h^{\binom{w}{2}})\), by successive divided differences (or the Vandermonde factor with bounded derivatives). The same bound applies to the polynomial error minor after removing its \(j\) error factors. Thus the whole determinant is
\[
                \ll\sum_{j=0}^3\eta^j h^{b_j},\qquad (b_0,b_1,b_2,b_3)=(15,10,7,6).
\]
Partition the fixed interval into
\[
       O\!\left(1+\max_{0\le j\le3}(Z^{18/5}\eta^j)^{1/b_j}\right)        \tag{4}
\]
equal cells, taking the implied constant sufficiently large. All six-row determinants in each cell vanish. Hence the entire cell lies on a nonzero auxiliary equation of bidegree at most \((2,1)\). In the unscaled rational coordinates the equation has integer coefficients of size \(X^{O(1)}\). To see this, use a maximal independent subset of at most five of the integer-cleared rows in these coordinates and a nonzero vector of minors from a maximal-rank submatrix. The rescaling only multiplies columns by constants and thus preserves rank.

## Counting the rational points on each auxiliary curve

Write the auxiliary equation in the unscaled coordinates as \(P(s)-tQ(s)=0\). A vertical component fixes a reduced slope and thus its two positive coprime coordinates. The partner slope lies in an interval of normalized length \(O(\eta)\) by the strictly positive derivative of the limiting power function or its inverse. The spacing of distinct normalized fractions in a box with coordinate product \(W\) is \(\gg1/W\). Both pair-size products are \(O(X)\), so there are \(O(1+A)\) partners. This also handles horizontal components and constant maps. Remove the common factors of \(P,Q\) and homogenize to their actual map degree \(r\in\{1,2\}\). The resulting integral forms, again denoted \(P,Q\), have coefficients \(X^{O(1)}\), by the fixed-degree integer polynomial factor bound. They have no common projective root.

Let \((m,n)\) be the primitive numerator-denominator pair for \(s\) before rescaling. The other primitive pair is \((P(m,n),Q(m,n))/g\) up to common sign, where \(g=\gcd(P(m,n),Q(m,n))\) divides the nonzero resultant of \(P,Q\). In fact homogeneous Bézout identities put the resultant times each of \(m^{2r-1},n^{2r-1}\) in the ideal generated by the evaluated forms. The resultant is \(X^{O(1)}\), giving \(X^{o(1)}\) choices for \(g\).

If \((m,n)=(u,v)\), the equation for a particular integer gap \(a\) becomes a binary form equation with right side \(\pm a g^2\) and left side
\[
                  F(m,n)=l n^3 P(m,n)^2-k m^3 Q(m,n)^2.
\]
It has degree \(2r+3\), which is five or seven. It has at least two distinct complex projective roots. If the summands have a common zero it is at \(0\) or infinity. The ratios of their homogeneous multiplicities there differ (the coordinate exponent three is odd and the other vanishing order is even); after cancellation this point is not in the fiber of ratio one. The nonconstant ratio has a preimage of one, giving a second root. Nonconstancy follows also from its odd valuation at zero. If there are no common zeros, the degree of the ratio is \(2r+3\); the fibers over zero and infinity together contain at most \(2r+2\) points. Riemann–Hurwitz for a rational function then gives at least three points over one. Indeed for a degree-\(d\) rational function the total number of distinct points over three prescribed values is at least \(d+2\).

If \((m,n)=(y,x)\), the binary form instead has terms \(l m^2 Q(m,n)^3-k n^2P(m,n)^3\) and right side \(\pm a g^3\). The common sign of the substituted coordinates is immaterial after allowing both right-hand signs. This time the form has degree \(3r+2\). Let \(c_0\) count its common zeros before cancellation. They lie at zero or infinity, and the minimum initial vanishing order at each is exactly two. The rational ratio after cancellation has degree \(3r+2-2c_0\); zero and infinity fibers together involve at most \(2r+2-c_0\) points because every common zero already belonged to a root of one of the two forms \(P,Q\). Each common zero still maps to zero or infinity after cancellation, as a multiple of three cannot equal two. Counting the fiber above one by Riemann–Hurwitz and adding the \(c_0\) common zeros therefore gives at least \(r+2\ge3\) distinct roots of the binary form. The ratio is nonconstant, for instance by its valuation at zero modulo three.

It follows in both orientations that the form cannot be a power of a single rational linear or irreducible quadratic form: the odd degree excludes a quadratic power in the first orientation, and at least three distinct geometric roots exclude it in the second. If there are two different irreducible rational factors, their nonzero integral values divide the right side up to fixed content, giving \(X^{o(1)}\) possibilities. For any two fixed values \(v_1,v_2\) of nonproportional irreducible homogeneous factors \(F_1,F_2\), the homogeneous polynomial \(v_2^{\deg F_1}F_1^{\deg F_2}-v_1^{\deg F_2}F_2^{\deg F_1}\) is nonzero and must vanish at \((m:n)\). It allows only boundedly many primitive pairs. If only one irreducible factor occurs, its degree is at least three. The uniform Thue bound for primitive solutions to an irreducible binary form of fixed degree \(d\ge3\) is \(O_d(C_d^{1+\omega(|v|)})\) for nonzero right side \(v\), independent of the coefficients. Apply it to that factor after accounting for a possible power. Since \(0<|v|\le X^{O(1)}\), this gives \(X^{o(1)}\) primitive pairs. E. Bombieri and W. M. Schmidt, *On Thue's equation*, Inventiones Mathematicae 88 (1987), 69–81.

Thus there are \(\ll_\varepsilon AX^\varepsilon\) triples per cell. There are logarithmically many dyadic ranges per variable. Summing (4) over \(k l\le B\) costs a divisor-function factor. For \(1\le B\le X\), each resulting term, apart from \(O(AX^\varepsilon B)\), is
\[
    AX^\varepsilon\, X^{(18/5-j)/b_j} A^{j/b_j} B^{1-9/(5b_j)}.
\]
The term with \(j=0\) covers \(B\) in this range. For bounded \(A\) and \(B\le X^{1/3}\) the \(j=1\) term dominates every other one, giving (1). For \(B=1\) and \(A\le X^{1/10}\) the same term gives (2).

## Why the balanced boxes matter

In boxes with \(D\asymp E\asymp (X/\sqrt L)^{2/5}\) one has \(\operatorname{rad}(abc)\le aLDE\ll A X^{4/5}L^{3/5}\). At bounded gap and \(L\asymp X^{1/4}\) this is the actual \(X^{19/20}\) scale up to a constant. In particular for any fixed \(\delta<1/20\) the whole such box satisfies \(\operatorname{rad}(abc)\le X^{1-\delta}\) for large \(X\). A count of high-quality triples in that regime really does have to bound these near coincidences.

For the raw determinant argument with monomials \(s^i,s^it\), \(0\le i\le r\), the fixed-gap balanced powerful box \(D=E\asymp X^{2/5}\) has nonzero determinant threshold \(X^{-(2/5)(r+1)^2}\). The corresponding Taylor expansion for \(h=X^{-t}\) gives terms of order \(X^{-j}h^{\binom{2r+2-j}{2}+\binom{j}{2}}\). To beat the determinant threshold with these bounds, \(r=1\) needs \(t\ge4/15\) from \(j=0\); \(r=2\) needs \(t\ge13/50\) from \(j=1\). For \(r\ge3\), the \(j=r\) term requires
\[
        t\ge\frac{(2/5)(r+1)^2-r}{r^2+r+1}>\frac{13}{50},
\]
since \(7r^2-23r+7>0\). This comparison concerns the displayed geometric bounds for auxiliary graphs. It gives no upper bound on the reach of different methods or extra congruence information at the actual integer points.

## Square smaller term and square height

In the [common-height square specialization](abc_common_height_multiplicity.md), take \(c=y^2\asymp X\), \(a=t^2\le A\), \((y,t)=1\). If \(b=c-a\) is powerful and \(1\le A\le X^{1/10}\), the total number of triples in this block is
\[
                   \ll_\varepsilon X^{13/100+\varepsilon}A^{11/20}.
\]
Indeed \(b=(y-t)(y+t)\). For opposite parities the two factors are coprime and powerful. For equal parities their positive halves are coprime (any common prime divides \(t,y\)); an odd prime in either half keeps its exponent in \(b\), so only 2 can occur as a singleton. In both cases the pair has height comparable to \(\sqrt X\) and gap at most \(2\sqrt A\), and it determines at most a bounded number of \((y,t)\). Equations (2) and (4) apply also with any fixed singleton-product cutoff and fixed constant factors in the height or gap bounds. More generally, for fixed \(A\), if the singleton-prime product of \(b\) is at most \(B\le X^{1/6}\), the half-factor pair has singleton product at most \(2B\); (1) gives \(\ll_{A,\varepsilon} X^{13/100+\varepsilon}B^{41/50}\). In the bounded-gap balanced powerful boxes for the two factors of \(b\), their radical is \(\ll_A X^{2/5}\). The additional square height contributes at most \(y\asymp X^{1/2}\) to the radical, and the small square costs only a constant. Thus every such triple satisfies a fixed height/radical gain of exponent \(\delta\) for every \(\delta<1/10\) once \(X\) is large.

For fixed **even** \(m\ge2\) the identical argument at \(c=y^m\asymp X\), \(a=t^m\le A\) gives \(\ll_{m,\varepsilon}X^{13/(50m)+\varepsilon}A^{11/(10m)}\) when \(b=c-a\) is powerful and \(A\le X^{1/10}\). At a prime \(p\nmid 2m\) dividing \(y-t\) or \(y+t\), the remaining factor \((y^m-t^m)/(y^2-t^2)\) is congruent to \((m/2)t^{m-2}\not\equiv0\pmod p\). Thus only the fixed primes dividing \(2m\) can be singletons in the two coprime factors after the same possible division by two.
