# Three close triples with a common radical, and a limit on rational identities

There are infinitely many groups of three distinct primitive positive abc triples with exactly the same radical \(R\). Their largest terms \(C_1<C_2<C_3\) can simultaneously satisfy
\[
 (C_3-C_1)/C_1\le e^{-k\sqrt{\log C_1}},\qquad
 C_1/R\ge \exp\!\big(k\sqrt{\log C_1}/\log\log C_1\big)
\]
for an absolute \(k>0\). Further, for any fixed \(\delta>0\), rational abc is equivalent to its restriction to groups of three distinct triples with a common radical and \(C_3/C_1<1+\delta\). The sufficient exponent for an infinite counterexample family changes under the transfer.

## The three identities

Take coprime \(x>y>0\) of opposite parity. The triples are
\[
\begin{aligned}
 y^4+(x^4-y^4)&=x^4,\\
 (x^2-y^2)^2+4x^2y^2&=(x^2+y^2)^2,\\
 (x-y)^4+8xy(x^2+y^2)&=(x+y)^4 .
\end{aligned}
\]
Primitivity follows from \(\gcd(x,y)=1\), opposite parity, and \(\gcd(x-y,x+y)=1\). Factoring each product of three terms gives the same radical \(\operatorname{rad}(xy(x-y)(x+y)(x^2+y^2))\). The ratio of the extreme heights is \((1+y/x)^4\). The input \((x,y)=(2,1)\) yields \(1+15=16,\ 9+16=25,\ 1+80=81\), all with radical 30.

For the unconditional bounds, use the [smooth-integer construction](abc_pairs_same_radical.md), omitting the prime 2. Choose two close odd products \(P>Q\), write \(d=\gcd(P,Q)\), and take \(x=Q/d,\ y=(P-Q)/d\). They are coprime and of opposite parity. With \(c=x+y,\ R_0=\operatorname{rad}(xyc)\), the same pigeonhole bounds yield
\[
 y/x\le\exp(-\Omega(\sqrt{\log c})),\qquad
 c/R_0\ge\exp(\Omega(\sqrt{\log c}/\log\log c)).
\]
The common radical is at most \(R_0(x-y)(x^2+y^2)\le 2 R_0c^3\), and \(x\asymp c\). This proves the two simultaneous assertions.

For the equivalence take any primitive \(u+v=w\) with \(0<u\le v\) and radical \(R_0\). Let \(B=u^m,\ W=w^m\) for a fixed integer \(m\ge2\), and put \(y=B\). Take \(x=W\) if \(B,W\) have opposite parity and \(x=W-B\) otherwise. Always \(\gcd(x,y)=1\) and the parities differ. Among the five factors of the common radical occur \(B,W,W-B\), whose combined radical is at most \(R_0(W-B)/(w-u)\le2R_0 w^{m-1}\). The two remaining factors cost at most \(4w^{3m}\). Also \(x\ge(1-2^{-m})W\), so the smallest output height divided by the common radical is \(\gg w/R_0\). All heights are \(\asymp w^{4m}\), and
\[
 C_3/C_1 \le (1+1/(2^m-1))^4 .
\]
Choose \(m\) large enough in terms of \(\delta\). If \(w/R_0\ge w^\eta\) infinitely often, the three output ratios exceed a fixed positive power of their heights, for instance any exponent smaller than \(\eta/(4m)\) at sufficiently large heights. This proves the nontrivial implication. A fixed \(\delta\) is essential to this particular argument.

## How many Belyi maps can preserve these prime factors universally?

Here is a precise limit on this construction as a rational-function identity. A Belyi map has all its ramification above \(0,1,\infty\). Two maps are regarded as equivalent if they differ by one of the six target permutations of \(0,1,\infty\). On a smooth projective curve over \(\mathbb Q\) with infinitely many rational points, at most **three** inequivalent \(\mathbb Q\)-defined Belyi maps can have the same geometric set of preimages of \(\{0,1,\infty\}\). If the three individual reduced fibers must coincide after relabeling, at most **two** maps are possible. The three maps above attain the first bound. Taking the ratios of addends to the sum, their ramification partitions are respectively \((4),(4),(1,1,1,1)\) up to order for the first and third, and \((2,2),(2,2),(2,2)\) for the middle. The two fourth-power maps are distinguished by their ramification points. Their common geometric set is \(0,\infty,1,-1,i,-i\) in the ratio \(x/y\).

The argument uses the classical modular uniformization of the three-punctured sphere and the Mazur–Kenku classification of rational cyclic isogenies. A proof follows to make the role of the assumptions explicit.

1. Remove the common set of preimages from the source. Each map is a finite unramified covering of \(Y=\mathbb P^1(\mathbb C)\setminus\{0,1,\infty\}=\mathfrak H/\Gamma(2)\), uniformized by the modular lambda function. On the common universal cover the maps are represented by \(\lambda(g_j \tau)\) for \(g_j\in\mathrm{PSL}_2(\mathbb R)\). Normalize one \(g_j\) to the identity. The uniformizing source group has finite index in each \(g_j^{-1}\Gamma(2)g_j\), so \(g_j\) preserves the common cusp set \(\mathbb P^1(\mathbb Q)\). A Möbius transformation carrying three distinct rational points to rational points lies in \(\mathrm{PGL}_2(\mathbb Q)\). Left multiplication by \(\mathrm{PSL}_2(\mathbb Z)\) amounts exactly to equivalence of the target maps.
2. For a pair of maps put their relative matrix in integral primitive Smith form, with invariant factors \(1,N\), allowing modular changes of basis on both sides. At any ordinary input point this gives a cyclic isogeny of degree \(N\) between the complex elliptic curves given by the two lambda values: up to changes of basis it is the inclusion of the lattices \(\mathbb Z+\mathbb Z N\tau\subset\mathbb Z+\mathbb Z\tau\). Choose a rational noncuspidal input with non-CM \(j\). Such a point exists since the \(j\)-map is nonconstant with finite fibers and only finitely many CM \(j\)-invariants are rational. The two Legendre models over \(\mathbb Q\) then have full rational 2-torsion. Their \(\overline{\mathbb Q}\)-homomorphisms have rank one as a \(\mathbb Z\)-module because they are isogenous and non-CM. Galois thus preserves the cyclic isogeny kernel, acting on the homomorphism by at most a sign. The quotient \(\theta:E\to B\) by this kernel is defined over \(\mathbb Q\). The curve \(B\) is a quadratic twist of the target Legendre curve, hence also has full rational 2-torsion.
3. These two full 2-torsion structures yield a rational cyclic isogeny of degree \(4N\). Choose a rational 2-torsion line \(L_1\subset E[2]\) on which \(\theta\) is injective, and a line \(L_2\subset B[2]\) different from \(\theta(L_1)\). This is possible because the kernel of \(\theta\) is cyclic. Write \(\alpha:E\to E/L_1\) and \(\beta:B\to B/L_2\). The map \(\beta\theta\widehat\alpha\) has degree \(4N\), and the odd part of its kernel is cyclic. Its kernel does not contain the full 2-torsion of \(E/L_1\) since \(\widehat\alpha((E/L_1)[2])=L_1\). A noncyclic finite 2-subgroup of an elliptic curve in characteristic zero would contain the full 2-torsion. Therefore this is a rational cyclic isogeny. The only multiples of 4 in the classification of rational cyclic isogeny degrees are \(4,8,12,16\), giving \(N\in\{1,2,3,4\}\).
4. Lattice homothety classes locally at \(p\) form the usual tree of valence \(p+1\): neighbors correspond to index-\(p\) sublattices up to homothety, parametrized by the lines mod \(p\). The distance between two vertices is \(v_p(N)\), the difference of the two Smith exponents. Primitive rational lattices specify different maps up to the modular equivalence in step 1 exactly when they differ in at least one such tree. If a pair differs at 3, its distance there is one. A third class differing at 2 from these cannot be compatible with both, since one relative index would be divisible by 6. A third class differing only at 3 would form a triangle, impossible in a tree. Otherwise all variation is in the trivalent tree at 2 with diameter at most two. Such a set has at most four vertices; a four-vertex set is a center and all three of its neighbors.
5. At the chosen real non-CM point, distinct lattice vertices give distinct elliptic isomorphism classes. Otherwise a nonscalar rational Möbius map would fix the parameter in \(\mathfrak H\), making it imaginary quadratic. The three neighbors of the hypothetical center would therefore be the quotients by its three different order-two subgroups. On a full-real-2-torsion model \(y^2=(x-e_1)(x-e_2)(x-e_3)\), \(e_1<e_2<e_3\), the quotient by the middle root lacks full real 2-torsion. Indeed after translation write the model \(y^2=x(x^2+A x+B)\) with \(B=(e_2-e_1)(e_2-e_3)<0\). The other 2-torsion coordinates on the quotient satisfy \(x^2-2Ax+A^2-4B=0\), of discriminant \(16B<0\). Quadratic twists have the same 2-torsion Galois action. This excludes four rational maps and proves the first bound.
6. When the individual fibers agree, even \(N\) is impossible. After Smith normalization the two distinct cusp labels of \(0,1\in\mathbb P^1(\mathbb Q)\) modulo 2 become the same label under \(\tau\mapsto N\tau\) for even \(N\). They were already distinct points on the compactified source since its group lies in \(\Gamma(2)\). Modular changes of basis merely permute the labels. Thus two inequivalent maps must differ at 3. Step 4 bounds their number by two. The [quartic identities with pairwise matching entries](abc_pairs_same_radical.md) attain this bound: their fibers interchange simple and triple multiplicities at the matched pairs of linear factors.

The bounds concern geometric fibers of Belyi maps. They permit additional arithmetic coincidences at special integer inputs and additional identities with ramification outside \(0,1,\infty\). Neither the bound on the number of maps nor the triple construction supplies \(C_1/R\ge C_1^\eta\) for infinitely many groups and one fixed \(\eta>0\).

The two external classification inputs used here are the modular interpretation of \(X(2)\) and the rational cyclic isogeny theorem of Mazur and Kenku. Standard references are F. Diamond and J. Shurman, *A First Course in Modular Forms* (2005), and M. A. Kenku, *On the number of \(\mathbb Q\)-isomorphism classes of elliptic curves in each \(\mathbb Q\)-isogeny class*, J. Number Theory 15 (1982), 199–202.

## A height gap one can verify exactly

In the explicit three-map family, the first two heights are squares \(x^4\) and \((x^2+y^2)^2\). Taking \(y=1,\ x=2^{3^j}\) makes these **consecutive squares**, so no two different square heights of comparable size can be closer in absolute difference. The common radical of the three triples is \(R=\operatorname{rad}(2(x^4-1))\). Lifting the exponent gives \(v_3(x^4-1)=j+1\), whence \(x^4/R\ge 3^j/2\gg\log(x^4)\). In this explicit infinite sequence the relative difference between the nearest two heights is \(2/x^2+1/x^4\) while all three have a growing absolute radical deficit. The factor \(\log(x^4)\) still has vanishing exponent relative to \(x^4\).
