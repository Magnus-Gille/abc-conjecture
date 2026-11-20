# Short and sparse congruence relations for the square conic

For the exact modulus in the [growing-primes construction](abc_square_conic_growing_primes.md), the rank-eight lattice has shortest coefficient 1-norm 21. Its unique shortest vector up to sign has five nonzero entries. It gives a fully factored ABC triple of quality **1.0416634433**. At rank 100, an explicit relation with 95 nonzero entries lies inside the theorem's weighted packing radius. A second relation with 75 nonzero entries gives a stronger radical gain at a larger height. Every relation supported on at most two of the 100 generators has coefficient 1-norm at least **2.75013 × 10¹⁴⁰**. These are finite results.

## Arithmetic and exact conventions

Use every prime up to the rank in D, followed by the first d odd split primes above d, just as in the theorem. For each split prime choose positive integers b,a minimizing b²+2a² among solutions of |b²−2a²|=ℓ with b²+2a²≤3ℓ. The last inequality is exactly the embedding balance bound in the theorem because (1+√2)²+(1+√2)⁻²=6. Searching a≤√(3ℓ/2) is exhaustive. The choice determines one ideal and representative without a free unit choice. Use precisely the theorem's H,U,E, k and t, with M=Dᵏ3ᵗ. Arb interval arithmetic proves the floors and the two inequalities M≤U/(2E)<3M. The records start at rank four. [Parameters and lattice code](abc_conic_short_kernel.py)

At each pʲ exactly dividing M, the code finds a projective generator by checking its N/ℓ powers for every prime factor of the stated group order N and verifying its Nth power is scalar. Discrete logarithms are lifted a digit at a time and checked by modular exponentiation. This gives ordinary linear congruences on the integer coefficient vector. For a congruence modulo a prime power q, choose the row of the current basis whose image has smallest common divisor g with q. Subtract an appropriate multiple of it from every other row, then multiply that row by q/g. The resulting basis lies in the kernel and has the same index as the image of the congruence, so it spans the full kernel. [Congruence reduction](abc_conic_short_kernel.py)

Let z be a relation and α=b+a√2 its integral product using conjugates at negative entries. All split norms are odd, b is odd and a is even. Thus C=S² and rad(ABC)=rad(JabS), with S=b²+2a² and J=b²−2a². Set R to the product of the supported split primes and V to the product of p raised to vₚ(a)−1 over p≤d. Two lower bounds for the logarithmic radical gain are
\[
 G_M=\log(M/D)-\log R+\log(\sqrt2/4),\qquad
 G_{\rm att}=\log V-\log R+\log(S/|ab|).
\]
The second follows from rad(a)≤|a|/V and rad(b)rad(S)≤|b|S. The first is the theorem's original certificate. The code computes every displayed valuation by directly multiplying α modulo pʲ⁺¹ until the first nonzero coefficient is reached. In particular vₚ(v)=vₚ(a) for odd p≤d and v₂(v)=v₂(a)+1. The true log height is 2 log S. Computing both embeddings with Arb avoids writing all digits of large integers. A separate integer verifier forms the exact pair, checks primitivity, M|a, the norm factorization, the conic identity and the valuations, then recomputes log C and the stronger gain from those integers. [Integer verifier](abc_conic_kernel_verify.py)

## Small-rank minima and a fully factored point

| Rank | k,t | Minimum coefficient 1-norm | Minimizers up to sign | Minimum on at most two coordinates |
|---:|---:|---:|---:|---:|
| 4 | 2,1 | 4 | 2 | 4 |
| 5 | 2,2 | 8 | 1 | 32 |
| 6 | 4,0 | 16 | 1 | 48 |
| 7 | 3,1 | 15 | 1 | 600 |
| 8 | 4,1 | 21 | 1 | 5,502 |

The proof enumerates the coefficient 1-norm ball on each half of the coordinates up to a known witness length, and matches opposite projective logarithm signatures. For each left signature it retains every shortest vector, handling zero separately. A longer left half with the same signature cannot be part of a globally shortest nonzero vector. At rank eight there are 143,529 half-vectors on each side. All reported small-rank triples have been factored and their residual prime factors tested for primality. [Exhaustive search](abc_conic_small_kernel.py) · [Exact small-rank records](abc_conic_small_kernel.jsonl)

At rank eight the split primes are 17,23,31,41,47,71,73,79, M=5,834,430,000, and
\[
  z=(0,0,3,1,2,-9,0,6),\qquad
  (|b|,|a|)=(10437080549083800673,6279384559900410000).
\]
The exact valuations of a at 2,3,5,7 are 4,7,4,6, giving respective exponents **11,14,8,12** in B=2v². Here log C=176.2568178376, G_att=4.6518538467 and log(C/rad(ABC))=7.0497491195. The full factorization accounts for the difference by 11² exactly dividing S. The original G_M is −3.5296204924. The exact gain for this point uses the additional attained exponents and the scale factor S/|ab|.

## Rank 100

Here D is the product of the 25 primes at most 100, k=8, t=42 and H=394,542.38813. Each row is a verified relation in this same lattice. The first uses BKZ with block size 38 on the first 95 generators. The second uses LLL on the first 75 generators. A positive certificate divided by log C gives a finite lower bound on the exponent in C/rad(ABC)≥Cᵋ.

| Nonzero coordinates | Coefficient 1-norm | Weighted norm / H | True log C | Digits in C | G_M | G_att | G_att / log C |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 95 | 45,867 | 0.95429 | 597,239.97525 | 259,379 | 24.51481 | 27.28740 | 0.00004569 |
| 75 | 388,331 | 7.821 | 4,844,985.61191 | 2,104,151 | 166.70684 | 171.08887 | 0.00003531 |

For support 95, v₂(a)=9, v₃(a)=50 and every other prescribed prime has exponent 8 in a. For support 75, v₂(a)=v₅(a)=9, v₃(a)=50, and every remaining prescribed prime has exponent 8. Direct integer construction gives 861,636 and 6,989,837 bits in the two C values. The second row uses a vector outside the weighted packing radius. Exact signed coefficients, powers and kernel determinants are in the linked records. LLL and BKZ give upper bounds on shortest lengths at these ranks. [Rank-100 block reduction](abc_conic_bkz38_kernel.jsonl) · [LLL census](abc_conic_short_kernel.jsonl) · [Block-reduction code](abc_conic_bkz_kernel.py)

## An exact two-coordinate obstruction

For every pair of coordinates, take an exact basis of its congruence kernel and perform two-dimensional Gauss reduction to get a,b with |a|₂≤|b|₂ and |a·b|≤|a|₂²/2. Lines parallel to a have separation at least √3|a|₂/2. Since a itself has coefficient 1-norm at most √2|a|₂, a shortest vector can only lie on the lines with b-coefficient 0 or ±1. On the latter lines, minimize |b₁+ka₁|+|b₂+ka₂| over integral k. The integers next to the two coordinate zeros suffice by convex piecewise linearity. This proves the minimum in each pair rigorously and covers singleton supports as well. [Two-coordinate search](abc_conic_two_sparse.py) · [Exact minima and coefficients](abc_conic_two_sparse.jsonl)

At rank 32 the minimum is 275068701973866457421856326244240. At rank 100, the best of all 4,950 pairs uses the split primes 1,321 and 1,361 and has minimum 2.750131659240116… × 10¹⁴⁰. The bound applies to supports of size at most two. Neither the exact low-support minima nor the constructive large-support witnesses settle the asymptotic criterion with a fixed missing fraction of coordinates and linear coefficient 1-norm.

## Reproduction

The scripts require SymPy and python-flint. The block-reduction script additionally uses fpylll 0.6.4 and cysignals 1.12.6. Run from the scratch directory.

~~~sh
python abc_conic_short_kernel.py 4 5 6 7 8 10 12 16 20 32 50 75 100
python abc_conic_small_kernel.py
python abc_conic_two_sparse.py 4 5 6 7 8 10 12 16 20 32 50 75 100
python abc_conic_bkz_kernel.py 100 97 95 92 90 --block 38 --loops 5
python abc_conic_kernel_verify.py abc_conic_bkz38_kernel.jsonl --dimension 100 --size 95
python abc_conic_kernel_verify.py abc_conic_short_kernel.jsonl --dimension 100 --size 75
~~~
