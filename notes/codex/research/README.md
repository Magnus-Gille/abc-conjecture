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

For fixed coprime integers $A>B\ge1$, an infinite sequence with bounded $\omega(n)$ and $P^+(A^n-B^n)=o(n^2)$ would give abc quality tending to infinity. The bound applies to every rate of decay and counts the divisor orders on both sides of $\sqrt X$. [Pointwise estimate](abc_few_index_primes.md)

For Mersenne triples, the prime divisors of the index determine a cutoff for the multiplicative order. Assuming abc, primes above this cutoff that occur just once in $2^n-1$ and have sufficiently high order contribute at least a fixed positive multiple of $n$ in log mass. [Order, prime size and multiplicity](abc_mersenne_coindex_prime_bound.md)

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
