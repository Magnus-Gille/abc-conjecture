# What a third base-2 Wieferich prime would change in the Mersenne abc triples

Put $M_n=2^n-1$, $C_n=2^n$ and $R_n=2\operatorname{rad}(M_n)$. For the primitive triple $1+M_n=C_n$ define
$$
               L=\limsup_{n\to\infty}\frac{C_n}{R_n\log C_n}.
$$
If 1093 and 3511 are the only base-2 Wieferich primes, then
$$
             L=L_0=\frac{1093\cdot3511}{8\log2}=692046.9\ldots .
$$
If there is even one additional such prime, $L>24L_0$. Moreover $L=\infty$ if and only if there are infinitely many base-2 Wieferich primes. These alternatives concern logarithmic gain. A disproof of rational abc requires $C_n/R_n^{1+\varepsilon}$ to be unbounded for a fixed $\varepsilon>0$.

## Ordinary lifting and the first occurrence of a prime

For an odd prime $p$ put $r_p=\operatorname{ord}_p(2)$ and $w_p=v_p(2^{r_p}-1)$. Since $r_p\mid p-1$, one has $w_p=v_p(2^{p-1}-1)$. The Wieferich primes are precisely those with $w_p\ge2$. The lifting lemma gives $v_p(M_n)=w_p+v_p(n)$ for $r_p\mid n$ and zero otherwise. Therefore, exactly,
$$
 \frac{M_n}{\operatorname{rad}(M_n)}
       =\gcd(n,M_n)\prod_{r_p\mid n}p^{w_p-1}.                    \tag{1}
$$
In particular the entire factor from ordinary lifting is at most $n$. If the Wieferich set is finite, (1) proves abc on this family, since $C_n/R_n\ll n$. The unknown size of that set is relevant to proving a much sharper bound than abc on this particular family.

Write $U(n)=n/\gcd(n,M_n)$. Apart from the fixed scale $1/(2\log 2)$ and the factor $2^n/(2^n-1)\to1$, the expression defining $L$ is the product on the right of (1) divided by $U(n)$.

## The minimum loss for simultaneous prescribed orders

For $m\ge1$ form the smallest multiple $T(m)$ of $m$ which contains $r_s$ as a divisor for every odd prime $s\mid T(m)$. It exists: starting at $m$, adjoin missing orders by least common multiple. All prime powers in an order $r_s$ are at most $s-1$, so throughout the iteration the integer divides $\operatorname{lcm}(1,\ldots,m)$. The construction is monotone, and it commutes with taking least common multiples because the lcm of two stable integers is stable. Define $B(m)=2^{v_2(T(m))}$; in particular $B(m)\le m$.
Then
$$
                       \min_{m\mid n} U(n)=B(m).                      \tag{2}
$$
Indeed $U(n)=2^{v_2(n)}\prod_{s\mid n,\ s\text{ odd},\ r_s\nmid n}s^{v_s(n)}$ by (1)'s valuation calculation. The closure $T(n)$ equals the lcm of $n$ and the integers $T(r_s)$ for the odd primes in this product. Their 2-parts are at most $r_s<s$. Thus $U(n)\ge B(n)\ge B(m)$ when $m\mid n$. At $n=T(m)$ equality holds.

For a finite nonempty set $S$ of Wieferich primes put $m_S=\operatorname{lcm}_{p\in S}r_p$ and $A_S=\prod_{p\in S}p^{w_p-1}$. Formula (2) shows
$$
                           L\ge \frac{A_S}{2\log 2\, B(m_S)}.         \tag{3}
$$
To obtain arbitrarily large indices, take $T(m_S)p^j$ for any $p\in S$. They stay stable and retain their 2-part, and all specified ranks divide them. The right-hand side strictly increases on adjoining a new Wieferich prime $p$: its numerator gains at least $p$, while its denominator changes by a factor at most $B(r_p)\le r_p<p$.

If the full Wieferich set $W$ is finite and nonempty, **equality holds in (3) at $S=W$**. At each $n$, apply (2) to its active subset $S=\{p\in W:r_p\mid n\}$, then use monotonicity of $A_S/B(m_S)$ (taking the empty-set ratio to be 1). If $W$ is infinite, a direct bound avoids estimating the closure. For any $k$ selected primes take $n=\operatorname{lcm}_{p\in S}(p-1)$. Since all $p-1$ are even, $n\le2^{1-k}\prod_{p\in S}(p-1)$, while $U(n)\le n$ and $A_S\ge\prod_{p\in S}p$. Thus the normalized gain in (1) exceeds $2^{k-1}$. These indices are unbounded as $k$ grows. Conversely (1) bounds $L$ for every finite $W$.

## The numerical threshold

Direct modular powers give $(r_{1093},w_{1093})=(364,2)$ and $(r_{3511},w_{3511})=(1755,2)$. Their lcm is $49140=2^2 3^3\cdot5\cdot7\cdot13$ and is already stable, so its loss is 4. The indices $49140\cdot3^j$ witness $L\ge L_0$ unconditionally.

For every odd prime $p\ge53$ one has $B(r_p)\le(p-1)/6$. To see this, first consider an odd prime $s\ge29$. If $8\nmid r_s$, the 2-part of $r_s$ is at most $4\le(s-1)/6$. Otherwise $s\equiv1\pmod8$, so 2 is a quadratic residue and $r_s\mid(s-1)/2$. If $s-1$ has odd part at least 3, its order has 2-part at most $(s-1)/6$. In the remaining case $s=2^a+1$ prime, $a$ is a power of two and $a\ge8$ in this range. The order divides $2a\le 2^a/6$. For odd primes $s<29$ the 2-part of $r_s$ is at most 8, by inspection. Every order adjoined in forming $T(r_p)$ comes from a smaller prime, so the largest 2-part is at most $\max((p-1)/6,8)=(p-1)/6$.

The finite check excludes Wieferich primes below 53. Adjoining any third Wieferich prime $p$ to the verified pair multiplies (3) by at least $4p/\max(4,B(r_p))>24$. This establishes the gap. The identity and the finite bounds can be checked without factoring $2^{49140}-1$. [Standard-library verifier](abc_mersenne_rank_certificate.py)
