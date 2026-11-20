# Exact high multiplicities in the eighth cyclotomic row

Fix \(n\ge1\) and \(Z\ge2\), and put \(d=4n+1,\ e=2n+1\).
For all sufficiently large \(X\), there are \(\gg_{n,Z} X^{2/d}\)
distinct primitive output pairs \(B<A\le X\) of the degree-\(d\)
eighth-order Padé map with the following property. Each pair comes
from a squarefree source value \(U=x^4+y^4\), and every prime \(p\mid U\)
has exact order eight for \(A/B\bmod p\) and satisfies
\[
      Z<p\le U\ll_n A^{4/d},\qquad v_p(A^4+B^4)=e.
\]
The certified part of the repeated-prime product is exactly
\[
 \prod_{p\mid U}p^{\,v_p(A^4+B^4)-1}
       =U^{e-1}\asymp_n A^{\,2-2/d}.
\]
These pairs make up a positive proportion of all distinct outputs of
this fixed map of height at most \(X\). Given \(\delta,\eta>0\) and
a prescribed minimum multiplicity, choose \(n\) with \(2/d<\delta\),
\(4/d<\eta\), and \(e\) at least that minimum. Every sufficiently large
pair counted here then has certified mass at least \(A^{2-\delta}\)
from primes \(Z<p<A^\eta\), each of valuation exactly \(e\).

## The fixed map and its exceptional primes

Use the dyadic construction with \(N=8\) and without an input power
substitution (\(k=1\)). Explicitly, put \(\alpha=-1/4\) and
\[
 P(z)=\sum_{j=0}^n{n+\alpha\choose j}{n-\alpha\choose n-j}z^j,
 \qquad Q(z)=z^nP(1/z),\qquad f(t)=tP(-t^4)/Q(-t^4).
\]
Let \(L_1,L_2\) be integral homogeneous coordinates of degree \(d\)
for this map, obtained by clearing denominators. Write
\(F(x,y)=x^4+y^4\). Exact Padé contact gives
\[
              F(L_1,L_2)=F(x,y)^e J(x,y),\quad J\in\mathbf Z[x,y],
              \qquad \gcd(F,J)=\gcd(F,L_2)=1
                       \quad\text{over }\mathbf Q.
\]
Take \(S\) to consist of \(2\) and the primes dividing the two nonzero
affine resultants of \(F(t,1)\) with \(J(t,1)\) and \(L_2(t,1)\).
For any primitive pair \(x,y\) and any \(p\mid F(x,y)\) outside \(S\),
\(y\) is a unit at \(p\). The resultants then make \(L_2(x,y)\) and
\(J(x,y)\) units there as well. After dividing the output coordinates
by their gcd, taking absolute values and ordering them as \(A>B>0\),
the identity gives \(v_p(A^4+B^4)=e\,v_p(F(x,y))\). Also \(p\nmid AB\)
and \((A/B)^4=-1\bmod p\), giving order eight since \(p\) is odd.
[Padé construction and exact contact](abc_dyadic_pade_power_transfer.md)

## Counting squarefree inputs

Let \(M\) be the product of the primes in \(S\) and all primes at most
\(Z\), taking each only once. Apply Stewart and Xiao's distinct-value
theorem to the fixed positive definite integral form
\[
                         G(u,v)=(Mu)^4+v^4 .
\]
The form has degree four, nonzero discriminant, and largest rational
irreducible factor degree \(r=4\): it is obtained from the homogenized
\(\Phi_8\) by invertible rational substitution. It has no fixed prime
square divisor since \(G(0,1)=1\). The theorem applies for squarefree
values because \(2>7r/18=14/9\). It gives
\(\#\{0<U\le T:U\text{ squarefree and represented by }G\}
 \sim C_{G,2}T^{1/2}\) with \(C_{G,2}>0\). Subtracting this
asymptotic at \(T=H^4/2\) from the one at \(T=H^4\) gives
\(\gg_{n,Z}H^2\) distinct such \(U\) in that shell.
[Stewart and Xiao, *On the representation of \(k\)-free integers by binary forms*](https://arxiv.org/abs/1612.00487)

Choose one integral representation for each of these \(U\). The
coordinates \((Mu,v)\) are primitive, since any common prime would
have fourth power dividing \(U\). Consequently every \(p\mid M\)
is prime to \(v\) and \(U\equiv v^4\not\equiv0\bmod p\).
Taking absolute values and ordering the two source coordinates as
\(0<x<y\) preserves \(U\). For large \(H\) neither coordinate can
vanish or have the same absolute value as the other: a primitive
pair of either type would give \(U=1\) or \(2\). Moreover
\(H/\sqrt2<y\le H\) by \(y^4\le U\le2y^4\).
Distinct \(U\) give distinct slopes \(x/y\), as a primitive positive
pair is recovered from its reduced slope.

The coordinate forms of \(f\) have no common projective zero. Their
resultant bounds the output gcd on primitive inputs; compactness on
the normalized real shell then gives \(A\asymp_n y^d\) after the
output is sorted. There are only finitely many source slopes with
\(f(x/y)=0,\infty,\pm1\), which may be discarded. For a given
ordered output \((A,B)\), the rational value before sorting and
taking absolute values is one of \(\pm A/B,\pm B/A\). Each has
at most \(d\) preimages, so the folding costs a factor of at most
\(4d\). Taking \(H=c_n X^{1/d}\) with \(c_n>0\) sufficiently small
proves the lower bound. Conversely every output of height at most
\(X\) has a source of height \(O_n(X^{1/d})\), giving the upper bound
\(O_n(X^{2/d})\) for all outputs of the fixed map. Finally \(U\) is
squarefree and prime to \(M\), so all its primes have the asserted
exact valuations. The mass estimate follows from
\(4(e-1)/d=2-2/d\).

The unrestricted Padé image has the marked-point transfer for abc.
Whether restricting that image to these squarefree source values
preserves its equivalence with unrestricted abc remains open here.
