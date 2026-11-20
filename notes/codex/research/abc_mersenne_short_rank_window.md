# Testing fixed abc exponents in short windows of Mersenne ranks

Write $M_n=2^n-1$, and let $\Phi_r$ be the $r$th cyclotomic polynomial. Define the normalized excess
$$
 e(r)=\frac{1}{\log2}\log\frac{\Phi_r(2)}{\operatorname{rad}(\Phi_r(2))}.
$$
For a fixed $K>0$ set
$$
 H=\limsup_{n\to\infty}\frac1n\sum_{r\mid n}e(r),\qquad
 H_K=\limsup_{n\to\infty}\frac1n\!
        \sum_{\substack{r\mid n\\ n/r\le(\log n)^K}}e(r).
$$
Then the Mersenne family violates abc at some fixed positive exponent if and only if $H_K>0$, for **any one fixed $K>0$**. At each index the test uses at most $\lfloor(\log n)^K\rfloor$ possible quotients $n/r$. The theorem compares limsups; the indices furnishing the short-window excess may differ from those furnishing the original excess. Computing the excess still requires information about the prime powers in the relevant cyclotomic factors.

More quantitatively,
$$
 \begin{aligned}
    (K/4)H&\le H_K\le H &&(0<K\le2),\\
    (1-1/K)H&\le H_K\le H &&(K\ge2).
 \end{aligned}                                                       \tag{1}
$$

## Which prime powers enter the test?

For $p$ odd let $r_p=\operatorname{ord}_p(2)$ and $w_p=v_p(2^{r_p}-1)$. The valuation of $\Phi_r(2)$ at $p$ is $w_p$ if $r=r_p$, one if $r=r_pp^j$ with $j\ge1$, and zero otherwise. This follows by Möbius inversion of $v_p(M_n)=\mathbf1_{r_p\mid n}(w_p+v_p(n))$. Thus
$$
 (\log2)e(r)=\sum_{r_p=r}(w_p-1)\log p,\qquad
 \log(M_n/\operatorname{rad}M_n)=\log\gcd(n,M_n)+(\log2)\sum_{r\mid n}e(r).
$$
It follows that $0\le H\le1$ and the limsup of abc quality on this family equals $1/(1-H)$, with value $+\infty$ if $H=1$. [Proof of the lifting identity](abc_mersenne_logarithmic_gain.md)

For use below, $0\le e(r)\le\varphi(r)$ at every $r$. Indeed Möbius inversion gives $\Phi_r(2)\le2^{\varphi(r)}\prod_{j\ge1}(1-2^{-j})^{-1}<4\cdot2^{\varphi(r)}$. The infinite product before inversion is at least $(1/2)(3/4)(1-\sum_{j\ge3}2^{-j})=9/32$. If $e(r)>0$ at $r\ge3$, some prime of order $r$ is repeated, and stripping its radical removes a factor at least 5. At $r=1,2$ the excess is zero.

## Proof of the short-window bound

The argument works for any nonnegative weights $e(r)\le\varphi(r)$. Put $S_K(m)=m^{-1}\sum_{r\mid m,\ m/r\le(\log m)^K}e(r)$. Fix $0<a<1$. For a large source index $n$, take $y=(\log n)^{aK}$ and keep **this same $y$** throughout the following decomposition. Let
$$
 B_y(m)=\frac1m\sum_{\substack{r\mid m\\ p\mid(m/r)\Rightarrow p\le y}}e(r).
$$
One has $0\le B_y(m)\le1$ by $\sum_{r\mid m}\varphi(r)=m$.

Factor each coindex $n/r$ into its full part $L$ supported on primes $>y$ and a remaining part supported on primes $\le y$. This gives the exact decomposition $n^{-1}\sum_{r\mid n}e(r)=\sum_L B_y(n/L)/L$, over divisors $L\mid n$ having only prime factors $>y$, including 1. The terms $L>\sqrt n$ contribute at most $\tau(n)/\sqrt n=o(1)$. For the rest, the total coefficient is bounded by
$$
 \sum_L\frac1L\le\prod_{p\mid n,\ p>y}(1-1/p)^{-1}
           \le \max(1,1/(aK))+o(1).
$$
For $y<p\le\log n$ use Mertens' product theorem. For the primes $p\mid n$, $p>\log n$, their number is at most $\log n/\log\log n$ and their reciprocals sum to $o(1)$.

For $k=m/r>(\log m)^K$ supported on primes $\le y$, insert
$1\le\log k/(K\log\log m)=\sum_{p^j\mid k,\,j\ge1}\log p/(K\log\log m)$ into $B_y(m)$. It follows that
$$
 B_y(m)\le S_K(m)+
 \sum_{\substack{p\le y,\,j\ge1\\ p^j\mid m}}
     \frac{\log p}{p^j K\log\log m}\,B_y(m/p^j).
$$
For each fixed $b>0$ and $n^b\le m\le n$, the sum of the coefficients is at most $a+o_b(1)$, because $\sum_{p\le y}(\log p)/(p-1)=\log y+O(1)$ and $\log\log m=\log\log n+O_b(1)$. The terms with $p^j>\sqrt m$ are $o_b(1)$ uniformly: their coefficient sum is at most $(\log m)/(\sqrt m K\log\log m)$. Starting at $m\ge\sqrt n$, iterate a fixed $J$ times using only the remaining terms. The last arguments are at least $n^{1/2^{J+1}}$, so every $S_K$ is bounded by $H_K+o_J(1)$. The last $B_y$ terms are at most 1. First taking $n\to\infty$ and then $J\to\infty$ gives a uniform limsup bound $H_K/(1-a)$ for $B_y(m)$ in the starting range. The coefficient bound for $L$ gives
$$
                    H_K\ge(1-a)\min(1,aK)H .
$$
Take $a=1/2$ if $K\le2$ and $a=1/K$ otherwise. This proves (1).

## Why a subpower of the logarithm requires new arithmetic

There are globally defined nonnegative weights under the same totient cap for which every window $n/r\le v(n)$ with $v(n)=(\log n)^{o(1)}$ has vanishing normalized sum, yet the full normalized sum has positive limsup. Take $e_0(r)=c r/\log\log(10r)$ with a sufficiently small constant $c>0$. The standard bound $r/\varphi(r)\ll\log\log(10r)$ gives the cap. In a short window $r\ge n/v(n)$ the normalized sum is at most $O((1+\log v(n))/\log\log n)=o(1)$. On the other hand for $n=\prod_{p\le y}p$, one has $\sigma(n)/n=\prod_{p\le y}(1+1/p)\asymp\log y$ and $\log\log n\sim\log y$. Since $r\le n$, the full sum is at least $c\,\sigma(n)/(n\log\log(10n))\gg1$. These are model weights. The actual Mersenne weights are determined by the first occurrences of prime squares. [Related totient-weight model for Pell numbers](abc_pell_direct_primitive_convolution.md)
