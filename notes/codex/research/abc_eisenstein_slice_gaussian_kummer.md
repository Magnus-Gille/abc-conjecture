# Split reduction ranks and a nonabelian division condition on the elliptic slice

Let \(E:Y^2=X^3+36X^2+36X\), \(P=(-2,8)\), and take \(p\ge5\). Write \(r=\operatorname{ord}(P\bmod p)\), and \(e=v_p(B_r)\) for the first denominator depth. The [slice construction](./abc_eisenstein_twelfth_elliptic_slice.md) would contradict abc from infinitely many \(e\ge2\) with \(\log p\ge\delta r^2\). The only first square up to ten million is at the inert prime 211, of rank 53 and depth 2. Here the split primes mean \(p\equiv1\bmod4\).

## The Gaussian annihilator and its lifts

The rational two-isogeny onto \(E_6:v^2=u^3-36u\) takes \(P\) to \(Q=(-2,-8)\). In coordinates it sends \((X,Y)\) to \(((X+12+36/X)/4,\;Y(1-36/X^2)/8)\). Over \(K=\mathbf Q(i)\), \(J(u,v)=(-u,iv)\) supplies full \(\mathbf Z[i]\) multiplication. At a split place identify the annihilator of the reduction of \(Q\) as \((\gamma)=(g\eta)\), where \(g\) is the positive gcd of the two coefficients and \(\eta\) is primitive Gaussian. Let \(r'=\operatorname{ord}(Q\bmod p)\). Then
\[
 r'\in\{r,r/2\},\qquad r'=gN\eta,\qquad N\gamma=r'^2/N\eta .
\]
The last two follow by taking the Smith normal form of multiplication by \(\gamma\). The two-isogeny has unit differential, and if \(r/r'=2\) that scalar also has unit differential. Thus \(r'Q\) has the first depth \(e\). The group order is prime to \(p\): it is a multiple of four and is less than \(2p\) for \(p\ge7\) by Hasse, with \(p=5\) checked directly. It follows that the Gaussian multiplier \(r'/\gamma\) has unit differential, so \(\gamma Q\) also has depth exactly \(e\). In fact the annihilator of \(Q\) modulo the \(j\)th power of this split place is
\[
                      (\gamma)\mathfrak p^{\max(0,j-e)}
\]
where \(\mathfrak p\) is the Gaussian prime whose endomorphism has nonunit differential at that place. This follows from the formal logarithm, which adds \(v_{\mathfrak p}(\xi)\) to the depth when multiplying by \(\xi\). The local annihilator stays unchanged modulo the square precisely at a first square.

From the split local denominator term in the absolute height of \(u(\gamma Q)\) one gets
\[
            e\log p\le 2\widehat h(Q)r'^2/N\eta+O(1).
\]
The global height identity uses \(\deg[\gamma]=N\gamma\). Thus on any single-prime sequence with \(\log p\ge\delta r^2\), \(N\eta\) belongs to a bounded finite list, and \(g\gg_\delta r\). This is the Gaussian instance of the [bounded complementary ideal argument](./abc_octic_elliptic_wieferich_literature.md) for a different CM field. The Frobenius \(\pi\) of norm \(p\) has \(\pi-1\in(g\eta)\). In particular \(E_6[g]\) is rational over \(\mathbf F_p\). At unbounded odd prime ranks \(q\) on a decisive sequence the annihilator is eventually \((q)\); for \(q\equiv3\bmod4\) this follows even without the height threshold since \((q)\) is prime. In these assertions \(r'=q\) because the original kernel has order two.

The dyadic constraints below give a stronger norm form at every split odd rank. Write \(\pi=a+bi\) with \(a\) odd and \(b\) even, which is possible for the actual Frobenius since full \(E_6[2]\) is rational. Odd \(r\) forces \(p\equiv1\bmod8\) and 2 to be a fourth power modulo \(p\). The quartic supplement for 2 gives \(8\mid b\). Since \(g\) is odd and \(\pi\equiv1\bmod g\),
\[
            p=(1+2gA)^2+64g^2 B^2,\qquad B\ne0.
\]
In particular \(p\ge64g^2+1\). When the odd-rank annihilator is full this has \(g=r\).

## Dyadic arithmetic special to this curve

At \(p\equiv5\bmod8\), \(E\) has a unique nonzero rational two-torsion point, since the other abscissas are \(-18\pm12\sqrt2\). Its 2-Sylow is cyclic. The abscissa character of rational two-isogeny descent sends \(P\) to the nonsquare \(-2\); hence \(P\) generates that Sylow after projection. On \(E_6\) the 2-torsion abscissas are \(0,\pm6\). At such a split prime some nonzero 2-torsion is divisible by two precisely if 6 is square: then \((0,0)\) is divisible, and otherwise none is. For \(\pi=a+bi\), one has \(b\equiv2\bmod4\), and \(v_{1+i}(\pi-1)\) is either 2 or 3. This is the 2-adic valuation of \(\#E_6(\mathbf F_p)=N(\pi-1)=\#E(\mathbf F_p)\), and it equals 3 exactly when some 2-torsion is divisible by two. Thus
\[
   v_2(r)=3\quad(p\equiv5\bmod24),\qquad
   v_2(r)=2\quad(p\equiv13\bmod24).
\]

Write \(t=\sqrt[4]2\), \(s=t^2\), and label the roots on \(E\) as \(e_0=0,\ e_1=-18+12s,\ e_2=-18-12s\). The full half-point field and the 4-torsion field are
\[
 K_0=\mathbf Q([2]^{-1}P)=\mathbf Q(i,t),\qquad
 F=\mathbf Q(E[4])=K_0(\sqrt3).
\]
For the first formula adjoin the square roots of \(X(P)-e_j\) over the two-torsion field \(\mathbf Q(s)\). All halves produce these square roots by the duplication identities, and conversely the standard halving formula recovers the points from them. Take
\[
 r_0=-is,\quad r_1=2i(1-s)t,\quad r_2=2(1+s)t .
\]
Their product is \(-8\). They generate exactly \(K_0\) over \(\mathbf Q(s)\). For the second formula apply halving to the two-torsion points, adjoining \(i\) and the square roots of their abscissa differences. One has \(0-e_{1,2}=6(1\mp s)^2\) and \(e_1-e_2=24s\). The field \(K_0\) has degree eight, is dihedral over \(\mathbf Q\), and is unramified outside 2; hence \([F:\mathbf Q]=16\).

For \(p\equiv1\bmod8\), full \(E[2]\) is rational, and \(P\) is a double over \(\mathbf F_p\) precisely when \(p\) splits completely in \(K_0\), equivalently when 2 is a fourth power modulo \(p\). At \(p\equiv17\bmod24\), \(6\) is a nonsquare, the 2-Sylow on \(E_6\) has order four by the halving test, and on \(E\) the entire 2-Sylow is rational \(E[2]\). Thus \(r\) is odd exactly when 2 is a fourth power in this class, and otherwise \(v_2(r)=1\). Among all primes the odd-rank portion of this residue class has density \(1/16\): these primes split in \(K_0\) and act nontrivially on \(\sqrt3\).

## The fourth preimages have a nonabelian condition independent of every CM ray field

Let \(L=\mathbf Q([4]^{-1}P)\). It contains \(F\) since differences of the preimages give \(E[4]\). Take the half \(H\) of \(P\) corresponding to \(r_0,r_1,r_2\), with abscissa \(x=-2+r_0r_1+r_0r_2+r_1r_2\). As all 4-torsion is \(F\)-rational, one half of \(H\) gives all fourth preimages of \(P\) over \(F\), and
\[
                    L=F(\sqrt{x-e_0},\sqrt{x-e_1}).
\]
At two places over 73 use \(i\mapsto27\) and \(t\mapsto18,48\). The first gives \(x=52,\ (e_0,e_1,e_2)=(0,1,36)\) and the three quadratic characters of the differences are \((-,-,+)\). The second gives \(x=59,\ (e_0,e_1,e_2)=(0,36,1)\) and \((-,+,-)\). Both embeddings extend over \(\sqrt3\). Independence of the first two sign columns proves \([L:F]=4\), so \([L:\mathbf Q]=64\).

In fact \(L\cap K^{\rm ab}=F\), for \(K=\mathbf Q(i)\). To see this, put \(G=\operatorname{Gal}(L/K)\). Its normal kernel over \(F\) acts on a fourth preimage by translation in \(E[2]\). Conjugation on that kernel is the usual two-torsion action, because \(E[4]\) is rational over \(F\). The element \(\sigma:t\mapsto it\) fixing \(\sqrt3,i\) exchanges \(T_1=(e_1,0)\) and \(T_2=(e_2,0)\). Thus \([G,G]\) contains translation by \(T_0=T_1+T_2\).

To obtain an independent commutator, \(\sigma H-H\) is \(T_1\) or \(T_2\). It is neither \(O\) nor \(T_0\) since the two above reductions \(52,59\) are distinct and \(52\cdot59\equiv2\not\equiv36\bmod73\), whereas \(x(H+T_0)=36/x\). The abscissa squareclass character on \(E(K_0)\) now gives \(\sigma(x)/x=3w^2\) with \(w\in K_0^\times\), because \(e_{1,2}=-6(1\mp s)^2\) and \(-2\) is square in \(K_0\). For \(z=\sqrt x\), any lift of \(\sigma\) sends \(z\) to \(\pm\sqrt3\,wz\). Let \(\tau\) fix \(K_0\) and negate \(\sqrt3\). Any of its lifts sends \(z\) to \(\pm z\). The two lifts anticommute on \(z\). Translation by \(T_0\) fixes \(z\): the subgroup fixing \(z\) inside \(E[2]\) is a line preserved by \(\sigma\) since \(\sigma z/z\in F\), and the only such line is \(\langle T_0\rangle\). The two commutators therefore generate the full kernel. Finally \(F/K\) is abelian, so \([G,G]=\operatorname{Gal}(L/F)\), proving the intersection.

Consequently for every fixed finite abelian \(A/K\) containing \(F\), exactly one quarter of the prime ideals splitting completely in \(A\) split completely in \(L\). This applies after arbitrarily many fixed Gaussian ray congruences or pure CM torsion splitting conditions. The primes have degree one up to a set of prime-ideal density zero. These are splitting conditions, and the proportion does not assert a distribution conditional on an exact point annihilator.

## Two exact odd-rank strata

At \(p\equiv1\bmod24\) with \(r\) odd, the point \(P\) is a double, hence \(p\) splits in \(K_0\), and in \(F\) since 3 is square. The point is also divisible by four. Since \(E[4]\) is rational here, all its fourth preimages are rational modulo \(p\). Thus it must split completely in \(L\).

At \(p\equiv25\bmod48\), this last condition is also sufficient. Splitting in \(L\) gives quartic residuacity of 2, hence \(8\mid b\). All of \(E_6[4]\) is rational since \(6\) and \(12\) are squares and \(-1\) is square. Thus \(a\equiv1\bmod4\). Now \(p\equiv9\bmod16\) implies \(a\equiv5\bmod8\), and \(v_2(N(\pi-1))=4\). The rational \(E[4]\) is therefore the entire 2-Sylow of \(E\); a four-divisible \(P\) has odd order.

Exactly half the primes splitting in \(L\) are \(9\bmod16\). Indeed the maximal subfield of \(F\) abelian over \(\mathbf Q\) is \(\mathbf Q(\zeta_{24})\), by the dihedral Galois group of \(K_0\) and the independent \(\sqrt3\). Hence \(F(\zeta_{16})/F\) is quadratic. It is abelian over \(K\) and the intersection just proved gives \([L(\zeta_{16}):L]=2\). Combining the exact \(17\bmod24\) and \(25\bmod48\) strata shows that the lower and upper natural densities, among all rational primes, of split primes of odd reduction rank satisfy
\[
              \frac{9}{128}\le\underline\delta
                   \le\overline\delta\le\frac{10}{128}.
\]
Only the completely splitting primes in \(L\) that are \(1\bmod48\), of density \(1/128\), remain undecided by these tests. The tests constrain early split squares; they do not settle their infinitude or the existence of a fixed-exponent witness.

## The full dyadic Kummer image and exact odd-rank density

In fact the family left in the preceding bounds is resolved by the same finite-layer certificate. The natural density of split primes of odd rank, among all rational primes, is
\[
                         \boxed{55/768}.
\]
Including inert primes the density of odd rank is \(151/768\). These results concern reduction order; first denominator depth two imposes a further condition.

Let \(T=T_2E\), and \(K_\infty=K(E[2^\infty])\). This torsion field is abelian over \(K\) by CM (one may equally use the rational 2-isogeny to the Gaussian curve on the rational Tate module). Its intersection with \(L\) is exactly \(F\), by the derived-subgroup calculation. Over \(K_\infty\) choose a compatible tower of \(2^n\)-division points of \(P\). The absolute Galois group acts on it by translations in the closed additive subgroup \(H\subseteq 2T\), since all halves of \(P\) are already rational. Its projection to \(2T/4T\) is the entire group, since \([LK_\infty:K_\infty]=4\). Nakayama's lemma, or successive approximation modulo powers of two in a closed subgroup, gives \(H=2T\). The same proof allows any further fixed abelian extension of \(K\) in the base.

In the full affine Galois image, Haar measure conditional on a torsion action \(M\) gives the uniform measure on a single translation coset \(t_0+2T\). For a good prime \(p\) with this Frobenius, the reduction of \(P\) has odd order exactly when the affine action on the compatible tower has a fixed point, that is, when its translation vector lies in \((M-1)T\). The equivalence uses the prime-to-\(p\) étale nature of all the finite division fibers and the fact that divisibility by every power of 2 in the finite group \(E(\mathbf F_p)\) is odd order. The latter subgroup of \(T\) has measure \(|\det(M-1)|_2=2^{-v_2(\#E(\mathbf F_p))}\). When full \(E[2]\) and all halves of \(P\) are rational its coset is \(2T\), and \((M-1)T\subseteq2T\). The conditional probability is then \(4|\det(M-1)|_2\). These formulas can be used in finite quotients then passed to Haar measure by Chebotarev. Once \(v_2(\det(M-1))<k\), membership in \((M-1)T\) is decided modulo \(2^k\) because \(2^kT\) is contained in it. In the ray classes below the density of the omitted large-valuation set tends to zero.

The \(17\bmod24\) class contributes \(1/16\) as above. In the \(1\bmod24\) class an odd rank requires splitting in \(F\), a set of density \(1/16\) among all primes. Conditional on splitting in \(F\), the signed Gaussian Frobenius has the form
\[
                    \pi=(1+4u)+8vi,\qquad u,v\in\mathbf Z_2,
\]
with \(u,v\) independent in Haar measure. Here is the ray-class justification. At split \(p\), the curve \(v^2=u^3-u\) has its rational \((0,0)\) divisible by two, so its signed Gaussian Frobenius is primary (equal to 1 modulo \((1+i)^3\)); the roots \(0,\pm1\) give the halving criterion. Of the four norm-\(p\) Gaussian generators exactly one is primary at either fixed Gaussian prime. The curve \(E_6\) is its quadratic twist by 6, which has sign \(+1\) on this stratum. The congruences for splitting in \(F\) amount to a primary generator with imaginary coefficient divisible by 8 and norm \(1\bmod3\); the prime-to-2 restriction is independent of all higher dyadic digits by the Chinese remainder theorem. The prime ideal theorem in fixed Gaussian ray classes now supplies uniformity of \(u,v\) modulo every fixed power of two. The conjugate choice gives the same statistic. The exceptional valuation tails tend to zero since \(v_2(u^2+4v^2)\to\infty\) forces both coordinates into arbitrarily small neighborhoods of zero.

Now \(\#E(\mathbf F_p)=16(u^2+4v^2)\). For two independent 2-adic Haar integers let \(J=\mathbb E|u^2+v^2|_2\). Splitting according to their parities gives \(J=1/2+1/8+J/16=2/3\). Similarly \(\mathbb E|u^2+4v^2|_2=1/2+J/8=7/12\). The odd-rank probability conditional on splitting in \(F\) is \(7/48\). Thus the contribution of this stratum is \(7/768\), giving \(55/768\) after addition.

For inert \(p\) the group order is \(p+1\) by the trace-zero character sum. If \(p\equiv7\bmod8\), full \(E[2]\) is rational but \(-2\) is a nonsquare so \(P\) is not a double. If \(p\equiv3\bmod8\), the 2-Sylow is cyclic of order four, \(E(\mathbf F_p)[2]\) has order two, and \(-2\) is a square. The rational 2-isogeny descent character is nontrivial (its kernel is the dual-isogeny image of index two); hence \(P\) is a double, as the group has a unique index-two subgroup. The image \((M-1)T\bmod2\) has two elements. Its intersection with the translation coset is nonempty by divisibility of \(P\) by 2 and contains exactly half of the measure of \((M-1)T\). Thus the conditional odd-rank probability is \(4\cdot2^{-2}/2=1/2\) throughout this class, giving the additional density \(1/8\).

## Densities for forced squares at a neighboring index

In the base-2 construction \(n=2^{k+1}-1\), primes with \(v_2(r)\le1\) can be placed to depth at least two at \(n-1=2(2^k-1)\). Their exact density is \(199/384\). For the base-3 choice \(n=2\cdot3^k-1\), the exact density of the usable rank condition \(3\nmid r\) is \(121/160\).

For the first statement the full dyadic translation image means that, conditional on torsion Frobenius, the 2-primary point class is uniformly distributed in one coset of \(2G\) in the 2-Sylow \(G\) of the residue group. Here \(G\simeq T/(M-1)T\). The coset modulo \(2G\) is the actual halving character already determined by the torsion field \(F\). One counts the elements of \(G[2]\) in that coset.

The classes \(5,13\bmod24\) give no primes, and \(17\bmod24\) contributes \(1/8\). At \(1\bmod24\) with quartic residuacity of 2, \(P\) is a double, all four points of \(G[2]\) are doubles, and the conditional probability \(16/|G|\) averages to \(7/12\), by the Gaussian integral above. Without quartic residuacity only \(T_0\) is divisible among the nonzero two-torsion, and \(P,T_1\) have the same three abscissa characters \((+,-,-)\) at the \(e_j\). Thus two points of \(G[2]\) belong to the point's coset, giving \(8/|G|\). Write \(\pi=(1+4u)+4vi\), \(v\) odd, with \(u\) Haar. Then \(\mathbb E|u^2+v^2|_2=3/4\), so the conditional probability averages to \(3/8\). Each of these two subfamilies has density \(1/16\), for a contribution of \(23/384\) from \(1\bmod24\).

At \(3\bmod8\) every rank is usable and the contribution is \(1/4\). At \(7\bmod8\) let \(s=v_2(p+1)\). The full \(E[2]\) is rational, and the first invariant factor of \(E(\mathbf F_p)\) divides \(p-1\) by the Weil pairing. Thus \(G\simeq\mathbf Z/2\oplus\mathbf Z/2^{s-1}\), \(s\ge3\). If \((6/p)=-1\), all of \(G[2]\) have trivial abscissa character at 0 (use \(e_{1,2}=-6(1\mp\sqrt2)^2\)), whereas \(P\) does not. This case occurs at \(7\bmod24\). If \((6/p)=1\), at \(23\bmod24\), put \(\nu=(\sqrt2/p)\) for either chosen square root. The abscissa characters of \(P\) and \(T_1\) are both \((-, -\nu,\nu)\), using the standard value \(\prod_{j\ne1}(e_1-e_j)\) in the \(T_1\) coordinate. Since exactly two 2-torsion points occupy its coset, the probability is \(8/2^s\). This averages to \(2/3\) within \(23\bmod24\), hence contributes \(1/12\). The sum of the contributions is \(199/384\).

For the 3-adic assertion put \(T'=T_3E\). At the split prime 37, the order of the group is 36 and that of \(P\) is 12 (one can check \(3P,4P,6P,12P\) directly from the given curve). Full \(E[3]\) is rational there since 3 is inert in \(\mathbf Z[i]\), the CM Frobenius norm \(N(\pi-1)\) is divisible by 9, and the 2-isogeny preserves the 3-torsion. The 3-Sylow is therefore \(E[3]\), so \(P\) is not triply divisible over \(K\). The image of \(G_K\) on \(E[3]\) is \(\mathbf F_9^\times\); indeed Frobenius at the split prime 5 has determinant \(-1\bmod3\) and hence order 8 in the nonsplit Cartan. As the full torsion field over \(K\) is abelian and the image has a scalar with invertible difference from 1, its \(H^1\) with coefficients \(E[3]\) vanishes by the central-element argument. Hence the global Kummer class remains nonzero on \(K(E[3^\infty])\). Its mod-3 translation image is nonzero and stable under \(\mathbf F_9^\times\), so it is all \(E[3]\). Nakayama now gives the full \(T'\) as the translation subgroup. Conditional on torsion Frobenius, the probability of 3-free rank is \(|\det(M-1)|_3\).

At split primes, the signed Gaussian \(\pi\) is Haar in \(\mathbf Z_3[i]^\times\). To verify this first take any fixed primary dyadic class for the untwisted Gaussian generator, and use the prime ideal theorem in ray classes at the independent 3-power modulus. Twisting by 6 multiplies the generator by a sign depending only on the dyadic class and on its norm modulo 3; multiplication by this sign permutes each norm class. Thus \(7/8\) of the Gaussian units are not 1 modulo 3 and contribute probability one. In the remaining \(1/8\), write \(\pi=1+3u\) with \(u\) Haar. Since 3 is inert, \(\mathbb E|N(u)|_3=(1-1/9)/(1-1/81)=9/10\). The split average is \(7/8+(1/8)(1/9)(9/10)=71/80\). The inert average of \(|p+1|_3\) is \(5/8\): half the primes give 1, and the other half have \(p+1=3u\) with \(u\) Haar in \(\mathbf Z_3\), giving \(1/4\). The final density is \(121/160\). The passage from finite Chebotarev conditions is justified by the vanishing density of large 3-adic determinant valuations, as above.

Using \(k\) a common multiple of the totients of the relevant prime-to-base integers at most \(2Y\), all primes up to \(Y\) in each respective class contribute a square at \(n-1\), apart from fixed bad primes. Hasse gives \(r\le2Y\) for all sufficiently large \(p\le Y\) and \(p\nmid r\). Partial summation gives \(\exp((199/384+o(1))Y)\) and \(\exp((121/160+o(1))Y)\), respectively, in addition to the designated prime-power gain at \(n+1\).

## Rank-free first-square test and a necessary class-group condition

At a split place choose the actual norm-\(p\) Gaussian Frobenius \(\pi\), with connected differential (valuation one). Since \(\pi-1\) lies in \((\gamma)\) and both \(\pi-1,\gamma\) have unit differential, \([\,\pi-1\,]Q\) has depth \(e\). In particular
\[
       e\ge2\quad\Longleftrightarrow\quad
       [\pi]Q\equiv Q\bmod\mathfrak p^2
       \quad\Longleftrightarrow\quad Q\in[\pi]E_6(K_{\mathfrak p}).
\]
For the last equivalence split off the unique prime-to-\(p\) torsion lift of \(Q\bmod p\); the residue group order is prime to \(p\), and \([\pi]\) on the formal logarithm multiplies by a uniformizer.

For sufficiently large split \(p\), this gives a nontrivial everywhere-unramified cyclic extension of degree \(p\) of \(k=K(E_6[\pi])\) whenever \(e\ge2\), split at every place above \(p\). Indeed \(Q\) is not \(\pi\)-divisible over \(K\) for all sufficiently large \(p\), since a putative preimage would have positive canonical height \(\widehat h(Q)/p\), contrary to Northcott over fixed \(K\). The degree of the cyclic scalar torsion extension \(k/K\) divides \(p-1\), so the nonzero Kummer class remains nonzero over \(k\). Adjoining one \(\pi\)-preimage gives all of them and degree \(p\). At the connected \(p\)-place the local class is zero by the displayed test, and at the conjugate place the isogeny is étale on the formal group and invertible on the reduction since there is no residue \(p\)-torsion. At good places away from \(p\), the integral finite étale division fiber is unramified. The finitely many bad places have a compact local group with open pro-residue-characteristic subgroup, so multiplication by \(p\) is an automorphism there for all large \(p\); multiplication by \(\pi\), a factor of \(p\), is also surjective. This verifies the class-group obstruction without a global BSD assumption. Related stronger class-group formulae for a different curve are recorded in the [class-tower note](./abc_cm_first_depth_class_tower.md).

As a finite check, all 2,549 split primes below 50,000 passed the stated residue-class and modulo-73 field-based tests of the split strata. Direct scalar arithmetic over all 17,982 good primes below 200,000 found 1,271 split primes of odd rank, 3,515 primes of odd rank overall, 9,284 ranks with \(v_2(r)\le1\), and 13,627 ranks prime to 3.

## What the observed prime 211 forces in a concrete torsion field

Put \(p=211\), \(k=K(E_6[p])\), \(H=k([p]^{-1}Q)\). The class group of \(k\) has a quotient \((\mathbf Z/211)^2\). More precisely,
\[
 [k:K]=44520,\qquad \operatorname{Gal}(H/k)\simeq(\mathbf Z/211)^2,
\]
and \(H/k\) is everywhere unramified and splits completely at the places above 211. This class group quotient persists after replacing \(k\) by any finite abelian extension of \(K\) containing it.

The prime is inert in \(K\), and the trace-zero reduction is supersingular. All geometric \(p\)-torsion therefore reduces to the identity, while the first unit coefficient of the reduced formal series \([p](z)\) has degree \(p^2\). Weierstrass preparation of \([p](z)/z\) gives an Eisenstein polynomial of degree \(p^2-1\) over \(K_p\) (its constant term has valuation one) whose roots are the nonzero torsion parameters. This remains Eisenstein over unramified extensions. All local and global Galois actions over \(K\) are scalars in \(\mathbf F_{p^2}^\times\) by CM, so this already gives the full scalar group, of order \(p^2-1\).

At the prime \(\ell=2531\equiv3\bmod4\), \(\#E_6(\mathbf F_\ell)=2532=12\cdot211\), whereas direct multiplication gives \([12]Q=(1059,317)\ne O\bmod\ell\). Thus \(Q\) is not divisible by 211 over \(\mathbf Q\). A preimage over \(K\) would make \(2Q\) divisible over \(\mathbf Q\) by tracing, also impossible. Over \(k\) the Kummer class stays nonzero by its prime-to-\(p\) degree. The translation image is stable under all \(\mathbf F_{p^2}^\times\), yielding the full two-dimensional translation module.

At the unique place of \(K\) over 211 the verified first depth two of \([53]P\) transfers to \([53]Q\) under the 2-isogeny. The residue group over \(\mathbf F_{211^2}\) has order \(212^2\), prime to \(211\). Splitting off the prime-to-\(p\) torsion lift, the formal logarithm over unramified \(K_p/\mathbf Q_p\) identifies depth two with divisibility by \(p\). Thus \(Q\) has a local preimage and \(H/k\) splits completely there. Good primes elsewhere give unramified division fibers. At the two bad residue characteristics, the local formal group is pro-2 or pro-3; potential good reduction gives a finite rest with connected residue group of size at most \((1+\sqrt9)^2=16\) and component group of order at most four in the additive case. The residue fields have sizes 2 and 9, respectively. Thus the points are locally \(211\)-divisible at the bad places as well.

Finally any lift of a scalar \(c\ne1\) conjugates a translation \(T\) into \(cT\); hence the derived group over \(K\) is precisely the translation module. The maximal abelian-over-\(K\) subfield is \(k\). Base change to any finite abelian \(A/K\) containing \(k\) therefore preserves the degree and group, as well as unramifiedness and splitting at 211. Class field theory gives the stated quotients. The field \(k\) here is a torsion field abelian over \(K\).
