# The first denominator multiplicity as a discriminant in a tower of division points

Use \(K=\mathbf Q(\sqrt{-2})\), \(E:y^2=x^3+16x^2+32x\), \(R=(-8,16)\). Take any split prime \(p>7\), with \(v\mid p\) and CM generator \(\pi\) whose differential has valuation one at \(v\). Write \(r=\operatorname{ord}(R\bmod p)\) and \(e=v_p(B_r)\), where \(B_r^2\) is the abscissa denominator. If the reduction of \(R\) has exact CM annihilator \((q)\) at a prime index \(q\), then \(r=q\). All odd-index denominator primes split in this CM field. [Reduction and annihilators](abc_odd_rank_quartic_cutoff.md)

Choose \(P_0=R\) and compatible division points \([\pi]P_m=P_{m-1}\). Set \(M_m=K(P_m)\), of degree \(p^m\) over \(K\), and \(M_0=K\). Define \(d_m=v_v(\mathfrak d_{M_m/K})\), the exponent in the relative discriminant ideal. Then
\[
 \boxed{\quad d_m-pd_{m-1}=
   \begin{cases}
       p^m-2,&1\le m<e,\\
       p^m,&m\ge e .
   \end{cases}\quad}                                                     \tag{1}
\]
In particular, \(e\) is exactly the first layer at which the exponent of \(v\) in \(N_{M_{m-1}/K}\mathfrak d_{M_m/M_{m-1}}\) equals \(p^m\). At the first layer, simple denominator primes give exponent \(p\), repeated primes exponent \(p-2\).

More explicitly, write \(s=\min(m,e-1)\), \(j=m-s\), and \(h_i=\varphi(p^i)\) with \(h_0=1\). The place \(v\) has exactly \(s+1\) extensions to \(M_m\), all with residue degree one, of respective ramification degrees
\[
                         p^j h_i,\qquad 0\le i\le s.                       \tag{2}
\]
The discriminant is
\[
                 d_m=m p^m-2\frac{p^m-p^{m-s}}{p-1}.                      \tag{3}
\]
In particular the number of places over \(v\) at every sufficiently high level is exactly \(e\). The computation takes place in the non-Galois division-point fields and uses no class-number formula.

## The global orbit

The rational point \(R\) generates the free part of \(E(\mathbf Q)\). It is indivisible by \(\pi\) over \(K\). Indeed if \(R=[\pi]Q\) with \(Q\in E(K)\), conjugating the equation after multiplication by \(\bar\pi\) gives \([p](Q+\bar Q)=[\pi+\bar\pi]R\). Since \(\pi=a+b\sqrt{-2}\) has norm \(p\), we have \(0<|2a|\le2\sqrt p<p\), contradicting rational primitivity. In the abelian field \(k_m=K(E[\pi^m])\), a scalar differing from unity modulo \(p\) acts on \(E[\pi]\). This follows also from the local Eisenstein calculation below at \(i=1\). As the scalar is central, \(H^1(\operatorname{Gal}(k_m/K),E[\pi])=0\), by the inner-automorphism identity on group cohomology. Hence the nonzero \(\pi\)-Kummer class of \(R\) remains nonzero over \(k_m\), so \(R\) has no \(\pi\)-preimage there. The action of \(G_{k_m}\) on a \(\pi^m\)-division point translates by a subgroup of the cyclic group \(E[\pi^m]\). A proper subgroup is killed by \([\pi^{m-1}]\) and would give such a rational \(\pi\)-preimage. Thus translations are transitive on all \(p^m\) division points, proving the asserted field degree over \(K\). [Global division group and generator](abc_dyadic_kummer_inertia.md)

## Integral factors over the completion

Work over \(K_v=\mathbf Q_p\), with integer-normalized valuation in each finite extension. The residue group has order prime to \(p\), since its order is even by rational two-torsion and is less than \(2p\) by Hasse. Let \(T\) be the unique prime-to-\(p\) torsion lift of \(R\bmod p\). It admits a rational \(\pi^m\)-preimage in its prime-to-\(p\) torsion group: on the group of points killed by \(r\), the inverse of \(\pi^m\) is an integral CM multiplier modulo \(r\). Subtract that preimage from all the local division points. Their images under \([\pi^m]\) now equal the formal point \(F=R-T\). On the special fibre \([\pi^m]\) is purely inseparable, so every division point of \(F\) belongs to the formal group.

The depth of \(F\) is \(e\), since \([r]F=[r]R\), \(p\nmid r\), and depth is the valuation of \(-x/y\). The formal logarithm identifies the formal group over \(\mathbf Q_p\) isometrically with \(p\mathbf Z_p\). Consequently \(F=[\pi^s]F_0\) with \(F_0\) rational of depth \(e-s\), equal to one if \(j>0\). The original division equation for the translated point \(Z\) becomes
\[
                 [\pi^j]Z=F_0+U,\qquad U\in E[\pi^s].                     \tag{4}
\]

Take an exact \(\pi^i\)-torsion point \(U\), \(1\le i\le s\), and its formal parameter \(u\). In formal group notation, \([\pi](t)\) has linear coefficient of valuation one and reduction of initial degree \(p\). Indeed the reduced isogeny has inseparable degree \(p\) and trivial geometric kernel. The power series
\[
             \frac{[\pi^i](t)}{[\pi^{i-1}](t)}
             =\left.\frac{[\pi](z)}{z}\right|_{z=[\pi^{i-1}](t)}
\]
has constant coefficient of valuation one and reduction of initial degree \(h_i=p^i-p^{i-1}\). Weierstrass preparation gives an Eisenstein polynomial of degree \(h_i\). Its roots are precisely the parameters of the exact \(\pi^i\)-torsion points. They form one local Galois orbit. The field \(L_i=\mathbf Q_p(U)\) is totally ramified of degree \(h_i\) with uniformizer \(u\). Put \(L_0=\mathbf Q_p\) for \(U=O\).

If \(j>0\) and \(i>0\), the parameter of \(F_0+U\) is a uniformizer in \(L_i\). The parameter of \(F_0\) has valuation \(h_i>1\), while \(u\) has valuation one, so this follows from the linear part of the formal group law. For \(i=0\) the same conclusion holds since \(F_0\) has depth one over \(\mathbf Q_p\). If \(a\) is this parameter, \([\pi^j](t)-a\) has constant coefficient of valuation one over \(L_i\), with reduction of initial degree \(p^j\). Its distinguished factor is again Eisenstein. Any solution of (4) generates a totally ramified degree-\(p^j\) extension of \(L_i\). It contains \(L_i\), since \(U=[\pi^j]Z-F_0\). For \(j=0\), translating by the rational \(F_0\) identifies the solution field directly with \(L_i\). Thus there is exactly one local orbit for each \(i\), giving (2). Their degrees sum to \(p^j\sum_{i=0}^s h_i=p^m\).

## Differents and discriminants

For a formal CM multiplier, invariance of the differential gives
\[
                        [\pi^a]'(t)=\pi_v^a\,\text{(unit)}
\]
at any positive-depth parameter, where \(\pi_v\) denotes its scalar differential at \(v\). In particular the derivative has the valuation of \(p^a\). Passing to a distinguished polynomial by Weierstrass preparation changes derivative values at roots by a unit. Differentiating the exact-torsion series at \(u\) therefore gives
\[
 v_{L_i}(\mathfrak D_{L_i/\mathbf Q_p})
       =i h_i-p^{i-1}\qquad (i\ge1).
\]
Indeed \([\pi^{i-1}](u)\) is a level-one torsion parameter, of valuation \(h_i/(p-1)=p^{i-1}\) in \(L_i\). The Eisenstein polynomial gives the full different because its root is a uniformizer and generates the ring of integers. For \(i=0\) the different exponent is zero.

The degree-\(p^j\) Eisenstein extension in (4) has relative different exponent \(j p^j h_i\), again from its derivative. Different transitivity gives absolute different exponent \(j p^j\) when \(i=0\) and
\[
                    p^j\big((j+i)h_i-p^{i-1}\big)
\]
when \(i>0\). All residue degrees equal one, so the sum of these exponents is \(d_m\). Using \(\sum_{i=1}^s i(p^i-p^{i-1})=s p^s-(p^s-1)/(p-1)\) gives (3). Subtraction at successive levels yields (1) by discriminant transitivity. The integral order given by the distinguished polynomial for \([\pi^m](t)-t(F)\) has discriminant exponent \(m p^m\), again by its derivative. Its index in the product of the local integer rings is therefore \(p^{(p^m-p^{m-s})/(p-1)}\).

The identities determine the first exponent from the splitting of \(v\) or the relative discriminants as the tower varies. They provide no estimate for how often the second or later layers occur at the primes dividing a given denominator.

## Independent field-discriminant check

At \(p=11\) take \(\pi=3+\sqrt{-2}\). The original seed has reduction order 9. Direct rational multiplication gives \(v_{11}(x([9]R))=-2\), hence first depth one. PARI's relative discriminant of the degree-11 abscissa polynomial of \([\pi]^{-1}R\) has exponents 11 and 0 at the connected and conjugate places. For a comparison using a point of first depth two, replace the seed locally by \([\pi]R\). Its division fibre factors into the rational point \(R\) and an irreducible degree-ten orbit. The discriminant of the degree-ten field has exponents 9 and 0. The calculation constructs the abscissa map by adding \([3]P\) and \([\sqrt{-2}]P\), and computes the relative *field* discriminants of the irreducible factors. Both local cases agree with (1). The second calculation varies the seed over \(K\). [Executable PARI/GP check](abc_cm_first_depth_discriminant.gp)

For an example with split prime index and full annihilator, take \(q=19\), \(p=2243\). Direct multiplication gives \(v_p(x([19]R))=-2\), so \(e=1\). The CM formula gives \([\tau]R=(-2,2\tau)\). For the two choices \(\tau=116,2127\) in \(\mathbf F_{2243}\), the reductions of \([1+3\tau]R\) are respectively \((840,1053)\) and \((1034,557)\). They are both affine. Since \(19=(1+3\tau)(1-3\tau)\), this excludes both proper annihilators. Thus for this prime the unique local factor has degree \(2243^m\) and relative discriminant increments \(2243^m\) at every layer. [Full-factor cutoff data](abc_odd_rank_quartic_cutoff.csv)

At level two, the same check factors the degree-121 division polynomials at 11 and computes local integral-basis differents. In the following rows the first column gives the seed and the next two columns give the degrees and different exponents of all local factors.

| Seed | Local degrees | Local different exponents | Discriminant exponent |
|---|---|---|---:|
| \(R\) | 121 | 242 | 242 |
| \([\pi]R\) | 11, 110 | 11, 209 | 220 |
| \([\pi^2]R\) | 1, 10, 110 | 0, 9, 209 | 218 |

Each nonlinear factor becomes Eisenstein after translating its single residue root. For an Eisenstein polynomial \(g(t)=\sum a_i t^i\) of degree \(d\), the valuations \(d v_p(i a_i)+i-1\) of the derivative terms at a root are distinct modulo \(d\). Their minimum is the different exponent, so seven digits of coefficient precision suffice here, using the monic leading term and \(d\le121\). The computation represents \(\sqrt{-2}\) to 90 digits. At each root the derivative of the full division polynomial has valuation two, since the target and preimage have nonzero ordinate on reduction, the denominator of the abscissa map is a unit in this disk, and the differential of \([\pi^2]\) has valuation two. Thus congruence of the monic polynomials beyond four digits gives corresponding roots in the same local fields by Hensel's lemma. The three level-two discriminants distinguish first depths one, two, and at least three.
