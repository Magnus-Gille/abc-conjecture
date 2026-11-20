# A degree-32 Belyi map on the mixed elliptic curve

Let \(E:v^2=u^3-8u^2+8u\), and let \(A=(1,1)\) and \(\tau=\sqrt{-2}\) under the complex multiplication of \(E\). There is a rational Belyi map of degree 32 whose fibre over one contains both \(\tau A\) and \(-\tau A\), each with multiplicity one. All four points of \(E[2]\) also lie over \(0,1,\infty\). The value of the map depends only on \(u\).

## Formula

First set \(z=8(u-3)^2/(u+4)^2\). The slope map has branch abscissas \(\infty,0,4+2\sqrt2,4-2\sqrt2\), and \(u(\pm\tau A)=-1/2\). The fractional linear expression inside the square was chosen to identify the two conjugate abscissas and to identify \(\infty\) with \(-1/2\) after squaring. The only critical values of \(z\) itself are zero and infinity.

| Input abscissa \(u\) | \(z\) |
|---|---:|
| \(\infty,-1/2\) | \(8\) |
| \(0\) | \(9/2\) |
| \(4+2\sqrt2,4-2\sqrt2\) | \(1\) |

For this configuration take the degree-eight map
\[
 F(z)=\frac{7^7z^2(6z+1)}{(z-1)^3(5z+9)(50z^2-345z-48)^2},\qquad
 1-F(z)=\frac{(z-8)(2z-9)^2(5z+2)^5}{(z-1)^3(5z+9)(50z^2-345z-48)^2}.
\]
Its fibres over zero and one have respective ramification partitions \((5,2,1)\) and \((5,2,1)\); the fibre over infinity has partition \((3,2,2,1)\). The displayed factors have distinct roots within and across the three fibres. Their ramification contributions sum to \(14=2\cdot8-2\), so these are all the branch values. In particular \(z=0,\infty\) go to zero, \(z=9/2,8\) to one, and \(z=1\) to infinity. Composition with the degree-two map \(E\to\mathbb P^1_u\) and the degree-two map \(u\mapsto z\) now gives the claimed Belyi map.

The degree-eight formula was located using the database of Musty, Schiavone, Sijsling and Voight. In the database coordinate for the entry below, substituting \(145/(30z-91)\) gives \(F(z)\). The two factorizations above verify the construction independently of the database. No minimality claim is needed. [Database entry](https://github.com/michaelmusty/BelyiDB/blob/master/belyi_db/8/8T50-%5B10%2C10%2C6%5D-521-521-3221-g0.m) · [Database paper](https://arxiv.org/abs/1805.07751)

## Rational factorization on \(E\)

Write \(\beta=F(z(u))=N(u)/D(u)\). Direct substitution gives
\[
\begin{aligned}
 N(u)&=(u-3)^4(u+4)^{10}(7u^2-40u+64),\\
 D(u)&=(u^2-8u+8)^3(7u^2-24u+72)(u^4-114u^3+591u^2-744u-384)^2,\\
 D(u)-N(u)&=-4u^2(u-24)^2(2u+1)(3u^2-16u+28)^5.
\end{aligned}
\]
The degree of the last polynomial is 15, so one additional simple zero occurs at infinity on the \(u\)-line. Over \(u=-1/2\) the map \(E\to\mathbb P^1_u\) is unramified, and the factor \(2u+1\) is simple. In the full mixed parametrization \(u([N_0]A)=(s^2-2t^2)^2/(YV)\) with \(Y=s^2+2t^2,\ V=(s-t)^2+t^2\). The factor \(2u+1\) consequently pulls back to
\[
 \frac{((s+t)^2+t^2)(3s^2-8st+6t^2)}{YV}.
\]
Thus both marked quadratic factors occur in the same special fibre. At the marked abscissa, \(D(-1/2)=7^{17}/2^{16}\) and \(((D-N)/(2u+1))(-1/2)=-3^5 7^{14}/2^{12}\). For any odd \(p\ne3,7\) at which \(2u+1\) has positive valuation, it follows that \(v_p(1-\beta)=v_p(2u+1)\). [Full mixed parametrization](abc_octic_full_mixed_orbit.md)

On \(E\) the three geometric ramification partitions are
\[
\begin{array}{c|c|c}
\text{value}&\text{partition}&\sum(e-1)\\ \hline
0&(10^2,4^2,1^4)&24\\
1&(5^4,4,2^3,1^2)&22\\
\infty&(6^2,2^8,1^4)&18 .
\end{array}
\]
Superscripts in this table indicate the number of occurrences. The sum \(64\) agrees with Riemann–Hurwitz on a genus-one source. The verifier checks the three polynomial identities by interpolation after clearing denominators and checks squarefreeness of the reduced fibre supports over \(\mathbb F_{101}\), preserving each degree. [Standard-library verifier](abc_octic_mixed_belyi_verify.py)
