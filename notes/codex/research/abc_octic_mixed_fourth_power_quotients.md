# The fourth-power condition on the mixed norm family

Suppose \(s,t\) are primitive, \(s\) is odd, \(t\) is even, \(s^2+2t^2\) is a fourth power and \(U_-=(s-t)^2+t^2\) is a square. The seed \((7,4)\) satisfies these conditions. They give a genus-three hyperelliptic curve with an elliptic quotient of positive rank and a genus-two quotient whose Jacobian has rank at least two. In particular neither quotient gives a rank-zero classification, and the usual Chabauty rank inequality fails for the genus-two and genus-three curves.

## The two quotients

In the norm-Euclidean ring \(\mathbb Z[\sqrt{-2}]\), the conjugates of \(s+t\sqrt{-2}\) have no common prime factor. A common prime would divide both \(2s\) and \(2t\sqrt{-2}\), and the norm is odd. The fourth-power norm thus gives \(s+t\sqrt{-2}=\pm(a+b\sqrt{-2})^4\), the unit being an overall sign. The two coordinates before that sign are
\[
 S=a^4-12a^2b^2+4b^4,\qquad V=4ab(a^2-2b^2).
\]
For the affine parameter \(u=a/b\), put \(S(u)=u^4-12u^2+4,\ V(u)=4u(u^2-2)\). The remaining square condition is the curve \(H:y^2=(S(u)-V(u))^2+V(u)^2\). At \(u=1\) the pair is \((-7,-4)\) and \(y=5\).

Set \(z=u-2/u,\ v=u+2/u,\ w=y/u^2\). Dividing \(S,V\) by \(u^2\) gives \(z^2-8,4z\). Thus the function field of \(H\) is generated over \(\mathbb Q(z)\) by
\[
 v^2=z^2+8,\qquad w^2=F(z)=(z^2-4z-8)^2+16z^2.
\]
The inverse for \(u\) is \((z+v)/2\). The two branch divisors are disjoint and simple, as one also sees from the nonzero discriminant of their product. This degree-four cover of the line has six branch points of index two and genus three. The involution \(u\mapsto-2/u,\ y\mapsto4y/u^4\) changes the sign of \(v\). Its quotient \(E_1:w^2=F(z)\) has genus one. The complementary quotient is obtained by changing the signs of both \(v,w\); it is
\[
 G:\quad W^2=(z^2+8)F(z)=z^6-8z^5+24z^4+192z^2+512z+512,\qquad W=vw .
\]
The third quadratic subfield is the genus-zero curve \(v^2=z^2+8\). Over \(\mathbb Q\), the pullbacks of the differentials of \(E_1,G\) belong to distinct characters of the sign-change group. They have dimensions one and two and span all differentials on \(H\). The quotient maps consequently induce a \(\mathbb Q\)-isogeny between \(\operatorname{Jac}(H)\) and \(\operatorname{Jac}(E_1)\times\operatorname{Jac}(G)\).

The elliptic quotient has a nonconstant map to the mixed seed curve \(C:y_0^2=(x^2+2)((x-1)^2+1)\), given by
\[
 x=(z^2-8)/(4z),\qquad y_0=(z^2+8)w/(16z^2).
\]
At \((z,w)=(-1,5)\) the image is \((7/4,45/16)\). Both curves have a rational point, and their Jacobians are \(\mathbb Q\)-isogenous. The seed curve has a point of infinite order by good reduction at 3, so \(\operatorname{rank}\operatorname{Jac}(E_1)(\mathbb Q)\ge1\). [Seed model and infinite-order point](abc_octic_mixed_seed_prime_orbit.md)

## An independence certificate on the genus-two quotient

Write \(\infty_\pm\) for the two rational points with \(W/z^3\to\pm1\). The factors \(z^2+8,F(z)\) give a nonzero rational 2-torsion class via the pair of roots of the first factor. The discriminant of the monic sextic is \(-2^{68}\), so all odd primes are good. For point counts \(N_i=\#G(\mathbb F_{p^i})\) we use
\[
       \#J(\mathbb F_p)=(N_1^2+N_2)/2-p,\qquad J=\operatorname{Jac}(G).
\]
Indeed the degree-two symmetric product has \((N_1^2+N_2)/2\) points. The map to \(\operatorname{Pic}^2\) has one rational point in each fiber except at the canonical class, whose fiber is a projective line.

| \(p\) | \(N_1\) | \(N_2\) | \(\#J(\mathbb F_p)\) |
|---:|---:|---:|---:|
| 3 | 4 | 18 | 14 |
| 11 | 12 | 162 | 142 |
| 43 | 44 | 1986 | 1918 |

Prime-to-\(p\) torsion injects under good reduction. The first two rows give rational torsion order at most two, since \(3\nmid142\), \(11\nmid14\), and \(\gcd(14,142)=2\).

Take \(D=[\infty_+-\infty_-]\), \(B=[(-1,15)-\infty_+]\). At \(p=3,43\) put \(h_p=\#J(\mathbb F_p)/7\). Direct addition gives \(h_pD\) of order seven at both primes, and
\[
       2B=3(2D)\quad\bmod3,\qquad 274B=4(274D)\quad\bmod43.
\]
The verifier counts the finite-field points, then moves a rational branch \(r\) of the reduced sextic to infinity using \(x=1/(z-r),\,y=W/(z-r)^3\). It uses \(r=1,11\) at \(p=3,43\), respectively. The old infinities become \((0,\pm1)\); with the new Weierstrass origin their divisor classes are negatives. Using the convention that a reduced Mumford pair \((U,V)\) satisfies \(y=V(x)\) at the roots of \(U\), the computed \(h_p D\) are

* \((x^2+x-1,-x-1)\) at \(p=3\).
* \((x^2+13x+17,8x+11)\) at \(p=43\).

If \(aD+bB\) were torsion for a nonzero primitive integer pair \((a,b)\), both even \(h_p\) would kill that torsion. The two reductions would imply \(a+3b\equiv a+4b\equiv0\bmod7\), contrary to primitivity. A dependence in the free quotient always gives a primitive one there. Therefore \(\operatorname{rank}J(\mathbb Q)\ge2\) and \(\operatorname{rank}\operatorname{Jac}(H)(\mathbb Q)\ge3\). The finite calculations can be rerun with standard-library Python. [Verifier](abc_octic_mixed_fourth_power_verify.py)

## The matching 2-descent bound

The étale algebra of the sextic is \(L_1\times L_4\), where \(L_1=\mathbb Q(\sqrt{-2})\) and \(L_4=\mathbb Q(i,\rho)\), \(\rho^2=1-i\). Indeed a root of \(F\) gives \(i\) up to sign from \((z^2-4z-8)/(4z)\), then satisfies \(z^2-4(1+i)z-8=0\) after choosing that sign. Its discriminant is \(32(1+i)\), with squareclass \(1-i\) in \(\mathbb Q(i)\). This class is nonsquare by its odd valuation at \(1+i\).

Both fields have class number one. The first is norm-Euclidean. In \(L_4\), the generator \(\rho\) has polynomial \(X^4-2X^2+2\), Eisenstein at 2 with discriminant 512. Thus 2 is totally ramified and its prime is generated by \(\rho\), of norm 2. The field discriminant divides 512. Since the field contains \(i\), Minkowski's bound on representatives of the class group is at most \((4! /4^4)(4/\pi)^2\sqrt{512}<4\). There is no prime of norm three, since 3 is inert in \(\mathbb Q(i)\). This proves the claim.

Use the even-degree hyperelliptic \(x-\theta\) map on \(J(\mathbb Q)\) into \((L_1^\times\times L_4^\times)/(\text{squares}\cdot\mathbb Q^\times)\). A rational divisor represents each class because the curve has rational infinities, and it can be moved off the branch points and infinities. Evaluation of \(x-\theta\) on this divisor gives the map. Its norm is square by the curve equation, since the leading coefficient is one. At every odd prime the sextic is monic with separable reduction. The valuation parities of all field components coincide there, up to a rational scalar. One can see this on the evaluated rational divisor by considering its closed points over their residue number fields. If the slope is nonintegral at a place, the valuations of all \(x-\theta\) are the same. If the slope is integral, at most one root meets it in the unramified splitting extension, and that valuation is even by the square curve equation. Taking the norms back from each closed point preserves this statement modulo the scalar from its nonintegral slope. Multiplying by suitable rational odd primes therefore gives a representative with even valuations away from 2.

The squareclasses unramified in this valuation sense outside 2 have dimensions two in \(L_1\) and three in \(L_4\). Indeed each has one prime above 2 and trivial class group, and the ordinary unit ranks are zero and one; in both cases roots of unity modulo squares have size two. The rational scalars \(-1,2\) give two independent classes in their product. In \(L_1\), \(-1\) is nonsquare and \(2\) has its squareclass. In \(L_4\), \(-1\) is square and \(2\) has the class of \(i\), since \(2=-i(1+i)^2\). The element \(i\) is nonsquare in \(L_4\): otherwise \(L_4=\mathbb Q(\zeta_8)=\mathbb Q(i,\sqrt2)\), but \(1-i\) and 2 have different valuation parity over \(\mathbb Q(i)\). The norm-square condition imposes at least one further independent condition, since \((\sqrt{-2},1)\) has norm 2 and all scalar pairs have square norm. The image dimension is therefore at most \(2+3-2-1=2\).

For clarity, passing from true to fake 2-descent loses at most one dimension here. In the permutation group \(M=\mu_2^{\{\text{six branches}\}}\), the classes of even subsets modulo complements form \(J[2]\). Thus \(J[2]\hookrightarrow M/\mu_2\) has cokernel \(\mu_2\) via parity. By the cohomology exact sequence, the kernel of \(H^1(\mathbb Q,J[2])\to H^1(\mathbb Q,M/\mu_2)\) has dimension at most one. The explicit \(x-\theta\) descent map is the image of the Kummer map under this arrow, with the squareclass description coming from \(H^1(\mathbb Q,M)\) modulo rational scalars. This is the standard hyperelliptic 2-descent identification. [Poonen and Schaefer, *Explicit descent for Jacobians of cyclic covers of the projective line*](https://doi.org/10.1515/crll.1997.488.141)

Consequently \(\dim_{\mathbb F_2}J(\mathbb Q)/2J(\mathbb Q)\le3\). The rational 2-torsion has dimension one, so \(\operatorname{rank}J(\mathbb Q)=2\). The isogenous seed elliptic factor has rank one by the elliptic descent below, giving \(\operatorname{rank}\operatorname{Jac}(H)(\mathbb Q)=3\).

The seed also rules out isolating the rational parameter by testing squareness at a fixed finite list of places. The nonzero square \(25\) has an open neighborhood of squares in every \(\mathbb Q_p\) and in \(\mathbb R\). Hence sufficiently close rational \(u\) pass every test in any prescribed such list. This does not classify \(H(\mathbb Q)\); Faltings gives finiteness, while determining the points remains open in this calculation.

## Taking the Pythagorean parametrization first

There is another genus-three cover of the same arithmetic problem. The primitive Pythagorean triple with odd leg \(s-t\) and even leg \(t\) gives \(t=2mn,\ s=m^2+2mn-n^2\) with signed choices of \(m,n\). Changing their order can reverse the sign of the odd leg. In this parametrization the fourth-power condition becomes the smooth plane quartic
\[
 D:\quad w^4=G_4(m,n)=m^4+4m^3n+10m^2n^2-4mn^3+n^4.
\]
The original seed is \((m,n,w)=(2,1,3)\). Over \(K=\mathbb Q(i)\), put \(U=m+in,\ V=m-in,\ A=-(1+i)/2\). Direct expansion gives \(G_4=A U^4+2U^2V^2+\bar A V^4\). Its four projective roots are simple since \(A\bar A=1/2\), showing smoothness of \(D\).

The involutions changing the signs of \(U,V,w\) give three genus-one quotients over \(K\). Their simultaneous quotient has coordinates \([U^2:V^2:w^2]\) on a smooth conic. Thus the three invariant differential lines belong to distinct sign characters and exhaust the differentials on \(D\). The sign of \(w\) yields the rational quotient \(W_0^2=G_4(m,n)\). Its elliptic Jacobian has positive rank, since it maps nonconstantly to the mixed seed curve via \(x=(m^2+2mn-n^2)/(2mn)\), \(y_0=W_0(m^2+n^2)/(4m^2n^2)\).

The other two quotients are conjugates over \(K\). In the \(V=1\) chart the quotient by the sign of \(U\) has coordinates \(h=w/V,\ B=1+A(U/V)^2\) satisfying \(B^2=A h^4+1/2\). It maps to \(y^2=x^3+(A/2)x\) by \(x=A h^2,\ y=A h B\). The latter curve is 2-isogenous over \(K\) to \(E':y^2=x^3+(1+i)x\) by quotienting by \((0,0)\). The maps from the two conjugate quotients give a map of the rational Jacobian to \(\operatorname{Res}_{K/\mathbb Q}E'\): over \(K\) its components are the map to \(E'\) and its conjugate. Together with the rational genus-one quotient, the differential decomposition proves a \(\mathbb Q\)-isogeny onto the product.

The point \(P'=(i,i)\) on \(E'\) has infinite order. Its double has abscissa \(-3/4-i\). At the prime over 5 where \(i=3\) this double reduces to \((0,0)\), so \(P'\) reduces to order four. At the other prime above 5 the reduction is \(y^2=x^3+3x\) and has order ten by direct counting. Both primes are good. A finite order for \(P'\) would be divisible by four from the first reduction, contrary to injectivity on 2-primary torsion at the second. Since \([i]\) is defined over \(K\), \(P'\) and \([i]P'\) are independent: any nontrivial relation would place \(P'\) in the kernel of a nonzero endomorphism. This proves \(\operatorname{rank}E'(K)\ge2\), hence the rational Jacobian of this alternate plane quartic also has rank at least three.

In fact the plane quartic has rational Jacobian rank **exactly three**. For \(E_{a,b}:y^2=x^3+ax^2+bx\), the usual 2-isogeny descent uses the squareclass of \(x\), with the value \(b\) at \((0,0)\) and 1 at infinity. Its partner has coefficients \((-2a,a^2-4b)\). In both applications below the original curve has exactly one nonzero rational 2-torsion point. The product of the two image sizes is \(2^{r+2}\) for Mordell–Weil rank \(r\): the respective kernels are the images of the dual isogeny and of the original isogeny, whose composition is doubling. The two-point dual kernel has only its identity in the image of rational 2-torsion. For integral \(a,b\), any prime not dividing \(b\) has even valuation on \(x\), by the curve equation, both for negative valuation and positive valuation.

For \(E/\mathbb Q\) on the seed model, \(b=8\) and the partner has \(b'=32\), so both images involve only 2 and the sign. On \(E(\mathbb R)\) one has \(x\ge0\), since its cubic \(x(x^2-8x+8)\) is negative for \(x<0\). The two image sizes are at most 2 and 4. This proves \(r\le1\), with equality by the seed point. For \(E'/K\) the two coefficients \(b,b'\) are \(1+i,-4(1+i)\). The ring \(\mathbb Z[i]\) is principal, there is only one prime over 2, and its unit group modulo squares has order two. Each image has size at most four, so \(r\le2\), with equality by \(P',[i]P'\). The plane Jacobian therefore has rational rank \(1+2=3\). The rational elliptic and surface factors supply two independent rational Néron–Severi classes, so it satisfies the quadratic Chabauty inequality \(r<g+\rho-1\). Computing a Chabauty locus and identifying the rational points require additional arguments.

The calculation at 11 now gives all rational slopes. The only nondegenerate signed slope in this fourth-power case is \(7/4\). [Complete rational-point classification](abc_octic_mixed_elliptic_chabauty_11.md)
