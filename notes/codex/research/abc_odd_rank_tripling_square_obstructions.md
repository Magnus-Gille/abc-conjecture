# Odd prime valuations outside 3 at every odd tripling index

At every odd \(m\ge3\), the factors \(F_m\) and \(M_m\) of \(B_{3m}\) are **neither squares nor three times squares**. In particular each has a prime other than 3 of odd valuation. The factor \(L_m\) is also never a square. All three conclusions follow from elementary descents on fixed elliptic curves. Together with the [odd-index factorization and character tests](abc_odd_rank_tripling_primitive_factors.md), these give at least three distinct primes of odd valuation in \(B_{3\ell}/9\) for **every** prime \(\ell>3\), and at least four if \(\ell\equiv5\pmod8\). For the first count, the witnesses come from \(B_\ell,F_\ell/3,M_\ell\); nonsquareness of \(B_\ell\) uses the [previous square classification](abc_octic_mixed_elliptic_chabauty_11.md).

In the notation of the factorization, \(s\) is odd, \(t>0\) even and \((s,t)=1\). Write
\[
 b^2=Y=s^2+2t^2,\quad v^2=V=(s-t)^2+t^2,\quad
 L=3s^2-4st+2t^2,\quad M=s^2-4st+6t^2.
\]
The positive odd integer \(w\) satisfies \(w^2=b^4-2(b^2-v^2)^2\), and \(F=w^2+2b^4\). The indices considered have \(st\ne0\); the origin slope \((1:0)\) at \(m=1\) accounts for the exception.

## The two quadratics

Put \(z=(s-t)/t\). Then
\[
       YM/t^4=z^4+2z^2+9.
\]
If \(YM\) is a square, \((z^2,z\sqrt{YM}/t^2)\) lies on \(E_1:y^2=x^3+2x^2+9x\). Its only rational points are \(O,(0,0)\), proved below. Since \(s\ne t\) this excludes a square for \(M\). Replacing \((s,t)\) by \((2t,s)\) sends \(Y\) to \(2Y\) and \(M\) to \(2L\). At the new pair \(z=(2t-s)/s\ne0\), giving the same obstruction to a square for \(L\); this step uses only the square of the product.

The identity \(YM=V^2+8t^4\) also excludes \(M=3u^2\). In that case \(P=(3(v/t)^2,9buv/t^3)\) is a rational point on \(E_2:y^2=x^3+72x\) with positive abscissa. Again this curve has only \(O,(0,0)\).

## The quartic factor

The congruence \(F=w^2+2b^4\equiv3\pmod8\) excludes squares. If \(F=3u^2\), put \(z=(b^2-v^2)/b^2\), \(w'=w/b^2\) and \(u'=u/b^2\). The two identities \((w')^2=1-2z^2\) and \((u')^2=1-2z^2/3\) give
\[
   (X,Y')=(12z^2,36zw'u')\in E_3(\mathbb Q),\qquad
   E_3:\ (Y')^2=X(X-6)(X-18).
\]
Here \(0<X<6\) since \(b^2-v^2=2st\ne0\) and \(w\ne0\). All rational points of \(E_3\) are its two-torsion, which excludes this interval.

## Descent certificates

For \(E:y^2=x^3+a x^2+c x\), write \(E'\) for its two-isogenous curve with coefficients \((-2a,a^2-4c)\). The abscissa squareclass map sends \((0,0)\) to the class of \(c\); the two image sizes multiply to \(2^{2+\operatorname{rank} E(\mathbb Q)}\). Every class has a signed squarefree representative \(d\mid c\) and a primitive solution of \(N^2=dU^4+aU^2V^2+(c/d)V^4\).

* For \(E_1\), the abscissa is nonnegative, leaving \(d=1,3\). At \(d=3\), opposite parities give 3 modulo 4, and odd \(U,V\) give 8 modulo 16. The image has size one. Its partner has \((a,c)=(-4,-32)\), with all four possible classes realized at \(O,(0,0),(-4,0),(8,0)\). Thus the rank is zero. Good reductions at 5 and 7 both have order four. A point of order four would double to \((0,0)\), requiring \(x^2=9\) by duplication; neither candidate has a rational ordinate. There is only one affine point of order two.
* For \(E_2\) the four candidates are \(1,2,3,6\). The class 2 occurs at \((0,0)\), and \(d=3\) gives \(3U^4+24V^4\), which is 3, 11 or 8 modulo 16. The partner has \((a,c)=(0,-288)\), with \(1,-2\) present. Representatives of the three other cosets are \(-1,3,-3\). At \(d=-1\), reduction modulo 3 first forces \(3\mid U\); dividing through by 9 then gives a nonsquare 2 modulo 3 on the right. At \(d=\pm3\) the right side is \(\pm3(U^4-32V^4)\), of 3-adic valuation one. Both images have size two. Reduction orders 2 and 8 at 5 and 7 leave torsion order two.
* Translate \(X=x+18\) on \(E_3\) to get \((a,c)=(30,216)\). The classes \(1,-2,-3,6\) occur at its two-torsion. Of the eight candidates it suffices to eliminate \(-1\). Reduction modulo 3 forces \(U=3u\), \(3\nmid V\); after factoring out 27 the right hand side is \(-3u^4+10u^2V^2-8V^4\), always nonzero modulo 3. Its valuation before division was three. The partner has \((a,c)=(-60,36)\), nonnegative abscissa and candidates \(1,2,3,6\). At \(d=2\), opposite parities give valuation one at 2 and equal odd parities give 8 modulo 16. At \(d=3\), odd \(U\) gives 3 modulo 4; writing \(U=2u\) when even and dividing by 4 gives \(12u^4-60u^2V^2+3V^4\equiv3\pmod4\). At \(d=6\) the right side is \(3(2U^4-20U^2V^2+2V^4)\) with the parenthesis nonzero modulo 3. The image sizes are four and one. Reduction orders 4 and 12 at 5 and 7 bound rational torsion by four, already supplied by the three affine roots and \(O\).

Each reduction order listed here is obtained by counting squares in the displayed equation over the specified prime field. These tests guarantee odd exponents; they allow an odd exponent to exceed one.

## Three new odd valuations at each power of three

Set \(r=3^j\) with \(j\ge2\) and \(m=r/3\). Then \(3\mid b\), so \(s\equiv\pm t\not\equiv0\pmod3\). The negative sign would give \(V\equiv2t^2\pmod3\), impossible for a square. Therefore \(L_m\equiv t^2\pmod3\). Its nonsquareness gives an odd-valuation prime outside 3. The same conclusion holds for \(F_m,M_m\) by their two squareclass exclusions, regardless of their valuations at 3. Thus each factor supplies a different prime \(p\) of odd valuation in \(B_r\). Each such prime has exact order \(r\) for \(R\), since its order divides \(3m\), does not divide \(m\), and these are consecutive powers of three.

At a prime in \(F_m\), let \(P=[m]R\bmod p\). As in the [CM test for the quartic factor](abc_odd_rank_tripling_primitive_factors.md), \(P,[\sqrt{-2}]P\) are independent in \(E'[3]\). Thus \(R,[\sqrt{-2}]R\) form a basis of \(E'[3^j]\): in any \(\mathbb Z/3^j\)-basis their coordinate matrix has invertible reduction modulo 3, by the stated independence after multiplication by \(3^{j-1}\). The CM operators act rationally at the split prime \(p\), so Frobenius \(\pi\) fixes the whole group, and \(\pi-1\) is divisible by \(r\) in \(\mathbb Z[\sqrt{-2}]\). Its norm gives \(p=(1+ra)^2+2r^2c^2\ge2r^2+1\), since \(c\ne0\) and \(r>1\). At either other prime, the rational point of order two and the point of odd order \(r\) force \(2r\le(\sqrt p+1)^2\) by Hasse. In particular \(p\ge r\) for \(r\ge9\).

The three chosen primes at each level are distinct from the primes at other levels by their exact orders. Every chosen odd valuation persists upon multiplication by three because the prime is different from 3. Writing \(\operatorname{sf}(N)\) for the product of the primes of odd valuation in \(N\), one therefore has for every \(k\ge2\)
\[
 \operatorname{sf}(B_{3^k})\ \ge\
  \prod_{j=2}^k 2(3^j)^4
     =2^{k-1}3^{2k(k+1)-4}.
\]
This also shows that a powerful term at one of these levels would have at least \(3(k-1)\) different prime divisors of odd valuation at least three.
