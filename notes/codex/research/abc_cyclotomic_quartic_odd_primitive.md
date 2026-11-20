# Odd first valuations at cyclotomic orders \(5,8,10,12,20\) and their lifts

Let \(A>B\ge1\) be coprime. Call an odd prime \(p\) a witness at order \(m\) if \(\operatorname{ord}_p(A/B)=m\) and \(v_p(A^m-B^m)\) is odd. If \(p\nmid m\) divides \(\Phi_m(A,B)\), its order is \(m\) by separability of \(T^m-1\) modulo \(p\), and its valuation there equals its valuation in \(A^m-B^m\).

* Every order \(2^i\) for \(i\ge3\), \(2^i3\) for \(i\ge2\), and \(2^i5^j\) for \(i\ge2,\ j\ge1\) has a witness for every base pair.
* For each \(j\ge1\), at least one of the orders \(5^j,2\cdot5^j\) has a witness for every base pair.
* At orders 5 and 10 individually, infinitely many coprime positive base pairs have no witness. The examples \(\Phi_5(3,1)=11^2\) and \(\Phi_{10}(11,8)=101^2\) show both failures. Neither cyclotomic value can be five times a square.

## The quartic maps and descent

For \(v^2=1+b t^2+c t^4\) with \(b^2\ne4c\) and \(t\ne0\), set
\[
 U=b+\frac{2(v+1)}{t^2},\qquad V=\frac{2U}{t}.
\]
Then \(V^2=U(U^2-2bU+b^2-4c)\). The equation for \(v\) gives \(((U-b)^2-4c)t^2=4U\), so \(U\ne0\), and hence \(V\ne0\). Conversely a point with \(UV\ne0\) gives \(t=2U/V,\ v=(U-b)t^2/2-1\).

We use the standard two-isogeny descent for \(E:y^2=x^3+a x^2+b_0x\), with \(E':y^2=x^3-2a x^2+(a^2-4b_0)x\). The descent homomorphism \(\alpha\) sends the identity to \(1\), \((0,0)\) to \(b_0\) modulo squares, and each other point to the squareclass of \(x\). Its image has representatives among signed squarefree divisors \(d\) of \(b_0\); such a nontrivial class requires coprime integers \(u,v\) with
\[
 N^2=d u^4+a u^2v^2+(b_0/d)v^4 .
\]
The same applies on \(E'\), and \(2^{\operatorname{rank}E(\mathbf Q)}=|\alpha(E)|\,|\alpha(E')|/4\). This is the rational two-isogeny descent formula, as in Silverman and Tate, *Rational Points on Elliptic Curves*, Chapter III.

Here are the rank-zero curves needed below. The columns \(a,b_0\) specify \(E\); the last column gives orders of its groups at good primes.

| Curve | \((a,b_0)\) | \(\alpha(E)\) | \(\alpha(E')\) | Reduction sizes |
|---|---|---|---|---|
| \(E_5\) | \((-25,125)\) | \(1,5\) | \(1,5\) | \(p=3,11:\ 2,16\) |
| \(E_{12}\) | \((2,-3)\) | \(1,-1,3,-3\) | \(1\) | \(p=5,7:\ 8,8\) |
| \(E_+\) | \((6,5)\) | \(1,-1,5,-5\) | \(1\) | \(p=3,7:\ 4,4\) |
| \(E_-\) | \((-6,5)\) | \(1,5\) | \(1,-1\) | \(p=3,11:\ 4,8\) |

For \(E_5\), \(x\ge0\) gives the first image. Its companion has coefficients \((50,125)\), so its image contains \(5\) and is contained in \(\{1,-1,5,-5\}\). Class \(-1\) would require
\[
              N^2=-u^4+50u^2v^2-125v^4=-(u^2-25v^2)^2+500v^4 .
\]
Opposite parities give \(3\bmod4\). If both variables are odd, \(8\mid u^2-25v^2\) and the right side is \(20\bmod32\), also impossible. This excludes \(-5\) as well.

For the last three curves the companions have \(b_0'=16\) and \(4\mid a'\). Their classes \(d=\pm2\) are impossible: the equation \(N^2=\pm2u^4+a'u^2v^2\pm8v^4\) has valuation 1 at two if \(u\) is odd, and valuation 3 if \(u\) is even. The companions of \(E_{12}\) and \(E_+\) have \(x\ge0\); that of \(E_-\) contains \((-4,8)\), representing \(-1\). On \(E_{12}\), \((-1,2)\) supplies \(-1\) and \((0,0)\) supplies \(-3\). On \(E_+\) the roots \(x=-1,-5\) supply both negative classes. On \(E_-\), \(x\ge0\) and \((0,0)\) supplies \(5\). This proves all the image entries. The reduction sizes follow by enumerating \(x\) over the indicated fields, and injectivity of prime-to-\(p\) torsion under good reduction bounds the rational torsion. Thus \(E_5\) has only \(O,(0,0)\), and \(E_+,E_-\) have only their four rational two-torsion points. The eight points of \(E_{12}\) are
\[
        O,\quad (0,0),(1,0),(-3,0),\quad (-1,\pm2),(3,\pm6).
\]

## The fifth and tenth factors

Write \(f(X,Y)=X^4+X^3Y+X^2Y^2+XY^3+Y^4\), so \(\Phi_5(A,B)=f(A,B)\) and \(\Phi_{10}(A,B)=f(A,-B)\). Put \(r=X-Y,\ s=X+Y\); then \(16 f=5s^4+10s^2r^2+r^4\). In both applications \(rs\ne0\). If \(f=5z^2\), take \(t=r/s,\ v=4z/s^2\); this gives \(v^2=1+2t^2+t^4/5\). The quartic map above followed by \((x,y)=(25U/4,125V/8)\) gives a point on \(E_5\) with \(y\ne0\), impossible. The factors are odd. Thus any nonsquare value has an odd-valuation prime different from 5 and hence a witness.

If \(f=z^2\), take \(t=s/r,\ v=4z/r^2\). Now \(v^2=1+10t^2+5t^4\). The quartic map followed by \((x,y)=(U/4,V/8)\) gives \(E_1:y^2=x^3-5x^2+5x\), with \(t=x/y\). The solution \((X,Y,z)=(3,1,11)\) gives \(P=(4,2)\) on \(E_1\). At the good primes 3 and 7 the group sizes are 6 and 10. Reduction bounds the rational torsion order by two, so \(P\) has infinite order. In the compact group \(E_1(\mathbf R)\), a sequence of distinct multiples of \(P\) tends to the identity; this follows by taking differences of a convergent subsequence. Translating by either rational point belonging to \((X,Y)=(3,1)\) or \((11,-8)\) supplies infinitely many rational points in its neighborhood. The inverse quartic map is regular there. The ratio \(X/Y=(t+1)/(t-1)\) remains respectively in \((1,\infty)\) or \((-\infty,-1)\). The map has finite fibers, so these give infinitely many distinct reduced ratios. Clearing the denominator gives a square integer value of \(f\), since the form is homogeneous of degree four. This proves both infinite families of exceptions.

## Coupling orders 5 and 10, and the twentieth factor

With \(T=A/B+B/A\),
\[
 \frac{\Phi_5(A,B)\Phi_{10}(A,B)}{A^4B^4}
       =\frac{\Phi_5(A^2,B^2)}{A^4B^4}=T^4-3T^2+1 .
\]
A square value would give a point with \(V\ne0\) on \(E_+\) by the quartic map. Thus at least one of the fifth and tenth factors has a witness. With \(T=A/B-B/A\ne0\),
\[
              \frac{\Phi_{20}(A,B)}{A^4B^4}=T^4+3T^2+1 .
\]
A square value would now give a point with \(V\ne0\) on \(E_-\). Moreover \(\Phi_{20}(A,B)=\Phi_{10}(A^2,B^2)\) cannot be five times a square by the \(E_5\) argument. It is odd, so it has an odd-valuation prime outside \(2,5\).

For \(i\ge2,\ j\ge1\) we have \(\Phi_{2^i5^j}(A,B)=\Phi_{20}(A^u,B^u)\), with \(u=2^{i-2}5^{j-1}\). The same two exclusions give an exact-order witness. Applying the coupled-order result at the powers \(A^{5^{j-1}},B^{5^{j-1}}\) gives the asserted alternative at orders \(5^j,2\cdot5^j\). These substitutions use \(\Phi_{p d}(T)=\Phi_d(T^p)\) when \(p\mid d\). The primitive order is always measured for the original ratio \(A/B\), by the separability argument in the first paragraph.

## Pure powers of two and orders \(3\cdot2^i\)

For \(i\ge3\), \(\Phi_{2^i}(A,B)=x^4+y^4\) with \(x=A^{2^{i-3}},y=B^{2^{i-3}}\). Fermat's fourth-power descent excludes \(x^4+y^4=z^2\). Briefly, in a primitive solution take \(x\) even. The primitive Pythagorean parametrization gives \(x^2=2ab,\ y^2=a^2-b^2\) with \(a>b\) coprime. The relation \(a^2=y^2+b^2\) forces \(b\) even. Hence \(a=u^2,\ b=2v^2\). Parametrizing the primitive right triangle with legs \(y,2v^2\) gives \(u^2=c^2+d^2,\ v^2=cd\) with \((c,d)=1\). Thus \(c,d\) are both squares, producing a smaller solution with hypotenuse \(u<z\).

If both \(x,y\) are odd, the two-adic valuation of \(x^4+y^4\) is one. The alternative \(x^4+y^4=2z^2\) is impossible for \(x>y\). Indeed \(t=x/y,\ v=2z/y^2\) would give \(v^2=2(t^4+1)\), hence \((u,w)=(2t^2,2tv)\) on \(w^2=u^3+4u\). The two-isogeny \((u,w)\mapsto (w^2/u^2,w(1-4/u^2))\) gives a point on \(Y^2=X^3-16X\) with \(Y\ne0\), since \(t>1\). Scaling by \(4,8\) gives a rational point with nonzero ordinate on \(Y^2=X^3-X\), contradicting Fermat's theorem that a rational right triangle cannot have area one. For a point \((X,Y)\) with \(Y\ne0\) the triangle has legs \(|(X^2-1)/Y|\) and \(|2X/Y|\). Alternatively the same descent as above gives images \(\{1,-1\}\) on \(y^2=x^3-x\) and \(\{1,2\}\) on \(y^2=x^3+4x\), where \((2,4)\) supplies \(2\). The first curve has rank zero, and reduction of sizes 4 and 8 at 3 and 5 leaves only its four rational two-torsion points. Consequently an odd-valuation odd prime always occurs in the required power-of-two factor. [Earlier twice-a-square calculation](abc_full_quartic_total_kernel_height.md)

Finally \(\Phi_{12}(A,B)=A^4-A^2B^2+B^4\) is odd and is \(1\bmod3\) for coprime inputs. A square value would give \(v^2=1-t^2+t^4,\ t=A/B>1\), and hence a point on \(E_{12}\) with \(V\ne0\). Its rational points listed above all have \(2U/V=\pm1\) when \(V\ne0\). Substituting \(A^{2^{i-2}},B^{2^{i-2}}\) now proves the exact-order claim at every \(2^i3,\ i\ge2\).

Together with the previously established orders \(2^i3^j\) for \(j\ge2\), this gives a witness at every \(2,3\)-smooth order except possibly \(1,2,3,4,6\). At \(3,4,6\) the square examples \(\Phi_3(5,3)=7^2,\ \Phi_4(4,3)=5^2,\ \Phi_6(8,3)=7^2\) show why those orders are excluded. [Previous grid](abc_cyclotomic_odd_primitive_grid.md) · [Uniform counting at fixed prime support](abc_cyclotomic_smooth_order_parity.md)
