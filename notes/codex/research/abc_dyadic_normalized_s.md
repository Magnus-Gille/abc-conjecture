# The 3-free part of the shifted factor is never a perfect power

For \(n=2^k\ge8\), let \(s_n=u_n^2+8v_n^2\) and put \(S_n=s_n/3^{v_3(s_n)}\). Then \(S_n>1\) and the gcd of its prime exponents is 1. In particular a squareful \(s_n\) must have **at least three distinct prime factors**, with at least two different exponents among the primes other than 3. If \(s_n\) has precisely two prime factors, the one other than 3 occurs to exponent 1. At the excluded initial index \(n=4\), \(s_4=9\).

The specific two-prime pattern \(p^2r^3\) can be excluded without modular forms. Every \(s_n\) is divisible by 3: \(u_n,v_n,w_n\) remain nonzero modulo 3 under the doubling recursion, so \(s_n\equiv1+8\equiv0\bmod3\). Indeed \(v_3(s_n)=2+v_3(k-1)\). If \(s_n=27p^2\), it would be \(3\bmod8\), whereas \(s_n\equiv1\bmod8\). If \(s_n=9r^3\), use the single prime 223: on all 20 states of the signed recursion from \(n=8\), \(s_n^{74}\equiv183\bmod223\), while \(9^{74}\equiv39\bmod223\). The remaining case \(p=r=3\) fails the same congruences. [Recursion and 3-adic valuation](abc_dyadic_direct_triple.md)

## The one additional conductor prime

For \(n=2m\) and \(m\ge8\), write \(a=w_m\), \(b=8u_m^2v_m^2\), so \(s_n=a^4+2b^2\) with \(\gcd(a,b)=1\). Suppose \(s_n=3^h z^q\) with \(q>7\) prime, \(h\ge0\), and \(3\nmid z\). Let \(F=\mathbf Q(\tau)\), \(\tau^2=-2\), \(g=a^2+b\tau\). The Q-curve \(C:y^2=x^3+4ax^2+2gx\) has \(\Delta=2^9g^2\bar g\) and \(c_4=16(16a^2-6g)\). At odd primes its bad reduction is multiplicative, and \(g,\bar g\) have coprime odd parts. The descended two-dimensional system has cyclotomic determinant. Its conductor exponent at 2 is at most ten, and the mod-\(q\) system is finite flat at \(q\). These arguments depend at \(q\) only on \(q\) dividing the relevant discriminant valuations there if the reduction is multiplicative. Since \(q\ne3\), the added coefficient \(3^h\) leaves the argument at \(q\) unchanged. [Q-curve construction, conductor and weight](abc_dyadic_fourth_factor.md)

Every odd conductor prime other than 3 can be removed just as for \(s_n=z^q\). At 3, the extension \(F/\mathbf Q\) is split and the descended representation identifies with a Tate-module representation at either place. Its residual conductor exponent is at most one by multiplicative reduction. Thus in the absolutely irreducible case weight-two Serre modularity puts the residual system at a level \(N\mid3072=3\cdot1024\). The character is trivial: its mod-\(q\) reduction is trivial by the determinant, and all Dirichlet characters at such a level have 2-power order.

## Three fixed traces

At the auxiliary primes 17 and 47, put \(x=(u_m/v_m)^2\). The duplication map \(x\mapsto(x^2-32)^2/[4x(x^2+16x+32)]\) fixes the \(m=8\) residue (respectively 1 and 32). The ratio \(b/a^2=8x/(x^2+16x+32)\) is respectively 13 and 4. Over the residue field the curve is a quadratic twist by \(a\) of
\[
             y^2=x^3+4x^2+2(1+\tau b/a^2)x .
\]
At split 17 the two choices of \(\tau\) give the coefficients 7 and 14, and both curves have trace 4. Hence the squared rational trace \(t_{17}^2=16\). At inert 47 the twist becomes trivial over \(\mathbf F_{47^2}\); the trace there is 4, so \(t_{47}^2=4+2\cdot47=98\). At inert 7 one has \(7\mid v_m\) for \(m\ge8\) and \(a\) is a unit, giving normalized curve \(y^2=x^3+4x^2+2x\) over \(\mathbf F_7\). Its trace over \(\mathbf F_7\) is zero, hence the trace of \(C\) over \(\mathbf F_{49}\) is \(-14\); therefore \(t_7=0\). All three comparisons use good reduction.

In the reducible case the two characters have the form \(\theta,\epsilon_q\theta^{-1}\) by finite flatness. The finite characters are unramified at 3, since any ramification there would contribute at least two to the conductor of the semisimplification. The conductor bound at 2 gives \(\operatorname{cond}(\theta)\mid32\). Now \(7^4\equiv1\bmod32\), so \(\theta(7)^4=1\). The zero trace at 7 would force \(\theta(7)^2=-7\bmod q\), hence \(q\mid48\), impossible for \(q>7\).

## The irreducible case

On each newspace \(S_2(\Gamma_0(N))^{\mathrm{new}}\), \(N\mid3072\), form the commuting Hecke operators
\[
             H=T_{47}^2-98,\qquad J=T_{17}^2-16,\qquad K=T_7^2.
\]
For two such operators \(U,V\), define \(d(U,V)=\gcd(\det U,\det(U+V),\det(U-V))\), using absolute values. An eigenform fulfilling both trace comparisons modulo a prime over \(q\) makes \(q\) divide this integer. These determinants are integers as products of algebraic-integer eigenvalues invariant under Galois.

Across all nonempty newspaces, every \(d(H,J)\) is nonzero, and the union of their prime supports is \(\{2,3,5,7\}\). For \(q=17\), where comparing traces at 17 is unavailable, every \(d(H,K)\) is prime to 17. For \(q=47\), every \(d(J,K)\) is prime to 47. This excludes every \(q>7\). The verifier computes the determinants for all 22 potential exact levels.

## The small exponents with unrestricted coefficient at 3

For each row below, the listed residues of \(h\bmod q\) make \(s_n=3^h z^q\) impossible modulo \(\ell\) for every \(n\ge8\). The test iterates the signed triple from \((31,14,2273)\) to its first repeated state. At every state \(s_n\) is nonzero modulo \(\ell\). Its value raised to \((\ell-1)/q\) differs from \(3^{h(\ell-1)/q}\) throughout the orbit for each excluded residue. The signed and positive recursions give the same square coordinates.

| \(q\) | \(\ell\) | Distinct states | Excluded \(h\bmod q\) |
|---:|---:|---:|---|
| 2 | 23 | 11 | 0, 1 |
| 3 | 7 | 2 | 0, 1 |
| 3 | 223 | 20 | 0, 2 |
| 5 | 31 | 4 | 0, 2, 3 |
| 5 | 191 | 12 | 1, 4 |
| 7 | 71 | 7 | 1, 4, 5, 6 |
| 7 | 113 | 3 | 0, 1, 2, 3, 4, 6 |

This also covers \(s_8=3^2\cdot281\) directly. Thus the \(3\)-free cofactor is a nonpower for every index in the claimed range. Coprime depths such as 2 and 3 at different primes outside 3 remain possible. [Exact trace, Hecke and residue verifier](abc_dyadic_normalized_s.py)

## Finiteness for two mixed exponents outside 3

There is a different restriction when the \(3\)-free cofactor has exactly two prime divisors. For every fixed \(q\ge2\), only finitely many dyadic indices have \(S_n=p^a r^b\) with distinct primes \(p,r\) and \(q\mid a\) or \(q\mid b\). In particular \(s_n=3^h p^2r^3\) with arbitrary \(h\) occurs at most finitely often. The following argument gives no effective cutoff.

Let \(E':y^2=x^3+16x^2+32x\), \(R=(-8,16)\), and let \(B_j\) have valuation equal to the formal denominator depth of \([j]R\) at each rational prime. For \(m=n/2\), \(x([m]R)-x(R)=s_n/v_n^2\). At every odd prime \(\ell\), \(R\) has unit ordinate. Thus meeting its abscissa on reduction means meeting precisely one of \(R,-R\), and the abscissa difference has the same local order as the formal parameter of \([m-1]R\) or \([m+1]R\), respectively. In particular the odd parts of \(B_{m-1}\) and \(B_{m+1}\) are coprime and their product equals \(s_n\).

Fix a finite set \(L\) of rational primes containing 2 and a fixed integer \(q\ge2\). Only finitely many \(j\ge1\) have \(q\mid v_\ell(B_j)\) for every \(\ell\notin L\). To see this, choose a fixed half \(R_0\) of \(R\) over a number field \(K\) and put \(Q=[j]R_0\). Outside primes above \(L\), the function \(x\) has divisor \(2(J)-2(O)\), where \(J=(0,0)\) remains a nonzero smooth simple root of the cubic. A nonzero valuation of \(x(Q)\) has absolute value twice the depth at \(O\) or \(J\); doubling is étale and carries either to \(O\), so this is twice the local formal depth of \([2]Q=[j]R\). It is therefore divisible by \(2q\), also after extension to \(K\). Finiteness of the class group and of the group of units outside \(L\) modulo \(2q\)-th powers now gives \(x(Q)=d z^{2q}\) for some \(d\) in a finite set in \(K^\times\), and \(z\in K^\times\). For each \(d\) this yields
\[
           (y(Q)/z^q)^2=d^3z^{4q}+16d^2z^{2q}+32d .
\]
The polynomial on the right has \(4q\) distinct roots because \(X^2+16X+32\) has two distinct nonzero roots. The smooth model has genus \(2q-1\), so Faltings gives finitely many \(K\)-points. The multiples \(Q\) are distinct since \(R\) is nontorsion.

Apply the lemma with \(L=\{2,3\}\). Both halves \(B_{m-1},B_{m+1}\) have some prime outside \(L\) at every sufficiently late index, since a half supported on \(L\) satisfies the condition for \(q=2\). If exactly two primes outside \(L\) divide \(s_n\), they then lie on different halves. A depth divisible by a fixed \(q\) on either half meets the condition of the lemma, proving the assertion.
