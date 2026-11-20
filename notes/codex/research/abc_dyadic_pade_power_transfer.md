# Near-quadratic repeated factors on an abc-equivalent power family

Fix \(N=2^h\), \(h\ge2\), and put \(m=\varphi(N)=N/2\). The cyclotomic
form at this fixed order is \(\Phi_N(A,B)=A^m+B^m\). For every
\(\delta,\eta>0\) and \(Z\ge2\), there is an explicit fixed family of
primitive triples \(B^N+(A^N-B^N)=A^N\), \(A>B>0\), with the following
properties.

* On every member of sufficiently large height, primes \(Z<p<A^\eta\)
  of exact order \(N\) for \(A/B\bmod p\) contribute at least
  \(A^{2-\delta}\) to the repeated part of the single form \(\Phi_N(A,B)\).
* Proving the usual abc bounds for every exponent increment on this
  family implies rational abc.

In particular \(N=8\) gives a single fixed quartic row and fixed eighth
powers for arbitrarily small \(\delta,\eta\). The multiplicity and the
parameterizing map are chosen after fixing those increments. The
construction exploits the regular polygon of roots of \(X^m+1\).

## A diagonal Padé map

Choose \(n\ge1\) and put \(d=mn+1,\ e=2n+1,\ \alpha=-1/m\). Using
generalized binomial coefficients, define
\[
  P(z)=\sum_{j=0}^n {n+\alpha\choose j}{n-\alpha\choose n-j}z^j,
  \qquad Q(z)=z^nP(1/z).
\]
These polynomials have degree \(n\), nonzero constant terms and
\(P(1)=Q(1)={2n\choose n}\). Their ratio is the diagonal Padé
approximant to \(z^\alpha\) about \(z=1\). The precise contact is
\[
 P(1+t)-(1+t)^\alpha Q(1+t)
   =(-1)^n{n-\alpha\choose 2n+1}t^{2n+1}+O(t^{2n+2}).
 \tag{1}
\]
For a direct proof, extract the coefficient of \(s^n\) from
\((1+s)^{n+\alpha}(1+s+t)^{n-\alpha}\). Expanding in \(s/(1+t)\)
gives \((1+t)^{-\alpha}P(1+t)\). Expanding instead in \(t/(1+s)\)
gives the coefficient at \(t^j\) as
\({n-\alpha\choose j}{2n-j\choose n}\). For \(0\le j\le n\)
this is the Taylor coefficient of \(Q(1+t)\), by Vandermonde's
identity. For \(n<j\le2n\) it vanishes. At \(2n+1\) it is
\((-1)^n{n-\alpha\choose 2n+1}\ne0\). This proves (1).

Set
\[
                     f(x)=x\,P(-x^m)/Q(-x^m).
\]
At every root \(\xi\) of \(x^m+1\), \(z=-x^m\) is a local coordinate
near \(1\), and \(x=\xi z^{1/m}\) on that branch. Equation (1) shows
that \(f(x)-\xi\) vanishes to exact order \(e\). These \(m\) points
contribute \(m(e-1)=2mn\) to ramification. The degree before any
cancellation is \(mn+1\); Riemann–Hurwitz forces this same degree
after reduction and accounts for all the ramification. In particular
the displayed coordinates are coprime. The map fixes \(0,\infty\),
and \(Q(-1)=(-1)^nP(-1)\); coprimality forces both values at \(-1\)
nonzero, so \(f(1)=(-1)^n\).

For example \(N=8,n=1\) gives
\(f=x(5-3x^4)/(3-5x^4)\). Its affine Wronskian is exactly
\(15(x^4+1)^2\). In general the unscaled Wronskian is
\(P(0)Q(0)(x^m+1)^{2n}\) by the same ramification count and evaluation at zero.

## Integer specialization and the exact multiplicities

Clear a common denominator and write \(L,M\) for integral coprime-over-
\(\mathbf Q\) homogeneous coordinates of degree \(d\) for \(f\).
Write \(F(X,Y)=X^m+Y^m\). Exact contact gives a polynomial identity
\[
        F(L,M)=F(X,Y)^e J(X,Y),\qquad J\in\mathbf Z[X,Y],
\]
with \(F\) coprime to \(J\) and to \(M\) over \(\mathbf Q\).
Indeed, \(F\) has simple roots, \(M(\xi,1)\ne0\), and \(f(x)-\xi\)
has exact order \(e\). Integrality follows by monic division in \(X\).
Let \(S\) contain \(2\) and the prime divisors of the nonzero affine
resultants \(\operatorname{Res}(F(X,1),J(X,1))\) and
\(\operatorname{Res}(F(X,1),M(X,1))\).
These primes can also be read off directly from (1). If \(\lambda\)
is the integer scaling of the displayed affine coordinates, put
\(C={2n\choose n}\) and \(b=(-1)^n{n-\alpha\choose 2n+1}\).
At every root \(\xi\), \(M(\xi,1)=\lambda C\) and
\(J(\xi,1)=\lambda^m m b C^{m-1}\), both fixed nonzero integers.
Indeed \(F(L,M)=\lambda^m(Q(z)^m-zP(z)^m)\) at \(z=-x^m\),
and \(F(x,1)=1-z\).

Fix \(k\ge1\) divisible by \(p-1\) for every prime \(p\le Z\) or
\(p\in S\). Enlarge \(k\) until \(2\varphi(Nk)<\eta dk\), which is
possible by adjoining sufficiently many distinct primes. For every
reduced \(0<x/y<1\), evaluate \(L,M\) at \((x^k,y^k)\). Divide their
absolute values by their gcd, taking the larger value for \(A\) and
the smaller for \(B\). Omit the finitely many rational parameters
where \(f((x/y)^k)\in\{0,\pm1,\infty\}\). The even exponent \(N\)
and the symmetry and even degree of \(F\) allow both signs and either
ordering. A homogeneous resultant bounds the output gcd by a fixed
constant, and compactness on the real shell gives
\[
             A\asymp_{f,k}y^{dk},\qquad
             y^{mk}\le U:=F(x^k,y^k)\le2y^{mk}.
\]

For any odd prime \(p\mid U\), one has \(p\nmid xy\). If \(p-1\mid k\),
then \(U\equiv2\bmod p\). Thus \(p>Z\) and \(p\notin S\). Both
\(M(x^k,y^k)\) and \(J(x^k,y^k)\) are units at \(p\), and the identity
gives the **exact normalized valuation**
\[
                       v_p(\Phi_N(A,B))=e\,v_p(U).
\]
The ratio \(A/B\) has order \(N\) modulo \(p\) because its \(m\)-th
power is \(-1\) and \(m\) is a power of two. Each \(p\mid U\) also
divides \(x^{Nk}-y^{Nk}\) and hence some \(\Phi_j(x,y)\) with
\(j\mid Nk\). The root-of-unity factorization gives
\(p\le(2y)^{\varphi(j)}\le y^{2\varphi(Nk)}<A^\eta\) for sufficiently
large \(y\). Finally \(v_2(U)\le1\), since \(m\) is even and the
inputs are coprime. The certified product therefore satisfies
\[
 \prod_{\substack{p\mid U\\p\ {\rm odd}}}
       p^{v_p(\Phi_N(A,B))-1}
       \ \ge\ (U/2)^{e-1}
       \ \gg_{f,k}\ A^{2-2/d},\qquad \frac{m(e-1)}d=2-\frac2d .
\]
Choosing \(n\) with \(2/d<\delta\) absorbs the fixed constant for
large \(A\) and proves the stated bound.

## Transfer to unrestricted abc

The map \(\beta(t)=f(t^k)^N\) has degree \(D=Ndk\). Its branch values
lie in \(0,1,\infty\). The inner power branches at \(0,\infty\),
which \(f\) fixes, and all critical values of \(f\) are primitive
\(N\)-th roots. Moreover \(0,1,\infty\) themselves belong to the
reduced inverse image of that boundary, since \(f(1)=\pm1\). By
Riemann–Hurwitz the inverse image has \(D+2\) distinct geometric
points. Its homogeneous squarefree equation over \(\mathbf Q\) is
therefore a constant times \(XY(X-Y)G(X,Y)\), where \(\deg G=D-1\).

For \(R_0=\operatorname{rad}(xy(y-x))\), homogenizing and factoring
the numerator, denominator and their difference for \(\beta\) gives
\[
     \operatorname{rad}\big(AB(A^N-B^N)\big)\ll_{f,k}R_0 y^{D-1},
     \qquad A^N\asymp_{f,k}y^D.
\]
Constants absorb primes in the fixed polynomial contents. An abc
bound with exponent \(1+s\) on the output gives
\(y^{1-(D-1)s}\ll_{f,k,s}R_0^{1+s}\). For any
\(\varepsilon>0\), taking \(s=\varepsilon/(D+(D-1)\varepsilon)\)
gives \(y\ll_\varepsilon R_0^{1+\varepsilon}\). The omitted rational
parameters account for finitely many primitive input triples, absorbed
in the constant. The forward implication is ordinary abc applied to
the primitive power triples themselves.
