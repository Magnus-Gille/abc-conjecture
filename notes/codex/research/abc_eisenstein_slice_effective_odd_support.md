# Effective odd-exponent witnesses and explicit neighboring-index growth

On the fixed elliptic slice let \(b_n=\operatorname{sf}(|F_+F_-|/512)\), \(d_4=\operatorname{sf}(|F_4|/16)\), and \(d_5=\operatorname{sf}(|F_5|/32)\). The odd indices start at \(n=3\). The kernels \(d_4,d_5\) are coprime, greater than one, and have all prime factors congruent to \(1\) or \(-1\bmod24\). [Descent](abc_eisenstein_slice_squareclass_descent.md)

## First occurrence of an odd exponent in any progression

Let \(n\equiv a\bmod M\) be a fixed progression of odd integers, taking \(M\) even. Let \(p\ge7\) be prime to \(M\), \(Q=(-8,-64)\) on \(E':v^2=u^3-576u\), and \(r=\operatorname{ord}_p(Q)\). If \(p\) divides \(b_n\) anywhere in this progression, it does so at an index
\[
                 n\le 2p\,\operatorname{lcm}(M,r)<4Mp^2.               \tag{1}
\]
This gives a finite, effective test at every individual prime. If the denominator of \(rQ\) has odd formal depth at \(p\), the bound improves to \(2\operatorname{lcm}(M,r)<4Mp\).

Indeed \(p\) occurs at an odd exponent when \(nQ\) approaches one of the four independent points \(S\) above \(u^2+336u+576=0\) with odd local depth. Each marked point at an actual hit belongs to \(E'(\mathbf Q_p)\). The quartic has a simple zero at each marked point and the depth is precisely \(v_p(J_n)\), where \(J_n=|F_+F_-|/512\). The good reduction group has size divisible by four. The Hasse upper bound is less than \(2p\) for \(p\ge7\), so \(r<2p\) and \(p\nmid r\). [Contact multiplicity and marked points](abc_eisenstein_slice_quartic_lcm.md)

Fix one witnessing index, put \(R=\operatorname{lcm}(M,r)\), and let \(h\le R\) be its least positive representative modulo \(R\). It is odd and \(h\ne1\) because the normalized pair at \(1\) is a unit. All indices \(h+tR\) reduce to the same mark. In the isometric good formal logarithm put \(L=\log(RQ)\), \(A=\log(S-hQ)\), \(e=v_p(L)\). Then \(e\) equals the formal depth of \(rQ\) since \(R/r\) is a \(p\)-adic unit. If \(v_p(A)<e\), the valuation is constant \(v_p(A)\) and the witnessing hypothesis makes it odd. Otherwise \(\alpha=A/L\) is integral and the valuations are \(e+v_p(t-\alpha)\). For odd \(e\), one of \(t=0,1\) gives exactly \(e\). For even \(e\), take \(t_0\in[0,p-1]\) equal to \(\alpha\bmod p\). One of \(t=t_0,t_0+p\) has \(v_p(t-\alpha)=1\), giving \(e+1\). In all cases the chosen \(t\) is at most \(2p-1\), proving (1). [Formal-logarithm identity](abc_eisenstein_slice_small_prime_mass.md)

There is an effective algorithm which, given \(M,a,N,Y\), returns \(n>N\) in this progression and a prime \(p>Y\) such that
\[
                         p\mid b_n,\qquad p>\sqrt{n/(4M)} .
\]
Enlarge \(Y\) to exceed \(M\), 7, and all \(J_j\) in the progression at \(3\le j\le N\). Test consecutive primes \(p>Y\) using (1), doing exact integer arithmetic, until one passes. The search terminates because every infinite progression has infinitely many odd-exponent primes. Otherwise \(d_4\) would have finitely many values there, contrary to the genus-three twists and Faltings' theorem. Consequently a computable unbounded sequence with this power bound occurs inside every fixed progression. The proof of termination uses qualitative finiteness, and the individual-prime test is bounded explicitly. [Genus-three twists](abc_eisenstein_slice_squareclass_census.md)

## Both kernels at indices near one modulo the small reduction orders

There is a constructive family on which both kernels have an effective lower bound. For \(B\ge5\) choose
\[
 L_B=\operatorname{lcm}\bigl(16,\{\operatorname{ord}_q(P):5\le q\le B,\ q\ {\rm prime}\}\bigr),
 \quad P=(-2,8),\quad n_B=1+2L_B.
\]
The calculation below applies to every positive \(n=1+2m\) with \(L_B\mid m\). For each \(i=4,5\), the signed integer \(\eta_i=(d_i/3)d_i\) is a nontrivial fundamental discriminant congruent to one modulo 24. All primes \(q\le B\) satisfy
\[
                              (\eta_i/q)=1.                         \tag{2}
\]
The symbol at two is the Kronecker symbol.

To control the orientation of the two factors at all these primes, use a single rational signed slope on the original elliptic curve. For \(T=(X,Y)\) write \(w=(X^2-36)/(2Y)\), \(U=w^2=X(2T)\), \(V=Y(2T)\). With \(X_0=-2,Y_0=8\), set
\[
       \nu=\frac{X_0V-UY_0}{X_0-U},\qquad g(T)=-\frac{\nu}{X_0 w}.
\]
The intercept of the chord through \(P,2T\) is \(\nu\). The three abscissas in its cubic of intersection have product \(\nu^2\), so \(X(P+2T)=X_0g(T)^2\). Duplication gives the formula for \(w\). Thus \(g(mP)\) is a signed choice of the rational \(x/y\) for \(nP\).

The function extends to \(g(O)=1\) with integral local expansion. More explicitly, use the formal parameter \(t=-X/Y\), \(A=t^2X=1+O(t^2)\) with integral coefficients, \(W=-2tw=A-36t^4/A\), and \(\Lambda=3A+72t^2+36t^4/A\). The tangent slope at \(T\) is \(-\Lambda/(2t)\). Hence \(V'=-8t^3V=\Lambda(4A-W^2)-8A=1+O(t^2)\) and
\[
                 g=\frac{V'-8tW^2}{W(8t^2+W^2)}\in1+t\mathbf Z[[t]] .
\]
For each \(5\le q\le B\), the point \(mP\) is formal at \(q\), giving \(g(mP)\equiv1\bmod q\). At two the known \(4P=(25/196,-6245/2744)\) is formal of depth one. Doubling increases positive 2-adic depth by at least one. Since \(16\mid m\), the depth at \(mP\) is at least three. The expansion above gives \(g=1-8t+O(t^2)\) with integral higher coefficients, so \(g(mP)\equiv1\bmod64\).

In these globally oriented coordinates \(F_-(g,1)\equiv16\bmod64\) and \(F_+(g,1)\equiv-32\bmod64\), so the minus form gives \(F_4\) and the plus form gives \(F_5\). Multiplying by the denominator to the fourth power does not change squareclasses. At each prime \(5\le q\le B\) one has \(F_-(g,1)/16\equiv-F_+(g,1)/32\equiv1\bmod q\). Their squareclasses are \(\eta_4,\eta_5\) by reduction of the original forms modulo three. All prime factors of \(d_i\) are \(\pm1\bmod24\), whence \(\eta_i\equiv1\bmod24\). This proves (2), including the symbols at 2 and 3.

In particular both \(d_i>B\). Pólya–Vinogradov improves this to \(d_i\gg B^2/(\log(2B))^2\), with an absolute effective constant. Indeed the primitive quadratic character of conductor \(d_i\) has sum \(\lfloor B\rfloor\) up to \(B\). When \(d_i\le B^2\), the usual bound \(2\sqrt{d_i}\log(2d_i)\) gives the inequality, and for \(d_i>B^2\) the conclusion holds directly.

More strongly, Burgess gives, for every \(\epsilon>0\),
\[
                      d_4,d_5\gg_\epsilon B^{4\sqrt e-\epsilon},
           \qquad b_n\gg_\epsilon B^{8\sqrt e-\epsilon}.             \tag{3}
\]
Here the modulus of each primitive character is squarefree. In the usual proof let \(x=d_i^{1/4+\delta}\) and \(y=d_i^{1/(4\sqrt e)+\delta'}\), with \(\delta>0\) sufficiently small relative to \(\delta'>0\). If all primes up to \(y\) have character one, then the character sum up to \(x\) is at least \(2\Psi(x,y)-x+O(1)\), where \(\Psi\) counts smooth integers. From \(x-\Psi(x,y)\le x\sum_{y<p\le x}1/p\), and \(\log(\log x/\log y)<1/2\), this is \(\gg_{\delta'}x\). The Burgess character-sum bound with fixed sufficiently large moment parameter gives \(o(x)\), a contradiction. All inequalities can use effective constants. This proves the least-nonresidue estimate for the precise possibly composite moduli needed here.

Finally \(L_B\to\infty\), since a bounded common multiple for all reductions would put a fixed nonzero multiple of \(P\) in the formal group at infinitely many good primes. Hasse's bound gives \(L_B\mid16\operatorname{lcm}(1,\ldots,\lfloor(\sqrt B+1)^2\rfloor)\), so \(\log n_B\ll B\) effectively. Thus the explicit indices \(n_B\) have \(b_{n_B}\gg_\epsilon(\log n_B)^{8\sqrt e-\epsilon}\), with the two separate component bounds in (3). For \(B=7,31,53,101\), direct finite-group addition gives \(n_B=33,481,68641,122522401\), respectively. The unrestricted height bound for an arbitrary index with specified small kernels remains open here. The homogeneous smooth quartic \(s^4+ks^2t^2+k^2t^4=3W^4\) has independent denominator \(t\), so a bound for hyperelliptic integral points alone does not supply one.

### Large odd-exponent primes in either specified factor

The square-root-in-the-index conclusion of (1) also holds separately for a prescribed \(d_i\) in every fixed odd progression, with an effectively computable constant depending on that progression. To see this, work with \(m=(n-1)/2\) and the signed rational function \(g\) just constructed. Fix any \(m_0\) in the progression with \(2m_0+1\ge3\). The value \(g(m_0P)\) is a 2-adic unit. Restricting \(m\) to an effective subprogression \(m=m_0\bmod M'\), one can force \(g(mP)\equiv g(m_0P)\bmod64\) by continuity of \(g(m_0P+T)\) at \(T=O\). Concretely, this rational function is regular there; substitute the standard integral formal parameter series into any local expression with nonzero denominator at \(O\), and choose a sufficiently deep 2-adic disk by the numerator and denominator valuations. Multiplying a fixed formal multiple of \(P\) by powers of two reaches the disk. Thus one sign \(\sigma\) consistently corresponds to \(F_i\) on the subprogression.

Outside an effectively determined finite set of primes, the zeros of \(F_\sigma(g(T),1)\) on the elliptic curve are simple and remain distinct modulo \(p\). Indeed \(F_\sigma\) has distinct nonzero roots disjoint from \(F_0\), the abscissa at \(P+2T\) there is unramified by the equation of the original curve, and multiplication by two and the square map on nonzero slopes are étale. All maps and divisors are fixed, making the finite bad set computable. Hence at a hitting prime the valuation of the normalized factor equals the formal depth to a unique mark over \(\mathbf Q_p\). The positive-slope denominator is a unit there. The proof of (1) applies verbatim to \(mP\), using \(\operatorname{ord}_p(P)\), the modulus \(M'\) and this new mark. Every such hit of odd depth recurs with \(m\le4M'p^2\). No odd-exponent prime of this factor can vanish from its squarefree kernel under the reduction of the index, since its sign label was fixed at two. Faltings supplies infinitely many such primes in the subprogression. Scanning sufficiently large primes therefore produces a computable unbounded sequence with \(P^+(d_i(n))>\sqrt{(n-1)/(8M')}\), for either chosen \(i\).

## A uniform effective count of the high valuations at a fixed prime

For each \(\epsilon>0\) there is an effectively computable \(C(\epsilon)\) such that for every prime \(p\ge5\),
\[
           \#\{n\ge3\text{ odd}: v_p(J_n)\log p\ge\epsilon n^2\}
                        \le C(\epsilon).                            \tag{4}
\]
The constant is uniform in the prime. The bound counts exceptional indices and does not locate the largest one. For any fixed set of \(k\) primes, the number of indices where their total valuation mass exceeds \(\epsilon n^2\) is at most \(kC(\epsilon/k)\).

Choose a positive integer \(m\) with \(\epsilon m^2>8\widehat h(Q)+1\), and write \(n=mj+r\), \(0\le r<m\). At a hit let \(v=v_p(J_n)>0\), and take the unique mark \(S\) with \(S-nQ\) of formal depth \(v\). A decomposition group fixes the mark because the four conjugate marks have distinct reductions at every \(p\ge5\); thus \(S\in E'(\mathbf Q_p)\) in the chosen embedding. If \(v\le v_p(m)\), the weighted valuation is at most \(\log m\), bounding \(n\) effectively. Otherwise the good formal logarithm and its inverse on \(p\mathbf Z_p\) give a point \(Z\in E'(\mathbf Q_p)\) of depth \(v-v_p(m)\) with \([m]Z=S-nQ\). In particular \(T=jQ+Z\) is one of the algebraic points satisfying \([m]T=S-rQ\). For all \(r,S\), their number is at most \(4m^3\). All are nontorsion, because \(S,Q\) are independent modulo torsion. Their abscissas are finite and nonzero, and their degrees, heights and a field containing them are effectively bounded using the fixed curve, the displayed algebraic marks and the division polynomials.

At every \(p\ge5\) the abscissa is a morphism from the smooth good elliptic model to \(\mathbf P^1\) over \(\mathbf Z_p\). It preserves congruence of integral projective points modulo every \(p^u\). Consequently \(X(jQ)\) and \(X(T)\) are congruent in \(\mathbf P^1\) to depth at least \(v-v_p(m)\). Use their ordinary affine coordinates when \(X(T)\) is \(p\)-integral and their reciprocal coordinates otherwise. For \(j>0\) write the resulting rational number as \(a/b\) in lowest terms, and the algebraic target as \(\beta\). Then \(p\nmid b\) and
\[
     -\log|a-\beta b|_p\ \ge\  v\log p-\log m,\qquad
     \log H(a:b)=h(X(jQ))\le2\widehat h(Q)j^2+c_E .
\]
Here \(H(a:b)=\max(|a|,|b|)\), and the ordinary difference between abscissa height and twice the canonical height is effectively bounded for the fixed curve. The choices of \(m\) and \(r\ge0\) imply \(v\log p-\log m\ge3\log H(a:b)\) under the hypothesis of (4), once \(j\) exceeds an effective fixed threshold.

Apply the quantitative absolute Subspace Theorem in dimension two, equivalently quantitative nonarchimedean Roth approximation in this setting. Take the forms \(X,Y\) at infinity and \(X-\beta Y,Y\) at \(p\). The product over these two places and two forms, on the primitive integer vector \((a,b)\), is at most
\[
                 |ab|\,|a-\beta b|_p\,|b|_p\le H(a:b)^{-1}.
\]
All local determinants are one. The number of forms and places is fixed. Their degrees and absolute heights are bounded by the effective data of the finite list of targets and reciprocals, independently of the choice of \(p\) or its embedding. The quantitative theorem gives an effectively bounded number of proper subspaces containing all solutions above its effective coefficient-height threshold. Each line meets \(\mathbf P^1(\mathbf Q)\) in at most one point. The number below that height threshold is bounded by counting primitive pairs in the corresponding integer box. The theorem only bounds the number of exceptional lines; no effective equations for them are required. For each fixed \((r,S,T)\) and choice of affine coordinate, a rational abscissa determines at most one positive \(j\), since \(Q\) has infinite order. Summing over the fixed finite list and the small \(j\) proves (4). The two bad primes on the original model have zero valuation in the normalized \(J_n\).

A reference for the quantitative theorem with effective numbers of exceptional subspaces is J.-H. Evertse and R. G. Ferretti, *A further improvement of the quantitative Subspace Theorem*, Annals of Mathematics 177 (2013), 513–590. This use of the theorem only needs effectiveness of the number and the starting height of the large solutions. For every fixed prime the estimate implies \(v_p(J_n)\log p=o(n^2)\), with an effective uniform bound for the total number of exceptions to each prescribed relative threshold.

## Effective constants for the all-height sublevel count

In this fixed-twist family the number of exceptions in the [all-height squareclass count](abc_eisenstein_slice_squareclass_census.md) can also be bounded effectively. One can use the classical fixed-curve Mumford and Vojta inequalities in their quantitative effective forms, without needing effective uniformity as the geometric isomorphism class of the curve varies.

For clarity, the fixed-curve input is the following usual combination of the Mumford gap principle and Rémond's effective Vojta inequality. Embed a fixed smooth geometric curve \(C\) of genus at least two in its Jacobian \(A\) using a fixed branch point as origin. In the real canonical-height space, there are effectively computable constants \(H_0>0\), \(1<u<v\) and \(0<\rho<1\), depending on the fixed embedded curve with its presentation, with these two properties. If two distinct points on \(C\) have norms \(H_0<\|x\|\le\|y\|\le u\|x\|\), their angle has cosine at most \(\rho\). If \(\|y\|>v\|x\|>vH_0\), their cosine also is at most \(\rho\). The first is Mumford's inequality for comparable heights and the second is the curve case of Vojta's inequality for widely separated heights. The curve has no positive-dimensional translate. References for the effective inequalities are G. Rémond, *Inégalité de Vojta en dimension supérieure*, Ann. Scuola Norm. Sup. Pisa (4) 29 (2000), 101–151, and *Décompte dans une conjecture de Lang*, Invent. Math. 142 (2000), 513–545.

A rank \(r\) Euclidean space admits a cover by \(c_\rho^r\) cones within each of which any pair of nonzero vectors has cosine greater than \(\rho\). This follows by packing disjoint small balls on the unit sphere and comparing with a larger ball. In one cone, all the large points of \(C\) have norm ratio at most \(v\) by the second inequality. Subdivide this range into ratios at most \(u\). The first inequality allows one point per such subrange. Thus at most \(c_1^{1+r}\) large points occur in a subgroup of rank \(r\), with an effective \(c_1\). Different algebraic points representing the same real canonical vector (difference torsion) also satisfy the first inequality when large, and hence cannot provide a multiplicity there. In the small range, all points defined over fields of a *bounded degree* are effectively bounded in number by Northcott enumeration: the fixed projective embedding has naive height at most canonical height plus an effective fixed constant for a symmetric polarization.

For the quartic twists \(Y^2=c d F_0F_\pm\), a fixed number field \(K\) contains the branch points and one may choose one as the Abel–Jacobi origin. All twists become one of finitely many fixed embedded curves over \(K(\sqrt d)\). Thus their rational points, viewed on the fixed curve, have degree at most \(2[K:\mathbf Q]\), independently of \(d\). Their Abel–Jacobi images belong to the group obtained from \(J_d(K)\) by this isomorphism. Its rank is effectively \(O_K(1+\omega(d))\): two-torsion splits over the fixed \(K\), and the two-Selmer estimate only uses the fixed class group, fixed bad places, the unit rank and places above \(d\). The cone count plus the effective bound for small points gives
\[
         \#\{n\ge3\text{ odd}:d_i(n)=d\}\le C^{1+\omega(d)}
\]
with an effective fixed \(C\). The consequent bound \(\#\{n:b_n\le Y\}\le C'\sqrt Y(\log(2Y))^A\) likewise has effective constants by elementary divisor-function estimates. It yields an effective density estimate for the odd \(n\le N\) with \(b_n\le n^2/(\log n)^B\) for \(B>2A\), even though it does not give the last index for a fixed \(Y\).
