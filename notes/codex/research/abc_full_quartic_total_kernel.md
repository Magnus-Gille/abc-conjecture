# The least squarefree parts of the four-coordinate product

For the primitive quartic orbit \(a^4+3b^2=4w^4\), write \(|b|=cd\) with \(c^2=2w^2-a^2\) and \(3d^2=2w^2+a^2\). Let \(D_n=\operatorname{sf}(awcd)\) at positive odd index \(n\). The **complete census through \(10^{19}\)** has three entries, each attained only at the displayed index.

| Index | \(\operatorname{sf}(w)\) | \(\operatorname{sf}(ac)\) | \(\operatorname{sf}(d)\) | \(D_n\) |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 1 |
| 3 | 37 | \(23\cdot47\) | \(3\cdot11\) | 1,319,901 |
| 5 | \(13\cdot3121\) | \(73\cdot97\cdot239\cdot719\) | \(17\cdot19\cdot139\) | 2,216,541,307,731,009,701 |

The largest-prime-factor census has a different ordering. Taking \(P^+(1)=1\), the only positive odd indices with \(P^+(D_n)\le80{,}217{,}359\) are **1, 3, 5, 9**, with respective maxima **1, 47, 3,121, 80,217,359**. At index 7, the factor \(c=2{,}802{,}064{,}609\) is already prime. [Small-index factor certificates](abc_congruent_six_initial_quality_factors.json) · [Independent arithmetic checks](abc_full_quartic_total_kernel.py)

## The complementary squarefree part

All four coordinates are pairwise coprime. Put \(F_n=\operatorname{sf}(ac)\). Its prime factors are \(\pm1\bmod24\). At a good prime dividing \(a\), the two displayed equations imply 2 and 3 are squares. At a prime dividing \(c\), one has \(a^2=2w^2\) and \(3d^2=4w^2\), giving the same restrictions. [Four-coordinate parametrization](abc_full_quartic_signature.md)

On \(E:y^2=x^3-36x\), write \(Q=nG\) for \(G=(-3,9)\). From \(x(Q)=-3a^2/w^2\) one gets
\[
                 (ac/w^2)^2=-x(Q)(x(Q)+6)/9.
\]
At any auxiliary prime \(\ell\equiv1\pmod4\) with affine reduction and \(x(Q)\ne0,-6\), raising the right side to \((\ell-1)/4\) gives \((F_n/\ell)\). At the identity, \(\ell\mid w\) gives \((c/a)^2=-1\pmod\ell\), so \((F_n/\ell)=(-1)^{(\ell-1)/4}\). At \(x=0,-6\) every possible valuation is allowed.

There are 85 such auxiliary primes through 200,000 with \(\operatorname{ord}_\ell(G)\mid2520\). Evaluating all odd index residues and enumerating the 85,279,401 squarefree products of primes \(\pm1\bmod24\) up to 5,000,000,000 gives precisely

| \(F_n\) | Necessary \(n\bmod2520\) |
|---:|:---|
| 1 | \(\pm1\) |
| \(1081=23\cdot47\) | \(\pm3\) |
| \(1216806121=73\cdot97\cdot239\cdot719\) | \(\pm5\) |

The verifier directly enumerates the periods and characters. It generates products supported on primes up to the square root of the bound by recursion. For the remainder, each product has one larger prime and a smaller coprime cofactor, so a segmented prime sieve completes the count. [C++17 verifier](abc_full_quartic_complementary_census.cpp)

The case \(F_n=1\) forces \(a=A^2,c=C^2\) and \(A^4+C^4=2w^2\). Set \(X=2A^2/C^2\), \(Y=4Aw/C^3\). Then \(Y^2=X^3+4X\). This curve is 2-isogenous to \(y^2=x^3-16x\), isomorphic to \(y^2=x^3-x\), of rank zero by Fermat's theorem that a rational right triangle cannot have square area. Reduction at 3 and 5 gives respective group orders 4 and 8, so \(O,(0,0),(2,\pm4)\) give all the rational points. Hence \(A=C\), and coprimality forces the seed.

For \(n>1\), take its largest prime factor \(q\). The abscissa denominator roots of the odd multiples of \(S_a=(12,36)\) and \(S_c=(18,-72)\) are \(a\) and \(c\), respectively. These are the translates of \(G\) by \((0,0)\) and \((-6,0)\). Every prime of \(F_q\) therefore has exact reduction order \(q\) for the corresponding integral point. The independent rational two-torsion gives \(p\ge(2\sqrt q-1)^2>q\). Hence \(p\nmid n\), and the formal group preserves its odd valuation on passage to index \(n\). In particular \(1<F_q\mid F_n\).

The orders of \((S_a,S_c)\) are \((3,6),(6,3)\) at 23 and 47. At 73, 97, 239 and 719 they are respectively \((5,10),(10,5),(10,5),(5,10)\). Thus \(F_n=1081\) forces \(q=3\), and the class \(\pm3\bmod2520\) forces \(n=3\). The third value forces \(q=5\), with \(3\nmid n\), so \(n\) is a power of 5. Exact reduction gives \(v_{2017}(a_{25})=1\), which persists at all higher 5-powers and excludes them. This completes the all-index complementary census.

For odd \(n\ge7\), therefore, \(F_n>5\cdot10^9\). The independent denominator census gives \(\operatorname{sf}(w_n)\ge2{,}005{,}752{,}169\) on that range. Multiplying these coprime factors gives \(D_n>10^{19}\) as claimed. [All-index denominator census](abc_full_quartic_square_denominators.md)

## Largest primes of odd valuation

Run the good-prime order scanner up to \(Y=80{,}217{,}359\) at \(p\equiv1\bmod12\). For each of the 86,731 possible prime indices \(q\), test every nonempty subset of the enumerated primes of exact order \(q\) as a possible support of \(\operatorname{sf}(w_q)\). There are 91,558 order pairs and 97,977 subsets in total. The denominator characters at auxiliary primes through 71 leave exactly \(q=3,5,7\), with the full original factorizations at these indices. Enumerating subsets allows arbitrary first valuations.

To justify exhaustiveness without a bound on \(n\), suppose \(P^+(\operatorname{sf}(w_n))\le Y\). For the largest prime factor \(q_0\) of \(n>1\), the exact square classification gives a prime of odd valuation at \(q_0\), which has size greater than \(q_0\) and retains its valuation at \(n\). Hence \(q_0<Y\). All primes exceeding \(Y\) are now prime to \(n\), so every divisor index of \(n\) also satisfies the smoothness condition. In particular, each prime divisor comes from the surviving list \(3,5,7\). Each integer supported on these primes outside \(1,3,5,7,9\) is divisible by at least one of \(15,21,25,27,35,49\). At those six indices one strips the primes at most \(Y\) from the denominator and tests the remaining integer for squareness. All six residuals are nonsquares. Thus no other index can have a \(Y\)-smooth total squarefree kernel. Checking the five surviving coordinates gives the four stated total-kernel entries. [Order scanner](abc_full_quartic_prime_rank_scan.cpp) · [Subset and composite-index verifier](abc_full_quartic_total_kernel.py) · [Earlier smoothness argument](abc_full_quartic_largest_prime_census.md)

## Local restrictions from two-torsion, 2 and 3

At a good prime \(p\mid D_n\), the reduction of \(nG\) distinguishes the four possibilities.

| Coordinate | Reduction | Possible unit classes of \(p\bmod24\) |
|:---|:---|:---|
| \(w\) | \(O\) | 1, 13 |
| \(a\) | \((0,0)\) | 1, 23 |
| \(c\) | \((-6,0)\) | 1, 23 |
| \(d\) | \((6,0)\) | 1, 11, 17, 19 |

For the last row \(a^2=-2w^2\pmod p\) gives \((-2/p)=1\). The only bad prime which can appear is 3, in \(d\). Moreover \(d\equiv1\pmod8\): since \(a\equiv\pm1\pmod8\), \(3d^2=2w^2+a^2\equiv3\pmod{16}\), giving \(d\equiv\pm1\pmod8\). All its prime divisors are 1 or 3 modulo 8, so only \(d\equiv1\pmod8\) occurs. The number of primes of \(D_n\) in the classes \(3\bmod8\), including 3, is even.

The signed unit congruence also records the index. Let \(e=v_3(n)\), \(n_0=n/3^e\), and \(\sigma=\operatorname{sgn}(y(nG))\). Then
\[
   v_3(D_n)=e\bmod2,\qquad
   \sigma\, D_n/3^{e\bmod2}\equiv n_0\pmod{24}.
\]
In particular \((2/D_n)=(2/n)\). Indeed \(\sigma awcd=y(nG)w^4/9\equiv y(nG)\pmod8\). The point \(G\) has nonsingular reduction at 2, \(8G\) lies in the kernel of reduction modulo 8, and direct multiplication gives \(y(jG)\equiv j\pmod8\) at \(j=1,3,5,7\). This proves the signed claim modulo 8.

At 3 use \(S=G+(6,0)=(-2,-8)\). The translation formula gives the exact identity \(\sigma awcd=-y(nS)d^4/8\). The nonsingular reduction of \(S\) has order 3 and \(y(nS)\equiv n\pmod3\) for \(3\nmid n\). If \(e\ge1\), the formal parameter \(t=-x/y\) satisfies \(t(3S)=1551/3404\) and \(t(3S)/3\equiv-1\pmod3\). The isometric formal logarithm gives \(v_3(d)=e\) and \(t(nS)/3^e\equiv-n_0\pmod3\). Since \(y=-t^{-3}\) to leading order, the unit part of \(\sigma awcd\) is \(n_0\pmod3\). Removing an odd square preserves its 2-adic residue modulo 8 and its 3-adic unit residue modulo 3. Finally \(3^{e-(e\bmod2)}\equiv1\pmod8\), proving the formula.

The same translation formula gives a rational squareclass identity. The absolute ordinate of \(nG\) represents \(D_n\). Translating by \((0,0)\) multiplies the ordinate by \(36/x^2\). Translating by either \((\pm6,0)\) multiplies it by \(-72/(x\mp6)^2\), so the corresponding positive squareclass is \(2D_n\).

```sh
g++ -std=c++17 -O3 abc_full_quartic_complementary_census.cpp -o /tmp/quartic-complement
/tmp/quartic-complement
g++ -std=c++17 -O3 abc_full_quartic_prime_rank_scan.cpp -o /tmp/quartic-prime-ranks
python3 abc_full_quartic_total_kernel.py /tmp/quartic-prime-ranks
```
