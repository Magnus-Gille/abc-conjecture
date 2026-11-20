# Prime multipliers and primitive primes on the orbit of (1,2)

Use the signed slope of \(P_m\) on \(65y^2=x^4+4\), where \(m\) is odd. Put \(N_\sigma(m)=(s+\sigma t)^2+t^2\) for \(x(P_m)=s/t\) in lowest terms. The curve \(E_{65}:Y^2=X^3-4225X\) and its point \(Q=(-16,-252)\) represent the difference \(T=P-\iota P\). For good primes \(p\), put \(r_p=\operatorname{ord}_{E_{65}(\mathbf F_p)}(Q)\). The simultaneous-squarefulness construction supplies the exact seed-prime valuations, and the arithmetic of the difference is detailed in the companion note. [Forced-index calculations](abc_octic_forced_index.md)

## Prime multiplication preserves a growing range of tests

At a good odd prime, one of the two norms is divisible by \(p\) precisely when \(r_p\mid m\). Indeed \([m]T=2P_m-(0,0)\) vanishes on reduction exactly at a branch. For odd multiples of \(r_p\), the branch stays fixed. The valuation of the norm on this branch at \(m=r_pk\) equals its valuation at \(r_p\) plus \(2v_p(k)\). The seed primes have valuations \(1+2v_{13}(m)\) and \(1+2v_5(m)\) in the signed plus and minus norms, respectively. The prime 2 divides neither norm. To see the parity for all odd \(m\), choose \(\sqrt{65}\equiv1\pmod4\) in \(\mathbf Q_2\). The seed on \(E\) is in the formal group, with parameter \(-X/V=-2\). Odd multiplication preserves its parameter valuation, and translation by \((0,0)\) changes only the sign of \(V/X\).

For odd \(r_p\), the full rational two-torsion group gives \(4r_p\mid\#E_{65}(\mathbf F_p)\). Consequently, if a prime \(p\) first appears on replacing an odd index \(n\) by \(nq\) for an odd prime \(q\), then
\[
 q\mid r_p,\qquad p\ge(2\sqrt q-1)^2>q.
\]
Every norm valuation below this protection threshold is inherited, with the sole possible increase by two at \(p=q\). Thus, for fixed \(n,Y\), **every prime \(q>Y\)** gives exactly the same valuations as \(n\) at \(p\le Y\). The density of passing the signed small-prime cubefull tests among primes \(q\) equals the zero-or-one pass indicator at \(n\).

If the slope is normalized to be positive, the two signs can interchange. Let \(I_+,I_-\) be the signed pass indicators at \(n\). For either designated norm in positive coordinates the relative density of passing is \((I_++I_-)/2\) among primes in any reduced arithmetic progression. To prove this, subdivide the progression modulo four. On each class, \(P_{nq}=P+[(nq-1)/2]T\) lies in a fixed real component. Real uniformization of the identity component as a circle takes the non-torsion point \(2T\) to an irrational angle. Vinogradov's equidistribution theorem for irrational prime multiples, applied in the progression (or by finite additive Fourier expansion of its indicator), makes these points Haar equidistributed on their component. Both real components are invariant under elliptic negation, which changes the sign of \(V/X\); the zeros and poles are finite. Each sign of slope therefore has measure one half. For \(n=65,Y=17\), the indicators are \((0,1)\): the signed plus norm has valuation two at 17, and the only possible prime at most 17 in the signed minus norm is 5, to exponent three. This gives a literal half-density example.

## Primitive primes on each individual branch

Let \(V_\sigma(m)\) be the product, with multiplicities, of primes dividing \(N_\sigma(m)\) which first divide this norm at the positive odd index \(m\). Then \(V_\sigma(m)>1\) for every odd \(m\ge3\), and
\[
 \log V_\sigma(m)>\tfrac34m^2 \qquad(m\ge11\text{ odd}).
\]
For either norm at a cubeful index \(m\ge3\), every prime in this primitive part is an elliptic Wieferich prime for \(Q\) at rank exactly \(m\), and each is at least \((2\sqrt m-1)^2\).

Here is a proof with explicit constants. For odd \(m\), \(s\) is odd and \(t\) is even, and \(s^4+4t^4\) is 65 times an integer square. Its gcd with \(st\) is one, hence its gcd with \(260s^2t^2\) is exactly 65. The reduced coordinate \(x([m]Q)=-260s^2t^2/(s^4+4t^4)\) therefore gives
\[
 4\log H-\log65 \le h(x([m]Q))\le 4\log H+\log4,\qquad
 H^2/2\le N_\sigma(m)\le5H^2
\]
for \(H=\max(|s|,t)\). The height estimates in the companion note give \(\lambda=\hat h(Q)>1.348\) and
\[
 \lambda m^2-4.2 \le\log N_\sigma(m)\le\lambda m^2+6.8.
\]
For every nonprimitive prime of \(N_\sigma(m)\), its first index \(r<m\) divides \(m\), including \(r=1\) at the seed primes. Choose any prime \(\ell\mid m/r\). The valuation at \(m/\ell\) equals that at \(m\), except for a possible gain of two at \(m\) when \(p=\ell\). Hence
\[
 N_\sigma(m)/V_\sigma(m)\ \bigm|\ m^2\prod_{\ell\mid m,\ \ell\ {\rm prime}}N_\sigma(m/\ell).
\]
Since \(\sum_{j\ge1}(2j+1)^{-2}<\sum_{j\ge1}(4j(j+1))^{-1}=1/4\), this yields
\[
 \log V_\sigma(m)\ge \tfrac34\lambda m^2-4.2-
 \left(2+\frac{6.8}{\log3}\right)\log m.
\]
The right hand side is positive for \(m\ge5\) and exceeds \(3m^2/4\) for \(m\ge11\), by evaluating at the endpoint and differentiating. At \(m=3\), the first-appearance factors are \(2521^2\) and \((61\cdot157)^2\). At a primitive prime \(p\) the residue order is \(m\), as follows from branch stability at odd multiples. The branch valuation is twice the valuation of the local parameter of \([m]Q\), because the map from the quartic is branched of order two and multiplication by two preserves the parameter valuation. Thus a cubeful primitive prime satisfies \([m]Q=O\bmod p^2\), the asserted elliptic Wieferich condition.

This gives a necessary moving-prime condition at every candidate index. It is compatible with any finite collection of local congruences, and gives no general bound on how many primes satisfy the Wieferich condition.

There is also a consequence at the largest prime divisor of a possible index. Suppose \(m\) makes both signed norms squareful and the designated norm cubeful. Let \(L\) be its largest prime divisor, and write \(B=\operatorname{rad}(m)\). For every \(d\mid B/L\), the designated norm at index \(r=Ld\) has a primitive prime \(p\) of exact rank \(r\). The lower bound above gives \(p>r\ge L\), so \(p\nmid m\). Its valuation stays the same on passing from \(r\) to \(m\). It must have been at least four on first appearance, since it is even and the final norm is cubeful. Distinct divisors \(d\) give distinct primes through their ranks. Hence at least \(2^{\omega(m)-1}\) distinct primes outside \(m\) must already have exponent at least four on first appearance. The certified forced divisors have 1,512 distinct primes for the signed plus condition and 764 for minus. The respective lower bounds on the number of outside primes are thus \(2^{1511}\) and \(2^{763}\). Establishing even one simple primitive prime at an appropriate rank would exclude that candidate. [Forced-divisor certificates](abc_octic_forced_index.md)

An exhaustive exact check through \(10^7\) found 332,178 good primes congruent to one modulo four, including 221,539 for which \(Q\) has odd order. None of these odd-order primes satisfied \([r_p]Q=O\bmod p^2\). The program verifies an annihilating multiple at every prime, factors that multiple to compute the exact odd order when applicable, and applies the Jacobian group law modulo \(p^2\) at that order. [Reproducible C++ check](abc_octic_elliptic_wieferich.cpp)

## First-rank fourth powers on the same twist

The good primes in the next table all have valuation **four** at their first appearance, in the signed minus norm. Here the initial slope varies but the curve \(65y^2=x^4+4\) stays fixed.

| Seed \((s,t)\) | \(p\) | Exact first rank \(r_p\) | Auxiliary \(\ell\) proving \(Q\notin pE_{65}(\mathbf Q)\) |
|---|---:|---:|---:|
| \((7,8)\) | 41 | 13 | 149 |
| \((7,8)\) | 173 | 37 | 691 |
| \((7,8)\) | 257 | 65 | 1,093 |
| \((73,28)\) | 298,897 | 24,855 | |

If \(s^4+4t^4=65z^2\), the seed difference on the twist is
\[
 Q=\left(-\frac{4s^2t^2}{z^2},\frac{2st(s^4-4t^4)}{z^3}\right).
\]
The verifier checks the exact rank modulo \(p\) and directly evaluates \((x(P_{r_p})-1)^2+1\bmod p^5\). For the first row, the slope modulo \(41^5\) is 6,903,490. For each listed auxiliary prime \(\ell\), direct point counting gives \(\#E_{65}(\mathbf F_\ell)=4p\), and \([4]Q\ne O\bmod\ell\). Thus these first-rank fourth powers occur without divisibility of the rational seed difference by \(p\). They also occur at prime rank. A different primitive prime at the same index could still be simple. [Exact modular verifier](abc_octic_alternate_wieferich.py)
