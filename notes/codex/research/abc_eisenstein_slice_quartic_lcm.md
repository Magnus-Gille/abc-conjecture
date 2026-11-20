# The lcm of the paired quartics on the elliptic square slice

Let \(P=(-2,8)\) on \(E:Y^2=X^3+36X^2+36X\), and for odd \(n\ge3\) write \(X(nP)=-2(x_n/y_n)^2\) in primitive positive coordinates. Define
\[
 F_0=x^4-18x^2y^2+9y^4,\qquad
 F_\pm=F_0\pm12xy(x^2-3y^2),\qquad J_n=|F_+(x_n,y_n)F_-(x_n,y_n)|.
\]
Then, with the usual canonical height on \(E\),
\[
 \log\operatorname{lcm}_{3\le n\le N,\;n\ {\rm odd}}J_n
     =\frac43\widehat h_E(P)N^3+O(N^{5/2}).
\]
The total difference between the logarithm of the product and the logarithm of the lcm is \(O(N^{5/2})\). It is possible for a prime to occur with a high exponent at just one index; such layers do not contribute to this difference. [Parameters and heights](abc_eisenstein_twelfth_elliptic_slice.md) · [CM marked points and their independence](abc_eisenstein_slice_marked_divisors.md)

## Contact and the bad primes

Set \(E':v^2=u^3-576u\), \(Q=(-8,-64)\) and \(T=(0,0)\). Let \(i^2=-1\), \(h=3^{1/4}>0\), \(K=\mathbb Q(h,i)\), \(s=-168+96\sqrt3\), and \(S=(s,8h^3s)\). The four marks are \(S_1,\ldots,S_4=\pm S,\pm[i](S+T)\). For every pair of marks there are \(u_0\in\{1,-1,i,-i\}\) and a two-torsion point \(T'\) such that \(S_j=[u_0]S_i+T'\). The points \(Q,S_i\) are independent over \(\mathbb Z[i]\) modulo torsion, as proved in the marked-point calculation. In particular a nonzero coefficient vector of these two points always gives a nontorsion point. The 2-isogeny takes \(nP\) to \(nQ\), with
\[
 u(nQ)=-2(x_n^2-3y_n^2)^2/(x_ny_n)^2,\qquad
 u(nQ)^2+336u(nQ)+576=4F_+F_-/(x_ny_n)^4.
\]
Fix once for all a prime \(\mathfrak p\) of \(K\) over each \(p\ge5\). At these primes \(K\) is unramified and \(E'\) has good reduction. The two target abscissas differ by the unit \(192\sqrt3\), and each target ordinate is a unit. Thus \(p^j\mid J_n\) if and only if the reduction of \(nQ\) modulo \(\mathfrak p^j\) is one of the four distinct marked sections. If so, there is precisely one. Indeed \(p\mid x_ny_n\) precludes any quartic zero, and elsewhere the abscissa is an étale local parameter at each mark. In all subsequent sums a denominator ideal of a point formal modulo \(\mathfrak p^j\) has absolute norm divisible by \(p^j\). The local parameter \(-u/v\) has valuation at least \(j\).

The slice has \(x_n,y_n\) both odd and \(3\nmid x_n\). Thus \(v_3(J_n)=0\). The transforms
\[
 M_+(x,y)=(-x-3y,x-y),\quad M_-(x,y)=(-x+3y,-x-y)
\]
satisfy \(F_0(M_\pm)=-8F_\pm\), with the indicated signs. One transformed pair is twice a pair of odds, the other four times a pair of opposite parities: the two entries in either pair are equal up to sign modulo 4 and their suitable sum or difference is \(4y\). On odd pairs \(F_0\equiv8\pmod{16}\), and on opposite parities it is odd. Hence \(\{v_2(F_+),v_2(F_-)\}=\{4,5\}\) and \(v_2(J_n)=9\).

## Bounded denominators and pairwise gcds

Let \(\mathfrak B(A)\) be the denominator ideal of a nontorsion point on \(E'(K)\), at good primes only. For \(s,a,b\in\mathbb Z\),
\[
 \log N\mathfrak B(sQ-aS_j-bS_i)\ll1+s^2+a^2+b^2
                                                               \tag{1}
\]
whenever this point is nontorsion. This follows from the finite-place contribution to the abscissa height and the canonical-height quadratic form on the fixed span of the three points. The field \(K\) is fixed.

If both \(m,n\) have contact modulo \(\mathfrak p^j\) with marks \(S_j',S_i'\), respectively, then for every \((a,b)\in\mathbb Z^2\setminus\{0\}\) the point
\[
     R=(am+bn)Q-aS_j'-bS_i'
\]
is formal there. It is nontorsion for positive distinct \(m,n\), since torsion would force both \(am+bn=0\) and \(au_0+b=0\) for the unit linking the two marks. These imply \(m=u_0n\), which is impossible. Summing the norms over the sixteen pairs of marks therefore gives
\[
 \log\gcd(J_m,J_n)\ll
  1+\min_{(a,b)\in\mathbb Z^2\setminus\{0\}}
                     \{(am+bn)^2+a^2+b^2\}.                    \tag{2}
\]
This is \(O(\max(m,n))\) by Dirichlet approximation. More explicitly for \(m,n\le N\), take \(m\le n\), approximate \(m/n\) by \(-b/a\) with \(1\le a\le\lceil\sqrt N\rceil\) and \(|am/n+b|\le 1/\lceil\sqrt N\rceil\); then \(|b|,|am+bn|\ll\sqrt N\). It is also \(O(1+(m-n)^2)\) or \(O((\max(m,n)/\gcd(m,n))^2)\) by explicit coefficient choices. All gcds at a fixed nonzero gap \(g\) divide one integer of logarithm \(O(1+g^2)\), by taking \((a,b)=(1,-1)\) throughout.

## Counting repeated layers only once

A layer \((p,j)\) signifies the single weight \(\log p\) for \(p^j\mid J_n\). Denote its number of hits in the index set by \(k_{p,j}\). For \(p\ge5\), the total weight of all layers with at least two hits, counting each such layer once, is \(O(N^{5/2})\). Indeed the Dirichlet choice above gives integer coefficients \(|a|,|b|,|s=am+bn|\ll\sqrt N\) and a nontorsion point \(sQ-aS_j'-bS_i'\) whose denominator contains each such layer. There are only \(O(N^{3/2})\) coefficient triples and sixteen choices of marks. The upper bound (1) is \(O(N)\) for each. In taking the union, retain only nontorsion points; every actual collision is covered.

A second bound controls multiplicities. For a layer define \(r=r_{p,j}\) to be the order of the reduction of \(Q\) modulo \(\mathfrak p^j\). Hits occur in at most four residue classes modulo \(r\), one per mark. Every layer with at least one hit and \(r\le B\) is represented in the denominator of a nontorsion point
\[
 sQ-aS_i',\qquad |s|,|a|\ll\sqrt B.
\]
For \(n_0\) the first hitting index reduced into \([0,r)\), apply Dirichlet to \(n_0/r\) with limit \(\lceil\sqrt B\rceil\). This gives \(1\le a\ll\sqrt B\), \(s=an_0+br\) with \(|s|\ll\sqrt B\), and the desired congruence. Nonzero \(a\) proves nontorsion by independence. There are \(O(B)\) points, each of denominator log norm \(O(B)\). Therefore the total distinct weight of these layers is \(O(B^2)\).

Dyadically sum over \(B/2<r\le B\le 2N\), allowing the last truncated interval. Each layer has multiplicity \(O(1+N/B)\), so the weight **with multiplicity** of the hit layers with \(r\le N\) is \(O(N^2)\). When \(r>N\), at most four indices can hit and the union bound \(O(N^{5/2})\) applies to all collisions. At 2 all exponents are fixed and their repetitions cost \(O(N)\). This proves
\[
 \sum_{p,j}(k_{p,j}-1)_+\log p=O(N^{5/2}).
\]
The left side is exactly the logarithmic product-to-lcm difference.

## The archimedean contribution

Write \(H_n=\max(x_n,y_n)\), so \(\log H_n=\widehat h_E(P)n^2+O(1)\). The pointwise quantity \(8\log H_n-\log J_n\) is bounded below by an absolute constant. Its positive part is \(O(1)\) plus the maximum logarithmic proximity of \(nQ\) to the real marks in \(E'(\mathbb R)\), for any fixed translation-invariant smooth metric there. To check this, use \(t=x_n/y_n\) as projective coordinate. The reduced homogeneous product \(F_+F_-\) has eight simple roots and is a unit on the axes. Near a real root, its normalized absolute value is comparable to the distance in the \(t\) coordinate. The map \(t\mapsto u(nQ)=-2(t-3/t)^2\) is regular and Lipschitz there. The possibilities for the ordinate at the limiting abscissa are the ordinates of the corresponding marks, all nonzero. Local inversion of the abscissa on either real branch shows that \(nQ\) has distance at most a fixed constant times the normalized quartic product from a mark. Roots whose abscissa has no real ordinate cannot be approached by the admissible slice. Away from the roots the normalized quartic product is bounded below on the projective circle.

For a fixed mark the largest proximity among \(n\le N\) is \(O(N^2)\): the abscissa \(u(nQ)\) is rational of height \(O(N^2)\), and the target abscissa is quadratic irrational, so Liouville's inequality applies. If \(k\ge2\) points have distance \(\le e^{-v}\), two indices differ by \(1\le d\le N/(k-1)\). In the invariant metric \(dQ\) is within \(2e^{-v}\) of the origin. Near the origin the abscissa has a double pole, and \(h(u(dQ))=O(1+d^2)\), so \(v\ll1+N^2/(k-1)^2\). Summing these ordered proximity bounds gives \(O(N^2)\) for each mark. Consequently
\[
 \sum_{3\le n\le N,\;n\ {\rm odd}}\log J_n
   =8\widehat h_E(P)\sum_{3\le n\le N,\;n\ {\rm odd}}n^2+O(N^2).
\]
The odd-index square sum is \(N^3/6+O(N^2)\), completing the asymptotic.

For each fixed \(\delta>0\), it follows that all but \(O_\delta(\sqrt N)\) odd indices \(N/2\le n\le N\) retain logarithmic weight at least \(8\widehat h_E(P)n^2-\delta N^2\) in layers occurring at just that index in the prefix. Indeed the summed weight removed by deleting every shared layer is at most twice the product-to-lcm loss, and the summed archimedean loss is \(O(N^2)\). Distinct layers of the same prime may have different uniqueness properties.
