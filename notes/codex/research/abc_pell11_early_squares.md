# First square divisors of the full rank-11 form on the Pell orbit

Write \(\epsilon=1+\sqrt2\), \(b_n+a_n\sqrt2=\epsilon^n\), and \(F_n=F_{11}(a_n,b_n)\) with the primitive degree-100 full CM form. For every prime \(p\le10^9\) and every nonzero integer \(n\) with \(p^2\mid F_n\),
\[
                     \frac{\log p}{|n|}\le\frac{\log683}{1213}
                           =0.0053804574275\ldots .
\]
Equality occurs only at \(p=683,n=1213\), where the valuation is exactly two. The entire rectangle \(-3900\le n\le4096,\ p\le10^9\) contains three pairs with square divisibility, all of exact exponent two. The normalized signed form used here is \(F_n=2^{-125}S^{50}G_{11}(-8H/S)\), which is negative on real primitive pairs. [Definition and CM identification](abc_cm_twist_sharp_depth.md) · [Exact rectangular search](abc_pell11_early_squares.py)

| \(n\) | \(p\) | \(G_{11}(-8H/S)/p^2\bmod p\) | \(\lvert F_n\rvert/p^2\bmod p\) |
|---:|---:|---:|---:|
| \(-3031\) | 683 | 84 | 219 |
| \(1213\) | 683 | 671 | 606 |
| \(3706\) | 1409 | 57 | 1365 |

For all primes \(p\le10^7\), the least positive index of exact exponent two was computed without an index cutoff. Of 6,607 compatible primes, 6,378 occur on the Pell orbit. Ranked by their own best \(\log p/n\), the first three primes are \(683,1409,65099\). The third is the only one of the 6,607 with a positive exact-square index \(n<p\). Its index, 13707, is just one projective period beyond a root at 687. At the other extreme, the largest first index was \(7\,463\,886\,553\,802\), for \(p=8\,239\,177\). [All prime periods and first indices](abc_pell11_square_periods.csv) · [Period search](abc_pell11_square_periods.py)

| \(p\) | Projective period \(m\) | Projective root classes visited | First positive exact-square index \(n\) | \(\lvert F_n\rvert/p^2\bmod p\) |
|---:|---:|---:|---:|---:|
| 683 | 228 | 28 | 1213 | 606 |
| 1409 | 64 | 4 | 3706 | 1365 |
| 65099 | 13020 | 28 | 13707 | 17802 |

## Exhausting the early indices

At \(p\ne2,11\), a necessary condition for \(p\mid F_n\) is
\[
                         p=(1+22h)^2+242b^2,\qquad h\in\mathbb Z,\quad b\ge1 .
\]
Indeed the initial abscissa is \(t=-8H/S\), with \(S=b_n^2+2a_n^2,\ H=S+2a_nb_n\). A root has good reduction on its twist. An odd-order point must be a double, and its twist abscissa \(-8H^2\) forces \(-2\) square modulo \(p\). Over such a split prime, the Frobenius multiplier fixes a full \(11\)-torsion generator up to sign, so its two coordinates are congruent to \((\pm1,0)\bmod11\). Sign and conjugation give the form above; the real coordinate is odd. Conversely, every prime of that form has 50 full abscissas and 100 distinct projective parameter roots. At the remaining primes the signed form equals 1 modulo 2 and 10 modulo 11 throughout the Pell orbit, verified over the full pair periods 2 and 24. [CM Frobenius and root counts](abc_cm_twist_repeat_density.md) · [Exceptional-prime verification](abc_pell11_square_verify.py)

There are 508,279 such primes through \(10^9\). The search enumerates the norm lattice and proves primality by an Eratosthenes sieve on \(1\bmod22\). It multiplies the primes into a squarefree integer \(D\) of 14,421,126 bits. Exact Pell coordinates give each \(F_n\): if \(s+t\sqrt2=\epsilon^{2n}\), then \(S=s,\ H=s+t\). The content \(2^{125}\) comes from the gcd of all coefficients of \(G_{11}(-8H,S)\). Within blocks of indices take \(g=\gcd(D,\prod |F_n|)\); for each single index put \(u=\gcd(g,|F_n|)\). Then \(\gcd(u,|F_n|/u)\) is exactly the product of the compatible primes through the cutoff whose square divides this value. At each positive result exact integer division determines the exponent. The integer inequality \(10^{9\cdot1213}<683^{3900}\) eliminates every remaining index from the score comparison.

Direct factorization also proves squarefreeness without any prime cutoff at \(n=0,\pm1,\pm2,\pm4,5\). In the table, the remaining cofactor in every row is a prime distinct from the displayed factors. The verifier computes the full integer and checks its cofactor by FLINT's proved primality test. At \(n=3\) the factors \(2179,4349753,21116393\) leave a composite 100-digit cofactor; its squarefreeness above the search cutoff is unresolved. [Exact small-index factors and scalar checks](abc_pell11_square_verify.py)

| \(n\) | Prime factors removed before the final prime |
|---:|---|
| 0 | 82633 |
| 1 | 2179, 18371 |
| \(-1\) | 9241, 519853819 |
| 2 | 268643, 132679547527986097 |
| \(-2\) | 79856463754211, 627829452273211 |
| 4 | 4027, 772040897 |
| \(-4\) | 2179, 1172777 |
| 5 | 26203 |

## Exhausting complete periods

For a finite root \(k=a/b\) of the degree-100 parameter form, use the norm-one element
\[
 w=\frac{1+k\sqrt2}{1-k\sqrt2}
  =\frac{1+2k^2+2k\sqrt2}{1-2k^2}.
\]
A root has nonzero quadratic norm, and the parameter at infinity gives \(w=-1\). This change identifies unit projective classes with the norm-one group in the split or nonsplit quadratic algebra. The Pell generator maps to \(g=-3-2\sqrt2\). Its order \(m\) divides \(p-(2/p)\). Successive division of that bound by prime factors, with modular powering to test \(g^{m/\ell}=1\), gives the exact \(m\).

Factoring the parameter polynomial over \(\mathbb F_p\) gives all 100 projective roots. A baby-step giant-step search finds each root lying in \(\langle g\rangle\) and its index \(r\bmod m\). For every prime with a root on this orbit, \(\epsilon^m\) has nonzero \(\sqrt2\)-coefficient modulo \(p^2\), checked by binary powering. Write \(A(n)=G_{11}(-8H/S)\). Since the parameter roots are simple, the projective translation by \(\epsilon^m\) gives
\[
 \frac{A(r+jm)}p\equiv\frac{A(r)}p
                +j\,\frac{A(r+m)-A(r)}p\pmod p .
\]
The coefficient of \(j\) is a unit and the code verifies this by inversion. Thus exactly one class \(j\bmod p\) gives square divisibility at each root. The least positive representative \(n\) is tested modulo \(p^3\); if its valuation exceeds two, the next representative \(n+mp\) has valuation exactly two, by the same nonzero tangent one level higher. Minimizing over the roots gives the results in the archive. A second verifier checks the abscissa of \([11]P\) directly at all 6,378 reported least indices, using projective doubling and differential addition modulo \(p^5\). Its numerator is a \(p\)-unit and denominator has valuation four in every case.

There are 356,138 visited projective root classes. The Laurent variable \(\epsilon^{4n}=w^2\) identifies \(w\) and \(-w\), which give the same abscissa because it depends only on the ratio of coefficients of \(\epsilon^{2n}\). On the cyclic orbit every visited Laurent target therefore has exactly \(\gcd(m,2)\) projective preimages. The total number of distinct visited Laurent targets, summed over primes, is **180,203**. Of the 6,607 primes, 2,542 visit all 50 targets, 229 visit zero, and 249 visit exactly one. The maximum count below 50 is 38, occurring once. The verifier prints the complete histogram. [Archive and histogram check](abc_pell11_square_verify.py)

## The first simultaneous positive index

Among prime bases at most \(10^7\), the first positive index with two exact square divisors is
\[
        n=4\,196\,890,\qquad 683^2\parallel F_n,\qquad 1409^2\parallel F_n .
\]
The respective residues of \(A(n)/p^2\bmod p\) are 475 and 1207. Exactly seven positive indices through \(200\,000\,000\) have two such primes, and none has three. The remaining six indices are \(54\,543\,975,\ 104\,185\,863,\ 114\,166\,522,\ 120\,415\,227,\ 182\,665\,765,\ 192\,107\,463\). Only 200 primes have first exact square within this interval. Enumerating their lifted congruence classes gives 59,631 distinct candidate indices; every collision is checked modulo the cubes of the corresponding primes. [Collision enumeration](abc_pell11_simultaneous.py)

## Reproduction

The Python scripts use SymPy and python-flint. From this directory the following commands reproduce the wide prime search, the complete periods and the independent checks.

~~~sh
python abc_pell11_early_squares.py --prime-bound 1000000000 --index-bound 4096 --block 16
python abc_pell11_early_squares.py --prime-bound 1000000000 --index-bound 3900 --block 32 --negative
python abc_pell11_square_periods.py 10000000 > /tmp/pell11_periods.csv
cmp /tmp/pell11_periods.csv abc_pell11_square_periods.csv
python abc_pell11_square_verify.py
python abc_pell11_simultaneous.py 200000000
~~~

The bound on \(\log p/|n|\) is finite in \(p\). The search does not decide whether a fixed positive score occurs infinitely often at unbounded primes.
