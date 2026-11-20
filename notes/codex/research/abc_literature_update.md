# Recent results relevant to the abc search

Reviewed 19 November 2026. I searched titles and abstracts of 2026 submissions in an arXiv metadata snapshot with an OAI datestamp of 18 November. Direct requests for the arXiv manuscripts returned HTTP 403 in this environment. The descriptions below identify the authors' claims and distinguish them from deductions checked here. The search cannot establish peer-review status, resolve disputes over a proof, or cover work absent from the index. [Metadata snapshot](https://github.com/guanqun-yang/ArxivDB/tree/33098fc296f82f103a8c99a6957e20a52884c589/data/2026)

## Proof audit with the highest priority

Carella's supplied v3 manuscript claims infinitely many exceptional triples at a fixed positive exponent. Its Corollary 4.1 requires at least $x^{3/5-o(1)}$ candidate integers in one short interval. A squarefree-part count bounds the number of candidates in the entire range up to $2x$ by $x^{4/7+o(1)}$. This refutes the counting step used in Theorem 5.1. The coprimality calculation and the proposed fixed-exponent implication can be checked independently. [Proof audit](carella_v3_reading.md) · [Carella](https://arxiv.org/abs/2608.16764v3)

In the subsequently supplied version 1 of Christophe Soulé's manuscript, Theorem B claims c ≤ A(ε) rad(abc)^(24+ε). This allows qualities slightly above 1, including the range relevant to Carella's claim. The exceptional-fiber dimension computation used to prove the weak bound also has a problem in Proposition 9. [Version-specific analysis](soule_v1_reading.md) · [Soulé](https://arxiv.org/abs/2611.05217)

## A test case for the fixed-exponent claim

Consider $(a,b,c)=(1,t^2-1,t^2)$ for integers $2\le t\le T$. This is a separate test family. Carella's §5 uses prime fifth powers and nearby smooth integers. Write $R=\operatorname{rad}((t-1)t(t+1))$. The three separate radicals have product at most $2R$, since only 2 can occur in two of the three factors. Therefore $c^{35}>R^{36}$ forces at least one of $t-1,t,t+1$ to have radical at most $2^{1/3}T^{35/54}$.

For each fixed $s>0$, the count of positive $u\le X$ with $\operatorname{rad}(u)\le Z$ is at most

$$
ZX^s\sum_{u\ge1}\frac{1}{u^s\operatorname{rad}(u)}
= ZX^s\prod_p\left(1+\frac{1}{p(p^s-1)}\right).
$$

The product converges because its logarithm has a tail bounded by a constant times $\sum_p p^{-1-s}$. Applying this inequality to the three shifts shows that the number of qualifying $t$ is $O_s(T^{35/54+s})$. This proves relative density zero among *all* integer parameters. It gives no finiteness conclusion, and it does not rule out concentration on the much sparser sequence $t=2^{3^n}$.

A sieve multiplying each prime into its multiples up to 1,000,001 gave 528 qualifying parameters through one million. The comparison used integer powers $t^{70}>R^{36}$ and divided the product of the three radicals by the gcd of the radicals of $t-1$ and $t+1$. The cumulative counts through 10, 100, 1,000, 10,000 and 100,000 were 4, 16, 42, 115 and 243 respectively.

## Direct overlap with the cubic orbit of 4

R. Laniewski studies the triples (1, 2^m - 1, 2^m) and describes an exact decomposition of the repeated-prime contribution into a Wieferich contribution and a divisor of m. Our family is the specialization m = 2 times 3^n. The largest divisor of m supported on primes dividing 2^m - 1 is precisely 3^n, since 2^m - 1 is odd and divisible by 3. This accounts for the known n log 3 contribution. When evaluating claims about this family, the general decomposition is prior work. [Laniewski](https://arxiv.org/abs/2609.00039)

Samin Riasat's November abstract bounds repeated primitive prime factors of Lucas terms along families with Euler's phi(m)/m bounded below, assuming rational abc. Here take the Lucas sequence (4^m - 1)/3, with roots 4 and 1 and coprime parameters 5 and 4. At m = 3^(n+1) we have phi(m)/m = 2/3. For p other than 3 dividing our U_n, the multiplicative order of 4 modulo p is exactly m. Thus these are precisely the kinds of primitive primes addressed by the abstract. The article also announces an independent Hensel-root description of multiplicities. The conditional size estimate cannot serve as an unconditional input to a proof of abc. [Riasat](https://arxiv.org/abs/2611.20650)

Hector Pasten reports that the absolute minimal discriminant and conductor of a semistable elliptic curve over the rationals satisfy log |Delta| = O(N), together with a general bound O(N log log N). Comparing scales is important on the Frey-curve route. A polynomial discriminant bound would instead give log |Delta| = O(log N). [Pasten](https://arxiv.org/abs/2609.17390)

## An unconditional bound available now

Write m = 3^(n+1), U_n = (4^(2m/3) + 4^(m/3) + 1)/3 and fix A > 0. The total contribution of repeated primes p <= m (log m)^A to log(U_n/rad(U_n)) is o(m). Every candidate prime is 1 modulo m, so there are O((log m)^A) candidates and each exceeds m. Stewart's valuation estimate applied to the fixed pair (4,1) bounds v_p(4^m - 1) by a constant times p exp(-log p/(51.9 log log p)) log m for sufficiently large p. In the indicated range, replacing p in the prefactor by the endpoint, and in the decreasing exponential by m, bounds the entire sum by O(m (log m)^(2A+2) exp(-log m/(51.9 log log m))). This is o(m). Since log U_n is asymptotic to (2/3)m log 4, any fixed fractional contribution must persist among larger primes. The repository's companion manuscript gives the stronger window m exp(gamma log m/log log m) for gamma < 1/103.8 by this same argument. [Stewart](https://arxiv.org/abs/1008.1274) · [Companion manuscript](../../../paper/chebyshev-companion.tex#L805)
