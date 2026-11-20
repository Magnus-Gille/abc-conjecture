# Odd valuations in every dyadic packet

Write \(w_n=d_n W_n^2\) with \(d_n\) positive and squarefree. The initial dyadic point has \((u_4,v_4,w_4)=(1,1,7)\). All dyadic triples satisfy
\[
       w_n^2=u_n^4+16u_n^2 v_n^2+32 v_n^4,\qquad u_n,v_n,w_n>0.
\]
Then \(d_n>1\) for every dyadic \(n\ge4\). In fact \(d_n\) is a congruent number: it is the area of a right triangle with rational sides. A second elliptic twist \(y^2=x^3+2d_n^2x\) also has positive rank.

## Rational points on the quartic

The smooth plane quartic \(W^4=U^4+16U^2V^2+32V^4\) has exactly two points in \(\mathbf P^2(\mathbf Q)\), namely \([U:V:W]=[1:0:1],[1:0:-1]\).

More generally let \(d>0\), and assume that
\[
     d^2W^4=U^4+16U^2V^2+32V^4.
\]
Adding \(U^4\) gives \(d^2W^4+U^4=2(U^2+4V^2)^2\). If \(U,V,W\ne0\), put \(z=W/U\) and \(t=1+4(V/U)^2>1\). Then \(d^2z^4+1=2t^2\). The following point lies on \(E_d:y^2=x^3-d^2 x\):
\[
       x=(t/z)^2,\qquad y=t(t^2-1)/z^3 .
\]
Indeed \(x\pm d=(dz^2\pm1)^2/(2z^2)\), and multiplying the three factors \(x,x-d,x+d\) gives \(y^2\). The ordinate is nonzero since \(t>1\). Thus the positive rational lengths
\[
       (x^2-d^2)/|y|,\qquad 2dx/|y|,\qquad (x^2+d^2)/|y|
\]
give a right triangle of area \(d\). Here \(x>d\) since \(dz^2=1\) would force \(t=1\). This also specifies the two-descent class of the point: \(x\) is a square, and \(x-d,x+d\) are twice squares.

When \(d=1\), this triangle contradicts Fermat's right-triangle theorem, proved below. On the coordinate axes, \(W=0\) is impossible by positivity unless \(U=V=0\); and \(U=0\) would give \((W/V)^4=32\), impossible by its 2-adic valuation. At \(V=0\) one obtains precisely the displayed points. Thus no \(w_n\) can be a square. More generally the same triangle excludes every twist by a noncongruent positive squarefree \(d\) at \(UVW\ne0\).

### Fermat's descent

If a rational right triangle has square area, clearing denominators produces an integral one with square area. Dividing by the gcd of the sides preserves this property (an integer which is a rational square is an integer square). Choose such a triangle of smallest integral hypotenuse and parametrize its legs by \(2mn,m^2-n^2\), with \(m>n\) coprime and of opposite parity. The area \(mn(m-n)(m+n)\) is a square. These four positive factors are pairwise coprime; for the two odd factors \(m-n,m+n\), their gcd divides 2. Hence
\[
        m=a^2,\qquad n=b^2,\qquad m+n=c^2,\qquad m-n=e^2.
\]
Set \(h=(c+e)/2\), \(k=(c-e)/2\). The positive integers \(h,k\) satisfy \(h^2+k^2=a^2\) and \(2hk=b^2\). Since \(b\) is even, the new right triangle has integral square area \(hk/2=(b/2)^2\). Its hypotenuse \(a\) is smaller than \(m^2+n^2\), contradicting minimality.

## A second elliptic quotient and the size of the parity kernel

The other sign quotient results from
\[
    d^2 W^4+32V^4=(U^2+8V^2)^2 .
\]
For \(V\ne0\) it gives
\[
     x=\left(\frac{dW}{2V}\right)^2,\qquad
     y=\frac{d^2W(U^2+8V^2)}{8V^3},\qquad y^2=x^3+2d^2x.
\]
For a dyadic triple \(w_n,d_n,W_n\) are odd and \(v_n\) is integral. The abscissa has negative valuation at 2, so the Nagell–Lutz theorem makes this point nontorsion. The congruent-number point on the first curve likewise has infinite order for these kernels. For \(n\ge8\) every prime dividing \(d_n\) is \(1\bmod8\), so the curve has good reduction at 3 and 7, with respectively 4 and 8 points. Indeed the values of \(x^3-d_n^2x\) at \(x,-x\) cancel in the quadratic character sum for primes \(3\bmod4\). The torsion order divides 4 by prime-to-characteristic reduction at these two primes. All four rational points of order dividing two are already accounted for, and the displayed point has nonzero ordinate. For \(n=4\), \(d_4=7\); use good primes 3 and 19 with group orders 4 and 20 in the same argument.

For \(n\ge8\), every prime divisor of \(w_n\) first appears at the odd family index \(n-1\), satisfies \(p\ge8n^2+1\), and occurs at both neighbours \(n-1,n+1\) at precisely its exponent in \(w_n\). Thus each pair of neighbouring slopes has a common new prime of odd valuation, and
\[
      d_n\ge8n^2+1 .
\]
The \(d_n\), \(n\ge8\), are consequently pairwise coprime, using disjointness of the dyadic packet supports. In particular one obtains infinitely many squarefree \(d\), all of whose prime divisors are \(1\bmod8\), for which both explicit elliptic curves above have positive rank. Odd valuations may exceed 1. This proof gives no constant upper bound for the odd valuation obtained. [Dyadic reduction and prime bound](abc_octic_dyadic_fermat_audit.md)

## Fixed higher powers and bounded exponents

No dyadic packet is a cube either. At \(n=8\) one has \(u_8=31\equiv3\bmod7\), \(v_8=14\), and \(3\) has multiplicative order 6 modulo 7. In all subsequent doublings \(7\mid v_n\) persists, \(u_{2n}\equiv\pm u_n^4\bmod7\), and \(w_{2n}\equiv u_n^8\bmod7\). The quotient of \(\mathbf F_7^\times\) by cubes has order 3, so \(-1\) is a cube and powers 4 and 8 preserve nontrivial classes. Thus \(w_{2n}\) is a noncube for every \(n\ge8\). The initial packets \(w_4=7\) and \(w_8=2273\equiv5\bmod7\) are noncubes as well.

The duplication identity \(w_{2n}=w_n^4-2(8u_n^2v_n^2)^2\) gives
\[
               w_{2n}=w_n^4-8(2u_nv_n)^4,\qquad \gcd(w_n,2u_nv_n)=1.
\]
Fix an integer \(q\ge3\). If \(w_{2n}=Z^q\), this supplies a primitive nonzero solution of \(X^4-8Y^4=Z^q\). Since \(1/4+1/4+1/q<1\), the generalized Fermat finiteness theorem of Darmon and Granville gives finitely many such triples with these fixed coefficients and exponents. The positive sequence \(v_n\) grows strictly under \(v_{2n}=2u_nv_nw_n\), so bounded \(Y=2u_nv_n\) permits only finitely many \(n\). Thus only finitely many dyadic packets are \(q\)-th powers. This argument supplies no effective bound on the exceptions for odd \(q\). [Darmon and Granville, *On the equations \(z^m=F(x,y)\) and \(Ax^p+By^q=Cz^r\)*](https://doi.org/10.1112/blms/27.6.513)

For every fixed \(B\), all sufficiently late packets have valuation gcd divisible by none of the primes \(\le B\), by taking a finite union over these exponents. Hence, if a sufficiently late packet is a prime power \(p^e\) with \(e\le B\), then \(e=1\). For fixed \(q\ge2\), its \(q\)-power-free part \(\prod_{p\mid w_n}p^{v_p(w_n)\bmod q}\) is at least \(8n^2+1\) for all sufficiently late \(n\). When \(2\mid q\) or \(3\mid q\), the explicit arguments give this bound for every \(n\ge8\).
