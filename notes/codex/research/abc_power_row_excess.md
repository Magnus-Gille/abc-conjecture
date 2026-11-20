# Mean excess multiplicity at each order of a binary power difference

Choose $(A,B)$ uniformly from the coprime pairs $1\le B<A\le H$ and write $V_r=A^r-B^r$. For $p\nmid AB$ let $r_p=\operatorname{ord}_p(AB^{-1})$. Fix $0<\nu<2$. Uniformly for $3\le r\le H^{2-\nu}$, put $k_r=\max(1,\varphi(r)/2-1)$. Then

$$
 \mathbb E\sum_{r_p=r}\big(v_p(V_r)-k_r\big)_+\log p\ll_\nu\varphi(r).       \tag{1}
$$

Here $x_+=\max(x,0)$. This counts excess in the first term divisible by the prime. For odd $p$ and $r_p=r\mid n$, the exponent in $V_n$ is $v_p(V_r)+v_p(n/r)$.

Set $k_1=k_2=1$, $w_r=\varphi(r)/k_r$, $W_n=2+\sum_{r\mid n}w_r$ and $R_n=\operatorname{rad}(ABV_n)$. For $1\le n\le H^{2-\nu}$,

$$
                    \mathbb E\big(W_n\log H-\log R_n\big)_+\ll_\nu W_n.       \tag{2}
$$

Thus for each $0<\eta<1$, the proportion with $R_n<H^{(1-\eta)W_n}$ is $O_\nu(1/(\eta\log H))$.

## Bounding the excess at one order

Write $d=\varphi(r)$, $k=k_r$ and $m=k+1$. A prime of order $r$ satisfies $p\equiv1\pmod r$, and its full power in $V_r$ divides $\Phi_r(A,B)\le(2H)^d$. If $v_p(V_r)\ge m$, then $p\le(2H)^{d/m}\le4H^2$ because $m\ge d/2$.

For each such candidate $p$ and any $j\ge1$, there are $d$ roots of $x^r=1\bmod p^j$ of exact order $r$ after reduction modulo $p$. Each primitive root modulo $p$ lifts uniquely since $p\nmid r$. Two distinct reduced fractions $B/A$ in one residue class modulo $p^j$ differ by at least $p^j/H^2$ by the determinant formula for their difference. Thus at most $d(1+H^2/p^j)$ pairs have $r_p=r$ and $p^j\mid V_r$, and at most $d$ pairs do when $p^j>H^2$.

Put $J_p=\max(m,\min\{j:p^j>H^2\})$. Call a pair exceptional for this order if $p^{J_p}\mid V_r$ at any prime $p$ of order $r$. The proportion of such pairs is

$$
 \ll \frac{d}{H^2}\pi(4H^2;r,1)\ll_\nu \frac1{\log H}
$$

by the spacing just proved, the $\asymp H^2$ primitive pairs in the box, and Brun–Titchmarsh with $r\le H^{2-\nu}$. The total log mass of the row on each exceptional pair is at most $d\log(2H)$, so these pairs contribute $O_\nu(d)$ to the mean. On the other pairs each level $j\ge m$ counted in the excess has $p^j\le H^2$. Its proportion of pairs is $O(d/p^j)$ by spacing. Summing the levels costs at most a constant times

$$
 d\sum_p\sum_{j\ge m}\frac{\log p}{p^j}
 \le d\sum_p\frac{\log p}{p(p-1)}\ll d,
$$

which proves (1).

## Adding the radicals of different orders

Let $L_r=\sum_{r_p=r}v_p(V_r)\log p$ and $P_r=\prod_{r_p=r}p$. For $r\ge3$, cyclotomic factorization gives

$$
 L_r\ge d\log A-(2^{\omega(r)}+1)\log r\ge d\log A-O(d).
$$

The first error term comes from Möbius inversion in $\Phi_r$ and removal of the imprimitive primes, whose product divides $\operatorname{rad}(r)$. The uniform second inequality uses $2^{\omega(r)}\le\tau(r)=r^{o(1)}$ and $d\ge\sqrt{r/2}$. The linked proof gives the cyclotomic estimates in detail. [Uniform exact-order estimates](abc_variable_seed_prime_mass.md)

Since $k\log P_r\ge L_r-\sum_{r_p=r}(v_p(V_r)-k)_+\log p$, (1) gives $\mathbb E(w_r\log A-\log P_r)_+\ll_\nu w_r$.

The linear forms $A,B,A-B,A+B$ each take any given positive value on at most $H$ pairs. For each form $U$, this gives $\mathbb E(\log H-\log U)_+\ll1$ by integrating the bound $\Pr(U\le He^{-t})\ll e^{-t}$ for $t\ge0$. It also gives $\Pr(p^j\mid U)\ll 1/p^j$ by counting multiples through $2H$. Summing over $p$ and $j\ge2$ as above yields $\mathbb E\log(U/\operatorname{rad}U)\ll1$. In particular $\mathbb E(\log H-\log A)\ll1$, so $\log H$ can replace $\log A$ in the bound for $P_r$.

For $r\mid n$, the primes in $P_r$ divide $V_n$ and are disjoint for different $r$. At $r\ge3$ they are also disjoint from $AB(A-B)(A+B)$. Use the radicals of $A,B,A-B$, and also $A+B$ if $n$ is even, for the remaining terms in $W_n$. By coprimality the only possible overlap is the prime $2$ between $A-B$ and $A+B$, costing at most $\log2$. Summing the positive deficits proves (2).

## The abc exponent supplied by the bound

For fixed $n$, (2) proves $A^n\le R_n^e$ on a proportion tending to one whenever $e>n/W_n$. For $\varphi(n)\le4$ every divisor $r\mid n$ has $k_r=1$ and $W_n=n+2$. The deterministic bound $R_n\le H^{n+2}$ and (2) then give $\mathbb E\lvert\log R_n-(n+2)\log H\rvert=O_n(1)$. The abc quality $n\log A/\log R_n$ converges in probability to $n/(n+2)$, and in particular every exponent $1+\varepsilon$, $\varepsilon>0$, holds in probability.

The indices with $\varphi(n)\le4$ are exactly $1,2,3,4,5,6,8,10,12$. For $\varphi(n)\ge6$ the term $r=n$ alone loses at least three from $\sum_{r\mid n}\varphi(r)=n$, so $W_n\le n-1$. This is the scope of (2); separate square- and cube-twist counts give all fixed abc exponents in probability at $n=7,9$. [Sextic exception count](abc_sextic_power_exception_count.md)

When $n\to\infty$, every $w_r\le4$ and hence $W_n\le2+4\tau(n)=n^{o(1)}$. Estimate (2) remains uniform in the stated range, but $W_n/n\to0$, leaving the radical bound short of any fixed abc exponent along growing indices.
