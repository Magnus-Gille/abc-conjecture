# The Gaussian angle requirements force a large height

The short-vector estimate suggested for the [many-triangle construction](abc_many_square_triples_with_distinct_primes.md) cannot hold. This has an elementary proof using one nonzero integer in each column. There is also an obstruction when only the final triangle angles are prescribed. That second obstruction depends on how many sign patterns are used.

## The height cost in the original construction

Retain the original notation. For each column \(b\) put \(G_b=\prod_j\gamma_{jb}^{|z_j|}\), conjugating each factor for which \(z_j<0\). Let \(D_b=N(G_b)\) and \(\theta_b=\sum_jz_j\arg(\gamma_{jb}/\bar\gamma_{jb})\). The disjoint norm supports and \(\gcd(\gamma_{jb},\bar\gamma_{jb})=1\) imply \(\gcd(G_b,\bar G_b)=1\). Since \(z\ne0\) and all original norms exceed 1, each \(G_b\) is a nonunit. In particular its imaginary part is a nonzero integer. The construction even makes it divisible by \(P=\prod_{p\le Y,\ p\nmid Q}p\), since every \(K_{jb}\) in \(\gamma_{jb}=1+iK_{jb}\) is zero modulo \(P\).

The identity \(G_b/\bar G_b=e^{i\theta_b}\) gives
\[
 P\le|\operatorname{Im}G_b|=\sqrt{D_b}\,|\sin(\theta_b/2)|.
\]
Thus \(|\theta_b|<e^{-S}\) in each column forces
\[
 \log u=\sum_{b=1}^r\log D_b>2r\bigl(S+\log(2P)\bigr).
\]
In the construction \(r\to\infty\) and \(T/S\to0\). In particular \(\log u/(S+T)\to\infty\) for **every** admissible nonzero vector. Optimizing the search for that vector cannot give a fixed-power saving from the stated angular accuracy and prescribed prime contributions. This leaves the established lower bound intact, and allows other prime factors of the actual legs to contribute.

## Allow each row to choose its nearest axis

More generally let \(G_1,\ldots,G_r\) be nonunit Gaussian integers, each coprime to its conjugate, with pairwise coprime odd norms \(D_b\). Put \(u=\prod_bD_b,\ \Omega_b=G_b/\bar G_b\), and \(\beta_s=\prod_b\Omega_b^{s_b}\) for \(s\in\{-1,1\}^r\). Then \(u\beta_s\) is a Gaussian integer of norm \(u^2\) giving primitive integer legs. Define the axis error to be the angular distance of \(\beta_s\) to \(\pi\mathbb Z/2\); equivalently, for \(v_s\) the smaller absolute coordinate, \(\sin(\text{axis error})=v_s/u\).

**The full set of signs.** If all signs have error at most \(\varepsilon<\pi/4\), then
\[
 \sin\varepsilon\ge 2^{-1/2}u^{-1/r}.
\]
Indeed, the two endpoints of any one-coordinate flip give \(\Omega_b^2\) within angular distance \(2\varepsilon\) of an axis. Hence \(G_b^2/D_b=\Omega_b\) lies within \(\varepsilon\) of a line at angle \(j\pi/4\). Each such line has a primitive integer normal of length at most \(\sqrt2\). The Gaussian integer \(G_b^2\) is off all these lines: lying on one would make \(\Omega_b\) a root of unity, impossible by the disjoint factorizations of \(G_b\) and \(\bar G_b\). Its distance from the line is therefore at least \(1/\sqrt2\). Since \(|G_b^2|=D_b\), multiplication of the inequalities \(D_b\sin\varepsilon\ge1/\sqrt2\) proves the claim.

**Any fixed positive fraction.** Suppose \(K\ge\lambda 2^r\) signs have error at most \(\varepsilon<\pi/4\), with \(\lambda>0\) fixed. At least half of those signs have their nearest axis of the same type, real or imaginary. For two distinct signs \(s,t\) of the same type, let \(I\) contain the coordinates on which they differ. Set \(X_I=\prod_{b\in I}G_b\), conjugating for negative \(s_b\), and \(U_I=\prod_{b\in I}D_b\). The quotient \(\beta_s/\beta_t=(X_I/\bar X_I)^2\) is within \(2\varepsilon\) of the real axis, so \(X_I\) is within \(\varepsilon/2\) in angle of a line at \(j\pi/4\). The same nonvanishing integer-normal argument now uses \(|X_I|=\sqrt{U_I}\). Thus the weighted Hamming distance of these signs satisfies
\[
 \log U_I\ \ge\ D:=\log\!\left(\frac{1}{2\sin^2(\varepsilon/2)}\right).
\]
Open weighted Hamming balls of radius \(D/2\) about those signs are disjoint. Each contains its center and the flip of every individual coordinate of weight \(\log D_b<D/2\). There can be at most \(2/\lambda-1\) such light coordinates, by counting vertices of the cube. Consequently
\[
 \log u\ge (r+1-2/\lambda)\,D/2 .
\]
In particular, when \(r\to\infty\) a fixed positive fraction of the signs cannot all have \(v_s/u\le u^{-\delta}\) for fixed \(\delta>0\). This applies to the retained rows of the original construction, which occupy a positive fraction of its column sign patterns. It also covers the proposal to constrain only the final angles and permit different axes for different rows.

## A family attaining the full-set exponent

For any fixed **even** \(r\ge2\), arbitrarily large \(u\) admit \(r\) such columns for which every sign choice has axis error \(O_r(u^{-1/r})\). These \(2^{r-1}\) unordered primitive representations need not exhaust all representations of \(u^2\).

Write \(A_j+B_j\sqrt2=(1+\sqrt2)^j\). Set \(G_j=A_j+B_j+iB_j\). Its norm is \(B_{2j+1}\), since \(A_{2j}=A_j^2+2B_j^2,\ B_{2j}=2A_jB_j\), and \(B_{2j+1}=A_{2j}+B_{2j}\). This is odd. The equation \(A_j^2-2B_j^2=(-1)^j\) implies that \(G_j\) is coprime to its conjugate. It also gives \(A_j/B_j=\sqrt2+O(B_j^{-2})\), so \(\arg(G_j/\bar G_j)=\pi/4+O(1/N(G_j))\).

Put \(W=r!\) and choose \(j_b=W(N+b)\) for \(1\le b\le r\), with \(N\to\infty\). The indices \(2j_b+1\) are pairwise coprime: any common prime would divide \(2W(b-b')\), hence \(2W\), whereas every index is 1 modulo \(2W\). The Pell identity \(\gcd(B_a,B_b)=B_{\gcd(a,b)}\) now gives pairwise coprime norms. It follows from the Euclidean algorithm using \(B_{a+b}=A_aB_b+B_aA_b\) and \(\gcd(A_b,B_b)=1\). The norms are comparable up to fixed \(r\)-dependent constants as their indices differ by bounded amounts. Each is therefore \(\asymp_r u^{1/r}\). Every signed sum of \(r\) copies of \(\pi/4\) belongs to \(\pi\mathbb Z/2\) when \(r\) is even. Summing the error terms proves the assertion. Distinct signs modulo simultaneous reversal give different unordered pairs by Gaussian factorization.

This shows exactly what can be gained through the real angles at fixed even \(r\). A small leg multiplies the radical saving by \(u^2/(v_sw_s)\); the full saving also divides by \(\operatorname{rad}(u)\) and depends on repeated prime divisors of both legs.
