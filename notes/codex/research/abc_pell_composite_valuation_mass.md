# Composite moduli and the total mass of repeated Pell primes

Put \(g=(1+\sqrt2)^4\). Write \(W_n\) for the positive Pell integer carrying the geometric support of the primitive abc triple, \(T_n\) for its degree-482 nonlinear part, and \(F_n=|F_{11}(a_n,b_n)|\) for the degree-100 homogeneous full 11-torsion factor. At an integer \(A\) the excess is \(\log(A/\operatorname{rad}A)=\sum_p\sum_{2\le j\le v_p(A)}\log p\). The logarithmic ratio of the height to the radical of the whole triple equals this excess at \(W_n\) up to a bounded error. [Whole support and its relation to the triple](abc_pell_whole_trace.md)

## A uniform bound for any prescribed collection of prime powers

For **every** \(M\ge1\), set \(L=\log M\). Uniformly in \(N,M\),

\[
 \sum_{n\le N}\log\gcd(W_n,M)
       \ll L+N(1+\sqrt L).
                                                                  \tag{1}
\]

For \(T_n\) and \(F_n\), the stronger bound \(L+N(1+L^{1/3})\) holds. The constants depend only on the fixed sequence. One may also replace \(M\) at each index by an arbitrary \(M_n\), and use \(L=\log\operatorname{lcm}_{n\le N}(M_n)\). Thus the estimate applies even if the moduli are selected after observing all their prime divisors and valuations.

At a good odd prime put \(r_{p,j}=\operatorname{ord}_{p^j}(g)\) in the real quadratic ring. A layer is the power \(p^j\), of logarithmic weight \(\log p\). For each geometric target at a fixed place there is at most one class of index modulo \(r_{p,j}\) attaining it, so there are at most \(d(1+N/r_{p,j})\) occurrences through \(N\), with \(d\) fixed. This includes the two linear Pell factors, whose targets are a root of unity and a power of the unit up to sign. All omitted fixed primes together have \(O(N)\) incidence weight even with no valuation cutoff, by fixed-prime spacing. [Local periods and fixed-prime spacing](abc_cm_pell_lcm.md) · [The two linear factors](abc_pell_whole_lcm.md)

Let \(A(R)\) be the sum of \(\log p\) over visited layers dividing \(M\) with \(r_{p,j}\le R\). Then \(A(R)\le L\). For the whole support one also has \(A(R)\ll R^2\). Every such layer divides the absolute norm of \(g^r-1\) for some \(1\le r\le R\), and the product of these norms has logarithm \(O(R^2)\). For the nonlinear terms the stronger \(A(R)\ll R^{3/2}\) comes from reducing a multiplicatively independent target and \(g\) into the same cyclic group at a hit. A box of more than \(R\) monomials gives a relation modulo the layer with coefficients \(O(\sqrt R)\). Across all coefficient pairs and targets the nonzero numerator norms have log product \(O(R^{3/2})\). [Nonlinear layer count](abc_pell_lcm_sharp_rate.md)

If \(A(R)\ll\min(L,R^\alpha)\), partial summation gives
\[
       \sum_{\text{visited }p^j\mid M}\frac{\log p}{r_{p,j}}
              \ll 1+L^{1-1/\alpha}.
\]
Indeed integrate \(\min(L,t^\alpha)/t^2\) from 1 to infinity, splitting at \(\max(1,L^{1/\alpha})\). Summing the occurrence bound gives (1) and its nonlinear improvement. The same reasoning works for the opposite Pell orientation.

## A restriction on positive-density abc exceptions

Taking \(M=\prod_{p\le Y}p^J\) gives
\[
 \sum_{n\le N}\sum_{p\le Y}\min\{J,v_p(W_n)\}\log p
     \ll JY+N(1+\sqrt{JY}).                                       \tag{2}
\]
Thus, for \(JY=o(N^2)\), the full weighted mass through these moving depths is \(o(N^2)\). For every fixed \(\delta>0\), only \(o(N)\) indices in \([N,2N]\) have even \(\delta n\) mass from those layers. In particular when \(Y=N^{4/3}\), take \(J=\lfloor N^{2/3}/\omega(N)\rfloor\) for any slowly increasing \(\omega\to\infty\). Apart from \(o(N)\) indices, any excess of at least \(\delta n\) from primes at most \(Y\) has at least \(\delta n/2\) beyond this depth. This conclusion uses actual valuations, including at Pell-Wieferich primes.

A single cutoff can also include all primes and all exponents simultaneously. For \(X=N^2/(\log(2N)\omega(N))\), with \(X\to\infty\) and \(\omega(N)\to\infty\), take \(M=\lfloor X\rfloor!\). The condition \(p\,j\le X\) guarantees \(p^j\mid M\), and \(\log M\le X\log X=o(N^2)\). Hence
\[
   \sum_{n\le N}\sum_{\substack{1\le j\le v_p(W_n)\\p\,j\le X}}
                    \log p=o(N^2),                                \tag{3}
\]
where the inner sum ranges over primes and positive exponents. Equivalently on each dyadic block, outside \(o(N)\) indices, the contribution is below \(\delta n\) for each fixed \(\delta>0\). A termwise formulation holds on a set of natural density one with \(X(n)=n^2/(\log(2n)\omega(n))\) for any nondecreasing slowly growing \(\omega\to\infty\), by dyadic comparison and a decreasing tolerance. Consequently any positive-density set with a linear abc excess derives its linear contribution, after discarding a relative \(o(1)\) set of indices and an \(o(n)\) error in density, from the layers above this threshold. This leaves open large previously unseen prime squares and exceptionally large powers at smaller primes.

## The common order of a composite divisor at one index

There is a separate uniform estimate for the whole nonlinear part at a **single** index. With \(a_h\) defined by \((1+\sqrt2)^h=b_h+a_h\sqrt2\), one has

\[
                \sup_{n\ge1}\log\gcd(T_n,a_{2h})=o(\sqrt h).
                                                                  \tag{4}
\]

The same estimate holds for \(F_n\). If \(D_n\) is any divisor of \(T_n/\operatorname{rad}T_n\) of size at least \(\exp(\delta n)\) for some fixed \(\delta>0\), then
\[
                      \operatorname{ord}_{D_n}(g)/n^2\longrightarrow\infty
                                                                  \tag{5}
\]
as \(n\to\infty\). The order in (5) is taken in \((\mathbb Z[\sqrt2]/D_n)^\times\). In particular a common local period bounded by a fixed multiple of \(n^2\) can supply only \(o(n)\) nonlinear mass, regardless of the number of distinct prime divisors or their exponents.

Here are the inputs to (4). For fixed multiplicatively independent algebraic \(S\)-units \(g,u\), integral ideals \(I\) outside \(S\) obey
\[
       \sup_{|\langle g,u\bmod I\rangle|\le h} \log N I=o(\sqrt h).
\]
For an effective \(O(\sqrt h)\), use the norm of one element \(g^a u^b-1\) for a nonzero relation of length \(O(\sqrt h)\) modulo \(I\). For the little-oh, if \(\log N I\ge c\sqrt h\), the shortest vector in the relation lattice has length \(\gg_c\sqrt h\), by the same height bound. Since the lattice index is at most \(h\), a reduced basis then has both vectors of length \(O_c(\sqrt h)\). Apply the Corvaja–Zannier gcd theorem to their two monomials, both congruent to 1 mod \(I\). An exceptional translated subtorus forces a fixed nonzero integral combination of the basis vectors to equal a fixed exponent vector by multiplicative independence. This contradicts the shortest-vector bound. The proof works for \(S\)-units by omitting places in \(S\) in the gcd. [Detailed rank-two lattice proof on a different Pell family](hall_pell_joint_periods.md) · [Corvaja and Zannier](https://arxiv.org/abs/math/0311030)

At each good prime ideal over \(\gcd(T_n,a_{2h})\), assign its full exponent to the unique target \(u\) with \(g^n\equiv u\) at that precision. For each target multiply its assigned ideals. Then \(g^h\equiv1\) on this ideal, using \(g^h-1=2\sqrt2\,\epsilon^{2h}a_{2h}\). Also \(u\equiv g^n\) on the entire assigned ideal, even when it involves many rational primes. The generated subgroup is cyclic of order at most \(h\). Apply the preceding estimate separately to the finitely many targets. Fixed bad primes contribute \(O(1+\log h)\) through \(a_{2h}\) by ordinary order lifting. This proves (4). The identical argument applies modulo \(D_n\) with \(h=\operatorname{ord}_{D_n}(g)\), controlling its fixed bad primes through \(g^h-1\), and gives (5).

One can use (4) for several possible periods at the same single index. For any collection \(\mathcal H\) of positive integers, the total weight of layers of \(T_n\) whose orders divide some \(h\in\mathcal H\) is bounded by \(\sum_{h\in\mathcal H} O(\sqrt h+1)\), and the summands improve to \(o(\sqrt h)\) as \(h\to\infty\), uniformly in \(n\). At good odd primes the layer with order dividing \(h\) divides \(a_{2h}\). The finitely many omitted places for \(g^h-1\) are bounded by \(O(1+\log h)\). For example fix \(\eta>0\); layers of order at most \(n^{2-\eta}\) involving only primes at most \(\log n\) **in their order** have total weight \(o(n)\) at every index. To count the allowed orders put \(X=n^2\). For each \(\sigma>0\) Rankin's bound gives \(\#\{h\le X:P^+(h)\le\log n\}\le X^\sigma\prod_{p\le\log n}(1-p^{-\sigma})^{-1}=X^{\sigma+o(1)}\), since the log Euler product is \(O_\sigma(1+(\log n)^{1-\min(\sigma,1/2)})\). Taking \(\sigma\) arbitrarily small gives \(n^{o(1)}\) possible \(h\). The sum of their square roots is \(n^{1-\eta/2+o(1)}\). This argument applies also to the layers of the excess, indexed as the powers \(p^j\mid T_n/\operatorname{rad}T_n\).

## Depth inherent in the unit itself

For a good \(p\), put \(r_p=r_{p,1}\) and \(w_p=v_p(g^{r_p}-1)\), so \(r_{p,j}=r_p\) through depth \(w_p\), followed by \(r_p p^{j-w_p}\). For every \(Y=N^{4/3}(\log(2N))^{2/3}\) and \(J=o(N^2/Y)\), the nonlinear terms satisfy

\[
  \sum_{n\le N}\sum_{\substack{p\le Y\\p\ \mathrm{good}}}
       \min\{v_p(T_n),w_p+J\}\log p=o(N^2).                         \tag{6}
\]

This includes the complete depth \(w_p\), which need not be bounded. To see this put \(m_p=\max_{n\le N}\min\{w_p,v_p(T_n)\}\). At a maximizing target there is a subgroup generated by \(g,u\bmod p^{m_p}\) of order \(r_p\). The rank-two bound from (4) gives \(m_p\log p=o(\sqrt{r_p})\) uniformly as the orders grow. The order tends to infinity with \(p\), since a prime of bounded order divides one of a fixed finite set of norms. Since \(r_p\le p+1\), one obtains \(\sum_{p\le Y}m_p\log p=o(Y^{3/2}/\log Y)\) by the elementary prime count upper bound. The total contribution of the \(N/r_p\) terms in the occurrence bound for these layers is \(O(N\sqrt Y)\) by partial summation of the nonlinear \(R^{3/2}\) estimate through \(R=Y+1\). Together this is \(o(N^2)\) at the indicated \(Y\).

For the next \(J\) layers the contribution from the endpoint in \(1+N/r_{p,j}\) is \(O(JY)\). The geometric tail is \(O(N\sum_{p\le Y}\log p/[r_p(p-1)])=O(N\log(2Y))\), since \(r_p\gg\log p\) by the norm of \(g^{r_p}-1\). This proves (6); the omitted fixed bad primes add only \(O(N)\). It follows that a linear contribution from primes through this \(Y\) on a positive-density set of nonlinear terms must extend by nearly \(N^{2/3}/(\log N)^{2/3}\) layers beyond the depth of the generating unit, in the sense that \(J\) can be taken as this quantity divided by any slowly increasing function. The two linear factors of \(W_n\) satisfy (1)–(3) directly.
