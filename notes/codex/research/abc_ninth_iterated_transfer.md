# Two iterations force a larger repeated part in the eighteenth-order sextic

Fix \(Z\ge3\). There is an abc-equivalent family of positive triples
\(B^{18}+(A^{18}-B^{18})=A^{18}\) on which primes \(p>Z\) of exact
order 18 for \(A/B\) supply a repeated part \(\gg_Z A^{27/16}\) in
\(\Phi_{18}(A,B)\). Here a prime of valuation \(v\) supplies \(p^{v-1}\).
For any fixed \(\eta>0\) a modified family puts every prime used in the
certificate below \(A^\eta\) at all sufficiently large heights. Its
exponent is \(3/2+3/(16K)\), where \(K\) may be any positive even
integer prime to three with \(\varphi(9K)<8K\eta\). Such \(K\) exist
by taking products of primes other than three. Both bounds hold for
every member of the respective family.

## The source interval and the two heights

Write \(F(U,V)=U^6+U^3V^3+V^6\), and put
\[
 f(T)=-\frac{5T^6+8T^3+2}{T^2(2T^6+8T^3+5)} .
\]
Choose \(k\ge2\) divisible by \(p-1\) for every prime \(p\le Z\).
For coprime \(0<x\le y/2\), set
\[
 t=(x/y)^k,\qquad U/V=f(t)\quad\text{in lowest terms},\quad V>0,
 \qquad G=f((U/V)^K).
\]
Use \(K=1\) for the unrestricted prime sizes. In both cases define
\(A/B=-1/G\) in positive lowest terms. The derivative of \(f\) has
numerator \(20T F(T,1)^2\). Thus \(f(t)\le f(1/4)=-23224/3499<-2\).
On \((-\infty,-2]\), \(f\) decreases from zero to \(-43/46\) without
a pole, so \(-1<G<0\) for \(K=1\). For even \(K\), the input to the
last map is greater than one, where \(f\) increases from \(-1\) to
zero. Consequently \(A>B>0\) in both families.

The power and rational maps defining the two stages have degrees
\(8k\) and \(64kK\) as functions of \(x/y\). For a fixed rational
map, its coprime homogeneous coordinates have bounded gcd on primitive
inputs by the resultant. Their maximum absolute value on the unit
shell is bounded above and away from zero. It follows that
\[
 H=\max(|U|,V)\asymp_k y^{8k},\qquad
 A\asymp_{k,K}y^{64kK}\asymp_{k,K}H^{8K}.
\]

## Which primes contribute twice

Use the positive integers \(I=F(x^k,y^k)\) and \(J=F(U^K,V^K)\).
Since \(F\) is positive on the real projective line,
\(I\asymp y^{6k}\) and \(J\asymp H^{6K}\).
The local identity for this map says that whenever \(p\ne3\) divides
\(F(a,b)\) for coprime inputs, its valuation in \(F\) at the reduced
output of \(f(a/b)\) is exactly \(3v_p(F(a,b))\). Indeed, putting
\(P/Q=f\) in the displayed coordinates, the polynomial quotient
\(F(P,Q)/F(T,1)^3\) reduces to \(-4860(T^3+1)\) modulo \(F(T,1)\).
Also \(\operatorname{Res}(F(T,1),Q)=3^9\). Such a prime has input
order nine and is at least 19, so both the quotient and denominator
are units. [First-stage calculation](abc_cyclotomic_small_repeats_transfer.md)

For \(p\ne3\) dividing \(I\), the ratio \(U/V\) has exact order nine
modulo \(p\). Since \(3\nmid K\), its \(K\)-th power retains that
order. Lifting the exponent in \(U^{9K}-V^{9K}\) therefore gives
\[
              v_p(J)=3v_p(I)+v_p(K).
\]
In particular every such \(p\) occurs in \(J\). For *every* \(p\ne3\)
dividing \(J\), the last application of \(f\) gives valuation
\(3v_p(J)\) in \(\Phi_{18}(A,B)=F(-B,A)\). Negation changes the
order from nine to eighteen, and inversion preserves it.

Both \(I\) and \(J\) have valuation at most one at three, by the
residues of cubes modulo nine. Neither has a prime divisor \(p\le Z\)
other than three. For \(p=2,5\) this follows from the order condition.
For \(7\le p\le Z\) the map has good reduction (its homogeneous
resultant has prime divisors only among \(2,3,5\)). If \(p\mid xy\),
the first input reduces to zero or infinity, which \(f\) exchanges.
Otherwise \(t\equiv1\pmod p\), and \(f(1)=-1\). In all cases the
inputs defining \(I,J\) avoid the primitive ninth roots modulo \(p\).

At \(p\mid J\), \(p\ne3\), the excess \(3v_p(J)-1\) pays for
\(2v_p(J)\). When \(p\mid I\) it also pays for \(2v_p(I)\), because
\(v_p(J)-1\ge3v_p(I)-1\ge2v_p(I)\). Multiplying gives
\[
 \prod_{\substack{p\mid J\\p>Z}}
 p^{v_p(\Phi_{18}(A,B))-1}
 \ \ge\ (IJ/9)^2\ \gg_{k,K}\ A^{3/2+3/(16K)} .
\]
For example, at \(x/y=1/2,\ k=2,\ K=1\), one has
\(I=4161=3\cdot19\cdot73\). The valuations at both 19 and 73 are
three in \(J=F(-23224,3499)\) and nine in the final sextic. At
\(K=1\) the exponent in the display is \(27/16\).

For the upper cutoff, a prime of \(J\) divides some \(\Phi_d(U,V)\)
with \(d\mid9K\), since it divides \(U^{9K}-V^{9K}\). Each such
factor has absolute value at most \((2H)^{\varphi(d)}\), with
\(\varphi(d)\le\varphi(9K)\). The strict inequality
\(\varphi(9K)<8K\eta\) and the height comparison put all certified
primes below \(A^\eta\) for large \(y\).

The same argument gives the exponent for any fixed number \(m\ge2\)
of iterations. Use \(m-1\) ordinary applications of \(f\) before
the final power \(K\) and the last \(f\). At each step, if the new
input sextic has valuation \(v\) then the output excess is
\(2v+(v-1)\). The second summand retains the entire previously
certified excess, since every previous ninth-order prime remains
ninth-order after the power. An ordinary step consequently changes
the exponent \(c\) to \(3/2+c/8\), starting at zero. The final
step gives \(3/2+c/(8K)\), or explicitly
\[
           \frac32+\frac{12}{56K}(1-8^{-(m-1)}).
\]
At \(K=1\) this is \((12/7)(1-8^{-m})\). The last input sextic
contains every earlier certified prime, so the same upper cutoff
applies for the chosen even \(K\). Enlarge \(k\) if necessary to
keep the full real orbit in the alternating small and large
negative intervals: \(f(t)\sim-2/(5t^2)\) at zero and
\(f(t)\sim-5/(2t^2)\) at infinity. Take the larger of
\(-G,-1/G\) as the positive output ratio.

## Transfer to general abc

As a function of \(s=x/y\), the map \(\beta(s)=G^{18}\) is Belyi:
the critical values of \(f\) lie in \(\{0,\infty\}\) and the
primitive ninth roots. The two rational points are exchanged by \(f\);
on the six roots \(f(\zeta)=\zeta^4\). The intermediate power
preserves these sets since \(3\nmid K\). Also \(f(1)=f(-1)=-1\), so
\(\beta(0),\beta(1),\beta(\infty)\in\{0,1,\infty\}\).
For \(D=18\cdot64kK\), the reduced inverse image of these three
target points has degree \(D+2\) by Riemann–Hurwitz. Removing the
three marked source points leaves degree \(D-1\). Thus the output
radical is \(\ll_{k,K}\operatorname{rad}(xy(y-x))y^{D-1}\), while
\(A^{18}\asymp_{k,K}y^D\). The marked-point argument gives the full
rational abc inequality from abc on this family. The restriction to
\(x\le y/2\) loses no input triple: choose \(x\) as the smaller of its
two positive summands. [Exponent transfer](abc_cyclotomic_small_repeats_transfer.md)
