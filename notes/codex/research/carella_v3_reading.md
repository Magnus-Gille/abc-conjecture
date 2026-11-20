# Carella v3 and the number of candidates in Corollary 4.1

The infinitude argument in the supplied version of *Note on the Exceptional Set in the ABC Conjecture* relies on a false counting estimate. The contradiction below uses the parameters and threshold printed in Corollary 4.1, pp. 12–13. It is independent of abc. [Supplied v3 manuscript](https://arxiv.org/abs/2608.16764v3)

## An elementary contradiction to (4.42)

Write $L=\log\log x$, $h=x^{3/5}$, $y=x^{1/(7L)}$ and $u=7L$. Corollary 4.1 counts integers $n$ in $(x,x+h]$ whose prime factors are all at most $y$ and whose number of distinct prime factors is at most $L+3\sqrt L$. Its lower bound is $\gg x^{3/5}\rho(7L)$. The Dickman estimate in the manuscript gives $-\log\rho(7L)=O(L\log L)=o(\log x)$, so this is at least $x^{3/5-o(1)}$.

Each counted integer satisfies

$$
\operatorname{rad}(n)\le y^{L+3\sqrt L}
=x^{1/7+3/(7\sqrt L)}=:R.
$$

Write $n=d s^2$ uniquely with $d$ squarefree. The number $d$ is a product of primes dividing $n$, so $d\le R$. Since $n\le2x$, even the count in the entire range up to $2x$ is at most

$$
\sum_{d\le R}\left\lfloor\sqrt{2x/d}\right\rfloor
\le 2\sqrt{2xR}=x^{4/7+o(1)}.
$$

The two exponents differ by $3/5-4/7=1/35>0$. Thus (4.42) is false for the stated parameters. The argument leaves intact the possibility of many smooth integers in this interval. The incompatible extra condition is the bound on their number of distinct prime factors.

## Where the analytic derivation goes wrong

Theorem 4.2, as stated on p. 7, assumes $u=o(\log\log y)$. The actual ratio $u/\log\log y=7L/(L-\log(7L))$ tends to 7. Moreover, the generating function (4.35) in the proof sketch of Theorem 4.7 has an incorrect Euler factor. With $t=p^{-s}$, the local series for the weight $z^{\omega(n)}$ is $1+zt/(1-t)$. Equation (4.35) gives $(1-t)^{-z}$. At $t^2$ the respective coefficients are $z$ and $z(z+1)/2$. The elementary count above shows that correcting the Euler factor while retaining (4.42) cannot succeed.

## What the construction in §5 would prove

Set $x=p^5$ with $p$ prime. If a qualifying $c$ existed, then $b=p^5$ and $a=c-p^5$ would be positive, satisfy $a+b=c$, and be coprime because $p>y$ for large $p$. The bounds $\operatorname{rad}(a)\le a\le x^{3/5}$, $\operatorname{rad}(b)=p=x^{1/5}$ and $\operatorname{rad}(c)\le x^{1/7+o(1)}$ would give $\operatorname{rad}(abc)\le x^{33/35+o(1)}$. For example, at $\varepsilon=1/35$ the resulting ratio $c/\operatorname{rad}(abc)^{36/35}$ grows at least as $x^{37/1225-o(1)}$. Thus finding one such $c$ for infinitely many distinct primes $p$ would suffice for a disproof. The claimed positive-proportion count does not establish this.

In fact almost every prime fifth-power interval misses the proposed candidates entirely. To see this, for fixed $\sigma>0$ use

$$
\#\{n\le X:\operatorname{rad}(n)\le Z\}
\le ZX^\sigma\prod_q\left(1+\frac{1}{q(q^\sigma-1)}\right),
$$

where the product ranges over primes. This follows by summing $ZX^\sigma/(n^\sigma\operatorname{rad}(n))$ and factoring its Dirichlet series. The product converges for every fixed $\sigma>0$. For primes $P<p\le2P$, the intervals $(p^5,p^5+p^3]$ are disjoint, their integers are $O(P^5)$, and every proposed candidate has radical at most $P^{5/7+o(1)}$. Taking $\sigma=1/35$ bounds the number of these intervals containing a candidate by $O(P^{6/7+o(1)})$. There are asymptotically $P/\log P$ primes in the range. The resulting proportion tends to zero. This still allows an infinite sparse subsequence. Neither its existence nor abc itself is decided by these bounds.
