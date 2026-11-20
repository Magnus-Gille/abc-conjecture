# Actual abc quality and denominator squarefree parts through index 35

For \(G=(-3,9)\) on \(y^2=x^3-36x\), set \(w=B_n\) and \(D_n=\operatorname{sf}(w)\). Every odd \(3\le n\le21\) has **squarefree \(B_n\)**. The inequality \(D_n\le\sqrt{B_n}\) holds with equality at the seed \(n=1\), fails at every odd \(3\le n\le21\) and also fails at \(n=25,35\). The five unresolved indices through 35 are \(23,27,29,31,33\). [Integer bounds for every row](abc_congruent_six_initial_quality.csv) · [Factor certificates](abc_congruent_six_initial_quality_factors.json) · [Verifier](abc_congruent_six_initial_quality.py)

The primitive triple is \(a^4+3b^2=C=4w^4\), with \(R=\operatorname{rad}(6a|b|w)\) and quality \(Q=\log C/\log R\). **Six of the ten nonseed rows through 21 have \(Q>1\)**. The largest quality in this completely factored range is at \(n=3\), where \((a,|b|,w)=(23,1551,37)\), \(C=7{,}496{,}644\) and \(R=2{,}639{,}802\). Four further indices, \(25,27,29,33\), have certified \(Q>1\). At \(23,31,35\) the bounds straddle one. [Elliptic parametrization](abc_full_quartic_signature.md)

| Odd index | \(D_n\le\sqrt{B_n}\) | Unfactored composite components | Quality |
|---:|:---:|---:|:---|
| 1 | yes | 0 | 0.773706 |
| 3 | no | 0 | 1.070590 |
| 5 | no | 0 | 0.995356 |
| 7 | no | 0 | 1.011215 |
| 9 | no | 0 | 1.036014 |
| 11 | no | 0 | 1.005343 |
| 13 | no | 0 | 0.999520 |
| 15 | no | 0 | 1.002754 |
| 17 | no | 0 | 0.999194 |
| 19 | no | 0 | 0.999387 |
| 21 | no | 0 | 1.001270 |
| 23 | open | 2 | [0.999728, 1.599644] |
| 25 | no | 1 | [1.000734, 1.109578] |
| 27 | open | 4 | [1.003862, 1.785696] |
| 29 | open | 4 | [1.000909, 2.829420] |
| 31 | open | 4 | [0.999957, 3.175108] |
| 33 | open | 4 | [1.001840, 2.552032] |
| 35 | no | 5 | [0.999808, 1.608788] |

For the completely factored rows the table rounds the quality to six decimals. The CSV gives outward-rounded endpoints for every row and the exact integer bounds on \(R,D_n\). For the remaining rows the displayed intervals are outward rounded.

## Verification

Exact rational group arithmetic recovers \(nG\) and the primitive integers from \(X=-3a^2/w^2\), \(|Y|=9a|b|/w^3\), \(c^2=2w^2-a^2\), \(3d^2=2w^2+a^2\), \(|b|=cd\). For each of \(w,a,c,d\) the archive records the bases, exponents and primality status, with `p` for a proven prime and `c` for a residual composite. The verifier reconstructs the coordinates and every factor product, applies FLINT's proven integer primality test, and checks coprimality of distinct factors. To obtain the factorizations, rational and Gaussian divisor-index relations were used before bounded trial division, ECM and quadratic-sieve attempts. Validation needs only the recorded factors.

Each remaining composite \(u\) is coprime to every prime through \(10^7\) by a primorial gcd. An exact perfect-power test proves that \(u\) has at least two different prime factors. Thus \(\operatorname{rad}(u)\ge(10^7+1)^2\), and \(\operatorname{sf}(u)\ge10^7+1\) because \(u\) is nonsquare. The trivial upper bound for both is \(u\). The certificate multiplies these bounds only across verified coprime components and counts 2 and 3 once. At \(n=35\), one odd-exponent prime greater than 38 in the remaining denominator component already forces \(D_n>\sqrt{B_n}\).

## The 74-digit denominator component at index 25

After proven prime powers are removed, the remaining component is
\[
 U=14490244477859042047973297613514261487530567454308598454798990909017899801.
\]
Let \(K\) be the product of the known odd-exponent primes in \(B_{25}\). Then \(\lfloor\sqrt{B_{25}}/K\rfloor=8{,}651{,}761{,}523{,}302\). We prove that **every** prime factor of \(U\) exceeds this threshold, without factoring \(U\).

Every \(p\mid U\) has exact order 25, since it divides \(B_{25}\) and is coprime to \(B_5\). Thus \(p\equiv1\pmod{12}\) and the Gaussian endomorphisms act over \(\mathbb F_p\). The annihilator divides \((25)\). If it were a proper ideal divisor, it would divide one of the two maximal proper divisors \((10+5i)\) or \((10-5i)\). This would give \(x(10G)+x(5G)=0\pmod p\). Both points are affine modulo \(p\), and the verifier checks that the cleared numerator is coprime to \(U\). Therefore the annihilator is \((25)\), and the Gaussian orbit contains \((\mathbb Z/25)^2=E[25]\). The Weil pairing gives \(p\equiv1\pmod{25}\), hence \(p\equiv1\pmod{300}\).

With \(b=170{,}000\) and \(c=300^{-1}\bmod U\), the verifier forms \(F(X)=\prod_{j=1}^b(X+c+j)\) modulo \(U\), evaluates it at \(0,b,\ldots,(b-1)b\), and multiplies the values. The resulting residue
\[
 5074352375271660377437669864059004213688244855226498489864709439897396372
\]
is coprime to \(U\). This tests all \(1+300j\) for \(1\le j\le b^2\) and excludes every prime divisor through \(8{,}670{,}000{,}000{,}001\). Since \(U\) is nonsquare, it supplies the required odd-exponent prime.

The verifier requires Python and `python-flint`. Running `python abc_congruent_six_initial_quality.py` rebuilds the CSV, including the polynomial product check at 25.
