# A degree-six lower bound for a halving-quartic construction

For odd \(r\), let \(B_r\) be the abscissa denominator square root of \([r](-8,16)\) on \(y^2=x^3+16x^2+32x\). There are coprime integers \(T,U\) for which
\[
   B_r^2=F(T,U),\qquad F(t,1)=t^4+4t^2-16t+12.
\]
For \(r=1\) use \((T,U)=(1,0)\). For larger positive odd indices, in the [odd-index parametrization](abc_octic_full_mixed_orbit.md), \(B_r^2=s^2+2u^2\) and \((s-u)^2+u^2\) is a square with \(s\) odd and \(u\) even. The primitive Pythagorean parametrization gives signed integers \(a,b\) with \(s-u=a^2-b^2\), \(u=2ab\). Direct expansion gives the displayed identity with \((T,U)=(a+b,b)\).

Let \(g\in\mathbb Q(t)\) have degree \(d\), and suppose all four zeros of \(F\) lie over \(0,1,\infty\). Let \(k\) count the *other* distinct geometric points in these three fibers. **If \(d\le5\), then \(k\ge d\).** Consequently, the elementary radical estimate that only uses smallness of \(\operatorname{rad}(B_r)\) and bounds the remaining forms by their degrees cannot improve the odd-index quality bound \(8/7\) at these degrees. In detail, with \(M=\max(|T|,|U|)\), the height of the associated primitive triple is \(\asymp_g M^d\), and this radical estimate is \(O_g(M^k\operatorname{rad}(B_r))\). The statement allows additional branch values for \(g\).

The quartic is irreducible. If \(\theta\) is a root, \(\tau=(\theta^2-2)/(2(\theta-1))\) has \(\tau^2=-2\), by \(F(t,1)=(t^2-2)^2+8(t-1)^2\). Over \(\mathbb Q(\tau)\) the root satisfies \(t^2-2\tau t+2\tau-2=0\), with discriminant \(-8\tau\) of odd valuation seven at the prime \((\tau)\). All four roots therefore land in one rational special fiber, with equal multiplicity, so \(d\ge4\).

## Degree four

If \(k\le3\), the two other fibers have at most three points between them. One is a single rational pole of multiplicity four after relabeling the target. With the quartet as the zero fiber, the map is a constant times \(F(t,1)/(t-h)^4\) for \(h\in\mathbb Q\), or a constant times \(F(t,1)\) for a pole at infinity. The third fiber has at most two points, hence total ramification at least two there. Its value would be a repeated root of the discriminant polynomial
\[
 D_h(y)=\operatorname{disc}_t(F(t,1)-y(t-h)^4).
\]
Indeed at a finite value of a polynomial map, the order of its discriminant equals the sum of \(e-1\) over that fiber. A fractional linear change moving the unique pole to infinity changes the binary quartic discriminant by a fixed nonzero factor.

For finite \(h\), direct discriminants give \(\deg_y D_h=3\), and
\[
 \operatorname{disc}_y D_h
 =-2^{48}(h^2-2h+2)^2(h^4-12h^2+16h-4)^2
 (29h^4-180h^3+296h^2-104h-12)^3.
\]
The three factors have no rational root. Reductions at \(3,3,5\), respectively, have nonzero leading coefficients and no affine roots, as one checks by substitution. For the pole at infinity the corresponding discriminant is \(-6864893206996189184\), also nonzero. This excludes \(k\le3\).

## Degree five

The marked fiber has one additional rational point. If \(k\le4\) the other two fibers again have at most three points between them. Normalize a single rational pole of order five to infinity. The other fiber is either a single rational point or two rational points with distinct multiplicities. Rational changes of variable and a scaling of the target now give one of
\[
 G(x)=x^5,\qquad x(x-1)^4,\qquad x^2(x-1)^3.
\]
For the additional rational point \(z\) in the marked fiber, the four zeros of \(Q_z(x)=(G(x)-G(z))/(x-z)\) would have to be projectively equivalent to the original quartet.

For a quartic with coefficients \(a,b,c,d,e\), write \(I=12ae-3bd+c^2\) and \(J=72ace+9bcd-27ad^2-27b^2e-2c^3\). Its smooth double cover has \(j=1728\cdot4I^3/(4I^3-J^2)\). The original quartet has \(j=8000\). Substituting the three candidates into \((1728-8000)4I^3+8000J^2\) and removing nonzero constants and roots corresponding to degenerate marked fibers gives, respectively,
\[
 \begin{gathered}
 1,\\
 11625z^3-41850z^2+53345z-25088,\\
 11625z^8-83700z^7+257880z^6-439304z^5+443070z^4
       -257700z^3+71500z^2-3375.
 \end{gathered}
\]
The two nonconstant polynomials have nonzero leading coefficients and no roots modulo \(17,19\), respectively. This excludes \(k\le4\) and finishes the degree bound. Degrees six and higher remain open in this calculation.
