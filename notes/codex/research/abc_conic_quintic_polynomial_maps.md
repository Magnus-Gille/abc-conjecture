# Quintic covers with a totally ramified point

For \(D=\{0,\infty,\pm\sqrt2,\pm\sqrt{-2}\}\), a degree-five rational map over \(\mathbb Q\) branched only above \(D\) and having three rational preimages of \(D\) cannot have a point of ramification index five. This leaves quintic maps with several poles and no totally ramified point.

A nonrational totally ramified branch value would have a conjugate of the same type. Together they exhaust the total ramification of eight. Over their quadratic field the map then has the form \(s=C u^5\) in coordinates sending the two branch values and two branched preimages to zero and infinity. The branch points in the source are in the quadratic field because they are unique over their values. A rational target has at most one rational input, because neither quadratic field \(\mathbb Q(\sqrt{\pm2})\) contains a nontrivial fifth root of unity. This leaves at most two rational cusps.

A rational totally ramified value is zero or infinity, and target inversion \(t\mapsto2/t\) preserves \(D\). Put its rational inverse image at infinity to obtain a polynomial. The number of distinct finite zeros must be odd since total residual ramification has even degree, and there must be at least two rational finite zeros. If there are three distinct finite zeros then all three are rational and there are just four geometric cusps, excluded by the [dyadic restriction](abc_conic_transfer_dyadic_cusps.md). Thus all five finite zeros are simple.

There are four finite ramification contributions; all are over nonzero elements of \(D\). If just one conjugate target pair \(\pm\alpha\) occurs, each member has either one point of index three or two simple critical points, with the same pattern at both.

* In the first case write \(f'=c((x-h)^2-v)^2\) with rational \(c,h,v\), \(cv\ne0\). The trace of the two critical values is zero, so integration gives \(f=cX(X^4/5-2vX^2/3+v^2)\) with \(X=x-h\). The quadratic in \(X^2\) has negative discriminant, so the only real zero is \(h\).
* In the second case the two simple preimages in these two fibers are a conjugate pair. Since the remaining points in them are precisely the four simple roots of \(f'\), comparison of divisors and leading coefficients gives
\[
             25(f^2-\alpha^2)=((x-h)^2-v)(f')^2,\quad h,v\in\mathbb Q,\ v\ne0 .
\]
Differentiation gives \(25f=Xf'+(X^2-v)f''\). Coefficient comparison yields \(f=a(X^5-5vX^3/4+5v^2X/16)\). A noncentral zero would require \(X^2/v=(5\pm\sqrt5)/8\), impossible over \(\mathbb Q\).

If all four nonzero members of \(D\) are simple branch values, apply a rational source translation and a scaling by the rational leading coefficient to write \(f\) proportional to \(g+d\), where
\[
                         g=x^5+a x^3+b x^2+c x .
\]
The monic normalization of \(\operatorname{Res}_x(g',g-t)\) has these four critical values up to common translation and scaling. After depressing this quartic in \(t\), its quadratic and linear terms must vanish. Their numerators, up to nonzero rational constants, are
\[
\begin{aligned}
 &216a^5-1800a^3c-1725a^2b^2+4000ac^2+4500b^2c ,\\
 &b(81a^6-765a^4c-205a^3b^2+2200a^2c^2+900ab^2c+135b^4-2000c^3).
\end{aligned}
\]
For \(ab\ne0\) divide by \(a^5\) and \(ba^6\), then eliminate \(v=b^2/a^3\) from the resulting equations in \(u=c/a^2,v\). The resultant gives
\[
 2700000000u^5-4104000000u^4+2690100000u^3-932642000u^2+164515275u-11396079=0.
\]
Its leading coefficient is a unit modulo seven and it has no root there. If \(a=0\) and \(b\ne0\), the first equation forces \(c=0\), contrary to the second. For \(b=0\) and \(a\ne0\), the first would give \(4000u^2-1800u+216=0\), whose discriminant is negative. Thus only \(a=b=0\) is left, and symmetry of the critical values then gives \(d=0\). A nonzero rational root of \(x^5+cx\) would give \(-c=r^4\) for rational \(r\ne0\). Its critical points would satisfy \((x/r)^4=1/5\) and have degree four, whereas each is the unique critical point over a quadratic branch value and must belong to that quadratic field. This excludes the final possibility.
