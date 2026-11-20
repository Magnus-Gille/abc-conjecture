# Growth of the squarefree part in each of the four coordinates

Let \(G=(-3,9)\) on \(E:Y^2=X^3-36X\), and take positive odd indices \(n\). The [elliptic parametrization](abc_full_quartic_signature.md) gives pairwise coprime positive odd integers \(a_n,c_n,d_n,w_n\), with
\[
 a_n^2+c_n^2=2w_n^2,\qquad a_n^2+2w_n^2=3d_n^2,\qquad b_n=c_nd_n.
\]
We take the positive sign of \(b_n\). Let \(s(F)=\prod_{v_p(F)\ {m odd}}p\). There are absolute constants \(c>0\) and \(A>1\) with the following properties.

* For all sufficiently large positive odd \(n\), **each** \(F_n\in\{a_n,c_n,d_n,w_n\}\) satisfies \(\log s(F_n)\ge c\log\log n\,\log\log\log n\).
* For each of the four choices of coordinate and every squarefree integer \(D\ge1\), at most \(A^{1+\omega(D)}\) positive odd indices satisfy \(s(F_n)=D\). In particular amongst all positive odd indices, the count with \(\min_F s(F_n)\le Y\) is at most \(Y^{1+O(1/\log\log Y)}\) as \(Y\to\infty\). For \(0<\delta<1\), at most \(N^{1-\delta+o(1)}\) odd indices \(n\le N\) satisfy \(\min_F s(F_n)\le n^{1-\delta}\).

The constants are not numerically evaluated. The proof extends the [ordered-divisor argument for the denominator](abc_congruent_six_pointwise_cofactor_growth.md) to the two numerators and the other denominator. No abc estimate is assumed.

## A quadratic twist of a plane quartic for each coordinate

Write \(F=Dz^2\). The following four algebraic integers, in the indicated rings of integers, have the listed real parts and norms. The second identity used in the last two rows is \(c^4+8(aw)^2=9d^4\).

| Coordinate \(F\) | Quadratic field | Algebraic integer \(\alpha\) | \(\operatorname{Re}\alpha\) | \(N\alpha\) |
|---|---|---|---|---|
| \(a\) | \(\mathbf Q(\sqrt{-3})\) | \((a^2+b\sqrt{-3})/2\) | \(a^2/2\) | \(w^4\) |
| \(w\) | \(\mathbf Q(\sqrt3)\) | \(2w^2+b\sqrt3\) | \(2w^2\) | \(a^4\) |
| \(c\) | \(\mathbf Q(\sqrt{-2})\) | \(c^2+2aw\sqrt{-2}\) | \(c^2\) | \(9d^4\) |
| \(d\) | \(\mathbf Q(\sqrt2)\) | \(3d^2+2aw\sqrt2\) | \(3d^2\) | \(c^4\) |

Here \(\operatorname{Re}\alpha\) means half the field trace, including in the real quadratic fields. All four rings have class number one by the quadratic Minkowski bound. In each row the ideals of \(\alpha\) and its conjugate are coprime. A prime ideal common to both must divide their trace as well as their norm. In the first two rows coprimality of \(a,w\) and their oddness suffice. In the third row \((c,3d)=1\). In the last row \((c,6d)=1\).

Therefore \(\alpha=\eta\beta^4\), with \(\beta\) an algebraic integer and \(\eta\) taken from a fixed finite set. For norms that are fourth powers the only multipliers required are representatives of the units modulo fourth powers. For the third row 3 splits as \((1+\sqrt{-2})(1-\sqrt{-2})\), and exactly one prime above 3 occurs in \(\alpha\), to exponent 2 modulo 4. Include its generator squared in \(\eta\). This also covers the case \(3\mid d\). The norm of \(\eta\) is 1 in the first, second and fourth rows and is 9 in the third.

Choose a rational basis of the quadratic field and write \(\beta=U+V\sqrt m\), allowing rational halves in the Eisenstein row. Taking the real part gives a plane quartic
\[
                 c_0D^2 Z^4=f_\eta(U,V),\qquad
 f_\eta=\tfrac12\big(\eta(U+V\sqrt m)^4+\bar\eta(U-V\sqrt m)^4\big),
\]
where \(Z=z\), and \(c_0=1/2,2,1,3\) in the respective rows. The two linear forms are independent, and their fourth powers have nonzero coefficients. Thus the binary quartic has four distinct roots over \(\overline{\mathbf Q}\), and the plane quartic is smooth of genus three. For a given row and \(\eta\), these curves are quadratic twists of the fixed \(D=1\) curve under \(Z\mapsto -Z\).

At rational points arising from the parametrization, the projective coordinates recover \(F=DZ^2\) and the paired coordinate \(|N\beta|=|U^2-mV^2|\) up to the same scaling. These paired coordinates are \(w,a,d,c\) in order. Hence one recovers \(a/w\) or \(c/d\). The latter determines \((a/w)^2=2(3-(c/d)^2)/(3+(c/d)^2)\). Since \(X(nG)=-3(a/w)^2\) and \(G\) has infinite order, distinct positive indices cannot yield the same projective point for a fixed row and multiplier.

## Rank and uniform multiplicity

For each of the finitely many base quartics, its Jacobian is isogenous over \(\mathbf Q\) to the product of the images of \(1+\tau\) and \(1-\tau\), where \(\tau\) is the involution \(Z\mapsto-Z\). Indeed their sum is multiplication by 2, and their intersection is killed by 2. The first factor is fixed on twisting, while the second is an abelian variety \(P\) quadratically twisted by \([-1]\). Its rank over \(\mathbf Q\) is \(O(1+\omega(D))\). To see this, pass to the fixed number field \(K=\mathbf Q(P[2])\). Since \([-1]\) fixes every point of order 2, all twists have the same rational two-torsion over \(K\). The Kummer map at 2 places their points modulo doubles in \((K^\times/K^{\times2})^{2\dim P}\). Its squareclasses are unramified outside the primes over \(2D\) and those of bad reduction of the fixed variety. At a good place of odd residue characteristic, multiplication by 2 on the abelian scheme is finite étale, yielding this local unramifiedness. The squareclasses unramified outside this set have dimension at most a constant plus its cardinality, by the ideal class group and the unit theorem for \(K\). This bounds the rank as claimed.

The uniform Mordell–Lang bound for curves now gives at most \(A_0^{1+\omega(D)}\) rational points on each twist, with an absolute constant after taking the finite maximum. Summing the finite choices of multiplier proves the stated multiplicity. If \(D\le Y\), then \(\omega(D)=O(\log Y/\log\log Y)\) by the factorial bound on a product of distinct primes. Summing over \(D\) and the four rows gives the count for variable \(D\). [Dimitrov, Gao and Habegger, *Uniformity in Mordell–Lang for curves*](https://arxiv.org/abs/2001.10276)

## The lower bound at every index

Put \(D_n^*=\prod_{p>3,\ v_p(F_n)\ {\rm odd}}p\). Specifying \(D_n^*=D\) allows at most the two full squarefree parts \(D,3D\), so the same multiplicity bound holds after enlarging \(A\). In the four rows \(F_n\) is the denominator root of \(nH\), where \(H=G+T\) is integral, \(T\) is a rational two-torsion point or the identity, and \(n\) is odd. For \(p>3\) contributing at an odd index, \(r=\mathrm{ord}(H\bmod p)\) divides that index and is greater than one. The full two-torsion and the order-\(r\) subgroup give \(p\ge(2\sqrt r-1)^2>2r\). When \(r\mid m\), the formal group gives \(v_p(F_{m j})=v_p(F_m)+v_p(j)\) for odd \(m,j\). [The four denominator identities](abc_full_quartic_signature.md)

Order the prime factors of \(n\), with multiplicity, as \(q_1\ge\cdots\ge q_t\), and put \(m_j=q_1\cdots q_j\), including \(m_0=1\). If \(p\mid D_{m_j}^*\), then \(r\mid m_j\), so \(r\ge q_j\). Every later multiplier has prime divisors smaller than \(p\). Thus \(D_{m_0}^*\mid\cdots\mid D_{m_t}^*\). With \(D=D_n^*\), at most \(1+\omega(D)\) distinct values can occur, each at most \(A^{1+\omega(D)}\) times. This gives \(t+1\le(1+\omega(D))A^{1+\omega(D)}\).

Only finitely many prime indices \(q\) have \(D_q^*=1\), by the multiplicity bound. If the largest index prime \(q_1\) exceeds every one of them, some \(p>2q_1\) divides \(D_{q_1}^*\) and survives in \(D\). Thus \(\log n\le t\log\max(D,C)\) with a fixed constant \(C\). As \(n\to\infty\), these inequalities force \(D\to\infty\). If \(\log D\ge(\log\log n)^2\) the lower bound follows immediately. In the other case taking logarithms in the last two estimates gives \(\omega(D)\gg\log\log n\). Since \(D\ge(1+\omega(D))!\), we obtain \(\log D\gg\log\log n\,\log\log\log n\). Taking the minimum of the constants for the four coordinates proves simultaneity.

For the abc application one needs to compare \(\log s(F_n)\) with \(\log F_n\asymp n^2\). The estimates here leave open whether a coordinate can satisfy \(s(F_n)\le\sqrt{F_n}\) infinitely often. Such a sequence would contradict rational abc. [Exact connection to abc quality](abc_full_quartic_twin_and_mixed_valuations.md)
