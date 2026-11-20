# Perfect-power obstructions at one exact dyadic rank and at adjacent CM packets

Let \(n\ge4\) range through powers of two, using \((u,v,w)=(u_n,v_n,w_n)\) from the dyadic octic construction. The initial triple is \((1,1,7)\), its factors are pairwise coprime, and \(w_{2n}=w_n^4-128(uv)^4\). Then
\[
 \gcd\{ v_p(w_nw_{2n}):p\mid w_nw_{2n}\}=1
\]
at every such index. This puts a uniform obstruction on the entire two packets while allowing different exponents at different primes of either individual packet. Equivalently their product is never a proper perfect power. The same holds for the odd part of the denominator quotient \(B_{2n}(R)/B_{n/2}(R)\), where \(B_m(R)\) is the positive square root of the rational abscissa denominator of \([m]R\) on \(E':y^2=x^3+16x^2+32x\), \(R=(-8,16)\). Indeed \(B_{n/2}(R)=v_n\) and the recursion gives \(B_{2n}(R)/B_{n/2}(R)=4u_nw_nu_{2n}w_{2n}\). The prime supports of \(w_n,w_{2n}\) are disjoint from the other factors by the coprimalities in the recursion and the different reduction orders. [Dyadic recurrence and first occurrences](abc_octic_dyadic_fermat_audit.md)

A second statement isolates one ordinary reduction order. For every dyadic \(n\ge4\),
\[
   \gcd\{v_p(u_nw_n):p\mid u_nw_n\}=1 .
\]
In fact \(u_nw_n\) is exactly the product of odd primes of ordinary reduction order \(n\), each raised to its formal depth at the first multiple of \(R\) reducing to the identity. Equivalently it is the odd part of \(B_n(R)/B_{n/2}(R)\). The two conclusions allow all prime depths to exceed one if the collection of exponents has gcd one.

## A level-256 obstruction for all primes above 37

Assume a prime \(q\) divides every prime exponent of \(w_nw_{2n}\). The factors are coprime, so write \(w_n=z^q, w_{2n}=t^q\), where \(z,t\) are odd, positive and coprime. Set \(X=z^4,\ Y=t,\ Z=8u_n^2v_n^2\), obtaining
\[
                    X^q-Y^q=2 Z^2 .
\]
The pair \(XY\) is coprime to \(Z\), and \(Y>1\). For \(q>37\) use the rational Frey curve
\[
 F:y^2=x^3+4Zx^2+2X^q x,\qquad
 \Delta_F=-2^9X^{2q}Y^q .
\]
At an odd prime dividing \(XY\), \(c_4=16((4Z)^2-6X^q)\) is a unit, so reduction is minimal multiplicative and the minimal discriminant valuation is divisible by \(q\). All other odd primes are good. Existence of a multiplicative prime implies \(F\) is non-CM.

At 2 the model is minimal because the discriminant has valuation nine. The singular point and its tangent are already at the origin. In Tate's algorithm \(a_6=0\) and \(v_2(b_8)=v_2(-a_4^2)=2\) give type III. Ogg's formula therefore gives conductor exponent eight. The valuation of \(c_4\) is five, hence the curve is potentially good at 2. Its finite inertia image at 2 has order dividing 24, so its conductor exponent is preserved by reduction modulo \(q>37\). At the characteristic \(q\) the representation is finite flat, including the multiplicative case since \(q\mid v_q(\Delta_{\min})\). Lemos's uniformity theorem applies to the non-CM curve \(F\) with its rational cyclic two-isogeny, giving surjective mod-\(q\) image. Modularity and weight-two level lowering thus give a newform of exact level 256 and trivial character. The possible orders of characters modulo 256 are powers of two and reduction cannot erase a nontrivial one here. [Lemos, arXiv:1702.01985](https://arxiv.org/abs/1702.01985) · [Details of the weight-two level-lowering criterion](abc_octic_mixed_frey_bound.md)

The level-256 newspace has four rational newforms, all CM. They are the forms of \(y^2=x^3\pm2x\) and \(y^2=x^3\pm4x^2+2x\), with \(j=1728\) and \(j=8000\) respectively. The other Galois orbit is quadratic, and has \(a_3^2=8\). The rational CM forms have mod-\(q\) image contained in a Cartan normalizer, contrary to surjectivity. To exclude the quadratic orbit, reduction of \(F\) at 3 is good, since \(3\nmid w_nw_{2n}\). Its trace is in \(\{-2,0,2\}\) by rational two-torsion and Hasse. The norms of the differences between \(a_3\) and these traces are \(-4,-8,-4\). The attached verifier recomputes the full weight-two newspace and identifies the rational forms through the Sturm bound 64. Thus \(q>37\) is impossible. [Exact verifier](abc_octic_dyadic_adjacent_powers.py)

## The remaining exponents

The direct starting value \(w_4=7\) excludes every exponent at \(n=4\). For \(n\ge8\), take \(P=[n/2]R\). The rational invariant
\[
       \frac{w_{2n}}{w_n^4}
           =1-128\left(\frac{x(P)}{y(P)}\right)^4
\]
would be a rational \(q\)-th power. Each column below gives one prime \(\ell\equiv1\bmod q\) at which every possible value is a nonzero non-\(q\)-th power. The orbit is obtained by starting with \(4R\bmod\ell\) and doubling until a point repeats. All these points are affine with nonzero ordinate, so both reduction and the value of the quotient are defined. The third line is the number of different points inspected. Fermat's theorem tests the residue by raising it to \((\ell-1)/q\).

| \(q\) | 2 | 3 | 5 | 7 | 11 | 13 | 17 | 19 | 23 | 29 | 31 | 37 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(\ell\) | 3 | 13 | 11 | 29 | 23 | 53 | 103 | 571 | 47 | 59 | 311 | 149 |
| Points | 2 | 3 | 6 | 4 | 2 | 18 | 12 | 10 | 2 | 10 | 12 | 20 |

## One exact ordinary reduction order

Duplication gives \(B_n(R)/B_{n/2}(R)=2u_nw_n\). For each of its odd prime factors, the point \(P=[n/2]R\) reduces to two-torsion: it is \(J'=(0,0)\) at primes of \(u_n\), and one of the two other nonidentity two-torsion points at primes of \(w_n\). This makes the ordinary reduction order of \(R\) exactly \(n\). Conversely any prime of this order divides the doubling quotient since \(P\) is affine on the reduced curve. The exponent in the quotient equals the full first formal depth, since \(B_{n/2}\) was a unit there.

The quartic identity also gives
\[
                         w_n^2+u_n^4=2(u_n^2+4v_n^2)^2 .
\]
Suppose \(u_n w_n\) is a \(q\)-th power. The factors are coprime, so both are powers. With \(w_n=z^q,u_n=b^q\), put \(X=z^2,Y=b^4,T=u_n^2+4v_n^2\). Now \(X^q+Y^q=2T^2\). For \(n\ge8\), \(w_n>1\), and \(X,Y\) are odd, coprime and prime to 3. The latter assertion follows from the doubling recursion modulo 3 starting with nonzero \(u_4,v_4,w_4\). On \(F:y^2=x^3+4Tx^2+2X^q x\) the discriminant is now \(+2^9X^{2q}Y^q\), with every odd bad prime minimal multiplicative. The proof of type III and conductor exponent eight at 2 uses only that \(X\) is odd: \(a_6=0\), \(v_2(b_8)=2\), \(v_2(c_4)=5\), and \(v_2(\Delta)=9\). Thus the same surjectivity, level lowering, exact newform enumeration and trace at 3 exclude every \(q>37\). The initial case \(n=4\) gives \(u_4w_4=7\).

Squares are impossible because \(w_n\equiv2\bmod 3\) for \(n\ge8\). For odd \(q\le37\) use a second rational invariant. If both factors are \(q\)-th powers so is
\[
      \frac{w_n^2}{u_n^4}=1+\frac{16}{x(P)}+\frac{32}{x(P)^2}.
\]
The verifier checks each finite doubling orbit, on which the abscissa, ordinate and invariant are nonzero. It verifies the following obstructions to a \(q\)-th-power residue.

| \(q\) | 3 | 5 | 7 | 11 | 13 | 17 | 19 | 23 | 29 | 31 | 37 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(\ell\) | 67 | 71 | 113 | 23 | 79 | 103 | 419 | 47 | 59 | 5209 | 223 |
| Points | 6 | 6 | 2 | 2 | 4 | 12 | 9 | 2 | 10 | 6 | 4 |

## What follows for one packet

For every fixed integer \(q\ge3\), only finitely many \(w_n\) are \(q\)-th powers. Indeed if \(w_{2n}=z^q\), the primitive triple \((w_n,u_nv_n,z)\) solves \(X^4-128Y^4=Z^q\). Its fixed signature is hyperbolic because \(1/4+1/4+1/q<1\); the Darmon–Granville theorem applies to fixed nonzero coefficients and primitive triples. The heights of \(w_n\) tend to infinity, so finitely many such triples give finitely many indices. Squares are explicitly impossible: all \(u_n,v_n,w_n\) are nonzero modulo 3 by the recursion at \((1,1,7)\), and hence \(w_{2n}=w_n^4-128(u_nv_n)^4\equiv2\bmod3\). [Darmon and Granville, “On the equations \(z^m=F(x,y)\) and \(Ax^p+By^q=Cz^r\)”](https://doi.org/10.1112/blms/27.6.513)

Consequently any infinite set of proper-power packets would have prime exponents tending to infinity. Along it \(\log\operatorname{rad}(w_n)=o(n^2)\), so the octic triples at both \(n-1\) and \(n+1\) would have quality at least \(16/15-o(1)\). An infinite set of powerful packets, allowing coprime exponents at its different primes, would give quality at least \(32/31-o(1)\) at both neighbours, using \(\operatorname{rad}(w_n)\le w_n^{1/2}\). The separate real-quadratic Frey calculation now excludes every proper perfect power of one packet. Existence of infinitely many powerful packets with valuation gcd one remains open. [Single-packet proof](abc_octic_dyadic_single_powers.md)

The rational Frey proof above uses power exponents at both adjacent packets to remove every odd conductor prime. For a single packet the remaining signed equation has coefficient \(-128\). The published positive-coefficient theorem for \(X^4+2Y^2=Z^q\) does not cover \(w_n^4-2(8u_n^2v_n^2)^2=z^q\). [Dieulefait and Jiménez Urroz, arXiv:math/0611663](https://arxiv.org/abs/math/0611663)
