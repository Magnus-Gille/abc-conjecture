# A quartic cutoff on average over all odd indices

For the fixed point \(R=(-8,16)\) on \(E':y^2=x^3+16x^2+32x\), let \(B_r\) be its scalar abscissa denominator square root at odd index \(r\), and put \(D_{\le X}(B_r)=\sum_{p\mid B_r,\ p\le X}\log p\). For each \(0<\eta<1/2\) and \(0<c<1/2\),
\[
 \limsup_{M\to\infty}\frac1M\sum_{M\le r\le2M,\ r\ {\rm odd}}
     \frac{D_{\le c r^4}(B_r)}{r^2}\ll_\eta c^{1/2-\eta}.                       \tag{1}
\]
Consequently for any prescribed cutoff \(X_r=o(r^4)\) the dyadic mean with cutoff \(X_r\) tends to zero. For each positive threshold the set of indices exceeding it has density zero, by Markov's inequality and summation over dyadic intervals. There is a single exceptional set of density zero, allowed to depend on the prescribed function \(X_r\), outside which \(D_{\le X_r}(B_r)/r^2\to0\). In detail, choose growing dyadic block thresholds \(1/j\), passing to the next threshold only once every subsequent dyadic block has proportion at most \(1/j\) exceeding it. The union of the exceptional portions has vanishing relative size in each block, hence density zero even at intermediate endpoints.

Outside this exceptional set, every subsequence satisfying \(P^+(B_r)\le X_r\) has \(q_r\ge8/7-o(1)\). Indeed \(\log B_r=hr^2+O(1)\), \(\log c_r=8hr^2+O(1)\), and \(B_r\mid T_r\ll c_r\), where \(h=\widehat h(R)>0\) and \(\operatorname{rad}(T_r)\) is the triple radical. This implication neither assumes nor proves a density estimate for the set of smooth indices itself. [Odd-index packet masses, sieve and height comparisons](abc_odd_rank_quartic_logarithm.md)

## Averaging the complementary ideal

Use \(K=\mathbb Q(\sqrt{-2})\), \(\mathcal O=\mathbb Z[\sqrt{-2}]\) and \(g(r)=\Phi_K((r))/r^2\). An exact annihilator \(I\mid(r)\) has complementary ideal \(\beta=(r)/I\) of norm \(d\). Conditional on \(r\), give \(I\) weight \(\Phi_K(I)/r^2\). Then \(d\) has the law of the norm of the gcd of a uniform residue with \((r)\). For fixed \(0<\alpha<1\) the conditional moment \(\mathbb E(d^\alpha\mid r)\) is at most \(\prod_{q\mid r}(1+b_q)\) where \(0\le b_q\ll_\alpha q^{\alpha-1}\). Indeed the factor for a prime ideal of norm \(Q\) is at most \(1+(Q^\alpha-1)/(Q-Q^\alpha)\) by the geometric valuation tail, with at most two prime ideals per rational \(q\). Expanding this nonnegative product gives
\[
 M^{-1}\sum_{r\le2M}\prod_{q\mid r}(1+b_q)
 \le 2\prod_q(1+b_q/q)\ll_\alpha1.
\]
The same calculation bounds the mean of \(g(r)^{-1}\), whose local coefficients are \(O(1/q)\). The exact packet mass formula therefore bounds the mean of the normalized *full* log prime mass at \(d>D\) by \(O_\alpha(D^{-\alpha})+o_M(1)\). The aggregate errors from that formula are \(r^{o(1)}\) before normalizing, uniformly in the selected set of ideals.

For \(d\le D\), keep \(c,D\) fixed while taking \(M\to\infty\). The uniform two-variable norm sieve bounds the distinct prime logarithm below \(c r^4\) for a single \(I\) by \(C c r^2 d/g(r)\). The scale of the box is comparable to \(r\sqrt{cd}\), whose logarithm is uniformly asymptotic to \(\log r\) for these fixed parameters. The implied absolute constant \(C\) is independent of \(c,D\); the threshold for \(r\) can depend on both. This is the inequality in the linked proof before it upper bounds the omission multiplier \(g(r)^{-1}\).

Let \(e_\beta\) be the least positive rational integer in \(\beta\). The ideal occurs only when \(e_\beta\mid r\). On writing \(r=e_\beta k\), \(1/g(r)\le1/(g(e_\beta)g(k))\), so the mean of \(\mathbf1_{e_\beta\mid r}/g(r)\) is \(O(1/(e_\beta g(e_\beta)))\). Here \(e_\beta\le d\le D\), and ideal Mertens gives \(1/g(e_\beta)\ll\log\log(3D)\).

Choose a generator \(m(u+v\sqrt{-2})\) of \(\beta\), with \(m>0\), \(\gcd(u,v)=1\), and put \(z=u+v\sqrt{-2}\). Since \(k/z=k\bar z/\operatorname N z\), a rational integer \(k\) is divisible by \(z\) in \(\mathcal O\) exactly when \(\operatorname N z\mid k\). Hence \(e_\beta=m\operatorname N z\) and \(d/e_\beta=m\). Lattice counting bounds the number of possible \(z\) up to sign by \(O(D/m^2)\) when \(m\le\sqrt D\). Therefore \(\sum_{\operatorname N\beta\le D} d/e_\beta\ll D\log(2D)\).

The limsup of the normalized mean of the small radical is now bounded by
\[
 O\big(cD\log(2D)\log\log(3D)\big)+O_\alpha(D^{-\alpha}).
\]
For each fixed \(c\), set \(D=c^{-1/2}\), then take the limsup in \(M\). Choosing \(\alpha\) sufficiently close to one proves (1). For variable \(X_r=o(r^4)\), first bound by \(c r^4\) eventually for each fixed \(c\), then send \(c\downarrow0\).

## Deep first valuations forced by a smooth index

The single ideal \(I=(r)\) already forces a distinct prime of large initial depth at each sufficiently large odd \(r\) with \(P^+(B_r)\le r^4/(\log r)^\epsilon\), for fixed \(\epsilon>0\). Its full rational mass is \((h+o(1))r^2 g(r)\), and its entire distinct prime mass is \(O(r^2/((\log r)^\epsilon g(r)))\). Thus some prime has first formal depth
\[
 d_p\gg (\log r)^\epsilon g(r)^2
       \gg (\log r)^\epsilon/(\log\log r)^2 .
\]
It has exact reduction order \(r\), is at least \((r-1)^2\), and has all of \(E'[r]\) rational in its residue field. Distinct indices force distinct primes.

Outside a further set of density zero, every such smooth index forces at least \((\log\log r)^{(\log3)/2-o(1)}\) distinct primes of initial depth at least \((\log r)^{\epsilon-o(1)}\). In a dyadic block \([M,2M]\) put \(z=\exp(\log\log M/(\log\log\log M)^2)\). For all but \(o(M)\) odd indices the number of split \(q\le z\) dividing \(r\) is \(k=(1/2+o(1))\log\log\log M\). The mean is given by Mertens in progressions and the variance is \(O(\log\log z+z^2/M)\) by counting multiples of individual primes and pairs among the odd integers. The log product of these primes is \(o(\log\log M)\) for all but \(o(M)\) indices by Markov, since its mean is \(O(\log z)\). For instance one can bound it by \(\log\log M/\log\log\log M\) outside a relative \(o(1)\) set.

At each of these \(k\) primes, choose to omit from \((r)\) neither prime ideal, one prime ideal, or its conjugate once. The resulting \(3^k\) ideals have rational additive exponent exactly \(r\), since above each rational prime at least one ideal retains its full exponent. Every complementary norm satisfies \(d=(\log r)^{o(1)}\). The exact full mass is \(\gg r^2 g(r)/d\), and the distinct-prime sieve bound under smoothness is \(O(r^2d/((\log r)^\epsilon g(r)))\). Uniformity follows by bounding \(d\le (\log r)^b\) with any fixed \(b>0\) eventually. Each ideal forces a prime of at least their ratio in valuation. Its lower bound \((r/\sqrt d-1)^2>r\) ensures that passing from the ideal generator to the first rational index introduces no extra valuation. A prime can be selected by at most two conjugate ideals. This proves the claim.

Infinitude of unconditional witnesses \(p>r^4/(\log r)^\epsilon\) remains undecided. At the least index \(r=\operatorname{ord}_p(R)\), such a prime must have \(r\ll p^{1/4}(\log p)^{\epsilon/4}\). In \([X,2X]\) the number of primes in this range is \(O(X^{3/4}(\log X)^{3\epsilon/4-1})\), by summing \(\log B_j\ll j^2\) up to the resulting order bound and dividing by \(\log X\). This is a set of density zero among primes; a nonempty Frobenius condition in a fixed finite Galois field has positive density and cannot force every prime in it to witness the desired inequality. This does not rule out methods that vary the field or control a thin subset of a Frobenius class.
