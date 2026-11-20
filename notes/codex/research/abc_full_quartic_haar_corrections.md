# Primitive parity and the distribution of ordinary lifts

For odd \(n>0\), let \(B_n\) be the positive square root of the reduced denominator of \(x(nG)\) on \(y^2=x^3-36x\), with \(G=(-3,9)\). Write \(d_n=\operatorname{sf}(B_n)\) for the product of the primes of odd valuation. For a good prime \(p\) of odd reduction order \(r_p\), write \(e_p=v_p(B_{r_p})\). Such \(p\) satisfy \(p>r_p>1\). All primes of \(B_n\) are good. Write \(H=\widehat h(G)\). We use the denominator bounds and formal group formulas proved in the [quartic parametrization](abc_full_quartic_signature.md).

## The integer correction

Put \(g(n)=\gcd(n,B_n)\) and \(a(r)=\prod_{r_p=r,\ e_p\ {\rm odd}}p\). One has
\[
 g(n)=\prod_{r_p\mid n}p^{v_p(n)},\qquad
 \left|\log d_n-\sum_{r\mid n}\log a(r)\right|\le\log g(n).
\]
Indeed at \(r_p\mid n\) the exponent is \(e_p+v_p(n)\), since \(p\nmid r_p\). In particular all these parity comparisons are equalities prime by prime when \(g(n)=1\).

Uniformly for real \(Y\ge3\) and integral \(X\ge1\), the proportion of odd \(n\le X\) with some \(p>Y\) dividing \(g(n)\) is
\[
                         O\big(Y^{-1/3}/\log Y\big).
\]
For a single \(p\), the divisibility condition is \(p r_p\mid n\), which has at most \(X/(p r_p)\) solutions. On \(P<p\le2P\), the number with \(r_p=r\) is \(O(r^2/\log P)\) by \(\log B_r\ll r^2\). For \(r\le P^{1/3}\) the contribution to \(\sum1/(p r_p)\) is therefore \(O(P^{-1}\sum_{r\le P^{1/3}}r/\log P)\). For larger ranks apply the ordinary prime counting upper bound, obtaining the same \(O(P^{-1/3}/\log P)\). Sum over dyadic \(P\).

The full distribution of \(g(n)\), under uniform sampling of odd indices through \(X\), converges in total variation to that obtained by sampling the local index in the profinite odd integers. Indeed first discard \(p>Y\) by the uniform bound, then cap the finitely many valuations at \(A\) with error \(O(\sum_{p\le Y} p^{-A})\). The result is a finite periodic law. The same argument applies to the vector of signs of the individual prime parity corrections.

Every attained value \(k=g(m)\) has positive probability. At primes dividing \(m\), impose the same valuations of \(n\) and reduction-order divisibilities as for \(m\). One fixed congruence \(n\equiv m\pmod{M}\) suffices, with \(2m\operatorname{rad}(m)\mid M\) and \(r_p\mid M\) for all good \(p\mid m\). Primes dividing \(M\) but not \(m\) are excluded from \(n\). At the primes \(p\le Y\) outside \(M\), exclude \(p\mid n\). These conditions have density \(\gg_m1/\log Y\) by the Chinese remainder theorem and Mertens' product. The global \(p>Y\) tail is smaller for sufficiently large fixed \(Y\). Taking \(m=1\) proves positivity for complete absence of ordinary lifts. For an odd \(k\) supported on primes of odd order, set \(l(k)=\operatorname{lcm}(k,\{r_p:p\mid k\})\), including \(l(1)=1\). Then \(k\) is attainable exactly when \(g(l(k))=k\), by denominator divisibility under \(l(k)\mid m\).

The real point \(nG\) is independent of this profinite law in the limiting joint distribution. Indeed the odd multiples in every fixed nonempty residue class are Haar equidistributed on the same real component, since a nonzero even multiple of \(G\) has infinite order on the identity circle. Finite periodic approximation in total variation gives the assertion for the full correction. The same holds jointly with \(J_2(n)/n^2\), since its prime products converge uniformly after truncation. For example, any achievable \(k\) occurs with positive natural density jointly with any real open arc of the odd component.

## Moments

For every fixed integer \(j\ge1\), with the same uniform in \(X\) meaning of the expectation,
\[
 {\mathbb E}\big[(\log g(n))^j\,{\bf1}_{\{\exists p>Y:p\mid g(n)\}}\big]
                 \ll_j Y^{-1/3}(\log Y)^{j-1}.
\]
Partition the event by the largest \(p\mid g(n)\) and write \(n=p r_p t\). The other primes of \(g(n)\) are at most \(p\), whence
\(\log g(n)\le\log(p r_p)+S_p(t)\), with
\(S_p(t)=\sum_{q\le p}v_q(t)\log q\). Uniformly for \(t\le T\) the mean of \(\exp(S_p(t)/\log(2p))\) is bounded by an absolute constant. To see this write the multiplicative weight as \(1*h\), where \(h\ge0\), and use \(\lfloor T/d\rfloor\le T/d\). The resulting product is
\[
 \prod_{q\le p}\frac{1-q^{-1}}{1-q^{-1+1/\log(2p)}}\ll1.
\]
Its logarithm is \(O(\sum_{q\le p}\log q/(q\log(2p)))=O(1)\), using \(q^{1/\log(2p)}\le e\) and treating the fixed small primes in the same bound. Thus the conditional \(j\)-th moment is \(O_j((\log p)^j)\), even if the largest-prime restriction on \(t\) is dropped. Summation over \(p>Y\) with the preceding dyadic estimate proves the claim. In particular all moments of \(\log g(n)\) have finite limits, by the same truncation and uniform integrability.

There is also a uniform stretched-exponential upper tail. For every \(c<1/\sqrt6\) and all sufficiently large \(t\),
\[
 \mathbb P_{n\le X,\ n\ {\rm odd}}\{\log g(n)\ge t\}
                  \ll \exp(-c\sqrt{t\log t}).
\]
Take \(\log Y=\sqrt{(3/2)t\log t}\). An active \(p>Y\) costs \(O(Y^{-1/3}/\log Y)\). Otherwise \(\log g(n)\le S_Y(n)\). Put \(s=((\log t)/2-\log\log t)/\log Y\). The preceding Euler-product argument for \(e^{sS_Y}\), with \(s<1/4\), bounds its log mean from above by \(O(1+\sum_{p\le Y}(p^s-1)/p)\). Since \(p^s-1\le sY^s\log p\), this is \(O(1+(s\log Y)e^{s\log Y})=O(\sqrt t)\). Markov's inequality now has exponent \(-st+O(\sqrt t)=-(1/\sqrt6+o(1))\sqrt{t\log t}\). The large-prime contribution has the same exponent. In particular for every fixed \(\eta>0\), outside \(O_\eta(X\exp(-c_\eta\sqrt{\log X\log\log X}))\) indices the full and primitive parity products differ by a factor between \(X^{-\eta}\) and \(X^\eta\).

## Contributions at one reduction order

Define \(L(r)=\sum_{r_p=r}e_p\log p\), \(g_0(r)=(L(r)-\log a(r))/r^2\), and \(f_0(n)=\log(B_n/d_n)/n^2\). The functions are bounded and nonnegative. The full logarithm adds the ordinary lifting contribution \(\log g(n)\). Comparing the square parts prime by prime therefore gives
\[
 0\le f_0(n)-\sum_{j\mid n}\frac{g_0(n/j)}{j^2}
             \le \frac{2\log g(n)}{n^2}.
\]
In particular \(g_0(n)\le f_0(n)\), and for each \(\epsilon>0\) a sufficiently large \(n\) with \(f_0(n)>\epsilon\) must have a divisor \(j\le C/\epsilon\) with \(g_0(n/j)>\epsilon/(3\zeta(2))\). Bound the large-\(j\) tail by \(\sup g_0\sum_{j>J}j^{-2}\); the finitely many smaller terms are bounded by the maximum times \(\zeta(2)\). Hence for adjusted fixed thresholds, a density-zero bound, a power saving, or a logarithmic saving for the failure of almost-squarefreeness is equivalent at primitive and full odd indices. No independent prime-depth assumption enters this equivalence.

If the Cesàro average over odd indices exists for either \(f_0\) or \(g_0\), both averages exist and satisfy \({\mathbb E} f_0=(7/8)\zeta(3){\mathbb E}g_0\). Average the dilation sum, observing that a fixed odd coindex \(j\) gives the factor \(1/j^3\). The converse follows by Möbius inversion with \(\mu(j)/j^2\). Dominated convergence applies to both series; the bounded errors tending to zero stay negligible under inversion. The analogous identity holds for \(\log d_n/n^2\) and \(\log a(n)/n^2\). The unconditional total primitive mass is \(L(r)=HJ_2(r)+o(r^2)\). For each odd \(j\), its mean normalized share \(L(n/j)/(Hn^2)\) on all odd \(n\), set to zero when \(j\nmid n\), is
\[
                   \frac{8}{7\zeta(3)j^3}.
\]
Indeed \(\mathbb E[J_2(n)/n^2]=\prod_{p\ {\rm odd}}(1-p^{-3})=8/(7\zeta(3))\). In particular the top order \(r=n\) has mean share \(8/(7\zeta(3))\) and individual share at least \(8/\pi^2+o(1)\). If \(\log a(n)=o(n^2)\) on an infinite subsequence, one gets \(\log d_n/\log B_n\le 1-8/\pi^2+o(1)\) there. Since \(\operatorname{rad}(B_n)\le\sqrt{B_n d_n}\) and the other three arms each have logarithm \(Hn^2+o(n^2)\), the associated primitive abc triples have \(\liminf \log C/\log R\ge(1-1/\pi^2)^{-1}\) on that subsequence.
