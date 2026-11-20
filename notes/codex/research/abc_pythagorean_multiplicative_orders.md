# Where a fixed exponent would have to come from at perfect-power hypotenuses

Suppose \(v^2+w^2=u^2\) is primitive and \(u=A^n,\ A>1\). Let \(n\to\infty\), allowing \(A,v,w\) to vary. For every function \(b(n)\to\infty\), the entire contribution of primes \(p\le n/(\log n)^{b(n)}\) to \(\log(vw)\), including their first factors of \(p\), is \(o(\log u)\), uniformly in \(A\). The contribution from an unusually small leg, \(\log(u^2/(vw))\), is also \(o(\log u)\).

In particular, if \(u^2/\operatorname{rad}(uvw)\ge (u^2)^\delta\) along such a sequence for fixed \(\delta>0\), then at least \((2\delta-o(1))\log u\) must come from repeated prime factors that *already occur with multiplicity at their first multiplicative order*, at orders greater than \(n/(\log n)^{b(n)}\). The bound permits arbitrarily large multiplicities at those first orders.

## Valuations and orders

All primes of \(A\) split in \(\mathbb Z[i]\). Choosing one Gaussian prime from each conjugate pair according to the factorization of \(v+iw\) gives \(\gamma\) of norm \(A\), coprime to its conjugate, such that \((v+iw)/u\) is \(\alpha^n\) up to a Gaussian unit, where \(\alpha=\gamma/\bar\gamma\). In particular \(\alpha\) is not a root of unity. Set \(N=4n\). The identity \(\beta^4-1=2i\beta^2\operatorname{Im}(\beta^2)\) for \(\beta=(v+iw)/u\) gives \(|\alpha^N-1|=4vw/u^2\).

If an odd prime \(p\mid vw\), then \(p\nmid A\); at any prime \(\mathfrak p\) above \(p\), let \(r_p\) be the order of \(\alpha\) modulo \(\mathfrak p\). The two split coordinates are inverse and give the same order. Then \(r_p\mid N\), and \(r_p\mid p-1\) for split primes or \(r_p\mid p+1\) for inert primes by the norm-one condition. The odd primes are unramified and binomial lifting gives
\[
 v_p(vw)=v_{\mathfrak p}(\alpha^{r_p}-1)+v_p(N/r_p).
\]
All second terms together contribute at most \(\log N\). At any fixed order \(r\) the first terms come from the homogeneous cyclotomic value \(\Phi_r(\gamma,\bar\gamma)\), since no earlier divisor of \(r\) vanishes modulo the prime. Its nonzero integer norm is at most \((4A)^{\varphi(r)}\) by the complex product over the primitive \(r\)-th roots. Therefore, for any \(Y\ge1\), the sum of \(v_p(vw)\log p\) over odd primes of order at most \(N/Y\) is bounded by
\[
 \log N+\log(4A)\sum_{\substack{r\mid N\\r\le N/Y}}\varphi(r).
\]
This includes all odd \(p\) with \(p+1\le N/Y\).

The prime 2 contributes \(O(\log(4A)+\log(2n))\). Indeed, apply the same identity first with exponent 1 to the representation with Gaussian numerator \(\gamma^2=x+iy\). At \(1+i\), \(\alpha^4-1=4i\alpha^2 xy/A^2\) has valuation greater than \(v_{1+i}(2)=2\). Binomial lifting now gives \(v_2(vw)=v_2(xy)+v_2(n)\).

## A uniform divisor bound

For \(J\) uniform modulo \(N\), let \(D=\gcd(J,N)\). The divisor sum above is exactly \(N\Pr(D\ge Y)\), by counting residues of additive order \(N/D\). For large \(N\), set \(s=1/\log\log(3N)\). Then \(\mathbb E D^s=O(1)\) absolutely. Chinese remaindering bounds the local expectation at \(p\mid N\) by
\[
 1+\frac{p^s-1}{p(1-p^{s-1})}.
\]
This follows by summing the successive increments of \(p^{js}\) with probabilities \(p^{-j}\). For \(p\le(\log(3N))^2\), the logarithms of these factors sum to \(O(s\sum(\log p)/p)=O(1)\), using \(p^s\le e^2\) and the elementary Chebyshev bound. At larger primes the increment is \(O((\log(3N))^{-2})\) since \(p^{s-1}\) is decreasing, and there are \(O(\log N)\) prime factors. Markov's inequality gives \(\Pr(D\ge Y)\ll\exp(-\log Y/\log\log(3N))\). Taking \(Y=(\log n)^{b(n)}\) proves the asserted negligible contribution for small orders, including all sufficiently small primes. Here \(n\log(4A)=O(\log u)\) uniformly for \(A>1\).

## The real contribution

The two-logarithm case of the Baker–Wüstholz theorem gives \(-\log|\alpha^{4n}-1|\ll\log(4A)\log(2n)\). For clarity, take \(4n\log\alpha-2j\log(-1)\) with the principal argument and the nearest choice of \(j\), so \(|j|=O(n)\) and the linear form is nonzero. The field degree is at most 2, the logarithmic height of \(\alpha\) is \(O(\log(4A))\), and the second algebraic number is fixed. Comparison with its exponential on imaginary arguments in \([-\pi,\pi]\) gives the inequality. Thus \(\log(u^2/(vw))=o(n\log A)\).

Finally \(u\) is coprime to both legs and the legs are coprime to each other, so the logarithmic saving is the sum of the real contribution and \(\sum_{p\mid vw}(v_p(vw)-1)\log p\), less \(\log\operatorname{rad}(u)\). Removing the small-order and valuation-lifting contributions just bounded gives the stated necessity. The conclusion concerns a fixed \(\delta\) as \(n\) grows. Raising a single starting triangle to higher Gaussian powers does not by itself preserve such a fixed exponent.
