# How many points of one square class can have the same denominator?

Write \(\operatorname{sf}(n)\) for the positive squarefree integer with \(n/\operatorname{sf}(n)\) a square. For \(u\ge5\), fix a squarefree \(D\) and count all \(1\le v\le u/2\) with \(\gcd(u,v)=1\) and
\[
 D=\operatorname{sf}\bigl(uv(u^2-v^2)\bigr).
\]
Let \(r\) be the rational rank of \(E_D:Y^2=X^3-D^2X\). There are no such \(v\) when \(r=0\), and at most \(2^{r-1}\) when \(r\ge1\). The constant and the threshold \(u\ge5\) are uniform in \(D\). In particular a rank-one twist supplies at most one point per denominator. This bound counts points whether or not they have a small radical.

## A height calculation on a single curve

Let \(E:y^2=x^3-x\). If \(uv(u^2-v^2)=D b^2\), take \(P_v\) on \(E\) with \(x=-v/u,\ y=b\sqrt D/u^2\). It belongs to the image of \(E_D(\mathbb Q)\) in \(E(\mathbb Q(\sqrt D))\) under \(x=X/D,\ y=Y/D^{3/2}\). This definition includes \(D=1\). Every point of that image has rational \(x\).

Use the logarithmic height \(h(a/b)=\log\max(|a|,|b|)\) in lowest terms, with \(h(\infty)=0\). The duplication formula has homogeneous coordinates \(((a^2+b^2)^2,4ab(a^2-b^2))\). The first coordinate dominates the second in absolute value by \(2|ab|\le a^2+b^2\) and \(2|a^2-b^2||2ab|\le(a^2+b^2)^2\). The gcd is 1 unless \(a,b\) are both odd, when it is 4. In fact any odd prime dividing \(a^2+b^2\) divides neither \(ab\) nor \(a^2-b^2\). These formulas cover points of order two and infinity as well. It follows that \(|h(x(2P))-4h(x(P))|\le\log4\). Telescoping the duplication formula for the canonical height gives
\[
 \left|\widehat h(P)-\tfrac12 h(x(P))\right|\le c,\qquad c=(\log2)/3 .
\]

Inside the image of \(E_D(\mathbb Q)\), take the subgroup \(\Gamma\) of points that are in the formal group at every prime above \(p\mid u\) with parameter \(z=-x/y\) satisfying \(v_p(z)\ge v_p(u)/2\). Include the identity; valuations are normalized by \(v_p(p)=1\). This is a subgroup because the formal group law for the integral Weierstrass equation has integral coefficients. It applies also at 2, at the smooth identity. For a nonidentity point in the formal group, \(v_p(x)=-2v_p(z)\). Each \(P_v\) therefore belongs to \(\Gamma\), and every other nonzero point in \(\Gamma\) has rational \(x\) with reduced denominator divisible by \(u\). Thus, with \(H=\log u\),
\[
 \widehat h(Q)\ge H/2-c\quad(0\ne Q\in\Gamma),\qquad
 \widehat h(P_v)\le H/2+c .
\]
In particular \(\Gamma\) is torsion-free. If \(P_v,P_w\) for different \(v,w\) had the same class in \(\Gamma/2\Gamma\), both their sum and difference would be doubles of nonzero elements of \(\Gamma\), since their \(x\) coordinates are distinct. The parallelogram law would then imply
\[
 8(H/2-c)\le\widehat h(P_v+P_w)+\widehat h(P_v-P_w)
 =2\widehat h(P_v)+2\widehat h(P_w)\le4(H/2+c).
\]
This is impossible for \(u>4\). Every \(P_v\) lies on the nonidentity real component of \(E\) because \(-1<x<0\). If there is a point, exactly half of the classes of \(\Gamma/2\Gamma\) have that component, so there are at most \(2^{\operatorname{rank}\Gamma-1}\le2^{r-1}\) choices. The proof uses classes modulo doubles in \(\Gamma\); a half in the entire Mordell–Weil group need not meet the local denominator conditions.

For example \(u=11\) gives \(D=330\) at both \(v=1\) and \(v=5\), since the products are \(330\cdot2^2\) and \(330\cdot4^2\). The corresponding points on \(E_{330}\) are \((-30,1800)\) and \((-150,3600)\). Applying the proof to the subgroup they generate shows they are independent.

## A bound uniform over growing sets of twists

Standard rational 2-isogeny descent on \(E_D\) and its quotient \(Y^2=X^3+4D^2 X\) gives \(2^r\le4^{\omega(D)}\), where \(\omega\) counts distinct primes. Indeed the two descent images consist of square classes supported on primes of \(D\) and \(2D\), respectively. The first sign is arbitrary and the second is positive, since \(X^3+4D^2X\ge0\) forces \(X\ge0\). The product of the image sizes is \(4\cdot2^r\), giving \(2^r\le2^{\omega(D)+\omega(2D)-1}\). Consequently the number of points at any exact \(u\ge5\) with \(D\le Y\) is \(O(Y(1+\log Y)^3)\). Here \(4^{\omega(n)}\le\tau_4(n)\) and the four-divisor sum has this upper bound by three harmonic sums.

If the [localized multiplicity forced by abc failure](abc_localized_prime_contributions.md) were to occur, the twists \(D\le\delta^{-3}\) could account for only \(O(\delta^{-3}(1+\log(1/\delta))^3)\) of those points at a height. For small \(\delta\) this is smaller than the forced count by a positive power after slightly decreasing its exponent. This still permits arbitrarily many different large square classes.
