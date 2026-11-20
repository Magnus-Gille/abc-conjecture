# Two square arms in the primitive quartic family

Let \(a,w>0\) and \(b\in\mathbf Z\) satisfy
\[
  a^4+3b^2=4w^4,\qquad \gcd(a,b,w)=1.
\]
Define the positive integers \(c,d\) by \(c^2=2w^2-a^2\) and \(3d^2=2w^2+a^2\), as justified below. **The arms \(a\) and \(c\) are both squares exactly when \((a,b,w)=(1,\pm1,1)\).** In particular, requiring \(a,c,d\) all to be squares gives the same two solutions.

## The two factors of \(3b^2\)

The integers \(a,w\) are coprime. A prime dividing both has fourth power dividing \(3b^2\), so divides \(b\) as well. Reduction modulo 3 then gives \(3\nmid aw\). Reduction modulo 4 shows that \(a,b\) have the same parity. If both were even, \(w\) would be odd, and the left side modulo 16 would be 0 or 12 while the right side would be 4. If \(a,b\) are odd, the left side is 4 or 12 modulo 16 and hence \(w\) is odd.

Now \((2w^2-a^2)(2w^2+a^2)=3b^2\). The first factor is positive since \(a^4\le 4w^4\) and \(a^2=2w^2\) is impossible. The two odd factors are coprime since a common prime would divide both their sum \(4w^2\) and their difference \(2a^2\). Only the second is divisible by 3. Taking prime valuations gives unique positive \(c,d\) as above, with \(|b|=cd\).

## A rank-zero elliptic curve

Write \(a=A^2\), \(c=C^2\) with \(A,C>0\). Then \(A^4+C^4=2w^2\). Setting \(u=C/A\), \(v=2w/A^2\) gives \(v^2=2(u^4+1)\), so
\[
 (X,Y)=(2u^2,2uv)\in E'(\mathbf Q),\qquad E'\colon Y^2=X^3+4X.
\]

Apply the standard rational 2-isogeny descent to \(E\colon y^2=x^3-x\) and its quotient \(E'\) by \(\{O,(0,0)\}\). On a curve \(y^2=x^3+kx\) the descent map \(\alpha\) takes a point with \(x\ne0\) to the squareclass of \(x\), takes \((0,0)\) to the class of \(k\), and takes \(O\) to 1. At a prime \(p\nmid k\), a positive valuation of \(x\) gives \(2v_p(y)=v_p(x)\), and a negative valuation gives \(2v_p(y)=3v_p(x)\). Thus the image on \(E\) is contained in \(\{1,-1\}\), both attained at \(O,(0,0)\). On \(E'\) every nonzero rational abscissa is positive, so the only possible classes are 1 and 2, both attained at \(O,(2,4)\). The two-isogeny rank formula gives
\[
 2^{\operatorname{rank} E'(\mathbf Q)}
 =|\alpha(E(\mathbf Q))|\,|\alpha(E'(\mathbf Q))|/4=1.
\]

At the good primes 3 and 7 the orders of \(E'(\mathbf F_p)\) are 4 and 8. Indeed \(-1\) is a nonsquare at both primes, so the quadratic characters of \(X^3+4X\) cancel in pairs \(X,-X\). Reduction injects torsion of order prime to \(p\). The two orders together exclude odd torsion and bound the 2-primary part by four. Thus \(E'(\mathbf Q)=\{O,(0,0),(2,4),(2,-4)\}\).

Since \(X=2u^2>0\), we obtain \(u=1\), hence \(C=A\) and \(w=A^2=a\). Coprimality forces \(a=w=1\), giving \(c=d=1\) and \(b=\pm1\). Both signs satisfy the defining equation.

In the odd-index notation \(nG=(-3a^2/w^2,9ab/w^3)\) on \(y^2=x^3-36x\), with \(G=(-3,9)\), the two solutions are exactly \(n=\pm1\). Indeed they give \(nG=\pm G\), and \(G\) has infinite order since \(x(2G)=25/4\) and rational torsion has integral coordinates by the Nagell–Lutz theorem.
