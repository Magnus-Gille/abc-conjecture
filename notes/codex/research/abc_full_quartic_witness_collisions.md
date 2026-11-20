# Prime-index witnesses and the cost of losing their odd depths

Let \(d_n=\operatorname{sf}(B_n)\) on the odd quartic orbit of \(G=(-3,9)\) on \(y^2=x^3-36x\). For each odd prime \(q\), choose one odd-depth prime \(P(q)\mid B_q\), using the [square classification](abc_full_quartic_square_chabauty.md). The reduction order of \(G\) at \(P(q)\) is \(q\), so \(P\) is injective. The full rational two-torsion gives
\[
 P(q)\ge (2\sqrt q-1)^2>2q.
\]
All \(P(q)\) are \(1\bmod12\). If \(q\equiv3\bmod4\), multiplication by \(i\) is defined over \(\mathbf F_{P(q)}\) and the annihilator of a point of order \(q\) is the inert Gaussian ideal \((q)\). This gives the full subgroup \(E[q]\), whence \(P(q)\ge(2q-1)^2\). The first-depth computations below are independent of the choice of \(P\). [Rank and CM identities](abc_full_quartic_signature.md)

A lost odd depth at \(P(q)\) in passing from \(B_q\) to \(B_n\) with \(q\mid n\) requires \(P(q)\mid n\). Let \(q\le w(q)\le P(q)\) be any real weights, \(H(n)=n/\operatorname{rad}(n)\), and \(Z(n)=\prod_{qP(q)\mid n}w(q)\), with \(q\) odd prime. Distinctness of the witnesses gives
\[
                d_n/n\ \ge\ \frac{\prod_{q\mid n}(w(q)/q)}{H(n)\,Z(n)} .
\]
The cost \(H(n)Z(n)\) has uniformly bounded moments of every order \(s<1\) with \(s>0\). In fact \((H Z)^s(n)=\sum_{b\mid n}h_s(b)\) with nonnegative \(h_s\) and
\[
                    \sum_b h_s(b)b^{-1+\lambda}<\infty
\]
for some \(\lambda>0\) depending only on \(s\). This bound remains uniform in the choice of weights and witnesses.

To prove the stronger assertion, take \(0<2\lambda<1-s\) and put \(\sigma=1-\lambda\). The factors of \(H^s\) at \(q^a\) are \(q^{s\max(0,a-1)}\). They have a nonnegative divisor expansion. The corresponding local Dirichlet sum \(L_q\) satisfies \(L_q=1+O_s(q^{-2\sigma+s})\); hence the product converges. If one imposes \(q\mid n\), the local Dirichlet sum of the resulting expansion is \(q^{-\sigma}+L_q-1\ll_s q^{-\sigma}\). Positivity is preserved, since imposing \(q\mid n\) changes the local values only at exponent zero, from 1 to 0.

Expand \(Z^s\) as a product of \(1+(w(q)^s-1){\bf1}_{qP(q)\mid n}\). A finite selected set of edges \(q\to P(q)\) decomposes into vertex-disjoint paths because \(P\) is increasing along each edge and injective. Each vertex of a path imposes divisibility once. After accounting for the finite total Euler product of \(H^s\), a path \(q_0\to\cdots\to q_m\) costs at most
\[
                    C_s^{m+1}q_0^{-\sigma}\prod_{i=1}^m q_i^{s-\sigma}.
\]
There is at most one path of a given length from each starting prime, and \(q_i\ge 2^i q_0\). The sum of these bounds over all paths of positive length converges, since \(2\sigma-s>1\) and \(\sigma-s>0\). Summing over path sets is bounded by the exponential of this finite sum. All coefficients being nonnegative, finite expansions increase to the desired result. Averaging the expansion over integers gives the claimed moment bound.

## Size of a prime-index witness at split indices

Fix \(C>1\). Among split rational prime indices \(q\equiv1\bmod4\), those with \(P(q)\le Cq\) have relative prime density zero. Indeed at the split witness \(p=P(q)\) the ordinary Frobenius of this Gaussian CM curve is a Gaussian integer \(\pi\) with \(N\pi=p\), and \(\#E(\mathbf F_p)=N(\pi-1)\). One can also see the Frobenius is Gaussian since it commutes with the defined multiplication by \(i\), whose centralizer in the endomorphism algebra is \(\mathbf Q(i)\), and is integral. Since \(q\mid N(\pi-1)\), some Gaussian prime generator \(\varpi\) of norm \(q\) divides \(\pi-1\). Write \(\pi=1+\gamma\varpi\). Then \(0<N\gamma\le(\sqrt{Cq}+1)^2/q=O_C(1)\).

For each of the finitely many \(\gamma\), normalize the generator \(\varpi\) to be primary, absorbing its unit in \(\gamma\). Gaussian prime generators of this type are equidistributed in the unit classes modulo any fixed odd Gaussian modulus, by the prime ideal theorem in ray classes and the primary residue modulo \((1+i)^3\). For every prime ideal \(\mathfrak l\nmid2\gamma\), the nonzero residue \(-\gamma^{-1}\bmod\mathfrak l\) is excluded by primality of \(N(1+\gamma\varpi)\), except when that norm is the fixed underlying rational prime. The latter exception yields only finitely many \(\varpi\) for fixed \(\mathfrak l,\gamma\). Applying the Chinese remainder theorem to a finite list of degree-one places gives upper density at most \(\prod_{\mathfrak l}(1-1/(N\mathfrak l-1))\). This tends to zero as the list increases because the reciprocal norms of the degree-one Gaussian primes have divergent sum. Counting the two orientations over each \(q\) changes no zero-density assertion. Partial summation gives harmonic upper density zero as well.

## An elementary index count using the witness graph

For fixed \(K>0\) and every \(\epsilon>0\),
\[
       \#\{n\le X:n\ {\rm odd},\ d_n\le K n\}
                         \ll_{K,\epsilon} X/(\log X)^{1-\epsilon}.
\]
This is a separate analytic consequence of the positive-moment result. The [four-arm inverse sieve](abc_full_quartic_four_arm_inverse_sieve.md) gives a stronger count at this threshold using global multiplicity of small twists.

Choose arbitrary fixed \(C>1\). Put \(w(q)=q^2\) at inert indices. At split indices with \(P(q)\ge Cq\), put \(w(q)=Cq\); at the zero-density exceptional split indices use \(w(q)=q\). Fix \(0<s<1\). The multiplicative function \(f(n)=\prod_{q\mid n,\ q\ {\rm odd}}(w(q)/q)^{-s}\) lies in \([0,1]\), satisfies \(f(bm)\le f(m)\), and has prime average \(C^{-s}/2\). Specifically \(\sum_{q\le X}f(q)/q=(C^{-s}/2+o(1))\log\log X\), by the preceding zero-density result and convergence of \(\sum_q q^{-1-s}\).

Markov's inequality bounds the count by \(K^s\sum_{n\le X}f(n)(HZ)^s(n)\). Insert the positive divisor expansion. For \(b\le\sqrt X\), the elementary mean upper bound for \(0\le f\le1\) gives
\[
          \sum_{m\le X/b} f(bm)\ll (X/b)(\log X)^{-1+C^{-s}/2+o(1)} .
\]
For larger \(b\) use \(f\le1\), with a cost \(O_s(X^{1-\lambda/2})\) from the Dirichlet sum. This proves the asserted exponent on choosing \(C\) sufficiently large. No uniformity as \(C\to\infty\) is needed. [Elementary multiplicative mean bound](abc_full_quartic_small_kernel_counts.md)
