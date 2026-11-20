# Odd prime exponents beyond the quartic cutoff

On \(E:y^2=x^3-36x\), write \(B_n^2\) for the reduced denominator of \(x(nG)\), where \(G=(-3,9)\). For each of the 86 primes \(3<r\le1000\) with \(r\equiv3\pmod4\), at least one prime \(p>r^4\) divides \(B_r\) to an odd exponent. These primes are distinct across ranks, as each has \(\operatorname{ord}_p(G)=r\). At 45 of the 86 ranks the prime can be chosen congruent to 13 modulo 24. At \(r=3\) the denominator is \(B_3=37\).

## Finite certificates

The earlier [quartic search](abc_gaussian_quartic_prime_scan.md) gives the exact product \(S_r\) of all prime powers in \(B_r\) whose base is at most \(r^4\). Set \(C_r=B_r/S_r\). For each nonunit \(C_r\) the rank table specifies a prime \(q\le43\) with \((C_r/q)=-1\). Every prime divisor of \(C_r\) is 1 or 13 modulo 24, so \(C_r\equiv5\pmod8\) forces an odd exponent in the latter class. [Rank table](abc_gaussian_quartic_cofactor_powers.csv)

In fact none of the 86 nonunits is any perfect power. If \(C_r=u^\ell\) for a prime exponent \(\ell\), then \(u>r^4\), giving the upper bound
\[
  \ell\le \left\lfloor\frac{\lfloor\log_2 C_r\rfloor}{\lfloor\log_2(r^4)\rfloor}\right\rfloor.
\]
For each of the resulting 56,092 pairs \((r,\ell)\) the verifier finds a prime \(q\equiv1\pmod\ell\) for which \(C_r\) is nonzero and \(C_r^{(q-1)/\ell}\not\equiv1\pmod q\). The tuple stream has SHA-256 digest `824484721a0e138ab631dacef72094b8e7f6829aeb36e374088a9bca9510d6a7`. [Verifier](abc_gaussian_quartic_cofactor_powers.py) · [Summary](abc_gaussian_quartic_cofactor_powers.json)

A search at \(r^4<p\le16r^4\) and partial small-factor extraction for \(r\le47\) give the following additional lower bounds. Each identified prime has exponent one. At \(r=7\) and \(r=11\) the entire cofactor is accounted for. In the other rows the remaining quotient is a quadratic nonresidue at the auxiliary prime in the last column, giving another distinct odd-exponent prime. [Verifier](abc_gaussian_quartic_extra_primes.py) · [Results](abc_gaussian_quartic_extra_primes.json)

| Rank | Identified primes greater than \(r^4\) | Minimum number of distinct odd-exponent primes greater than \(r^4\) | Auxiliary prime |
|---:|---|---:|---:|
| 7 | 14,281 and 140,449 | 2 | |
| 11 | 157,142,624,025,079,880,485,453 | 1 | |
| 19 | 11,899,549 and 53,531,209 and 15,883,629,577 | 4 | 11 |
| 31 | 38,227,093 and 11,032,003,729 and 2,488,067,906,131,501 | 4 | 5 |
| 43 | 27,100,321 | 2 | 5 |
| 179 | 14,365,392,253 | 2 | 17 |
| 283 | 72,682,485,877 | 2 | 7 |
| 503 | 93,544,841,521 | 2 | 5 |
| 691 | 3,013,597,364,857 | 2 | 5 |
| 827 | 6,299,255,963,257 | 2 | 7 |

## A character identity at every positive odd index

For every positive odd integer \(n\),
\[
                B_n\equiv (-1)^{(n-1)/2}n\pmod8.
\]
In particular, \((2/B_n)=(2/n)\). For every prime \(r\equiv3\pmod8\) some prime \(p\equiv13\pmod{24}\) divides \(B_r\) to an odd exponent.

Over \(\mathbb Q(\sqrt3)\), \((x,y)\mapsto(3x,3\sqrt3 y)\) takes \(T=(-1,\sqrt3)\) on \(y^2=x^3-4x\) to \(G\). Let \(f_n=\psi_n(T)\) at odd \(n\), and \(f_n=\psi_n(T)/(2\sqrt3)\) at even \(n\). The normalized division-polynomial recurrence gives integers with \(f_1=1,f_3=-37\). At \(n=2k+1\) the recurrence modulo both 8 and 3 becomes
\[
 f_{2k+1}\equiv
 \begin{cases}
   f_{k+2}f_k^3 & k\text{ odd},\\
   -f_{k-1}f_{k+1}^3 & k\text{ even},
 \end{cases}
\]
since the suppressed term has coefficient \((2\sqrt3)^4=144\). Induction at odd indices gives \(f_n\equiv n\pmod8\). Indeed, for odd \(k\), \(k^2\equiv1\pmod8\), so \((k+2)k^3\equiv2k+1\). For even \(k\), \(-(k-1)(k+1)^3\equiv1-k^2\equiv2k+1\pmod8\) since \(8\mid k(k+2)\). Induction likewise gives \(f_n\equiv(-1)^{(n-1)/2}\pmod3\) because indices two apart have opposite signs.

Thus \(f_n\) is coprime to 6 at odd \(n\). At any prime ideal over \(p>3\) the curve has good reduction. If \(p\mid f_n\) and \(p\mid f_{n\pm1}\), then both \(nT\) and \((n\pm1)T\) reduce to the identity, which would give \(T=O\) in the residue field. The identity
\[
 x(nG)=-3-36f_{n-1}f_{n+1}/f_n^2
\]
therefore shows \(B_n=|f_n|\). Every prime \(p\mid B_n\) has odd reduction order, so \(G\) is a double modulo \(p\). The full rational two-torsion criterion implies that \(-3,-9,3\) are squares, hence \(p\equiv1\pmod{12}\). In particular \(B_n\equiv1\pmod3\), fixing the sign of \(f_n\) from its residue modulo 3 and proving the claim.

## Infinitely many ranks with no prime base in a prescribed quadratic range

For every fixed \(H>0\), a positive-density arithmetic progression of primes \(r\equiv3\pmod8\) has the following properties. Every prime factor of \(B_r\) exceeds \(Hr^2\), and at least one of them is 13 modulo 24 with odd exponent.

Indeed, the Gaussian annihilator and rational two-torsion restrict every possible base to
\[
 F_{a,b}(r)=(1+ar)^2+(br)^2,\qquad 4\mid a,\quad 2\mid b,\quad b\ne0.
\]
If \(F_{a,b}(r)\le Hr^2\), then \(\left|1-a-ib\right|\le \sqrt H+1+1/r\le\sqrt H+2\). The integer \(m=F_{a,b}(-1)\) is odd and \(5\le m\le(\sqrt H+2)^2\). Let \(M\) be the odd part of \(\operatorname{lcm}(1,\ldots,\lceil(\sqrt H+2)^2\rceil)\). Choose \(r\equiv-1\pmod M\) and \(r\equiv3\pmod8\); this is a reduced residue class modulo \(8M\). Then \(m\mid F_{a,b}(r)\), whereas
\[
 F_{a,b}(r)-m=(r+1)\big[(a^2+b^2)(r-1)+2a\big]>0
\]
for \(r\ge3\). This rules out all the candidate primes. The prime number theorem for progressions gives positive relative density among primes, and the character identity supplies the odd exponent. [Gaussian shape proof](abc_gaussian_scalar_prime_scan.md)

Quantitatively, there is an unbounded sequence of such primes with \(\min_{p\mid B_r}p\gg r^2\log r\). For \(H\to\infty\), choose the least prime in the class above. Since \(r\ge M-1\), these ranks are unbounded. Chebyshev's bound gives \(\log M=O(H)\) and Linnik's theorem gives \(r\ll(8M)^L\) with absolute constants, so \(\log r=O(H)\). The finite certificates reach the larger \(r^4\) scale through 1,000.
