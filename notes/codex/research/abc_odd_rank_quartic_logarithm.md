# Prime divisors near the quartic scale at every odd scalar index

Let \(E':y^2=x^3+16x^2+32x\), \(R=(-8,16)\), \(h=\widehat h(R)>0\), and let \(B_r\) be the positive square root of the reduced abscissa denominator of \([r]R\). Take odd integers \(r\ge3\), without restriction on their prime factors. Write \(D_{\le X}(B)=\sum_{p\mid B,\ p\le X}\log p\) and \(D_{>X}(B)=\sum_{p\mid B,\ p>X}\log p\). Logs are natural. Then:

1. For every fixed \(\epsilon>0\), there exists \(c_\epsilon>0\) such that, at all sufficiently large odd \(r\), with \(X=r^4/(\log r)^\epsilon\),
   \[
   \log(B_r/\operatorname{rad}B_r)+D_{>X}(B_r)
     =\log B_r-D_{\le X}(B_r)\ \ge c_\epsilon h r^2.                      \tag{1}
   \]
2. For any function \(A(r)\to\infty\), at \(X(r)=r^4/(\log r)^{A(r)}\) one has \(D_{\le X(r)}(B_r)=o(r^2)\) unconditionally.

The family has \(B_r=\sqrt{Y_r}\), \(\log B_r=hr^2+O(1)\), \(\log c_r=8hr^2+O(1)\), and \(B_r\mid T_r\) with \(T_r\ll c_r\) and \(\operatorname{rad}(T_r)=\operatorname{rad}(a_rb_rc_r)\). Thus a subsequence with \(P^+(B_r)\le r^4/(\log r)^\epsilon\) would give a fixed quality gap above one on that subsequence. Conversely, if \(q_r\le1+o(1)\) along some sequence of odd indices, (1) forces \(D_{>X}(B_r)\ge(c_\epsilon-o(1))hr^2\) along that sequence. If \(P^+(B_r)\le r^4/(\log r)^{A(r)}\) with \(A(r)\to\infty\) on a subsequence, the second assertion gives \(q_r\ge8/7-o(1)\) there. These are implications; no such smoothness or quality hypothesis enters (1) or assertion 2. [Coordinates and height](abc_octic_mixed_skew_denominator.md) · [Whole-triple comparison](abc_octic_whole_radical_tail.md)

## Distribution of exact annihilator ideals

Put \(K=\mathbb Q(\sqrt{-2})\), \(\mathcal O=\mathbb Z[\sqrt{-2}]\), and let \(F(I)\) denote the *full initial logarithmic denominator mass over places* of exact annihilator \(I\) for the reduction of \(R\). Each place is counted at the first formal depth of a generator of \(I\), before any additional depth at scalar index \(r\). All primes of odd \(B_r\) are split in \(K\). Indeed a point of odd reduction order is a double, the duplication abscissa on \(E'\) is a square, and \(x(R)=-8\). The exact packet formula, for odd \(I\), gives
\[
 F(I)=2h\Phi_K(I)+O(\tau_K(I)\log(2\operatorname NI)),\quad
 \Phi_K(I)=\operatorname NI\prod_{\lambda\mid I}(1-1/\operatorname N\lambda).
\]
For \(I\mid(r)\) the total errors are \(r^{o(1)}\). The increase in formal depths beyond the first ones contributes at most \(2\log r\) over all places, because the multiplier from \(I=(\gamma)\) to \((r)\) has differential dividing \(r\). The two conjugate places over a rational prime of \(B_r\) have conjugate annihilator ideals of the same norm and equal depths. Consequently, for any set \(\mathcal D\) of complementary norms, the full rational logarithmic mass at those primes is
\[
 \sum_{\substack{p\mid B_r\\\operatorname N((r)/I_p)\in\mathcal D}}
       v_p(B_r)\log p
 =h\!\sum_{\substack{I\mid(r)\\\operatorname N((r)/I)\in\mathcal D}}\!\Phi_K(I)
       +O(r^{o(1)}),                                                          \tag{2}
\]
uniformly in the set. Here \(I_p\) is the annihilator at either place above \(p\). [Exact ideal mass and formal lifting](abc_octic_mixed_cm_prime_mass.md)

Choose \(a\) uniformly in \(\mathcal O/(r)\), and write \(G=\operatorname N((a)+(r))\) for the norm of the ideal gcd. The law of \(G\) is exactly the normalized main term in (2). Indeed at \(\lambda^e\parallel (r)\) the gcd exponent has probabilities \(\Pr(v\ge j)=(\operatorname N\lambda)^{-j}\) for \(1\le j\le e\), independently across primes by CRT. Equivalently the annihilator \(I\) of the residue \(a\) under multiplication occurs with probability \(\Phi_K(I)/r^2\), and its complementary ideal is this gcd.

Let \(y=\log r\). Two uniform facts about this distribution suffice. First,
\[
 \mathbb E\log G\le(1+o(1))\log y.                                           \tag{3}
\]
For prime ideals over rational \(q\le y\) this follows from the prime ideal Mertens estimate \(\sum_{q\le y,\ \lambda\mid q}\log\operatorname N\lambda/(\operatorname N\lambda-1)=(1+o(1))\log y\). Equivalently one may sum over the split rational primes \(q\equiv1,3\bmod8\) with multiplicity two; the inert-prime terms are absolutely summable. For \(q>y\) dividing \(r\), the contribution is \(O(\sum_{q\mid r,q>y}\log q/q)\le O(\log r/y)=O(1)\).

Second, for each fixed \(b>0\),
\[
 \liminf_{r\to\infty,\ r\ {\rm odd}}\Pr(G\le y^b)\gg\min(b,1).               \tag{4}
\]
Set \(\theta=\min(b/4,1/2)\), and require the gcd to avoid all prime ideals over \(q>y^\theta\). Its probability is \(\prod_{q\mid r,\ q>y^\theta}\prod_{\lambda\mid q}(1-1/\operatorname N\lambda)\). Up to \(y\), the product over *all* rational primes in this interval is a lower bound and is asymptotic to \(\theta\) by Mertens in \(K\). Beyond \(y\) the sum of the reciprocals of the possible prime ideal norms is \(O(1/\log y)\), since at most \(\log r/\log y\) such rational primes divide \(r\). Conditional on avoidance, CRT leaves the smaller-prime distribution unchanged. Its expected log gcd is at most \((\theta+o(1))\log y\), so Markov leaves at least half the conditional mass at \(G\le y^b\). This proves (4).

## Uniform sieve for a fixed annihilator

Fix constants \(a,b>0\). In this section \(X=r^4/(\log r)^a\), \(I=(\gamma)\mid(r)\), \(d=\operatorname N((r)/I)\le D=(\log r)^b\). Write \(m=\operatorname NI=r^2/d\). A rational prime assigned to \(I\) is the norm of a Frobenius \(\pi\) with \(\pi\equiv1\bmod I\). This uses good split reduction and the CM action rational at the chosen place. The prime norms \(p\le X\) are among the values
\[
  \operatorname N(1+\gamma(u+v\sqrt{-2})),\qquad |u|,|v|\le B,
  \qquad B\asymp\sqrt{X/m}.
\]
Enlarge the box by a fixed factor and round its radius up if necessary. Uniformly here \(B=r(\log r)^{O_{a,b}(1)}\). Distinct rational primes require distinct pairs; an upper bound may count pairs with multiplicity.

Sieve this box by odd primes \(q\nmid r\). Multiplication by \(\gamma\) is a bijection modulo \(q\) since \(I\mid(r)\). Thus the number \(\nu(q)\) of norm-zero classes in the two-variable box modulo \(q\) is \(2q-1\) at split \(q\) and one at inert \(q\). For squarefree \(k\) supported on these sieving primes, CRT and an elementary box count give the expected fraction \(\prod_{q\mid k}\nu(q)/q^2\) of all pairs with error \(O(2^{\omega(k)}(B+k))\), uniformly in \(I,r\). Including all odd primes gives a sieve density product \(\asymp1/\log z\); the inverse inflation from omitting all \(q\mid r\) is at most
\[
 \prod_{q\mid r}\prod_{\lambda\mid q}(1-1/\operatorname N\lambda)^{-1}
 \ll\log\log(3r).
\]
The local factors here are exact, since at split \(q\) the retained density is \((1-1/q)^2\) and at inert \(q\) it is \(1-1/q^2\). The upper bound follows from ideal Mertens up to \(y=\log r\) and the preceding tail estimate above \(y\).

Apply the dimension-one upper-bound sieve at level \(B^{1/2}\) with cutoff \(z=B^{1/10}\). Its dimension constant is uniform: deleting sieving primes decreases every inverse local product on an interval. The sieve main term is \(O(B^2\log\log(3r)/\log B)\). The summed box errors to the level, even with a fixed divisor-power weight, are \(O(B^{3/2+o(1)})\), absorbed into the main bound. Every prime in question survives the sieve because \(p\ge(\sqrt m-1)^2\gg r^2/(\log r)^b\), from \(0\ne\pi-1\in I\), and this exceeds \(z\). Since \(\log X/\log B\) is bounded uniformly in these ranges, the rational sum of log prime divisors of \(B_r\) below \(X\) assigned to this ideal is
\[
 \ll (X/m)\log\log(3r).
\]
This is an upper bound on distinct primes; it does not bound their valuations. [Lattice sieve with its local densities and error terms](abc_octic_dyadic_fermat_audit.md)

Every complementary ideal of norm at most \(D\) is principal, and lattice point counting gives \(O(D)\) such ideals, with sum of norms \(O(D^2)\). Therefore
\[
 \sum_{\substack{p\mid B_r,\ p\le X\\\operatorname N((r)/I_p)\le D}}\log p
 \ll \frac{X}{r^2}D^2\log\log(3r)
 =o(r^2)\qquad(2b<a).                                                    \tag{5}
\]
This summation avoids the total number of divisors of \((r)\).

## Deducing the radical estimates

For (1), take \(a=\epsilon\) and \(b=\epsilon/3\). Equations (2) and (4) give a positive fraction \(\gg\min(\epsilon,1)\) of full logarithmic mass at complementary norms at most \((\log r)^b\). Their small-prime radical is \(o(r^2)\) by (5). Every other prime makes a nonnegative contribution to \(\log B_r-D_{\le X}(B_r)\). In particular \(c_\epsilon\) can be taken as a fixed absolute constant times \(\min(\epsilon,1)\).

For assertion 2 fix any \(b>1\). Equations (2), (3) and Markov bound the full mass at larger complementary norms by \((1+o(1))hr^2/b\). For large \(r\) one has \(A(r)\ge3b\), so the radical below the claimed cutoff at smaller complementary norms is at most the bound (5) with the fixed exponent \(a=3b\). Taking the limsup and then increasing \(b\) proves assertion 2.

## An unconditional lower bound using the actual prime multiplicities

Write \(e_p=v_p(B_r)\). For every fixed \(\epsilon>0\), at every sufficiently large odd \(r\) a positive fraction of \(\log B_r\) is contributed by prime powers satisfying
\[
                  p e_p > \frac{r^4}{(\log r)^{1+\epsilon}}.
\]
This statement counts the full contribution \(e_p\log p\) and requires no hypothesis about abc or smoothness.

Indeed set \(X=r^4/(\log r)^{1+\epsilon}\), \(D=(\log r)^{\epsilon/4}\). Ideals with \(d=\operatorname N((r)/I)\le D\) have a fixed positive fraction of the total weight by (2) and (4). Put \(m=r^2/d\). For one such ideal the sum of \(e_p\log p\) over primes with \(p e_p\le X\) is bounded above by \(X\sum_{p\le X}\log p/p\), restricting the sum to primes assigned to that ideal. Each such prime is at least \(m/4\) for large \(r\). On the intervals of scale \(T=2^i m/4\) up to \(X\), the same box sieve gives
\[
 \#\{\text{assigned primes}\le 2T\}\ll
 \frac{T}{m}\min\left(1,\frac{\log\log(3r)}{1+i}\right).
\]
For bounded \(T/m\) use the direct lattice count. Otherwise use a box of radius comparable to \(\sqrt{T/m}\) and the uniform upper-bound sieve above. The sieve error is absorbed as the radius grows, uniformly in \(r,I\), and every actual prime exceeds the sieve cutoff since \(m\ge r^2/D\). The number of intervals is \(O(\log r)\). On each interval \(\log p/p\ll\log r/T\), whence the reciprocal sum is \(O(m^{-1}\log r(\log\log(3r))^2)\) by harmonic summation. Summing over all \(d\le D\) gives the full log mass in question at most
\[
 O\left(\frac{X D^2}{r^2}\log r\,(\log\log(3r))^2\right)=o(r^2).
\]
The rest of the positive fraction has \(p e_p>X\), as claimed.

## When a constant multiple of the quartic scale suffices

Write \(g(r)=\Phi_K((r))/r^2\). On any sequence with \(g(r)\ge\xi>0\), the single packet \(I=(r)\) has full rational mass at least \((\xi-o(1))h r^2\). The uniform sieve just proved also applies at \(X=c r^4\) for each fixed \(0<c<1\): the box has radius comparable to \(\sqrt c\,r\), and the exact omission multiplier is \(1/g(r)\). Therefore the distinct prime mass of this packet at \(p\le c r^4\) has limsup after dividing by \(r^2\) at most \(C c/\xi\), with \(C\) independent of \(c,\xi\). Choosing \(0<c<h\xi^2/(2C)\) gives \(\log B_r-D_{\le c r^4}(B_r)\ge h\xi r^2/2\) at all sufficiently large indices in the sequence. This includes sequences with a bounded number of distinct prime factors.

The same argument cannot capture a positive fraction by keeping complementary norms bounded at all odd indices. Take \(r\) to be the product of odd split primes up to \(y\). For each fixed \(D\), a gcd norm at most \(D\) must avoid both prime ideals above each \(D<q\le y\) split in \(K\). Thus \(\Pr(G\le D)\le\prod_{D<q\le y,\ q\ {\rm split}}(1-1/q)^2\to0\). Every packet has \(\Phi_K(I)\le\Phi_K((r))=o(r^2)\) on this sequence. This identifies a limitation of using the mass formula and the sieve capacity at each ideal to obtain a fixed proportion at a fixed quartic cutoff. Whether a constant quartic cutoff gives (1) for every odd index remains open here.
