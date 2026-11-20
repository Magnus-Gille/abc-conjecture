# Rational abc research notes

These notes investigate the rational abc conjecture. A proof would give an upper bound $C\ll_\varepsilon\operatorname{rad}(ABC)^{1+\varepsilon}$ for every fixed $\varepsilon>0$ and every primitive positive triple $A+B=C$. The computations and subfamily results here leave this question open.

## A reduction for general rational abc

For every fixed $k\ge3$, one can construct a family of primitive triples for which $\log C\ll_k R^{1/k}(\log(2R))^3$, where $R=\operatorname{rad}(ABC)$. Proving the abc power bound for any one of these entire families would prove it for every primitive triple. The proof gives a degree-three example with five rational marked points and explains why the logarithmic bound does not transfer back to a proof of abc. [Proof and cubic example](abc_marked_rational_radical_bounds.md) · [Cubic verifier](abc_marked_rational_cubic.py)

For the familiar case of primitive Pythagorean triples, the estimate for $A+B=C$ with all three terms squares is $\log C\ll R^{1/5}(\log(2R))^3$. The proof uses six elementary sums whose radicals can be multiplied exactly. [Pythagorean proof](abc_pythagorean_stewart_yu.md)

The two extra cubic factors can contribute a radical of order $z^2$ on a positive proportion of inputs of height $z$. Even on explicit abc hits with gain at least a constant times any prescribed power $(\log z)^\theta$, $0<\theta<2$, all six orderings can introduce more than every fixed power of $\log z$ in new primes. [Density and non-Wieferich primes](abc_cubic_radical_loss.md) · [Simultaneous construction](abc_cubic_ordering_hits.md)

## Mersenne triples

For $1+(2^n-1)=2^n$, the factor in the radical loss coming from ordinary lifting is exactly $\gcd(n,2^n-1)$. The remaining loss is from base-2 Wieferich primes. At the logarithmic scale this gives an explicit gap for a third Wieferich prime. At the scale of a fixed abc exponent, it suffices to track first occurrences at divisors $r\mid n$ with $n/r\le(\log n)^K$ for any fixed $K>0$, taking the limsup over all $n$. [Logarithmic gain](abc_mersenne_logarithmic_gain.md) · [Fixed-exponent criterion](abc_mersenne_short_rank_window.md)

An infinite sequence of prime powers $n$ on which the largest prime divisor of $\Phi_n(2)$ stays below $\alpha\varphi(n)^2$ for one fixed $\alpha<(\log2)/2$ would disprove abc. Through $n=10000$, the smallest observed ratio to $\varphi(n)^2$ is $89/100$, certified at $n=11$. [Proof and finite census](abc_mersenne_quadratic_prime_threshold.md) · [Reproduce the census](abc_mersenne_quadratic_prime_scan.py)

For almost every exponent $n$, primes below $n^2(\log n)^a$ contribute $o(n)$ to $\log\operatorname{rad}(A^n-B^n)$, for fixed coprime $A>B\ge1$ and each $0\le a<0.0860713\ldots$. If abc holds, large primes of exact order $n$ occurring once carry asymptotically $\varphi(n)\log A$ in density. A complete census found exactly 20 indices $2\le n\le10{,}000$ with $P^+(2^n-1)\le n^2$, the last at 60. [Proof and counterexample conditions](abc_average_order_radical.md) · [Census](abc_mersenne_all_indices_scan.py) · [Exact average identity](abc_average_order_check.py)

For Mersenne triples, the prime divisors of the index determine a cutoff for the multiplicative order. Assuming abc, primes above this cutoff that occur just once in $2^n-1$ and have sufficiently high order contribute at least a fixed positive multiple of $n$ in log mass. [Order, prime size and multiplicity](abc_mersenne_coindex_prime_bound.md)

For \(2^m-1\), a prime of exact order \(m\) occurs to odd exponent at every odd prime power \(m=p^k\) and every twice-prime-power \(m=2p^k\) except \(m=6\). Here \(p\) ranges over all odd primes. [Elementary square-gap proof](abc_mersenne_prime_power_parity.md)

There is also an explicit construction in the opposite direction. At every $n=4m$ with $m$ odd, Aurifeuillian factorization gives $P^+(2^n-1)\le e^2\,2^{\varphi(m)}$. Taking $m$ to be an odd primorial produces a subexponential upper bound on an infinite sequence. [Integer factorization and size bound](abc_mersenne_constructed_smooth_indices.md)

## Differences of powers with varying bases

For indices with bounded $\omega(n)$, the condition $P^+(A^n-B^n)=o(n^2\log A)$ forces abc quality to tend to infinity, even when the coprime pair $A>B$ changes at every index. An average estimate allows a set of candidate pairs on each doubling interval and a cutoff beyond $n^2\log A$. [Pointwise estimate](abc_few_index_primes.md) · [Uniform average and search criterion](abc_average_order_varying_bases.md)

At the fixed index $n=H\to\infty$, all but an $O(1/\log H)$ fraction of coprime pairs $B<A\le H$ have a prime factor of $A^n-B^n$ above $H^2$ of exact order $n$. Counting over all heights at a fixed $n\ge7$, at most $\exp(O_C(n^2/\varphi(n)))$ pairs have even their cyclotomic factor $\Phi_n(A,B)$ supported on primes up to $Cn^2$. [Prime powers averaged over the pairs](abc_variable_seed_prime_mass.md) · [All-heights count](abc_cyclotomic_smooth_seed_count.md)

At the cutoff $n^2$, a complete search over the 489 coprime pairs $1\le B<A\le40$ and all $2\le n\le300$ found 253 smooth cyclotomic factors and 88 smooth full differences. The highest abc quality among the latter was $4\log7/\log210$ at $1+2400=2401$. [Results and disproof criterion](abc_cyclotomic_smooth_seed_count.md) · [Verifier](abc_variable_base_smooth_scan.py)

For the four sextic orders $7,9,14,18$, only two of 304,460 rows at $A\le500$ have a squared prime larger than $A^2$. The order-14 example at $(A,B)=(223,181)$ gives abc quality $1.080786\ldots$. At order 12 no prime above $A^2$ can occur twice, yet abc on all twelfth-power triples remains equivalent to the general conjecture. [Proof, examples and transfer](abc_cyclotomic_large_square_twists.md) · [Census](abc_cyclotomic_large_square_scan.py)

At $n=7,9$, for every fixed $\varepsilon>0$ the actual exceptions $A^n>\operatorname{rad}(AB(A^n-B^n))^{1+\varepsilon}$ among $B<A\le H$ have count $O(H^{2-c})$ for some $c>0$. At $\varepsilon=1/20$ the exponents are $16/9+o(1)$ and $12/7+o(1)$, respectively. Through $H=500$ the exact exception counts are 21 and 49. [Counting proof and maximum-quality examples](abc_sextic_power_exception_count.md) · [Verifier](abc_sextic_power_quality_scan.py)

At a fixed prime of primitive order $n$, the sharp limsup of $(v_p(A^n-B^n)-1)\log p/\log A$ over positive primitive base pairs is 2. A lattice construction attains the threshold to bounded additive error in the logarithm. Searching for a single prime that guarantees quality above $21/20$ at $n=7,9$ found just two seeds in three ranges reaching $p=2{,}000{,}000$ or $e=300$. [Sharp fixed-prime bound and search ranges](abc_fixed_prime_power_approximation.md) · [Hensel verifier](abc_cyclotomic_hensel_search.py)

For every coprime pair, every order of the form $2^i3^j$ with $j\ge2$ and $2^i7^j$ with $j\ge1$ has a prime occurring to odd exponent in the corresponding power difference. The underlying rational square classifications at orders 7, 9, 14 and 18 hold at all heights. [Pointwise theorem and product bounds](abc_cyclotomic_odd_primitive_grid.md) · [Seventh-order descent](abc_cyclotomic_seventh_square_points.md) · [Ninth-order descents](abc_cyclotomic_sextic_square_points.md)

Fix a finite set of index primes \(S\). Across all coprime bases and all \(S\)-smooth orders with \(\varphi(m)\ge6\), only \(O_S(Y(1+\log Y)^{C_S})\) triples have product at most \(Y\) of the exact-order primes outside \(S\) occurring to odd exponent. This gives \(\operatorname{sf}_{S^c}(A^N-B^N)\gg_S N^{\tau(N)/2}\) at every \(S\)-smooth \(N\), uniformly in both bases. [All-heights proof and simultaneous density bound](abc_cyclotomic_smooth_order_parity.md)

For \(S=\{2,3\}\) the universal odd-valuation assertion holds at exactly the orders outside \(1,2,3,4,6\). The constant in the full-difference lower bound can be taken as \(1/144\). At orders 5 and 10 each assertion fails for infinitely many bases, although at least one of the two orders always works. [Explicit products and the order-3/6 alternative](abc_cyclotomic_odd_primitive_grid.md) · [Quartic descents and the fifth-order examples](abc_cyclotomic_quartic_odd_primitive.md)

For any fixed \(e\ge3\), the all-heights count also holds for the product of primes whose valuations are nonzero modulo \(e\), at every \(S\)-smooth order with \(\varphi(m)\ge4\). The four-branch-point cover cancels the base denominator even when \(e\) does not divide the degree. [Proof and sharp degree threshold](abc_cyclotomic_smooth_order_higher_powers.md)

A separate mean bound controls the amount by which prime exponents exceed $\max(1,\varphi(r)/2-1)$ at each exact order $r\le H^{2-\nu}$ for coprime pairs of height at most $H$. [Mean multiplicity and radical bounds](abc_power_row_excess.md)

## The primitive quartic family

The family $a^4+3b^2=4w^4$ has a complete parametrization by the odd multiples of $(-3,9)$ on $y^2=x^3-36x$. The coordinates $a,c,d,w$, where $|b|=cd$, are pairwise coprime. Write $s(m)$ for the product of the primes occurring to odd exponent in $m$. [Parametrization](abc_full_quartic_signature.md)

| Question | Result and verification |
|---|---|
| What can be proved for the height of every triple in this family? | For the full radical $R=\operatorname{rad}(6awcd)$, one has $\log(4w^4)\ll R^{1/6}(\log(2R))^{5/2}$. The proof bounds the radical of $aw$ through elliptic and Lucas sequences and the radical of $cd$ through a primitive sum. [One-sixth exponent](abc_full_quartic_one_sixth_radical.md) · [Unit-equation estimate](abc_full_quartic_one_fifth_radical.md) · [Radical identity and numerical example](abc_full_quartic_divisor_sensitive_radical.md) |
| How often can the squarefree part of $a\lvert b\rvert w$ be at most $Y$? | The count is $O(Y^{1/8-\eta})$ for some absolute $\eta>0$, over indices of unrestricted size. [Sieve proof](abc_full_quartic_four_arm_inverse_sieve.md) · [Multiplicity on each coordinate](abc_full_quartic_four_squarefree_parts.md) |
| How large can an index with small squarefree part be? | For $n>1$ and squarefree part at most $Y$, one has $n\le Y^{1/4}/2$ throughout the explicit range $Y\le4(11210216592196440-1)^2$. [Proof](abc_full_quartic_four_arm_prefixes.md) · [Character table verifier](abc_full_quartic_four_arm_prefixes.py) |
| Which parts occur through $10^{19}$? | Exactly three, at indices 1, 3 and 5. [Values, proof and programs](abc_full_quartic_total_kernel.md) |
| Can $w$ be a perfect power? | For every $2\le k\le10^9$, the only primitive solutions with $w=z^k$ are $(a,b,z)=(1,\pm1,1)$. [Descent and exponent census](abc_full_quartic_perfect_power_census.md) · [Independent verification](abc_congruent_six_exponent_trace_audit.txt) |
| How close do these results come to a counterexample? | The ratio $C/(\operatorname{rad}(ABC)\sqrt{\log C})$ is unbounded along a subsequence. A disproof requires $C/\operatorname{rad}(ABC)^{1+\varepsilon}$ unbounded for one fixed $\varepsilon>0$. [Subsequence proof](abc_full_quartic_smooth_index_radical.md) · [Mixed valuations and abc quality](abc_full_quartic_twin_and_mixed_valuations.md) |

## Other investigations and manuscript readings

The collection includes earlier attempts, conditional results and finite experiments. Their hypotheses and ranges are recorded in the individual notes. The literature review links to the two supplied manuscript versions. The readings examine Soulé's treatment of exceptional fibers and the size of the candidate set in Carella's Corollary 4.1. [Literature review](abc_literature_update.md) · [Soulé v1](soule_v1_reading.md) · [Carella v3](carella_v3_reading.md)

For work beyond the quartic family, the fixed-gap notes study the squarefree parts of two integers at a fixed difference. Another route bounds the squarefree parts of triples of consecutive integers by estimating Pell regulators. [Fixed differences](abc_fixed_gap_variable_square_kernel.md) · [Consecutive integers](abc_consecutive_powerful_kernels.md)

## Reproducing the calculations

Run the following in this directory. The first three programs use the Python standard library and check the two main descent calculations and the small-index kernel arithmetic. The C++17 program checks the complementary squarefree-part sieve through five billion. The linked proofs explain how the finite calculations apply to indices of unrestricted size.

```sh
python3 abc_full_quartic_square_classification.py
python3 abc_full_quartic_cube_split17.py
python3 abc_full_quartic_total_kernel.py
c++ -O3 -std=c++17 abc_full_quartic_complementary_census.cpp -o /tmp/abc-quartic-complement
/tmp/abc-quartic-complement
```

For the exponent calculation, run `python3 abc_congruent_six_exponent_trace_sieve.py`. The separate audit uses PARI/GP through a Python binding (`cypari2` or `cypari`) and a C++17 compiler. Its module docstring gives the exact commands. Each research note links its other prerequisites and, where applicable, the programs and numerical certificates used in its argument. [Audit instructions](abc_congruent_six_exponent_trace_audit.py)
