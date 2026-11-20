# Primes with a divisor of \(p-1\) near \(\sqrt{x}\)

Fix \(B\ge0\). For \(x<p\le 2x\), call a prime \(p\) eligible if some divisor \(d\mid p-1\) lies in
\[
  \frac{\sqrt{x}}{(\log x)^B}\le d\le \sqrt{x}(\log x)^B.
\]
For every fixed \(0<\delta<\delta_0\), where
\[
     \delta_0=1-\frac e2\log 2=0.0579153073\ldots,
\]
the number of eligible primes is
\[
       \ll_{B,\delta}\frac{x}{(\log x)^{1+\delta}}.                 \tag{1}
\]
All logarithms are natural. The estimate uses only the divisor condition on \(p-1\). In particular it applies when an additional condition specifies which divisor to use.

## Counting small primes of \(p-1\) and their squares

Put \(L=\log\log x\) and \(T=x^{1/(10L)}\), taking \(x\) sufficiently large. Define
\[
 D(p)=\#\{\ell\le T:\ell\text{ prime},\ \ell\mid p-1\},\qquad
 J(p)=\#\{\ell\le T:\ell\text{ prime},\ \ell^2\mid p-1\}.
\]
Write \(Q(v)=1-v+v\log v\). For fixed \(1<\lambda<2\), the upper tail satisfies
\[
 \#\{x<p\le 2x:D(p)\ge\lambda L\}
       \ll \frac{x}{\log x}\exp\bigl((-Q(\lambda)+o(1))L\bigr).      \tag{2}
\]
Indeed take \(t=\lceil\lambda L\rceil\), \(k=\lfloor(\lambda-1)L\rfloor\), and expand \(\binom{D(p)}k\) into incidences of \(k\) distinct primes. Their product \(m\le T^k\le x^{1/2}\) divides \(p-1\). Brun–Titchmarsh bounds the number for each such modulus by \(O(x/(\varphi(m)\log x))\). Summing over products and dividing by \(\binom tk\) bounds the left side of (2) by
\[
 \ll\frac{x}{\log x}\frac{V^k}{t(t-1)\cdots(t-k+1)},\qquad
 V=\sum_{\ell\le T,\ \ell\ {\rm prime}}\frac1{\ell-1}=L+o(L)
\]
by Mertens' theorem. The logarithm of the last ratio divided by \(L\) tends to \(-\int_1^\lambda\log v\,dv=-Q(\lambda)\).

For fixed \(0<\varepsilon<1\), the same argument with \(t=\lceil\varepsilon L\rceil\), \(k=\lfloor\varepsilon L/2\rfloor\) gives
\[
 \#\{x<p\le2x:J(p)\ge\varepsilon L\}
       \ll\frac{x}{\log x}\exp(-c_\varepsilon L\log L)               \tag{3}
\]
for some \(c_\varepsilon>0\). The moduli are now products of \(k\) distinct prime squares, at most \(T^{2k}\le x^{1/2}\). Here \(\sum_\ell 1/\varphi(\ell^2)<\infty\), while every factor of the falling factorial is at least \(\varepsilon L/2\).

## Counting complementary factors with few small primes

Choose \(1<c<2\) and put \(z=c/2\). If \(p-1=uv\), then
\[
 \omega_T(u)+\omega_T(v)=D(p)+\omega_T(\gcd(u,v))\le D(p)+J(p),
\]
where \(\omega_T\) counts distinct prime factors at most \(T\). If \(D(p)+J(p)<cL\), one factor therefore satisfies \(\omega_T(u)\le zL\), relabeling the factors if necessary. When \(p\) is eligible, both factors lie in
\[
 I=\bigl[\tfrac12\sqrt{x}(\log x)^{-B},\,2\sqrt{x}(\log x)^B\bigr].
\]

To count the possible \(u\), let \(f(n)=z^{\omega_T(n)}\). Uniformly for \(U\) between half the lower endpoint and twice the upper endpoint of \(I\), we have
\[
                \sum_{n\le U}f(n)\ll_z U(\log T)^{z-1}.              \tag{4}
\]
Indeed \(f\) is multiplicative and bounded by one. Grouping by the exact prime powers \(\ell^j\parallel n\) gives
\[
 \sum_{n\le U}f(n)\log n
  =\sum_{m\le U} f(m)
       \sum_{\substack{\ell^j\le U/m,\ j\ge1\\ \ell\ {\rm prime},\ \ell\nmid m}}
          j f(\ell^j)\log\ell
  \ll U\sum_{m\le U}\frac{f(m)}{m}.
\]
The inner bound uses \(\sum_{\ell^j\le v}j\log\ell\ll v\) by Chebyshev's estimate, with prime powers of exponent at least two contributing \(O(\sqrt v\log^2(2v))\). Since \(T<U\), the Euler product bound and Mertens' theorem give
\[
 \sum_{m\le U}\frac{f(m)}m
 \le \prod_{\ell\le T}\left(1+\frac z{\ell-1}\right)
       \prod_{T<\ell\le U}\left(1+\frac1{\ell-1}\right)
 \ll_z (\log U)(\log T)^{z-1},
\]
where the products run over primes. Splitting the original sum at \(\sqrt U\) proves (4). For \(\omega_T(u)\le zL\) one has \(f(u)\ge z^{zL}\), and \(\log\log T=L-\log(10L)\). It follows uniformly in the same range that
\[
          \#\{u\le U:\omega_T(u)\le zL\}
           \le U\exp\bigl((-Q(z)+o(1))L\bigr).                     \tag{5}
\]

Brun–Titchmarsh gives \(O(x/(\varphi(u)\log x))\) primes \(x<p\le2x\) with \(p\equiv1\pmod u\), uniformly for \(u\in I\). Here \(u/\varphi(u)\ll\log\log(3u)\ll L\). Cover \(I\) by \(O_B(1+L)\) intervals \((U/2,U]\) and use (5) on each. These factors polynomial in \(L\) are \(\exp(o(L))\), giving the bound
\[
 \#\{x<p\le2x:p\text{ eligible},\ D(p)+J(p)<cL\}
 \ll\frac{x}{\log x}\exp\bigl((-Q(c/2)+o(1))L\bigr).                \tag{6}
\]

## Optimizing the exponent

For the remaining primes, either \(D(p)\ge(c-\varepsilon)L\) or \(J(p)\ge\varepsilon L\). Apply (2) and (3) with \(0<\varepsilon<c-1\). The limiting saving available from (2) and (6) is \(\min\{Q(c),Q(c/2)\}\) as \(\varepsilon\downarrow0\). On \(1<c<2\), the first term increases and the second decreases. They coincide when \(\log(2c)=1\), so \(c=e/2\) and their common value is \(\delta_0\). Given \(\delta<\delta_0\), first choose \(\varepsilon>0\) with \(Q(c-\varepsilon)>\delta\), then take \(x\) large enough to absorb the \(o(1)\) terms. This proves (1).

The progression estimate used twice above is the Brun–Titchmarsh inequality in the form \(\pi(Y;q,a)\le 2Y/(\varphi(q)\log(Y/q))\) for \(Y>q\) and \((q,a)=1\). H. L. Montgomery and R. C. Vaughan, *The large sieve*, Mathematika **20** (1973), 119–134.
