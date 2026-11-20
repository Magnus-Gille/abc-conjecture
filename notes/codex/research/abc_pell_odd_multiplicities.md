# Odd multiplicities at prescribed Pell ranks

Write \(P_0=0,\ P_1=1,\ P_{j+2}=2P_{j+1}+P_j\), and let \(r_q\) be the first index with \(q\mid P_{r_q}\). For every sufficiently large **odd prime power** \(d=p^a\), the quotient \(P_{p^a}/P_{p^{a-1}}\) has a prime divisor \(q\) of odd valuation with exact rank \(r_q=d\). In particular \(q\ge2d-1\). The threshold is absolute as both \(p\) and \(a\) vary. For indices whose prime factors belong to a fixed finite set, one obtains an odd multiplicity at every sufficiently large order, including composite orders.

The distinction between a primitive prime and a primitive prime of odd multiplicity matters here. Only the latter survives in the squarefree part \(\operatorname{sf}(P_m)\) without an additional multiplicity condition. These results concern the [Pell radical criterion for a family of abc triples](abc_two_small_legs_and_pell_radicals.md); they do not bound the total repeated part sharply enough to settle that criterion.

## A nonsquare quotient by an integer trace estimate

In fact \(P_{pt}/P_t\) is never square for **any odd integers** \(t\ge p\ge3\). Set \(\lambda=1+\sqrt2,\ \bar\lambda=1-\sqrt2,\ A=\lambda^t,\ p=2k+1\). The conjugate of \(A\) is \(-A^{-1}\). Thus the positive square root of the quotient is
\[
 H=A^k(1+A^{-2})^{-1/2}(1+A^{-2p})^{1/2}.
\]
Write \(b_j=4^{-j}\binom{2j}{j}\), the unsigned coefficients of the series for \((1+x)^{-1/2}\). Put \(J=\lfloor k/2\rfloor\). In \(\sum_{j=0}^J(-1)^j b_j A^{k-2j}\), replace every positive power \(A^h\) by its integer trace \(A^h+(-1)^h A^{-h}\), leaving the constant term unchanged. Denote the resulting rational number by \(L\); \(4^J L\) is integral.

For \(k=2J+1\), the leading term of \(H-L\) is \(cA^{-1}\) with \(c=(-1)^{J+1}(b_{J+1}-b_J)\). For \(k=2J\ge2\) it is \(cA^{-2}\) with \(c=(-1)^{J+1}(b_{J+1}-b_{J-1})\). These coefficients are the sum of the first omitted term and the negative of the nearest conjugate term. Write \(h=1,2\) respectively. The remaining binomial terms and remaining conjugate terms each cost at most \(A^{-h-2}/(1-A^{-2})\), since all \(b_j\le1\). The factor \((1+A^{-2p})^{1/2}\) contributes at most \(A^{k-2p}/2\). Altogether
\[
 |H-L-cA^{-h}|\le3A^{-h-2}.
\]
Since \(b_{J+1}/b_J=(2J+1)/(2J+2)\) and \(b_J\ge1/(2J+1)\), one has \(1\ge|c|\ge1/((k+1)(k+2))\) in both cases. Now \(A\ge\lambda^{2k+1}>2^{2k+1}\) implies \(A^2>3(k+1)(k+2)\). It follows that \(H-L\ne0\), whereas \(4^J|H-L|\le2^k(1+3/A^2)/A<1\). Thus \(H\) cannot be an integer. Applying this with \(t=p^{a-1}\) covers every odd prime power of exponent \(a\ge2\).

When \(a=1\), failure of the nonsquare assertion for infinitely many \(p\) would give infinitely many integral points on \(Y^2=2Z^4-1\): write \(\lambda^p=A_p+P_p\sqrt2\) and take \(P_p=Z^2\). This affine curve has genus one, contradicting Siegel's theorem. This step, as well as the fixed-support argument below, is ineffective.

Finally \(P_{p^a}/P_{p^{a-1}}\) is odd and all its prime divisors have exact rank \(p^a\). A lower rank would divide \(p^{a-1}\); by odd-prime lifting its valuation in the quotient would be zero unless the prime were \(p\). The prime \(p\) itself cannot occur, since \(r_p>1\) divides \(p-(2/p)\) and is coprime to \(p\). The nonsquare quotient therefore has a prime \(q\) of odd valuation at the asserted rank. As \(q\) is odd and \(q\equiv\pm1\bmod p^a\) with \(p^a\) odd, \(q\ge2p^a-1\).

## All large orders on a fixed prime support

Fix a finite set \(S\) of rational primes. For all sufficiently large \(r\) with prime factors in \(S\), there is a prime \(q\notin S\) of exact rank \(r_q=r\) occurring to odd order in \(P_r\).

Here are the details. For each such \(r\) choose \(e\mid r\) of bounded size in terms of \(S\), with the same prime support as \(r\) and \(\varphi(e)\ge4\). This is possible for large \(r\): begin with the squarefree kernel in the sense of the product of distinct primes and, if necessary, multiply by powers of one of the primes whose exponent in \(r\) is large. The homogeneous cyclotomic identity gives
\[
 \Phi_r(\lambda,\bar\lambda)=\Phi_e(\lambda^{r/e},\bar\lambda^{r/e}).
\]
Indeed every prime dividing \(r/e\) divides \(e\), so raising to the \(r/e\)-th power has precisely the primitive \(r\)-th roots as inverse images of the primitive \(e\)-th roots.

The right side is an integer polynomial \(H_{e,s}(X)\) in \(X=\lambda^{r/e}+\bar\lambda^{r/e}\) with \(s=(-1)^{r/e}\) fixed to one of two signs. Symmetry in the two bases gives integral coefficients after substituting their product \(s\). The polynomial is monic of degree \(\varphi(e)\); its roots satisfy \(X^2=s(2+\zeta+\zeta^{-1})\) for primitive \(e\)-th roots \(\zeta\), one pair for each unordered \(\{\zeta,\zeta^{-1}\}\). All are simple since \(e>2\). Only finitely many such polynomials occur, and \(X\to\infty\). For any bounded positive squarefree part \(h\), the curve \(hY^2=H_{e,s}(X)\) has genus at least one and only finitely many integral points by Siegel's theorem. Thus \(\operatorname{sf}(|\Phi_r(\lambda,\bar\lambda)|)\to\infty\) on these orders.

In particular the cyclotomic value has an odd-valuation prime \(q\) outside \(S\cup\{2\}\) for all sufficiently large such \(r\). A prime \(q\nmid r\) outside 2 dividing this value has exact order \(r\) for \(\lambda/\bar\lambda\) modulo \(q\), by separability of \(T^r-1\) in the residue field. Its multiplicity equals its valuation in \(P_r\), since no lower order contributes. If \(m\) also has support in \(S\) and \(r\mid m\), its valuation in \(P_m\) stays odd by lifting, because \(q\nmid m/r\). Distinct \(r\)'s give distinct primes \(q\ge r-1\). In particular, as \(m\to\infty\) on this fixed support,
\[
 \log\operatorname{sf}(P_m)
 \ \ge\ \sum_{\substack{r\mid m\\r>C_S}}\log(r-1)
 \ \ge\ \tfrac12\tau(m)\log m-O_S(1).
\]
The last estimate uses \(\sum_{r\mid m}\log r=(\tau(m)/2)\log m\) and \(\sum_{r\mid m,r>1}1/r\le\prod_{p\in S}(1-1/p)^{-1}\). For \(m\) a power of a fixed prime this gives a quadratic lower bound in \(\log m\) for the logarithm of the squarefree part. The logarithm of the entire Pell number is of order \(m\).
