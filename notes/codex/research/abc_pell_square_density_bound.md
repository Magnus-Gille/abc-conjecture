# An explicit lower bound on the density of indices avoiding ordinary squares

Write \(F_n=|F_{11}(a_n,b_n)|\) for the rank-eleven Pell value, and \(g=(1+\sqrt2)^4\). For a good odd prime put \(r_p=\operatorname{ord}_p(g)\) in the quadratic torus and \(e_p=v_p(g^{r_p}-1)\), normalized by \(v_p(p)=1\). The value is independent of the place above \(p\). For more than **99.95%** of positive indices, in the sense of limiting natural density, every good prime \(p\le n\log n/\log\log n\) satisfies \(v_p(F_n)\le e_p\). For ordinary primes \(e_p=1\), so these indices avoid their squares throughout this range. A square can survive at an exceptional prime with \(e_p>1\), or at a prime above the cutoff. [Local roots, moving cutoff and existence of the density](abc_cm_pell_index_square_sieve.md)

Let \(h_p\le50\) be the number of targets the orbit actually visits modulo \(p\). The local density of valuations exceeding \(e_p\) is at most \(h_p/(p r_p)\) by order lifting. Summing these upper bounds and the endpoint error \(50\pi(X)/N\) at \(X=N\log N/\log\log N\) gives the limiting inequality. The cutoff at each index \(n\le N\) is bounded by \(X\), apart from immaterial small indices. The argument requires no independence between primes.

The sum through \(10^7\) is at most \(2981795442179/10^{16}\). This uses the complete period census, with the ratio of hit classes to period unchanged on passing from the projective generator to its square \(g\). For \(10^7<p\le10^9\) the upper bound is \(314508201136/10^{16}\). To verify it, enumerate all 501,672 compatible primes in that interval by the norm representation \(p=(1+22h)^2+242b^2\), \(b>0\). If \(r_p\le4000\), then \(p\mid a_{2r_p}\), since \(g^r-1=2\sqrt2(1+\sqrt2)^{2r}a_{2r}\). An integer product gcd identifies all 41 such possibilities, and modular powering gives their exact orders. At the other candidates use \(50/(4000p)\). The sums round each term up to the next multiple of \(10^{-16}\). [Finite certificate](abc_pell_square_density_bound.py) · [Prime support and census](abc_pell11_early_squares.md)

For the infinite tail let \(T\ge10^9\). There are at most \(0.0021T\) compatible primes in \([T,2T)\). Here is an elementary count. In the coordinates \(X=1+22h,\ Y=\sqrt{242}\,b\) the points lie in the circular annulus of radii \(\sqrt T,\sqrt{2T}\). Modulo 3 the norm equals \(X^2-b^2\), so just four pairs \((h,b)\bmod3\) are admissible. In each class the centered rectangular lattice cells have area \(9\cdot22\sqrt{242}\) and half-diagonal \(\rho=(3/2)\sqrt{22^2+242}<41\). Their union for centers in the annulus lies between radii \(\sqrt T-\rho\) and \(\sqrt{2T}+\rho\). Count both signs of \(b\), then divide by two. The resulting upper bound divided by \(T\) is
\[
  \frac{4\pi}{9\cdot44\sqrt{242}}
       \left(1+\frac{2(\sqrt2+1)\rho}{\sqrt T}\right)<0.0021.
\]
Multiple representations can only increase this upper bound.

For each \(r\), the number of primes in the same interval of order \(r\) is at most \(\log(a_{2r})/\log T\le 1.77r/\log T\). Summing \(1/r_p\) for \(r_p\le R\), and using the annulus count for the remaining orders, shows that the contribution of the interval to the density sum is at most
\[
  \frac{50}{T}\left(\frac{1.77R}{\log T}+\frac{0.0021T}{R}\right)
  =\frac{100\sqrt{1.77\cdot0.0021}}{\sqrt{T\log T}}
\]
at the minimizing real \(R\). Sum over \(T=2^k10^9\), using \(\log T>20\). The infinite tail is smaller than \(0.000148\). With the two finite bounds the total is less than \(0.000478\), which proves the claim. This density controls a single explicit factor of the triples. It leaves sparse exceptional indices open.

## An average bound for the full support, including exceptional lifting

For the whole positive geometric support \(W_n\) of the associated triple, every cutoff \(Y=Y(N)\) with \(\pi(Y)=o(N)\) satisfies
\[
 \sum_{n\le N}\ \sum_{p\le Y}v_p(W_n)\log p=o(N^2).
\]
This counts every copy, including at Pell-Wieferich primes. In particular, with \(Y(n)=n\log n/\log\log n\), these primes contribute \(o(n)\) on a set of indices of natural density one. The same statement holds for the negative orientation.

To prove it, fix any good prime, write \(r=\operatorname{ord}_p(g)\) and \(e=v_p(g^r-1)\). A good reduction has at most 484 targets, including the two elementary Pell factors. The index period at depth \(j\) is \(r_j=r p^{\max(0,j-e)}\), so at most \(484(1+N/r_j)\) indices attain that depth. If \(V=\max_{n\le N}v_p(W_n)\), then \(V\log p=O(N)\) by the ordinary size bound \(W_n=\exp(O(n))\). Also \(e\log p\le\log(a_{2r})=O(r)\) from the order witness above. Hence the total sum of valuations at this one prime, weighted by \(\log p\), is at most
\[
 484\log p\left(V+\frac Nr\left(e+\frac{1}{p-1}\right)\right)=O(N)
\]
uniformly in the prime. The representation by targets at high precision follows by separability and the fixed projective change of variable. For the pole use \(g^n=-1\) directly. At each of the finitely many excluded primes the contribution is \(O(N\log(2N))\) by fixed-prime logarithmic forms, or by local spacing. Summing over \(p\le Y\) and applying Markov's inequality on dyadic blocks gives the assertion. [Full support and the two elementary factors](abc_pell_whole_lcm.md) · [Local factorization](abc_pell_whole_trace.md)
