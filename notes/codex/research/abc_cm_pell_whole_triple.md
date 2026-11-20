# A moving repeated prime in the full radical of a primitive abc triple

There is a fixed rational-function family of positive primitive triples \(A+B=C\) and an infinite set of distinct primes \(p\) with the following property. For each sufficiently large prime in this set there is a member of the family satisfying
\[
 p^2\parallel F_{11}(a,b),\qquad p^{16}\parallel C,\qquad
 \frac{C}{\operatorname{rad}(ABC)}\gg\frac{p}{(\log p)^2},
 \qquad \log C\ll p^2\log\log p .
\]
Here \(F_{11}\) records precisely the full complex-multiplication abscissas at rank 11 on the [quadratic twist family](abc_cm_twist_sharp_depth.md). The constants are absolute for this fixed construction. The bound on the complete triple uses just this one repeated prime and the radical of a controlled quadratic norm. It gives unbounded height-to-radical ratios, and thus infinitely many triples of quality greater than one. It does not establish a fixed positive lower bound on the quality minus one.

## Explicit triple and its radical

For coprime integers \(a,b\), set
\[
 H_0=\max(|a|,|b|),\ S=b^2+2a^2,\ H=S+2ab,\ J=b^2-2a^2,\ D=SH.
\]
On the twist \(Y^2=X^3+16DX^2+32D^2X\) take \(P=(-8H^2,16H^2J)\). Write the reduced fraction \(U/V=X([11]P)/D\), \(V>0\). The positive entries before dividing by their common gcd are
\[
 (U^2+16UV+32V^2)^2,\qquad
 -U(U+16V)(U+8V)^2,\qquad
 1024 V^4.
\]
The first two sum to the third by expansion. The gcd divides 1024 as \(U,V\) are coprime. On the untwisted curve \(y^2=x^3+16x^2+32x\), the point of initial abscissa \(t=-8H/S\) is on the bounded real component, which odd multiplication preserves. In particular \(U/V\) lies strictly between \(-8-4\sqrt2\) and \(-8+4\sqrt2\). Possible zero entries can be discarded as finitely many specializations of a nonconstant map; all constructions below give heights tending to infinity.

Let \(h(z)=z^2+16z+32\) and \(\beta(z)=(h(z)/32)^2\). The ratio of the first to the last entry is the composition of \(t\), the abscissa map for multiplication by 11, and \(\beta\). Its degree is \(2\cdot121\cdot4=968\). All branch values of the composite lie in \(0,1,\infty\). Indeed \(t\) branches over the roots of \(h\); these are two-torsion abscissas fixed by odd multiplication. The branch values of the abscissa multiplication map are contained in the four two-torsion abscissas, including infinity, since multiplication is étale on the elliptic curve. The polynomial \(\beta\) sends these to \(0,1,\infty\), and its own critical values also belong to this set. Consequently Riemann–Hurwitz gives exactly \(968+2=970\) distinct geometric points in the three fibers. The primitive largest entry \(C\) is comparable to \(H_0^{968}\), by the ordinary height formula for a fixed map of projective lines.

The primitive homogeneous form \(F_{11}\), of degree 100, occurs in the squarefree product of those three fibers: its roots map to infinity under multiplication by 11. Also \(J\) is a squarefree degree-two factor. Its roots map to the roots of \(h(t)\), and thence to zero. The two factors are disjoint since the torsion orders are 11 and 2. The residual squarefree product has degree 868. Each prime of the triple belongs to this geometric support up to finitely many fixed coefficient primes. Bounding the residual form by \(O(H_0^{868})\) gives
\[
 \operatorname{rad}(ABC)\ll H_0^{868}\operatorname{rad}|F_{11}(a,b)|
                                      \operatorname{rad}|J|.
\]
The degree-100 form has no real projective zero, hence \(|F_{11}(a,b)|\asymp H_0^{100}\). Therefore, uniformly on nondegenerate triples,
\[
 \frac C{\operatorname{rad}(ABC)}
    \gg\frac{|F_{11}(a,b)|}
             {\operatorname{rad}|F_{11}(a,b)|\,\operatorname{rad}|J|}.       \tag{1}
\]
At good full primes \(p>11\) with \(e=v_p(F_{11})\), one has \(v_p(V)=2e\) by the abscissa formula, and \(v_p(C)=8e\). The extra eightfold multiplicity is ramification of the fixed map. Its contribution has already been accounted for in the support degree; the new gain from this prime in (1) is \(p^{e-1}\).

## Moving the repeated prime

Write \(\epsilon=1+\sqrt2\), \(b_n+a_n\sqrt2=\epsilon^n\). Then \(J=(-1)^n\), and the pairs are primitive. There are infinitely many primes \(p\) dividing at least one \(F_{11}(a_n,b_n)\). Otherwise take a modulus \(M\) supported on all such primes, containing each to a power strictly above its valuation in \(F_{11}(0,1)\ne0\). Take \(n\) through multiples of the order of \(\epsilon\bmod M\), a unit. Every value would have exactly its seed valuations at all possible primes, whereas its absolute value grows exponentially with \(n\). Discard the finitely many bad primes of the form and curve. At each remaining \(p\) the seed is a simple projective root with unit quadratic norm, with \(0\le n\le p+1\) selectable by projective periodicity.

In \(\mathbb Z[\sqrt2]\), take \(\eta=\epsilon\) if its projective order increases from \(p\) to \(p^2\). Otherwise there is a generator \(\eta\) of a prime of norm \(\ell\ll(\log p)^2\) with this same order increase. The elementary counting proof uses products of small prime generators balanced in the two real embeddings. More than \(p+1\) such products of height \(O(p)\) can be distinguished already modulo \(p^2\), while the projective elements with no order increase number at most \(p+1\). The generator can be taken balanced as well. [Small-generator and lifting proofs](abc_pell_projective_generator.md)

Let \(m\le p+1\) be the projective order of \(\eta\bmod p\). In the projective unit group modulo \(p^3\), \(\eta^m\) generates the kernel of reduction to \(p\), of order \(p^2\). Multiplication acts transitively on the lifts of the seed projective point because its quadratic norm is a unit. As \(j\) varies, exactly one class modulo \(p\) makes \(F_{11}\) at \(\epsilon^n\eta^{mj}\) vanish modulo \(p^2\). Among two representatives \(j_0,j_0+p\), \(0\le j_0<p\), at most one lifts to a zero modulo \(p^3\), since the parameter root is simple. Choose the other. The coefficients of this quadratic integer are coprime: outside the unit factor, the principal ideal is supported at a single place over a split prime, so no rational prime divides the element. Its norm \(J\) is \(\pm1\) or \(\pm\ell^{mj}\), giving \(\operatorname{rad}|J|\ll(\log p)^2\). Also \(\log H_0\ll p^2\log\log p\) by the archimedean bound on the generator. Formula (1) proves the claimed theorem. Since any fixed form value has finitely many prime divisors, the heights grow unboundedly as the marked primes change.

At the same infinite set one may prescribe any depth \(e\ge2\). Take two representatives separated by \(p^{e-1}\) after solving modulo \(p^e\). This gives
\[
 \frac C{\operatorname{rad}(ABC)}\gg \frac{p^{e-1}}{(\log p)^2},
 \qquad \log C\ll p^e\log\log p.
\]
For any fixed positive function \(\omega(x)\to\infty\), one can choose successive, distinct \(p\), and then \(e\) sufficiently large, to get a gain \(\gg\log C/\omega(\log C)\) from the marked prime and the norm estimate. Indeed \(\log C\gg e\log p-O(1)\) follows from \(p^e\mid F_{11}\). Choose \(e\) so that \(\omega(\log C)\ge p(\log p)^2\log\log p\) throughout the resulting height range and combine the two displayed bounds.

There is a further version for **every** sufficiently large \(p\) at which \(F_{11}\) has a projective root modulo \(p\). Such roots have unit norm \(J\), apart from finitely many primes by the resultant. A determinant-\(p\) lattice supplies an initial rational representative of height \(O(\sqrt p)\), hence norm \(O(p)\). Its primitive reduction preserves the projective class. The same lift bounds the norm radical by \(O(p(\log p)^2)\), and the whole gain is \(\gg p^{e-2}/(\log p)^2\). In particular depth three suffices for an unbounded gain on this entire set. These primes have positive density since primes splitting completely in the splitting field of \(F_{11}\) away from the discriminant are included.

## Keeping previously marked squares

There exist distinct increasing primes \(p_1,p_2,\ldots\) and a sequence of triples in this same family such that at stage \(j\) every \(p_i\), \(i\le j\), occurs to exact exponent two in the full form and exact exponent sixteen in \(C\). The entire radical satisfies
\[
 \frac C{\operatorname{rad}(ABC)}
     \gg \prod_{i\le j}\frac{p_i}{100(\log p_i)^2}.
\]
Start with the parameter element \(1\) and an empty list. Given the current primitive element \(\alpha\), let \(M\) be a multiple of all the orders of the projective unit groups modulo \(p_i^3\). The elements \(\alpha\epsilon^{Mt}\) preserve all marked valuations and the norm radical. Infinitely many new primes occur in their form values: the finite-modulus contradiction above applies with seed \(\alpha\), since \(F_{11}(\alpha)\ne0\) and the heights tend to infinity. Choose a new prime \(p\) not dividing \(M\) or the norm of \(\alpha\). Apply the small-generator proof omitting the earlier marked primes from the allowed auxiliary primes; deleting any fixed finite list does not change its prime-counting asymptotic. The new \(p\) can be taken beyond its threshold for this omission. Multiplying the new starting element by \((\eta^{mM})^s\) now preserves the earlier projective classes and runs through all principal lifts at \(p\), since \(M\) is a \(p\)-unit. Take a lift of exact depth two. Removing any coordinate gcd preserves all marked valuations because the norm is a unit at every marked prime. The radical of the new norm increases by at most \(100(\log p)^2\). Induction and (1) give the claim. This argument does not control the combined height by a power of the product of the marked primes.

## A single prime on the Pell sequence

At \(p=683\), the auxiliary generator can be the Pell unit itself. One computes
\[
 \epsilon^{228}\equiv -1+59p\sqrt2\pmod{p^2},\qquad
 v_p(F_{11}(a_{73},b_{73}))=1,\quad v_p(F_{11}(a_{1213},b_{1213}))=2 .
\]
The displayed congruence supplies a nonzero projective tangent at every lift. Thus for each \(e\ge2\) there is a Pell index \(n_e=O(p^e)\) of exact full depth \(e\). Since \(J=\pm1\) and \(\log C\asymp n_e\), the resulting triples have \(C/\operatorname{rad}(ABC)\gg \log C\). This conclusion applies to the very same degree-968 map and requires no change of its coefficients.

For comparison, a disproof would follow if some fixed \(\delta>0\) gave \(\log(|F_{11}(a_n,b_n)|/\operatorname{rad}|F_{11}(a_n,b_n)|)\ge\delta n\) infinitely often on the Pell orbit. A single \(p^2\mid F_{11}(a_n,b_n)\) with \(\log p\ge\delta n\) would suffice. This follows directly from (1), \(J=\pm1\), and \(\log C\asymp n\). Neither the lifting construction nor the finite example establishes this growth.

## An exact numerical certificate

At \(a/b=-6437/73\) the primitive triple has 3931 decimal digits in \(C\), satisfies \(683^{16}\parallel C\), and
\[
       \frac C{\operatorname{rad}(ABC)}\ge295.2658019718.
\]
Indeed write \(-U=163870930\,L^2,\ V=9208363\,M^2,\ -(U^2+16UV+32V^2)=2W^2\), using positive integer square roots. All primes of \(ABC\) divide
\[
 T=2\cdot163870930\cdot9208363\,LMW\,|U+8V|\,|U+16V|.
\]
Its valuations at \(2,199,683,9103\) are \(12,2,2,2\), respectively. Hence \(\operatorname{rad}(ABC)\le T/(2^{11}\cdot199\cdot683\cdot9103)\). The [exact verifier](abc_cm_pell_whole_triple.py) checks the common gcd, integer square roots, four valuations and displayed lower bound by integer division. It independently evaluates the degree-50 full abscissa factor at the parameter, obtaining \(316\cdot683^2\bmod683^3\).
