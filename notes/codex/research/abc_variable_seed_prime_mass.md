# Large prime powers for almost all pairs of bases

Choose $(A,B)$ uniformly among the coprime integer pairs $1\le B<A\le H$, and put $V_n=A^n-B^n$. For $p\mid V_n$, write $r_p=\operatorname{ord}_p(AB^{-1})$. Fix $0<\nu<2$, let $H\to\infty$, and take any $n=n(H)\to\infty$ with $n\le H^{2-\nu}$. For any $1\le g=g(H)=o(\log H)$ put $X=H^2g$. Then both ratios

$$
 \frac{\sum_{p\mid V_n,\ p>X,\ r_p=n}v_p(V_n)\log p}{\varphi(n)\log A},
 \qquad
 \frac{\sum_{p\mid V_n,\ p>X}v_p(V_n)\log p}{n\log A}
$$

converge to $1$ in probability over the pairs. In particular, one may take $X=H^2$. The weights count the full prime powers. For all sufficiently large $n$ in this range, the proportion of pairs having **no exact-order prime above $X$** is

$$
 \ll_\nu \frac{g}{\log H}+\frac1{\varphi(n)}.                         \tag{1}
$$

The same bound applies to the proportion for which the whole $V_n$ is $X$-smooth. These statements allow a different index at each $H$ and average over the pairs at that index.

## The exact-order part of a cyclotomic factor

Let $\Phi_r(A,B)$ be the homogeneous cyclotomic polynomial evaluated at the pair. For $r\ge3$, let $L_r$ be the full logarithmic mass in $V_r$ at primes of order $r$. Then

$$
 0\le \log\Phi_r(A,B)-L_r\le\log r,\qquad
 |\log\Phi_r(A,B)-\varphi(r)\log A|\le 2^{\omega(r)}\log r.            \tag{2}
$$

For an odd prime of order $s$, lifting gives $v_p(V_{sj})=v_p(V_s)+v_p(j)$. Möbius inversion on the divisors shows that its full first valuation occurs in $\Phi_s$, followed by a single copy in each $\Phi_{sp^k}$ for $k\ge1$. If both bases are odd, the even-prime lifting formula puts a single copy of $2$ in each $\Phi_{2^k}$ for $k\ge2$ and none at other $r\ge3$. Thus the product of the imprimitive factors at $r\ge3$ divides $\operatorname{rad}(r)$. For the second inequality put $t=B/A$. In the Möbius sum for $\log\Phi_r-\varphi(r)\log A$, the common term $\log(1-t)$ cancels. Each remaining term $\log(1+t+\cdots+t^{d-1})$ lies between $0$ and $\log d$ and has coefficient $\mu(r/d)$. This proves (2). Since $2^{\omega(r)}\le\tau(r)=r^{o(1)}$ and $\varphi(r)\ge\sqrt{r/2}$, equation (2) gives $L_r=(1+o(1))\varphi(r)\log A$ uniformly over the pairs as $r\to\infty$. Also, the factorization over the primitive roots of unity gives $\Phi_r(A,B)\le(2H)^{\varphi(r)}$ for every $r$.

## Counting small-prime mass for one order

The number of pairs is $\sum_{2\le A\le H}\varphi(A)\asymp H^2$. Two distinct reduced fractions $B/A,B'/A'$ in a common residue class modulo $q$, with both denominators units modulo $q$, satisfy

$$
 \left|\frac BA-\frac{B'}{A'}\right|
   =\frac{|BA'-B'A|}{AA'}\ge\frac q{H^2}.
$$

Consequently each residue class contains at most $1+H^2/q$ such fractions, and at most one when $q>H^2$.

Fix $3\le r\le H^{2-\nu}$. An exact-order prime $p$ satisfies $p\equiv1\pmod r$. Modulo $p$ there are $\varphi(r)$ residues of exact order $r$. Each lifts uniquely to a root of $x^r=1\bmod p^j$ for every $j\ge1$, since $p\nmid r$. The inverse fraction $B/A$ has the same order as $A/B$. Thus the number of pairs with $r_p=r$ and $p^j\mid V_r$ is at most $\varphi(r)(1+H^2/p^j)$.

For each $p\le H^2$ in this progression take the least $j_p$ with $p^{j_p}>H^2$. Call a pair exceptional for $r$ if some such prime has both $r_p=r$ and $p^{j_p}\mid V_r$, or if a prime in $(H^2,X]$ has $r_p=r$. The number of exceptional pairs is at most $\varphi(r)\pi(X;r,1)$. Indeed, each prime costs at most $\varphi(r)$ pairs by spacing, using modulus $p^{j_p}$ in the first range and $p$ in the second. Brun–Titchmarsh and $\log(X/r)\ge\nu\log H$ bound this count by $O_\nu(gH^2/\log H)$. On those pairs the entire row contributes at most $\varphi(r)\log(2H)$ per pair. Their contribution to the unconditional mean is therefore $O_\nu(g\varphi(r))$.

On the other pairs all exact-order contributions up to $X$ are counted by $p^j\le H^2$. Summing the spacing bound with $1+H^2/p^j\le 2H^2/p^j$, then summing the geometric series in $j$, bounds their contribution to the unconditional mean by a constant times

$$
 \varphi(r)\sum_{\substack{p\le H^2\\p\equiv1\pmod r}}\frac{\log p}{p-1}
 \ll \varphi(r)+\log H.                                                 \tag{3}
$$

For $p\le r^2$ write $p=kr+1$ and sum over all $k\le r$, obtaining $O(\log^2(2r)/r)=O(1)$ before multiplication by $\varphi(r)$. For $r^2<p\le H^2$ use dyadic intervals $(z,2z]$ starting at $z=r^2$. Brun–Titchmarsh gives $O(z/(\varphi(r)\log z))$ primes per interval since $\log(2z/r)\ge\tfrac12\log z$. Each prime costs $O(\log z/z)$, and there are $O(\log H)$ intervals. This proves (3).

Combining both parts of the mean gives the uniform bound

$$
 \mathbb E\!\sum_{\substack{p\mid V_r,\ p\le X\\r_p=r}}
          v_p(V_r)\log p\ll_\nu g\varphi(r)+\log H.                     \tag{4}
$$

Only $O(H)$ pairs have $A<\sqrt H$. On the others $\log A\ge\tfrac12\log H$. Apply Markov's inequality to (4) with $r=n$ and use (2) to get the first convergence statement. A pair lacking an exact-order prime above $X$ has the whole mass $L_n$ in (4). For large $n$ this costs at least $\tfrac14\varphi(n)\log H$ on $A\ge\sqrt H$, giving (1) after including the $O(1/H)$ proportion with smaller $A$.

## Summing all orders at an index

At $r\ge3$, (2) adds at most $\log r=O(\varphi(r))$ to (4) when counting the small-prime mass in the full $\Phi_r(A,B)$. The factors $\Phi_1=A-B$ and $\Phi_2=A+B$ each cost $O(\log H)$. Summing the expectations over $r\mid n$ and using $\sum_{r\mid n}\varphi(r)=n$ gives

$$
 \mathbb E\sum_{\substack{p\mid V_n\\p\le X}}v_p(V_n)\log p
     \ll_\nu gn+\tau(n)\log H.                                          \tag{5}
$$

Here the product $V_n=\prod_{r\mid n}\Phi_r(A,B)$ accounts for every valuation with its multiplicity. The uniform bound $(n-1)\log A\le\log V_n\le n\log A$ follows from $1-(B/A)^n\ge1-B/A\ge1/A$. Equation (5), Markov's inequality and $\tau(n)/n\to0$ now give the second convergence statement.

At $n=H$ this bounds the proportion with no prime of exact order $n$ above $n^2$ by $O(1/\log n)$. It also permits a cutoff $n^2(\log n)^a$ for each fixed $0\le a<1$, with exceptional proportion $O((\log n)^{a-1}+1/\varphi(n))$. These primes may occur with multiplicity. The exponent-one conclusion for a fixed pair in the exponent average uses abc. [Fixed-pair density argument](abc_average_order_radical.md)
