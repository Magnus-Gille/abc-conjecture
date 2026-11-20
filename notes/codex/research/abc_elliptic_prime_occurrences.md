# First occurrences of primes in an elliptic family of abc triples

Fix \(D=14637\), \(N=2D\), and \(E:y^2=x^3-N^2x\). Take the four independent points \(A_1,\ldots,A_4\) with coordinates

\[
(1771077,2356659459),\quad (142188,52467372),\quad
(171462,69956496),\quad (313650,174891240).
\]

Set \(Q_i=2A_i\) and \(Q(\mathbf m)=\sum_{i=1}^4 m_iQ_i\) for \(\mathbf m\in\mathbb Z^4\). For nonzero \(\mathbf m\), write \(t=y(Q)/(2x(Q))=u/v\) in lowest terms, \(v>0\), and \(w=|x(Q)/2-t^2|v^2\). We use the primitive triple
\[
 a=u^4,\qquad b=D^2v^4,\qquad c=w^2=a+b.
\]
Here \(\operatorname{rad}(h)\) is the product of the distinct primes dividing the positive integer \(h\). Independence and the height and isogeny facts recalled below are proved in the [previous note](abc_elliptic_quartics.md).

## Primitivity for all nonzero vectors

Every point in this group is a double. To check the condition \(\gcd(u,D)=1\) for \(Q=2S\), write \(t(S)=j/k\) in lowest terms, \(g=\gcd(j,D)>0\), \(j=gj_0\), and \(D=ge\). Then \(w(S)^2=j^4+D^2 k^4=g^2W^2\), with \(W^2=g^2j_0^4+e^2k^4\). The duplication formula gives
\[
 x(2S)=\left(\frac{W}{j_0k}\right)^2,\qquad
 t(2S)=\pm\frac{g^2j_0^4-e^2k^4}{2j_0k W}.
\]
Each prime dividing \(D\) divides exactly one of \(g,e\), since \(D\) is squarefree. If it divides \(g\) it divides neither \(e\) nor \(k\). If it divides \(e\) it divides neither \(g\) nor \(j_0\). Thus every such prime avoids the numerator of \(t(2S)\). The resulting \(u^4,D^2v^4\) are coprime.

Let \(E':y^2=x^3+4N^2x\), with the isogeny \(\phi:E\to E'\) given away from its kernel by
\[
 (x,y)\longmapsto (x-N^2/x,\; y(1+N^2/x^2)).
\]
For \(Q=Q(\mathbf m)\ne O\), set \(B(Q)=|uvw|\), \(C(Q)=w^2\) and \(R(Q)=\operatorname{rad}(abc)\). The reduced denominator of \(x(\phi(2Q))\) is \(B(Q)^2\). Moreover
\[
 R(Q)=\operatorname{rad}(D B(Q)),\qquad
 \log C(Q)=8\widehat h(Q)+O(1),\qquad B(Q)\le C(Q).
\]
The last inequality follows from \(w^2\ge2D u^2v^2\). With \(D\) fixed, the fixed-place estimates in the previous note give \(\log(C(Q)/B(Q))=o(\log C(Q))\) and \(v_p(B(Q))\log p=o(\log C(Q))\) for each fixed \(p\).

## Repeated factors along multiples of one point

Take \(Q\ne O\) in this group, \(T=\phi(2Q)\), \(B_n=B(nQ)\), \(C_n=C(nQ)\), \(R_n=R(nQ)\), and \(H_n=8n^2\widehat h(Q)\). For \(p\nmid2N\) let \(r_p\) be the order of \(T\bmod p\) in \(E'(\mathbb F_p)\), including order one. Then \(p\mid B_n\) exactly when \(r_p\mid n\), and in that case
\[
 v_p(B_n)=v_p(B_{r_p})+v_p(n/r_p).                                      \tag{1}
\]
Indeed divisibility is reduction to the identity. The formal parameter \(-x/y\) has valuation \(v_p(B_n)\) there. At these odd good primes the formal logarithm is an isometry on \(p\mathbb Z_p\) and carries multiplication by \(n/r_p\) to ordinary multiplication. These are standard good-reduction and formal-group facts. [Silverman, *The Arithmetic of Elliptic Curves*, Chapters IV and VII](https://doi.org/10.1007/978-0-387-09494-6)

Group the good primes by their first index. Write \(F_d=\prod_{r_p=d}p^{v_p(B_d)}\) and \(W_d=F_d/\operatorname{rad}(F_d)\), taking empty products as one. By (1), the part of \(B_n\) supported on good primes is \(\prod_{d\mid n} F_d\) times the integer \(\prod_{r_p\mid n}p^{v_p(n/r_p)}\), which divides \(n\). Removing the finitely many bad primes by the fixed-place estimates gives
\[
 \log(C_n/R_n)=\sum_{d\mid n}\log W_d+o(H_n).                              \tag{2}
\]
The error estimate holds as \(H_n\to\infty\), including when \(Q\) varies in the group. Indeed \(\log n=o(H_n)\) uniformly because the positive canonical heights here are bounded below.

The total log size at the first index can be evaluated:
\[
 \log F_n=8\widehat h(Q)\, n^2\prod_{\ell\mid n,\ \ell\ \mathrm{prime}}(1-\ell^{-2})+o(H_n).  \tag{3}
\]
For the proof, the preceding product gives \(\sum_{d\mid n}\log F_d=H_n+o(H_n)\). Möbius inversion gives the displayed main term. To control the errors in inversion, use \(\sum_{d\mid n}d^2\le\zeta(2)n^2\). Above any sufficiently large height cutoff the error at \(d\) is at most an arbitrarily small constant times \(d^2\widehat h(Q)\). Below that cutoff the group has finitely many points and, for each \(Q\), the points \(dQ\) for positive \(d\) are distinct. Their total error is uniformly bounded for that cutoff.

For a fixed \(Q\), put \(L_Q=\limsup_{d\to\infty}\log W_d/(8d^2\widehat h(Q))\). Nonnegativity, (2), and the same divisor-sum estimate give
\[
 L_Q\ \le\ \limsup_{n\to\infty}\frac{\log(C_n/R_n)}{H_n}\ \le\ \zeta(2)L_Q.
\]
Thus a fixed positive-power deficit on this sequence is equivalent to one already present in the repeated part of infinitely many first-index products. Equation (3) controls the size of \(F_n\); it supplies no lower bound of comparable log size for its radical.

## A density bound including primes with an exceptional first exponent

Let \(M\ge2\), let the coefficient vectors range over \(0<\|\mathbf m\|_\infty\le M\), and put
\[
 S_X(\mathbf m)=\sum_{\substack{p\le X\\p\nmid 2N}}
            \max(v_p(B(Q(\mathbf m)))-1,0)\log p .
\]
For every real \(X\ge3\) the following bounds hold, with constants depending only on the curve and the four points:
\[
 \frac{1}{(2\lfloor M\rfloor+1)^4}\sum_{0<\|\mathbf m\|_\infty\le M}S_X(\mathbf m)
       \ll \frac{X}{(\log X)^2},                                             \tag{4}
\]
\[
 \frac{\#\{\mathbf m:0<\|\mathbf m\|_\infty\le M,\ S_X(\mathbf m)\ge\eta\log C(Q(\mathbf m))\}}
 {(2\lfloor M\rfloor+1)^4}
       \ll \frac{X}{\eta M^2(\log X)^2}\qquad(\eta>0).                     \tag{5}
\]
In particular, take \(X=M^2(\log M)^{2-\delta}\) with any fixed \(0<\delta<2\). For each fixed \(\eta>0\) the exceptional proportion in (5) is \(O_\eta((\log M)^{-\delta})\) as \(M\to\infty\). The finite bad primes also give a vanishing fraction of \(\log C\) as the height grows.

To prove (4), for a good \(p\) and \(k\ge2\) let \(\Lambda_{p,k}\subset\mathbb Z^4\) be the vectors for which \(\phi(2Q(\mathbf m))\) is the identity modulo \(p^k\). This is a subgroup and, away from zero, it is exactly the condition \(p^k\mid B(Q(\mathbf m))\). Quadraticity of the canonical height gives, for each nonzero member,
\[
 k\log p\le\log B(Q(\mathbf m))\le \log C(Q(\mathbf m))\le K\|\mathbf m\|_\infty^2
\]
for a fixed \(K\). Distinct vectors in the subgroup are separated in the sup norm by at least \(s=\sqrt{k\log p/K}\). If a nonzero member occurs in the box then \(M\ge s\). Packing disjoint cubes of side \(s\) about subgroup members therefore bounds the number in the box by \((1+2M/s)^4\ll M^4/(k\log p)^2\). When the box has no nonzero member the same bound on their number is immediate. Multiply by \(\log p\) and sum over \(k\ge2\). A given prime contributes at most \(O(1/\log p)\) to the box average. Summing this over \(p\le X\) gives (4) by the elementary Chebyshev bound for the prime-counting function and partial summation.

For (5), independence of the four points makes the height pairing positive definite, hence \(\log C(Q(\mathbf m))\gg \|\mathbf m\|_\infty^2\) for nonzero vectors. The bounded height error can be absorbed on the finitely many small vectors since \(C>1\). Apply (4) on each dyadic shell \(U/2<\|\mathbf m\|_\infty\le U\) using the enclosing box of radius \(U\). The sum of \(S_X/\log C\) on the shell is \(O(U^2 X/(\log X)^2)\). Summing the geometric series in \(U^2\) and applying Markov's inequality proves (5).

## Numerical check of the first exponents

On each generator \(Q_i\) check all 9587 primes \(p\le100000\) with \(p\nmid2N\). These are all pairs with \(v_p(B(r_pQ_i))\ge2\).

| Generator | Prime \(p\) | First index \(r_p\) | \(v_p(B(r_pQ_i))\) |
|---|---:|---:|---:|
| \(Q_1\) | 359 | 45 | 2 |
| \(Q_2\) | 79 | 5 | 2 |
| \(Q_3\) | 23 | 1 | 2 |
| \(Q_4\) | 23 | 3 | 2 |
| \(Q_4\) | 1231 | 77 | 2 |
| \(Q_4\) | 3881 | 25 | 2 |

The script computes \(r_p\) in the reduction and tests whether \((r_p-1)T=-T\bmod p^k\) for successive \(k\), starting at two. For \(r_p>1\) the binary multiplication uses positive intermediate scalars strictly below \(r_p\). A noninvertible doubling denominator would make the doubled scalar a multiple of \(r_p\), and a noninvertible addition denominator would require the even intermediate scalar to equal \(1\) or \(-1\bmod r_p\). Neither can occur during that addition. For \(r_p=1\) the script uses the exact rational denominator. For all six listed pairs a second calculation multiplied \(T\) by \(r_p\) directly over \(\mathbb Q\) and found \(v_p(x(r_pT))=-4\). Run the script with Python and the cypari and sympy packages. [Reproducible calculation](abc_elliptic_prime_check.py)

For a disproof it suffices to find \(\log(c/\operatorname{rad}(abc))\ge\eta\log c\) for one fixed \(\eta>0\) and unbounded \(c\). The density bound permits an infinite exceptional sequence. It also leaves primes above \(X\) unrestricted. Equations (1)–(3) locate the obstacle on a fixed sequence of multiples: the total excess multiplicity already present when the varying good primes first occur.
