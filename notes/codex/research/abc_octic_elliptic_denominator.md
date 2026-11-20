# One elliptic denominator measures the radical of the entire octic triple

Fix an admissible seed and the genus-one orbit \(P_m\) from the [two-squareful construction](abc_octic_two_squareful_norms.md). The index \(m\) is positive and odd, \(d\) is the squarefree part of \(s_0^4+4t_0^4\), and \(T=[P-\iota P]\) is the non-torsion seed class. Write \(S=2T\) on the rational elliptic curve \(E_d:V^2=X^3-d^2X\). Define the positive integer \(B_m\) by writing \(X([m]S)\) in lowest terms with denominator \(B_m^2\).

For the normalized primitive pair \(s,t\) at this index, put \(H=\max(s,t)\), \(C=(s^4+4t^4)^2\), and \(R=\operatorname{rad}(|2st(s^8-16t^8)|)\). Then
\[
 R=\operatorname{rad}(dB_m),\qquad
 \log C=\widehat h(S)m^2+O(1),\qquad
 \log B_m=\widehat h(S)m^2+o(m^2).
\]
This includes all six factors of the radical; an exceptional contribution from \(s,t\) or \(s^4-4t^4\) is included too. The constants in this note are for a fixed seed.

## Coordinates and the height

On the untwisted model \(V^2=X^3-X\) the quartic coordinate is \(x=V/X\). The involution on the quartic becomes \(P\mapsto(0,0)-P\), and duplication gives \(X(2P)=(x^4+4)/(4x^2)\). Translating by \((0,0)\) negates and inverts the elliptic \(X\)-coordinate. Twisting multiplies that coordinate by \(d\). Since \(P_m-\iota P_m=mT\), for \(x(P_m)=s/t\) and \(s^4+4t^4=d z^2\) this yields
\[
 X(mT)=-4s^2t^2/z^2,\qquad
 V(mT)=\pm 2st(s^4-4t^4)/z^3 .
\]
Taking absolute values of the coordinates preserves \(X(mT)\). One may arrange \(s\) odd and \(t\) even for any odd \(m\): the two cannot both be odd since \(d\equiv1\bmod8\). If \(s\) is even and \(t\) odd, reduction of \(d(z/2)^2=4(s/2)^4+t^4\) modulo 8 gives \(4\mid s\), and the primitive replacement \((s,t,z)\mapsto(t,s/2,z/2)\) preserves \(X(mT)\). Zero and infinite slopes give at most finitely many exceptional indices and can be discarded.

The duplication formula on the twist now gives
\[
 X(mS)=
 \left(\frac{s^8+24s^4t^4+16t^8}
 {4st(s^4-4t^4)z}\right)^2.
\]
This fraction is reduced. The numerator is odd. At odd primes dividing \(s\) or \(t\) it is a unit. At a prime dividing \(s^4-4t^4\) it reduces to \(128t^8\), and at a prime dividing \(z\) it reduces to \(16s^4t^4\). These are units by primitivity. Hence \(B_m=4|st(s^4-4t^4)|z\) and the asserted radical identity follows. The numerator is comparable to \(H^8\) and the absolute denominator is \(O(H^8)\), so \(h(X(mS))=16\log H+O(1)=2m^2\widehat h(S)+O(1)\).

For completeness the archimedean contribution \(\log^+|X(mS)|\) is \(o(m^2)\). Fix \(k\) and write \(m=a+kb\), \(0\le a<k\). If \(mS\) approaches the origin, \(bS\) must approach one of finitely many algebraic preimages of \(-aS\) under the unramified map \([k]\). Using a local coordinate, the logarithmic proximity of \(mS\) to the origin is at most the proximity of \(X(bS)\) to the corresponding algebraic coordinate plus a \(k\)-dependent constant. At a pole use projective distance. Rational height separation for rational targets and Roth's theorem for irrational targets bound the latter by \(3h(X(bS))+O_k(1)\). The possible exact coincidences are finite for fixed \(k\). The pole of \(X\) has order two, so \(\limsup m^{-2}\log^+|X(mS)|\ll \widehat h(S)/k^2\). Let \(k\) grow. Subtracting this term from \(h(X(mS))\) gives \(2\log B_m\) and proves the stated asymptotic.

## The remaining first-occurrence question

For \(p\nmid2d\) let \(r_p\) be the order of the reduction of \(S\) modulo \(p\), and let \(e_p=v_p(B_{r_p})\). Then \(p\mid B_m\) exactly when \(r_p\mid m\); at such indices
\[
 v_p(B_m)=e_p+v_p(m/r_p).
\]
Indeed \(p\mid B_m\) means reduction to the identity, and its valuation is the valuation of the formal parameter there. The good-reduction formal logarithm preserves that valuation for odd \(p\). For fixed bad primes the denominator valuations at multiples of \(S\) are \(O(1+\log m)\) by passing to the finite-index deep formal subgroup, then applying the same logarithm there. [Formal group background, Silverman, Chapters IV and VII](https://doi.org/10.1007/978-0-387-09494-6)

Put \(W_r=\prod_{p\nmid2d,\ r_p=r}p^{e_p-1}\). The product of all factors from the subsequent increments \(v_p(m/r_p)\) divides \(m\). Consequently
\[
 \log(C/R)=\sum_{r\mid m}\log W_r+o(m^2).
\]
There is a fixed-exponent abc violation infinitely often on this orbit **if and only if** \(\limsup_{r\to\infty,\ r\ {\rm odd}}r^{-2}\log W_r>0\). For the converse direction of the equivalence use \(\sum_{r\mid m}r^2\le\zeta(2)m^2\). Finite initial ranks contribute a bounded amount. At this point the size of the first-occurrence excess at varying primes is unknown. This is a criterion on a fixed orbit; there is no reduction here of arbitrary rational abc triples to that one orbit.

## A size constraint on primes that could provide the excess

For every fixed \(0<\epsilon<1\), the following two contributions to \(\log B_m\) are each \(o(m^2)\) as \(m\) tends to infinity through odd indices:

* Primes \(p\equiv1\bmod4\) with \(p\,v_p(B_m)\le m^{4-\epsilon}\).
* Primes \(p\equiv3\bmod4\) with \(p\,v_p(B_m)\le m^{3-\epsilon}\).

Here the *entire* valuation is counted. The result in particular controls the repeated part. To prove it, discard the fixed bad primes and account for the increments after first occurrence by \(O(\log m)\).

At a split good prime \(p\), choose one of the places over it in \(K=\mathbb Q(i)\). The reduction of \(S\) has annihilator ideal \(I\) under Gaussian multiplication on the elliptic curve. The ideal \(I\) divides \((m)\) for \(p\mid B_m\). Choose a generator \(\alpha\) of \(I\) and put \(D_I=N(I)\). At these primes the first formal depth of \([\alpha]S\) equals \(e_p\). Indeed \(r_p/\alpha\) is integral and its differential is a unit there: \(r_p\mid\#E_d(\mathbb F_p)\), whose order is divisible by four because of full rational 2-torsion, and is less than \(4p\) by Hasse's bound, so \(p\nmid r_p\). The differential of any Gaussian integer has norm its Gaussian norm, and \(N(r_p/\alpha)\mid r_p^2\). A fixed \(I\) therefore satisfies
\[
 \sum_{p\ {\rm assigned\ to}\ I} e_p\log p \ll 1+D_I .
\]
This follows by summing the denominator contributions to \(h(X([\alpha]S))=2D_I\widehat h(S)+O(1)\) over the selected places. The degree of \(K\) is fixed.

At each such split prime the Frobenius endomorphism commutes with \(i\), since the latter is defined over \(\mathbb F_p\). Thus Frobenius belongs to \(\mathbb Z[i]\): the centralizer of \(i\) in the elliptic endomorphism algebra is \(\mathbb Q(i)\), and Frobenius is integral. Write it \(\pi\), with \(N(\pi)=p\). Rationality of the reduction gives \(\pi\equiv1\bmod I\). For \(D_I\ge4,\ X\ge2\) this implies
\[
 \sum_{\substack{p\le X\\p\ {\rm assigned\ to}\ I}}\frac{\log p}{p}
 \ll \frac{\log^2(2X)}{D_I}.
\]
Indeed \(\pi=1+\alpha u\) with nonzero \(u\in\mathbb Z[i]\), and \(|\pi|\ge|\alpha u|/2\). Sum over lattice points using \(\sum_{0<|u|\le 2\sqrt X}|u|^{-2}\ll\log(2X)\). Small \(D_I\) can always use the height bound. Among primes satisfying \(p\,v_p(B_m)\le X\) the mass of *initial* valuations per \(I\) is therefore \(O(\sqrt X\log(2X))\), taking the smaller of the height and lattice bounds. The number of ideals dividing \((m)\) is at most \(\tau(m)^2=m^{o(1)}\). Put \(X=m^{4-\epsilon}\) to obtain \(O(m^{2-\epsilon/2+o(1)})\), including the lifts.

For \(p\equiv3\bmod4\) of good reduction, \(\#E_d(\mathbb F_p)=p+1\), by cancellation in the character sum under \(X\mapsto-X\). Thus for a fixed ordinary rank \(r=r_p\mid m\), \(p\equiv-1\bmod r\). The initial mass at that rank is \(O(r^2)\) by the height of \(X(rS)\), while
\(\sum_{p\le X,\ p\equiv-1\bmod r}(\log p)/p\ll\log^2(2X)/r\) for \(r\ge2\), by summing over \(jr-1\). For \(p\,v_p(B_m)\le X\) the smaller of the two mass bounds is \(O((X\log^2(2X))^{2/3})\). Summing over the divisors of \(m\) and setting \(X=m^{3-\epsilon}\) gives \(O(m^{2-2\epsilon/3+o(1)})\).

All primes dividing \(U_\pm=(s\pm t)^2+t^2\) are split. At good primes of either norm \(v_p(U_\pm)=2v_p(B_m)\), since the other factors of the displayed denominator are coprime to that norm there. Hence for either sign the mass of primes satisfying \(p\,v_p(U_\pm)\le m^{4-\epsilon}\) is \(o(m^2)\), while \(\log U_\pm\asymp m^2\). In particular, deciding whether there is *any* prime of exact valuation two becomes much weaker than deciding whether such primes carry almost all of the logarithm: a positive proportion of the logarithm at valuations at least four in one fixed norm would already give a counterexample subsequence, because \(\operatorname{rad}(U_\mp)\ll_d\sqrt{U_\mp}\). The estimates here leave the large-prime first valuations unresolved.
