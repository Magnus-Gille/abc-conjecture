# A stronger radical bound at every composite index

On the primitive congruent-six quartic orbit, put $C_n=4w_n^4$ and $R_n=\operatorname{rad}(6a_nc_nd_nw_n)$. For every positive odd composite index, and also at every odd prime index whose $a_n$ has at least two distinct prime factors, one has effective bounds
$$
 \operatorname{rad}(a_n)\gg\frac{n^3}{(\log(2n))^9},\qquad
 \log C_n\ll R_n^{4/21}(\log(2R_n))^{24/7}.
$$
In particular an infinite sequence violating the latter effective estimate up to arbitrarily large constants would have to include infinitely many prime indices $q$ with $a_q=p^e$, $p<q^3$, and $e\gg q^2/\log(2q)$. All odd indices satisfy the [one-fifth bound](abc_full_quartic_one_fifth_radical.md).

## The largest prime with a bounded number of prime factors

If $a_m$ has $k\ge1$ distinct prime factors and largest prime $P$, the same quartic factorization over $K=\mathbf Q(\sqrt2,\sqrt3)$ as in the [one-fifth proof](abc_full_quartic_one_fifth_radical.md) gives
$$
                 P\gg_k m^2/(\log(2m))^{3k}. \tag{1}
$$
Indeed $F(x,y)=-8a_m^2$ and every prime of $a_m$ splits completely in $K$. For each rational prime keep only the three places supporting the three chosen linear factors of $F$. The number of places of $S$ is bounded in terms of $k$, its largest finite norm is $O(P)$ and at least $P$, and its regulator is $O_k((\log(2P))^{3k})$. Győry–Yu gives $m^2\ll_k P(\log(2P))^{3k}$. To obtain (1), separate $P\ge m^2$ from $P<m^2$. The unit case is effectively bounded.

The sequence $a_m$ is the denominator root of $[m](12,36)$ on $Y^2=X^3-36X$ at odd indices. Each prime of $a_m$ has exact rank some divisor $i>1$ of $m$ and exceeds $i$. Distinct ranks give distinct primes. Every sufficiently large odd rank occurs effectively, and $\operatorname{rad}(a_m)\gg m^{\tau(m)/2}$ follows by multiplying one prime at each divisor above the fixed cutoff. Also $\operatorname{rad}(a_q)\gg q^2/(\log(2q))^3$ for a prime index $q$. [Primitive divisors and effectivity](abc_full_quartic_divisor_sensitive_radical.md) · [Prime-index improvement](abc_full_quartic_one_fifth_radical.md)

## Composite indices

If $\tau(n)\ge6$, the primitive-divisor bound gives $\operatorname{rad}(a_n)\gg n^3$. When $n=qr$ for distinct primes, the prime supports of $a_q,a_r$ are disjoint; so is a primitive prime of rank $n$, which exceeds $n$. Multiplication gives $\operatorname{rad}(a_n)\gg n^3/(\log(2n))^6$. The finitely many indices under the effective cutoff are absorbed in the constant.

Every remaining composite index has the form $n=q^b$ with $b=2,3,4$. One can assume $q$ above the primitive-divisor cutoff since $b$ is bounded. Write $k=\omega(a_n)$. Every prime of $a_n$ exceeds $q$. If $k\ge3b$, their product already exceeds $n^3$. Otherwise (1) gives a largest prime $P\gg n^2/(\log(2n))^{3k}$, for an effective absolute constant since $k\le11$.

For $b=2$ and $k\ge4$, the product of $P$ and three other primes exceeds $n^{7/2}/(\log(2n))^{3k}$ up to a constant, which implies $\operatorname{rad}(a_n)\gg n^3$ since $k\le5$ in this case. With $k=3$, the other two primes exceed $q$, giving $\operatorname{rad}(a_n)\gg n^3/(\log(2n))^9$. If $k=2$, one prime has rank $q$ and the other rank $q^2$. If $P$ has rank $q$, the other prime exceeds $n$. If $P$ has rank $n$, the other prime is the entire radical of $a_q$ and hence is $\gg n/(\log(2n))^3$. Combining with the two-prime bound (1) gives the stated ninth power in both cases.

For $b=3$ or 4, select one primitive prime at each rank $q^i$ with $1\le i\le b$, choosing $P$ at its rank. Multiplying these lower bounds upgrades the base product $n^{(b+1)/2}$ by at least $P/n$, so it gives $\gg n^{(b+3)/2}/(\log(2n))^{3k}$. When $b=4$ this exceeds a constant times $n^3$. For $b=3$ and $k=3$ it already gives $\gg n^3/(\log(2n))^9$. For $b=3$ and $4\le k\le8$, an unselected prime exceeds $q=n^{1/3}$ and absorbs the entire logarithmic loss. This proves the claim for all composites.

## Prime indices and the full triple

At a prime index $q$ with at least three distinct primes of $a_q$, all exceed $q$, giving $\operatorname{rad}(a_q)>q^3$. With exactly two primes, (1) supplies one $\gg q^2/(\log(2q))^6$ and the other exceeds $q$.

Finally the [three primitive triples](abc_full_quartic_divisor_sensitive_radical.md) give $n^{18}\operatorname{rad}(a_n)\ll R_n^2(\log(2R_n))^{27}$, hence $\log(2n)\ll\log(2R_n)$. Substituting the bound just proved gives $n^{21}\ll R_n^2(\log(2R_n))^{36}$; use $\log C_n\asymp n^2$. The same conclusion holds if $a_q=p^e$ and $p\ge q^3$. In the residual prime-power case with $p<q^3$, the [effective logarithmic height estimate](abc_full_quartic_divisor_sensitive_radical.md) yields $e\log p=\log a_q\gg q^2$ for large $q$, proving the asserted growth of $e$.
