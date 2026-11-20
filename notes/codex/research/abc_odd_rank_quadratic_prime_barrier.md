# Which primes carry the denominator at typical odd indices?

Let \(R=(-8,16)\) on \(E:y^2=x^3+16x^2+32x\). For odd \(r>0\), write \(B_r^2\) for the reduced denominator of \(x([r]R)\). Then \(\log B_r=hr^2+O(1)\) with \(h=\widehat h(R)>0\). For any positive \(L(t)=o(\log t)\),
\[
 \frac1M\sum_{\substack{M\le r\le2M\\r\ {\rm odd}}}
 \frac1{r^2}\sum_{\substack{p\mid B_r\\p\le r^2 L(r)}}v_p(B_r)\log p\longrightarrow0 .
\]
The analogous statement holds for prime indices, replacing \(1/M\) by \((\log M)/M\). Thus for every fixed \(\eta>0\), the proportion of indices where these primes carry more than \(\eta\log B_r\) tends to zero. The conclusion counts all multiplicities. One may take \(L(r)=\log r/\log\log r\). This leaves a gap to the [quartic abc criterion](abc_odd_rank_quartic_logarithm.md).

## Sieve in the integer index

For \(A\ge2\), integer coefficients \(|a|,b\ll\sqrt A\), \(b\ge1\), put \(D=a^2+2b^2\) and \(f(k)=(1+ak)^2+2b^2k^2\). For \(A\ll\log M\), the number of \(k\in[M,2M]\) at which at least one such polynomial is prime is \(O(AM/\log M)\). If \(k\) must itself be prime, the number is \(O(AM/(\log M)^2)\). All constants may depend on the absolute coefficient bound.

At odd split primes \(q\nmid bD\) of \(K=\mathbb Q(\sqrt{-2})\) the polynomial has two distinct roots, since its discriminant is \(-8b^2\). At inert primes outside \(bD\) it has none. Discard \(2,3\). At primes dividing \(bD\) discard the potential roots. In the prime-index sieve, also remove \(k=0\bmod q\) at every \(q\ge5\), including those dividing \(bD\). This residue differs from each polynomial root since \(f(0)=1\).

Write \(g(n)=\prod_{q\mid n}(1-1/q)^{-2}\). The cost from each omitted pair of roots is \((1-2/q)^{-1}\) in the first sieve and \((1-1/q)/(1-3/q)\) in the second. Each is \((1-1/q)^{-2}(1+O(q^{-2}))\), hence the total cost is \(O(g(b)g(D))\). Mertens' theorem for the split residue classes \(1,3\bmod8\) gives sieve dimensions \(j=1,2\) respectively. The retained density product to \(z\) is \(\ll g(b)g(D)/(\log z)^j\), and the inverse local-product bound on subintervals is uniform since deleting polynomial roots decreases it. Apply the ordinary upper-bound sieve with level \(M^{1/2}\), \(z=M^{1/100}\). The counting error for a squarefree divisor \(d\) is bounded by the number of forbidden classes, at most \(3^{\omega(d)}\). Its sum to the level, even with a fixed divisor-power weight, is \(M^{1/2+o(1)}\). The primes being counted exceed \(z\), since \(f(k)\ge2k^2\). This bounds the count at each pair by \(O(Mg(b)g(D)/(\log M)^j)\).

Summing the weights costs \(O(A)\) by Cauchy–Schwarz. Indeed write \(g(n)^2=\sum_{d\mid n}h_d\), supported on squarefree \(d\) with multiplicative coefficients \(h_q=(1-1/q)^{-4}-1=O(1/q)\). The sum of \(g(b)^2\) over all pairs is \(O(A)\) since \(\sum h_d/d<\infty\). For the other square moment, if \(d\mid D\), the element \(a+b\sqrt{-2}\) belongs to at least one of at most \(2^{\omega(d)}\) ideals of norm at least \(d\), choosing a prime ideal over each \(q\mid d\). In this principal ring an ideal of norm \(m\) contains \(O(A/m)\) nonzero elements of norm \(\ll A\) for \(m\ll A\), and none when \(m\) exceeds the norm bound. The second square moment is \(O(A\sum 2^{\omega(d)}h_d/d)=O(A)\). This proves both counts.

## Contributions from the possible annihilators

At \(p\mid B_r\) choose a place over \(p\) in \(K\). The annihilator \(I\) of \(R\) modulo this place divides \((r)\). Put \(J=(r)/I\). The Frobenius element \(\pi\) has norm \(p\) and satisfies \(\pi-1\in I\). At each \(I\) the sum of initial depths over places weighted by \(\log p\) is \(O(\operatorname NI)\). Subsequent increases summed over all ideals contribute only \(O(\log r)\). For odd-norm \(I\), the initial mass is \(2h\Phi_K(I)+O(\tau_K(I)\log(2\operatorname NI))\), with \(\Phi_K\) counting units in the residue ring. [Height and reduction formulas](abc_octic_mixed_cm_prime_mass.md)

Fix \(T\). For \(J\) of norm at most \(T\), put \(c=\min(J\cap\mathbb Z_{>0})\). Then \(c\mid r\) and \(I=(r/c)((c)/J)\subseteq(r/c)\). Hence \(p=f(k)\) for \(k=r/c\), choosing \(b\ge1\) by conjugation, since a rational Frobenius would have square norm. If \(p\le r^2 L(r)\) then \(|a|,b\ll_c\sqrt{1+L(r)}\). The sieve on \(k\in[M/c,2M/c]\) gives \(o(M)\) possibilities at this fixed \(J\), since \(1+\sup_{M\le t\le2M}L(t)=o(\log M)\). There are finitely many \(J\) of norm at most \(T\). The entire normalized mass is bounded at each exceptional index by the height formula.

For \(\operatorname NJ>T\), each \(J\) contributes normalized initial mass \(O(1/\operatorname NJ)\) whenever \(J\mid(r)\). There are at most \(2M/c\) such indices in the interval and \(c\ge\sqrt{\operatorname NJ}\) since \((c)\subseteq J\). Their total mean is \(O(\sum_{\operatorname NJ>T}(\operatorname NJ)^{-3/2})=O(T^{-1/2})\), using the \(O(t)\) count of ideals of norm at most \(t\). Lifting contributes \(o(1)\) to the normalized mean. Let \(T\) tend to infinity.

At prime indices the proper nonunit divisors of \((r)\) have norm \(r\) and number at most two, so their initial mass is \(O(r)\). For \(I=(r)\) use the prime-index sieve with \(k=r\), giving \(o(M/\log M)\) exceptions. This proves the second claim. Dyadic decomposition gives the corresponding density statements on initial intervals.

## An explicit family at a constant multiple of the logarithmic scale

For \(T\ge3\) take \(r=1+2\prod_{q\le T,\ q\ {\rm split}}q\prod_{q\le\sqrt T,\ q\ {\rm inert}}q\), with odd rational primes in both products. Then \(\log r=(1/2+o(1))T\) by the prime number theorem for the split classes. At an exact annihilator \((r)\) write \(p=|1+r\alpha|^2\), \(\alpha=a+b\sqrt{-2}\), \(b\ge1\). If \(p\le r^2(\sqrt T-2)^2\) for large \(T\), then \(2\le|1+\alpha|^2\le T\). Any prime divisor \(q\) of this integer divides \(r-1\). A split divisor is at most \(T\), and an inert divisor appears to order at least two, hence is at most \(\sqrt T\). Consequently \(q\mid|1+r\alpha|^2\), although \(q\le T<p\) since \(p\ge2r^2\). This excludes all such primes below the cutoff.

Moreover \(\Phi_K((r))/r^2\to1\). Every split prime factor of \(r\) exceeds \(T\), so their reciprocal sum is \(O(\log r/(T\log T))=o(1)\). Inert factors exceed \(\sqrt T\), and their local loss is bounded by \(O(\sum_{q>\sqrt T}q^{-2})=o(1)\). By the exact mass formula, dividing by two for conjugate places, primes of exact annihilator \((r)\) contribute \((h-o(1))r^2\). Thus almost the entire denominator on this sequence comes from primes above \(r^2(\sqrt T-2)^2=(2-o(1))r^2\log r\). Their individual exponents remain unrestricted.
