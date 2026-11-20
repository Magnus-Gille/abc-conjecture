# Pell–Wieferich primes and exponential radical loss at squarefree trace indices

Write \(\epsilon=1+\sqrt2,\ \epsilon'=1-\sqrt2,\ \epsilon^n=b_n+a_n\sqrt2\), and \(S_n=b_{2n}\). Set \(D(m)=\log(m/\operatorname{rad}m)\) for positive integers \(m\). For each odd prime \(p\), let \(r_p=\min\{r\ge1:p\mid a_r\}\) and \(w_p=v_p(a_{r_p})\). A Pell–Wieferich prime is one with \(w_p\ge2\), equivalently \(p^2\mid a_{p-(2/p)}\). Define
\[
 W(d)=\sum_{r_p=4d}(w_p-1)\log p,\qquad
 H_d=\left|\Phi_{4d}(\epsilon,\epsilon')\right|
\]
using the homogeneous cyclotomic polynomial.

For every \(n\ge1\) there are exact identities
\[
   D(S_n)=\log\gcd(n,S_n)+\sum_{\substack{d\mid n\\n/d\ {\rm odd}}}W(d),
        \qquad W(d)=D(H_d).                                      \tag{1}
\]
Thus at squarefree indices only Pell–Wieferich primes with \(r_p/4\) integral and squarefree can supply more than the aggregate lifting term \(\log n\).

The following equivalences hold for positive **upper natural density**, and separately for positive **lower natural density**. Thresholds may change from one assertion to another.

1. \(D(S_n)\ge\delta n\) on a set of squarefree \(n\) of positive density in the indicated sense, for some \(\delta>0\).
2. \(D(H_d)\ge\delta' d\) on a set of squarefree \(d\) of positive density in that same sense.
3. For some \(c,\delta''>0\), on a set of squarefree \(d\) of positive density in that sense one has
   \[
     \sum_{\substack{r_p=4d,\ w_p\ge2\\
                 p(w_p-1)>c d^2/\log(2d)}} (w_p-1)\log p\ \ge\ \delta''d .
   \]
   One may additionally require \(p>d\exp(\gamma\log d/\log\log d)\) for any fixed \(0<\gamma<1/103.8\). For fixed \(\eta>0\) one may instead use the cutoff \(p\,V_\eta(w_p-1)>c d^2\), where
   \(V_\eta(t)=t(1+\log t)[1+\log(1+\log t)]^{1+\eta}\) for \(t\ge1\).

In the primitive sum the same prime never serves two distinct \(d\). It is \(1\bmod 8d\) or \(-1\bmod 4d\); the negative class can occur only for odd \(d\), at primes \(3\bmod8\). All three assertions remain equivalent when restricted throughout to odd squarefree indices or throughout to even squarefree indices. An affirmative conclusion in (1) of the list would disprove rational abc already in the elementary primitive triples \(1+2a_{2n}^2=S_n^2\). Indeed \(\gcd(S_n,a_{2n})=1\), \(a_{2n}\asymp S_n\), and \(S_n^2/\operatorname{rad}(2a_{2n}S_n)\gg \exp D(S_n)\). The existence of a positive-density set, or even of a sparse sequence with linear \(D(S_n)\), remains open.

## Exact first occurrences

For odd \(p\), \(r_p\) is the order of \(g=\epsilon/\epsilon'=-\epsilon^2\) in the residue field of \(\mathbb Q(\sqrt2)\), independent of the choice of a split place. It divides \(p-(2/p)\), hence \(p\nmid r_p\). Binomial lifting gives \(v_p(a_m)=w_p+v_p(m)\) if \(r_p\mid m\) and zero otherwise. Since \(a_{4n}=2a_{2n}S_n\), an odd prime belongs to \(S_n\) precisely when \(r_p\mid4n,\ r_p\nmid2n\), or equivalently \(r_p=4d,\ d\mid n,\ n/d\) odd. Then \(v_p(S_n)=w_p+v_p(n)\). Evenness never contributes since \(S_n\) is odd. At primes of \(S_n\) the valuation in \(\gcd(n,S_n)\) is exactly \(v_p(n)\). This proves the first formula in (1).

At split \(p\) with \(4\mid r_p\), necessarily \(p\equiv1\bmod8\): for \(p\equiv7\bmod8\), \(p-1\) is not divisible by 4. In the first case \(g=-\epsilon^2\) is a square modulo \(p\), so \(4d\mid(p-1)/2\). In the inert case \(4\mid p+1\) forces \(p\equiv3\bmod8\), and \(v_2(p+1)=2\), so \(d\) is odd.

For \(t=4d\), Möbius inversion on \(a_m\) computes \(v_p(|\Phi_t(\epsilon,\epsilon')|)\). It vanishes if \(r_p\nmid t\); it equals \(w_p\) if \(t=r_p\). For \(t=r_pm,\ m>1\), it is \(\sum_{h\mid m}\mu(m/h)v_p(h)\), equal to 1 when \(m\) is a positive power of \(p\) and zero otherwise. At 2 one has \(v_2(a_m)=v_2(m)\), by doubling and the oddness of all \(b_j\). This valuation also gives at most one in the cyclotomic factor. Thus every imprimitive prime in \(H_d\) occurs once, proving its identity in (1). Moreover
\[
      0\le W(d)\le \log H_d=\varphi(4d)\log\epsilon+O(1)\ll d.
\]
In the Möbius sum for the logarithm, the Binet error is bounded uniformly by the convergent sum \(\sum_{m\ge1}|\log(1-(\epsilon'/\epsilon)^m)|\). This derivation uses the full valuations and needs no primitive-divisor existence theorem.

## Upper, lower and logarithmic density

Let \(\mathcal S\) be the squarefree integers, optionally of one fixed parity, and write
\[
 A_X=X^{-1}\sum_{\substack{n\le X\\ n\in\mathcal S}}D(S_n)/n,\qquad
 B_X=X^{-1}\sum_{\substack{d\le X\\ d\in\mathcal S}}W(d)/d .
\]
The normalization is by all integers; squarefree integers of either parity have positive natural density. Both means are bounded. Since nonnegative bounded values exceed a fixed positive threshold on a positive-upper-density set exactly when their upper mean is positive, and likewise for lower density, it suffices to compare means. The diagonal \(d=n\) gives \(B_X\le A_X\). In (1) write \(n=kd\); here \(k\) is odd and squarefree, \((k,d)=1\), and \(d\) retains the parity of \(n\). Dropping coprimality gives
\[
 A_X\le o(1)+\sum_{\substack{k\le X\\ k\ {\rm odd,\ squarefree}}}k^{-2}B_{X/k}.
\]
In particular
\[
 \limsup B_X\ \le\ \limsup A_X\ \le\
 \frac{12}{\pi^2}\limsup B_X,\qquad
 \frac{12}{\pi^2}=\prod_{q>2}(1+q^{-2}) .
\]
For lower-density positivity, \(B_{X/k}\le k B_X\) by monotonicity of the unnormalized sum. Truncating at fixed \(K\) gives \(A_X\ll B_X(1+\log K)+1/K+o(1)\). A subsequence with \(B_X\to0\) consequently has \(A_X\to0\), which proves the lower-density equivalence too.

There is a more precise identity for the logarithmic mean, with bounded absolute error for all \(X\ge2\):
\[
 \sum_{\substack{n\le X\\n\in\mathcal S}}\frac{D(S_n)}{n^2}
   =\frac{12}{\pi^2}
      \sum_{\substack{d\le X\\d\in\mathcal S}}\frac{W(d)}{d^2}
         \prod_{\substack{q\mid d\\q>2}}(1+q^{-2})^{-1}
       +O(1).                                                     \tag{2}
\]
Indeed summing over \(k\) coprime to \(2d\) produces this Euler product. Its tail \(k>X/d\) is \(O(d/X)\); after multiplication by \(W(d)/d^2\) the total cost is \(O(1)\). The lifting term costs at most \(\sum_n(\log n)/n^2\). Substitution of the exact prime sum defining \(W(d)\) gives the individual Wieferich-prime criterion for positive upper or lower logarithmic density. In particular convergence of \(\sum_{p:\,w_p\ge2,\ r_p=4d,\ d\in\mathcal S}(w_p-1)\log p/d^2\) would make the reciprocal sum of all squarefree exceptional indices with \(D(S_n)\ge\delta n\) finite for each \(\delta>0\).

One can also give a frequency bound using only the *number* of Pell–Wieferich primes. Let \(E(x)\) count those \(p\le x\) with \(r_p=4d,\ d\in\mathcal S\). Put \(h=\log\epsilon\) and \(M=\min(X,E(e^{hX}))\). For \(X\ge2,\ \delta>0\),
\[
 \#\{n\le X:n\in\mathcal S,\ D(S_n)\ge\delta n\}
 \ll \frac1{\delta}\left[\log(2X)+M\left(1+\log\frac XM\right)\right],       \tag{2a}
\]
where the second summand is zero when \(M=0\). In fact \(W(d)>0\) gives a prime \(p^2\mid S_d\), so \(p<e^{hd}\), and distinct ranks give distinct primes. In the sum of \(D(S_n)/n\) over \(n\le X\), each of these ranks contributes at most \(O(\sum_{k\le X/d}1/k)\), by \(W(d)\ll d\). Placing at most \(M\) ranks at \(1,\ldots,\lfloor M\rfloor\) maximizes this bound and gives the expression in (2a). The lifting term contributes \(O(\log^2(2X))\), or \(O(\log(2X))\) by (4) below and partial summation. In particular, \(E(x)=o(\log x)\) suffices for zero upper natural density of every linear-excess set. Positive lower natural density forces \(E(x)\gg\log x\) for all large \(x\), and positive upper density forces the same lower bound along a sequence. Also, \(\sum_{p:\, w_p\ge2,\, r_p=4d,\,d\in\mathcal S}1/\log p<\infty\) implies finite reciprocal sum for every such set by (2), since \((w_p-1)\log p\ll d\) and \(d>\log p/h\).

## A quadratic size and depth restriction on average over primitive indices

For \(D\le d<2D\), each prime of rank \(4d\) has \(p=4dj\pm1\) for an integer \(j\ge1\). Uniformly at \(D\ll T\ll D^2\), the aggregate distinct log weight of such prime occurrences with \(T<p\le2T\) is \(O(T)\), even if one drops the rank test and counts all these representations. In fact \(j\asymp T/D\). For each \(j\), the Brun–Titchmarsh inequality in modulus \(4j\), up to \(2T\), bounds the count of these primes by \(O(T/[\varphi(4j)\log D])\), and each costs \(O(\log D)\) in this range. The dyadic sum of \(1/\varphi(j)\) is \(O(1)\), using \(j/\varphi(j)=\sum_{h\mid j}\mu^2(h)/\varphi(h)\) and \(\sum_h\mu^2(h)/(h\varphi(h))<\infty\). Bounded \(T/D\) is included. At \(T\) below a constant times \(D\) there are no candidate primes except in the immediately adjacent interval. Switching the modulus from \(4d\) to \(4j\) keeps the sieve denominator of size \(\log D\) even near \(p\asymp d\).

Put \(e=w_p-1\ge1\). With \(0<c<1\), take \(Z=4cD^2/\log D\). At each dyadic scale \(p\asymp T\) with \(pe\le Z\), multiplication by \(e\le O(Z/T)\) bounds the full excess weight by \(O(Z)\). There are \(O(\log D)\) such scales. Therefore \(\sum_{D\le d<2D}\sum_{r_p=4d,\,pe\le c d^2/\log(2d)} e\log p\ll cD^2\), with an absolute constant and \(D\) sufficiently large for fixed \(c\).

For \(pV_\eta(e)\le c d^2\) take \(Z=4cD^2\) and split into \(Z/2^{j+1}<p\le Z/2^j\). Inverting \(V_\eta(e)\le2^{j+1}\) gives
\[
       e\ll_\eta \frac{2^j}{(1+j)[1+\log(1+j)]^{1+\eta}} .
\]
This follows by separating \(e\le 2^{j/2}\) and its complement. The aggregate log mass bound at that scale is \(O(Z/2^j)\) and the resulting series over \(j\) converges. Thus the omitted mass is \(O_\eta(cD^2)\) in this version as well. Summing dyadic blocks after dividing by \(d\) gives \(O_\eta(c)\) in the normalized primitive mean, for either choice of \(\mathcal S\). Choosing \(c\) small relative to a positive upper or lower mean and using boundedness gives assertion 3.

The extra cutoff uses C. L. Stewart's valuation bound for the fixed Lucas pair \((\epsilon,\epsilon')\). At all sufficiently large odd \(p\), its statement specializes to \(w_p\ll p\exp(-\log p/[51.9\log\log p])\log(2r_p)\). Here the ratio is a quadratic norm-one unit of infinite order and \(2\sqrt2\) is a local unit. At fixed \(r_p=4d\), the possible primes up to \(Y=d\exp(\gamma\log d/\log\log d)\) lie among \(O(1+Y/d)\) integers in the two progressions, each at least \(4d-1\). The resulting full log mass is \(\ll d\exp[-c_\gamma\log d/\log\log d]\) for every fixed \(\gamma<1/103.8\), by summing the displayed valuation bound and taking \(c_\gamma>0\) small enough. This is pointwise in \(d\). Stewart's primitive-prime bound concerns a prime divisor's size; the valuation lemma here controls the complete mass at small primes without assuming abc. [Stewart, *On divisors of Lucas and Lehmer numbers*, published Lemma 4.3](https://doi.org/10.1007/s11511-013-0105-y) · [Preprint, Lemma 8](https://arxiv.org/abs/1008.1274)

## A positive-density set with the ordinary lifting term identically zero

Among squarefree indices of either fixed parity, the relative natural density \(\rho_a\) of \(\gcd(n,S_n)=1\) exists. Here \(a=v_2(n)\in\{0,1\}\). The following rigorous intervals use only primes through \(2^{20}\) and an elementary tail bound.

| Squarefree indices | Lower bound | Upper bound |
|---|---:|---:|
| Odd | 0.735732 | 0.737558 |
| Even | 0.941615 | 0.943419 |

The corresponding densities among all integers are \(4\rho_0/\pi^2\) and \(2\rho_1/\pi^2\). On each of these sets the sum of the first-occurrence Pell–Wieferich contributions in (1) is the entire radical defect.

To prove this, write \(n=2^am\) with \(m\) odd and squarefree. An odd prime divides \(\gcd(n,S_n)\) exactly if \(r_p=4d_p\), \(d_p\) is squarefree with \(v_2(d_p)=a\), and \(p d_p/2^a\mid m\). Indeed \(p\nmid d_p\), by its order, and the trace divisibility condition in (1) requires the odd quotient. Conditional on odd squarefreeness, the indicators \(q\mid m\) at any finitely many odd primes are independent, with probabilities \(1/(q+1)\), by the squarefree sieve in fixed progressions. Thus a single forbidden event of support \(E_p=\{q:q\mid p d_p/2^a\}\) has probability \(\prod_{q\in E_p}(q+1)^{-1}\le 2^a/(pd_p)\). The avoidances are decreasing events. Harris's inequality bounds their joint probability from below by the product of the individual avoidance probabilities. Each factor is positive.

For a power of two \(T\ge2\), consider \(T<p\le2T\). For each \(d\le\sqrt T\), the sum of the logs of the primes of rank \(4d\) in this interval is at most \(\log S_d<2d\log\epsilon\). Summing \(1/(pd)\) for these \(d\) therefore costs at most \(2\log\epsilon/(\sqrt T\log T)\). For \(d>\sqrt T\), use \(\#\{T<p\le2T\}\le T\log4/\log T\), by divisibility of the central binomial coefficient. Dyadic summation gives, for every power of two \(Y\ge2\),
\[
 \sum_{\substack{p>Y\\ r_p=4d_p}}\frac1{p d_p}
 \ \le\ \frac{2\log\epsilon+\log4}{1-1/\sqrt2}\frac1{\sqrt Y\log Y}
 \ <\ \frac{12}{\sqrt Y\log Y}.                                  \tag{3}
\]
For integer multiples of \(L\), the unconditioned count up to \(X\) is at most \(X/L\). Hence the unconditioned upper density of the union of the omitted events tends to zero, even before the squarefree restriction. This proves existence of the relative natural density as the limit of the finite probabilities. It also justifies the sharper conditional tail bound \(2^a\) times (3), by a union bound on any finite extension of the cutoff followed by the limit. Harris's convergent product now proves \(\rho_a>0\).

For the intervals in the table, the finite calculation removes an event whenever a previous event's support is a subset. There are 15,308 remaining events for odd indices and 2,496 for even indices. It applies exact rational inclusion–exclusion to the twelve most probable events for each parity, bounds the rest by their summed probabilities rounded upwards to \(10^{-14}\), then uses (3) for \(Y=2^{20}\). [Reproduce the density bounds](./abc_pell_trace_clean_density.py)

On these sets \(S_n\) itself is squarefree precisely when no Pell–Wieferich prime has \(r_p=4d_p\) with \(d_p\mid n\) and \(n/d_p\) odd. In particular, convergence of \(\sum_{p:\,w_p\ge2,\ r_p=4d_p,\ d_p\ {\rm squarefree},\ v_2(d_p)=a}1/d_p\) would give a positive natural density of squarefree \(S_n\) on that parity, by adding the decreasing avoidance events \(d_p/2^a\nmid m\) to the same argument. Each such event has positive avoidance probability since \(S_1=3,\ S_2=17\) are squarefree. This extra convergence remains unproved.

An exhaustive finite verification tested \(a_{p-(2/p)}\bmod p^2\) for all 2,880,514 primes \(p\le10^8\) in the eligible classes \(1,3\bmod8\). None was Pell–Wieferich. The same code recovered \(13,31,1546463\) as positive controls outside these classes. Consequently for every squarefree \(n\), each prime \(p\le10^8\) which occurs repeatedly in \(S_n\) divides \(n\) and has exponent exactly two. The calculation uses the binary doubling identities in the quadratic ring with integer arithmetic. [Reproduce the Wieferich scan](./abc_pell_trace_wieferich_scan.cpp)

## Uniform tail for the entire ordinary lifting term

Uniformly in \(X\ge1\), as \(z\to\infty\),
\[
 \frac1X\#\{n\le X:n\ {\rm squarefree},\ \log\gcd(n,S_n)\ge z\}
 \ \le\ \exp\!\left[-\left(\tfrac12-o(1)\right)\sqrt{z\log z}\right].
                                                                    \tag{4}
\]
Indeed if a participating \(p>y\), then \(p d_p\mid n\); (3) and the elementary count of multiples bound this entire frequency by \(O(1/(\sqrt y\log y))\). If all participating primes satisfy \(p\le y\), then \(\log\gcd(n,S_n)\le G_y(n)=\sum_{q\le y,\ q\mid n}\log q\), since \(n\) is squarefree. For \(t>0\), expansion over squarefree products and the count of multiples give
\[
 \frac1X\sum_{n\le X} e^{t G_y(n)}
 \ \le\ \prod_{q\le y}\left(1+\frac{q^t-1}{q}\right).
\]
Take \(u=z/\log y>1,\ t=\log u/\log y\). Convexity gives \(q^t-1\le(u-1)\log q/\log y\), so the logarithm of this product is \(O(u)\), using \(\sum_{q\le y}\log q/q\ll\log y\). Markov's inequality bounds the second frequency by \(\exp(-u\log u+O(u))\). Choose \(y\) a power of two with \(\log y=\sqrt{z\log z}+O(1)\) to obtain (4).

In particular, on each squarefree parity the ordinary lifting term has a limiting distribution and all fixed positive moments converge and are finite. The finite-prime distribution follows by the squarefree sieve, (3) controls its limiting tail of prime supports, and (4) gives uniform integrability for each moment. Its conditional mean is the absolutely convergent local sum
\[
 \sum_{\substack{r_p=4d_p\\d_p\ {\rm squarefree},\ v_2(d_p)=a}}
     \log p\prod_{q\mid p d_p/2^a}(q+1)^{-1}.
\]
