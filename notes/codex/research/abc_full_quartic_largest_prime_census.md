# The five smallest possible largest primes of odd exponent

Let \(G=(-3,9)\) on \(E:y^2=x^3-36x\), and let \(B_n\) be the positive square root of the denominator of \(x([n]G)\) in lowest terms. Write \(D_n\) for the squarefree integer with \(B_n/D_n\) a square. For \(D_n>1\), put \(M_n=P^+(D_n)\), and use \(M_n=1\) if \(D_n=1\).

The following are **all** positive odd indices with \(M_n\le31{,}904{,}497\).

| Index \(n\) | Factorization of \(B_n=D_n\) | \(M_n\) |
|---:|---|---:|
| 1 | 1 | 1 |
| 3 | 37 | 37 |
| 5 | \(13\cdot3121\) | 3,121 |
| 7 | \(14281\cdot140449\) | 140,449 |
| 9 | \(37\cdot2148661\cdot31904497\) | 31,904,497 |

In particular, at **every odd \(n\ge11\)** the denominator has a prime larger than 31,904,497 to odd exponent. No upper bound on the index enters the verification.

## Why a finite sieve is exhaustive

Write \(Y=31{,}904{,}497\). If an odd \(n>1\) is eligible, its largest prime divisor \(q_0\) satisfies \(q_0<Y/2\). The [square classification](abc_full_quartic_square_classification.md) gives a prime \(p\mid D_{q_0}\). The reduction of \(G\) at \(p\) has order \(q_0\) since \(G\) is integral; these odd denominators are prime to 6. The full two-torsion and Hasse's bound give \(p\ge(2\sqrt{q_0}-1)^2>2q_0\). Thus \(p\nmid n\), and its odd exponent survives in \(B_n\) by the formal group. Eligibility implies \(p\le Y\).

Consequently **for every divisor** \(m\mid n\), every prime of odd exponent in \(B_m\) is at most \(Y\). Indeed any prime exceeding \(Y\) is prime to \(n/m\) and retains its exponent in \(B_n\).

For an odd prime \(q\mid n\), \(D_q>1\) again, and every prime in \(D_q\) has exact reduction order \(q\). Also every prime of any odd \(B_j\) is \(1\bmod12\) by the [parametrization](abc_full_quartic_signature.md). Enumerate all 491,780 primes \(p\le Y\) with \(p\equiv1\pmod{12}\). For each, the rank scanner verifies by point multiplication an integer that annihilates \(G\bmod p\), factors it with the smallest-prime-factor sieve, and tests each odd prime factor \(q\) directly by computing \([q]G\). The finite point \(G\) has order \(q\) exactly when this multiple is the identity. The annihilator candidates \(p+1\pm2a\) use \(p=a^2+b^2\) with \(a\) odd. The scanner checks the successful candidate at every prime, so the certification does not need a CM trace formula.

There are 41,146 such prime-order reductions, at 38,854 distinct possible index primes. They give a second result. **For every odd prime index \(q\), every prime \(p\le Y\) dividing \(B_q\) has exponent exactly one.** For each enumerated pair compute \(H=[(q-1)/2]G\) and \(K=H+G\) modulo \(p^2\). Their reductions modulo \(p\) are opposite and have nonzero ordinates. Therefore their sum \([q]G\) reduces to the identity modulo \(p^2\) exactly when their abscissas agree modulo \(p^2\). Indeed, at equal abscissas the curve equations give equal squared ordinates, and the difference of the two ordinates is a unit at \(p\). Congruence to the identity at this depth is equivalent to \(p^2\mid B_q\) by the parameter \(-x/y\) of the formal group. The verifier finds unequal abscissas modulo \(p^2\) in every case. All intermediate nonidentity multiples used for computing \(H\) and \(K\) have good affine addition or doubling in these local rings.

Write \(S_q\) for the enumerated primes at order \(q\); the largest set has six elements. For an eligible \(q\) we now know the entire prospective cofactor, \(D_q=\prod_{p\in S_q}p\), since every such prime has exponent one and larger prime factors must have even exponent. On \(E_0:y^2=x^3+36x^2+36x\) with \(P=(-2,8)\), the [slope formula](abc_full_quartic_square_denominators.md) evaluates the quadratic character of \(B_q\) at each auxiliary prime \(\ell\ge5\) by \((8(6-x([q]P))/\ell)\) at a finite reduction, with sign \(+1\) at the identity. For every candidate except \(q=3,5,7\), this sign differs from the symbol of the prospective cofactor at some \(\ell\le71\) where both tests are nonzero. That excludes the candidate.

Any integer supported on \(3,5,7\) outside the five in the table has a divisor in \(\{15,21,25,27,35,49\}\). For each of these six divisors the verifier computes \(B_m\) from exact rational point arithmetic, strips all powers of primes at most \(Y\) congruent to 1 modulo 12, and takes the integer square root of the residue. Each residue is nonsquare. Its bit length in the displayed order is 31, 190, 335, 404, 689, and 1508. This forces a prime of odd valuation above \(Y\), which excludes all such multiples among the eligible \(n\). Exact point arithmetic and a primality sieve also verify each surviving entry of the table.

From this directory run the following commands. The Python verifier runs the scanner itself; the two files and its imported smaller-census module use only standard C++ and Python libraries. [Prime-order scan](abc_full_quartic_prime_rank_scan.cpp) · [Character and cofactor verification](abc_full_quartic_largest_prime_census.py) · [Shared rational and modular arithmetic](abc_congruent_six_smooth_odd_support.py)

```sh
g++ -O3 -std=c++17 abc_full_quartic_prime_rank_scan.cpp -o /tmp/abc-quartic-rank-scan
python3 abc_full_quartic_largest_prime_census.py /tmp/abc-quartic-rank-scan
```
