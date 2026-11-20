# Square and nearly square denominators on the full quartic signature

Let \(a^4+3b^2=4w^4\) be primitive, and index the positive solutions up to sign by the positive odd integers. Write \(d_n=\operatorname{sf}(w_n)\) for the product of the primes occurring to odd exponent. The four least values that occur anywhere on this orbit, in increasing order, are exactly
\[
  1,\qquad 37,\qquad 40573=13\cdot3121,\qquad
  2005752169=14281\cdot140449.
\]
They occur at \(n=1,3,5,7\), respectively, with \(w_n=d_n\) in each case. At every other index having a cofactor this small, the largest prime factor \(q\) of \(n\) must itself give an **exact square** \(w_q\) and satisfy
\[
 q\equiv\pm1\pmod M,\qquad
 M=2035433130100664667454667191389711157017292886782476011604079828416000.
\]
In particular \(q\ge M-1\). Every index of an exact square, including composite indices, satisfies the same congruence modulo \(M\). The independent quadratic-field elliptic Chabauty argument excludes every prime-index square. Consequently the four displayed values are attained only at their four displayed indices. [Exact square classification](abc_full_quartic_square_chabauty.md) [Full parametrization](abc_full_quartic_signature.md) · [Standalone C++17 verifier](abc_full_quartic_square_sieve.cpp)

## The finite-field computation

On \(E:Y^2=X^3+36X^2+36X\) take \(P=(-2,8)\). At odd \(n\), write \(X(nP)=-2x^2/y^2\) with \((x,y)=1\), so \(w_n=(x^2+3y^2)/4\). For every \(p\ge5\), when \(nP\) reduces to a finite point with \(X\ne6\), the quadratic character of \(w_n\) equals
\[
 \left(\frac{8(6-X(nP))}{p}\right).
\]
This follows because \(w_n=y^2(6-X(nP))/8\) and \(y\) is a unit. If \(nP\) reduces to the identity then \(p\mid y\) and \(w_n\equiv(x/2)^2\bmod p\), a nonzero square. When \(X=6\) one can allow every squareclass in the sieve. Thus the local necessary condition for \(d_n=d\) is equality of the predicted character with \((d/p)\) at all the other residues. Reduction order \(r=\mathrm{ord}_p(P)\) is a period, and changing the sign of the index preserves every test.

For the census take \(L=2520\) and all 71 primes \(5\le p\le10000\) with \(r\mid L\). All prime factors of \(w_n\) are \(1\bmod12\): at a prime dividing \(w\), the identities \(c^2=2w^2-a^2\), \(3d'^2=2w^2+a^2\) imply that \(-1\) and 3 are squares. Test all squarefree products of such primes at most \(2005752169\), including the empty product. The exhaustive count is 37,178,200. The surviving classes are

| Squarefree part | Necessary index modulo 2520 |
|---:|---:|
| 1 | \(\pm1\) |
| 37 | \(\pm3\) |
| 40573 | \(\pm5\) |
| 2005752169 | \(\pm7\) |

The same calculation at modulus 12600 forces \(n\equiv\pm5\) for cofactor 40573. At modulus 17640 it forces \(n\equiv\pm7\) for cofactor 2005752169. These moduli include \(25\) and \(49\), respectively. To check the least nonsquare cofactor by hand, the only candidate between 1 and 37 is 13. On \(E_6:Y^2=X^3-36X\) the point \(G=(-3,9)\) has order 5 modulo 13, forcing \(5\mid n\) if \(13\mid w_n=B(nG)\). But \(X(5P)=-2(323/139)^2\), so \(5P\) reduces to \((0,0)\) modulo 17. The same holds for every odd multiple of \(5P\). There \((w_n/17)=(3/17)=-1\), whereas \((13/17)=1\).

For the larger modulus in the square case, first reduce modulo 24. The tests at \(p=5,23,577\) already leave precisely \(\pm1\). Change the sign of \(n\) so that \(n\equiv1\) modulo the current modulus \(m\). For a prime \(\ell\), take all auxiliary primes with \(r/\gcd(r,m)=\ell\) and test \(n=1+km\), \(1\le k<\ell\). When every nonzero \(k\) fails at some auxiliary prime, the residue lifts to \(1\bmod m\ell\). Distinct productive primes in the same round may be adjoined together. With auxiliary primes up to 10000, six rounds give the displayed \(M\). This lifting step iterates the same type of character sieve previously used on a different elliptic orbit. [Earlier denominator-character method](abc_octic_mixed_denominator_characters.md)

The verifier computes group periods by affine addition from \(P\), including the identity as the initial residue. In the cofactor census, it enumerates all products using primes up to the square root of the cutoff and then all products with one larger prime by a segmented sieve. These parts are disjoint. The first twelve character tests at primes other than \(1\bmod12\) group the index classes by sign, which speeds up the exhaustive computation. It independently recomputes every character used in the lifting and census. Compile with \(\texttt{g++ -std=c++17 -O3}\). A smaller optional bound reduces the census time; the full run uses the fourth value as the default cutoff.

## Largest prime factor of the index

Suppose \(q\) is the largest prime factor of an odd \(n>1\). Every \(p\mid w_q\) is at least 5 and has exact reduction order \(q\) for \(G\). Indeed \(w_q=B(qG)\), \(q\) is prime, and \(G\) is integral. There are four rational points of order dividing 2, so \(4q\mid\#E_6(\mathbf F_p)\). Hasse's bound gives \(p\ge(2\sqrt q-1)^2>q\). Thus \(p\nmid n\) and its formal depth is unchanged on passage from \(qG\) to \(nG\). In particular
\[
                    \operatorname{sf}(w_q)\mid d_n.
\]
This proves that a nontrivial square anywhere implies a square already at a prime index.

Every prime of each of the three nontrivial listed cofactors has exact order equal to its original index \(3,5,7\), respectively. Therefore if \(d_n\) is among the four listed values and \(q\) differs from its original index, \(w_q\) is square. If \(q\) equals that small prime, the census congruences exclude every smaller prime divisor of \(n\) and the refined moduli force \(v_q(n)=1\). This gives exactly its original index.

For any odd \(n>1\) whose largest prime factor \(q\) lies outside the two classes \(\pm1\bmod M\), the same argument gives the effective bound
\[
                    d_n\ge(2\sqrt q-1)^2.
\]
There is a quadratic improvement when \(q\equiv3\bmod4\), \(q\ge7\). A witnessing odd-exponent prime \(p\mid w_q\) splits in \(\mathbf Q(i)\). Its reduced point has annihilator \((q)\) as a Gaussian ideal because \(q\) is inert. Thus its Gaussian Frobenius satisfies \(\pi\equiv1\bmod q\). It also satisfies \(\pi\equiv1\bmod2\) since the full two-torsion is rational. Hence \(p=(1+2qu)^2+4q^2v^2\) with \(v\ne0\). For \(u\ne0\) this is at least \((2q-1)^2+4q^2\). For \(u=0\), the condition \(p\equiv1\bmod3\) forces \(3\mid v\). Thus
\[
                    d_n\ge 8q^2-4q+1
\]
throughout the stated inert classes. The [exact square classification](abc_full_quartic_square_chabauty.md) removes the residue-class restriction: the linear lower bound holds for every odd \(q\), and the quadratic lower bound holds for every \(q\equiv3\bmod4\), \(q\ge7\).

## The curves for a fixed squareclass

Write \(r=x/y\). For \(d_n=d\) the equations become
\[
 s^2=-2(r^4-18r^2+9),\qquad d h^2=r^2+3.
\]
The first uses \(x^4-18x^2y^2+9y^4=-8a^2\) and \(s=4a/y^2\); the second uses \(h=2\sqrt{w_n/d}/y\). Conversely the second equation at a primitive slope of the original orbit forces its indicated squareclass. The two branch sets over the \(r\)-line are disjoint, with four and two simple points. Their fiber product is a smooth genus-three curve after normalization by Riemann–Hurwitz. Faltings gives finiteness for every fixed \(d\), and hence \(d_n\to\infty\). The primes and index bounds above are effective without a complete determination of rational points.

The product cover has the genus-two quotient
\[
 Z^2=-2d(r^2+3)(r^4-18r^2+9).
\]
Its two rational elliptic quotients are both explicit. Set \(A_t:Y^2=X^3+48tX^2+288t^2X\). With \(u=r^2\) the cubic equation is \(Z^2=-2d(u+3)(u^2-18u+9)\), yielding \(X=-2d(u+3),Y=-2dZ\) on \(A_d\). The inversion \((r,Z)\mapsto(3/r,9Z/r^3)\) maps the genus-two curve at \(d\) to its twist at \(3d\), yielding the second quotient \(A_{3d}\). The two pullback differentials are proportional to \(r\,dr/Z\) and \(dr/Z\), hence independent. The genus-three Jacobian is isogenous to the product of these two curves and the Jacobian of the first quartic. The latter maps by a degree-two isogeny after choosing a rational origin to the original rank-one elliptic curve. This follows directly from \((r,s)\mapsto(-2r^2,2rs)\). The three quotients account for all dimensions.

Both \(A_d\) and \(A_{3d}\) must have positive rank for a solution. At 5 and 7 their group orders are 6 and 8 for every admissible \(d\), by direct counting on the two local twist classes (these primes do not divide \(d\)). Their torsion is therefore exactly the visible group of order two. Each quotient point above has negative nonzero abscissa. The curves \(A_1,A_3\) have rank exactly one, so the ranks of the indicated genus-three and genus-two Jacobians for the square case are exactly 3 and 2.

Here is an elementary rank certificate. On a curve \(y^2=x^3+A x^2+B x\) the two-isogeny descent uses \(N^2=e u^4+A u^2v^2+(B/e)v^4\) for signed squarefree divisors \(e\) of \(B\), and the dual coefficients \((-2A,A^2-4B)\). For \(t=1,3\) the only prime classes are 2 and 3. At \(t=1\), for \(3\mid e\) the right hand side divided by 3 is nonzero modulo 3 for every primitive pair. If just one of \(u,v\) is a unit this is immediate, and when both are units the first and last terms cancel while the middle term is 1 modulo 3 on both curves. At \(t=3\), if \(3\nmid u\) the valuation is 1, and if \(3\mid u\) it is 3. Thus the class 3 cannot occur in either descent image. The original image contains \(2\) from torsion and \(-2\) from negative abscissas at the seed \(r=1\) and its inverse \(r'=3\). The dual cubic is negative at negative abscissas, so its positive image has only \(1,2\), both attained. The rank formula gives \(2^{\mathrm{rank}}=4\cdot2/4=2\). The equality of rank and genus on both curves explains why the classical rank-less-than-genus Chabauty criterion does not settle the remaining square case.
