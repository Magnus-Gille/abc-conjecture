# Odd exponents at every sufficiently large smooth index

Let \(B_n^2\) be the reduced denominator of \(x([n]G)\) for \(G=(-3,9)\) on \(E:y^2=x^3-36x\). Fix a finite set \(S\) of odd rational primes, and write \(n=\prod_{q\in S}q^{e_q}\). Every sufficiently large such \(n\) has at least
\[
             \frac{1+\prod_{q\equiv1\pmod4}(2e_q+1)}{2}
\]
distinct primes of exact first-occurrence index \(n\) with odd first valuation. Put
\[
 T(n)=\prod_{q\equiv3\pmod4}(e_q+1)
       \prod_{q\equiv1\pmod4}(e_q+1)^2,\qquad
 H(n)=\frac{T(n)+\tau(n)}2.
\]
The complete denominator satisfies
\[
 \omega(\operatorname{sf}B_n)\ge H(n)-O_S(1),\qquad
 \operatorname{sf}B_n\gg_S(4n)^{H(n)}.
\]
The constants here are ineffective. In particular, for every fixed split prime \(q\), all sufficiently large \(q^k\) have at least \(k+1\) distinct first-occurrence primes of odd valuation, and \(\operatorname{sf}B_{q^k}\gg_q(4q^k)^{(k+1)(k+2)/2}\). For fixed inert \(q\), the lower bound is \(\operatorname{sf}B_{q^k}\gg_q(4q^k)^{k+1}\).

## A rational division-polynomial proof for fixed multipliers

For any odd positive \(m\), \(B_m=|f_m|\), where \(f_m=\psi_m(T)\) at \(T=(-1,\sqrt3)\) on \(y^2=x^3-4x\). Indeed \(f_m\) is a unit at 2 and 3, and a prime dividing its adjacent division polynomial at a good place would annihilate both \([m]T\) and \([m\pm1]T\) in reduction. The isomorphism \((x,y)\mapsto(3x,3\sqrt3 y)\) takes \(T\) to \(G\). Consequently \(\psi_m(G)=3^{(m^2-1)/2}f_m\), where \(\psi_m\) is now computed on \(E\). [Normalized all-index identity](abc_gaussian_quartic_odd_cofactors.md)

For odd \(a>1\), composition gives
\[
 \frac{B_{am}}{B_m}
   =|\psi_a([m]G)|\,B_m^{a^2-1}\,3^{-(a^2-1)/2}.
\]
The last two factors are rational squares. The division function \(\psi_a\) has a simple zero at each nonzero point of \(E[a]\) and a pole of even order \(a^2-1\) at the origin. The connected double cover of \(E\) defined by \(z^2=c\psi_a(Q)\) therefore has genus \(1+(a^2-1)/2\) for any nonzero twist \(c\). If only a fixed finite set of primes occurred to odd exponent in \(B_{am}/B_m\) at infinitely many \(m\), the points \([m]G\) would lift to a finite collection of these curves. They are distinct because \(G\) is nontorsion. Faltings's theorem gives a contradiction. In particular the squarefree part of \(B_{am}/B_m\) tends to infinity for every fixed odd \(a>1\).

Alternatively the ordinary primitive division polynomial \(F_a(X)\) is the monic polynomial whose distinct roots are the abscissas of points of exact order \(a\), counted up to sign. The monic definition avoids any convention on the leading coefficient. It belongs to \(\mathbb Q[X]\) and its degree is \(J_2(a)/2\), where \(J_2(a)=a^2\prod_{q\mid a}(1-q^{-2})\). On \(E\) it has \(J_2(a)\) simple zeros and an even pole at the origin, so its quadratic-twist covers have genus \(1+J_2(a)/2\). For fixed \(a\), outside any prescribed finite enlargement of the primes dividing \(6a\) and the denominators and discriminant of \(F_a\), the product \(F_a(x([m]G))\) has a prime of odd positive valuation at every sufficiently large \(m\). Negative valuations are even, and otherwise the same finite-twist argument applies.

At this prime, \([m]G\) reduces to exact order \(a\). Its distance from its prime-to-characteristic torsion lift has valuation \(v_p(F_a(x([m]G)))\) because the corresponding root is simple and the abscissa map is unramified there. Multiplication by \(a\) preserves this formal depth. Thus \(v_p(B_{am})\) is odd. Taking \(a=\operatorname{rad}(n)\), \(m=n/a\), with \(n\) supported on \(S\), forces the reduction order of \(G\) to be exactly \(n\). Indeed \(r/\gcd(r,m)=a\) forces the exponent of every \(q\mid a\) to be \(1+v_q(m)\), and every other exponent zero. As \(a\) varies in a finite list, this already proves one odd first occurrence at every sufficiently large \(S\)-smooth index.

For \(q\equiv3,5\pmod8\) there is also an effective statement for every odd \(m\). The exact congruence \(B_j\equiv(-1)^{(j-1)/2}j\pmod8\) gives \(B_{qm}/B_m\equiv5\pmod8\), hence an odd-exponent prime that is 13 modulo 24. This particular congruence gives 1 at \(q\equiv1,7\pmod8\).

## Gaussian division and exact annihilators

Work over \(K=\mathbb Q(i)\) with \(\mathcal O=\mathbb Z[i]\), the full endomorphism ring acting over \(K\). Write \(E[I]=\{T:[\gamma]T=O\text{ for every }\gamma\in I\}\). For an odd proper nonzero ideal \(I\), form the monic polynomial \(F_I(X)\) with roots the abscissas, up to sign, of points of exact annihilator \(I\). All Galois elements over \(K\) commute with the endomorphisms, proving \(F_I\in K[X]\). By complex uniformization \(E[I]\simeq\mathcal O/I\); exactly \(\phi_K(I)=| (\mathcal O/I)^\times |\) of its points have full annihilator \(I\). None is two-torsion, so \(F_I(x)\) on \(E\) has this many distinct simple zeros and a pole of even order at the origin. The connected covers \(z^2=cF_I(x)\) have genus \(1+\phi_K(I)/2\ge3\), since an odd Gaussian prime ideal has norm at least 5.

Let \(A\) range over ideals supported above \(S\), let \(I=\operatorname{rad}(A)\ne(1)\), and choose \((\beta)=A/I\). Consider \(Q=[\beta]G\). Only finitely many \(I\) occur. Exclude places above \(6\prod_{q\in S}q\) and those at which a coefficient or discriminant of one of these finitely many polynomials fails to be integral or a discriminant fails to be a unit. The group of elements of \(K^\times/K^{\times2}\) with even valuations outside these places is finite, by unique factorization and finiteness of the unit group. A bound on the odd-valuation support of \(F_I(x(Q))\) would therefore place \(Q\) on a finite set of twists of these fixed curves. Faltings proves this can happen for only finitely many \(Q\). There are finitely many \(A\) for each such \(Q\), since two Gaussian integers acting identically on \(G\) must be equal: a nonzero difference is an isogeny with finite kernel. All but finitely many \(A\) therefore have a place \(\mathfrak p\) outside the exclusions with odd valuation of \(F_I(x(Q))\).

At a pole the valuation is even because a nonintegral abscissa of a point on the integral good Weierstrass model has negative even valuation, and \(F_I\) is monic integral. Thus the odd valuation is positive. The reduction of \(Q\) equals that of a point \(T\) of exact annihilator \(I\). Indeed the relevant torsion has order prime to the residue characteristic and is unramified at this good place, and its distinct abscissas stay distinct after reduction. Work in the unramified torsion field when comparing the coordinates. The simple zero and the unramified abscissa map show that \(Q-T\) has formal depth \(v_{\mathfrak p}(F_I(x(Q)))\).

Writing \(J\) for the annihilator of the reduction of \(G\), the reduction of \([\beta]G\) has annihilator \(J/\gcd(J,(\beta))\). Its equality with \(I\) implies \(J=A\) prime by prime, because \((\beta)\) is supported on \(I\) and has exponent \(v_\lambda(A)-1\) there. Let \(d\) generate \(A\cap\mathbb Z\) positively, so \(d\) is the rational reduction order. For a generator \(\alpha\) of \(I\), both \(\alpha\) and \(d/(\alpha\beta)\) are integral and units at \(\mathfrak p\). Each acts isometrically on the formal group because its linear coefficient is a local unit and all higher coefficients are integral. Consequently \([d]G=[d/(\alpha\beta)][\alpha](Q-T)\) has the same odd depth.

The rational prime \(p\) under \(\mathfrak p\) is an odd-order prime for \(G\), since its rational reduction order is the same after extending the residue field. As \(G\) is a double modulo \(p\), the rational two-torsion descent makes \(-3,-9,3\) squares. Hence \(p\equiv1\pmod{12}\), so it splits in \(K\) and the local depth is exactly \(v_p(B_d)\). At any \(S\)-smooth multiple \(n\) of \(d\), multiplication by \(n/d\) leaves that depth unchanged because \(p\notin S\). A rational prime supplies at most a conjugate pair of annihilator ideals, as \(G\) is rational.

## Counting and prime sizes

If \(q\equiv3\pmod4\) has exponent \(e\) in \(n\), there is one Gaussian prime above it and \(e+1\) divisor choices. If \(q\equiv1\pmod4\), the two exponents can be chosen independently, giving \((e+1)^2\) choices. Conjugation fixes exactly the \(\tau(n)\) ideals \((d)\), \(d\mid n\), proving the count \(H(n)\). Ideally supported divisors with rational order exactly \(n\) have a forced exponent at each inert prime and \(2e+1\) choices with maximum \(e\) at each split pair. Exactly one such ideal is fixed by conjugation. As every ideal of exact rational order \(n\) has norm at least \(n\), all of them escape the finite set of exceptions for sufficiently large \(n\). This gives the exact-rank lower bound.

At a witnessing prime \(p\), all Gaussian endomorphisms are defined over \(\mathbb F_p\) and the orbit subgroup generated from \(G\) is isomorphic to \(\mathcal O/A\). Its order \(NA\) is odd. The rational two-torsion is independent and has order 4. Hasse's inequality therefore gives
\[
        p\ge(2\sqrt{NA}-1)^2
         =4NA\bigl(1-1/(2\sqrt{NA})\bigr)^2.
\]
For all nontrivial divisor classes outside the finite exceptional set, select one such prime. They are distinct and retain their odd exponent at \(n\). The involution \(A\mapsto(n)/A\) descends to conjugacy classes and pairs norms with product \(n^2\). Therefore \(\prod_{[A]\mid(n)}NA=n^{H(n)}\), with one factor per class. The product of the correction factors in Hasse's bound is bounded below uniformly in \(n\), because
\[
   \sum_{A\text{ supported above }S}(NA)^{-1/2}
    =\prod_{\lambda\mid\prod_{q\in S}q}
       (1-(N\lambda)^{-1/2})^{-1}<\infty.
\]
Discarding the fixed finite set removes at most a constant product of \(4NA\). This proves the asserted bound for \(\operatorname{sf}B_n\).
