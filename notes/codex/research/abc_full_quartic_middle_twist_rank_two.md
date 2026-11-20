# A rank-two condition on the squarefree cofactor of the middle term

For each odd positive \(n>1\) on the congruent-six orbit, write
\[
      a^4+3b^2=4w^4,\qquad
      c^2=2w^2-a^2,\qquad 3d^2=2w^2+a^2,\qquad b=cd>0 .
\]
Choose all four arm coordinates positive. They are pairwise coprime and odd, with only \(d\) possibly divisible by 3. Put \(k=\operatorname{sf}(b)\), the squarefree part retaining the primes of odd valuation. Then
\[
                \operatorname{rank}\bigl(y^2=x^3+3k^2x\bigr)(\mathbf Q)\ge2 .
\]
Its proof is effective at every \(w\ge37\), covering every \(n>1\) by the known least squarefree cofactor or the elementary denominator height bounds. This condition concerns the actual middle term \(3b^2\) of the primitive abc triple. [Orbit and coprimality](abc_full_quartic_signature.md) · [Least cofactors](abc_full_quartic_square_denominators.md)

## Two points, with a positive height determinant

The curve \(E_b:y^2=x^3+3b^2x\) is isomorphic over \(\mathbf Q\) to the curve with parameter \(k\). Writing \(r=a/w\), this curve also specializes from the rational elliptic surface \(y^2=x^3+(4-r^4)x\) by scaling the abscissa and ordinate by \(w^2,w^3\). Its two sections are \((2-r^2,2(2-r^2))\) and \((r^2,2r)\). It has the two rational points
\[
              P=(c^2,2c^2 w),\qquad Q=(a^2,2aw^2).
\]
For the first point the identity is \(c^2+3d^2=4w^2\). For the second it is \(a^4+3b^2=4w^4\). Since \(a=w\) or \(a=c\) forces the primitive seed, the usual addition and subtraction formulas apply for \(n>1\). Their abscissas are \(w^2c^2/(a+w)^2\) and \(w^2c^2/(a-w)^2\), respectively. For example the chord slope for \(P+Q\) is \(w(a+2w)/(a+w)\).

Move the points to the constant curve \(E:y^2=x^3+3x\) over \(\mathbf Q(\sqrt b)\) by dividing the abscissas by \(b\) and the ordinates by \(b^{3/2}\). Their abscissas there, in lowest terms, are
\[
    x_P=c/d,\qquad x_Q=a^2/(cd),\qquad
    x_{P\pm Q}=\frac{w^2c}{d(a\pm w)^2}.
\]
For the last reduction, an odd prime dividing \(c\) and \(a\pm w\) also divides \(w\), by \(c^2=2w^2-a^2\). The other coprimality statements follow from the four arms, and the numerator is odd.

For positive rational \(x=u/v\) in lowest terms let \(h(x)=\log\max(u,v)\). On \(E\) the raw abscissa coordinates after doubling are \((u^2-3v^2)^2\) and \(4uv(u^2+3v^2)\). Their gcd divides 36. For an odd common prime one must have \(p=3\) and \(3\mid u\), giving exactly 2 in the numerator valuation. At 2 they can only share a factor if \(u,v\) are odd, giving numerator valuation 2. The larger raw coordinate lies between \(\max(u,v)^4/4\) and \(16\max(u,v)^4\). For the lower bound, when \(u\ge\sqrt6\,v\) use the numerator, when \(v\le u<\sqrt6\,v\) use the denominator, and when \(u<v\) use the numerator. Iteration gives
\[
 h(x)-\tfrac13\log144\ \le\ 2\widehat h\ \le\ h(x)+\tfrac13\log16 .
\]
This bound also holds at poles and zero by continuity or projective doubling. All multiples under consideration have rational nonnegative abscissas on this fixed curve.

Write \(t=a/w\), with \(0<t<\sqrt2\), so \(c/w=\sqrt{2-t^2}\) and \(d/w=\sqrt{(2+t^2)/3}\). Then
\[
 h(x_P)\ge\log w+\tfrac12\log(2/3),\qquad
 h(x_Q)\ge2\log w+\tfrac12\log(2/3).
\]
For the second inequality use \(a^2\) when \(t\ge1\), and \(cd\) otherwise. Furthermore \(0\le h(x_{P+Q})-h(x_{P-Q})<\log54\). Indeed the two height arguments, after division by \(w^3\), are \(\max(c/w,(d/w)(t\pm1)^2)\). For \(t\le4/3\) the common first term is at least \(\sqrt2/3\), while both arguments are less than 7. For \(t\ge4/3\) their ratio is at most \(((\sqrt2+1)/(1/3))^2<54\). Therefore
\[
 |\langle P,Q\rangle|\le
 \tfrac18\left(\log54+\tfrac13\log2304\right)<0.83 .
\]
Here the pairing is one fourth of \(\widehat h(P+Q)-\widehat h(P-Q)\). At \(w\ge37\), the two diagonal heights exceed \(0.87\) and \(2.67\), respectively, so their determinant is positive. The points are independent over \(\mathbf Q\) on \(E_b\), proving the claim.

## An infinite excluded set of squarefree cofactors

For every \(n>1\), some prime \(p\ge5\) dividing \(b\) to odd exponent is outside \(5\bmod12\). In particular \(k\) cannot be supported on 3 and primes that are \(17\bmod24\), even with arbitrarily many such primes. This conclusion uses no factorization of the corresponding denominator or cofactor.

Indeed, suppose all \(p\ge5\) dividing \(k\) were \(5\bmod12\). The usual 2-isogeny images are the squareclasses of divisors \(e\) of \(B=3k^2\) and \(B'=-12k^2\) satisfying \(N^2=eU^4+(B/e)V^4\), and analogously on the dual. If \(p\mid e\) for a squarefree representative, then \(v_p(B)=2\) and cancellation of the two valuation-one terms requires \((-3/p)=1\) on the first curve or \((12/p)=1\) on the dual. Both symbols are negative for \(p\equiv5\bmod12\). Thus the only possible primes in the images are 2 and 3. The first image consists of positive classes, is unramified at 2, and has size two from \(1,3\). The dual image is contained in the eight signed squareclasses supported at 2 and 3. It excludes \(-1\), since \(N^2=-U^4+12k^2V^4\) gives a nonsquare modulo 3 when \(3\nmid U\), and an odd valuation (1 or 3) otherwise for coprime \(U,V\). Its size is therefore at most four. The isogeny rank formula gives \(2^{\mathrm{rank}}\le2\cdot4/4=2\), a contradiction.

The supports of \(c,d\) allow only \(1,11,17,19,23\bmod24\) away from 3. Thus at least one prime of odd exponent in \(b\) is \(1,11,19\) or \(23\bmod24\). The restriction on the twist rank is substantially stronger than this particular local corollary, as it applies to every cofactor.
