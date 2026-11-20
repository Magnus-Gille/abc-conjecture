# An elliptic family with prescribed fourth-power classes

There are infinitely many positive primitive triples of the form
\[
 a=u^4,\qquad b=14637^2v^4,\qquad c=w^2=a+b
\]
such that
\[
\frac{c}{\operatorname{rad}(abc)}\gg(\log c)^2. \tag{1}
\]
The constant is fixed throughout this family. Every term has squarefree part 1, and the fourth-power-free parts of the two addends are fixed. Here the squarefree part of \(n\) means the unique squarefree \(d\) such that \(n/d\) is a square.

This addresses a limitation of using the three quadratic fields \(\mathbb Q(\sqrt{ab}),\mathbb Q(\sqrt{bc}),\mathbb Q(\sqrt{ca})\) together. All three are \(\mathbb Q\) throughout this family. More generally, full abc is already equivalent to its restriction to primitive triples of three squares. Indeed an input \(a+b=c\), \(a<b\), gives Pythagorean legs \(2ab,\ b^2-a^2\) and hypotenuse \(a^2+b^2\). Divide all three by their gcd, at most 2, and square. The output height is comparable to \(c^4\), and its radical is at most \(2\operatorname{rad}(abc)(b-a)(a^2+b^2)\). Thus the output height divided by its radical is at least a fixed positive constant times \(c/\operatorname{rad}(abc)\). A fixed-power violation survives with a smaller fixed exponent. This equivalence applies to the full three-square class. [Earlier transfer](abc_quadratic_maps.md)

## Four independent points

Set \(D=14637,\ N=2D=2\cdot3\cdot7\cdot17\cdot41\) and let \(E\) be \(Y^2=X^3-N^2X\). The following points and their images under the usual full 2-descent map are rational. The last two columns represent \(X\) and \(X-N\) modulo nonzero rational squares.

| \(X\) | \(Y\) | class of \(X\) | class of \(X-N\) |
|---:|---:|---:|---:|
| 1771077 | 2356659459 | 14637 | 123 |
| 142188 | 52467372 | 123 | 1394 |
| 171462 | 69956496 | 102 | 123 |
| 313650 | 174891240 | 1394 | 246 |

The good reductions at 11 and 19 have respectively 12 and 20 points, as is also seen by pairing \(X\) and \(-X\) in the character sum. Reduction of prime-to-residue-characteristic torsion at the two primes bounds the rational torsion order by 4. The rational 2-torsion attains that bound. Its generators \((0,0)\) and \((N,0)\) have descent images \((-1,-N)\) and \((N,2)\).

List those two generators followed by the four table rows. Keep the sign and the parities at \(2,3,7,17\) from the first component, and the parity at 17 from the second. The resulting six rows are
\[
\begin{pmatrix}
1&0&0&0&0&1\\0&1&1&1&1&0\\0&0&1&1&1&0\\
0&0&1&0&0&1\\0&1&1&0&1&0\\0&1&0&0&1&0
\end{pmatrix}.
\]
Its integer determinant is \(-1\). Thus the four points are independent modulo torsion. Indeed any integral dependence modulo torsion can first be divided by the gcd of the coefficients in the torsion-free quotient, giving an odd coefficient and contradicting the descent calculation. The argument only needs rank at least four. The descent map, formal group, and canonical height used here are standard. [Silverman, *The Arithmetic of Elliptic Curves*](https://doi.org/10.1007/978-0-387-09494-6)

## From congruences on the curve to primitive triples

For a non-torsion point \(Q=(X,Y)\), put
\[
t=Y/(2X),\qquad s=X/2-t^2.
\]
The curve equation gives \(s^2=t^4+D^2\). Write \(t=u/v\) in lowest terms with \(v>0\). Then \(w=|s|v^2\) is an integer, since its square is the integer \(u^4+D^2v^4\). The inputs below have \(\gcd(u,D)=1\), so the terms \(u^4,D^2v^4,w^2\) are pairwise coprime. Absolute values of \(u\) can be taken throughout. The duplication formula gives the exact identity
\[
X(2Q)=\left(\frac{s}{t}\right)^2=\left(\frac{w}{uv}\right)^2 .
\]
The fraction \(w/(uv)\) is reduced and \(w^2\ge2D u^2v^2\). Thus its squared numerator gives the full logarithmic height of \(X(2Q)\):
\[
\log c=h(X(2Q))=8\widehat h(Q)+O_D(1).
\tag{2}
\]

For each prime \(\ell\mid 5D\), take the open subgroup of \(E(\mathbb Q_\ell)\) at the identity with formal parameter \(z=-X/Y\) in \(\ell\mathbb Z_\ell\). It has finite index by compactness, including at the bad primes. A common fixed positive multiple of the four points lies in all of these subgroups. Call the resulting independent points \(P_1,\ldots,P_4\). For a nonzero point in their span, \(t=-1/(2z)\) at each \(\ell\mid D\), so \(\ell\mid v\) and \(\ell\nmid u\). This proves the primitivity asserted above.

At 5 the subgroup with \(z\in5^k\mathbb Z_5\) has index \(5^{k-1}\) in the subgroup with \(z\in5\mathbb Z_5\), by the formal group filtration. Among the \((M+1)^4\) points \(\sum n_iP_i\) with \(0\le n_i\le M\), take two in the same coset for the largest \(k\) with \(5^{k-1}<(M+1)^4\). Their difference \(Q\) is nonzero, has coefficients of absolute value at most \(M\), and satisfies \(5^k\mid v\). Since \(5^{k-1}\ge(M+1)^4/5\), the associated triple satisfies
\[
\operatorname{rad}(abc)=\operatorname{rad}(Duvw)
\le D|uvw|/5^{k-1},\qquad
\frac{c}{\operatorname{rad}(abc)}
\ge 5^{k-1}\frac{w}{D|uv|}\gg_D M^4.
\]
On the other hand \(\widehat h(Q)\ll_D M^2\) by the quadratic height pairing on the four fixed points. Equation (2) proves (1). The lower bound tends to infinity, forcing infinitely many distinct triples.

For a numerical check, denote the four original table points in order by \(A_1,\ldots,A_4\). Taking \(Q=4A_1-4A_2-6A_3\) gives a 256-digit \(c\), \(\gcd(u,D)=1\), \(v_5(v)=4\), and \(125w>5D|uv|\). Thus \(c>5\operatorname{rad}(abc)\) for this point without factoring its large coordinates. The following PARI/GP commands reproduce the check. Here the numerator of \(t\) is taken in absolute value.

~~~gp
D = 14637;
E = ellinit([0,0,0,-(2*D)^2,0]);
A = [1771077,2356659459]; B = [142188,52467372]; F = [171462,69956496];
Q = elladd(E,elladd(E,ellmul(E,A,4),ellmul(E,B,-4)),ellmul(E,F,-6));
t = Q[2]/(2*Q[1]); u = abs(numerator(t)); v = denominator(t);
w = abs(Q[1]/2-t^2)*v^2;
[gcd(u,D), valuation(v,5), w^2==u^4+D^2*v^4, #digits(w^2), 125*w>5*D*u*v]
~~~

The output is \([1,4,1,256,1]\).

## A limit on increasing rank in this construction

Here \(D\) may be any odd positive squarefree integer and \(N=2D\). The following uniform bound concerns the number of points available on **one** twist at a time. For the primitive outputs with \(\gcd(u,D)=1\) and \(\log c\le H\), the number of generating rational points is at most
\[
\exp\!\left(O\!\left(\frac{H}{\log(2+H)}\right)\right)\qquad (H\ge2),
\tag{3}
\]
with absolute implied constant.

First \(E_N\) is isomorphic over \(\overline{\mathbb Q}\) to the fixed curve \(y^2=x^3-x\) via \(x=X/N,\ y=Y/(N\sqrt N)\). Thus \(h(X/N)=2\widehat h(Q)+O(1)\) with an absolute error. If \(X/N=j/k\) in lowest terms and \(Y\ne0\), then \(N j k(j-k)(j+k)=(Yk^2/N)^2\) is a nonzero integer square. Since \(N\) is squarefree, it divides \(jk(j-k)(j+k)\). Therefore \(h(X/N)\ge\tfrac14\log N-O(1)\). For non-torsion rational points this gives \(\widehat h(Q)\gg\log(2D)\) uniformly, using discreteness on the finitely many small twists. Conversely, for the stated outputs \(D\le\sqrt c\) and \(h(X(2Q))=\log c\). Applying the fixed-curve height estimate to \(2Q\) gives \(\widehat h(Q)\ll H\).

Full 2-descent bounds the rank \(r\) by \(2(\omega(2N)+1)\). Indeed, away from the primes dividing \(2N\), a positive valuation of \(X\) or \(X-N\) must be even by the curve equation and coprimality of the three local factors. A negative valuation of \(X\) is even as well. The torsion classes satisfy the same support bound. Thus both descent coordinates have only \(\omega(2N)+1\) possible binary sign and valuation coordinates. The rational torsion order is absolutely bounded by Mazur's theorem.

Put \(d=\log(2D)\). By \(s!\le2N\) for \(s=\omega(2N)\), \(r\ll d/\log(2+d)\). In the Euclidean norm \(\sqrt{\widehat h}\) on the free group the shortest nonzero length is \(\gg\sqrt d\). Disjoint balls about the points of norm \(O(\sqrt H)\) therefore bound their number, up to the absolute torsion factor, by \((1+C\sqrt{H/d})^r\). Since \(d\ll H\), the log of this bound is \(O(H/\log(2+H))\): split at \(d=\sqrt H\) and use \(d\log(1+C\sqrt{H/d})=O(H)\) in the larger range. This proves (3).

In particular, counting points of bounded height on a single twist and comparing that count to the number of formal group cosets cannot by itself force divisibility of size \(e^{\eta H}\) for fixed \(\eta>0\). This statement permits exceptional individual points and additional arithmetic restrictions on the occupied cosets.

## What remains for a disproof

The moving-prime condition on this fixed curve can be made exact up to \(o(\log c)\). The degree-two isogeny with kernel generated by \((0,0)\) sends the \(X\)-coordinate to \(X-N^2/X\) on the curve \(Y'^2=X'^3+4N^2X'\). Composing it with doubling gives
\[
X'(\phi(2Q))
=\left(\frac{u^4-D^2v^4}{uvw}\right)^2 .
\]
The displayed fraction is reduced. A prime dividing \(uv\) cannot divide its numerator since \((u,v)=(u,D)=1\). An odd prime dividing both \(w\) and the numerator would divide both \(2u^4\) and \(2D^2v^4\). Also \(u,v\) have opposite parity: with both odd, \(u^4+D^2v^4\) is 2 or 10 modulo 16. Thus \(w\) and the numerator are odd. Consequently \(|uvw|\) is exactly the square root of the reduced denominator of \(X'(\phi(2Q))\).

For any fixed elliptic curve over \(\mathbb Q\) and any fixed place \(\nu\), rational points \(A\) of increasing height satisfy \(\log^+|X(A)|_\nu=o(h(X(A)))\). One proof fixes \(m\) and writes \(A=[m]Z+T\), taking \(T\) from finitely many representatives modulo \(mE(\mathbb Q)\). The rational function \(X([m]Z+T)\) has poles of order two above the identity, since multiplication by \(m\) is unramified in characteristic zero. Near each such algebraic pole, use \(X(Z)\) or, at infinity, \(1/X(Z)\). Its difference from its value at the pole vanishes to order at least one. Local expansion therefore bounds \(\log^+|X(A)|_\nu\) by twice the local approximation logarithm for this rational coordinate, plus \(O_{m,E,\nu}(1)\). The real or \(p\)-adic Roth theorem bounds that logarithm by \((2+\epsilon)h(X(Z))+O_{m,E,\nu,\epsilon}(1)\); for a rational target the elementary height bound suffices. Exact equalities of coordinates account for only finitely many points for each \(m\). Away from the poles the local function is bounded by compactness. Finally \(h(X(Z))/h(X(A))\to1/m^2\) by the canonical height pairing. Letting \(m\) increase proves the assertion.

Apply this first to \(2Q\) at the real place, then to \(\phi(2Q)\) at each prime in a fixed finite set \(S\). The height of the latter coordinate is at most \(2\log c\) by the reduced fraction above. Hence \(\log(w/|uv|)=o(\log c)\) and \(\sum_{p\in S}v_p(uvw)\log p=o(\log c)\). Since \(D\) is fixed, this gives
\[
\log\!\left(\frac{c}{\operatorname{rad}(abc)}\right)
=\sum_{p\notin S}\max(v_p(uvw)-1,0)\log p+o(\log c).
\tag{4}
\]
In particular the single prime 5 used in (1) cannot by itself furnish a fixed-power disproof even by exceptional congruences at unbounded heights on this curve. A positive limit superior of the sum in (4) divided by \(\log c\) would give such a disproof.

For the fixed \(D=14637\) family with \(\gcd(u,D)=1\), the full radical can be small for reasons besides the forced factor at 5. In fact the squarefree part of \(w\) tends to infinity as \(c\) tends to infinity. Fixing \(w=d_0 m^2\) gives the smooth plane quartic \(u^4+D^2v^4=d_0^2m^4\), of genus 3. For fixed \(d_0\), Faltings' theorem gives only finitely many rational projective points, and coprimality fixes the integer representatives up to signs. This gives no growth rate on the scale of \(c\). Neither (1) nor (3) decides whether \(c/\operatorname{rad}(abc)\ge c^\eta\) can hold infinitely often on this family for some fixed \(\eta>0\).
