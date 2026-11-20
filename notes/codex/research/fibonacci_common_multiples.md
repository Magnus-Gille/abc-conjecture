# What taking common multiples can contribute to a Fibonacci abc example

Let \(F_n\) be the \(n\)th Fibonacci number, \(\alpha=(1+\sqrt5)/2\), and \(E(F_n)=\log(F_n/\operatorname{rad}(F_n))\). A sequence of indices with \(E(F_n)\ge\delta n\) for fixed \(\delta>0\) disproves rational abc through the primitive triples obtained from \(L_n^2-5F_n^2=4(-1)^n\). For a prime \(p\ge7\) let \(\rho(p)\) be its first index of divisibility, and \(w_p=v_p(F_{\rho(p)})\). [Proof of the reduction and valuation formulas](hall_pell_fibonacci_ranks.md)

## The contribution from any selection of ranks

For any \(n\ge2\) and any subset \(S\) of its positive divisors, uniformly in \(S\),

\[
\sum_{\substack{p\ge7,\ p\mid F_n\\\rho(p)\in S}}v_p(F_n)\log p
=\log\alpha\sum_{r\in S}\phi(r)+O\bigl(\tau(n)+\log n\bigr).
\tag{1}
\]

Here \(\tau(n)\) is the divisor count. To prove this, take \(J_1=U_1=1\), \(J_r=\Phi_r(\alpha,(1-\sqrt5)/2)\) for \(r>1\), and \(U_r=\prod_{p\ge7,\,\rho(p)=r}p^{w_p}\). The cyclotomic factorization gives \(U_r\mid J_r\), \(\prod_{r\mid n}J_r=F_n\), and \(\log J_r=\phi(r)\log\alpha+O(1)\) with an absolute error bound. The lifting formula \(v_p(F_n)=w_p+v_p(n)\) when \(\rho(p)\mid n\), together with the valuations at \(2,3,5\), gives
\[
0\le\sum_{r\mid n}\log(J_r/U_r)=O(\log(2n)).
\]
The same bound holds for any subsum by nonnegativity. Reinstating the \(v_p(n)\) terms costs at most \(\log n\). These facts prove (1). In particular \(\tau(n)\le 2\sqrt n\) makes the error \(o(n)\) uniformly.

## Prime factors at the least common multiple of the first \(m\) integers

Put \(N_m=\operatorname{lcm}(1,\ldots,m)\). The log contribution to \(F_{N_m}\) from primes of ranks at most \(m\), including all their powers, is \(O(m^2+\log N_m)\). Indeed \(\sum_{r\le m}\log U_r\ll\sum_{r\le m}\phi(r)\ll m^2\), and the total cost of lifting and the small primes is \(O(\log N_m)\). Since \(\log N_m\asymp m\) by Chebyshev's estimates, this contribution is \(o(\log F_{N_m})\). In particular the prime factors inherited directly from the inputs \(F_1,\ldots,F_m\) cannot produce a fixed-exponent counterexample at this common multiple as \(m\to\infty\).

The larger divisors of \(N_m\) have a different behavior. Fix \(0<\theta<1\), put \(D=N_{\lfloor m^\theta\rfloor}\), and put \(h=\lfloor\theta/(1-\theta)\rfloor\). Then

\[
\lim_{m\to\infty}
\frac{\displaystyle\sum_{\substack{p\ge7,\ p\mid F_{N_m}\\D\mid\rho(p)}}
 v_p(F_{N_m})\log p}{\log F_{N_m}}
=\frac{1}{(h+1)\theta^h}.
\tag{2}
\]

In particular the limit is 1 for \(\theta=1/2\), \(3/4\) for \(\theta=2/3\), and \(16/27\) for \(\theta=3/4\).

For the proof, write \(N=N_m\). With \(t\) uniform on \(\{1,\ldots,N\}\), the integer \(r=N/\gcd(t,N)\) has distribution \(\Pr(r=d)=\phi(d)/N\) for \(d\mid N\). For \(q^a\parallel N,\ q^b\parallel D\), the condition \(q^b\mid r\) fails with probability \(q^{-(a-b+1)}\). The Chinese remainder theorem and (1) express the left side of (2), before taking the limit, as

\[
\prod_{q^b\parallel D}\left(1-q^{-(v_q(N)-b+1)}\right)+o(1).
\]

The factors with \(a>b\) have product tending to 1. Each failure probability is at most \(q^{-2}\) there, and for each fixed prime it tends to zero because \(a-b\to\infty\). For \(a=b=j\ge1\), the primes in question are exactly
\[
m^{1/(j+1)}<q\le m^{\theta/j}.
\]
The interval has positive length only when \(j/(j+1)<\theta\). By Mertens' product theorem the product of \(1-1/q\) in this interval tends to \(j/((j+1)\theta)\). Multiplication telescopes to (2). At a boundary \(\theta=j/(j+1)\), including the extra factor of 1 gives the same formula.

There is a congruence consequence at \(\theta=1/2\). For large \(m\), \(5\mid D\). If \(D\mid \rho(p)\), the order formula \(\rho(p)\mid p-(5/p)\) implies \(p\equiv\pm1\bmod5\). Quadratic reciprocity then gives \((5/p)=1\), so \(p\equiv1\bmod D\). Thus

\[
\sum_{\substack{p\mid F_{N_m}\\p\not\equiv1\bmod N_{\lfloor\sqrt m\rfloor}}}
v_p(F_{N_m})\log p=o(N_m).
\]

Any fixed positive fraction of repeated-prime mass along this sequence must therefore persist among primes in that single residue class.

## How rare ranks can carry almost all the mass

For any \(\eta>0\), write \(\gamma_{\rm E}\) for Euler's constant and define
\[
S_\eta=\left\{r\ge3:\frac{\phi(r)}{r}\log\log r
                    \le e^{-\gamma_{\rm E}}+\eta\right\}.
\]
This set has natural density zero, yet the fraction of \(\log F_{N_m}\) coming from primes of ranks in \(S_\eta\) tends to 1.

For the density statement, the mean of \(r/\phi(r)\) is bounded because \(r/\phi(r)=\sum_{d\mid r}\mu(d)^2/\phi(d)\) and \(\sum_d\mu(d)^2/(d\phi(d))=\prod_q(1+1/(q(q-1)))<\infty\). On \(S_\eta\), the ratio \(r/\phi(r)\) grows at least proportionally to \(\log\log r\), so Markov's inequality gives density zero.

For concentration, use the preceding probability distribution on divisors of \(N=N_m\). The random variable \(Z=(\phi(r)/r)/(\phi(N)/N)\) is at least 1. A prime \(q^a\parallel N\) is absent from \(r\) with probability \(q^{-a}\), independently across primes. Hence
\[
\mathbb E Z=\prod_{q^a\parallel N}\left(1+\frac{q^{-a}}{q-1}\right)\longrightarrow1
\]
by dominated convergence of the logarithms. Consequently \(Z\to1\) in probability. Mertens' theorem and \(\log N_m\asymp m\) give \((\phi(N)/N)\log\log N\to e^{-\gamma_{\rm E}}\). Since \(\log\log r\le\log\log N\) for \(r\ge3\), the probability of \(r\in S_\eta\) tends to 1 (the two smaller ranks have mass \(2/N\)). Applying (1) transfers the statement to actual prime-factor mass.

The multiplicities of interest for abc are \(\Gamma_r=\sum_{\rho(p)=r,\,p\ge7}(w_p-1)\log p\). We have \(E(F_n)=\sum_{r\mid n}\Gamma_r+O(\log(2n))\). A uniform estimate \(\Gamma_r=o(r/\log\log r)\) would suffice for \(E(F_n)=o(n)\), because \(r/\phi(r)\ll\log\log(3r)\) and the totient weights sum to \(n\). The inverse-totient bound follows by splitting its Euler product at \(\log r\), applying Mertens below that point, and using \(\#\{q\mid r:q>\log r\}\le \log r/\log\log r\) above it.

The order \(O(r/\log\log r)\), even on a density-zero set with zero contribution elsewhere, allows linear accumulation at the level of these divisor weights. For example the model weights \(b_r=\phi(r)\mathbf 1_{S_\eta}(r)\) have exactly those bounds, and \(\sum_{r\mid N_m}b_r/N_m\to1\). The actual \(\Gamma_r\) depend on prime squares at their first Fibonacci index. Formula (2) describes the full prime-factor mass and leaves the proportion contributed by these squares undetermined.
