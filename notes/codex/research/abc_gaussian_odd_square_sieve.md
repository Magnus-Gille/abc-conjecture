# A square sieve for primitive primes of odd exponent at prime ranks

Let \(G=(-3,9)\) on \(E:y^2=x^3-36x\), and \(B_n^2\) be the reduced denominator of \(X(nG)\). Put \(P_{\rm odd}(n)=P^+(\operatorname{sf}(B_n))\) when the kernel is greater than one. For every \(u(X)\to\infty\), a relative density-one set of primes \(r\equiv3\bmod4\) satisfies
\[
       P_{\rm odd}(r)>
       \frac{r^2(\log r)^2}{\log_2 r\,u(r)}.                         \tag{1}
\]
Each such prime divisor has first appearance at \(r\). Infinitely many prime \(r\equiv3\bmod8\) satisfy the same inequality with \(u(r)\) replaced by an absolute constant. These are lower bounds for a prime base occurring to odd exponent, allowing exponent one or any larger odd integer. The prime in (1) need not itself be \(13\bmod24\).

Here is another consequence. Fix \(k\ge1\) and \(0<\delta<1/(4k)\). At a relative density-one set of prime ranks \(r\equiv3\bmod4\), either \(P_{\rm odd}(r)>r^{2+\delta}\), or \(B_r\) has at least \(k+1\) distinct prime factors with odd exponent. Moreover for every \(0<\delta<1/4\) one has \(\operatorname{sf}(B_r)>r^{2+\delta}\) at relative density one: the alternative for \(k=1\) gives a product of two distinct bases, both \(\gg r^2\).

## Possible products in the window

Take \(r\in[X,2X]\) prime, \(r\equiv3\bmod4\). Every \(p\mid B_r\) has exact order \(r\) and is of the form \(N(1+r\alpha)\), \(\alpha=a+bi\in\mathbf Z[i]\), \(b>0\). If \(p\le r^2Y\) with \(Y\ge1\), then \(N\alpha\le4Y\) for large \(X\), uniformly in \(Y\). There are \(O(Y)\) oriented choices. Write \(A_r(Y)\) for the number of these choices giving a *prime* norm at \(r\), whether or not \(rG\equiv O\bmod p\). The averaged dimension-two sieve, with its bounds uniform for the coefficient box, proves
\[
                \sum_{r\in[X,2X]\ {\rm prime}} A_r(Y)
                    \ll XY/(\log X)^2.                              \tag{2}
\]
For (1) only \(Y\) of polylogarithmic size is needed in (2). [Gaussian norms, averaged sieve and odd-exponent character](abc_gaussian_odd_primitive_prime_gaps.md)

If all odd-valuation primes at \(r\) lie in the window and their number is \(j\ge1\), select one orientation for each such distinct prime. With \(\mathcal A\) the resulting set, the integer \(B_r F_{\mathcal A}(r)\) is a square, where
\[
    F_{\mathcal A}(t)=\prod_{\alpha\in\mathcal A}(1+\alpha t)(1+\bar\alpha t).
\]
Its value at \(r\) equals \(\operatorname{sf}(B_r)\). In particular it has no auxiliary prime divisor below \(r\) at this index. For \(r\equiv3\bmod8\), nonsquareness is already elementary since \((2/B_r)=-1\). For \(r\equiv7\bmod8\) the independent elliptic Chabauty classification gives \(B_r\) nonsquare at every such prime. [All square denominators](abc_full_quartic_square_chabauty5.md)

## Uniform bound for one possible nonempty product

Let \(Z=X^{1/4}\), and let \(\mathcal P\) consist of the primes \(q\equiv1\bmod4\) in \([Z,3Z/2]\); put \(H=|\mathcal P|\asymp Z/\log Z\). For odd \(n\) set \(c_q(n)=(B_n/q)\), with value zero if \(q\mid B_n\). This sequence on odd indices has period \(4s_q\), \(s_q=\operatorname{ord}_q(G)\).

To prove the period, write \(W_j=\psi_j(G)\) for the signed division polynomials. For odd \(n\), the scaling from \(T=(-1,\sqrt3)\) to \(G\) gives \(W_n=3^{(n^2-1)/2}f_n\) with a square multiplier and \(B_n=|f_n|\), as shown in the preceding source. Since \(q\equiv1\bmod4\), sign leaves the quadratic character unchanged even when the denominator vanishes modulo \(q\). The division-polynomial addition identity gives
\[
        W_{v+s}W_{v-s}=\phi_s(G) W_v^2-\phi_v(G) W_s^2 ,
                  \qquad s=s_q ,
\]
where \(X(jG)=\phi_j(G)/W_j^2\). This follows from the usual abscissa difference formula; the identity is polynomial and may be reduced at \(W_s=0\). At this good prime \(W_s=0\bmod q\) and \(\phi_s(G)\ne0\bmod q\): multiplication by \(s\) maps the reduction of \(G\) to the identity, with coprime projective abscissa coordinates. For \(s\nmid n\), setting \(v=n+s\) gives \((W_{n+2s}/q)=(\phi_s(G)/q)(W_n/q)\). For \(s\mid n\) the terms are both zero. Iteration gives period \(4s\) for the character. The sequence may be set to zero at even indices with the same period.

The full rational 2-torsion survives at every auxiliary prime. The finite group has a factor of order two outside any cyclic subgroup containing \(G\), since a cyclic group has at most one element of order two. Hence \(s_q\le\#E(\mathbf F_q)/2<Z\) for large \(X\) by Hasse and \(q\le3Z/2\). Thus for distinct \(q,q'\in\mathcal P\), both are prime to \(M=\operatorname{lcm}(4s_q,4s_{q'})\), with \(M\ll Z^2\). The restriction to prime \(r\ge X\) ensures \(q\nmid B_r\), as \(q<r\) and \(\operatorname{ord}_q(G)\) cannot be \(r\).

Suppose \(Y\le Z/100\), and \(F=F_{\mathcal A}\) has \(j\) factors. In \(\mathbf F_q\) all \(2j\) roots are distinct. Indeed, choose either reduction \(i\mapsto\sqrt{-1}\). No Gaussian coefficient vanishes since \(0<N\alpha\le4Y<q\). If two reciprocal negative coefficients coincide, \(q\) divides the norm of the difference of the corresponding signed Gaussian coefficients. These norms are nonzero since every \(b>0\), the chosen elements are distinct, and conjugates are taken once apiece. Each difference has norm at most \(16Y<q\). This treats collinear distinct coefficients as well. The internal pair \(\alpha,\bar\alpha\) has the same bound. Thus the complete quadratic-character sum of \(F\) modulo \(q\) has absolute value at most \((2j-1)\sqrt q\) by Weil.

For distinct \(q,q'\), the product \(c_q(n)c_{q'}(n)\) on odd \(n\), extended by zero at even \(n\), is a weight bounded by one and periodic modulo \(M\). The full weighted sum of \((F(n)/q)(F(n)/q')\) factors over a period \(Mqq'\) by the Chinese remainder theorem. Its mean has absolute value at most \((2j-1)^2/\sqrt{qq'}\). For a sharper incomplete bound, separate the classes \(n=h\bmod M\) and sum over consecutive \(t=(n-h)/M\) in each. At every additive character modulo \(q\), the complete hybrid sum with \((F(h+Mt)/q)\) is \(O(j\sqrt q)\): at frequency zero this is the preceding Weil bound, and at nonzero frequencies the linear additive phase gives the standard mixed Weil bound. The same holds modulo \(q'\). As \(M\) is a unit modulo both primes, the simple-root hypothesis continues to hold for these affine changes. All complete Fourier coefficients modulo \(D=qq'\) thus have absolute value \(O(j^2\sqrt D)\). Completion using the geometric sum of each frequency bounds the error from the zero-frequency mean on an interval of arbitrary length by \(O(j^2\sqrt D\log(2D))\). Multiplying by the weight of each class and summing over the \(M\ll Z^2\) classes gives
\[
 \left|\sum_{\substack{X\le n\le2X\\n\ {\rm odd}}}
                 c_q(n)c_{q'}(n)(F(n)/q)(F(n)/q')\right|
                        \ll j^2(X/Z+ Z^3\log(2Z)).                 \tag{3}
\]

At every target rank \(r\) for this particular polynomial, \(F(r)=\operatorname{sf}(B_r)\) and \(q\nmid F(r)B_r\) for all \(q\in\mathcal P\). Hence \(\sum_{q\in\mathcal P}c_q(r)(F(r)/q)=H\). Majorize the number of these ranks by \(H^{-2}\) times the sum of the square of this expression over all odd integers \(n\) in the interval. The diagonal is at most \(X/H+O(1)\) after normalization; zero characters at nontarget integers cause no problem. From (3) we obtain
\[
             \#\{r\ {\rm target\ for}\ F\}\ll X/H+j^2(X/Z+Z^3\log(2Z))
                      \ll X^{3/4}(1+j^2)\log X.                     \tag{4}
\]
All constants in this bound are independent of the coefficient choices.

## Summing the polynomial possibilities

Write \(L=\log X,\ l=\log_2 X\), \(K=\lfloor L/(40l)\rfloor\), and take \(1\le Y\le L^2/l\). The number of distinct nonempty subsets of at most \(K\) choices is bounded by \(\sum_{j=1}^K(CY)^j\le X^{1/20+o(1)}\). Applying (4) to all these polynomials shows that at most \(X^{4/5+o(1)}\) ranks can have all odd-exponent primes in the window and at most \(K\) of them. All remaining ranks with the same small-prime property have \(A_r(Y)>K\); (2) bounds their number by \(O(XYl/L^3)\). In particular
\[
  \#\{X\le r\le2X:\ r\equiv3(4)\text{ prime},\ P_{\rm odd}(r)\le r^2Y\}
       \ll XY\log_2 X/(\log X)^3+X^{4/5+o(1)}
\]
for the indicated range. For \(Y=o(L^2/l)\) this is \(o(X/L)\). Dyadic summation and a monotone lower envelope for \(u(r)\) give (1) in natural relative density. For \(Y=cL^2/l\) with \(c>0\) sufficiently small, a positive relative proportion remains even among \(r\equiv3\bmod8\), by the prime number theorem for this progression.

For the fixed-power alternative put \(Y=(2X)^\delta\). If \(1\le j\le k\), the nonempty family has size \(O_k(X^{k\delta})\). The hypothesis \(k\delta<1/4\) keeps \(16Y<Z\) eventually and makes the summation of (4) \(o(X/\log X)\). Thus except at a density-zero set, absence of a large odd-exponent prime forces \(j\ge k+1\). For \(k=1\), any two primitive bases already have product \(\gg r^4\) by the Gaussian norm bound. This proves the claim for \(\operatorname{sf}(B_r)\).

These estimates do not establish a prime of odd exponent exceeding \(r^{2+\delta}\) for any fixed \(\delta>0\) along an infinite sequence; the fixed-power alternative allows multiple small bases at every candidate rank. [Explicit least-prime gap construction](abc_gaussian_odd_primitive_prime_gaps.md)
