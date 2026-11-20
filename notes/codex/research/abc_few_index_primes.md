# The small-prime radical at indices with few distinct prime factors

Let $A>B\ge1$ be coprime integers, $V_n=A^n-B^n$, and let $\omega(n)$ count the distinct prime divisors of $n$. Write
$$
  B_X(n)=\sum_{\substack{p\mid V_n\\p\le X}}\log p .
$$
Put $h=\log A$ and $U=\sqrt{X/h}$. For each integer $s\ge1$, uniformly for $n\ge2$, $\omega(n)\le s$, $X\ge2$ and $1\le U\le n$,
$$
 B_X(n)\ll_s\sqrt{Xh}\,
 \big[1+\log\min\{U,n/U\}\big]^{s-1}.                                  \tag{1}
$$
The implied constant is independent of $A,B$. In particular, even if the pair is chosen separately for each $n$, an infinite sequence of such indices with $P^+(V_n)=o(n^2\log A)$ would give abc quality tending to infinity. For a fixed pair the condition reduces to $P^+(V_n)=o(n^2)$. If instead $A\to\infty$, the upper bound $P^+(V_n)\le n^2$ already suffices. The existence of any of these sequences is open here.

## The contribution at one order

Every $p\mid V_n$ is coprime to $AB$. Its multiplicative order $d=\operatorname{ord}_p(A/B)$ divides both $n$ and $p-1$. Let $H_X(d)$ denote the sum of $\log p$ over all such orders equal to $d$ and primes up to $X$, independent of $n$. Since these primes divide $A^d-B^d$, we have $H_X(d)\le d\log A$. For $U<d\le X^{3/4}$, Brun–Titchmarsh in the class $1\bmod d$ gives $H_X(d)\le 8X/\varphi(d)\ll_s X/d$ when $\omega(d)\le s$. Indeed, $d/\varphi(d)$ is bounded by the corresponding product for the first $s$ primes. For $d>X^{3/4}$ the congruence alone gives $H_X(d)\le (X/d)\log X$. When also $d>U$, the inequalities $U\le\sqrt{X/\log2}$ and $\log X\ll X^{1/8}\ll(d/U)^{1/2}$ then give, over all three ranges,
$$
 H_X(d)\ll_s\sqrt{Xh}
 \min\left\{\frac dU,\left(\frac Ud\right)^{1/2}\right\}.       \tag{2}
$$
This includes order one, and $H_X(d)=0$ for $d\ge X$.

## Summing over divisors near the transition

For any $U\ge1$ there are $O_s((1+\log(2U))^{s-1})$ divisors of $n$ in $[U,2U)$. To count them, choose one prime dividing $n$ and fix the exponents of all other primes. There are at most $1+\log(2U)/\log 2$ possibilities for each of those exponents. Successive powers of the remaining prime differ by a factor of at least two, so at most one fits. The same bound with a constant covers intervals meeting 1 from below.

Use (2) in the sum $B_X(n)=\sum_{d\mid n}H_X(d)$. In the intervals $[2^j U,2^{j+1}U)$ for all integral $j$, the weight in (2) is $O(2^{-|j|/2})$. The divisor count is $O_s((1+\log U+|j|)^{s-1})$ on each nonempty interval. Summation gives (1) with $U$ in place of the minimum. Repeat the count with $g=n/d$, also a divisor of $n$, using intervals $[2^jT,2^{j+1}T)$ with $T=n/U\ge1$. Now $d/U=T/g$, and the same geometric bound holds. Taking the smaller of the resulting bounds proves (1).

Set $X=P^+(V_n)$ on the proposed sequence. Then $T=n/U\to\infty$. For $U\ge1$, (1) bounds $\log\operatorname{rad}(V_n)/(nh)$ by $O_s((1+\log T)^{s-1}/T)$. For $U<1$, Chebyshev gives $B_X(n)\le\sum_{p\le X}\log p\ll X<h$. In either case the radical of the triple is $\operatorname{rad}(AB)\operatorname{rad}(V_n)$, with $\log\operatorname{rad}(AB)\le2h$, proving the implication uniformly. For $A=2$, $B=1$ and $s=1$, a separate proof gives the explicit bound $5\sqrt X$. [Prime-power bound](abc_mersenne_quadratic_prime_threshold.md)
