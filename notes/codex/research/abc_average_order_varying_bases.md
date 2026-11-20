# Searching several rational bases at a height-dependent prime cutoff

Let $A>B\ge1$ be coprime, $h=\log A$ and $V_n=A^n-B^n$. There is a version of the average radical estimate uniform in the height of $A/B$. It allows a different set of rational bases on every interval $N<n\le2N$. Put
$$
 \delta=1-\frac{1+\log\log2}{\log2},\qquad
 X_n(A)=n^2h(\log n)^a,\qquad 0\le a<\delta .
$$
For $a/2<b<\delta/2$, uniformly in the pair,
$$
  \sum_{N<n\le2N}\frac1{nh}
       \sum_{\substack{p\mid V_n\\p\le X_n(A)}}\log p
    \ll_{a,b}\frac{N}{(\log N)^{b-a/2}}.                               \tag{1}
$$

Suppose a search uses at most $O((\log N)^k)$ coprime rational bases on each such interval, with $k\ge0$. For a particular index it may select whichever base gives the smallest largest prime factor. If on infinitely many intervals at least $\gg N/(\log N)^\rho$ indices have one base with $P^+(V_n)\le X_n(A)$, where
$$
                               k+\rho<(\delta-a)/2,\qquad \rho\ge0 ,
$$
then the abc quality of the selected triples is unbounded. The height of each base can be chosen arbitrarily. This is a sufficient condition for disproof. No sequence realizing it is known here.

## Counting over exponents and over the search set

For each $p\nmid AB$ write $r_p=\operatorname{ord}_p(A/B)$. The uniform sieve gives
$$
 \sum_{\substack{p\le X\\p\nmid AB}}\frac{\log p}{r_p}
   \ll_b \frac{\sqrt{Xh}}{(\log(2+X/h))^b} .                             \tag{2}
$$
The scale at which the trivial bounds on these orders meet is $\sqrt{X/h}$. The divisor sieve on the shorter and longer factors of $p-1$ gives a constant independent of $h$. [Uniform sieve proof](abc_shifted_prime_unbalanced_sieve.md)

Use (2) with $X=(2N)^2h(\log(2N))^a$ in the order counting identity. The number of exponents up to $2N$ divisible by $r_p$ is $\lfloor2N/r_p\rfloor$. Dividing the resulting bound by $Nh$ proves (1), since $X/h$ depends only on the interval and $a$. Sum (1) over all bases in the search set. For a smooth index, the sum on the left over the bases bounds the normalized log radical of the selected $V_n$ from above. Dividing by the number of smooth indices shows that one selected example on each qualifying interval satisfies
$$
     \frac{\log\operatorname{rad}(V_n)}{nh}
       \ll(\log N)^{k+\rho+a/2-b}.
$$
Choose $k+\rho+a/2<b<\delta/2$. The radical of $B^n+V_n=A^n$ also includes $\operatorname{rad}(AB)$, whose log is at most $2h$. Thus the entire log radical divided by $nh$ tends to zero on a subsequence.

For indices with a bounded number of distinct prime factors, the pointwise criterion allows a different rational base at **every** index. There, the sufficient condition is $P^+(V_n)=o(n^2\log A)$. In the average criterion, the factor $(\log n)^a$ raises the cutoff at the cost of a hypothesis on the number of qualifying indices. [Pointwise bound](abc_few_index_primes.md) · [Fixed base and exact order](abc_average_order_radical.md)

The quantifier over the choice of base matters. For example, with $n=H$ fixed before choosing the pair, nearly all pairs $1\le B<A\le H$ have prime divisors of exact order $n$ larger than $n^2$ unconditionally. An exceptional selection is needed to realize the proposed search criterion. [Counting over a box of bases](abc_variable_seed_prime_mass.md) · [All-heights count at one order](abc_cyclotomic_smooth_seed_count.md)
