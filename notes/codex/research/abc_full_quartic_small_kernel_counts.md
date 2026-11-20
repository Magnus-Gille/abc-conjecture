# Counting small squarefree kernels and their mean size

For odd \(n\), let \(B_n\) be the positive denominator square root at \(n(-3,9)\) on \(y^2=x^3-36x\), and let \(d_n=\operatorname{sf}(B_n)\) denote its product of odd-valuation primes.

For every fixed \(A>0\),
\[
 \#\{n\le X:n\text{ odd},\ d_n\le n^A\}
                 \ll_A X(\log X)^{-7/36}.
\]
In fact, except for \(O(X(\log X)^{-7/36})\) odd \(n\le X\),
\[
                \log d_n\gg(\log X)^{3/4+0.361\log 2}.
\]
The exponent is greater than \(1.00022\). The stronger almost-everywhere estimate with exponent \(2.038296\ldots-o(1)\) remains available separately. In mean, one has
\[
 \sum_{\substack{n\le X\\n\ {\rm odd}}}\log d_n
       \gg X(\log X)^{\,3-3/(2\cdot15813)-1/(2\cdot251)} .
\]
The exponent is greater than \(2.99791\). The arguments use the two previously verified Gaussian packet characters. [Character at 193](abc_congruent_six_typical_odd_prime_factors.md) · [Character at 2011](abc_congruent_six_density_odd_depth.md)

## Exceptional indices

Use the character at 193. Its two labels \(u,v\) on Gaussian places are modulo 3. A place is available if \(u\ne0\); \(K(n)\) counts the available places over the distinct prime factors of \(n\), outside the finitely many excluded primes. At split rational primes the two conjugate labels are interchanged and the ordered pairs are uniform in \(\mathbf F_3^2\) when both places are counted. At inert primes the common label is uniform in \(\mathbf F_3\). All densities used below have fixed-class Mertens estimates. A rational prime is called available if at least one place is available, a set of density \((8/9+2/3)/2=7/9\). A split prime with one label zero and the other nonzero is called asymmetric, a set of density \((4/9)/2=2/9\).

Let \(Y=\exp((\log X)^{3/4})\). Require \(n\) to have an available prime \(q>Y\), at least two distinct asymmetric primes, \(K(n)\ge0.361\log\log X\), and \(\omega(n)\le4\log\log X\). Choose an available place above \(q\) and an asymmetric place \(\lambda_*\) above a different rational prime with \(u\ne0,v=0\). In the proof of the character estimate at 193 require both chosen places. Its subset-sum count in \(\mathbf F_3\) gives \(\gg2^{K(n)}\) negative symbols, of which at most \(4\omega(n)\) fail to supply an actual odd depth in \(B_n\). The first chosen place may lie over a split prime. Only its norm lower bound \(NI\ge q\) on the corresponding annihilator ideal is needed. Hasse gives each resulting prime \(p\ge(\sqrt q-1)^2\ge q/4\) for all sufficiently large \(X\). The asymmetric place ensures distinctness up to conjugation. Therefore \(\log d_n\gg 2^{K(n)}\log Y\) on this set.

For \(0\le f\le1\) multiplicative,
\[
 \sum_{m\le X} f(m)\ll\frac X{\log X}\exp\left(\sum_{p\le X}\frac{f(p)}p\right)
\]
with an absolute constant. To see this, expand \(\sum f(m)\log m\) by exact prime powers dividing \(m\), and drop the coprimality condition after separating \(f\). Since \(\sum_{p^a\le y}a\log p\ll y\), the result is \(O(X\sum_{b\le X}f(b)/b)\). Bound this harmonic sum by its Euler product and handle \(m\le\sqrt X\) trivially.

Apply the bound to the indicator excluding all available primes in \((Y,X]\). Their reciprocal sum is \((7/36)\log\log X+O(1)\). Apply it again to \(f(n)=(1/16)^{\#\{\text{asymmetric }p\mid n\}}\). Fewer than two such divisors gives \(f(n)\ge1/16\), hence costs \(O(X(\log X)^{-5/24})\). For the lower tail of \(K\), use \(f(n)=z^{K(n)}\), \(z=12/25\). With \(t=(1+2z)/3=49/75\), the prime average is \((t+t^2)/2\), because split labels are independent when averaged over the two places. Markov's inequality saves the power
\[
      1-\frac{t+t^2}{2}-0.361\log(25/12)>7/36 .
\]
Finally \(2^{\omega(n)}\le\tau(n)\) gives \(O(X(\log X)^{1-4\log2})\) for the upper tail of \(\omega\). These four estimates prove the claimed exception count.

## A lower bound for the arithmetic mean

Use the 2011 character and its notation \(M=15813\). Choose an odd constant \(D\), a product of distinct split rational primes supplying the three mandatory and seventeen reserved places of that proof, avoiding its finite excluded set. Restrict to \(n=Dmq\le X\), with \(q\) an available inert prime in \([X^{2/3},X^{3/4}]\) and \(m\) coprime to \(2D\). Such \(q\) is unique when \(X\) is sufficiently large. The proof yields at least \(c2^{K(m)}-4\omega(n)\) distinct odd-depth primes of size at least \((q-1)^2\), with an absolute \(c>0\). Here \(K\) denotes the 2011 count. Only the fixed prescribed places, the place above \(q\), and the available places in \(m\) need be used. Consequently one may sum the lower bound \(c'(\log X)2^{K(m)}-O((\log X)\omega(n))\) over these indices.

The prime average of \(2^{K(p)}-1\) is
\[
      \beta=\frac32(1-1/M)+\frac12(1-1/251).
\]
Indeed at a split prime the two conjugate exponent classes are related by \(u\mapsto503u\); divisibility by \(M\) is simultaneous. Thus \(K(p)=2\) at proportion \(1-1/M\) of split primes, zero at the others. For inert primes \(K(p)=1\) at proportion \(1-1/251\).

For fixed \(D\) one has
\[
       \sum_{\substack{m\le T\\(m,2D)=1}}2^{K(m)}
                          \gg_D T(\log T)^\beta.
\]
To verify this without an asymptotic mean-value theorem, write \(2^{K(m)}=\sum_{b\mid m}h(b)\), with \(h\ge0\) supported on squarefree integers and \(h(p)=2^{K(p)}-1\). For \(b\le\sqrt T\) coprime to \(2D\) there are \(\gg_D T/b\) eligible multiples. Set \(Z=T^\delta\) for a sufficiently small fixed \(\delta>0\). On subsets of primes \(p\le Z\) outside \(2D\), normalized weights \(h(b)/b\) give independent inclusions of probability \(h(p)/(p+h(p))\). The mean of \(\log b\) is \(O(\log Z)\), since \(h(p)\le3\). Choose \(\delta\) small enough that at least half the weight is on \(b\le\sqrt T\). The full product \(\prod_{p\le Z,\ p\nmid 2D}(1+h(p)/p)\asymp_D(\log T)^\beta\) by the fixed ray-class Mertens estimate, as claimed.

For the restricted \(q\), \(T=X/(Dq)\) has logarithm comparable to \(\log X\). The reciprocal sum of the available inert primes in the indicated interval is bounded below by a positive constant for large \(X\), by the prime number theorem in the fixed rational progressions. The error costs \(O(X\log X\log\log X)\), using \(\sum_{n\le X}\omega(n)\ll X\log\log X\). Summation gives the mean exponent \(1+\beta\).
