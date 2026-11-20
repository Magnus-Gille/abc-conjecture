# Repeated ninth-order factors in rational maps

Let \(F(T)=T^6+T^3+1\). For every integer \(e\ge2\), there is an effectively constructible rational function over \(\mathbf Q\), of degree \(d\) between \(3e-2\) and \(3e\), fixing each root \(\zeta\) of \(F\) with ramification index at least \(e\). If \((P,Q)\) are its coprime homogeneous coordinates, then
\[
                    F(X,Y)^e\mid\Phi_9(P(X,Y),Q(X,Y)).
\]
Here \(F(X,Y)=\Phi_9(X,Y)\). The forced loss of \(6(e-1)\) in the degree of the radical of the right-hand form comes within four of the total ramification \(2d-2\). The construction applies to any separable irreducible sextic, with its own homogenization substituted for \(\Phi_9\).

## Interpolation and cancellation

Impose the rational linear conditions
\[
              P^{(j)}(T)-TQ^{(j)}(T)\equiv0\bmod F(T),\qquad 0\le j<e ,
\]
initially on polynomials of degree at most \(3e\). There are at most \(6e\) scalar conditions and \(6e+2\) coefficients. At each root \(\zeta\) these say that \(P(T)-\zeta Q(T)\) vanishes there to order at least \(e\). The derivative in the displayed condition applies to \(Q\) alone.

A nonzero solution cannot have \(F\) dividing both coordinates. If their common divisor contains \(F^j\) with \(j\ge1\) maximal, \(j<e\) by the degree bound. After cancellation the map still fixes all six roots with index at least \(e-j\), and has degree at most \(3e-6j\). The remaining coordinates cannot vanish at just one of the roots without vanishing at all, by irreducibility. In particular the resulting map is nonconstant. Riemann–Hurwitz would give \(3(e-j)-2\le3e-6j\), impossible for \(j\ge1\). A zero coordinate would force the other to be divisible by \(F^e\), likewise impossible. Additional common factors that are coprime to \(F\) can be canceled. This proves the claim, including \(d\ge3e-2\).

One may prescribe any nonempty open interval for positive output ratios, allowing degree at most \(3e+2\). The solution space at that degree has dimension at least six. If all its pairs represented a single fraction, they would be polynomial multiples of one coprime representative of degree at least \(3e-2\), a space of dimension at most five. Choose two genuinely different solutions, one with no \(F\)-cancellation from the smaller degree bound. At a positive rational input where their determinant is nonzero, their linear combinations realize every rational target ratio. Avoiding at most one target for which the combination vanishes identically modulo \(F\), choose a ratio in the desired interval. After canceling common factors the map has degree \(3e-2\le d\le3e+2\) and the stipulated contact at the sixth-degree orbit.

## An integral specialization

For every \(\delta>0\) and every prescribed interval \(I\subset(0,1)\) with nonempty interior, there are infinitely many positive coprime pairs \(B<A\), \(B/A\in I\), for which
\[
  \prod_{\substack{c_\delta\log A<p<A^\delta\\p\mid\Phi_9(A,B)}}
                         p^{v_p(\Phi_9(A,B))-1} \ \ge A^{2-\delta}.
\]
One obtains this directly from the polynomial identity, without factoring an integer value. Choose \(e\) so large that \(6(e-1)/(3e+2)>2-\delta\) and \(6/(3e-2)<\delta\). Prescribe \(P/Q\) near a positive reduced ratio \(\rho>1\) with \(1/\rho\in I\), as in the preceding paragraph, at a positive reduced input \(a/b\). Evaluate at the primitive pairs \((x,y)=(aM+1,bM)\) with \(M=b\prod_{p\le Z}p\), as \(Z\to\infty\). They approach \(a/b\), and \(F(x,y)\asymp M^6\); every prime divisor of this value exceeds \(Z\). The normalized output height satisfies \(A\asymp M^d\), since the common divisor of the integral homogeneous coordinates divides a fixed resultant. Choosing the common sign makes the output positive. By the prime number theorem \(Z\sim (\log A)/d\), while every prime of \(F(x,y)\) is \(O(M^6)<A^\delta\). For all large \(Z\) these primes avoid the fixed exceptional primes of the map. Their contribution to the repeated part of \(\Phi_9(A,B)\) is at least \(F(x,y)^{e-1}\), proving the estimate. An independent lattice construction places the whole contribution inside a single dyadic interval. [Moving-prime construction](abc_cyclotomic_moving_packet.md)

## Degree eight with all critical values in the power-triple boundary

A different interpolation, sending \(\zeta\) to \(\zeta^4\), gives the explicit map
\[
 f(T)=\frac{P(T)}{Q(T)}
      =-\frac{5T^6+8T^3+2}{T^2(2T^6+8T^3+5)} .
\]
Its affine Wronskian is \(P'Q-PQ'=20T F(T)^2\), the resultant of the two affine polynomials is \(-9841500\), and \(P-T^4Q\equiv0\bmod F\). Thus the six primitive ninth roots have local degree three, and \(0,\infty\) have local degree two and exchange places. These account for all \(14\) units of ramification. In particular \(F^3\mid\Phi_9(P,Q)\). On \(0<t<1\) the function increases from \(-\infty\) to \(f(1)=-1\). The two additional critical values make it possible to retain an equivalence with general rational abc while forcing large repeated factors in a single sextic. [Positive eighteenth-power family](abc_cyclotomic_small_repeats_transfer.md)
