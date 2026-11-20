# Rational abc research notes

These notes investigate the rational abc conjecture. A proof would give an upper bound \(C\ll_\varepsilon\operatorname{rad}(ABC)^{1+\varepsilon}\) for every fixed \(\varepsilon>0\) and every primitive positive triple \(A+B=C\). The computations and subfamily results here leave this question open.

## The primitive quartic family

The family \(a^4+3b^2=4w^4\) has a complete parametrization by the odd multiples of \((-3,9)\) on \(y^2=x^3-36x\). The coordinates \(a,c,d,w\), where \(|b|=cd\), are pairwise coprime. Write \(s(m)\) for the product of the primes occurring to odd exponent in \(m\). [Parametrization](abc_full_quartic_signature.md)

| Question | Result and verification |
|---|---|
| What can be proved for the height of every triple in this family? | For the full radical \(R=\operatorname{rad}(6awcd)\), one has \(\log(4w^4)\ll R^{4/19}(\log R)^{54/19}\). The proof tracks exactly which primes occur in three related sums, then uses a primitive divisor at each sufficiently large elliptic index. [Proof and numerical example](abc_full_quartic_divisor_sensitive_radical.md) |
| How often can the squarefree part of \(a|b|w\) be at most \(Y\)? | The count is \(O(Y^{1/8-\eta})\) for some absolute \(\eta>0\), over indices of unrestricted size. [Sieve proof](abc_full_quartic_four_arm_inverse_sieve.md) · [Multiplicity on each coordinate](abc_full_quartic_four_squarefree_parts.md) |
| Which parts occur through \(10^{19}\)? | Exactly three, at indices 1, 3 and 5. [Values, proof and programs](abc_full_quartic_total_kernel.md) |
| Can \(w\) be a perfect power? | For every \(2\le k\le10^9\), the only primitive solutions with \(w=z^k\) are \((a,b,z)=(1,\pm1,1)\). [Descent and exponent census](abc_full_quartic_perfect_power_census.md) · [Independent verification](abc_congruent_six_exponent_trace_audit.txt) |
| How close do these results come to a counterexample? | The ratio \(C/(\operatorname{rad}(ABC)\sqrt{\log C})\) is unbounded along a subsequence. A disproof requires \(C/\operatorname{rad}(ABC)^{1+\varepsilon}\) unbounded for one fixed \(\varepsilon>0\). [Subsequence proof](abc_full_quartic_smooth_index_radical.md) · [Mixed valuations and abc quality](abc_full_quartic_twin_and_mixed_valuations.md) |

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
