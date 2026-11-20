# Large common factors in small Pell solutions over varying fields

For infinitely many distinct positive squarefree composite integers \(D\), there is a positive solution to \(x^2-Dy^2=1\) with
\[
 x\ll D^{9/4},\qquad
 g=\gcd(D,y)\gg \frac{D^{3/7}}{(\log D)^{3/7}}.                         \tag{1}
\]
The same common-factor lower bound, up to an absolute constant, applies to the coefficient of \(\sqrt D\) in the least positive norm-one unit greater than one in \(\mathbb Z[\sqrt D]\). The common factor alone would force an abc counterexample sequence if it exceeded \(D^{1/2+\eta}\) for fixed \(\eta>0\) under this polynomial height bound.

## Constructing the fields

Let \(G(t)=t(t^3-1)\), \(H(t)=t^6-3t^3+3\), and \(x(t)=2(t^3-1)^3+1\). Direct expansion gives
\[
 x(t)^2-1=4G(t)^3 H(t).
\]
For \(t\equiv2\bmod12\), \(G(t)\) and \(H(t)\) are coprime: \(H(t)\) is 3 modulo \(t\) and 1 modulo \(t^3-1\). If \(G\) is squarefree and \(H=sv^2\) with \(s\) squarefree, put \(D=Gs\) and \(y=2Gv\). Then \(D\) is squarefree, \(g\ge G\asymp t^4\) and \(x\asymp t^9\). It remains to arrange a sufficiently large square in \(H(t)\) while keeping \(G(t)\) squarefree.

For \(T\) large set \(P=T^{1/3}/\sqrt{\log T}\). There are \(\gg P/\log P\) primes \(p\in[P,2P]\) at which \(H\) has a simple root. Indeed \(H\) is separable, and Chebotarev's density theorem applied to its fixed splitting field supplies that many completely split primes. For each such \(p>3\) choose one lift of a root modulo \(p^2\) by Hensel's lemma. We count pairs \((p,t)\) with \(T\le t\le2T\), \(t\equiv2\bmod12\), and \(t\) in this chosen class modulo \(p^2\).

Fix a sufficiently large constant \(z\). Sieve out \(\ell^2\mid G(t)\) for primes \(\ell\le z\) by the Chinese remainder theorem. On this progression the factors \(t,t-1,t^2+t+1\) are pairwise coprime, 2 occurs exactly once, and 3 is absent. For \(\ell\ge5\) at most four residue classes modulo \(\ell^2\) are forbidden, since the quadratic has discriminant \(-3\) and all roots modulo \(\ell\) are simple. The local density is bounded below independently of \(z\) by a positive constant times \(\prod_{\ell\ge5}(1-4/\ell^2)>0\). With \(z\) fixed the counting error per \(p\) is \(O_z(1)\); thus \(\gg T/(P\log P)\) pairs remain, with an absolute lower-bound constant for sufficiently large \(T\) depending on \(z\).

Put \(Z=T^{1/3}\log T\). For \(z<\ell\le Z,\ \ell\ne p\), the number of discarded pairs is at most
\[
 O\!\left(\frac{T}{P\log P}\sum_{\ell>z}\frac1{\ell^2}
           +PZ/(\log T)^2\right).
\]
This follows by CRT for each pair \(p,\ell\), with at most four progressions of modulus \(p^2\ell^2\). The case \(\ell=p\) cannot occur since \(G(t)\) and \(H(t)\) are coprime. Chebyshev's prime bound gives \(O(PZ/(\log T)^2)\) prime pairs. This term is \(o(T/(P\log P))\), and \(z\) can be chosen large enough to absorb the first term.

For \(\ell>Z\), count the exceptional \(t\) without the progression at \(p\). Put \(B=T^{2/3}(\log T)^{1/3}\). Between \(Z\) and \(B\), summing root classes gives \(O(T/Z+B/\log B)\). Above \(B\), only \(t^2+t+1\) can be divisible by \(\ell^2\). Write \(t^2+t+1=j\ell^2\), where \(j\ll T^2/B^2\). For each \(j\) there are \(O(1)\) possibilities. Indeed
\[
 \left|\frac{2t+1}{\ell}-2\sqrt j\right|
 =\frac{3}{\ell^2((2t+1)/\ell+2\sqrt j)}
 \ll \frac{\sqrt j}{T^2}.
\]
The fractions are reduced since any common prime would divide 3, and \(\ell>B\). Their denominators are \(O(T/\sqrt j)\), so distinct fractions have distance \(\gg j/T^2\). This proves the claimed bound for \(j\ge1\). Each excluded \(t\) could occur for at most \(O(1)\) selected \(p\), since the product of their squares divides \(H(t)\ll T^6\). Consequently the large-\(\ell\) exclusions cost \(O(T/Z+B/\log B+T^2/B^2)=o(T/(P\log P))\) pairs. These estimates establish the existence of the desired \(t\) in every sufficiently large dyadic interval.

As \(p^2\mid H(t)\), we have \(s\le H(t)/p^2\). Therefore
\[
 t^4\ll D\ll t^{28/3}\log t,\qquad g\gg t^4.
\]
This proves (1) and forces unbounded \(D\). To pass to the least norm-one unit \(V=x_1+y_1\sqrt D\), write \(x+y\sqrt D=V^k\). Since \(V>\sqrt D\) and \(x+y\sqrt D<2x\ll D^{9/4}\), \(k\) is absolutely bounded. Expansion gives \(y\equiv kx_1^{k-1}y_1\bmod D\); also \(\gcd(x_1,D)=1\). Squarefreeness now gives \(g\le k\gcd(D,y_1)\).

## Full divisibility and the fixed-exponent gap

For \(m=D/g\), write \((x+y\sqrt D)^m=X+Y\sqrt D\). The same expansion yields \(D\mid Y\). Thus the primitive triple \(1+D Y^2=X^2=C\) satisfies
\[
 \frac{C}{\operatorname{rad}(C D Y)}\ge\frac{X}{Y}>\sqrt D,\qquad
 \log C \ll D^{4/7}(\log D)^{10/7}.
\]
In particular, on this infinite family the guaranteed factor from ramified primes alone is at least a constant times \((\log C)^{7/8}/(\log\log C)^{5/4}\). This construction controls divisibility in distinct quadratic fields. It does not retain the small-unit height bound after enforcing \(D\mid Y\).

The original identity also shows precisely what would give a disproof. If \(s=\operatorname{sf}(H(t))\le t^{4-\delta}\) infinitely often for any fixed \(\delta>0\), then \(\operatorname{rad}(H)\le sv=\sqrt{sH}\) gives
\[
 \frac{x^2}{\operatorname{rad}(x(x^2-1))}
 \ge \frac{x}{2G\sqrt{sH}}\gg t^{\delta/2}.
\]
Here \(x^2\asymp t^{18}\). This last implication does not require \(G(t)\) squarefree and holds for positive \(t\ge2\).

A small instance of the identity, separate from the progression used in the sieve, is \(t=11\). It gives \(G=14630\), \(H=13^2\cdot10459\), \(D=153015170\), \(x=4705274001\), and \(y=380380\). Here \(x^2-Dy^2=1\) and \(\gcd(D,y)=14630>\sqrt D\). A finite crossing of the threshold does not supply the fixed exponent or infinitude required above.

Several possible ways of forcing that event can be bounded.

* For any fixed finite set \(S\) of primes and any \(\epsilon>0\), the \(S\)-part of \(H(t)\) is \(O_{S,\epsilon}(t^{1+\epsilon})\). Apply the \(p\)-adic Subspace Theorem to \((t,1)\), using the two coordinate forms at infinity and \(X-\alpha_pY,Y\) at \(p\), where \(\alpha_p\) is a nearest \(p\)-adic root when the valuation is large. Separability and compactness give \(\lvert t-\alpha_p\rvert_p\asymp_{H,p}\lvert H(t)\rvert_p\) in this case. Bounded valuations can be ignored. There are finitely many choices, and each exceptional rational line gives at most one such \((t,1)\).
* For a fixed rational substitution \(t=F(s)\) of degree \(d\) with infinitely many integral outputs at rational \(s\), \(F\) has at most two distinct geometric poles by Siegel's theorem on integral points on the projective line with the poles removed. Equivalently, writing the two coprime homogeneous forms representing \(F\) at primitive coordinates, their common divisor is bounded by a fixed resultant. At integral outputs this bounds the denominator form. If \(r\) is the number of poles, \(d-r\) units of the total ramification \(2d-2\) are already used there. Above the six simple roots of \(H\), a point of multiplicity \(e\) contributes at most \(2\lfloor e/2\rfloor\le2(e-1)\) to the degree of a square divisor of the homogeneous numerator of \(H(F)\). Such a square has degree at most \(2(d+r-2)\le2d\). Since \(|t|\asymp_F \max(|a|,|b|)^d\) for large integral outputs \(F(a/b)\), this polynomially forced square is \(O_F(t^2)\). Extra squares of individual integer values are outside this degree bound.
* A concrete variable-prime lift illustrates the scale. Put \(P(u)=u+u(u^3-1)H(u)/9\). Its derivative is \(2(5u^3+1)H(u)/9\) and \(P(u)\equiv u\bmod H(u)\) in \(\mathbb Q[u]\). Thus \(H(u)^2\mid H(P(u))\) there. For \(u\equiv1\bmod9\), \(P(u)\) is integral and \(3\nmid H(u)\), so the divisibility holds over the integers after specialization. The square has size \(\asymp |P(u)|^{6/5}\), below the sufficient \(t^{2+\delta}\) scale.

For context, Yijie Diao's preprint states a power-saving upper bound for the number of nonsquare \(D<X\) whose least positive norm-one Pell unit is at most \(D^L\), for every fixed \(L\). We checked the statement of Theorem 1.3 in the author's manuscript. Its count allows the infinite sparse family in (1). None of the proofs above use the preprint. [Diao, Theorem 1.3](https://github.com/s6yidiao-cloud/pell-lean/blob/c54387e7d4914e2e98ae5ec4c1f004d0b862e34a/paper/main.pdf)

## A related norm-two construction

We also read the author's copy of Wouter van Doorn's *Three-term arithmetic progressions of consecutive powerful numbers*. It proves the existence of infinitely many progressions of powerful numbers of the form \((X-2)^2,(X-1)^2,X^2-2\), using a fixed squarefree kernel 7. That infinitely many such progressions are consecutive **in the sequence of all powerful numbers** is a conjecture in the paper. Sections 4–5 consider the set of squarefree \(D\) for which \(X^2-D^3z^2=2\) has solutions. [Author's manuscript](https://github.com/Woett/A-normal-paper-is-probably-fine/blob/c965cf4b00d554fdb8dc05887bec0851a17e7709/Three-term%20arithmetic%20progressions%20of%20consecutive%20powerful%20numbers.pdf)

For an unconditional varying-kernel example set \(U=j(3072j^4-320j^2+15)\), \(A=32j^2-1\), \(B=288j^4-33j^2+2\) with \(j\) positive and odd. Expansion gives \(U^2-2=A^3B\). Also \(32B\equiv40\bmod A\), while \(A\) is odd and \(5\nmid A\) (the required square would be \(3\bmod5\)). Thus \(\gcd(A,B)=1\). A positive proportion of odd \(j\) have squarefree \(A\). Indeed the small-prime local sieve has positive density, with at most two roots modulo each odd prime square. For \(\ell>T^{2/3}\) dividing \(A\) twice on \(T\le j\le2T\), write \(32j^2-1=k\ell^2\). Then \(k\ll T^{2/3}\), \(\gcd(j,\ell)=1\), and \(j/\ell\) is within \(O(\sqrt k/T^2)\) of \(\sqrt{k/32}\) with denominator \(O(T/\sqrt k)\). The same spacing argument as above gives \(O(1)\) pairs per \(k\); the intervening primes cost \(O(T/z+T^{2/3})\) after a fixed small-prime cutoff \(z\).

Write \(B=s v^2\), \(D=As,\ y=Av\). Then \(U^2-Dy^2=2\), and odd squarefree \(D\) satisfies \(T^2\ll D\ll T^6\), \(g=\gcd(D,y)\ge A\gg D^{1/3}\). For the odd integer \(m=D/g\), define
\[
 X+Y\sqrt D=(U+y\sqrt D)^m/2^{(m-1)/2}.
\]
The coefficients are integral since \((U+y\sqrt D)^2/2=(U^2-1)+Uy\sqrt D\). The norm is 2, and \(D\mid Y\) by expansion modulo \(D\), since \(2\) is invertible there. Hence \(X^2-2=DY^2\) is powerful and has squarefree kernel \(D\). The primitive triple \(2+DY^2=X^2=C\) satisfies \(C/\operatorname{rad}(2CDY)\ge\sqrt D/2\) and \(\log C\ll D^{2/3}\log D\). Here \(X,Y\) are odd since \(D\equiv7\bmod8\), as follows from \(U^2-Dy^2=2\) with \(U,y\) odd. For example \(j=1\) gives \(U=2767,\ D=31\cdot257,\ y=31,\ m=257\). These moving examples establish no consecutiveness assertion and leave the fixed-exponent abc question open.
