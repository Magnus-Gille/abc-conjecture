# A logarithmic prime cutoff on the orbit of the mixed norm seed \((7,4)\)

Let \(Y=s^2+2t^2\), \(U_-=(s-t)^2+t^2\), \(H=\max(|s|,t)\) and \(R=\operatorname{rad}(|2st(s^8-16t^8)|)\). There are constants \(c,\eta>0\) and infinitely many primitive signed pairs with \(s\) odd, \(t>0\) even and \(H\to\infty\) such that

* \(Y\) and \(U_-\) are both integer squares.
* The only prime divisor of \(Y\) at most \(c(\log H)\log\log H\) is 3, and \(v_3(Y)=4\).
* \(R\ll H^8/(\log H)^\eta\).

The signed slope keeps the same quadratic factor \(U_-\) throughout. If positive coordinates are wanted, taking \(|s|\) preserves \(Y,H,R\) and makes one of \((|s|-t)^2+t^2\) and \((|s|+t)^2+t^2\) a square. The argument controls the smallest new prime of \(Y\). Its exponent at a new prime can still be two.

## The orbit and its height

The genus-one curve and its seed are
\[
 C:\ y^2=(x^2+2)((x-1)^2+1),\qquad P=(7/4,45/16).
\]
At the seed, \(Y=81\) and \(U_-=25\). Write \(\iota(x,y)=(x,-y)\). A rational elliptic model is \(E:v^2=u^3-8u^2+8u\), with discriminant \(2^{15}\) and \(j=8000\). The formulas
\[
 u=2(y+x^2-x+2),\qquad v=2(u-1)x-u,\qquad x=\frac{v+u}{2(u-1)}
\]
give inverse birational changes on their domains, with \(y=u/2-x^2+x-2\), and identify the smooth projective curves. On \(E\), write \(A=(1,1)\). Then \(P=(49/4,217/8)=2A\) and \(\iota P=(1,-1)=-A\). The point \(T=P-\iota P=3A\) has \(u(T)=289/2025=(17/45)^2\). It is nonzero in the kernel of reduction at the good prime 3 and has infinite order, since the formal logarithm there is injective on that kernel over \(\mathbb Q_3\).

For signed odd \(m\) set \(P_m=P+[(m-1)/2]T=[(3m+1)/2]A\). Take any branch point \(W\) of \(x:C\to\mathbb P^1\) as elliptic origin over a fixed number field. The involution is then negation, so \(T=2(P-W)\) and \(P_m-W=[m](P-W)\). The slope \(x\) is the degree-two quotient by negation and thus differs from a Weierstrass abscissa by a fixed fractional linear change. Comparison with the canonical height gives
\[
 h(x(P_m))=2m^2\widehat h(P-W)+O(1)=\tfrac12m^2\widehat h(T)+O(1).
\]
Zero and infinite slopes occur only finitely often. At other indices normalize \(x(P_m)=s/t\) to a primitive pair with \(t>0\), so \(h(x(P_m))=\log H\).

## The factor at 2 and the two squares

At \(2A=(49/4,217/8)\) the formal parameter \(z=-u/v\) on \(E\) has \(v_2(z)=1\). On the formal group of this integral model, multiplication by an odd integer preserves positive depth \(v_2(z)\). Doubling raises it by exactly one, since \([2]z=2z-a_1z^2+O(z^3)\) with integral coefficients and \(a_1=0\). Consequently for every nonzero even \(k\) the point \(kA\) has depth \(h=v_2(k)\). Its coordinates have valuations \(v_2(u)=-2h,\ v_2(v)=-3h\). By the inverse slope formula \(v_2(x)=-h-1\).

In particular for an odd prime \(\ell\equiv5\bmod8\), \(k=(3\ell+1)/2\) is even and the primitive coordinates at \(P_\ell\) satisfy \(s\) odd and \(v_2(t)=v_2(3\ell+1)\). The integer norms \(Y,U_-\) are odd and coprime, since their difference is \(2st\) and an odd common prime cannot divide either primitive coordinate. Their product equals \((yt^2)^2\) by the curve equation. A rational square root of an integer is integral, so each norm is an integer square.

## The restriction at a new prime

Let \(\ell>5\) be a prime congruent to 5 modulo 8. If \(p\mid Y\), primitivity and parity give \(p\nmid 2t\), and \(-2\) is a nonzero square modulo \(p\). Thus \(p\) splits in \(K=\mathbb Q(\sqrt{-2})\), while \(\ell\) is inert, so \(p\ne\ell\).

At \(p=3\) the seed meets the branch \(W\) above the root of \(x^2+2\) congruent to \(7/4\). The root lifts to \(\mathbb Q_3\) by Hensel's lemma. In the smooth integral model, \(y\) is a local parameter at this branch, and the difference of the slope from its root has twice its valuation. Multiplication by \(\ell\) preserves the formal depth of \(P-W\) at 3, as \(3\nmid\ell\). The denominator of the slope remains a 3-adic unit in this branch neighborhood. Hence \(v_3(Y)=4\) at index \(\ell\).

For \(p\ne3\), the reduction of \(P_\ell\) is a branch point and \([\ell]T=P_\ell-\iota P_\ell\) reduces to the identity. These reduction statements use good reduction at odd primes. The two monic quadratics have discriminants \(-8,-4\) and resultant 8, and the quartic double cover is smooth also at infinity in odd characteristic. From the reduced fraction for \(u(T)\), the only odd primes where \(T\) reduces to the identity are 3 and 5. The prime 5 is inert in \(K\). Hence at every new \(p\mid Y\) the reduction of \(T\) has order exactly \(\ell\).

The curve \(E\) has complex multiplication by \(\mathcal O_K=\mathbb Z[\sqrt{-2}]\), all defined over \(K\). Indeed the quotient by \((0,0)\) has model \(v^2=u^3+16u^2+32u\), the quadratic twist by \(-2\) of \(E\). Composing the quotient isogeny with the twist isomorphism over \(K\) gives a degree-two endomorphism negated by complex conjugation. Its multiplier on the complex uniformization is purely imaginary, of absolute square two, so its square is \(-2\). It generates the maximal order.

At the split prime \(p\), these endomorphisms act over \(\mathbb F_p\). Because \(\ell\) is inert, \(\mathcal O_K/\ell\mathcal O_K\) is the field of order \(\ell^2\). Its action on \(E[\ell]\) makes \(E[\ell]\) a one-dimensional vector space over that field. The \(\mathcal O_K\)-multiples of the nonzero reduction of \(T\) therefore give all of \(E[\ell]\) as \(\mathbb F_p\)-points. Frobenius at \(p\) commutes with \(\mathcal O_K\) and belongs to \(\mathcal O_K\). Indeed the centralizer of \(K\) in the geometric endomorphism algebra is \(K\), also in the quaternion case, and Frobenius is integral. Write Frobenius as \(\pi\), of norm \(p\). The endomorphism \(\pi-1\) kills the full \(\ell\)-torsion, so it factors through \([\ell]\) on the reduction. Its quotient by \(\ell\) is an integral endomorphism in \(K\), hence lies in \(\mathcal O_K\). Consequently for some \(a,b\in\mathbb Z\),
\[
       p=(1+a\ell)^2+2b^2\ell^2.
\]
Here \(b\ne0\) since \(p\) is prime, and \(a\) is even since \(p\) and \(\ell\) are odd. In particular \(p\ge2\ell^2+1\) at every such index.

## Forcing the small Frobenius norms to be composite

For an integer \(J\ge4\), let \(D_J\) be the product of the odd primes up to \(10(J+1)\). Put \(n=J\). Choose the least positive prime \(\ell\) satisfying
\[
          \ell\equiv-1\bmod D_J,\qquad 3\ell+1\equiv0\bmod 2^n .
\]
The Chinese remainder theorem gives one reduced class modulo \(2^n D_J\), and the second congruence gives \(\ell\equiv5\bmod8\). Since \(\ell\ge D_J-1\), these primes are unbounded. Linnik's theorem bounds \(\ell\ll(2^nD_J)^L\) for an absolute exponent \(L\). Chebyshev's bound on the sum of \(\log q\) over primes \(q\le10(J+1)\) gives \(\log\ell\ll J\). [Heath-Brown, *Zero-free regions for Dirichlet L-functions, and the least prime in an arithmetic progression*](https://doi.org/10.1112/plms/s3-64.2.265)

Suppose a new prime \(p\mid Y\) satisfied \(p\le J\ell^2\). The Frobenius norm gives \(|a|\le\sqrt J+1/\ell\) and \(2b^2\le J\). The integer
\[
      h_0=(1-a)^2+2b^2
\]
is odd, at least 3 and at most \(10(J+1)\). Choose a prime \(q\mid h_0\). Then \(q\mid D_J\), and \(\ell\equiv-1\bmod q\) makes \(p\equiv h_0\equiv0\bmod q\). But \(q\le10(J+1)<2\ell^2+1\le p\) for sufficiently large \(J\), by the growth of the primorial \(D_J\). This excludes every new prime \(p\le J\ell^2\).

The height formula and \(\log\ell\ll J\) now give \(J\ell^2\ge c(\log H)\log\log H\) with a fixed \(c>0\). The radical is supported on the six factors \(s,t,s^2-2t^2,Y,U_-,(s+t)^2+t^2\). In the factor \(t\), the congruence at 2 gives \(\operatorname{rad}(t)\le 2^{1-n}t\). The two square norms have radicals \(O(H)\) each, and the other quadratic factors have absolute values \(O(H^2)\). Thus \(R\ll 2^{-n}H^8\), and \(2^n\gg(\log H)^\eta\) for some \(\eta>0\).

The only contribution to \(\log Y\) from primes in the cutoff is \(4\log 3\), whereas \(Y\asymp H^2\). A positive proportion of \(\log Y\) in exponents above two at the new primes would give a fixed-power saving in the octic radical. Their exponents remain undetermined here.
