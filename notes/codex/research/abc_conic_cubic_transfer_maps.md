# Cubic covers for the conic transfer

Write \(D=\{0,\infty,\pm\sqrt2,\pm\sqrt{-2}\}\). There is no degree-three rational function over \(\mathbb Q\) branched only above \(D\) for which \(f^{-1}(D)\) contains at least three rational points. The same holds for either composition of a quadratic function and a cubic function defined over \(\mathbb Q\). These assertions concern possible transfers to the conic \(u^2+2v^2=w^2\) using rational functions. Higher degrees remain open here.

## The cubic obstruction

A rational input above \(D\) must map to \(0\) or \(\infty\). Write \(r=\#f^{-1}(\{0,\infty\})\), counting geometric points. For a rational function of any degree, Riemann–Hurwitz gives total ramification outside these two fibers equal to \(r-2\). It is even if every other possible branch value belongs to a Galois orbit of even size. For a cubic satisfying the rational-point requirement, \(r=4\) or 6.

* If \(r=4\) and there is a triple point over a rational value, all four points are rational (three already are). Make the triple point a pole using a rational source coordinate and, if necessary, target inversion. The cubic polynomial has three distinct rational roots; its two other critical values are conjugate and nonrational, hence distinct. In the present target they have sum zero, also after inversion. Depressing the cubic puts it in the form \(a(x^3+bx)\), since the constant is the midpoint of its two critical values. The roots are \(0,\pm h\) with \(h\in\mathbb Q^\times\). The squared critical value is \(4a^2h^6/27\), of squareclass 3, whereas the allowed squareclasses are \(2,-2\).
* If \(r=4\) and the rational fibers each have simple ramification, there are four simple branch values in total, namely \(0,\infty\) and one conjugate pair. If \(r=6\) and the four residual contributions are all simple at different values, the four branch values are the four nonrational elements of \(D\). Both cases are excluded by the Jacobian criterion below. Their discriminant double covers have equations \(y^2=cx(x^2\pm2)\) or \(y^2=c(x^4-4)\), and their Jacobians have \(j=1728\).
* The remaining \(r=6\) case has two totally ramified points over a quadratic conjugate pair. The points themselves lie in that quadratic field \(K\), since each is uniquely specified by its value. In coordinates \(s=(t-\alpha)/(t-\bar\alpha)\) and \(u=(x-\beta)/(x-\bar\beta)\) taking these branch values and points to \(0,\infty\), the cubic has \(s=C u^3\). Rational inputs give \(u\in K\) of norm one. No two can map to the same rational value since \(K=\mathbb Q(\sqrt2)\) or \(\mathbb Q(\sqrt{-2})\) has no nontrivial cube root of unity. This accounts for at most one point over each rational value.

For the Jacobian criterion, a cubic with four simple branch values has geometric monodromy \(S_3\) because it is transitive and contains transpositions. Its arithmetic monodromy is the same subgroup of \(S_3\), so its Galois closure is geometrically connected over \(\mathbb Q\). The quotient by \(A_3\) is the discriminant double cover of the target, branched at those four values. The degree-three morphism onto this quotient is unramified since the inertia groups are transpositions. Both curves have genus one, and the induced map of Jacobians is a degree-three isogeny defined over \(\mathbb Q\), as seen by choosing origins over \(\overline{\mathbb Q}\). Its dual gives a rational cyclic 3-isogeny from the discriminant Jacobian. For a rational elliptic curve \(y^2=x^3+Bx\) with \(j=1728\), a rational cyclic subgroup of order three would give a rational abscissa solving \(3x^4+6Bx^2-B^2=0\). The quadratic \(3v^2+6v-1\) for \(v=x^2/B\) has no rational root.

## A quadratic outer function

Such a quadratic must have at least one rational point in the preimage of \(D\), since every rational point in the proposed composite maps to one. Its branch pair lies in \(D\). If it is the rational pair, a choice of source coordinate gives \(f_2(z)=c z^2\) with \(c\in\mathbb Q^\times\), up to interchanging zero and infinity. If it is a quadratic conjugate pair, the rational fibers above \(0,\infty\) are unramified. They cannot both split. Indeed, with branch coordinates as in the cyclic cubic case, the map is \(s=C u^2\); the two target values give \(s=-1,1\). Splitting both requires a square root of \(-1\) in \(K=\mathbb Q(\sqrt{\pm2})\). Thus just one rational fiber splits. Target inversion \(t\mapsto2/t\) preserves \(D\) and makes this fiber the poles. Put them at zero and infinity in the source. The function is \(a z+b+c/z\); its critical values \(b\pm2\sqrt{ac}\) force \(b=0\), \(ac=\pm1/2\). A rational scaling now gives the two alternatives \(z\pm1/(2z)\). Each normalized outer function has exactly two rational cusps \(0,\infty\).

For \(cz^2\) the remaining cusps comprise two quartic orbits \(z^4=\pm2/c^2\). They have degree four by the odd 2-adic valuation of the right side, since the valuation of a root has denominator four. The cubic analysis over this new cusp set leaves only a four-simple-branch cover with a whole quartic orbit as branch set, whose Jacobian again has \(j=1728\).

For \(z-1/(2z)\), the nonrational cusps are the roots of four irreducible quadratics:
\[
 A=2z^2-1,\qquad B_+=2(z-1)^2-1,\qquad B_-=2(z+1)^2-1,\qquad C=2z^2+1 .
\]
For \(z+1/(2z)\) they are the roots of \(A,C\) and the quartic orbit \(H=4z^4+12z^2+1\). The roots of \(H\) are \(\pm i(1\pm1/\sqrt2)\), individually of degree four. All the listed fibers follow by solving the quadratic in \(z\).

If the cubic has a triple pole after inversion as appropriate, a critical pair from \(A\) has squareclass two and sum zero, and a pair from \(C\) is nonreal. A pair from either \(B\) has both critical values of the same sign. A real cubic with three distinct real roots has a positive and a negative critical value. Taking reciprocals preserves this same-sign obstruction and the squareclasses in the pure case. The two-branch cyclic case is excluded as before; each quadratic orbit lies in one of the same two fields.

For four distinct simple branch values, the following table lists the \(j\)-invariants of the discriminant Jacobians. For a quartic with coefficients \((a,b,c,d,e)\), including a degree-three polynomial by setting \(a=0\), use \(I=12ae-3bd+c^2\), \(J=72ace+9bcd-27ad^2-27b^2e-2c^3\). A model is \(y^2=x^3-27Ix-27J\); a constant factor in the quartic changes this model by quadratic twisting.

| Branch polynomial, with infinity included for cubics | \(j\) |
|---|---:|
| \(zA, zC\) | 1728 |
| \(zB_+, zB_-\) | 8000 |
| \(AB_+, AB_-, AC, B_+B_-, H\) | 1728 |
| \(B_+C, B_-C\) | 128 |

For \(j=8000\) a representative has \((A_E,B_E)=(-270,-1512)\); its 3-division polynomial \(3x^4+6A_E x^2+12B_E x-A_E^2\) has no root modulo 7. For \(j=128\) the representative \((864,34560)\) has no root modulo 5. A rational root would reduce at these primes since the leading coefficient is 3. Quadratic twisting preserves the existence of a rational cyclic 3-isogeny, and all rational curves with either of these two \(j\)-values are quadratic twists. This proves the quadratic-outer, cubic-inner obstruction.

## A cubic outer function

There is also no composite with a cubic outer function and a quadratic inner function. The outer function must have at least two rational cusps to supply three rational points after a quadratic pullback. The cubic analysis already excludes three. Normalize its two rational cusps to \(0,\infty\). We check its quadratic cusp orbits, since a quadratic inner function may branch only above a Galois-stable pair.

If the outer cubic has \(r=2\), it is \(cz^3\) up to source coordinates and target inversion. A quadratic input over \(\alpha=\pm\sqrt{\pm2}\) must lie in \(K=\mathbb Q(\alpha)\). Its conjugate ratio has cube \(-1\), and hence is \(-1\), since \(K\) has no nontrivial cube roots of unity. Every quadratic cusp pair has opposite coordinates and field \(\mathbb Q(\sqrt{\pm2})\).

For \(r=4\) with a triple point over a rational value, make that point the pole. There is one rational zero, since there are two rational cusps. The other two critical values are opposite, so depressing the polynomial makes its constant zero and puts the rational zero at the origin. The critical-value square \(-4b^3/(27a)\) of \(az^3+bz\) is \(\pm2\). A rational variable scaling and, if needed, target sign give \((z^3\pm6z)/4\).

For \((z^3-6z)/4\), the finite roots and the points over its nonrational branch values give the rational zero and the pairs \(\pm\sqrt6,\pm\sqrt2,\pm2\sqrt2\). An input of degree two over the remaining target pair must have the form \(p+q\sqrt{-2}\), with \(p,q\in\mathbb Q\), \(q\ne0\). Its real coefficient forces \(p=0\) or \(p^2=6+6q^2\). Its imaginary coefficient then gives \(q^3+3q=\pm2\) or \(4q^3+3q=\pm1\), respectively. Neither equation has a rational root by the rational root test. The model with the plus sign instead gives pairs \(\pm\sqrt{-6},\pm\sqrt{-2},\pm2\sqrt{-2}\). Over its remaining target \(\pm\sqrt2\), the real part of \((p+q\sqrt2)^3+6(p+q\sqrt2)\) forces \(p=0\), and the same first cubic excludes a solution.

For the two-branch cyclic cubic case, write the branch pair as \(\pm\sqrt D\), \(D=\pm2\). There is one rational preimage of each rational target, and take them to be \(0,\infty\) in that order. The expression \(s=C u^3\) above has \(C=1\) by evaluation at infinity. At zero it gives \((\beta/\bar\beta)^3=-1\). Thus \(\beta/\bar\beta=-1\); after rational scaling, \(\beta=\sqrt D\). The normalized map is
\[
                      \frac{z^3+3Dz}{3z^2+D}.
\]
The zeros, poles and branch fibers give quadratic pairs \(\pm\sqrt{-3D},\pm\sqrt{-D/3},\pm\sqrt D\). At the remaining target pair \(t=\pm\sqrt{-D}\), the target torus coordinate \(s\) equals \(\pm i\). A degree-two preimage \(z\) would lie in \(\mathbb Q(\sqrt{-D})\), so its torus coordinate \(u\) lies in \(\mathbb Q(i,\sqrt2)\). The only cube roots there of \(\pm i\) are \(\mp i\), since this biquadratic field contains no cube root of unity of order three (its quadratic subfields have squareclasses \(-1,2,-2\)). Hence \(z=\pm\sqrt{-D}\). The other cubic branch configurations were excluded by the discriminant Jacobian regardless of their rational cusps.

In all these models every quadratic cusp pair is opposite, and its field is one of \(\mathbb Q(\sqrt{\pm2}),\mathbb Q(\sqrt{\pm6})\). For a quadratic inner map to yield three rational preimages of \(0,\infty\), it cannot branch at both rational values, since those fibers would be singletons. If it branches instead at an opposite pair, neither rational value is a branch value, so both fibers must split. The torus coordinate argument would put \(\sqrt{-1}\) into the quadratic field of that pair. None contains it. This completes both orders of the degree-six decomposition.
