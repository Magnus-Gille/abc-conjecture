# A two-variable sieve for divisors near the square root of a shifted prime

Put
\[
 I(t)=1-t+t\log t,\qquad
 t_0=1/\log 2,\qquad
 \delta=I(t_0)=1-\frac{1+\log\log2}{\log2}=0.08607\ldots .
\]
All logarithms are natural. For every fixed \(B>0\), the number of primes \(X/2<p\le X\) for which \(p-1=de\) with
\[
        \sqrt X/(\log X)^B\le d\le\sqrt X(\log X)^B
\]
is at most \(X(\log X)^{-1-\delta+o_B(1)}\). This is an upper bound of the classical multiplication-table type. The proof below gives the logarithmic exponent directly and does not optimize factors of \(\log\log X\). [Kevin Ford, *The distribution of integers with a divisor in a given interval*](https://arxiv.org/abs/math/0401223)

## The prime tail

Let \(K=\log\log X\), \(y=X^{1/K^2}\), and \(L=\sum_{q\le y}1/q=K-2\log K+O(1)\), with \(q\) always prime. Define
\[
 D(m)=\sum_{q\le y}{\bf1}_{q\mid m},\qquad
 J(m)=\sum_{q\le y}{\bf1}_{q^2\mid m}.
\]
Use the uniform probability measure on primes \(X/2<p\le X\). For \(1\le j\le 3L\), expanding the binomial coefficient and applying Brun–Titchmarsh gives
\[
 \mathbb E\binom{D(p-1)}j
 \ll \frac{(L+O(1))^j}{j!},\qquad
 \mathbb E\binom{J(p-1)}j
 \ll \frac{C^j}{j!}.
\]
Indeed the respective moduli are products of \(j\) distinct primes, or of their squares, of size at most \(y^{2j}=X^{o(1)}\), uniformly in this range. Brun–Titchmarsh and the prime number theorem give a bound \(O(1/\varphi(m))\) for the probability of \(p\equiv1\bmod m\), with an absolute implied constant. The sums over distinct primes are bounded by the corresponding powers of \(\sum_{q\le y}1/(q-1)=L+O(1)\) and \(\sum_q1/(q(q-1))<\infty\), divided by \(j!\).

For fixed \(1<t<2\), choose \(j=\lfloor(t-1)L\rfloor\). Dividing the first moment bound by \(\binom{\lceil tL\rceil}j\) and applying Stirling gives
\[
 \mathbb P(D(p-1)\ge tL)
       \le \exp\{-(I(t)+o(1))L\}.
\]
For example the log of the reciprocal falling-factorial ratio, after subtracting \(j\log L\), is \(L\int_1^t\log u\,du+o(L)=L I(t)+o(L)\). For every fixed \(0<\eta<1\), the second moment bound with \(j=\lceil\eta L\rceil\) gives
\(\mathbb P(J(p-1)\ge\eta L)\le\exp(-\eta L\log L+O_\eta(L))\).
Consequently the primes with \(D(p-1)+J(p-1)>tL\) number at most
\[
             X(\log X)^{-1-I(t)+o(1)}.                                  \tag{1}
\]
To interpret the exponent rigorously, use the \(D\) bound first with \(t-\eta>1\), then take \(\eta\downarrow0\). This proves the stated limit superior of the logarithmic exponent.

## A weighted upper bound in one rectangle

Divide the allowed \(d\)'s into \(O_B(\log\log X)\) dyadic intervals \([U,2U)\). Since \(X/2<p\le X\), the corresponding \(e\)'s lie in \([X/(5U),X/U]\) for large \(X\). Enclose each set by this rectangle of integers. Its row and column lengths \(H_1,H_2\) are \(\asymp U,X/U\), respectively, with \(H_1H_2\asymp X\) and \(\min(H_1,H_2)\ge X^{1/2-o_B(1)}\).

Fix \(0<z<1\). For residues \((d,e)\) modulo \(q\) put
\[
 F_q(d,e)={\bf1}_{q\nmid de+1}\,
           z^{{\bf1}_{q\mid d}+{\bf1}_{q\mid e}},\qquad g_q=1-F_q.
\]
Both functions take values in \([0,1]\). For uniform independent residues the exact average is
\[
 \overline F_q=
       \left(1-\frac{1-z}{q}\right)^2-\frac{q-1}{q^2}
       =1-\frac{3-2z}{q}+O(q^{-2}).
\]
The subtraction counts the \(q-1\) solutions of \(de=-1\), where both divisibility indicators vanish. In particular \(\sum_{q\le y}\overline g_q=(3-2z)L+O(1)\).

We claim that, uniformly on these rectangles,
\[
       \frac{1}{H_1H_2}\sum_{d,e}\prod_{q\le y} F_q(d,e)
                   \ll_z \exp(-(3-2z)L).                               \tag{2}
\]
Take an even \(T\) between \(40L\) and \(40L+2\). For fixed \((d,e)\), introduce independent events of probabilities \(g_q(d,e)\). Ordinary inclusion-exclusion for these events gives the upper Bonferroni sum of order \(T\) for \(\prod(1-g_q)\), including fractional \(g_q\).

For each subset of at most \(T\) primes, put \(m\) equal to their product. Its product of \(g_q\)'s is bounded by one and is periodic in each variable modulo \(m\). The discrepancy between its rectangle average and its complete-residue average is
\[
 O\left(\frac{m}{H_1}+\frac{m}{H_2}
                       +\frac{m^2}{H_1H_2}\right).
\]
This follows by multiplying the two residue-class counts \(H_i/m+O(1)\) and summing over the \(m^2\) residue pairs. By the Chinese remainder theorem its complete-residue average is exactly \(\prod_{q\mid m}\overline g_q\). The number of subsets and the largest possible \(m\) are each at most \((T+1)y^T=X^{o(1)}\), so even summing absolute discrepancies costs at most \(X^{-1/2+o_B(1)}\).

Let \(\lambda=\sum_{q\le y}\overline g_q\le 3L+O(1)\). The difference between the complete-residue Bonferroni sum and the full product \(\prod_{q\le y}(1-\overline g_q)\) has absolute value at most \(\sum_{j>T}\lambda^j/j!\). At \(T\ge40L\) the factorial bound and a geometric tail make this \(O(e^{-10L})\). Finally the full product is at most \(e^{-\lambda}\ll_z e^{-(3-2z)L}\), which proves (2).

## Counting the balanced primes

If \(p=de+1>X/2\) is prime, all local primality indicators in (2) equal one. Each prime \(q\le y\) dividing both \(d\) and \(e\) contributes twice to \(D(p-1)+J(p-1)\), and a prime dividing only one contributes at least once. Thus
\[
        D(d)+D(e)\le D(p-1)+J(p-1).
\]
If the right side is at most \(tL\), then \(z^{D(d)+D(e)}\ge z^{tL}\). Therefore the count of all such pairs in one rectangle is at most
\[
      O_z\!\left(X\,\exp\big(-[3-2z+t\log z]L\big)\right).
\]
This upper bounds their distinct primes as well. Choose \(z=t/2\). Summing over the rectangles and using \(L=(1+o(1))\log\log X\) bounds the low-\(D+J\) count by \(X(\log X)^{-1-2I(t/2)+o_B(1)}\). The high-\(D+J\) count was estimated in (1). At \(t=t_0\) the exponents match because \(2I(t/2)-I(t)=1-t\log2\). This gives the asserted shifted-prime estimate.

## Applications and sources

The weighted order estimate and its consequences for the radicals of $A^n-B^n$ use the exponent above. A separate one-variable proof gives a smaller positive exponent. [Differences of powers](abc_average_order_radical.md) · [One-variable proof](abc_balanced_shifted_primes.md)

Divisors of shifted primes in prescribed intervals have long been studied. Koukoulopoulos credits Ford with upper bounds of the expected order and obtains corresponding lower bounds. The calculation here supplies the specific range and exponent used in the radical argument. [Kevin Ford, *The distribution of integers with a divisor in a given interval*](https://doi.org/10.4007/annals.2008.168.367) · [Dimitris Koukoulopoulos, *Divisors of shifted primes*](https://doi.org/10.1093/imrn/rnq045)

For all sufficiently large $n$, Stewart gives $P^+(2^n-1)>n\exp(\log n/(104\log\log n))$. Akbary and Yazdani describe the abc-conditional lower bound of Murty and Wong of order $n^{2-\varepsilon}$ for $P^+(a^n-1)$ at every index for fixed integer $a>1$. [Stewart](https://arxiv.org/abs/1008.1274) · [Akbary and Yazdani](https://arxiv.org/abs/1505.06500)
