# Fixed powers in the octic radical inequality

For positive coprime \(s,t\), with \(s\) odd and \(t\) even, write \(H=\max(s,t)\) and use the six binary forms
\[
 f_i=s,\quad t,\quad s^2-2t^2,\quad s^2+2t^2,\quad
 (s-t)^2+t^2,\quad(s+t)^2+t^2 .
\]
Their values are nonzero and coprime in pairs. Their product equals \(st(s^8-16t^8)\); the extra factor 2 already occurs in \(t\). Write \(R\) for the radical of the product. The full rational abc conjecture is equivalent to \(R\gg_\eta H^{8-\eta}\) for every \(\eta>0\). [Explicit transfer](abc_rational_pell_transfer.md)

Choose fixed positive integers \(m_i,c_i\), taking \(c_i=1\) when \(m_i=1\). Impose \(|f_i(s,t)|=c_i u_i^{m_i}\) with \(u_i\) a positive integer. Set \(d_i=\deg f_i\) and
\[
 W=\sum_{i=1}^6d_i(1-1/m_i).
\]
The fixed identities give \(R\ll_{\boldsymbol c}H^{10-W}\). Consequently \(W>2\) would suffice to disprove abc if such a family were infinite. In fact **every fixed choice with \(W>2\) has only finitely many primitive pairs**. For example this excludes a square and a cube, up to fixed coefficients, in any two distinct quadratic factors. The primes dividing the square and cube bases can range freely.

When \(W=2\), an infinite family would lie on finitely many fixed curves of genus one over a fixed number field. For any fixed finite set of rational primes \(S\), let
\[
 B_{S^c}=\prod_i\prod_{p\notin S}p^{\max(v_p(u_i)-1,0)}.
\]
Along every infinite sequence in such a fixed family,
\[
 \log R=8\log H-\log B_{S^c}+o(\log H).
\]
Thus a fixed-exponent abc violation on a boundary family would need a positive proportion of \(\log H\) from repetitions in the bases \(u_i\) outside **every** fixed set of primes. The finiteness assertion above and this boundary estimate are ineffective.

## Constructing the covers for different exponents

Here is a direct proof for these six forms. It uses the covering principle behind the fixed-signature generalized Fermat theorem. The explicit construction explains why different powers in different factors are permitted. [Darmon and Granville](https://doi.org/10.1112/blms/27.6.513)

Over \(K=\mathbb Q(i,\sqrt2)\) the ten distinct projective roots are \(0,\infty,\pm\sqrt2,\pm i\sqrt2,1\pm i,-1\pm i\). Mark the roots of every \(f_i\) having \(m_i>1\) with the order \(m_i\). Remove a finite set of primes containing those over the \(c_i\) and 2, the primes at which any marked roots collide, and primes used by the coefficients of the projective changes of coordinate. At every other prime the reduction of \((s:t)\) can meet at most one marked point. If it does, the order of vanishing of the corresponding primitive linear form is a multiple of its marked order. Indeed the other linear factors and the local coordinate used for normalization are units, so the order is that of \(f_i(s,t)\).

For \(W\ge2\) at least one quadratic factor is marked. The two linear factors alone have total weight strictly below 2. Take the two roots \(\alpha,\beta\) of a marked quadratic of order \(m\). The value of \((x-\alpha)/(x-\beta)\), \(x=s/t\), has all its valuations outside that finite set divisible by \(m\). Such values occupy finitely many classes modulo \(K^{*m}\). This follows by taking prime ideals with their exponents divided by \(m\), using finiteness of the ideal class group and finite generation of the group of units outside the excluded primes. After one fixed finite extension of \(K\), each of these values has an \(m\)-th root. All input slopes therefore lift to points, over that fixed field, on the rational curve
\[
 w^m=(x-\alpha)/(x-\beta).
\]
Its projection to \(x\) has degree \(m\) and branches only at \(\alpha,\beta\).

Each other marked point of order \(n\) has \(m\) distinct inverse images on this \(w\)-line. Enlarge the fixed field to contain their coordinates. Away from finitely many further primes the map has unramified good reduction at the inverse images, so contact with any of them still has order divisible by \(n\). For each such group of \(m\) points choose one as base point \(b\); for every other member \(a\), adjoin an \(n\)-th root of the ratio of their projective linear forms \(\ell_a(w)/\ell_b(w)\). The same finite-class argument puts lifts of all inputs over a single fixed finite extension. If the simultaneous radical equations have several geometric components, take their normalizations and enlarge the field to define all of them.

At a marked inverse image the ramification index of each component over the \(w\)-line is exactly \(n\). At least one ratio has a simple zero or pole there, and the other groups have only units there. Over the algebraic closure in characteristic zero such local units have all their required roots. The ratios from that same group have the same exponent \(n\), so they cannot give a larger local index. There is no other branching. By Riemann–Hurwitz each component \(C\) satisfies
\[
 2g(C)-2=\deg(C\longrightarrow\mathbb P^1_w)
 \left[-2+m\{W-2(1-1/m)\}\right]
 =\deg(C\longrightarrow\mathbb P^1_w)\,m(W-2).
\]
For \(W>2\), Faltings' theorem now gives finitely many points over the fixed field. Each slope gives only one positive primitive pair. For \(W=2\), all these components have genus one.

## What fixed places can contribute on a boundary curve

There are only three possible lists of marked orders at \(W=2\). They are four points of order 2; three points of order 3; and one point of order 2 together with two of order 4. In the first case the forms are two quadratics or both linears and a quadratic. In the second case they are a linear and a quadratic. In the third case the linear has order 2 and the quadratic has order 4. To check this list, every marked point contributes at least \(1/2\). Four points must all have order 2. With three points their reciprocal orders sum to one, yielding \((3,3,3),(2,4,4),(2,3,6)\). The last would require three distinct orders, whereas a selected quadratic contributes two identical orders and there are only two linear forms.

Here are details of the fixed-place estimate. On any component with points over our fixed number field choose one as origin to obtain an elliptic curve \(E\). For a fixed algebraic point \(T\), a fixed place \(v\), and a sequence \(P\in E(K)\) of increasing canonical height, the local logarithmic proximity to \(T\) is \(o(\widehat h(P))\). One can see this by fixing an arbitrary positive integer \(M\) and writing \(P=A+[M]Q\). By the Mordell–Weil theorem only finitely many \(A\) are needed. The map \([M]\) is locally unramified in characteristic zero, and its fiber over \(T-A\) is finite. Near any such preimage \(T'\), closeness of \(Q\) implies at least as much closeness up to a constant of its Weierstrass coordinate to that of \(T'\), using projective distance at infinity. Roth's theorem at \(v\), or ordinary height separation for a target in \(K\), bounds that coordinate proximity by a fixed constant times \(h(x_E(Q))+O_{M,v}(1)\). Equal-coordinate exceptions give only finitely many points. The leading constant can be chosen independently of \(M\). Now \(h(x_E(Q))=2\widehat h(Q)+O(1)\), and for fixed \(M\), \(\widehat h(Q)=(\widehat h(P)+O_M(\sqrt{\widehat h(P)}+1))/M^2\). Letting \(M\) increase proves the assertion. The same argument applies at complex and nonarchimedean places with normalized absolute values.

Apply this estimate to the finite fibers over the ten roots of the forms under the fixed map from \(E\) to the input line. Local orders of this map are bounded by its degree. The height of the image is comparable to \(\widehat h(P)\) at large height by the height theorem for a nonconstant morphism of curves, and here it equals \(\log H\). At the real place this gives \(\log|f_i(s,t)|=d_i\log H+o(\log H)\) for every \(i\). At each fixed rational prime, primitivity normalizes the projective coordinates and gives \(v_p(f_i(s,t))\log p=o(\log H)\), using the linear factorizations over \(K\). Consequently \(\sum_i\log u_i=(10-W)\log H+o(\log H)\), and the repeated factors of \(\prod u_i\) at primes of \(S\) contribute \(o(\log H)\) to its logarithm. The \(u_i\) are coprime in pairs. Multiplication by the fixed coefficients changes the logarithm of the radical by \(O_{\boldsymbol c}(1)\). This proves the formula for \(R\).

## Why the borderline of two is sharp

For **every** \(W=2\) pattern and **every** admissible seed slope, the seed's own power-free parts in its constrained factors occur again at infinitely many other slopes. Here the \(m\)-power-free part retains the exponent of each prime modulo \(m\), as an integer from \(0\) to \(m-1\).

For example, \((s,t)=(1,2)\) gives the signed square classes \((1,2,-7)\) for \((s,t,s^2-2t^2)\). One other pair with the same classes is
\[
 (s,t,s^2-2t^2)=(143^2,\ 2\cdot109^2,\ -7\cdot10079^2).
\]
It comes from the third multiple of \((-7,49)\) on \(V^2=X^3-392X\), by taking the reduced fraction \(s/t=-X/14\).

Use the following homogeneous polynomial \(G\) and exponent \(e\).

| Marked orders | \(G\) | \(e\) |
|---|---|---:|
| \(2,2,2,2\) | product of all marked forms, of total degree four | 2 |
| \(3,3,3\) | \(\ell Q\), with the marked linear and quadratic forms | 3 |
| \(2,4,4\) | \(\ell^2 Q\), with the marked linear and quadratic forms | 4 |

For a seed slope \(x_0=s_0/t_0\) take \(d=G(x_0,1)\). The smooth projective model \(C_d\) of \(d y^e=G(x,1)\) has genus one by the given branch orders and Riemann–Hurwitz. If a linear factor is the second projective coordinate, its root is at infinity and the same orders follow from homogeneity. The seed lifts to \(P_0=(x_0,1)\) in affine coordinates \((x,y)\).

We show below that the Jacobian of every such seed twist has a non-torsion rational point \(T\). Translate \(P_0\) by multiples of \(T\). Infinitely many of these translates approach \(P_0\) in the product of the real place and any prescribed finite set of rational \(p\)-adic places: the corresponding product of local elliptic groups is compact, and a subsequence of positive multiples of \(T\) tends to the identity. Include 2 and all primes dividing the numerator or denominator of \(d\) or the pairwise resultants in this finite set. Outside it, primitivity makes at most one marked form divisible; the equation of the cover forces that valuation to be a multiple of its prescribed order. This follows for normalized homogeneous coordinates because \(\deg G\) is divisible by \(e\). At each included prime, the valuations of the marked forms evaluated on primitive coordinates are locally constant near the seed, since their values there are nonzero. The real and 2-adic conditions also preserve positivity and parity. The resulting slopes have exactly the seed's individual power-free parts, and infinitely many are distinct since the projection has finite fibers.

### Non-torsion in the four-point case

Write \(D=s^2-2t^2,\ Y=s^2+2t^2,\ U_\pm=(s\pm t)^2+t^2\). First suppose a marked quadratic at the seed has a prime divisor \(p\ge5\). The same seed lifts to \(P\) on the fixed double cover \(C_1\) over \(\mathbb Q(\sqrt d)\), with \(\iota\) given by \(y\mapsto-y\). This double cover and its Jacobian have good reduction at \(p\), since the branch points remain distinct and \(p\) is odd. The point reduces to a branch point, hence \(P\) and \(\iota P\) have the same reduction. The nonzero class \([P-\iota P]\) lies in the kernel of reduction of the Jacobian. This kernel is torsion-free: the local ramification index is at most two and \(2<p-1\), so the elliptic formal logarithm is injective on the entire maximal ideal. Untwisting identifies this class with the rational class \([P_0-\iota P_0]\) on the seed twist.

If \(U_+\) or \(U_-\) is marked, such a prime always exists: its value is an odd primitive sum of two squares greater than one, and each prime factor is \(1\bmod4\). If the two marked quadratics are \(D,Y\) and neither had such a prime, then \(Y=3^j>1\) and \(|D|=1\) by coprimality. As \(D\equiv1\bmod8\), one would have \(D=1\) and \(Y=4t^2+1\equiv1\bmod8\). This makes \(j\) even, although \(4t^2+1\) lies strictly between consecutive squares.

It remains to consider both linear forms and one quadratic \(s^2+\nu t^2\) for \(\nu=\pm2\). The covering equation is \(d y^2=x^3+\nu x\); the coordinates \(X=dx,\ V=d^2y\) give \(V^2=X^3+\nu d^2 X\). For any nonzero rational coefficient \(B\), the rational torsion of \(V^2=X^3+BX\) has order dividing four. At every good prime \(p\equiv3\bmod4\) the group has order \(p+1\), by cancellation under \(X\mapsto-X\). Choosing primes \(p\equiv3\bmod8\) bounds the 2-part by four, and for each odd prime \(\ell\) choosing \(p\equiv1\bmod\ell,\ p\equiv3\bmod4\) excludes \(\ell\) by reduction and Dirichlet's theorem. An order-four point must double to \((0,0)\): a different rational 2-torsion point would give a torsion group of order at least eight. The duplication formula thus requires \(X^2=B\). Here \(B=\nu d^2\) cannot be a rational square, and the seed has \(V\ne0\). It has infinite order.

### Non-torsion in the three-point cases

Normalize by the marked linear coordinate \(\ell\), and let \(z\) be the other coordinate divided by \(\ell\). The marked quadratic divided by \(\ell^2\) is \(q(z)=a z^2+bz+c\). The covering equation becomes \(d y^e=q(z)\), with \(d=q(z_0)\ne0\) for the seed \(z_0\), which gives the same twist after scaling \(y\). Set \(\Delta=b^2-4ac\), \(A=4ad\), and \(u=2az+b\). Then \(u^2=A y^e+\Delta\), with \(\Delta\in\{8,-8,-4\}\). At a positive admissible seed \(u_0\ne0\). The only positive vertices of the possible quadratics occur for \(U_-\) at \(s/t=1\) or \(t/s=1/2\), both excluded by parity and primitivity.

For \(e=3\) the coordinates \(X=A y,\ V=A u\) identify the curve with \(V^2=X^3+A^2\Delta\). Its rational torsion has order dividing six. At good primes \(p\equiv2\bmod3\) its group has order \(p+1\) since cubing permutes the residue field. Taking \(p\equiv5\bmod12\) bounds the 2-part by two, taking \(p\equiv2\bmod9\) bounds the 3-part by three, and choosing \(p\equiv1\bmod\ell,\ p\equiv2\bmod3\) excludes each prime \(\ell>3\). A point of order three on \(V^2=X^3+B\) satisfies \(3X(X^3+4B)=0\) by the division polynomial. Its existence would make \(B\) or \(-3B\) a square. Neither \(\Delta\) nor \(-3\Delta\) is a rational square. Thus the seed \((A,A u_0)\), with nonzero second coordinate, has infinite order.

For \(e=4\) there is a nonconstant map to \(V^2=X^3+A\Delta X\) given by \(X=A y^2,\ V=Ayu\). The seed maps to \((A,Au_0)\), and \(y\mapsto-y\) maps to its elliptic inverse. By the order-four test above, finite order would require \(A^2=A\Delta\), hence \(u_0^2=A+\Delta=2\Delta\). This is possible only when \(\Delta=8\), for the form \(s^2-2t^2\). In the two choices of coordinate it forces \(s/t=2\) or \(t/s=1\), both impossible for our primitive parities. The image has infinite order. The rational divisor class of the difference of the seed and its image under \(y\mapsto-y\) maps on Jacobians to twice that infinite-order point, so it too has infinite order. This completes all boundary cases. The argument controls recurrence of the fixed-power parts; a fixed-exponent abc violation would still require additional prime repetitions.

## A counterexample test with varying multiplicities

Let \(U_\pm=(s\pm t)^2+t^2\). Suppose that every prime in one of \(U_+,U_-\) occurs to exponent at least two, and every prime in the other occurs to exponent at least three. Then their radicals are at most \(O(H)\) and \(O(H^{2/3})\), respectively. The remaining four radicals have product \(O(H^6)\). Thus \(R\ll H^{23/3}\), and infinitely many such pairs would disprove rational abc by the octic equivalence. This test permits the exponents at distinct primes of one factor to be, for example, 2 and 3. Finiteness for a fixed square times a fixed coefficient and a cube times a fixed coefficient cannot cover all these possibilities.

An exhaustive search through \(H=100{,}000{,}000\) found 129,087 orientations for which every prime in the designated one of \(U_\pm\) has exponent at least three. None had every prime in the other factor occurring at least twice. To enumerate them, \((s\pm t)+it\) is coprime to its conjugate in the Gaussian integers. Every prime in its odd norm is \(1\bmod 4\), and for a prime of exponent \(e\) its entire contribution is either \(\pi^e\) or \(\bar\pi^e\) up to a unit. Enumerate all these products of norm at most \(5H^2\) with \(e\ge3\). Use the absolute even coordinate as \(t\), then test all choices of \(s\) from the absolute odd coordinate \(|s\pm t|\). Simultaneous conjugation duplicates the same inputs. For the other norm, trial division removes small split primes with rejection at exponent one. Once the next possible prime cubed exceeds the remainder, a surviving remainder with every valuation at least two is either one or a square. A direct double loop and trial factorization at \(H=128\) independently verified the enumeration and both orientation counts there. The finite search places no constraint on larger inputs. [Reproducible search](abc_octic_powerful_pairs.py)
