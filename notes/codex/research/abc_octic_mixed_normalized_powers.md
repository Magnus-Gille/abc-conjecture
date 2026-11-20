# Cubes, fifth powers and seventh powers of the normalized square root

Suppose that \(s,t\) are coprime integers, with \(s\) odd and \(t>0\) even. Then
\[
 s^2+2t^2=81w^6,\qquad (s-t)^2+t^2=z^2
\]
has just the signed slope \(s/t=7/4\). It gives \(|w|=1,\ |z|=5\). Equivalently, on the orbit through \((7,4)\), \(A_m=\sqrt{Y_{3m}}/9\) is a cube only at the positive odd multiplier \(m=1\). Here \(Y_N\) uses the full positive odd index \(N\).

## The singular exception in the parametrization

Recall the elliptic sequence \(B_N\), the positive square root of the reduced denominator of \(x([N]R_0)\), where \(R_0=(-8,16)\) on \(y^2=x^3+16x^2+32x\). For odd \(N\ge3\) it equals \(\sqrt{Y_N}\) on the full two-square parametrization. At \(N=1\) the slope is infinity and \(B_1=1\); the primitive homogeneous pair there is \((1,0)\). Every admissible slope occurs once among the positive odd indices \(N\ge3\). The order of \(R_0\) modulo 3 is 3, and \(B_3=9\), so \(3\mid Y_N\) forces \(N=3m\). [Full group and parametrization](abc_octic_full_mixed_orbit.md) · [Denominator identity](abc_octic_mixed_three_factors.md)

First take odd \(m\) prime to 3. Put \(b=B_m,\ v=\sqrt{V_m}\), using \(b=v=1\) if \(m=1\). The tripling formula gives
\[
 A_m=b C_1 C_2,\qquad 3 C_1=b^4-4b^2v^2+6v^4,\qquad 3 C_2=b^4+4b^2v^2-2v^4.
\]
The three factors are pairwise coprime positive integers. The proof by division polynomials only uses that \(m\) is odd and prime to 3: the 3-adic valuation of \(B_{3m}\) remains two, and every odd common divisor of the two quartic numerators must be 3. In particular \(b,v\) are both prime to 3. Set \(h=(b^2-v^2)/3\). Then
\[
 b^4-C_2=6h^2.
\]
If \(A_m\) is a cube, coprimality gives \(b=u^3\), \(C_2=d^3\) with positive integers \(u,d\). Thus \(X=-6d/u^4\), \(W=36h/u^6\) satisfy \(W^2=X^3+216\).

## Why the Mordell curve has no rational point with nonzero ordinate

Translating its abscissa by six gives \(y^2=x^3-18x^2+108x\); the curve 2-isogenous by its point \((0,0)\) has equation \(y^2=x^3+36x^2-108x\). For a model \(y^2=x^3+a x^2+b x\), the 2-isogeny descent squareclasses are represented by signed squarefree divisors \(d\) of \(b\). A necessary condition for such a class is a primitive solution of
\[
 L^2=d U^4+a U^2 V^2+(b/d)V^4.
\]
The class of the point \((0,0)\) is that of \(b\). The original cubic after translation is nonnegative only for \(x\ge0\), so its candidate classes are \(1,2,3,6\). The classes 1 and 3 occur. For \(d=2,6\) the right side has 2-adic valuation one: after division by 2 it reduces to \(U^4+U^2V^2+V^4\equiv1\bmod2\) for primitive inputs. The original image has order two.

The partner image contains \(1,-3\). Representatives of the other cosets modulo this subgroup are \(-1,2,-2\). For \(d=-1,2\), if \(3\nmid U\) the right side is 2 modulo 3; if \(3\mid U\), it has exact 3-adic valuation three. For \(d=-2\), opposite parities of \(U,V\) give 2-adic valuation one, and both odd give 8 modulo 16. Thus the partner image also has order two. The rank formula \(2^{r+2}=|\operatorname{im}\alpha|\,|\operatorname{im}\alpha'|\) yields rank zero. Good reductions of the Mordell curve at 5 and 7 have respective group orders 6 and 4; these follow by direct point counts. Injection of prime-to-residue-characteristic torsion, with 5 and 7 also excluded at the opposite prime, leaves just the identity and \((-6,0)\) over \(\mathbf Q\).

It follows that \(h=0\), so \(b^2=v^2\). For the full slope at index \(m\), \(b^2-v^2=2s_mt_m\). This cannot vanish at a nondegenerate slope. Hence \(m=1\) is the unique cube index prime to 3. In fact the rational identity \(C_2/b^4=1-6(h/b^2)^2\) shows that this quotient cannot be a rational cube at any nondegenerate such slope.

## Removing all powers of 3 from the index

Write \(m=3^e m'\) with \(3\nmid m'\). At any odd good prime \(p\mid B_n\), the formal group gives \(v_p(B_{kn})=v_p(B_n)+v_p(k)\), since the denominator depth is the formal-parameter valuation of \([n]R_0\). Every \(A_j\) at odd index is odd. Also \(A_{m'}\) is prime to 3. Therefore every prime of \(A_{m'}\) retains its valuation in \(A_m\). A cube at index \(m\) forces a cube at \(m'\), hence \(m'=1\). At multiplier 3 the tripling identity, evaluated with \(b=9,v=5\), gives
\[
 A_3=B_9/9=2211\cdot13411=3\cdot11\cdot67\cdot13411.
\]
The 11-adic valuation is one, and stays one at all multipliers \(3^e\), \(e\ge1\). This completes the classification. At \(m=1\) the full index is 3, which indeed gives \((7,4)\).

## Fifth powers

The same signed pair \((7,4)\) is the only solution when \(s^2+2t^2=81w^{10}\) and \((s-t)^2+t^2=z^2\). At an odd multiplier prime to 3, suppose \(A_m\) is a fifth power. The coprime factors above give \(b=u^5\), \(C_2=d^5\), with \(\gcd(u,d)=1\) and \(3\nmid u\). Divide \(b^4-C_2=6h^2\) by \(b^4\) and put \(x=d/u^4\), \(y=h/u^{10}\). The resulting curve \(6y^2=1-x^5\) has just three rational affine points, \((1,0)\) and \((1/3,\pm11/27)\). The fraction \(d/u^4\) is reduced and its denominator is prime to 3. This leaves \(x=1\) and \(h=0\), hence \(m=1\). The valuation argument at powers of 3 applies verbatim to fifth powers, including the depth-one witness at 11. The same two classifications exclude any power exponent in \(A_m\) divisible by 3 or 5 for every \(m>1\). [Genus-two classification](abc_octic_mixed_fifth_power_chabauty.md) · [Arithmetic verifier](abc_octic_mixed_fifth_power_verify.py)
## Seventh powers

The same classification holds for \(s^2+2t^2=81w^{14}\). In the preceding argument take \(b=u^7\), \(C_2=d^7\), \(x=d/u^4\), and \(y=h/u^{14}\). The curve \(6y^2=1-x^7\) has just the affine rational point \((1,0)\), so the argument at multiples of 3 again leaves only \((s,t)=(7,4)\). Thus any exponent in \(A_m\) divisible by 3, 5 or 7 is excluded for \(m>1\). [Genus-three descent](abc_octic_mixed_seventh_power_descent.md) · [Arithmetic verifier](abc_octic_mixed_seventh_power_verify.py)
