# Shifted primes with an unbalanced divisor and a uniform sum of reciprocal orders

For coprime integers \(A>B\ge1\), put \(h=\log A\). For primes \(p\nmid AB\), let \(r_p\) be the order of \(A/B\) modulo \(p\). Write
\[
 S_{A,B}(X)=\sum_{\substack{p\le X\\p\nmid AB}}\frac{\log p}{r_p},
 \qquad \delta=1-\frac{1+\log\log2}{\log2}=0.08607\ldots .
\]
For \(X\ge2\), every \(h\ge\log 2\) arising from these seeds, and every fixed \(0<b<\delta/2\), one has
\[
 \boxed{\displaystyle
 S_{A,B}(X)\ll_b\frac{\sqrt{Xh}}{(\log(2+X/h))^b}.}                  \tag{1}
\]
The constants are uniform in \(A,B,X\). The underlying shifted-prime estimate applies even when the two divisors of \(p-1\) have logarithms of different orders of magnitude. Conditioning on the smaller divisor and sieving the other variable for primality retains the factor \(1/\log X\). [Balanced-divisor argument](abc_shifted_prime_rectangular_sieve.md) · [Ford, *The distribution of integers with a divisor in a given interval*](https://arxiv.org/abs/math/0401223)

## A divisor interval

For \(x\) sufficiently large and \(2\le D\le x^{3/5}\), consider primes \(x/2<p\le x\) with
\[
        p=de+1,\qquad D\le d<2D.
\]
For every \(\varepsilon>0\), their number is
\[
             \ll_\varepsilon
        \frac{x}{\log x}(\log(2D))^{-\delta+\varepsilon}.             \tag{2}
\]
Write \(E=x/D\), so \(E/5\le e\le E\) for large \(x\) and \(\log E\ge(2/5)\log x\). Bounded \(D\) is covered by the prime number theorem. For large \(D\) put
\[
 K=\log\log D,\qquad w=D^{1/K^2},\qquad
 L=\sum_{q\le w}\frac1q=K-2\log K+O(1),
\]
with \(q\) always prime. Put \(\omega_w(m)=\sum_{q\le w}{\bf1}_{q\mid m}\) and \(J_w(m)=\sum_{q\le w}{\bf1}_{q^2\mid m}\). All estimates as \(D\to\infty\) below are uniform in the allowed \(x\).

## An upper sieve for an interval

Let \(P_0=E^{1/64}\). For each prime \(q\le P_0\) prescribe \(\nu(q)\le2\) forbidden residue classes. If \(\nu(q)=q\) at any prime, the surviving set is empty. Otherwise the number of survivors in any interval of at most \(E+1\) consecutive integers is
\[
             \ll E\prod_{q\le P_0}(1-\nu(q)/q).                      \tag{3}
\]
Here and below \(E\) is sufficiently large. The implied constant is absolute.

For a verification by Selberg's upper weights, omit the primes with \(\nu(q)=0\), let \(P\) be the product of the other sieving primes, and set \(f(q)=\nu(q)/q,\ g(q)=f(q)/(1-f(q))\). Extend each multiplicatively to squarefree divisors of \(P\). For \(d\mid P\), denote by \(\Omega_d\) the residue classes simultaneously forbidden at every prime of \(d\). For \(d=1\) take all integers. The number of members of an interval of length \(H\) belonging to \(\Omega_d\) is \(Hf(d)+O(\prod_{q\mid d}\nu(q))\). Use weights supported on \(d\mid P,\ d\le V=P_0^8\), with \(\lambda_1=1\). Summing the nonnegative squares \((\sum_{d\le V}\lambda_d{\bf1}_{e\in\Omega_d})^2\) gives an upper bound for the surviving count. Its main quadratic form divided by \(H\) is
\[
 \sum_{a,d}\lambda_a\lambda_d f([a,d])
     =\sum_{\ell\mid P,\,\ell\le V}\frac{u_\ell^2}{g(\ell)},
 \qquad
 u_\ell=\sum_{\substack{d\mid P,\,d\le V\\\ell\mid d}}\lambda_d f(d).
\]
This follows from \(f([a,d])=f(a)f(d)\sum_{\ell\mid(a,d)}1/g(\ell)\). Put \(G=\sum_{\ell\mid P,\,\ell\le V}g(\ell)\). Choosing \(u_\ell=\mu(\ell)g(\ell)/G\) gives \(\lambda_1=1\) by inversion, and the quadratic form equals \(1/G\). The inversion formula also gives
\[
 |\lambda_d|=
 \frac{g(d)}{f(d)G}
       \sum_{\substack{a\mid P,\ a\le V/d\\(a,d)=1}}g(a)\le1 .
\]
Indeed \(g(d)/f(d)=\sum_{s\mid d}g(s)\), and all resulting \(sa\) are distinct divisors counted by \(G\). The total interval discrepancy is at most a constant times
\[
 \sum_{a,d\le V}2^{\omega([a,d])}
 \le\left(\sum_{a\le V}2^{\omega(a)}\right)^2
 \ll V^2\log^2(2V),
\]
using \(2^{\omega(a)}\le\tau(a)\).

To lower bound \(G\), place mass proportional to \(g(k)\) on all \(k\mid P\). Under this probability distribution the events \(q\mid k\) are independent with probabilities \(f(q)\). Thus
\[
       \mathbb E\log k\le2\sum_{q\le P_0}\frac{\log q}{q}
                       =(2+o(1))\log P_0 .
\]
Markov's inequality leaves at least half the mass below \(V=P_0^8\). Hence \(1/G\ll\prod(1-\nu(q)/q)\). This product is \(\gg(\log E)^{-2}\) uniformly when no local factor vanishes. For \(q>2\) compare \(1-2/q\) with \((1-1/q)^2\) using their ratio \(1-1/(q-1)^2\), whose product converges to a positive limit. At two the admissible factor is at least \(1/2\). Now \(V^2=E^{1/4}\) makes the discrepancy negligible and proves (3).

## The weighted pairs

Fix \(0<z<1\). Independently select each prime \(q\le w\) with probability \(1-z\). For fixed \(e\), the probability that no selected prime divides \(e\) is \(z^{\omega_w(e)}\). At fixed \(d\) apply (3) in \(e\), forbidding \(de+1\equiv0\bmod q\) for every \(q\le P_0\) where \(q\nmid d\), and additionally forbidding \(e\equiv0\bmod q\) at each selected prime. Here \(w\le P_0\) for all sufficiently large \(D\) uniformly, since \(\log D/\log E\le3/2\). Every counted prime \(p>x/2\) exceeds \(P_0\). Thus all actual pairs contributing to this prime slab satisfy the primality exclusions. If \(d\) is odd and 2 is selected, both residues modulo 2 are forbidden and the count is zero, as required by its local factor.

When \(q\le w\) and \(q\nmid d\), averaging the local factor gives
\[
             (1-1/q)\big(1-(1-z)/(q-1)\big).
\]
When \(q\le w\) and \(q\mid d\) it gives \(1-(1-z)/q\). For \(w<q\le P_0\) only the primality constraint contributes. Independence of the selections and Mertens' theorem therefore give
\[
 \sum_{\substack{E/5\le e\le E\\de+1\ {\rm prime},\ x/2<de+1\le x}}
       z^{\omega_w(e)}
   \ll \frac{E}{\log E}\frac{d}{\varphi(d)}\,e^{-(1-z)L}.            \tag{4}
\]
The factor \(d/\varphi(d)\) bounds the cost of omitting the primality condition at primes dividing \(d\). The remaining factors for \(q\le w\) are each at most \(1-(1-z)/q\).

For the other variable, unweighted Bonferroni gives
\[
       \sum_{D\le d<2D}z^{\omega_w(d)}\ll_z D\,e^{-(1-z)L}.
\]
In detail, expand \(\prod_{q\le w}(1-(1-z){\bf1}_{q\mid d})\) through an even order \(T\) between \(30L\) and \(30L+2\) for an upper bound. Replacing the average of each divisibility indicator product by the reciprocal of the corresponding squarefree modulus costs \(O(1/D)\) per term. There are at most \((T+1)w^T=D^{o(1)}\) terms. The complete-residue sum differs from \(\prod_{q\le w}(1-(1-z)/q)\) by at most \(\sum_{j>T}L^j/j!\ll e^{-10L}\). The fractional-weight Bonferroni inequality follows from ordinary inclusion-exclusion by independently selecting the primes with probability \(1-z\). Finally \(\max_{D\le d<2D}d/\varphi(d)\ll\log\log(3D)=\exp(o(L))\). This follows by Mertens' theorem for primes up to \(\log(3D)\); the larger primes of \(d\) contribute at most \(\exp(O(\omega(d)/\log(3D)))=O(1)\). Multiplying (4) by \(z^{\omega_w(d)}\) and summing yields
\[
  \sum_{\substack{d,e\ {\rm in\ the\ rectangle}\\de+1\ {\rm prime},\
                         x/2<de+1\le x}}
            z^{\omega_w(d)+\omega_w(e)}
       \ll \frac{x}{\log x}\exp\big((-2(1-z)+o(1))L\big).            \tag{5}
\]

## Combining the two tails

Write \(I(t)=1-t+t\log t\). On primes \(x/2<p\le x\) with uniform probability, Brun–Titchmarsh gives, for \(1\le j\le3L\),
\[
 \mathbb E\binom{\omega_w(p-1)}j\ll\frac{(L+O(1))^j}{j!},\qquad
 \mathbb E\binom{J_w(p-1)}j\ll\frac{C^j}{j!}.
\]
Every modulus in these factorial moments is at most \(w^{2j}=D^{o(1)}\le x^{o(1)}\). Its class \(1\) has probability \(O(1/\varphi(m))\), by Brun–Titchmarsh and the prime number theorem in the slab. Summing over the \(j\) distinct primes uses \(\sum_{q\le w}1/(q-1)=L+O(1)\) and \(\sum_q1/(q(q-1))<\infty\).

For fixed \(1<t<2\), use \(j=\lfloor(t-1)L\rfloor\) in the first estimate and divide by \(\binom{\lceil tL\rceil}{j}\). Stirling's formula gives \(\Pr(\omega_w(p-1)\ge tL)\le\exp(-(I(t)+o(1))L)\). For each fixed \(\eta>0\) sufficiently small, the second estimate with \(j=\lceil\eta L\rceil\) bounds \(\Pr(J_w(p-1)\ge\eta L)\) by \(\exp(-\eta L\log L+O_\eta(L))\). Applying the first estimate at \(t-\eta\) and then letting \(\eta\downarrow0\) shows that the upper tail \(\omega_w(p-1)+J_w(p-1)>tL\) has probability at most \(\exp((-I(t)+o(1))L)\), in the sense of the upper logarithmic exponent.

On the complementary event, \(\omega_w(d)+\omega_w(e)\le\omega_w(p-1)+J_w(p-1)\le tL\). Thus (5) bounds the number of these pairs relative to \(x/\log x\) by \(\exp((-2(1-z)-t\log z+o(1))L)\). At \(z=t/2\) the saving is \(2I(t/2)\). At \(t=1/\log2\) this equals \(I(t)=\delta\). Counting each prime in the high tail once and bounding the low tail by its pair count proves (2).

## Summing reciprocal orders uniformly in the height

For every real \(U\ge2\), the crude bound \(S_{A,B}(U)\ll\sqrt{Uh}\) holds. The product of the distinct primes of any fixed rank \(r\) divides \(A^r-B^r\), which has logarithm at most \(rh\). If \(U\ge h\), ranks up to \(\sqrt{U/h}\) therefore cost \(O(\sqrt{Uh})\). The complementary ranks have reciprocal at most \(\sqrt{h/U}\) and cost \(O(\sqrt{Uh})\) by Chebyshev's prime estimate. If \(U<h\), the trivial bound \(O(U)\) suffices. For \(U<2\) the sum is empty.

On the slab \(x/2<p\le x\) let \(Q=x/h\). When \(Q\) is bounded the crude estimate gives the slab version of (1). Otherwise put \(Y=\sqrt Q\), \(Z=(\log(2+Q))^b\). As in the crude bound, ranks below \(Y/Z\) and above \(YZ\) together cost \(O(\sqrt{xh}/Z)\). Split the remaining ranks into \(O(1+\log Z)\) intervals \([D,2D)\) with \(D\asymp Y/Z\) or larger and \(D\le YZ\). Here \(\log(2D)\asymp\log(2+Q)\), and \(2\le D\le x^{3/5}\) for all large \(Q\), since \(h\ge\log 2\). The order \(r_p\) divides \(p-1\), so (2) applies to each interval. The weight per prime is at most \(Z\log x/Y\), giving in total
\[
      \ll_\varepsilon \sqrt{xh}\,
          (\log(2+Q))^{b-\delta+\varepsilon}(1+\log Z).
\]
Choosing \(\varepsilon<\delta-2b\) absorbs the interval count and proves the slab bound uniformly.

Finally put \(R=X/h\). For bounded \(R\), the crude estimate already proves (1). For large \(R\), let \(U=X/(\log(2+R))^2\), and cover primes down to \(U\) by slabs whose upper endpoints are \(X,X/2,X/4,\ldots\) and are at least \(U\). For those endpoints \(\log(2+x/h)\asymp\log(2+R)\) because \(U/h=R/(\log(2+R))^2\). The sum of the square roots of the endpoints is \(O(\sqrt X)\). The remaining primes cost at most \(O(\sqrt{Uh})=O(\sqrt{Xh}/\log(2+R))\) by the crude estimate. This proves (1) without restricting how the seed varies with \(X\).
