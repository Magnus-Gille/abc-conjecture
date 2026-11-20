# Two primitive triples from one dyadic factor

For \(n=4,8,16,\ldots\), start with \((u_4,v_4,w_4)=(1,1,7)\) and double by
\[
 u_{2n}=|u_n^4-32v_n^4|,\qquad v_{2n}=2u_nv_nw_n,\qquad
 w_{2n}=w_n^4-128(u_nv_n)^4.
\]
The identity \(w_n^2=u_n^4+16u_n^2v_n^2+32v_n^4\) is preserved by this recursion by substitution. The three entries are positive and pairwise coprime, and \(u_n,w_n\) are odd. Indeed, \(4u_nv_n\le w_n\) gives \(w_{2n}\ge w_n^4/2\). Any odd prime common to \(u^4-32v^4\) and \(uvw\) would have to divide \(w\) and be coprime to \(uv\). Writing \(x=u^2/v^2\) modulo that prime gives \(x^2=32\) and \(x^2+16x+32=0\), hence \(x=-4\) and \(16=32\), an impossibility. The quartic identity then gives coprimality with the new \(w\). These bounds also prove the terms increase without limit. [Elliptic interpretation](abc_octic_dyadic_fermat_audit.md)

Write \(\operatorname{rad}(d)=\prod_{p\mid d}p\) and \(\rho_n=\log\operatorname{rad}(w_n)/\log w_n\). For a primitive triple \(a+b=c\), write \(q=\log c/\log\operatorname{rad}(abc)\).

## A fixed loss in the radical gives a fixed abc violation

Take \(u=u_n,v=v_n,w=w_n\). The quartic identity gives \(w^2-32v^4=u^2(u^2+16v^2)\) and \(w^2+32v^4=(u^2+8v^2)^2\). Multiplying yields
\[
 \boxed{\quad 1024v^8+u^2(u^2+8v^2)^2(u^2+16v^2)=w^4.\quad}
\]
The first and last terms are coprime because \(w\) is odd and \((v,w)=1\). Thus the triple is primitive. Its radical satisfies
\[
 \operatorname{rad}(abc)
 \le 2uv(u^2+8v^2)(u^2+16v^2)\operatorname{rad}(w)
 < w^3\operatorname{rad}(w).
\]
For the strict inequality set \(z=u^2/v^2\), \(H=z^2+16z+32\), and square. The difference \(H^3-4z(z+8)^2(z+16)^2\) is
\[
 z^6+44z^5+672z^4+3840z^3+1024(3z^2-16z+32)>0.
\]
The last quadratic has negative discriminant. For \(n=2^k\ge8\), the recursion gives \(v_2(v)=k-2\). Thus \(\operatorname{rad}(2v)\le 8v/n\) and
\[
        \operatorname{rad}(abc)<(4/n)w^3\operatorname{rad}(w)\le (4/n)c .
\]
In particular these are infinitely many distinct triples with \(c/\operatorname{rad}(abc)>n/4\) unconditionally. The gain \(n/4\) has order \(\sqrt{\log c}\), using the height formula below. It supplies no fixed exponent above one. Along any subsequence with \(\limsup\rho_n\le\rho\), the stronger, radical-dependent inequality gives
\[
 \liminf q\ \ge\frac4{3+\rho}.
\]
In particular, infinitely many squareful terms \(w_n\) (every prime divisor occurring at least twice) would give lower limiting quality at least \(8/7\). More generally, any fixed \(\delta>0\) with \(\operatorname{rad}(w_n)\le w_n^{1-\delta}\) infinitely often suffices for a disproof. In the opposite direction rational abc implies \(\rho_n\to1\), and hence \(\sum_{p\parallel w_n}\log p/\log w_n\to1\). Indeed the total logarithmic mass at exponents \(e\ge2\) is at most twice \(\log(w_n/\operatorname{rad}(w_n))\).

The same explicit test applies to either shifted factor \(s=u^2+8v^2\) or \(t=u^2+16v^2\). Both are at least \(w\). For each \(f\in\{w,s,t\}\), retaining its radical in the product bound gives \(c/\operatorname{rad}(abc)>(n/4)f/\operatorname{rad}(f)\). Thus even one squareful \(f\) at index \(n\ge8\) gives
\[
        c/\operatorname{rad}(abc)^{8/7}>(n/4)^{8/7}.
\]
Infinitely many such indices would violate the constant-factor form of rational abc for the fixed \(\varepsilon=1/7\). Each of \(u,w,s,t\) has been proved not to be a perfect power for every dyadic \(n\ge8\). [Three factors](abc_octic_dyadic_single_powers.md) · [Fourth factor](abc_dyadic_fourth_factor.md)

For instance \(n=4\) gives \(1024+1377=2401\), with radical \(714\). At \(n=8\) the triple is \(1511207993344+25181813914497=26693021907841\), with radical \(3407082923622\). At \(n=16\), the exact quotient \(c/\operatorname{rad}(abc)\) is approximately \(166.4630\) while its quality is approximately \(1.04342\).

## A sharper bound for unusually small radicals

For \(n=2m\), a second primitive triple is
\[
 128(u_mv_m)^4+w_n=w_m^4=c.
\]
Since \(c/2\le w_n<c\) and \(4u_mv_m\le w_m\),
\[
 \operatorname{rad}(abc)
 \le 2u_m v_mw_m\operatorname{rad}(w_n)
 \le \tfrac12\sqrt c\,\operatorname{rad}(w_n).
\]
The same subsequence therefore gives \(\liminf q\ge 1/(1/2+\rho)\). This bound improves the first triple's bound when \(\rho<1/3\). At \(n=16\) the triple is \(4541181790208+22151840117633=26693021907841\).

For example, if the largest prime factor \(P^+(w_n)\le n^4/1000\) infinitely often, the established ellipse sieve gives \(\limsup\rho_n\le 8/(1000\widehat h(R))<0.04\) on those indices. Here \(\log w_n=\widehat h(R)n^2/2+O(1)\), \(\widehat h(R)>1/5\), and the distinct log prime mass below \(cn^4\) is at most \((4c+o(1))n^2\) for fixed \(c>0\). Thus the quality eventually exceeds \(11/6\) on that subsequence. If \(P^+(w_n)/n^4\to0\) along a subsequence, applying the sieve for each fixed \(c>0\) gives \(\rho_n\to0\) there and lower limiting quality at least \(2\). [Sieve and height constants](abc_octic_dyadic_fermat_audit.md) · [Computed prime support](abc_dyadic_cm_prime_support.md)

The separate quadratic Frey-curve argument excludes every proper perfect power \(w_n\). Thus if a squareful term occurs, its prime exponents are all at least two and have greatest common divisor one. At least two distinct primes would be necessary. Even squareful terms of the form \(p^2r^3\) would suffice for the first triple's \(8/7\) bound, if there were infinitely many. [All-index perfect-power proof](abc_octic_dyadic_single_powers.md)

There is also an exact class-group formulation of the remaining hypothesis. For each \(p\mid w_n\), \(n\ge8\), the strict Selmer calculation identifies a class-group character space of dimension \(d(p)\in\{0,1\}\), with \(d(p)=1\) precisely when \(p^2\mid w_n\). Put
\[
 M_n=\frac{\sum_{p\mid w_n} d(p)\,v_p(w_n)\log p}{\log w_n}.
\]
Then \(1-\rho_n\le M_n\le2(1-\rho_n)\), by \(e-1\le e\le2(e-1)\) for \(e\ge2\). A positive upper limit of this weighted fraction would suffice for a disproof, even if each term contains many primes of exponent one. The frequency and total weight of the nonzero character spaces remain undetermined. [Strict Selmer and class-group calculation](abc_dyadic_strict_selmer_eigenspace.md)

## Blocks of small radicals

Suppose \(K\ge1\) is fixed and \(\rho_{n/2^i}\to0\) on a subsequence for every \(0\le i<K\). For \(K=1\) the preceding bound gives \(2\). For \(K\ge2\), put \(m=n/2\), \(t=m/2^{K-2}\) and \(H=\log w_m\). In the radical of the second triple, expand \(v_m\) down to \(t\) using \(v_{2j}=2u_jv_jw_j\). Powers of 2 cost only \(\log 2\) in the radical. All \(w_j\) from \(t\) to \(n\) contribute \(o(H)\). The residual terms have radical bounded by
\[
  2u_tv_t\prod_{j=2t,4t,\dots,m}u_j.
\]
Here an empty product equals one. Since \(u_tv_t\le w_t/4\), \(u_j\le\sqrt{w_j}\), and \(\log w_{m/2^\ell}=4^{-\ell}H+O(1)\) for fixed \(\ell\), the remaining log radical is at most \((2/3+(1/3)4^{2-K})H+o(H)\). Dividing by \(\log c=4H\) proves
\[
 \liminf q\ \ge \left(\frac16+\frac13\,4^{1-K}\right)^{-1}.
\]
The first three values are \(2,4,16/3\). If \(\rho_n\to0\) on all dyadic indices, taking arbitrary fixed \(K\) gives \(\liminf q\ge6\).

The identities and radical bounds are unconditional. The argument does not establish a fixed fractional radical loss at infinitely many indices.

## All possible sources of a fixed loss for the first triple

Put \(s_n=u_n^2+8v_n^2,\ t_n=u_n^2+16v_n^2\), and \(D(f)=\log(f/\operatorname{rad}(f))\) for a positive integer \(f\). For \(n\ge8\) the five factors \(u_n,v_n,w_n,s_n,t_n\) are pairwise coprime. For instance \((s_n,t_n)\mid8v_n^2\) and both are odd and coprime to \(v_n\). At an odd prime of \(s_n\) or \(t_n\), respectively, the quartic gives \(w_n^2\equiv-32v_n^4\) or \(32v_n^4\); the remaining pairs follow immediately. Hence the radical of the triple is exactly the product of their radicals.

Both \(s_n,t_n\) are bounded above and below by absolute positive multiples of \(w_n\). Also
\[
 \log u_n,\ \log v_n=(\tfrac12+o(1))\log w_n
\]
for each of the two quantities. Here is one archimedean argument for the latter assertion. The coordinate \(x_n=(u_n/v_n)^2\) on \(E'\) obeys \(x_{2n}=f(x_n)\) for the degree-four duplication map
\[
 f(X)=\frac{(X^2-32)^2}{4X(X^2+16X+32)} .
\]
Every local degree of \(f^h\) is at most two for every fixed \(h\), since the map is induced by étale multiplication on the elliptic curve through a degree-two quotient. On the complex projective line, the logarithmic inverse chordal distance of \(f^h(x)\) to \(0\) or \(\infty\) is bounded by twice the largest logarithmic inverse distance of \(x\) to one of their finitely many algebraic inverse images plus \(O_h(1)\). This follows by a local parameter at each inverse image and compactness away from them. Roth's theorem bounds the latter logarithmic distance by \(3h_{\rm Weil}(x)+O_h(1)\) for rational \(x\) outside the inverse images. For rational inverse images the elementary bound \(h_{\rm Weil}(x)+O_h(1)\) suffices, and nonreal targets have bounded proximity. The orbit avoids \(0,\infty\). As \(h_{\rm Weil}(f^h(x))=4^h h_{\rm Weil}(x)+O_h(1)\), applying the bound to \(x=x_{n/2^h}\) yields \(\limsup|\log x_n|/h_{\rm Weil}(x_n)\le6/4^h\). Let \(h\) tend to infinity. Finally \(h_{\rm Weil}(x_n)=2\log\max(u_n,v_n)=\log w_n+O(1)\) by the positive quartic. This proves the stated individual sizes.

It follows that \(\log(c/\operatorname{rad}(abc))=\sum_{f=u,v,w,s,t}D(f_n)+o(\log c)\). There is a fixed-exponent infinite violation among these first triples if and only if at least one of \(u,w,s,t\) has \(D(f_n)\ge\eta\log w_n\) for some fixed \(\eta>0\) infinitely often. Indeed \(v\) adds no independent possibility. The exact recursion and coprimality give
\[
 D(v_{2^k})=(k-3)\log2+
       \sum_{j=4,8,\ldots,2^{k-1}}\bigl(D(u_j)+D(w_j)\bigr)\qquad(k\ge3).
\]
If the normalized defects of \(u,w\) tend to zero, the right side is \(o(\log w_{2^k})\) by geometric summation using \(\log w_j\asymp j^2\). The converse direction follows from positivity of every defect and the logarithmic identity.

The extra factors have an elliptic interpretation. The zeros of \(x+8\) are \(\pm R\), where \(R=(-8,16)\). The zeros of \(x+16\) are \(J\pm[\sqrt{-2}]R\), where \(J=(0,0)\). To see the second assertion, the CM formula gives \(x([\sqrt{-2}]R)=-2\), and addition by \(J\) replaces \(x\) by \(32/x\). Thus \(s,t\) measure closeness to two fixed pairs of points. Their valuation estimates would also bear directly on the fixed-exponent question. [CM formula](abc_dyadic_cm_prime_support.md)

## An explicit unbounded multiplicity in the other summand

At every dyadic index \(n=2^k\), \(k\ge2\), one has the exact identity
\[
       v_3(s_n)=2+v_3(k-1).
\]
Indeed \(2R=(1,-7)\) reduces to \(-R\) on the good curve modulo 3, and the reduction of \(R\) has exact order three. The depth of \([3]R\) in the formal group at 3 is two: \(x(2R)-x(-R)=9\), and both points reduce to the same point with nonzero ordinate. At such a point the abscissa difference is a uniformizer, since \(2y\) is a unit, and translation to the identity preserves depth. With \(j=k-1\), the point \([2^j]R\) reduces to \([(-1)^j]R\). The same local abscissa calculation gives \(v_3(s_n)\) as the depth of \([2^j-(-1)^j]R\); the denominator \(v_n\) is a 3-adic unit. Multiplication by an integer \(d\) on the positive-depth group increases depth by \(v_3(d)\), by the formal logarithm. Finally \(v_3(2^j-(-1)^j)=1+v_3(j)\) by the odd-prime lifting lemma applied to \((-2)^j-1\). This proves the formula.

Retaining \(\operatorname{rad}(s_n)/s_n\) in the elementary bound above shows that the same explicit primitive triples satisfy
\[
      \frac{c}{\operatorname{rad}(abc)}>
      \frac n4\,3^{1+v_3(k-1)}\qquad(k\ge3).
\]
Taking \(k=3^h+1\) gives a gain greater than \(3n(k-1)/4\), of order \(\sqrt{\log c}\,\log\log c\). This proves that repeated prime factors really do grow in this family. The explicit contribution still has logarithm \(o(\log c)\), so it alone gives no fixed exponent above one.
