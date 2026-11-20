# An abc-equivalent eighteenth-power family with forced repeated primes in one sextic

Fix a real \(\eta>0\) and an integer cutoff \(Z\ge3\). There is an explicit fixed family of primitive positive triples
\[
                    B^{18}+(A^{18}-B^{18})=A^{18},\qquad B<A ,
\]
with both properties below.

* Proving the abc inequality on this one family, for every positive exponent increment, implies the full rational abc conjecture.
* For **every** member of sufficiently large height, primes \(Z<p<A^\eta\) of exact order 18 for \(A/B\bmod p\) supply a repeated part of \(\Phi_{18}(A,B)=A^6-A^3B^3+B^6\) at least \(c_{\eta,Z}A^{3/2}\). Every prime used in this certificate has valuation at least three.

## The family and its repeated factors

Let \(f(T)=-(5T^6+8T^3+2)/(T^2(2T^6+8T^3+5))\). Choose \(k\) divisible by \(p-1\) for all \(p\le Z\) and large enough that \(2\varphi(9k)<8k\eta\). Such multiples exist by adjoining distinct primes, since \(\varphi(9k)/k=9\prod_{p\mid9k}(1-1/p)\). For each reduced \(0<x/y<1\) define \(A/B=-f((x/y)^k)\) in positive lowest terms, with \(A>B\). In homogeneous integral coordinates the defining map has degree \(8k\), has no common projective zero and has bounded output gcd on primitive inputs by its resultant. The maximum of the two coordinate moduli on the normalized real shell is bounded above and away from zero. Consequently \(A\asymp_k y^{8k}\). [Explicit map and its ramification](abc_cyclotomic_ninth_contact_maps.md)

Put \(U=\Phi_9(x^k,y^k)\), so \(y^{6k}\le U\le3y^{6k}\). The polynomial identity at the six roots gives \(U^3\mid\Phi_9(P(x^k,y^k),Q(x^k,y^k))\) in homogeneous integral coordinates for \(f\). The sign change in the positive output replaces \(\Phi_9\) by \(\Phi_{18}\). If \(g\) is the output gcd, then \(U^3\mid g^6\Phi_{18}(A,B)\). In fact every \(p\ne3\) dividing \(U\) has **exactly** \(3v_p(U)\) as its valuation in the normalized output form. To see this put \(F(T)=\Phi_9(T,1)\) and \(V=(P^6+P^3Q^3+Q^6)/F^3\) in affine coordinates. Direct polynomial division gives \(V\equiv-4860(T^3+1)\bmod F\) and \(\operatorname{Res}(F,Q)=3^9\). At \(p\mid U,\ p\ne3\), the input \(t=x^k/y^k\) has order nine, so \(p\ge19\), \(t^3\ne-1\), and both \(Q(t)\) and \(V(t)\) are units. This proves the exact valuation, including after gcd normalization.

For \(p\le Z\), \(p\mid xy\) makes \(U\) a unit, and \(p\nmid xy\) gives \(U\equiv3\bmod p\) since \(p-1\mid k\). Only \(3\) can remain; its valuation is at most one by the ninth-order form modulo nine. For every remaining \(p\mid U\), one has \(v_p(\Phi_{18}(A,B))\ge3v_p(U)\). Also \(p\) divides \(x^{9k}-y^{9k}\), hence some \(\Phi_d(x,y)\) for \(d\mid9k\). Thus
\[
          p\le (2y)^{\varphi(d)}\le y^{2\varphi(9k)}<A^\eta
\]
for sufficiently large \(y\), by the strict choice of exponent. These primes are prime to \(18AB\) and have exact multiplicative order 18 by separability modulo \(p\). Taking their contributions gives at least \((U/3)^2\gg_k A^{3/2}\), as claimed.

The family can also require **any prescribed number \(J\)** of distinct contributing primes for every sufficiently large base. Enlarge the power of two dividing \(k\) until \(v_2(k)+1\ge J\). Put \(a=v_3(k)\). For \(0\le i\le v_2(k)\), each order \(m_i=2^i3^{a+2}\) has a primitive prime \(q_i\) for \(x/y\) by the explicit odd-valuation theorem. These primes are distinct. Since \(m_i/\gcd(m_i,k)=9\), the ratio \(x^k/y^k\) has order nine at each \(q_i\); hence \(q_i\mid U\). They are all in the indicated size range and have output valuations divisible by three. [Primitive primes at every required order](abc_cyclotomic_odd_primitive_grid.md)

## Recovering unrestricted abc

The rational map \(\beta(t)=f(t^k)^{18}\) has degree \(D=144k\). Its branch values lie in \(0,1,\infty\). Indeed the only critical values of \(f\) are \(0,\infty\) and primitive ninth roots; the eighteenth power sends the latter to one. The intermediate power \(t^k\) branches only at zero and infinity, which \(f\) exchanges. Moreover \(\beta(0),\beta(1),\beta(\infty)\in\{0,1,\infty\}\) since \(f(1)=-1\).

By Riemann–Hurwitz the reduced preimage of \(0,1,\infty\) has degree \(D+2\). Its homogeneous squarefree polynomial over \(\mathbf Q\) is a constant times \(X Y(X-Y)G(X,Y)\) with \(\deg G=D-1\), after integral scaling. For primitive inputs, outside a fixed finite set of primes, every prime dividing the output radical \(R'=\operatorname{rad}(AB(A^{18}-B^{18}))\) divides this reduced boundary value. This also follows directly by factoring the three unnormalized output coordinates of the power triple. No factor vanishes on \(0<x/y<1\). With \(R_0=\operatorname{rad}(xy(y-x))\) we therefore have
\[
          R'\ll_k R_0\, y^{D-1},\qquad A^{18}\asymp_k y^D .
\]
A restricted abc inequality \(A^{18}\ll_{k,s} (R')^{1+s}\) gives \(y^{1-(D-1)s}\ll_{k,s} R_0^{1+s}\). To obtain any specified \(1+\varepsilon\), choose \(s=\varepsilon/(D+(D-1)\varepsilon)\). This proves the unrestricted inequality for the arbitrary triple \(x+(y-x)=y\). The forward implication applies ordinary abc directly to each primitive triple in this family. [General marked-point argument](abc_marked_rational_radical_bounds.md)

The guaranteed \(A^{3/2}\) concerns one sextic factor at every base. Proving the required bound for the full radical on this family remains equivalent to the conjecture.
