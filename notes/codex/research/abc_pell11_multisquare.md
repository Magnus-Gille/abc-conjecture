# Three exact squares for the full rank-11 Pell factor

For the primitive full factor and orbit in [the Pell census](abc_pell11_early_squares.md), the earliest positive index at which three distinct primes at most ten million divide the full factor to exponent at least two is **707,104,450,727**. It is the only such index through two trillion. The three prime exponents at that index all equal two.

| Prime | Least period of its square divisibility | Classes per period | Index residue | Absolute full factor divided by the square, modulo the prime |
|---:|---:|---:|---:|---:|
| 683 | 77,862 | 14 | 74,831 | 467 |
| 1,409 | 45,088 | 2 | 32,583 | 965 |
| 2,707 | 3,665,278 | 50 | 2,684,245 | 6 |

The search starts with all 6,607 norm-compatible primes at most ten million. The established local census gives projective periods and identifies the 229 primes whose projective root sets miss the orbit. For each of the remaining 6,378 primes, the class generator factors the full parameter form modulo the prime, finds every visited root by a discrete logarithm, and solves its nondegenerate linear lifting equation modulo the prime square. It emits all 356,138 lifted classes, including classes whose first representative could have exponent greater than two. [Local census](abc_pell11_square_periods.py) · [Class generation](abc_pell11_multisquare_classes.py)

To exhaust the index interval, order the 6,378 primes by the number of square classes per index. Treat the first 32 as one group. Emit every pair intersection from that group by generalized CRT and every individual occurrence of a prime outside it. The two streams contribute 51,154 and 5,144,726 events, respectively. Any triple gives at least two events at its index. This follows separately with zero, one, two or three of its primes inside the first group. At every index with at least two events, recover the outside primes from their events and test all 32 inside primes by residue membership. This certifies completeness throughout the stated rectangle. [Interval enumeration](abc_pell11_multisquare_scan.cpp)

For the displayed triple the full simultaneous square-divisibility set has 348 residues in its primitive period 3,216,869,590,168,992. Its first three positive representatives are 707,104,450,727, 13,432,128,644,455 and 49,993,487,457,831. To obtain the primitive period, intersect residue sets by generalized CRT. The translations preserving a residue set form a subgroup of the cyclic group, whose order divides both the ambient modulus and the number of residues. Test each such divisor explicitly. [Support periods and modular checks](abc_pell11_multisquare_crt.py)

Writing D for that primitive period, over each square-support class modulo D and for each of the three primes p, precisely one digit of the step modulo p raises its valuation to at least three. This follows from the nonzero Hensel tangent and from the fact that D divided by each local square-support period is coprime to its prime. The local period is half of the projective lifted period, so taking twice its step gives the nonzero projective tangent. The three digits can be chosen independently. Every square-support class therefore occurs in the projection of the exact-exponent-two set. Any period of the exact set is consequently a multiple of D, and its multiple must preserve the one excluded digit at each prime. The least period for three exponents *equal* to two is 8,380,181,172,220,401,662,014,368.

For the four prescribed primes 683, 1,409, 2,179 and 2,267, the earliest simultaneous square index is 97,751,649,103,127,879. Their full square support contains 340 residues in primitive period 127,592,617,713,945,507,360. The absolute full-factor quotients modulo the four primes are 486, 580, 679 and 1,187. A separate eightfold witness is 4,574,441,773,427,136,006,251,480,889,031,807,871,431,605,383. Its prime list in construction order is 683, 1,409, 2,707, 5,897, 82,633, 2,267, 2,179 and 24,179. The respective absolute full-factor quotients modulo those primes are 411, 515, 1,390, 5,786, 24,437, 2,089, 1,261 and 1,253. All fifteen pairs across the three examples also pass the independent multiplication-by-11 denominator test modulo the fifth power of the prime. [Independent scalar test](abc_pell11_square_verify.py)

For the alternative four primes 683, 2,267, 4,027 and 13,883, the earliest simultaneous square occurs at 82,615,750,400,795,551. There are just 11 simultaneous square classes in primitive period 1,256,815,907,183,783,336,526. The four absolute quotients are 498, 2,210, 462 and 12,989 modulo the respective primes. This gives an upper bound on the earliest quadruple over all allowed primes.

The commands below run from the scratch directory with SymPy and python-flint installed.

~~~sh
python abc_pell11_multisquare_classes.py > /tmp/pell11-square-classes.txt
g++ -std=c++17 -O3 abc_pell11_multisquare_scan.cpp -o /tmp/pell11-scan
/tmp/pell11-scan /tmp/pell11-square-classes.txt 1 2000000000000 32
python abc_pell11_multisquare_crt.py /tmp/pell11-square-classes.txt --extend 5
python abc_pell11_multisquare_crt.py /tmp/pell11-square-classes.txt --primes 683 1409 2179 2267
~~~
