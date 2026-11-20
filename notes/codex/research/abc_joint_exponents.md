# Combining the fifth- and seventh-power tests for abc

For a primitive triple \(a+b=c\) of positive integers, let \(R=\operatorname{rad}(abc)\), the product of its distinct prime factors. For a prime \(\ell\), let \(R_\ell\) be the product restricted to primes \(p\) for which \(\ell\nmid v_p(abc)\). Then
\[
\frac{R}{\operatorname{lcm}(R_5,R_7)}
=D_{35},\qquad D_M=\prod_{\substack{p\mid abc\\M\mid v_p(abc)}}p.
\]
This note describes a sparsity bound, an infinite family showing a limit of the bound, and a search for primitive triples with small radical. The search supplies individual exceptions at a fixed exponent. Infinitude at any such exponent remains open here. [Earlier single-exponent calculation](abc_field_discriminants.md)

## A determinant bound for simultaneous omissions

For each fixed integer \(M\ge2\), the number of ordered primitive positive triples with \(c\le H\) and \(D_M^M>c^2\) is
\[
O_M\!\left(H^{3/M}(1+\log H)^2\right).
\]
Write \(D_M=uvw\), distributing its primes according to whether they divide \(a,b,c\). Then \(u^M\mid a,\ v^M\mid b,\ w^M\mid c\), and \(u,v,w\) are pairwise coprime. For two solutions with the same assignment, the determinant \(ab'-a'b\) is divisible by \(u^Mv^M\). Rewriting it as \(ac'-a'c\) also gives divisibility by \(w^M\). Its absolute value is less than \(cc'\). If both solutions satisfy the strict threshold, then \(cc'<(uvw)^M\), so the determinant vanishes. Primitivity identifies the two solutions. Finally \(D_M^M\le abc\le H^3\). For \(L=H^{3/M}\) there are at most \(L(1+\log L)^2\) ordered positive integer triples with \(uvw\le L\), by summing \(L/(uv)\) over \(u,v\). This proves the count.

The exceptional set is infinite even for \(M=35\). In fact, for each fixed \(M\ge2\) there are infinitely many primitive triples satisfying
\[
D_M\gg_M c^{\,2/M+1/M^2}.
\]
Take a large prime \(r\nmid M\), put \(L=r^M\), and choose squarefree \(x\in[L,2L]\) with \(y=x+L\) squarefree and \(r\nmid x\). Such \(x\) exist for every sufficiently large \(r\). Square divisibility in either shift rules out at most \(2L\sum_p p^{-2}+O(\sqrt L)\) values. Here \(\sum_p p^{-2}\le 1/4+\sum_{j\ge1}(2j+1)^{-2}=\pi^2/8-3/4<1/2\). Removing multiples of \(r\) costs at most \(L/r+1\) more. Now \(\gcd(x,y)=1\), and the binomial expansion gives \(v_r(y^M-x^M)=M\). In the triple \((y^M-x^M,x^M,y^M)\), every prime in \(rxy\) occurs to exponent exactly \(M\). Thus \(D_M\ge rxy\gg_M c^{2/M+1/M^2}\), since \(c=y^M\asymp_M r^{M^2}\). This construction controls only a divisor of the radical.

## A certified numerical exception

For coprime \(y=x+h>x>0\), set \(a=y^m-x^m,\ b=x^m,\ c=y^m\). Suppose \(p\nmid h\) and \(p^{35}\mid a\). Since \(h\mid a\) and \(a/h\le m y^{m-1}\),
\[
R\le xy\,\operatorname{rad}(h)\,\frac{a/h}{p^{34}},
\qquad
\frac{c}{R}\ge\frac{p^{34}}{m x\operatorname{rad}(h)}.
\]
An infinite sequence satisfying \(p^{34}\ge m x\operatorname{rad}(h)c^\eta\) with fixed \(m\), fixed \(\eta>0\), and unbounded \(c\) would therefore disprove abc.

One numerical witness uses \(p=631,\ m=5\) and the following bases.

~~~text
x = 188501707118483312662842033434214073534
y = 14106104618039134064040525112584509829903089804413987905
~~~

Their gcd is 1, \(631^{35}\mid y^5-x^5\), and \(31^2\mid x\). Consequently \(R\le B=axy/(631^{34}\cdot31)\). Integer arithmetic gives \(\lfloor c/B\rfloor=1851\) and \(c^{100}>B^{101}\). Thus the 276-digit integer \(c\) exceeds \(R^{1.01}\). The following verification needs only Python's standard library.

~~~python
from math import gcd

x = 188501707118483312662842033434214073534
y = 14106104618039134064040525112584509829903089804413987905
c = y**5
b = x**5
a = c - b
assert a > 0 and gcd(a, b) == 1
assert a % 631**35 == 0 and x % 31**2 == 0
B = a*x*y // (631**34 * 31)
assert len(str(c)) == 276 and c // B == 1851
assert c**100 > B**101
~~~

### How the search found the bases

For each prime \(p\le100000\) with \(p\nmid35\), find the nontrivial 35th roots of unity \(z\bmod p^{35}\). Each gives the invertible residue \(n=(z-1)^{-1}\), so \((n+1)^{35}\equiv n^{35}\pmod{p^{35}}\). The initial test \(p^{34}>35n\) succeeded for none of the 28,514 residues. Allowing a difference \(h\) between the bases also tests approximations to \(n/p^{35}\). If \(k/h\) is a continued-fraction convergent, then \(s=hn-kp^{35}\) satisfies \((s+h)^{35}\equiv s^{35}\pmod{p^{35}}\). For same-sign \(s,s+h\) and \(p\nmid h\), taking the absolute values gives coprime bases. Coprimality follows from \(\gcd(k,h)=1\).

Of the 3,588 eligible primes, the tested convergents for eight distinct primes gave \(p^{34}>35xh\). This certifies \(c>R\) for the corresponding exponent-35 triples. For \(p=631\), the order of \(y/x\) modulo \(631^{35}\) is already 5, yielding the smaller triple above. The search retained one representative of each pair of residues \(n,p^{35}-1-n\). The counts describe these tested convergents only. [Reproducible search](abc_joint_exponents.py)

### A limitation of polynomial constructions

Suppose \(X,Y\in\mathbb Q[t]\) are coprime, \(Y/X\) is nonconstant, \(\deg X\le\deg Y=N\), and \(H=Y-X\). If \(S^k\mid Y^m-X^m\) for a nonzero polynomial \(S\) coprime to \(H\), then
\[
(k-1)\deg S\le \deg X+\deg\operatorname{rad}(H)-1 .
\]
Here the radical is the product of the distinct polynomial factors. Mason–Stothers applied to \(X^m+(Y^m-X^m)=Y^m\) gives \(mN+1\le\deg\operatorname{rad}(XY(Y^m-X^m))\). Factor \(Y^m-X^m=H G\), where \(\deg G\le(m-1)N\). Since \(S^k\mid G\), the radical of \(G\) has degree at most \(\deg G-(k-1)\deg S\). Adding the degrees of \(X,Y,\operatorname{rad}(H)\) gives the inequality. Thus a polynomial identity faces a strict degree loss if it tries to enforce the needed comparison through that one divisibility. Special integer values can have additional repeated prime factors.
