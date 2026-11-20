# Least rational Belyi degree for elliptic curves with \(j=8000\)

Every elliptic curve over \(\mathbb Q\) with \(j=8000\) has least rational Belyi degree eight, with no prescribed points above the three branch values. Every genus-one curve over \(\mathbb Q\) with that invariant has rational Belyi degree at least eight.

The degree-three through degree-seven census excludes \(j=8000\) geometrically for every passport except the degree-seven passport with fibers \((6,1),(6,1),(4,2,1)\). On \(E\colon y^2=x^3+16x^2+32x\) the census also verifies the degree-eight Belyi map \(\big((x^2+16x+32)/32\big)^2\). Every elliptic curve over \(\mathbb Q\) with \(j=8000\) is a quadratic twist of \(E\), since \(8000\notin\{0,1728\}\). On the twist \(d y^2=x^3+16x^2+32x\), the same expression in \(x\) defines a rational Belyi map of degree eight. [Prior census and upper bound](abc_octic_marked_belyi_minimum.md)

The independent two-prime enumeration now proves the full lower bound directly by checking every possible rational passport in degrees three through seven. [Two-prime proof](abc_octic_all_belyi_local.md)

## Good reduction at eleven

Suppose a rational Belyi map has the exceptional passport. Each multiplicity occurs once in its fiber, so all seven points are rational. The Galois closure has group contained in \(S_7\), of order prime to 11. The good reduction theorem for prime-to-\(p\) three-point covers gives a smooth reduction of the cover, after finite extension of \(\mathbb Q_{11}\), with the marked points over \(0,1,\infty\) specializing distinctly with the same multiplicities. One can apply the theorem to the Galois closure and take the tame quotient for the original cover. [Grothendieck, *SGA 1*, Exposé XIII](https://arxiv.org/abs/math/0206203)

The curve \(E\) already has good reduction at 11. Its smooth proper model stays the minimal regular model after finite extension. Uniqueness of the minimal regular model in genus one, applied after choosing a section, identifies it with the good source of the cover. Consequently the seven reductions for a map on \(E\) would be distinct points of \(E(\mathbb F_{11})\), and the three fiber divisors would lie in one pencil over \(\overline{\mathbb F}_{11}\).

## The finite calculation

Direct counting gives \(\#E(\mathbb F_{11})=18\). Under \(E\simeq\operatorname{Pic}^0(E)\), the common class of the three fiber divisors minus \(7O\) is rational. Multiplication by 7 permutes this group since \(\gcd(7,18)=1\). Translating all points by a common rational point thus places the three divisors in \(|7O|\). They now have rational section vectors up to scale. Three such vectors are collinear over the algebraic closure exactly when they are collinear over \(\mathbb F_{11}\).

Use \(1,x,y,x^2,xy,x^3,x^2y\) as the basis of sections of \(7O\). At each rational point \(P\), six vanishing conditions give a unique projective section with multiplicity at least six at \(P\). For each ordered pair \(U,V\) of distinct rational points the four vanishing conditions at \(U\) and two at \(V\) also determine a unique section. Both uniqueness statements follow from Riemann–Roch for the residual degree-one divisor. Retain sections with exactly two or three distinct rational zeros, respectively, counting zeros as sections of \(7O\), including \(O\).

| Prime | Rational points | Sections of type \((6,1)\) | Sections of type \((4,2,1)\) | Unordered disjoint pairs of type \((6,1)\) | Incidences of a third fiber of type \((4,2,1)\) with their pencils |
|---:|---:|---:|---:|---:|---:|
| 11 | 18 | 17 | 272 | 84 | 0 |
| 17 | 24 | 23 | 506 | 120 | 0 |
| 19 | 22 | 21 | 420 | 180 | 0 |

The first row suffices. The checker computes expansions using \(x-x(P)\) as local parameter when \(y(P)\ne0\) and \(y\) otherwise. At \(O\) it uses the distinct pole orders of the basis. For each pair \(s,t\) with disjoint zeros, it tests the projective vectors \(s+ct\) for every nonzero \(c\) in the residue field. Its only dependency is Python's standard library. [Checker](abc_octic_unmarked_belyi_local.py)

## Other rational forms

For this passport, each rational genus-one source has a rational point and therefore admits an elliptic curve structure over \(\mathbb Q\). Its model over \(\mathbb Q_{11}\) is a quadratic twist of \(E\). An unramified nonsquare twist has \(2(11+1)-18=6\) rational points on its good special fiber, too few for seven distinct rational specializations. A ramified twist becomes isomorphic to \(E\) over its ramified quadratic splitting field. Under this isomorphism an inertia element acts by negation on the images of the seven rational points. Inertia fixes their residue coordinates on the good model of \(E\). The seven distinct reductions would therefore all be points of order dividing two, while there are only four such geometric points. This excludes all remaining rational forms for the exceptional passport.
