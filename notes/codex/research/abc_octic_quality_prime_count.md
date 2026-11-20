# How a bound on the prime count would force a fixed abc exponent

Use the full two-square orbit, its quality \(q_N=\log c_N/\log\operatorname{rad}(a_Nb_Nc_N)\), elliptic denominator \(B_N\) and prime count \(W(X)\) from the [octic construction](abc_octic_mixed_quality_dichotomy.md) and [complex multiplication calculation](abc_octic_mixed_cm_prime_mass.md). All limits over indices use positive odd integers. Put
\[
 D=\limsup_{N\to\infty}N^{-2}\log\frac{B_N}{\operatorname{rad}(B_N)},\qquad
 K=\liminf_{X\to\infty}\frac{W(X)}{\sqrt{\log X}}.
\]
There is a constant \(c_*>0\), depending only on the fixed orbit, such that if \(K<\infty\) then
\[
 D\ge\frac{c_*}{(1+K)^2},\qquad
 \limsup q_N\ge 1+\frac{c_*}{(1+K)^2},
\]
after decreasing \(c_*\) if necessary. Thus even a finite liminf for this normalized elliptic prime count would yield infinitely many primitive violations of rational abc at a fixed exponent. The actual liminf is unknown here.

## A positive proportion of primitive complex multipliers

In \(\mathcal O=\mathbb Z[\sqrt{-2}]\), choose \(\beta=a+b\sqrt{-2}\) with \(1\le a,b\le J\), \(a\) odd and \(\gcd(a,b)=1\). Put \(d=a^2+2b^2\) and \(g(n)=\prod_{\mathfrak q\mid(n)}(1-1/\operatorname N\mathfrak q)\). There are \(\gg J^2\) such pairs, by the usual primitive lattice-point estimate with \(a\) odd (or by deleting common odd prime divisors from all the pairs with odd \(a\)). Among them \(\gg J^2\) have \(g(d)\ge c_0>0\) with \(c_0\) absolute.

Indeed \(-\log g(d)\le 3\sum_{p\mid d}1/p\) for odd \(d\). For each odd \(p\le J\), and each fixed \(b\), the congruence \(a^2+2b^2=0\bmod p\) admits at most two classes of \(a\). Hence the sum of \(1/p\) over divisibilities in the box contributes \(O(\sum_{p\le J}(J^2/p+J)/p)=O(J^2)\). At a given pair at most two primes exceeding \(J\) divide \(d\le3J^2\) when \(J>3\). Markov's inequality on the primitive subset gives the assertion.

The ideal \((\beta)\) involves only split odd primes, with at most one of the two places above each rational prime. Indeed an inert prime dividing \(\beta\), or both conjugate places dividing \(\beta\), would divide \(a,b\). Distinct selected \(\beta\) give distinct ideals even up to conjugation, since the only units are \(\pm1\) and both coordinates are positive.

## Counting at the height of each multiplier

Fix \(J\) and take \(M\) sufficiently large in terms of \(J\). For each selected \(\beta\), use odd indices \(N=dk\) in \([M\sqrt d,2M\sqrt d]\). A positive proportion of the odd \(k\) in that interval after scaling by \(1/d\) satisfy \(g(k)\ge c_1>0\), uniformly. This follows from the bounded mean of \(\sum_{p\mid k}1/p\) on odd dyadic intervals. Therefore \(\gg M/\sqrt d\) indices have \(g(N)\ge g(d)g(k)\ge c_0c_1\).

For each pair \((N,\beta)\) obtained this way let \(\mathfrak a=(N)/(\beta)\). This integral ideal has norm \(N^2/d\) and \(\mathfrak a\cap\mathbb Z=N\mathbb Z\). For the latter assertion each split prime of \((\beta)\) leaves its conjugate exponent in \((N)\) intact. The prime-weighted sum \(F(\mathfrak a)\) of first formal depths at exact annihilator \(\mathfrak a\), as in the CM calculation, satisfies
\[
 c_2N^2/d\le F(\mathfrak a)\le c_3N^2/d.
\]
The lower constant is independent of \(J\) because the product in the ideal mass formula is at least \(c_0c_1\), and its divisor-function error is \(o(\operatorname N\mathfrak a)\) uniformly as the norm grows. The upper bound also follows from the denominator height at a generator. If every contributing place lay over a rational prime of exponent at least two in \(B_N\), the mass would be at most \(4\log(B_N/\operatorname{rad}(B_N))\). This counts at most two places above each prime and uses \(e\le2(e-1)\) for \(e\ge2\).

If \(D<c_2/(24J^2)\), then for all sufficiently large \(N\) the last upper bound is less than \(c_2N^2/d\). There is therefore a prime \(p\) with \(v_p(B_N)=1\) in the exact annihilator group. Its reduction order for \(R=(-8,16)\) is \(N\). As shown in the CM calculation, transfer through the two-isogeny puts this prime in \(W\). The rational order distinguishes different \(N\), and at a fixed \(N\) a prime can occur only for two conjugate annihilator ideals. Thus each selected pair gives a distinct rational prime. Crucially
\[
 \log p\le F(\mathfrak a)\le c_3 N^2/d\le 4c_3 M^2
\]
holds with the same constant for every \(J\). Summing over the selected multipliers yields
\[
 W(\exp(4c_3M^2))\gg M\sum_{\beta}d^{-1/2}\gg MJ,
\]
with absolute implied constants for this fixed orbit. This proves \(K\ge c_4J\) whenever \(D<c_2/(24J^2)\). For finite \(K\), choose an integer \(J>K/c_4\) above the fixed lattice-count threshold. The contrapositive gives the claimed bound for \(D\).

Finally \(B_N\mid T_N\), where \(\operatorname{rad}(T_N)=\operatorname{rad}(a_Nb_Nc_N)\) and \(T_N\ll c_N\). Therefore \(\log(c_N/\operatorname{rad}(a_Nb_Nc_N))\ge\log(B_N/\operatorname{rad}(B_N))-O(1)\). Since \(\log\operatorname{rad}(a_Nb_Nc_N)\le\log c_N+O(1)\ll N^2\), this gives \(\limsup q_N\ge1+c_5D\). Heights tend to infinity, so any strict fixed exponent below this limsup gives infinitely many distinct primitive triples.
