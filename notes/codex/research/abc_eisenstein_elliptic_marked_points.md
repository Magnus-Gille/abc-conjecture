# The marked points on the Eisenstein quartic have rank four

On the [twelfth-power elliptic slice](abc_eisenstein_twelfth_elliptic_slice.md), the 24 distinct marked points on \(E:Y^2=X^3+36X^2+36X\) comprise eight torsion points and sixteen nontorsion points. Modulo torsion the latter lie on four mutually orthogonal rational lines. Two lines are in the complex multiplication span of \(P=(-2,8)\); the other two span a second independent line over \(\mathbb Q(i)\).

## A second elliptic quotient and its marks

Use \(r=x/y\), \(s=z/y^2\), \(d=\sqrt{-3}\). The smooth projective quartic \(C\) with \(r^4-18r^2+9=-2s^2\) maps to \(E\) by \(\pi(r,s)=(-2r^2,4rs)\). It has degree two. Set
\[
 \lambda=(r+d)/(r-d),\qquad v=2s/(i(r-d)^2).
\]
Expanding \((r+d)^4+(r-d)^4\) gives \(v^2=\lambda^4+1\). Another degree-two map is
\[
 \Phi(\lambda,v)=(\lambda^2,\lambda v)\in E_1:\quad Y^2=X^3+X .
\]
Take either point \(B_0\) of \(C\) above \(r=\infty\) as origin. Then \(\pi(B_0)=O\), and \(\Phi(B_0)=(1,\pm\sqrt2)\) has order four. Thus \(\pi\) and \(\Phi-\Phi(B_0)\) are degree-two isogenies, which identify the groups tensored by \(\mathbb Q\). The specific isogeny \(\Theta:E\to E_1\) obtained by composing the dual of \(\pi\) with \(\Phi-\Phi(B_0)\) satisfies
\[
             \Theta(\pi(T))=2\Phi(T)-(0,0).
\]
These maps and the selected origins are defined over \(\mathbb Q(\zeta_{24})\).

The boundary consists of \(\lambda=0,\infty\) and \(\lambda=\zeta_{24}^k\) for \(k\bmod24\). For the last 24 values, \(X(\Phi)=\zeta_{12}^k\). The values \(X=\pm1,\pm i\) are torsion: \(\pm i\) are abscissas of points of order two, while doubling at \(\pm1\) gives \((0,0)\). The fibers at \(\lambda=0,\infty\) are also torsion. On \(E\) these are exactly the four points of \(E[2]\) and the four halves of \((0,0)\) with abscissa \(\pm6\), by \(X(\pi)=-2r^2\) or ordinary duplication on \(E\).

On \(E_1\), multiplication by \(i\) sends \(X\) to \(-X\), and translation by \((0,0)\) sends \(X\) to \(1/X\). Let \(T\) have \(X=e^{i\pi/3}\), and \(H\) have \(X=e^{i\pi/6}\), selecting either ordinate. Duplication gives
\[
  2T=(-3/4,\ \pm5\sqrt{-3}/8),\qquad
  2H=(-1/(4\sqrt3),\ \pm7i/(8\,3^{3/4})).
\]
Write \(u=3^{1/4}>0\). Scaling \((X,Y)\mapsto(h^2X,h^3Y)\) takes \(E_1\) to \(E_{h^4}:Y^2=X^3+h^4X\). With \(h=\sqrt{-3}\) for \(2T\) and \(h=iu\) for \(2H\), one obtains up to sign
\[
 A=(9/4,45/8)\in E_9(\mathbb Q),\qquad
 (1/4,7/8)=-2B,\quad B=(1,2)\in E_3(\mathbb Q).
\]
Both nonintegral rational points have infinite order by Nagell–Lutz. In \(L=\mathbb Q(\zeta_{24},u)\), the automorphism fixing \(\mathbb Q(\zeta_{24})\) and negating \(u\) fixes \(2T\) and negates \(2H\). It exists since \(\mathbb Q(u)\) is nonnormal and cannot be a subfield of the abelian cyclotomic extension. Since this automorphism fixes \(i\), the two points are independent over \(\mathbb Q(i)\) modulo torsion. Each point and its \(i\)-multiple are independent over \(\mathbb Q\). The Néron–Tate pairing between the two complex multiplication lines vanishes by the same automorphism. A point is orthogonal to its \(i\)-multiple because \(i\) is an isometry and \(i^2=-1\); the isogenies transfer orthogonality to \(E\).

The 48 boundary points of \(C\) give 24 points of \(E\), since the fixed-point-free deck involution \((r,s)\mapsto(-r,-s)\) preserves the boundary and interchanges \(\lambda\) with \(1/\lambda\). Among the sixteen nontorsion images, four lie on each of the following rational lines modulo torsion. The CM action is understood on \(E\otimes\mathbb Q\) via isogeny.

| \(k\pmod{12}\) | Rational line on \(E\) | Identification |
|---|---|---|
| 4, 8 | \(\mathbb Q P\) | \(X=-2,-18\), giving \(\pm P\) and \(\pm(P+(0,0))\) |
| 2, 10 | \(\mathbb Q iP\) | \(X=-42\pm24\sqrt3\) |
| 1, 11 | first new rational line | \(\Phi\) has class \(\pm H\) modulo torsion |
| 5, 7 | its \(i\)-multiple | \(\Phi\) has class \(\pm iH\) modulo torsion |

The subgroup generated over \(\mathbb Z\) by all marks is isomorphic to \(\mathbb Z^4\oplus\mathbb Z/4\oplus\mathbb Z/2\). In each of the four nontorsion classes choose one point \(V\). The four marks there are exactly \(\pm V\) and \(\pm(V+(0,0))\). Indeed \(\lambda\mapsto-\lambda\) sends \(r\mapsto-3/r\), hence \(X(\pi)\mapsto36/X(\pi)\), the abscissa transformation for translation by \((0,0)\). The four chosen points are independent modulo torsion, and the eight marked torsion points already form \([2]^{-1}(\langle(0,0)\rangle)\).

## The primes admitting a primitive-24 mark locally

For \(p>3\), the eight primitive-24 slopes are precisely roots of \(F_+F_-\). The ratio \(\lambda\) for a rational projective slope lies in the norm-one group of order \(p-(-3/p)\), using the split quadratic algebra when appropriate. The fractional linear transformation gives every element of this group, with the usual projective conventions (in the split case the two missing norm-zero directions correspond to 0 and infinity). Thus primitive-24 slopes occur exactly for \(p\equiv\pm1\bmod24\), with all eight slopes rational then. At each such slope
\[
   \frac{4s^2}{(r^2+3)^2}=-(\lambda^2+\lambda^{-2})=\pm\sqrt3 ,
\]
each sign occurring four times. For \(p\equiv23\bmod24\), exactly one sign is square. For \(p\equiv1\bmod24\), both are square if 3 is a fourth power modulo \(p\), and neither otherwise. This gives respectively eight, sixteen or zero points of \(C(\mathbb F_p)\) above primitive-24 slopes. The corresponding density of locally available primes is \(1/8+1/16=3/16\): the latter contribution is precisely the primes splitting completely in \(L\), which has degree 16. All the other good primes are excluded from dividing \(F_+F_-\) on the slice.

## A three-division obstruction on the orbit

The set of primes dividing some \(F_+F_-\) along the odd multiples of \(P\) has upper natural density at most
\[
                              \boxed{187/1296}.
\]
The finite test below removes primes of density \(5/324+1/36\) within the locally available set. Additional obstructions can further reduce the actual density.

Let \(M=L(E_1[3])\). This is also the field obtained by adjoining \(E_9[3],E_3[3]\) to \(L\), since the twists are isomorphic over \(L\). The 3-division polynomial of \(E_1\) is \(3X^4+6X^2-1\). Its abscissas are in \(L\); one is \((\sqrt6-\sqrt2)/(2u)\), and its conjugates give all four. More explicitly its square is \(-1+2/\sqrt3\), and the other pair of signed roots have square \(-1-2/\sqrt3\); their product squared is \(-1/3\), a square in \(L\). Since \(i\in L\), adjoining the ordinate of one point gives all of \(E_1[3]\): that point and its \(i\)-multiple span the one-dimensional \(\mathbb F_9\)-module. This extension has degree exactly two. At 5 a Frobenius commutes with \(i\) and has determinant \(5\bmod3=-1\), so its \(\mathbb F_9\)-scalar has order eight. The Galois group of \(L\) has exponent dividing four because it embeds in the direct product of the dihedral splitting group of \(X^4-3\) and the quadratic group of \(\sqrt2\). Hence \(\mathbb Q(E_1[3])\) is not a subfield of \(L\), and \([M:\mathbb Q]=32\).

Over \(M\), the field obtained by adjoining the 3-division points of \(A\) and \(B\) has translation group exactly \(E_9[3]\oplus E_3[3]\), of size 81. Here a 3-division point of \(A\) is any solution of \(3V=A\). The translation group is initially a subgroup, normal in the full Galois group over \(\mathbb Q\), because the two curves and points are rational. Two Frobenius computations prove equality:

| \(p\) | \(\#E_1(\mathbb F_p)=9h\) | \([h]A\) on \(E_9\) | \([h]B\) on \(E_3\) |
|---:|---:|---|---|
| 313 | 288 | \((256,290)\) | \((12,42)\) |
| 1201 | 1152 | \(O\) | \((803,258)\) |

Both primes split in \(L\), and at both the 3-torsion is rational: Frobenius commutes with \(i\), so one fixed nonzero vector forces the whole \(\mathbb F_9\)-line to be fixed. Here \(3\nmid h\), so \([h]\) projects onto the 3-primary part up to an automorphism there, and its vanishing is equivalent to local 3-divisibility. The primes are unramified in the division fields (good reduction and \(p\ne3\)). The row at 1201 supplies a translation \((0,b)\), \(b\ne0\), and the row at 313 supplies \((a,b')\), \(a\ne0\). Conjugating by any Frobenius at 5 acts on either coordinate by a primitive \(\mathbb F_9\)-scalar, by the same determinant argument on each twist. From \((0,b)\) this gives the entire second coordinate space. Subtracting a suitable element gives \((a,0)\), which yields the entire first space in turn.

At a prime splitting completely in \(M\), identify the two 3-torsion groups with \(E_1[3]\) using the twists. Up to a zero-density finite set, the Frobenius translations \((a,b)\) in this set of primes are distributed by counting elements of the 81-element translation group for any conjugacy-invariant condition. The finite-field Kummer map into \(E_1[3]\) is additive and commutes with \(i\). The comparison via \(\Theta\) shows that an orbit hit needs \(na=\xi b\) for one of \(\xi=\pm1,\pm i\); factors of 2 in the twists reduce to signs, and the marked torsion shifts are killed in the quotient by triples. For \(a=0\) and \(b\ne0\) all hits are excluded (eight pairs). For each of the eight nonzero \(a\), four choices of \(b\) outside \(\{0,\pm a,\pm ia\}\) likewise exclude every hit. The condition is invariant under conjugation: the fourth-root scalings used for the twist identifications change by fourth roots of unity, and Galois preserves their group. Chebotarev thus removes density \(40/(81\cdot32)=5/324\).

For primes \(p\equiv23\bmod24\), the two rational twists have trace zero (the character sums for \(X^3+aX\) cancel at \(X,-X\)). Their mod-3 Frobenius has eigenvalues \(+1,-1\). On each 3-division torsor, for a fixed base Frobenius in \(M\), varying the lift adds uniform independent translations. A fixed point exists precisely when the translation lies in the image of Frobenius minus one, which has three elements. Thus the conditional frequency that \(A\) is locally 3-divisible and \(B\) is not is \((1/3)(2/3)=2/9\). Such a pair of conditions rules out a hit: all elements of \(L\) reduce in \(\mathbb F_{p^2}\), since its cyclotomic part has residue degree two and \(3\) is already a fourth power in \(\mathbb F_p\) (it is a square and \(p\equiv3\bmod4\)). The twist identifications and marked comparisons therefore apply over \(\mathbb F_{p^2}\). Nondivisibility of a rational \(B\) persists there, by taking the trace and using that two is invertible modulo three. This removes density \((1/8)(2/9)=1/36\). Subtraction from \(3/16\) gives the stated bound. [Arithmetic verifier](abc_eisenstein_elliptic_marked_verify.py)

## The least common multiple of the two primitive factors

For the admissible positive odd indices \(n\ge3\) put \(U_n\) equal to the positive part of \(|F_+(x_n,y_n)F_-(x_n,y_n)|\) prime to 6. For \(h\ne0\) even one has, uniformly in the two admissible indices,
\[
                   \log\gcd(U_n,U_{n+h})\ll 1+h^2.                      \tag{1}
\]
In fact for the odd indices of *any* interval \(I\) of length \(H\ge1\),
\[
 0\le\sum_{n\in I}\log U_n-\log\operatorname{lcm}_{n\in I}U_n
                   \ll 1+H^3.                                         \tag{2}
\]
The implied constants depend only on the fixed curve, point and marks. In particular, if \(I\subset[N,N+H]\) is the full interval there with \(H=o(N)\) and contains some admissible index, its least common multiple has logarithm \((8\widehat h(P)+o(1))\sum_{n\in I}n^2\), summing over the odd indices. Over all admissible indices through \(N\) the logarithm of the least common multiple has order \(N^3\).

To prove (1), write \(\mathcal T\) for the eight marked points of \(E\) arising from primitive-24 slopes, all in \(E(L)\). For every \(T,T'\in\mathcal T\) and nonzero integer \(h\), the point \(Z_{h,T,T'}=hP-(T'-T)\) is nonzero. This follows from the independence of the two complex multiplication lines: modulo torsion every difference on the right is in the new line. Put \(G_h\) equal to the product, over the ordered pairs, of the absolute norms of the denominator ideals of these points away from 6. At good primes define the denominator ideal exponent as \(\max(0,-v_{\mathfrak p}(X(Z))/2)\), the formal-group depth. The height comparison on the fixed curve and the quadratic canonical height give \(\log G_h\ll1+h^2\).

For every \(p>3\), primitive-24 slopes remain distinct modulo \(p\) and have \(r\), \(r^2+3\), and \(s\) units at each of their lifts. They are simple roots of the dehomogenized \(F_+F_-\), since the torus coordinate change is invertible there and \(p\nmid24\). Also the leading coefficient of this polynomial is one, so \(y_n\) is a unit at a prime dividing \(U_n\). Fix a place of \(L\) above \(p\); it is unramified. A divisibility \(p^e\mid U_n\) then places \(r_n\) modulo \(p^e\) at one of the corresponding slopes, with the sign of \(s_n\) specifying its lift since \(2s\) is a unit. Consequently \(nP\) reduces modulo \(p^e\) to a point of \(\mathcal T\). If the same prime power divides \(U_{n+h}\), subtraction in the good reduction group puts \(Z_{h,T,T'}\) in the depth-\(e\) kernel. Thus \(p^e\mid G_h\). This proves (1) with a common integer \(G_h\) for all \(n\) at that gap.

Let \(r(p,e)\) be the order of \(P\) in the group of points modulo \(p^e\). For each prime power, hits occupy at most eight index classes modulo this order. Moreover \(p^e\mid B_{r(p,e)}\), where \(B_j^2\) is the denominator of \(X(jP)\) over \(\mathbb Q\). Therefore the sum of \(\log p\) over all pairs \((p,e)\) with a given order \(r\) is at most \(\log B_r\ll r^2\). The contribution of all pairs of order at most \(H\) to the sum of log factors on the interval is at most
\[
             8\sum_{r\le H}(1+H/r)\log B_r\ll 1+H^3.
\]
For order larger than \(H\), each prime power appears at most eight times in \(I\). If it appears twice or more, some gap \(1\le h\le H\) places it in \(G_h\). The sum of its repeated logarithms across all such prime powers is bounded by \(8\sum_{h\le H}\log G_h\ll1+H^3\). Together these bounds prove (2).

Finally \(\log U_n=8\widehat h(P)n^2+o(n^2)\) by the archimedean proximity estimate in the slice note for the degree-eight form \(F_+F_-\). Removing 2 and 3 costs only a constant. At 3 the unit \(x_n\) gives \(3\nmid F_+F_-\). At 2, for odd \(r=x_n/y_n\), the values \(F_\pm(r,1)\bmod64\) depend only on \(r\bmod4\), by polynomial expansion after replacing \(r\) by \(r+4\). For \(r=1,3\) the residues are respectively \((32,16),(16,32)\), so their product has exact 2-adic valuation nine. The interval asymptotic follows since the loss in (2) is \(o(\sum_{n\in I}n^2)\) there. For the lower bound through \(N\), take a terminal interval of length \(\delta N\) with \(\delta>0\) a sufficiently small constant; the factor sum is \(\gg\delta N^3\) and the loss is \(O(\delta^3 N^3)\). The matching upper bound follows by summing the individual heights. These estimates control prime powers and do not by themselves bound individual radicals from below.

## Thirteen separate large primes for almost every index

Uniformly in \(N,Y\ge2\), for all sufficiently large \(N\), at most \(O(1+\pi(Y))\) of the admissible odd indices \(N<n\le2N\) lack a prime greater than \(Y\) in at least one of the following thirteen integers:
\[
 |z|,\quad |F_+|,\quad |F_-|,\quad x,\quad y,\quad
 |x-y|,\ x+y,\ |x-3y|,\ x+3y,\quad
 |x^2-3y^2|,\quad |x^2\pm6xy-3y^2|,\quad x^2+3y^2 .
\]
The two choices in \(\pm\) are counted separately. For \(Y\ge3\) the thirteen primes at each remaining index are distinct. In particular all thirteen exceed any specified \(Y(N)=o(N\log N)\) simultaneously for density one of the odd indices. This lower bound on the sizes and number of primes does not imply a positive-power lower bound for the radical in terms of \(W^{12}\).

Let \(D'_n\) be the product of these thirteen integers after removing 2 and 3. Each prime \(p>3\) occurs in at most one factor, since the directions for the factors are disjoint: they are \(0,\infty\) and the 24th roots of unity in the \(\lambda\)-coordinate, with \(z\) using the four simple directions of \(F_0\). A divisibility \(p^e\mid D'_n\) puts \(nP\) within depth \(e\) of one of the 24 marks on \(E\). For the primitive-24 directions this was shown above. In the other finite directions distinct from \(r=0\) and \(F_0=0\), both \(r,s\) are units and the same simple-root argument applies. At \(r=0\), the depth at \((0,0)\) is given by \(Y=4rs\). At a root of \(F_0\), \(s\) is the local parameter on the quartic and \(Y=4rs\) is the local parameter at the corresponding 2-torsion point of \(E\). At \(y=0\), the order of the denominator of \(X=-2(x/y)^2\) gives the required depth at infinity.

The classification shows that \(T'-T=hP\) for two marks is impossible whenever \(|h|>2\): the coefficients in the rational \(P\)-line of the marked points take only the values \(0,1,-1\). Applying the denominator-product proof of (1) to the full set of marks consequently gives
\[
                 \log\gcd(D'_n,D'_{n+h})\ll h^2 \quad(h\ge4\text{ even}).
\]
For each prime \(p\) order the weights \(v_p(D'_n)\log p\) in the dyadic interval in decreasing order. The first three weights are \(O(N^2)\) by height. Among the indices of the largest \(j\ge4\) weights, select alternating ones in order of index; some two selected indices have gap at least four and at most \(O(N/j)\). The preceding gcd bound makes the \(j\)-th largest weight at most \(O(1+N^2/j^2)\). Summing gives, for any prescribed set \(S\) of \(K\) primes outside 6,
\[
             \sum_{N<n\le2N}\sum_{p\in S}v_p(D'_n)\log p\ll K N^2.         \tag{3}
\]

Each of the thirteen factors has logarithm \(c_i n^2+o(n^2)\) after removing 2 and 3, for a fixed \(c_i>0\). At infinity this is the proximity estimate in the slice note, using half the quartic degree for \(z\). At either fixed finite prime the same proof gives proximity \(o(n^2)\) to each fixed algebraic projective root. Explicitly, write \(n=ma+j\) for each fixed \(m\). The local degrees of \(T\mapsto X([m]T+jP)\) are at most two. Proximity to its finitely many algebraic preimages is bounded by proximity of \(X(aP)\) to the respective algebraic abscissas, plus constants depending on \(m\). The finite-place Roth theorem for irrational targets and elementary height separation for rational ones give an upper bound \(O(h(X(aP)))+O_m(1)\) on logarithmic proximity. After division by \(n^2\), let \(m\) grow. The fixed map \(X=-2r^2\) transfers the estimate to the \(r\)-direction. This proves the asserted negligibility at 2 and 3.

If an index lacks a prime outside \(S\cup\{2,3\}\) in *any* of the thirteen factors, it contributes at least \(\frac12\min_i c_i\,N^2\) to the sum in (3), for sufficiently large \(N\). There are therefore only \(O(K)\) such indices. Taking all primes through \(Y\) proves the assertion.
