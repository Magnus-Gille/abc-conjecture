# Large primes and first valuations at every odd elliptic rank

Let \(R=(-8,16)\) on \(E:y^2=x^3+16x^2+32x\), put \(h=\widehat h(R)>0\), and let \(B_r^2\) be the reduced denominator of \(x(rR)\). All ranks below are odd. Write \(e_p=v_p(B_r)\), and let \(\mathcal P_r\) be the primes where the reduced point has order exactly \(r\). These prime sets are disjoint as \(r\) varies. Put \(J_2(r)=r^2\prod_{q\mid r}(1-q^{-2})\). Define
\[
 F(v)=e^{-\gamma}\int_0^v\rho(u)\,du ,
\]
where \(\rho\) is the Dickman function. In particular \(F(v)=e^{-\gamma}v\) for \(0\le v\le1\), and \(F(v)\to1\) as \(v\to\infty\).

For every fixed \(a>\kappa\ge0\), put \(X=r^4/(\log r)^a\). Then
\[
 \liminf_{r\to\infty}
 \frac{\sum_{p\in\mathcal P_r,\;p>X\ \mathrm{or}\ e_p>(\log r)^\kappa} e_p\log p}
      {hJ_2(r)}
 \ \ge\ F((a-\kappa)/2).
 \tag{1}
\]
For \(\kappa=0\) the same lower bound \(F(a/2)\) holds for the smaller numerator
\[
 \sum_{p\in\mathcal P_r}e_p\log p-\sum_{p\in\mathcal P_r,\;p\le X}\log p .
 \tag{2}
\]
Both results hold for all prime divisors together upon replacing \(hJ_2(r)\) by \(hr^2\). Thus along a subsequence with \(P^+(B_r)\le X\), an asymptotic lower fraction \(F((a-\kappa)/2)\) of the exact-order mass comes from valuations exceeding \((\log r)^\kappa\). Every valuation counted at exact order is already the valuation at its first scalar index.

There is an unconditional bound for the size and valuation of **the same prime**. For \(t\ge1\) put \(L(t)=1+\log t\), and for fixed \(\eta>0\) put
\[
 W_\eta(t)=t L(t) [1+\log L(t)]^{1+\eta}.
\]
With the same \(X\) as above, the full mass of \(p\in\mathcal P_r\) satisfying \(pW_\eta(e_p)>X\), divided by \(hJ_2(r)\), has lower limit at least \(F(a/2)\). The assertion with all primes and normalizing factor \(hr^2\) also holds.

For a bound closer to \(r^4\), use \(K=\mathbb Q(\sqrt{-2})\) and put \(g(r)=\prod_{\lambda\mid(r)}(1-1/\operatorname N\lambda)\), over prime ideals of \(\mathcal O_K\). There exists \(c_\eta>0\) such that at every sufficiently large odd \(r\), primes with full CM annihilator \((r)\) satisfying
\[
          pW_\eta(e_p)>c_\eta r^4g(r)^2
 \tag{3}
\]
carry at least \(\tfrac12hr^2g(r)\) in log mass. In particular \(g(r)\gg1/\log\log(3r)\), and \(g(r)\to1\) along prime indices. For the simpler weight \(p e_p\), at least the same mass satisfies
\[
       p e_p> c\,\frac{r^4g(r)^2}{\log r\,\log\log r}
 \tag{4}
\]
for an absolute positive constant for this fixed curve and point. The constants in (3) and (4) may select different primes. These conclusions allow an exponent-one prime to supply all the mass, so they do not settle the growth of the repeated-prime contribution.

## The distribution of the complementary ideal

At a place above each denominator prime let \(I\mid(r)\) be the annihilator ideal of the reduction, and let \(d=\operatorname N((r)/I)\). Conjugation preserves its norm and the additive exponent of \(\mathcal O_K/I\). Over any conjugation-invariant collection of such ideals the exact rational denominator mass, counting exponents, is \(h\sum_I\Phi_K(I)+O(r^{o(1)})\). Here \(\Phi_K(I)=\#(\mathcal O_K/I)^\times\), and the error is uniform in the collection. The total mass is \(hr^2+O(1)\). The normalized weight \(\Phi_K(I)/r^2\) is the law of the annihilator of a uniform residue in \(\mathcal O_K/(r)\). Thus \(d\) is the norm of its gcd ideal with \((r)\). [Exact mass and normalization](abc_odd_rank_quartic_logarithm.md)

At each prime ideal \(\lambda\) above \(q\mid r\), take independent random variables \(V_\lambda\) with \(\Pr(V_\lambda\ge j)=(\operatorname N\lambda)^{-j}\) for \(j\ge0\). The gcd valuation has the law of \(\min(V_\lambda,v_\lambda(r))\). Write \(y=\log r\). The probability of any positive gcd valuation over \(q\mid r\), \(q>y\), is \(O(1/\log y)\), since there are at most \(\log r/\log y\) such rational prime factors and the sum of reciprocal ideal norms over a fixed \(q\) is at most \(2/q\). Outside this event, couple \(\log d\) below the sum
\[
 T_y=\sum_{2<q\le y}\sum_{\lambda\mid q} V_\lambda\log\operatorname N\lambda
\]
by adding the unused primes and removing truncations.

The law of \(T_y/\log y\) tends to the Dickman probability distribution. Indeed, for \(s>0\) the logarithm of its Laplace transform is
\[
 \sum_{2<q\le y}\sum_{\lambda\mid q}\sum_{k\ge1}
 \frac{e^{-s k\log\operatorname N\lambda/\log y}-1}
      {k(\operatorname N\lambda)^k}.
\]
The terms at inert primes, and all terms with \(k\ge2\), are \(O_s(1/\log y)\) by \(1-e^{-u}\le u\). The remaining sum is over the two ideals above each split prime. By Mertens' theorem for the classes \(1,3\bmod8\) its limit is \(\int_0^1(e^{-st}-1)\,dt/t\). One can first restrict to \(t\ge\delta\) and then bound the missing sum by \(O_s(\delta)\) using \(\sum_{q\le z}(\log q)/q\ll\log z\).

For completeness \(\rho(u)=1\) on \([0,1]\), vanishes for \(u<0\), and satisfies \(u\rho'(u)=-\rho(u-1)\) for \(u>1\). Integrating gives \(u\rho(u)=\int_{u-1}^u\rho(t)dt\) for \(u>0\), from which positivity, monotonicity and factorial decay follow successively on unit intervals. Its Laplace transform \(M(s)\) obeys \(M'(s)/M(s)=(e^{-s}-1)/s\), by the integral identity or integration by parts. Since \(M(s)\sim1/s\) as \(s\to\infty\) and \(\int_0^s(1-e^{-t})dt/t=\log s+\gamma+o(1)\), its value at zero is \(e^\gamma\). This identifies the limiting probability density as \(e^{-\gamma}\rho\). Consequently for every fixed \(b>0\),
\[
       \liminf_{r\to\infty}\Pr(d\le y^b)\ \ge\ F(b).
\]
This probabilistic inequality is sharp. For the product \(r\) of all odd split primes up to \(z\), one has \(\log r\sim z/2\). Truncating each geometric valuation at one changes its total expected log norm by \(O(\sum_q\log q/[q(q-1)])=O(1)\); the sum of the omitted inert contributions also has bounded expectation. Dividing by \(\log z\) leaves the stated limiting law. This sharpness concerns the gcd distribution.

The event that the uniform residue has additive order exactly \(r\) is decreasing in the independent valuations. At split \(q\mid r\) it requires at least one of the two valuations to vanish, and at inert \(q\mid r\) it requires the only one to vanish. Its probability is \(\prod_{q\mid r}(1-q^{-2})=J_2(r)/r^2\ge8/\pi^2\). The event \(d\le y^b\) is also decreasing. Product-measure positive association gives its conditional probability, given exact order, at least its unconditional probability. This association follows by induction from nonnegative covariance of two monotone functions of a single variable. The uniform errors in the mass formula are therefore negligible after conditioning, giving the same lower fraction \(F(b)\) of full mass for exact scalar order.

## Applying the norm sieve with multiplicities

For \(d\le D=y^b\) put \(m=\operatorname NI=r^2/d\). Every prime assigned to \(I\) is a norm of a CM Frobenius \(\pi\equiv1\bmod I\), hence at least \((\sqrt m-1)^2>m/4\). In particular it exceeds \(r\) for large \(r\). The elementary norm sieve bounds the count up to \(T\ge m/4\) in the range \(T\le O(r^4)\) by
\[
  \ll \frac{T}{m g(r)\,[1+\max(0,\log(T/m))]}.
 \tag{5}
\]
For bounded \(T/m\) use the lattice count. Otherwise sieve a box of side \(\asymp\sqrt{T/m}\); the cost of omitting sieve primes dividing \(r\) is at most \(1/g(r)\). The lower bound \(m/4\) exceeds the sieve cutoff throughout. The constants are absolute for the fixed field. The elementary ideal count gives \(\sum_{\operatorname N J\le D}\operatorname N J\ll D^2\), and ideal Mertens gives \(1/g(r)\ll\log\log(3r)\). [Uniform two-variable sieve with its local factors](abc_odd_rank_quartic_logarithm.md)

At \(T=X=r^4/y^a\) one has \(\log(T/m)\asymp\log r\). Multiplying (5) by \(\log X\) and summing over \(d\le D\) bounds the distinct log mass below \(X\) by \(O(XD^2/[r^2g(r)])\). Even after multiplying by \(y^\kappa\) this is \(o(r^2)\) if \(2b<a-\kappa\). Compare with the full mass proved above, then take \(b\uparrow(a-\kappa)/2\) by continuity. This gives (1). To get (2) subtract the distinct log mass just once and use nonnegativity of the excess away from these ideals.

For the weight \(W_\eta\), consider any cutoff \(Z\) between \(r^{7/2}\) and \(r^4\). The mass in one ideal for which \(pW_\eta(e_p)\le Z\) is \(O_\eta(Z/[m g(r)])\), uniformly in this range. Indeed \(W_\eta(e)\le u\) gives
\[
 e\ll_\eta\frac{u}{L(u)[1+\log L(u)]^{1+\eta}}.
\]
This follows by splitting at \(e=\sqrt u\). For \(p>r^3\) split into intervals \((Z/2^{j+1},Z/2^j]\), intersected with \((r^3,Z]\). Their distinct log mass is \(O(Z/[2^j m g(r)])\) by (5). The inverse valuation weight then gives the summable majorant
\[
 \frac{Z}{m g(r)}
 \sum_{j\ge0}\frac{O_\eta(1)}{(1+j)[1+\log(1+j)]^{1+\eta}} .
\]
For \(p\le r^3\), the dyadic intervals starting at \(m/4\) give from (5)
\[
   \sum_{p\le r^3\ \mathrm{assigned}}\frac{\log p}{p}
      \ll\frac{\log r\,\log\log r}{m g(r)}.
\]
Here the interval with scale \(2^i m/4\) costs \(O(\log r/[m g(r)(1+i)])\). Since \(Z/p\ge r^{1/2}\), inversion of the weight at these primes contributes at most \(O_\eta(Z/[m g(r)(\log\log r)^\eta])\). This proves the single-ideal bound. Taking \(Z=X\), summing at \(d\le D\), and sending \(b\uparrow a/2\) gives the asserted lower proportion.

For (3) take just \(I=(r)\). Its full rational mass is \(h r^2g(r)+O(r^{o(1)})\), and \(m=r^2\). Set \(Z=c_\eta r^4g(r)^2\) and choose a sufficiently small fixed \(c_\eta\). For large \(r\), \(Z\ge r^{7/2}\) because \(g(r)\gg1/\log\log(3r)\). The single-ideal upper bound removes at most one third of its main term if \(c_\eta\) is sufficiently small. The error in its full mass is \(o(r^2g(r))\). For (4) the same dyadic reciprocal estimate holds all the way to \(r^4\), so the full mass with \(pe_p\le Z\) is at most \(C Z\log r\log\log r/[r^2g(r)]\) in this ideal. Choosing the cutoff in (4) proves the claim.

## Consequence for the primitive triples

The primitive triples of height \(\log c_r=8hr^2+O(r)\) satisfy \(\log(c_r/\operatorname{rad}(a_rb_rc_r))\ge\log(B_r/\operatorname{rad}B_r)-O(1)\). If \(P^+(B_r)\le r^4/(\log r)^a\) along an infinite subsequence, (2) with all primes makes its lower limiting quality at least \(8/(8-F(a/2))\). The existence of a subsequence satisfying the smoothness condition remains open. [Primitive triples and radical comparison](abc_odd_rank_truncated_radical.md)

Smoothness of only the primes of exact order already has a consequence. If \(p\le X\) for every \(p\in\mathcal P_r\) on a subsequence, (2) gives a lower limiting quality at least \(8/[8-(8/\pi^2)F(a/2)]\), since \(J_2(r)/r^2\ge8/\pi^2\). Conversely, rational abc forces total excess \(\log(B_r/\operatorname{rad}B_r)=o(r^2)\) on this orbit. In that case (2) gives a lower limiting fraction at least \(F(a/2)\) of the exact-order mass at primes \(p>X\) of exponent one. Indeed every repeated prime contributes \(e_p\le2(e_p-1)\) times \(\log p\).
