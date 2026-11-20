# Counting small radicals and constructing them on a Pell sequence

For coprime integers \(x>y>0\) of opposite parity put
\[
P=xy(x-y)(x+y)(x^2+y^2)(x^2+2xy-y^2)(x^2-2xy-y^2),\qquad R=\operatorname{rad}(|P|).
\]
The seven factors are pairwise coprime in absolute value. Squaring the real and imaginary parts of \((x+iy)^4\) gives a primitive abc triple of height \(C=(x^2+y^2)^4\) and radical \(R\). Full rational abc is equivalent to \(R\gg_\delta x^{8-\delta}\) for every \(\delta>0\) on these pairs. [Proof of the equivalence](abc_quadratic_maps.md)

## A uniform count at the critical exponent

For \(H\ge2\), at most \(O(H^{4/3}(\log(2H))^9)\) admissible pairs with \(H<x\le2H\) satisfy \(R\le x^8\). The constant is absolute.

Write \(f(t)=P(1,t)\). Its only zeros on \([0,1]\) are \(0,1,\sqrt2-1\), all simple. If \(|f(y/x)|<H^{-2/3}\), then the reduced fraction \(y/x\) lies in one of three intervals of length \(O(H^{-2/3})\). Two distinct such fractions are at distance at least \(1/(4H^2)\). These intervals account for \(O(H^{4/3})\) pairs.

Otherwise let \(S=\prod_{p^e\parallel P}p^{\lfloor e/2\rfloor}\), so \(S^2\mid P\) and \(S^2\ge |P|/R\). At a qualifying pair,
\[
S^2\ge x^{10}|f(y/x)|/x^8\ge H^{4/3}.
\]
Every prime in \(S\) is at most \(3H\), because its square must divide one of the seven separate factors, each of absolute value at most \(8H^2\). There is a divisor \(d\mid S\) with \(H^{2/3}\le d\le3H^{4/3}\). Take a single prime factor at least \(H^{2/3}\) if available. Otherwise multiply prime factors, with multiplicity, until the product first reaches that threshold.

For odd \(p\), on primitive vectors the condition \(p^a\mid P\) specifies at most ten projective classes modulo \(p^a\). There are four linear roots and at most six quadratic roots. They are distinct modulo every odd prime where they exist; the quadratic discriminants are \(-4,8,8\), so each root lifts uniquely. At 2 only one of \(x,y\) can be even and all other factors are odd, so the two coordinate axes suffice at every level. By the Chinese remainder theorem there are at most \(10^{\omega(d)}\) classes modulo \(d^2\). In a single class every determinant \(x_1y_2-x_2y_1\) is divisible by \(d^2\), giving spacing at least \(d^2/(4H^2)\). Thus the number of pairs captured by this \(d\) is \(O(10^{\omega(d)}(1+H^2/d^2))\), including when \(d>H\).

Sum over the displayed interval for \(d\). The elementary bound \(\sum_{d\le T}10^{\omega(d)}\ll T(\log(2T))^9\) follows by majorizing by the ten-fold divisor function and summing over its first nine factors. Partial summation handles \(1/d^2\) and proves the count.

There is also a pointwise restriction on the source of any exceptional sequence. For any fixed finite set of primes \(S_0\) and any \(\epsilon>0\), the simultaneous real and \(p\)-adic Roth theorem (the two-variable Subspace Theorem) gives
\[
\frac{x^{10}}{|P|}\prod_{p\in S_0}p^{v_p(P)}\ll_{S_0,\epsilon} x^{2+\epsilon}.
\]
Indeed, at each of the finitely many places, the local size is controlled by proximity to the closest of the distinct algebraic projective roots of \(P\); all other roots there contribute at most a constant. Use the simultaneous theorem for each of the finitely many tuples of roots. Its exceptional rational lines contain only finitely many primitive positive vectors. No admissible pair is an exact root. In particular, if \(R\le x^{8-\delta}\) at arbitrarily large \(x\), those pairs must have \(\prod_{p\notin S_0}p^{(v_p(P)-1)_+}\gg_{S_0,\delta} x^{\delta/2}\). The uniform counting result above does not require the Subspace Theorem.

## An infinite family below the critical scale

There are absolute \(\kappa,c_1,c_2>0\) and an explicit sequence of these triples of unbounded height such that
\[
\frac C R\ \ge\ c_1\log C\,
\exp\!\big(c_2(\log\log\log C)^{1+\kappa}\big).
\tag{1}
\]
In particular \(C/R\) eventually exceeds \(\log C\,(\log\log C)^B\) for each fixed \(B>0\) along the same sequence. The proof constructs repeated primes on the locus \(x^2-2xy-y^2=-1\). The logarithm of the displayed lower bound is \(o(\log C)\).

Write \(T_j+U_j\sqrt2=(1+\sqrt2)^j\). For integers \(m\) tending to infinity, set
\[
L=\operatorname{lcm}(1,\ldots,m),\qquad n=2^L-1,\qquad x=U_{n+1},\qquad y=U_n.
\]
The norm identity gives \(T_n^2-2U_n^2=(-1)^n\), and \(T_n\) is odd by the recurrence. Since \(x=T_n+U_n\), the pair is coprime and of opposite parity. Substitution and multiplication of Pell units give
\[
\begin{aligned}
x-y&=T_n, & x+y&=T_{n+1},\\
x^2+y^2&=U_{2n+1}, &x^2+2xy-y^2&=T_{2n+1},\\
x^2-2xy-y^2&=(-1)^n. &&
\end{aligned}
\]
Consequently \(|P|=U_{2n}U_{2n+2}U_{4n+2}/8\), since \(U_{2j}=2T_jU_j\). Also \(|P|\ll x^8\) since the last quadratic has absolute value 1. Duplication gives \(v_2(x)=L\), contributing \(2^{L-1}\) to \(|P|/R\).

Take a prime \(p\equiv7\bmod8\) for which every prime power exactly dividing \(p-1\) is at most \(m\). Then \(p-1\mid L\), giving \(p\mid n\). Write \(p-1=2s\) with \(s\) odd. For each \(q^a\parallel s\), its totient is at most \(m\) and hence divides \(L\). Euler's theorem gives \(q^a\mid 2^L-1\), so \(s\mid n\). Thus \(p(p-1)\mid 2n\). Since 2 is a square modulo \(p\), lift a square root \(t\) to modulus \(p^2\). The units \(1+t\) and \(1-t\) have powers of exponent \(p(p-1)\) equal to 1 modulo \(p^2\). The Pell formula with denominator \(2t\) now gives \(p^2\mid U_{2n}\). Each eligible prime supplies an additional factor \(p\) to \(|P|/R\).

### There are enough eligible primes

For a sufficiently small absolute \(\kappa>0\), put \(X=m^{1+\kappa}\). A positive proportion of the primes in \((X/2,X]\) have the specified residue class and prime-power condition on \(p-1\). To see this, the prime number theorem modulo 8 supplies \(\gg X/\log X\) primes in the class. The number with \(q^a\mid p-1\) for some \(q^a>m,\ a\ge2\) is \(O(X/\sqrt m)\). For \(q\le\sqrt m\), the sum of the reciprocals of powers of \(q\) above \(m\) is \(O(1/m)\); for \(q>\sqrt m\), sum \(O(q^{-2})\). Each such power divides at most \(X/q^a\) of the integers \(p-1\) in question.

If a prime \(q>m\) divides \(p-1\), write \(p=tq+1,\ t\le X/m\). The upper-bound sieve for the two linear forms gives
\[
\#\{q\le Y:q,\ tq+1\text{ prime}\}
\ll (t/\phi(t))^2 Y/(\log Y)^2
\]
uniformly in positive integers \(t\) and \(Y\ge3\). Summing at \(Y=X/t\) gives \(O(X\log(2X/m)/(\log m)^2)\). Here \(\sum_{t\le T}(t/\phi(t))^2/t\ll\log(2T)\), by expanding the multiplicative weight as a divisor sum whose local increments \((1-1/p)^{-2}-1\) are \(O(1/p)\). For \(0<\kappa<1/4\), the absolute constant in this upper bound is independent of \(\kappa\). Taking \(\kappa\) small enough leaves \(\gg X/\log X\) eligible primes. Their logarithms sum to \(\gg X\).

For completeness, the required uniform sieve estimate follows from Selberg's quadratic weights. For even \(t\) let \(\nu(p)\) count the roots of \(z(tz+1)\) modulo \(p\); it is 1 for \(p\mid t\) and 2 otherwise. Extend \(\nu\) multiplicatively to squarefree moduli. Set \(Z=Y^{1/16}\), \(g(p)=\nu(p)/p\), \(h(p)=g(p)/(1-g(p))\), and \(G=\sum_{d\le Z}\mu^2(d)h(d)\), with \(h\) extended multiplicatively on squarefree integers. Squaring \(\sum_{d\mid z(tz+1)}\lambda_d\), with weights supported on squarefree \(d\le Z\) and \(\lambda_1=1\), majorizes the sifted indicator. The main quadratic form has summand \(\lambda_d\lambda_e g([d,e])\). It equals \(\sum_r u_r^2/h(r)\), where \(u_r=\sum_{r\mid d}\lambda_dg(d)\) and \(g\) is extended multiplicatively. This follows by expanding \(1/g((d,e))\) as \(\sum_{r\mid(d,e)}1/h(r)\). Choosing \(u_r=\mu(r)h(r)/G\) on squarefree \(r\le Z\) gives main term \(Y/G\) and \(\lambda_1=1\). Möbius inversion gives \(|\lambda_d|\le\prod_{p\mid d}(1-g(p))^{-1}\le d\). The remainder from residue-class counts is \(O(\sum_{d,e\le Z} de\,\nu([d,e]))=O(Z^6)\).

To bound \(G\) from below take the full Euler product \(\prod_{p\le Z^{1/10}}(1+h(p))\). Under its normalized positive weights the expected logarithm of a divisor is \(\sum_{p\le Z^{1/10}} g(p)\log p\le(1/5)\log Z+O(1)\) by Mertens' estimate. At least half the weight is on \(d\le Z\) for large \(Y\). The product is \(\gg(\phi(t)/t)^2(\log Y)^2\), by retaining the primes coprime to \(2t\) and using Mertens' product theorem. This proves the sieve bound, adding \(O(Z)\) instances where one prime is at most \(Z\). For odd \(t\), at least one of the two primes must be 2, which is immediate.

Finally the Pell formula gives \(\log x=2^L\log(1+\sqrt2)+O(1)\), while the prime number theorem gives \(\log L\sim m\). We have \(x^8\le C\le16x^8\) and \(|P|\ll x^8\). Combining the factor \(2^{L-1}\) with the eligible-prime product \(\exp(\gg m^{1+\kappa})\) proves (1).

### How far the forced divisibilities reach

At every index on this Pell locus, primes \(p\le\sqrt n\), counted with their full multiplicities in \(P\), contribute \(O(n/\log(2n))\) to \(\log |P|\). In particular they supply \(o(\log C)\). This includes all eligible primes used in (1) for large \(m\), since \(p-1\mid L\) implies \(p\le L+1\).

For an odd prime \(p\), let \(r\) be the order of \((1+\sqrt2)/(1-\sqrt2)\) in the residue field at \(p\). Frobenius fixes this ratio or sends it to its inverse, so \(r\mid p-(2/p)\). Binet's formula and binomial lifting at an unramified odd prime give \(v_p(U_j)=v_p(U_r)+v_p(j)\) when \(r\mid j\), and zero otherwise. Also \(v_p(U_r)\log p\le\log U_r\ll p\). Thus at each of \(j=2n,2n+2,4n+2\) the full contribution up to \(Y\) is \(O(Y^2/\log(2Y)+\log(2n))\), using \(\sum_{p\le Y}p\ll Y^2/\log(2Y)\). The prime 2 contributes \(O(\log(2n))\) by duplication and the parity of \(U_j\) at odd \(j\). Set \(Y=\sqrt n\). Finally \(y/x\to\sqrt2-1\), where all six other factors, normalized by their degrees, are nonzero. Thus \(\log |P|=\log C+O(1)\) here. A fixed-power counterexample on this locus would need a contribution of order \(\log C\) from repeated factors above the indicated cutoff. Their actual multiplicities are undetermined.

## Finite checks

Two independent radical computations found 212740 admissible pairs with \(x\le1024\), of which 822 have \(R\le x^8\) and 71 have \(R^2\le x^{15}\). The comparisons used integers. For \(x=408,y=169\) the seven absolute factors are \(408,169,239,577,195025,275807,1\); their radical is \(63457230056004330\). This example belongs to the Pell locus at \(n=7\), illustrating the locus without requiring the particular index choice in (1). At \(m=12\) the eligible primes up to \(120\) are \(7,23,31,71\); modular powering verified the divisibilities by their squares at \(L=27720\).
