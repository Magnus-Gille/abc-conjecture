# A single trace polynomial for the whole radical on the Pell sequence

Let \(\epsilon=1+\sqrt2,\ b_n+a_n\sqrt2=\epsilon^n\), and let \(A_n+B_n=C_n\) be the positive primitive triples from the [degree-968 family](abc_cm_pell_whole_triple.md) at \((a_n,b_n)\). Write \(S_n=b_{2n}\), \(D(m)=\log(|m|/\operatorname{rad}|m|)\) for nonzero integers, and \(d_n=\log(C_n/\operatorname{rad}(A_nB_nC_n))\). There is an explicit squarefree integer polynomial \(P\) of degree 967 such that, uniformly for \(n\ge1\),
\[
     d_n+d_{-n}=D(P(S_n))+D(S_n)+O(1).
\]
In particular the two orientations of the Pell family produce a fixed-exponent counterexample sequence **if and only if** \(D(P(S_n))\ge\delta n\) infinitely often for some fixed positive \(\delta\). This criterion covers all three entries and every prime. It neither asserts that this happens nor reduces unrestricted rational abc to this single sequence. [Polynomial constructor and exact checks](abc_pell_whole_trace.py)

## Constructing the polynomial

On \(y^2=x^3+16x^2+32x\) let \(N(x)/Q(x)=x([11]T)\) for \(x=x(T)\), using the integral division-polynomial numerator \(\phi_{11}\) and denominator \(\psi_{11}^2\). Write \(h(x)=x^2+16x+32\). Take the primitive squarefree part of
\[
 QN(N+16Q)(N+8Q)(N^2+16NQ+32Q^2)
\]
and divide by \(h(x)\) to obtain \(u(x)\) of degree 483. The finite roots before removing \(h\), together with infinity, are exactly the preimages of \(0,1,\infty\) for \(h(N/Q)^2/1024\). The two removed roots pull back to the norm \(b^2-2a^2=\pm1\) on our Pell orbit. The following polynomial computations are exact: the finite squarefree part has degree 485, \(u(-8)\ne0\), \(\gcd(u,h)=1\), and \(\gcd(u(x),u(-16-x))=1\).

Put \(s=S_n\) and \(t=a_{2n}\), so that \(s^2-2t^2=1\). The two initial abscissas are \(x_\pm=-8(s\pm t)/s\); thus \(x_-=-16-x_+\). Define \(U_\pm=s^{483}u(x_\pm)\). The integer products \(sU_+\) and \(sU_-\) contain precisely the geometric prime support of their respective triples, up to fixed primes. Indeed the point at infinity contributes \(s\), the removed pair contributes a unit, and the other factors are the homogenization of \(u\). On primitive parameter pairs a numerical gcd from the rational map is bounded by a fixed resultant, so the radicals differ from the indicated ones by at most a fixed factor. The ratio \(t/s\) tends to \(1/\sqrt2\) as \(n\to+\infty\); neither limiting abscissa is a zero of \(u\). Consequently \(|sU_\pm|\asymp s^{484}\asymp C_{\pm n}\), and \(d_{\pm n}=D(sU_\pm)+O(1)\).

The numbers \(s,U_+,U_-\) have pairwise bounded gcd. For \(s\) versus \(U_\pm\) this follows from \((s,t)=1\), \(s\) odd, and the fixed leading coefficient of \(u\). For the pair \(U_+,U_-\) it follows from the nonzero resultant under reflection and the primitive homogeneous abscissa pair \((-8(s+t),s)\). The even polynomial \(u(z-8)u(-z-8)\) is \(V(z^2)\) with \(\deg V=483\). Now set
\[
 P(s)=s^{967} V\!\left(32(1-s^{-2})\right)=sU_+U_-.
\]
The right-hand product identity applies at the indicated Pell values. As a polynomial the expression is integral, squarefree over \(\mathbb Q\) and of degree 967, as is also checked by the verifier. The term \(s\) occurs just once. Bounded gcd gives the claimed sum of logarithmic defects since \(D(xy)=D(x)+D(y)+\log\operatorname{rad}(\gcd(x,y))\). Also \(D(S_n)\le D(P(S_n))\), each \(d_{\pm n}\) is bounded below by a fixed constant, and \(\log C_{\pm n}=968n\log\epsilon+O(1)\). These facts prove both directions of the criterion.

## The local periods that can contribute

For odd \(p\), let \(r_{p,j}\) be the order of \(g=\epsilon^4\) modulo \(p^j\) in \(\mathbb Z[\sqrt2]\). For all \(R\ge2\) and all positive \(n\), the total valuation copies of \(sU_+\) with period at most \(R\) satisfy
\[
 \sum_{\substack{p^j\mid sU_+,\,j\ge1\\ r_{p,j}\le R}}\log p
   \ll R^{3/2}+R\{\tau(2n)+\tau(2n+1)\}+\log(2R).
\]
Here the finitely many primes of bad reduction may be omitted, or included with the last term by the fixed-prime order-lifting law. The analogous bound for the opposite orientation uses \(2n-1\). Thus period at most \(n^{2/3}/\omega(n)\), for any \(\omega(n)\to\infty\), accounts for \(o(n)\) at **every** index. This is a restriction on the order of a given power \(p^j\), distinct from a size restriction on its underlying prime.

Here are the algebraic checks needed for this bound. The linear factor \(x\) of \(u\) contributes \(s+t=a_{2n+1}\), up to powers of fixed constants in the support. Its order divides \(2n+1\): \(a_{2n+1}\equiv0\bmod p^j\) makes \(\epsilon^{2n+1}\) scalar of norm \(-1\), so \(g^{2n+1}\equiv1\bmod p^j\). Similarly \(p^j\mid s\) implies \(g^n\equiv-1\bmod p^j\). For \(r=r_{p,j}\) one has \(p^j\mid a_{2r}\) since \(g^r-1=2\sqrt2\,\epsilon^{2r}a_{2r}\). Summing \(\log a_{2r}=O(r)\) over divisors \(r\le R\) of the indicated integers bounds all copies at the two linear-recurrence factors; copying a prime up to its highest exponent at a given period costs at most that full logarithm.

For the remaining 482 roots, substitute \(x=(\theta_- Z+\theta_+)/(Z+1)\), where \(\theta_\pm=-8\pm4\sqrt2\), so \(Z=g^n\). Every transformed root \(\beta\) is multiplicatively independent of \(g\), modulo roots of unity. To check this, factor over \(\mathbb Q(\sqrt2)\) and apply the substitution to each irreducible factor. If \(\beta^a g^b\) were a root of unity with \(a\ne0\), all conjugates over \(\mathbb Q(\sqrt2)\) would have the same complex absolute value \(r\). A real polynomial \(\sum c_j Z^j\) of degree \(d\) whose nonzero roots all have that absolute value is invariant up to a scalar under \(Z\mapsto r^2/Z\); this gives
\[
        c_2 c_0 c_{d-1}^2-c_{d-2} c_d c_1^2=0.
\]
The verifier factors in characteristic zero, then evaluates this expression modulo 1009 at one square root of 2. For the four degree-ten factors the nonzero residues are \(80,103,733,880\); for the four degree-fifty factors they are \(156,465,544,554\); and for the two degree-121 factors they are \(702,821\). Thus there are no additional multiplicatively dependent targets. This calculation concerns the whole support, which contains more roots than the full-annihilator form \(F_{11}\).

At a hit of depth \(j\) outside finitely many exceptional primes, \(\beta\equiv g^n\bmod p^j\) at a place of a fixed splitting field. In particular if \(r_{p,j}\le R\), the group generated by \(g,\beta\) at that precision has at most \(R\) elements. Comparing the \((1+\lfloor\sqrt R\rfloor)^2>R\) products \(g^i\beta^k\), \(0\le i,k\le\lfloor\sqrt R\rfloor\), gives a nonzero \((i',k')\) in the symmetric box with \(g^{i'}\beta^{k'}-1\equiv0\bmod p^j\). The difference is nonzero globally by independence. The product of its absolute numerator norms over all such pairs and the finitely many targets has logarithm \(O(R^{3/2})\) by the height bound for each pair. At every rational prime the product captures its highest qualifying depth, even across different indices. This proves the nonlinear part of the estimate. At fixed bad primes the number of allowed depth levels is \(O_p(1+\log R)\) by binomial lifting for the nontorsion \(g\); application at 2 follows after taking a fixed power inside its logarithm disk.

## How much can come from lifting at an already visited root

For the full rank-eleven form \(F_n\), and more generally for the nonlinear factors of \(u\) above, a stronger estimate applies specifically to ordinary increases in valuation. At a good odd prime put \(r_p=r_{p,1}\) and \(s_p=v_p(g^{r_p}-1)\) at a place above \(p\). The two places in the split case agree since conjugation inverts \(g\). Binomial lifting gives \(r_{p,j}=r_p p^{\max(0,j-s_p)}\). If \(j>s_p\) and \(r_{p,j}<n\), a hit at index \(n\) has already occurred at the same target and precision at the positive index \(n-r_{p,j}\). The total weight of *all* possible such levels for \(1\le n\le N\), counting each \((p,j)\) just once, is
\[
                         O(N^{3/5}).
\]
For \(p\le N^{3/5}\), the number of possible levels \(j>s_p\) is at most \(\log N/\log p\). By the elementary prime-counting upper bound their weight is \(O(N^{3/5})\). At \(p>N^{3/5}\) there can be just one such level, \(j=s_p+1\), and \(r_p<N^{2/5}\). The short-relation bound proved above at depth one gives total weight \(O((N^{2/5})^{3/2})\) for these primes over all the nonlinear targets. The finitely many fixed bad primes may be omitted.

Thus, at an index with linear logarithmic excess from nonlinear factors, all but \(O(n^{3/5})\) of the excess outside the fixed bad primes comes from two possibilities. A level \(2\le j\le s_p\) forces \(g^{r_p}\equiv\beta^{r_p}\equiv1\bmod p^j\) at the target place. A level \(j>s_p\) with \(r_{p,j}\ge n\) is a first visit at that precision for its particular target among positive indices. A different target can have appeared earlier. The estimate leaves both possibilities open. Fixed primes separately contribute \(O(\log n)\) to the nonlinear factors by fixed-prime logarithmic-form estimates. [Local height bounds](abc_pell_full11_small_prime_mass.md)

## Mean distinct prime contribution below the quadratic scale

For \(X=o(N^2)\), the mean of
\[
 \frac1n\sum_{\substack{p\mid S_n U_+\\p\le X}}\log p
\]
over \(N\le n<2N\) tends to zero. This estimate counts each prime once. At a good \(p\), at most 484 classes of \(n\bmod r_{p,1}\) hit the necessary targets: one from the pole and 483 from \(u\). For a rough bound on all primes with \(r_{p,1}\le R\), take the product of the \(a_{2r}\) for \(1\le r\le R\), whose logarithm is \(O(R^2)\). Thus, using also \(\sum_{p\le X}\log p=O(X)\), partial summation split at \(R=\sqrt X\) gives \(\sum_{p\le X}\log p/r_{p,1}=O(\sqrt X)\). Counting visits to each class bounds the unnormalized block mean by \(O(\sqrt X+X/N)\). Fixed bad primes count only \(O(1)\) per index for this distinct-prime estimate. The opposite orientation obeys the same bound.

Consequently, a positive-density subsequence on which the whole geometric support is \(o(n^2)\)-smooth would already force unbounded abc quality along a further subsequence. No such smoothness is established. The estimates leave open a sparse set of exceptional indices and the contribution of prime powers of large local order.
