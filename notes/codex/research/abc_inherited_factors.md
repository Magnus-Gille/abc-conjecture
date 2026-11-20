# Can one exceptional abc triple generate an infinite chain?

For a primitive triple of positive integers \(a+b=c\), write \(n=abc\), \(R(n)=\operatorname{rad}(n)\), and \(f(n)=n/R(n)\). Thus \(f(n)\) counts the powers left after retaining one copy of each prime. Fix \(0<\eta<1\), and call a triple exceptional here when \(R(n)\le c^{1-\eta}\). Infinitely many such triples for one fixed \(\eta\) would disprove rational abc, using a slightly smaller exponent if necessary in the usual formulation with an arbitrary constant.

Given a previous triple with product \(N\), define
\[
 F(N,n)=\frac{f(n)}{f(\gcd(N,n))}.
\]
This is an integer. A prime may switch freely among the three terms. For example, a prime that occurs simply in the seed and then to exponent three in the next triple contributes its square to \(F\). Primes appearing simply in the new triple contribute one, regardless of their size.

## An infinite chain needs unbounded new or increased repeated factors

Fix a starting triple and a constant \(K\ge1\). There are only finitely many triples reachable by an arbitrarily long chain of exceptional triples with \(F(N,n)\le K\) at every step.

To prove this, put in \(S\) the primes of the starting triple and all primes at most \(K\). No prime outside \(S\) can acquire a second copy for the first time along a chain: that step would multiply \(F\) by at least \(p>K\). Thus all repeated primes in every reached triple lie in \(S\).

More generally, fix any finite \(S\) and \(0\le\delta<\eta\). Only finitely many exceptional triples satisfy
\[
 F_{\mathrm{out}}=\prod_{p\notin S}p^{\max(v_p(n)-1,0)}\le c^\delta .
 \tag{1}
\]
Indeed let \(D_S=\prod_{p\in S}p^{v_p(n)}\). Since \(f(n)\ge ab\,c^\eta\), (1) implies \(D_S\ge f(D_S)\ge ab\,c^{\eta-\delta}\). Apply the \(p\)-adic Subspace Theorem in dimension two to the primitive integer vector \((a,c)\). At infinity choose the independent forms \(a,c-a\). At each \(p\in S\) choose whichever of \(a,c,c-a\) is divisible by \(p\), if any, and another of the three forms that is a unit. When all are units choose any two. The complete product of their absolute values is \(ab/D_S\le c^{-(\eta-\delta)}\). There are finitely many choices of the forms. The theorem, with exponent \((\eta-\delta)/2\), gives finitely many rational lines containing the solutions; each has at most one such positive primitive vector. Taking \(\delta=0\) proves the chain assertion. This proof does not bound the heights effectively.

## Exact test allowing \(F\) to grow with the new height

Take a fixed \(N\). Allow all exceptional children satisfying \(F(N,n)\le c^\eta\). Their complete list can be obtained by ordinary continued fractions. The algorithm requires no preassigned height cutoff.

Put \(d_a=\gcd(a,N)\), \(d_b=\gcd(b,N)\), \(d_c=\gcd(c,N)\), \(D=d_a d_b d_c=\gcd(n,N)\), and \(U=\operatorname{rad}(D)\). The three \(d_i\) are pairwise coprime. The two threshold conditions imply
\[
 ab\le f(D)=D/U,\qquad c\le ab+1\le f(N)+1.                              \tag{2}
\]
The second inequality follows from \((a-1)(b-1)\ge0\). For each \(p^e\parallel N\) there are \(1+3e\) choices for its assignment: absent, or in one of the three \(d_i\) to an exponent from one through \(e\).

Write \(a=d_a x\), \(b=d_b y\). Then \(\gcd(x,y)=1\) and (2) gives
\[
 xy\le d_c/U,\qquad y\equiv r x\pmod {d_c},\qquad
 r=-d_a d_b^{-1}\pmod{d_c},\quad 0\le r<d_c .
\]
If \(U=1\) then \(ab\le1\), which gives no exceptional triple. If \(U=2\), the power \(D\) divides one term, so \(c\ge D\) and \(D-1\le c-1\le ab\le D/2\). This also forces \(a=b=1\). For \(U\ge3\), \(d_c\ge U\) and \(y=rx-kd_c\) gives a reduced fraction \(k/x\), since every common divisor of \(k,x\) divides \(y\). It satisfies
\[
 \left|\frac{r}{d_c}-\frac{k}{x}\right|
      =\frac{y}{d_c x}\le\frac{1}{U x^2}<\frac{1}{2x^2}.
\]
Legendre's continued-fraction criterion makes \(k/x\) a convergent of \(r/d_c\). Enumerate its convergents, recover \(y\), and check the gcds and the two original inequalities. The number of candidates before those final checks is
\[
 O\!\left(\log(2N)\prod_{p^e\parallel N}(1+3e)\right)=N^{o(1)} .
\]
The final estimate follows from \(1+3e\le(e+1)^3\) and the elementary divisor bound. This bounds the number of candidates, without assigning a complexity bound to integer factorization.

## Exhaustive results at \(\eta=1/10\)

The test is \(R(n)^{10}\le c^9\) and \(F(N,n)^{10}\le c\). We sort the two addends \(a\le b\) and include a qualifying seed among its own children. For the high-quality triple \(2+6436341=6436343\), whose radical is 15042, its only child is itself. The seed \(625+2048=2673\) has exactly 14 children, at heights
\[
9,\ 64,\ 81,\ 128,\ 256,\ 513,\ 1025,\ 1216,\ 2048,\ 2673,\ 5632,\ 6400,\ 14337,\ 186625 .
\]
Only \(1+186624=186625\) has \(F>1\), with \(F=3\) and radical 44790. A second calculation scanned all positive \(a\le b\) with \(ab\le f(N)=10368000\) and returned the identical list.

As a separate test, all **25** primitive exceptional triples of height at most 3000 were used as starting points at once. Iterating over every eligible child until the list stopped growing produced **32** distinct triples and **135** directed edges including self-loops. The seven triples beyond the starting set are

| \(a\) | \(b\) | \(c\) |
|---:|---:|---:|
| 1 | 3968 | 3969 |
| 7 | 5625 | 5632 |
| 1 | 6399 | 6400 |
| 1 | 14336 | 14337 |
| 1 | 186624 | 186625 |
| 1 | 228095 | 228096 |
| 1 | 263168 | 263169 |

The initial sieve is bounded by 3000; subsequent steps use the all-heights continued-fraction test. The finite closure proves that this particular rule and these starting points cannot yield an infinite sequence. Other starting points, or transitions with a larger \(F\), remain possible. The fixed-\(K\) theorem does not imply finiteness of this variable-threshold rule for arbitrary starting points.

Run the calculation with \(\texttt{python abc_inherited_factors.py 625 2048}\) or \(\texttt{python abc_inherited_factors.py --through 3000}\). [Enumeration and initial sieve](abc_inherited_factors.py)

## An upper bound for sharing partial sets of primes on a fixed elliptic curve

Use the rank-four group of the [elliptic denominator calculation](abc_elliptic_prime_occurrences.md). Write \(H(P)=8\widehat h(P)\), \(B(P)=|uvw|\). Then \(\log B(P)\le K_0H(P)\) holds for every nonzero point in the group with a single constant \(K_0\), since its positive heights are bounded below. A good prime satisfies \(p^j\mid B(P)\) exactly when the image of \(P\) under the fixed isogeny composed with doubling is the identity modulo \(p^j\).

Fix \(\eta>0,\ K>0\) and a point \(P\ne O\). There are at most \(O_{K,\eta}(1)\) points \(Q\ne O\) with \(H(Q)\le K H(P)\) that retain weight at least \(\eta H(P)\) from the repeated good primes of \(B(P)\). Here each level \((p,j)\), \(2\le j\le v_p(B(P))\), has weight \(\log p\), and \(Q\) retains it if \(p^j\mid B(Q)\). Each \(Q\) may retain a different subset.

Indeed the weight \(W\) of all seed levels is at most \(K_0H(P)\). For two distinct \(Q,Q'\), every level common to them also divides \(B(Q-Q')\), by the subgroup property. Their common weight is therefore at most \(K_0 H(Q-Q')\). The norm \(\sqrt H\) comes from a Euclidean inner product in four dimensions. Cover the ball \(H(Q)\le KH(P)\) by \(O_{K,\eta}(1)\) smaller balls such that \(K_0H(Q-Q')\le\eta^2 H(P)/(2K_0)\) for points in the same smaller ball. In one such ball consider \(t\) candidate points, and let \(u\) on seed levels count the number retaining each level. Cauchy–Schwarz with these weights yields
\[
 (t\eta H(P))^2\le W\sum u^2\,\mathrm{weight}
 \le K_0H(P)\left(tK_0H(P)+t(t-1)\frac{\eta^2 H(P)}{2K_0}\right).
\]
Thus \(t\le2K_0^2/\eta^2\). This excludes a growing cluster of comparable-height examples made by different rearrangements of the same seed's divisibility on this curve.

There is also a pointwise bound along multiples \(nQ\) of a nonzero point. If a good prime \(p\le X\) occurs for the first time at index \(d\), then \(d\le(\sqrt X+1)^2\) by Hasse's bound. Write \(Y=(\sqrt X+1)^2\). The formal group contributes at most \(\log n\) in valuation increases beyond those first appearances, and the total first-appearance weight at \(d\) is at most \(K_0 d^2H(Q)\). Summing over \(d\mid n,\ d\le Y\) and putting \(j=n/d\) gives
\[
 \sum_{\substack{p\le X\\p\ {\rm good}}}
       (v_p(B(nQ))-1)_+\log p
 \ll \log n + H(nQ)\min(1,Y/n).
\]
Here \(\sum_{j\ge n/Y}j^{-2}\ll\min(1,Y/n)\). As \(n\to\infty\), the range \(p\le X=o(n)\) makes a vanishing contribution relative to \(H(nQ)\) for every point on the sequence. Exponents of larger primes at their first occurrence remain uncontrolled.
