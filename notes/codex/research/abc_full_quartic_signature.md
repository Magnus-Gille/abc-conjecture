# The full signature \(a^4+3b^2=4w^4\) and primitive denominator excess

Let \(a,w>0\) and allow either sign for \(b\). Every primitive solution has odd pairwise coprime coordinates, with \(3\nmid aw\). Indeed a common prime of a pair forces it into the third, including 3 by reduction and valuations, and the primitive even possibilities are excluded modulo 16. The associated abc triple is already primitive.

## The complete elliptic parametrization

Let \(E_6:Y^2=X^3-36X\), \(G=(-3,9)\), \(T_0=(0,0)\), \(T_- =(-6,0)\), \(T_+=(6,0)\). The signed triples correspond bijectively to odd integers \(n\) under
\[
 X(nG)=-3a^2/w^2,\qquad Y(nG)=9ab/w^3.
\]
To see the converse, write the positive square root of \(-X/3\) as \(a/w\) in lowest terms, and set \(b=w^3Y/(9a)\). Then \(3b^2=4w^4-a^4\) forces the rational number \(b\) to be an integer. Pairwise coprimality follows. The abscissa squareclass map for the rational two-isogeny is a homomorphism, with values \(-1,-6,6\) respectively on \(T_0,T_-,T_+\), and \(-3\) on \(G\). Its fiber at \(-3\) therefore consists of precisely the odd multiples of \(G\), using the group computation below. Opposite signs for \(b\) correspond to opposite indices. The first positive indices give \((a,|b|,w)=(1,1,1),(23,1551,37),(52487,1040847151,40573)\).

Geometrically, the displayed map on the smooth quartic is an unramified degree-two map to \(E_6\). Its deck involution sends both signed affine coordinates \((a/w,b/w^2)\) to their negatives. Its Jacobian has model \(y^2=x^3+144x\), from the standard Jacobian of \(v^2=A u^4+B\) with \(v=3b/w^2\), \(A=-3,B=12\). The rational point \((1,1)\) identifies the quartic with this isogenous curve.

The earlier elliptic slice maps onto this entire parametrization. Its isogeny sends \(P=(-2,8)\) to \(Q=(-2,-8)=G+T_+\). For odd \(n\), write \(X(nP)=-2r^2\) with \(r=x/y\). Translation of \(nQ\) by \(T_+\) gives
\[
 X(nG)=6-144r^2/(r^2+3)^2=-3s^2/W^2,
\]
where \(x^4-18x^2y^2+9y^4=-8s^2\) and \(W=(x^2+3y^2)/4\). Since \((s,W)=1\), one has \((a,w)=(s,W)\). The signed squareclass identities there give \(|b|=|s^2+2kt^2|/3\), where \(F_4=16kt^2\). [Earlier orbit](abc_eisenstein_twelfth_elliptic_slice.md) · [Signed squareclasses](abc_eisenstein_slice_squareclass_descent.md)

### An elementary certificate for the rational group

Reduction at 7 and 11 gives group orders 8 and 12; hence the torsion is exactly the visible two-torsion. The usual rational two-isogeny descent on \(E_6\) and \(E':y^2=x^3+144x\) gives \(2^{\mathrm{rank}}=|\alpha(E_6)||\alpha(E')|/4\). The first image is all eight signed squarefree divisors of 6 by the points above. On the second curve only the positive classes \(1,2,3,6\) are possible. For \(d>1\) one needs \(N^2=du^4+(144/d)v^4\) with \((u,v)=1\). At \(d=2\), the 2-adic valuation on the right is 1 or 3. At \(d=3,6\), its 3-adic valuation is 1. Thus the rank is one.

Here are explicit bounds certifying that \(G\) generates the free quotient. Write \(h(x)=\log\max(|A|,B)\) for \(x=A/B\) in lowest terms and use the canonical height convention \(h(x(S))=2\widehat h(S)+O(1)\). The duplication numerator and denominator are
\[
 (A^2+36B^2)^2,\qquad 4AB(A^2-36B^2).
\]
Their gcd divides \(5184=2^6 3^4\). Away from 2,3 they have no common prime. If \(2\mid A\) then \(v_2(A^2+36B^2)\le3\) by odd squares modulo 8. If \(3\mid A\), then \(v_3(A^2+36B^2)=2\) by squares modulo 3. Thus
\[
 4h(x)-\log5184\le h(x(2S))\le4h(x)+\log1369
\]
for nontorsion \(S\). Summing the geometric series gives \(h(x(S))\le2\widehat h(S)+\log(5184)/3\) and \(2\widehat h(G)\le(h(1442401/19600)+\log(1369)/3)/16<1.04\), using \(x(4G)=1442401/19600\). If \(G=mS+T\) with torsion \(T\) and \(m\ge2\), then \(h(x(S))<\log25\). A finite square test at \(x=A/d^2\), \(1\le d\le5\), \(|A|\le25\), \((A,d)=1\), checks whether \(A(A^2-36d^4)\) is a nonnegative square. The complete list of abscissas is \(-6,-3,-2,0,6,12,18,25/4\). The four values \(-3,-2,12,18\) arise from \(G+E_6[2]\) up to sign, and \(25/4\) from \(2G\). All listed nontorsion points have height at least \(\widehat h(G)\), excluding \(m\ge2\). This proves \(E_6(\mathbf Q)=\mathbf ZG\oplus E_6[2]\).

## Four coprime factors and one denominator

Factor \(3b^2=(2w^2-a^2)(2w^2+a^2)\). The two positive odd factors are coprime, and only the second is divisible by 3. Hence there are uniquely determined positive integers \(c,d\) such that
\[
 2w^2-a^2=c^2,\qquad 2w^2+a^2=3d^2,\qquad |b|=cd.
\]
The four integers \(w,a,c,d\) are pairwise coprime; only \(d\) can be divisible by 3. For any finite rational point \(S\), let \(B(S)\) be the positive square root of the reduced abscissa denominator. The three translated abscissas are
\[
 X(nG+T_0)=12w^2/a^2,\qquad X(nG+T_-)=-6+24w^2/c^2,
 \qquad X(nG+T_+)=6-8w^2/d^2.
\]
Consequently the four denominators \(B(nG+T)\), in order \(T=O,T_0,T_-,T_+\), are exactly \(w,a,c,d\). Duplication gives, in lowest terms,
\[
 X(2nG)=\frac{(a^4+4w^4)^2}{4a^2 b^2 w^2},\qquad
 B(2nG)=2|abw|,\qquad R=\operatorname{rad}(3B(2nG)).
\]
Indeed a prime dividing \(b\) divides neither \(aw\) nor \(a^4+4w^4\), the latter being \(8w^4\bmod p\). From the factor equations any good prime dividing \(w\) is \(1\bmod12\); those dividing \(a\) or \(c\) are \(\pm1\bmod24\); those dividing \(d\) are \(1,3\bmod8\).

## Primitive order and the uniform inequality

Write \(H=\widehat h(G)>0\), \(C=4w^4\). We use
\[
 \log C=4Hn^2+O(1),\qquad
 \log B(nG+T)=Hn^2+o(n^2) \quad (T\in E_6[2],\ n\text{ odd}).
\]
The first follows from \(-6<X(nG)<0\) and the exact denominator \(w\). For the second, the archimedean contribution \(\log^+|X(nG+T)|\) is \(o(n^2)\). For completeness fix \(k\), write \(n=kj+t\), and consider the map \(S\mapsto X(kS+tG+T)\). Its poles lie at finitely many algebraic points and have multiplicity 2. Proximity of \(jG\) to such a point in local distance is bounded logarithmically by proximity of \(X(jG)\) to its algebraic abscissa, up to a constant. Roth's theorem and the elementary rational-target bound give an upper bound \(3h(X(jG))+O_k(1)\) for the latter, using projective distance. At infinity the rational-target bound applies as well. Away from the poles compactness gives a bounded contribution. Exact equality with a pole can occur only finitely often for fixed \(k\). Dividing by \(n^2\) gives an upper limit \(O(H/k^2)\); let \(k\) grow. The same proof applies to \(B(mG)\) for unrestricted \(m\).

For \(p\ge5\), let \(r_p=\mathrm{ord}(G\bmod p)\), \(e_p=v_p(B(r_pG))\). Define
\[
 W(r)=\sum_{r_p=r}(e_p-1)\log p,\qquad
 L(r)=\sum_{r_p=r}e_p\log p.
\]
The formal group at odd \(p\) gives \(v_p(B(mG))=e_p+v_p(m/r_p)\) if \(r_p\mid m\), zero otherwise. Thus the total ordinary lifting cost at a given \(m\) is at most \(\log m\). Each fixed bad prime contributes \(O(\log(2m))\): the preimage of the local formal subgroup under \(m\mapsto mG\) is a finite-index subgroup of \(\mathbf Z\), and at sufficiently deep a fixed level the formal logarithm preserves valuations. More explicitly outside that subgroup the denominator valuation is bounded, and inside it the valuation adds \(v_p(m/m_0)\) to a fixed depth. With \(m=2n\), the radical identity and the four denominator estimates imply
\[
 \log(C/R)=\sum_{r\mid 2n}W(r)+o(n^2).
\]
Thus the abc inequality for this full signature, in the form \(C\ll_\epsilon R^{1+\epsilon}\) for every \(\epsilon>0\), is equivalent to
\[
 W(r)=o(r^2)\qquad(r\to\infty,\ v_2(r)\le1).
\]
Indeed a rank with positive normalized excess enters \(m=\mathrm{lcm}(2,r)\le2r\), with \(m/2\) odd. Conversely \(\sum_{r\mid m}r^2\le\zeta(2)m^2\); a finite set of small ranks contributes only a constant. A positive proportion of the height also forces a rank \(r\ge m/K\) with positive normalized excess for some fixed \(K\), since \(W(r)\ll r^2\) and \(\sum_{j>K}j^{-2}\to0\). Accumulation of individually subquadratic rank totals cannot violate the inequality; aggregation of many primes at a single rank remains possible.

Möbius inversion gives the unconditional first-appearance mass
\[
 L(r)=H J_2(r)+o(r^2),\qquad J_2(r)=r^2\prod_{q\mid r}(1-q^{-2}).
\]
Indeed \(\log B(mG)=\sum_{r\mid m}L(r)+O(\log(2m))=Hm^2+o(m^2)\). After inversion, errors \(o(d^2)\) over divisors \(d\mid r\) sum to \(o(r^2)\) by the same convergent-square estimate and a finite cutoff. Equivalently the uniform inequality demands first-appearance radical logarithm \(HJ_2(r)+o(r^2)\) for eligible ranks.

The individual factors have an equally sharp statement. At odd \(s\), partition primes by their first odd index encountering \(T\). For \(T=O\) this means \(r_p=s\), and for \(T\ne O\) it means \(r_p=2s\) with \(sG\equiv T\bmod p\). Write \(L_T(s),W_T(s)\) for the same weights on such primes. At odd multiples \(n\) of \(s\), the factor \(B(nG+T)\) contains \(p\) to depth \(e_p+v_p(n/s)\). This follows since doubling preserves formal depth at \(p\ge5\), and \((n/s)(sG+T)=nG+T\). At 2 and 3 the coordinates divide \(B(2nG)\). The same inversion over odd divisors gives
\[
 L_T(s)=HJ_2(s)+o(s^2)\quad\text{for each of the four }T.
\]
At \(r=2s\), the three nonidentity layers give the expected total \(3HJ_2(s)=HJ_2(2s)\). The uniform inequality is equivalent to \(W_T(s)=o(s^2)\) in each layer.

For a single prime the exact normalized limiting excess is
\[
 \limsup_{n\to\infty,\;n\ {\rm odd}}
 \frac{\max_{p\mid abw}(v_p(abw)-1)\log p}{\log C}
 =
 \frac1H\limsup_{r\to\infty,\;v_2(r)\le1}
 \frac{\max_{r_p=r}(e_p-1)\log p}{\mathrm{lcm}(r,2)^2}
\]
with empty maxima defined as zero. The earliest index \(2n=\mathrm{lcm}(2,r)\) attains the first depth. Every later index has a larger denominator in this ratio and ordinary lifting contributes only \(O(\log n)\). The identical statement holds upon replacing both excess functions \(v-1\) by \(\lfloor v/2\rfloor\), since additional lifting changes this exponent by at most the added valuation. Thus an isolated large power can decide abc here precisely when first-depth excess already carries a fixed fraction of the earliest height. In particular infinitely many \(e_p\ge2\) and \(\log p\gg r_p^2\) at eligible ranks suffice. The already verified good prime 211 occurs to depth 2 in \(d\) at \(n=53\): \(Q=G+T_+\) has order 53 modulo 211, and the previous first-depth calculation transfers under the degree-two isogeny. [Finite first-depth computation](abc_eisenstein_slice_gaussian_kummer.md)

## A CM restriction and a quantitative smoothness test

Take an unbounded sequence of odd indices \(s\) with all prime divisors \(3\bmod4\), for example the primes in that class. Consider primes of first appearance in the \(w\) factor, so \(r_p=s\). They all satisfy \(p\equiv1\bmod12\) and the Gaussian action on the reduction of \(E_6\) is rational over \(\mathbf F_p\). Its ordinary Frobenius \(\pi\in\mathbf Z[i]\) has norm \(p\). The annihilator of \(G\bmod p\) as a Gaussian module ideal contains \((s)\) and meets \(\mathbf Z\) in \(s\mathbf Z\). Every Gaussian prime over a divisor of \(s\) remains inert, so the only possible ideal is \((s)\) itself. Therefore
\[
 \pi=1+s(u+iv),\qquad p=(1+su)^2+s^2v^2\ge(s-1)^2,
 \qquad u,v\in\mathbf Z.
\]
In particular there are at most \(O((1+\sqrt X/s)^2)\) candidate primes up to \(X\). This already implies a primitive prime power \(p^{e_p}\gg s^4/\log s\), by comparing the count times \(\log X\) with \(L_O(s)\gg s^2\).

A sieve removes the logarithm. Uniformly in these \(s\), the number of candidates at \(X\) is
\[
 \ll \frac{(1+\sqrt X/s)^2}{\log(2+\sqrt X/s)}.
\]
Indeed put \(L=2+\sqrt X/s\); all pairs lie in a square \(|u|,|v|\le L\). For every prime \(\ell\equiv1\bmod4\), the norm polynomial vanishes in exactly \(2\ell-1\) residue pairs modulo \(\ell\): it is a union of two distinct affine lines since \(\ell\nmid s\). For squarefree \(h\) made of these primes, the count in the box equals its area in lattice points times \(g(h)=\prod_{\ell\mid h}(2\ell-1)/\ell^2\), with error \(O(2^{\omega(h)}(L+h))\) by counting each residue in both coordinates. The usual dimension-one upper-bound sieve through \(z=L^{1/40}\), with level \(D=L^{1/4}\), gives \(O(L^2/\log L)\) survivors. Its Euler product is \(\prod_{\ell<z,\,\ell\equiv1(4)}(1-1/\ell)^2\asymp1/\log z\) by Mertens in progressions; the weighted remainder \(\sum_{h<D} 3^{\omega(h)}2^{\omega(h)}(L+h)\ll L^{5/4}(\log(2L))^5\) is negligible. Sieving may remove prime values below \(z\), contributing at most \(z\) additional distinct rational primes.

It follows unconditionally that the largest primitive prime power in \(w\) satisfies
\[
 \max_{r_p=s}p^{e_p}\gg s^4.
\]
If this maximum \(X\) exceeds \(s^4\) the result is immediate. If \(X\le s^3\), the elementary count times \(\log X\) is \(o(s^2)\), impossible for large \(s\). In the remaining interval \(s^3\le X\le s^4\), the logarithms \(\log X\) and \(\log(2+\sqrt X/s)\) are comparable. Hence \(L_O(s)\le\log X\cdot\#\{p\le X:r_p=s\}\ll X/s^2\), proving the bound. The prime power may have exponent one.

These bounds also give two routes to a fixed abc exponent, both conditional on smoothness at infinitely many such indices.

* If every primitive prime of \(w\) is at most \(o(s^4)\), the primitive radical in \(w\) has logarithm \(o(s^2)\) by the sieved count and the same two intervals. Hence \(W(s)=HJ_2(s)+o(s^2)\), contradicting the uniform inequality. Even \(\max_{r_p=s}p\le c_0s^4\) infinitely often suffices for any sufficiently small absolute \(c_0>0\) depending on this curve. Under abc the largest primitive prime itself is \(\gg s^4\).
* If all primitive primes of \(w\) are at most \(K s^2\) for fixed \(K\), the elementary Gaussian count gives only \(O_K(1)\) possibilities. One individual first-depth prime power then has \((e_p-1)\log p\gg_K s^2\); its exponent is \(\gg_K s^2/\log s\). Such an infinite smooth subsequence would contradict abc via an isolated prime power. Each candidate has the displayed norm with \(u,v\) bounded solely in terms of \(K\).

For prime \(s\equiv3\bmod4\), the first criterion gives \(W(s)=Hs^2+o(s^2)\). Along such a smooth subsequence one would have \(\log R/\log C\le 3/4+o(1)\) from the single factor \(w\), and therefore abc qualities at least \(4/3-o(1)\). No infinite smooth subsequence or positive first-depth proportion is established here.
