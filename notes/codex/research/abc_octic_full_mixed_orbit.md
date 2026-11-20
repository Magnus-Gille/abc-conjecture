# All primitive slopes with two specified square norms

Let \(s,t\) be coprime, with \(s\) odd and \(t>0\) even. Keep \(s\) signed. Set
\[
 Y=s^2+2t^2,\quad V=(s-t)^2+t^2,\quad D=s^2-2t^2,\quad U=(s+t)^2+t^2.
\]
Every pair for which \(Y,V\) are squares arises exactly once from a positive odd integer \(N\ge3\). The elliptic curve, point, and slope for this parametrization are
\[
 E:v^2=u^3-8u^2+8u,\quad A=(1,1),\quad Q=[(N+1)/2]A,\quad x=s/t=(v(Q)+u(Q))/(2(u(Q)-1)).
\]
The orbit with initial slope \(7/4\) and odd multiplier \(m\) has \(N=3m\). This distinction matters when a new prime divisor is identified by its first index.

## The full group and the admissible component

Here is an elementary height check of the generator. The curve and its quotient by \(J=(0,0)\) have coefficients \((a,b)=(-8,8),(16,32)\) in \(v^2=u^3+au^2+bu\). Under ordinary two-isogeny descent the abscissa squareclasses are supported only on 2, using the class of \(b\) for \(J\). On the first curve every real abscissa is nonnegative, giving at most two squareclasses. The other curve has at most four. The two-isogeny rank formula gives \(2^{r+2}\le2\cdot4\). Also \([3]A\) has abscissa \(289/2025\), so it is nonzero in the formal kernel at the good prime 3. This kernel over \(\mathbf Q_3\) is torsion-free, giving \(r=1\).

For a reduced abscissa \(u=b_0/c_0\), doubling gives the homogeneous pair
\[
 ((b_0^2-8c_0^2)^2,\ 4b_0c_0(b_0^2-8b_0c_0+8c_0^2)).
\]
The gcd is at most 64. At an odd common prime, the first equation forces \(b_0^2=8c_0^2\), and the second then forces \(b_0=2c_0\), an impossibility. At 2 the numerator has valuation zero, four or six according as \(b_0\) is odd, twice an odd number, or divisible by four. Write \(h(u)=\log\max(|b_0|,c_0)\). Real points have \(0\le u\le4-2\sqrt2<2\) or \(u\ge4+2\sqrt2>6\). On the former interval the numerator is at least \(16c_0^4\), on the latter at least \((1-8/36)^2 b_0^4\). Both homogeneous forms are at most \(68\max(|b_0|,c_0)^4\) in absolute value. The doubling limit consequently gives
\[
 h(u)-\tfrac13\log128\ \le\ 2\widehat h(P)\ \le\ h(u)+\tfrac13\log68.
\]
Use projective height zero at infinity, including for iterates landing at infinity. If \(A\) were divisible by \(k\ge2\) modulo torsion, its preimage would have \(h(u)\le (\log68)/12+(\log128)/3<\log8\). Torsion points satisfy the same bound. The abscissa denominator is a square on this integral monic model. In height at most 7 the real intervals leave \(u=0,1,7,1/4,3/4\). The last three give nonsquares, and \(u=1\) gives just \(\pm A\). Hence
\[
 E(\mathbf Q)=\mathbf Z A\oplus\{O,J\}.
\]

The quartic \(y^2=(x^2+2)((x-1)^2+1)\) has the indicated slope map on \(E\). Its involution sends \(Q\) to \(A-Q\). Translation by \(J\) sends \((u,v)\) to \((8/u,-8v/u^2)\), hence sends the slope to \(2/x\). For \(Q=nA\), one of \(n,1-n\) is even, and these two points have the same slope. For nonzero even \(k\), the local parameter \(-u/v\) at \(kA\) has depth \(v_2(k)\), since \(2A\) has depth one and the doubling series is \(2z+O(z^3)\). Thus \(v_2(x(kA))=-v_2(k)-1\). The coset \(nA+J\) has slope of positive 2-adic valuation, whereas \(nA\) has the required odd numerator and even denominator. The degenerate slopes at zero and infinity are omitted. Conversely \(Y,V\) are coprime odd integers, their difference being \(2st\). Their product is a square exactly when both are squares. Every slope in question therefore occurs, and the two points with any such slope correspond to \(N=2n-1\) and \(-N\). [Quartic model and formal parameter](abc_octic_mixed_seed_prime_orbit.md)

## Four reduction-order constraints

Let \(r_p\) be the order of \(A\) on \(E(\mathbf F_p)\) at an odd prime. Then

| Divisibility at \(p\) | Consequence |
|---|---|
| \(p\mid YV\) | \(r_p\mid N\) |
| \(p\mid D\) | \([N]A=J\pmod p\), hence \(r_p\mid 2N\) |
| \(p\mid st\) | \([N]A=\pm A\pmod p\), hence \(r_p\mid N-1\) or \(r_p\mid N+1\) |
| \(p\mid U\) | \(r_p\mid N^2+2\) |

Indeed there is an identity of rational functions
\[
 u([N]A)=\frac{D^2}{YV}.
\]
To see it, write \([N]A=2Q-A\). Its elliptic abscissa descends through \(x\), since swapping the two points over \(x\) negates \(2Q-A\). As a function of \(x\) it has simple poles at the four branch values, where \(2Q=A\). Its zeros are double, at the fixed slopes of the involution \(x\mapsto2/x\), where \(Q+J=A-Q\). At infinity it takes the value \(u(A)=1\). This proves the identity. The homogeneous numerator and denominator are coprime at all odd primes on primitive inputs, by the distinct roots of the three quadratic forms there. This gives the first three rows. The fraction is a degree-four morphism in characteristic zero, so comparison of heights also gives \(\log H=\widehat h(A)N^2/2+O(1)\), where \(H=\max(|s|,t)\). Consequently the total number of these signed pairs of height at most \(H\) is \(\tfrac12\sqrt{2\log H/\widehat h(A)}+O(1)\).

For the last row factor
\[
 2D^2+YV=U(3s^2-8st+6t^2).
\]
Over \(K=\mathbf Q(\sqrt{-2})\), the curve has the endomorphism \(\tau=\sqrt{-2}\). The 2-isogeny and the identification of its target with the \(-2\) twist give \(u(\tau A)=-(1-8+8)/2=-1/2\). At an odd \(p\mid U\), the displayed factorization gives \(u([N]A)=-1/2\). Thus \([N]A=\pm\tau A\) over the residue algebraic closure. Applying the conjugate endomorphism gives \([N^2+2]A=O\). Only the forward implication is used. [Simultaneous application to an abc triple](abc_octic_mixed_all_factors_sieve.md)
