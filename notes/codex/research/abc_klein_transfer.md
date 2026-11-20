# A generalized Fermat reduction for rational abc

For a signed integer equation \(X^2+Y^3=1728Z^5\) with \(XYZ\ne0\), reorder the absolute values of its three terms into a positive sum with largest term \(C\). Its radical is \(R'=\operatorname{rad}(6XYZ)\). We call the equation primitive when the three *terms* are relatively prime. Full rational abc is equivalent to abc on just these primitive solutions. The fixed coefficient \(1728\) is part of this statement.

## What rules out a direct transfer to exponent seven

Let a nonconstant rational map on the projective line in characteristic zero have degree \(D\). Every fiber has total multiplicity \(D\). The three fibers over \(0,1,\infty\) together have at least \(D+2\) distinct points, since total ramification on the entire line is \(2D-2\) by Riemann–Hurwitz. If all multiplicities in the respective fibers are divisible by \(e_1,e_2,e_3\), their number is at most \(D\sum_i 1/e_i\). A necessary condition is therefore
\[
D\left(\frac1{e_1}+\frac1{e_2}+\frac1{e_3}-1\right)\ge2.
\]
For signature \((2,3,7)\), the sum is \(41/42\), ruling out such a map at every degree. This applies to a rational-function identity with powers in its reduced fibers. A polynomial identity that acquires common factors must be checked after cancellation.

There is also a cost to allowing residual factors in the fibers. At a point \(P\) in fiber \(i\) write \(m_P\) for its multiplicity and \(r_P\) for the least nonnegative residue of \(m_P\bmod e_i\). Then \(1-m_P/e_i\le(1-1/e_i)r_P\). Adding over the three fibers gives, in signature \((2,3,7)\),
\[
\sum_{i}\sum_{P\text{ in fiber }i} r_P\ \ge\ \tfrac76(2+D/42).
\]
Thus increasing the degree cannot reduce the residual degree to \(o(D)\). On the arithmetic side, Poonen, Schaefer and Stoll determined the primitive integer solutions of the fixed equation \(X^2+Y^3=Z^7\). A contradiction from that theorem would require an independent argument forcing a hypothetical abc violation into that finite set. [Poonen, Schaefer and Stoll](https://arxiv.org/abs/math/0508174)

## A transfer at exponent five

Signature \((2,3,5)\) has reciprocal sum \(31/30\); the necessary degree for a map with the prescribed divisibilities is at least 60. Use Klein's binary icosahedral forms
\[
\begin{aligned}
F(s,t)&=st(s^{10}+11s^5t^5-t^{10}),\\
H(s,t)&=-(s^{20}+t^{20})+228(s^{15}t^5-s^5t^{15})-494s^{10}t^{10},\\
T(s,t)&=s^{30}+t^{30}+522(s^{25}t^5-s^5t^{25})-10005(s^{20}t^{10}+s^{10}t^{20}).
\end{aligned}
\]
Direct expansion gives \(T^2+H^3=1728F^5\). Also \(T=(s^2+t^2)K\) for an integer form \(K\) of degree 28, as can be checked at \(s/t=\pm i\) and by monic polynomial division.

Start from a primitive positive triple \(a+b=c\), with radical \(R=\operatorname{rad}(abc)\). Put \(y=c\) and choose for \(x\) an addend of parity opposite to \(c\), choosing the smaller one if both qualify. Then \(\gcd(x,y)=1\), and \(xy(y-x)=abc\). Put
\[
s=y^2-x^2,\qquad t=2xy.
\]
If \(s\equiv2t\bmod5\), replace \(t\) by \(-t\). The resulting \(s,t\) are coprime, \(s\) odd and \(t\) even, and \(s\not\equiv2t\bmod5\). The sign switch is always sufficient since \((s,t)\) is primitive. Evaluate the three forms at this pair and take \(X=T,\ Y=H,\ Z=F\).

**Primitivity.** At 2, \(T\) and \(H\) are odd. At 3, \(H\equiv-1\bmod3\) for any nonzero pair modulo 3, by considering which coordinates are units. If a prime \(p\ge5\) divided both \(T\) and \(H\), it would divide \(F\). On a coordinate axis \(H\) is a unit, so \(st\) is invertible modulo \(p\). Set \(z=(s/t)^5\). From \(F=0\) we get \(z^2+11z-1=0\). Reduction of \(H/t^{20}\) modulo this quadratic gives \(3125(11z-1)=-5^5z^2\). Thus only \(p=5\) is possible. There \(z^2+11z-1=(z-2)^2\) and \(z=s/t\), excluded by the sign choice. Hence the terms are primitive. They are nonzero: away from the coordinate axes the three univariate factors have leading and constant coefficients of absolute value 1, so any rational zero would be \(\pm1\); the odd/even pair cannot have this ratio.

**Height and radical.** Uniformly in the input, \(C\asymp c^{120}\). All three terms are homogeneous of degree 120 in \(x,y\). For the lower bound, \(F,H\) have no common projective zero in characteristic zero by the same remainder calculation. Also \(y^2-x^2\) and \(2xy\) have no common projective zero. For either sign, the maximum of the absolute terms on \(y=1,\ 0\le x\le1\) therefore has positive minimum.

The radical calculation uses two exact identities:
\[
st=\pm2xy(y-x)(y+x),\qquad s^2+t^2=(x^2+y^2)^2 .
\]
The first provides the entire original prime support \(R\). The second means that \(x^2+y^2\) only needs to be counted once. The remaining factors, after the fixed primes, are
\[
(y+x),\quad (s^{10}+11s^5t^5-t^{10}),\quad H(s,t),\quad
(x^2+y^2),\quad K(s,t).
\]
Their degrees in \(x,y\) are \(1,20,40,2,56\), respectively. Their product in absolute value is \(O(c^{119})\), giving
\[
R'\ll R c^{119},\qquad \frac{C}{R'}\gg\frac cR .
\]
In particular an infinite sequence with \(c/R\ge c^\eta\), for fixed \(\eta>0\), yields unbounded primitive outputs with \(C/R'\gg C^{\eta/120}\). This proves the equivalence in the opening paragraph: the other implication follows since the reordered outputs are ordinary primitive abc triples. The size loss in the transferred exponent is harmless for finiteness, but it matters for numerical searches.

## What fixed-coefficient finiteness gives

On any sequence of primitive solutions to \(X^2+Y^3=1728Z^5\) whose heights tend to infinity, the squarefree part of each of \(|X|,|Y|,|Z|\) tends to infinity. Here the squarefree part of \(n\) is the squarefree \(d\) in \(n=du^2\). For example, fixing the signed squarefree part \(d\) of \(Z\) gives \(X^2+Y^3=1728d^5u^{10}\), a fixed-coefficient generalized Fermat equation of signature \((2,3,10)\). Darmon–Granville finiteness applies since the reciprocal sum is less than 1 and the roots are coprime. Fixing the squarefree part of \(X\) or \(Y\) instead gives \((4,3,5)\) or \((2,6,5)\), again with reciprocal sum less than 1. Taking a finite union over bounded \(d\) proves the assertion. [Darmon and Granville, *On the equations \(z^m=F(x,y)\) and \(Ax^p+By^q=Cz^r\)*](https://doi.org/10.1112/blms/27.6.513)

This argument allows the squarefree parts to grow arbitrarily slowly relative to \(C\). The estimate that would settle abc here is \(\operatorname{rad}(6XYZ)\gg_\delta C^{1-\delta}\) for every \(\delta>0\). Fixed-twist finiteness supplies no such rate. Rescaling the identity to make \(1728F^5\) an unweighted fifth power introduces a common factor, so the transfer above does not establish the corresponding equivalence for primitive solutions with coefficient 1.

## Checks

Symbolic expansion verified the Klein identity, the divisibility by \(s^2+t^2\), and the remainder used in the primitivity proof. Integer evaluation checked all 13698 primitive inputs \(a<b,\ a+b\le300\). The modulo-5 rule switched the sign in 2279 cases; all output triples had gcd 1.
