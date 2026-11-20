# Counting pairs with a squareful and a cubeful quadratic factor

Let \(s,t>0\) be coprime, \(s\) odd and \(t\) even, and set
\[
 D=s^2-2t^2,\qquad Y=s^2+2t^2,\qquad U_\pm=(s\pm t)^2+t^2 .
\]
Choose **any two distinct forms in order**. Require every prime divisor of the absolute value of the first to have exponent at least three, and every prime divisor of the second to have exponent at least two. The absolute value 1 meets either convention. For each \(\delta>0\), the number of such pairs with \(\max(s,t)\le H\) is
\[
 O_\delta(H^{3/5+\delta}).
\]
This also bounds the union of all twelve choices. A search through \(10^9\) found two pairs. The example \((7,4)\) gives \(Y=81=3^4,\ U_-=25=5^2\). The other, \((17,12)\), gives \(D=1,\ U_-=169=13^2\). The count theorem allows an infinite sequence; any such sequence would disprove rational abc, since the radical of the octic triple would be \(O(H^{23/3})\) at its actual parameter height. [Transfer to abc](abc_rational_pell_transfer.md) · [Fixed-power finiteness](abc_octic_power_patterns.md) · [Census program](abc_octic_norm_census.cpp)

At \((7,4)\) the abc triple and its radical are \(9{,}834{,}496+1{,}896{,}129=11{,}730{,}625\) and \(489{,}090\). The search enumerates primitive cubeful norms using wholly oriented powers of split prime ideals. In the real ring it enumerates the positive unit orbits in the box, including the orbit of norm one. The cubeful occurrence counts through \(10^9\) were \(508{,}312\) for \(|D|\), \(312{,}647\) for \(Y\), \(407{,}463\) for \(U_-\), and \(195{,}508\) for \(U_+\). An independent enumeration in the full box through \(2048\) used the integer descriptions \(a^3b^4c^5\) for cubeful numbers and \(a^2b^3\) for squareful numbers. It gave the same four counts there, \(74,48,55,27\), and the same two matches. A separate build with an undefined-behavior sanitizer reproduced the full \(10^9\) run. The numerical data establish no upper bound on the height of a possible third pair.

## Writing the norm elements as products of powers

Each form is the norm of an element \(G\) in \(\mathbb Z[\sqrt2],\mathbb Z[\sqrt{-2}]\) or \(\mathbb Z[i]\), with coordinates related to \((s,t)\) by an integral change of determinant \(\pm1\). Each ring is norm-Euclidean. The norm is odd. A common prime ideal divisor of \(G\) and its conjugate would thus divide both coordinates at an odd rational prime, impossible by primitivity. In particular every prime divisor of the norm splits, and its full exponent occurs in only one of the two conjugate prime ideals.

Write \(\|x\|\) for the maximum of the absolute values at the two complex embeddings. In each ring it is comparable to the maximum absolute value of the two integral coordinates. In the real quadratic ring any nonzero principal ideal has a generator with both absolute values comparable to the square root of its absolute norm: multiply a generator by an appropriate power of \(1+\sqrt2\). We call such a choice balanced. In the other rings equality holds for both absolute values.

For the element of cubeful norm we may therefore write \(G_1=\alpha z^3\), where \(\alpha=\xi b^4 c^5\) and \(\xi\) lies in a fixed finite list of units. Indeed every exponent at least three is \(3k,\ 4+3k\), or \(5+3k\). Take balanced generators \(b,c\) for the corresponding two products of prime ideals and absorb all but a unit modulo cubes into \(z\). For \(A=\|\alpha\|\) we have
\[
 \|z\|\ll (H/A)^{1/3},\qquad
 \#\{(\xi,b,c): A\le L\}\ll L^{1/2}\quad(L\ge1).
\]
To prove the second inequality, \(\|\alpha\|\asymp\|b\|^4\|c\|^5\) by the choice of generators. A disk or coordinate box of radius \(T\ge1\) in a fixed rank-two lattice contains \(O(T^2)\) elements. Summing \(O(L^{1/2}\|c\|^{-5/2})\) over \(c\ne0\) proves the claim.

For the element of squareful norm write \(G_2=\xi' w^2 v^3\), separating the odd exponents, all of which are at least three. Take \(v\) balanced, with squarefree absolute norm \(d\), and \(\xi'\) from a fixed list of units modulo squares. Then
\[
 \|v\|\asymp\sqrt d,\qquad \|w\|^2\|v\|^3\ll H .
\]
The latter uses balancing only for \(v\); the element \(w\) can be unbalanced. Primitivity gives primitive lattice coordinates for all of \(z,w,v\). For counting, a rational slope determines primitive lattice coordinates up to sign. These properties hold even when a norm is negative or a unit.

## Three bounds with the parameters separated

The contribution of \(A>H^{2/5}\) is \(O(H^{3/5})\). In a dyadic range \(A\asymp L\), count all \(z\) to get \(O(H^{2/3}L^{-1/6})\) using the preceding estimates. Sum the geometric series. In the rest of the proof there are \(O(H^{1/5})\) choices of \(\alpha\), counted with their representations.

For later use, fixing a nonzero \(\gamma\) and sending the projective coordinates of a field element \(a\) to the slope of \(\gamma a^m\) is a degree-\(m\) rational map. Here the target is expressed in the common input coordinates \((s:t)\). Over the algebraic closure the map is conjugate in source and target to taking the \(m\)-th power: use the ratio of the two embeddings of \(a\). Its only branch values on the target are the two roots of the associated quadratic form. The two chosen forms have disjoint sets of roots. Consequently the fiber product of their two maps is smooth and geometrically irreducible. At each target point at least one map is unramified, giving smoothness. For irreducibility, both maps are geometrically cyclic Galois covers, and their common subextension would be unramified everywhere on the projective line, hence trivial. The fiber product in the product of the two projective lines has Segre degree equal to the sum of the map degrees.

**Small \(d\).** If \(d\le H^{1/20}\), fix \(v,\xi'\), giving \(O(H^{1/20})\) choices. The slopes of \(z,w\) lie on the fiber product of maps of degrees three and two. Its Segre degree is five; its rational points of interest have projective height \(O(H^{1/3+1/2})\) under this embedding. The uniform determinant bound for a geometrically integral projective curve of degree five is \(O(B^{2/5})\) at height \(B\), independently of its coefficients. Thus this range contributes \(O(H^{1/5+1/20+1/3})=O(H^{7/12})\). [Walsh, *Bounded rational points on curves*](https://arxiv.org/abs/1308.0574)

**Middle \(d\).** Suppose \(H^{1/20}<d\le H^{2/5}\). Since \(d^3\) divides the second norm, the projective coordinates of \(z\) satisfy one of \(O_\delta(d^\delta)\) residue conditions modulo \(d^3\), for each fixed \(\alpha,d\). Indeed each odd \(p\mid d\) is coprime to \(N(\alpha)\) because the two original form values are coprime. For \(p\ne3\) the power map of degree three has good separable reduction. The two distinct target roots of the second form remain disjoint from the branch values, since all four quadratic forms have pairwise disjoint, simple projective roots in every odd characteristic. Their inverse images give at most six simple projective classes modulo \(p\), each lifting uniquely modulo \(p^3\). At \(p=3\) one can use all 36 classes of \(\mathbb P^1(\mathbb Z/27)\), a fixed factor since \(d\) is squarefree. The Chinese remainder theorem gives the bound.

A fixed class modulo \(d^3\) contains \(O(1+Z^2/d^3)\) primitive pairs of coordinate height at most \(Z\), up to sign. Use two charts with bounded real slope. Two distinct slopes in a chart differ by at least \(d^3/Z^2\) by divisibility of their determinant. Use \(Z\ll(H/A)^{1/3}\) and sum over \(d\). The contributions of the unit term sum to \(O_\delta(H^{1/5+2/5+\delta})\). The remaining contributions sum to \(O_\delta(H^{2/3-1/10+\delta})\), since \(\sum_\alpha A^{-2/3}<\infty\) and \(\sum_{d>H^{1/20}}d^{-3}\ll H^{-1/10}\).

**Large \(d\).** Now \(d>H^{2/5}\), hence \(\|w\|\ll H^{1/5}\). Fix \(\alpha,\xi',w\), giving \(O(H^{1/5+2/5})\) choices. Both maps, with free variables \(z,v\), have degree three. Each fiber product has genus four by Riemann–Hurwitz: its degree-nine map to the target is branched at four points, each of index three. For these particular twists the number of rational points on each curve is \(O_\delta(H^\delta)\), as proved below. This completes the count.

## Why the genus-four estimate is uniform

Fix the ordered pair of forms. Over a fixed number field their norm coordinates split and the cube roots of unity are present. In these coordinates a fixed reference fiber product \(C_0\) is obtained by taking both scalar coefficients to be one. The actual equations for the two cubes differ from the reference ones by multiplication by \(\alpha/\bar\alpha\) and by \((\xi'w^2)/\overline{\xi'w^2}\), respectively. Thus adjoining cube roots of these two constants identifies the curve with \(C_0\). Enlarge the fixed ground field \(K\) once to contain all the 3-torsion of \(J_0=\operatorname{Jac}(C_0)\). Put \(n=|N(\alpha)N(w)|\), taking each norm in its own quadratic field. The needed extension \(L/K\) is Galois of degree dividing nine, with Galois group a 3-group. It is unramified outside a set \(S\) containing a fixed finite set of places and the primes above the rational divisors of \(n\). Include all primes over 3 and of bad reduction of \(J_0\) in the fixed set. The variable Jacobian has good reduction over \(K\) away from \(S\), for example by the unramified isomorphism after descent and the good-reduction criterion.

On the variable Jacobian \(J\), the action on \(J[3]\) factors over \(K\) through this 3-group. As a representation in characteristic three, \(J[3]\) therefore has a filtration with trivial one-dimensional quotients. The Kummer map injects \(J(K)/3J(K)\) into \(H^1(G_{K,S},J[3])\), where \(G_{K,S}\) is the Galois group outside \(S\). Division by three of an integral point on an abelian scheme of good reduction gives a finite étale torsor away from 3, so its Kummer class is unramified there. By the filtration and the long exact sequence, the dimension of this cohomology is at most eight times \(\dim H^1(G_{K,S},\mathbb F_3)\). Since \(K\) contains the cube roots of unity, ordinary Kummer theory bounds the latter by \(O_K(1+|S|)\) using the units outside \(S\) and the fixed field's class group. Thus
\[
 \operatorname{rank}J(\mathbb Q)\le\operatorname{rank}J(K)
 \ll 1+\omega(n).
\]
The integer \(n\) is nonzero and \(O(H^C)\) for an absolute constant \(C\), so its number of distinct primes is \(O(\log H/\log\log H)\) at large \(H\). The uniform Mordell–Lang bound for curves gives at most \(c(4,1)^{1+\operatorname{rank}J(\mathbb Q)}\) rational points. This is \(O_\delta(H^\delta)\) for every fixed \(\delta>0\), as claimed. This use of the theorem bounds the number of points per twist; the infinitely many possible twists are the reason a power of \(H\) remains in the answer. [Dimitrov, Gao and Habegger, *Uniformity in Mordell–Lang for curves*](https://arxiv.org/abs/2001.10276)
