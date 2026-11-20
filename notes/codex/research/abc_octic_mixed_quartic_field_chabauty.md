# A single elliptic Chabauty cover for the mixed fourth-power problem

For the primitive signed fourth-power and square problem \(s^2+2t_0^2=\text{fourth power}\), \((s-t_0)^2+t_0^2=\text{square}\), write \(s+t_0\sqrt{-2}=\pm(A+B\sqrt{-2})^4\) and \(u=A/B\) at finite nonzero parameters. The genus-three equations can be given as
\[
 z=u-2/u,\qquad v^2=z^2+8,\qquad w^2=F(z)=(z^2-4z-8)^2+16z^2 .
\]
Since \(s\) is odd, \(A\) is odd, and \(z=r/d=(A^2-2B^2)/(AB)\) is reduced with \(r\) odd. The seed gives \(z=-1\). All these rational parameters lift to **one** elliptic curve over the quartic field \(L=\mathbb Q(t)\), \(t^4-2t^2-1=0\), whose Mordell–Weil rank is at most two. This is strictly below \([L:\mathbb Q]=4\), the rank bound for elliptic Chabauty. [Derivation of the genus-three equations](abc_octic_mixed_fourth_power_quotients.md)

## Why there is just one twist

The field \(L\) has two real embeddings, one conjugate complex pair, and \(1/t=t^3-2t\). Take \(t>0\) at the chosen real embedding. Set
\[
  g_t(z)=(z-2(1+t))^2+4(1+1/t)^2=z^2-4(1+t)z+8(t^3+t^2-t).
\]
Direct multiplication gives \(F(z)=g_t(z)g_{-t}(z)\). Write \(g_t(r,d)=d^2g_t(r/d)\) for its homogenization. We claim \(g_t(r,d)\) is a square in \(L\).

The polynomial of \(t\) has discriminant \(-1024\), and that of \(t-1\) is \(X^4+4X^3+4X^2-2\), Eisenstein at 2. Thus the unique prime \(\mathfrak p\) above 2 has \(v_{\mathfrak p}(2)=4\), with uniformizer \(t-1\), and locally the integers are \(\mathbb Z_2[t]\). The archimedean signature gives a Minkowski bound at most \((4!/4^4)(4/\pi)\sqrt{1024}<4\). The prime above 2 is principal, since \(|N(t-1)|=2\); there is no prime of norm three, since 3 does not divide the polynomial discriminant and the polynomial has no root modulo 3. Hence \(L\) has class number one.

At an odd prime dividing \(g_t(r,d)\) the denominator \(d\) is a unit, and \(g_{-t}(r,d)\) is a unit as well: the two factors have disjoint projective roots in odd characteristic because \(F\) has discriminant supported at 2. The square \(d^4F(r/d)\) then forces an even valuation. The two real values of \(g_t(r,d)\) are positive, as both are sums of two real squares with no common zero. At \(\mathfrak p\), one has \(v_{\mathfrak p}(1+t)=1\), since \(1+t=(t-1)+2\). As \(r\) is odd, \(g_t(r,d)\equiv r^2\bmod\mathfrak p^9\). Hensel's lemma gives a local square, since \(9>2v_{\mathfrak p}(2)\). The quadratic extension obtained by adjoining a square root is consequently unramified at all finite places and split at all real places. Class number one forces that extension to be trivial by the Hilbert class field theorem.

Thus rational \(z\) from the original problem gives a point on
\[
 \mathcal E:\quad W^2=(z^2+8)g_t(z)
\]
over \(L\). At \(z=-1\), \(W=\pm3(2t^2+2t-1)\); there are also the two rational-over-\(L\) infinities.

## A split cubic model

Write \(a=1+1/t,\ b=at^2\). The elliptic model with the positive infinity as origin is
\[
          E:\quad Y^2=X(X-a)(X-b).
\]
For an explicit change of coordinates put
\[
\begin{split}
 \beta&=-2(1+t),\qquad
 \gamma=4t^3+2t^2-8t+2,\qquad
 k=-12t^3-4t^2+28t+4,\\
 U&=2(W+z^2+\beta z+\gamma),\qquad V=2Uz+\beta U-2k,\\
 X&=(U+4(1+t)^2)/16,\qquad Y=V/64.
\end{split}
\]
Substitution verifies the cubic, and \(z=(64Y-\beta U+2k)/(2U)\) recovers the slope where \(U\ne0\). For example the negative infinity has coordinates \(X=(1+t)^2/4,\ Y=k/32\): on its branch \(U\to0\) and \(Uz\to2k\). The inverse maps extend over the smooth projective models, with \(U=0\) treated by limits. In particular the slope condition is rationality of this explicit \(L\)-valued function.

## A rank bound from full 2-descent

Let \(S=\{\mathfrak p\}\). The roots \(a,b\) and their difference are \(S\)-units: \(a=(t+1)/t\) has absolute norm 2, \(t\) is a unit, and \(t^2-1=\sqrt2\). The standard full-2-torsion Kummer map \(E(L)/2E(L)\to(L^\times/L^{\times2})^2\) sends a generic point to \((X,X-a)\), using the leading nonzero value at a 2-torsion point. The two squareclasses have even valuations outside \(S\), since the three roots are distinct and integral modulo each such prime. The \(S\)-unit squareclasses have dimension four by class number one, Dirichlet unit rank two, one dyadic prime and the sign unit. This gives an ambient space of dimension eight. At each real embedding \(a,b>0\); the cubic forces \(X\ge0\) and both possible first-component classes at \(X=0\) or infinity are positive there as well. The classes of \(-1,t\) have independent sign vectors, so the remaining ambient space has dimension six.

There are two further independent local obstructions. Put \(h=t^2+t-1\), a unit of norm \(-1\). For \(d_2=t,h,th\), no local point at \(\mathfrak p\) has Kummer class \((1,d_2)\). Indeed its covering equations would require a nonzero projective solution of
\[
        Z_1^2-a Z_0^2=d_2 Z_2^2,\qquad
        Z_1^2-b Z_0^2=d_2 Z_3^2 .
\]
Normalize the coordinates in the dyadic integers with at least one unit. If \(Z_0\) is a unit, scale it to one. Otherwise reduction modulo \(\mathfrak p\) and the fact that \(d_2\) is a unit force \(Z_1\) to be a unit; scale \(Z_1\) to one. Over \(\mathbb Z_2[t]/8\) there are 4096 residues and 96 distinct squares, of which 32 are squares of nonunits. For each of the three \(d_2\), exhaustive arithmetic gives zero possibilities for the square of the free coordinate in either chart. The three classes are therefore nonzero and distinct, and their span meets the Kummer image only at zero. The remaining image has dimension at most four. Subtracting \(\dim E(L)[2]=2\) gives \(\operatorname{rank}E(L)\le2\). [Standard-library local verifier](abc_octic_mixed_quartic_field_verify.py)

## Points and saturation at small primes

Write \(P=((1+t)^2/4,k/32)\) for the negative infinity and \(H=(t^2-1,t^3-3t)\). Doubling \(H\) gives the point \(Q\) above \(z=-1,\ W=3(2t^2+2t-1)\):
\[
 Q=\left((2t^3+5t^2+2t+2)/4,\ (-5t^3-11t^2-8t-5)/8\right).
\]
The full rational torsion is \(E[2]\). At the degree-one places given by \((q,t\bmod q)=(7,2),(41,5)\), the reduced orders are 8 and 36; prime-to-residue-characteristic torsion injects, and neither residue characteristic divides the other order. All three nonzero 2-torsion points are defined over \(L\).

Let \(\Gamma=\langle P,H,E[2]\rangle\). It has rank two and index prime to every prime up to 31 in \(E(L)\). For the prime 2, evaluate the two Kummer squareclass characters modulo the two indicated degree-one places over 7. On the columns \(P,H,(0,0),(a,0)\), the rows for \(X,X-a\) are respectively \((0,1,0,1),(1,1,0,0)\) when \(t=2\), and \((0,1,0,0),(1,1,1,0)\) when \(t=5\). They are independent over \(\mathbb F_2\). The rank upper bound then makes their span all of \(E(L)/2E(L)\), proving the rank equality and 2-saturation.

For each odd prime \(\ell\le31\), two degree-one reductions give independent projection rows on \(P,Q\) after multiplication by the reduced group order divided by \(\ell\); since \(Q=2H\) this suffices for \(P,H\) as well. For example, for \(\ell=3\) the places \((41,5),(41,36)\) give \((1,1),(0,1)\). For \(\ell=11\), \((313,302),(599,261)\) give \((1,0),(1,6)\). The verifier checks each required point count and group relation. Together these prove the index assertion using only reduction at good primes. [Local descent and saturation verifier](abc_octic_mixed_quartic_field_verify.py)

If the rational-value computation restricts \(z\) to \(-1,\infty\) and the roots of \(z^2+8\), only \(-1\) can give a nondegenerate rational solution. Indeed \(z=-1\) gives \(u=1\) or \(-2\); the latter has even primitive numerator, whereas \(u=1\) yields the original pair \(\pm(7,4)\). An infinite \(z\) requires \(u=0\) or \(\infty\), in either case \(t_0=0\). The roots of \(z^2+8\) are irrational. This reduction and the rank computation alone do not exclude other residue classes; they supply the global inputs for checking them.

The calculation at 11 now gives all rational slopes. The only nondegenerate signed slope in this fourth-power case is \(7/4\). [Complete rational-point classification](abc_octic_mixed_elliptic_chabauty_11.md)
