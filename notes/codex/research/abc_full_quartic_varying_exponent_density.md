# An upper bound uniform over all perfect-power exponents

Let \(B_n^2\) be the reduced denominator of \(X(nG)\), where \(G=(-3,9)\) on \(Y^2=X^3-36X\). Fix a finite set of primes \(S\), possibly empty. Let \(N_S(X)\) count positive odd \(n\le X\) for which some integer \(k\ge2\) divides every valuation \(v_p(B_n)\) at primes \(p\notin S\). Then
\[
                         N_S(X)\ll_S X/\log(2X).
\]
The exponent can vary with \(n\) and has no upper bound. At \(S=\varnothing\) this counts all perfect powers, including \(B_1=1\). Moreover, for any fixed integer \(d>1\), the number of such perfect-power indices divisible by \(d\) is \(O_{d,\eta}(X^\eta)\) for **every** \(\eta>0\).

An additional Gaussian factorization sharpens the result at every fixed divisor \(d>1\): only finitely many perfect-power indices can be divisible by \(d\), and all can be enumerated for that input \(d\). Indeed each index must be a power of one inert prime \(q\). Thus \(d\) must be a power of the same \(q\). All possible prime exponents divide the computable numerator \(a_q\), by the prime-index descent. For each such exponent, higher-genus finiteness and the terminating census apply. This gives a finite calculation for fixed \(d\) with the exponent allowed to vary. [Gaussian index restriction](abc_full_quartic_prime_power_indices.md) · [Terminating census](abc_congruent_six_all_power_cofactors.md)

## The smallest and largest prime factors of an exceptional index

First let \(S=\varnothing\). Put \(q=P^+(n)\), \(s=P^-(n)\) for \(n>1\), and take any prime \(\ell\mid k\). The square and cube classifications exclude \(\ell=2,3\). Each prime divisor of \(B_q\) is greater than \(2q\), so its valuation in \(B_n\) is unchanged. Thus \(B_q\) is an \(\ell\)-th power. The Eisenstein descent at prime index gives \(qG=(0,0)\bmod\ell\). The order of \(G\) there is \(2q\); adjoining an independent two-torsion point gives \(4q\le(\sqrt\ell+1)^2\), hence \(\ell\ge(2\sqrt q-1)^2>2q\). [Prime-index descent](abc_full_quartic_perfect_power_census.md)

Take any prime \(p\mid B_s\), which exists since \(B_s>1\). We have \(p>2s\). The formal group gives \(v_p(B_n)=v_p(B_s)+v_p(n/s)\), a positive multiple of \(\ell\). Therefore
\[
      2q\log(2s)<\ell\log p\le \log B_s+\log n
                        \le 0.52s^2+1.5+\log n .
\]
For \(s\ge3\) this implies \(q\le\max(s^2,\log n)\). All estimates in this restriction are independent of \(k\). [Height and valuation estimates](abc_full_quartic_prime_exponents.md)

For a general \(S\), set \(M=\max(\{3\}\cup S)\) and write \(n=dm\), with \(d\) supported on primes at most \(M\) and every prime divisor of \(m\) greater than \(M\). If \(m>1\), apply the argument with \(q=P^+(m),s=P^-(m)\). Every prime of \(B_q\) is greater than \(2q\), so it is outside \(S\) and divides neither \(d\) nor \(m\). Thus \(B_q\) is an \(\ell\)-th power even here. For the second inequality each \(p\mid B_s\) is greater than \(2s>M\), so \(v_p(n/s)=v_p(m/s)\). We obtain
\[
                       P^+(m)\le\max\big((P^-(m))^2,\log m\big).
\]

## Counting the permitted integers

The integers \(m\le x\) with \(P^+(m)\le\log x\) contribute \(O_\eta(x^\eta)\) for each fixed \(\eta>0\). For \(0<\sigma<\min(\eta,1)\), Rankin's bound gives
\[
 x^\sigma\prod_{p\le\log x}(1-p^{-\sigma})^{-1}
    \le x^\sigma\exp\big(O_\sigma((\log x)^{1-\sigma})\big).
\]
This argument also handles \(P^+(m)\le C\log x\) for fixed \(C\). For a prescribed divisor \(d>1\) in the perfect-power case, even \(d\) yields no odd indices and odd \(d\) forces \(s\le P^-(d)\). Hence \(q\le\log X\) for all sufficiently large \(X\), proving the asserted bound at multiples of \(d\).

It remains to count odd \(m\le x\) with \(P^+(m)\le(P^-(m))^2\). Those at most \(\sqrt{x}\) cause no difficulty. For larger \(m\) write \(j=\Omega(m)\), counting prime factors with multiplicity. Every prime factor lies in
\[
             I_j=[x^{1/(4j)},x^{2/j}].
\]
Indeed the smallest prime is at least \(m^{1/(2j)}\), whereas the largest is at most \(m^{2/j}\). Remove the largest prime \(q\), writing \(m=bq\). For a possible \(b\), \(x/b\ge q\ge x^{1/(2j)}\), and Chebyshev's elementary prime-counting bound allows at most \(O(jx/(b\log x))\) choices of \(q\).

Uniformly in \(x,j\), \(\sum_{p\in I_j}1/p=O(1)\). Partial summation of \(\pi(y)\ll y/\log y\) proves this since the upper endpoint is the eighth power of the lower; if the lower endpoint is below 3, all primes in the interval are bounded. Since \(b\) is odd,
\[
 \sum_{\substack{\Omega(b)=j-1\\p\mid b\Rightarrow p\in I_j,\ p>2}}\frac1b
 \le 2^{1-j}\prod_{p\in I_j,\ p>2}(1-2/p)^{-1}=O(2^{-j}).
\]
The product is bounded by exponentiating a constant times \(\sum_{p\in I_j}1/p\). Summing \(O(j2^{-j}x/\log x)\) over \(j\) proves the required count for \(m\), including the prime indices.

Finally sum over the possible \(d\). For \(d\le\sqrt X\), \(\log(2X/d)\gg\log(2X)\) and \(\sum_d 1/d=\prod_{p\le M}(1-1/p)^{-1}<\infty\). The \(d>\sqrt X\) contribute at most \(X\sum_{d>\sqrt X}1/d\ll_M X^{3/4}\), using convergence of \(\sum_d d^{-1/2}\). This also covers \(m=1\), and completes the proof.

The elementary counting argument already allows all prime indices. To improve this method beyond \(X/\log X\) one would need additional restrictions on the indices that survive its largest-prime and smallest-prime comparison. The abc inequality concerns the radical at *every* index and also allows varying sets of exceptional valuation primes. [What a fixed abc exponent requires](abc_full_quartic_twin_and_mixed_valuations.md)

## Allowing a fixed exceptional set cannot create the first infinite family

The following two existence statements are equivalent.

1. At infinitely many odd prime indices \(q\equiv3\pmod4\), \(B_q\) is a perfect power of exponent at least two.
2. For some fixed finite set \(S\), infinitely many odd indices \(n\) have all valuations of \(B_n\) outside \(S\) divisible by a common integer \(k_n\ge2\).

The first implies the second with \(S=\varnothing\). To prove the converse, fix any integer \(K\ge\max(\{3\}\cup S)\). Only finitely many indices counted in the second statement can have \(P^+(n)\le K\). Indeed for each odd prime \(r\le K\), choose \(j_r\) so large that \(r^{j_r}>(\sqrt K+1)^2\). There is a prime \(h_r\) of first appearance at \(r^{j_r}\), by the primitive-divisor estimate for this curve. Hasse gives \(h_r>K\). For an index supported on primes at most \(K\) and divisible by \(r^{j_r}\), its valuation at \(h_r\) is the fixed positive integer \(v_{h_r}(B_{r^{j_r}})\). Consequently \(k_n\) is bounded on these indices. Those divisible by none of the finitely many \(r^{j_r}\) form a finite set themselves. For each of the bounded exponents, finiteness with fixed exceptional support follows from Faltings' theorem on the trace curves. [Primitive divisors](abc_full_quartic_prime_exponents.md) · [Finiteness and effective enumeration](abc_congruent_six_all_power_cofactors.md)

It follows that \(q=P^+(n)\) is unbounded in the second statement. At each \(q>\max(\{3\}\cup S)\), every \(p\mid B_q\) is greater than \(2q\) and outside \(S\), and its valuation in \(B_n\) is unchanged. Thus \(B_q\) is a \(k_n\)-th power. The Gaussian argument forces \(q\equiv3\pmod4\), proving the first statement. In particular either infinite family would disprove rational abc at \(\varepsilon=1/4\) via the prime-index subfamily. [Index restriction](abc_full_quartic_prime_power_indices.md) · [Radical calculation](abc_full_quartic_perfect_power_census.md)
