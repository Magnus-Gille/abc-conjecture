# Distinct primes at a single elliptic index

Let \(E:y^2=x^3-36x\), \(G=(-3,9)\), and let \(B_m\) denote the positive square root of the reduced denominator of \(x([m]G)\). For \(p\ge5\), let \(r_p\) be the order of \(G\) in \(E(\mathbf F_p)\). Thus \(r_p=r\) means that \(p\) divides \(B_r\) for the first time. The point \(G\) has infinite order. Indeed \(x(2G)=25/4\), and Nagell–Lutz applies to this integral short equation.

For every sufficiently large **odd** \(r=\prod\ell^{k_\ell}\), at least
\[
 \frac{1+\prod_{\ell\mid r,\ \ell\equiv1\bmod4}(2k_\ell+1)}2
 \tag{1}
\]
distinct rational primes have \(r_p=r\). Every one of these primes is \(1\bmod12\). In particular the lower bound is \((3^k+1)/2\) when \(r\) is a product of \(k\) distinct primes \(1\bmod4\).

For \(r=\prod_{\ell\le X,\ \ell\equiv1\bmod4}\ell\), put \(R_r=\prod_{p:r_p=r}p\). Hasse's bound gives \(p\ge(\sqrt r-1)^2\), and the prime number theorem in arithmetic progressions gives
\[
 \log\log R_r\ge(\log 3+o(1))\frac{\log r}{\log\log r}.
\]
This lower bound on \(\log R_r\) grows faster than every fixed power of \(\log r\). An estimate for abc on this orbit would need to control logarithmic mass on the scale \(r^2\).

## Why the real component controls every odd Gaussian index

Work over \(K=\mathbf Q(i)\) with \(\mathcal O=\mathbf Z[i]\) and \([i](x,y)=(-x,iy)\). Use flat distance on the complex torus \(E(\mathbf C)\); \([\alpha]\) is Lipschitz with constant \(|\alpha|\). The point \(G\) lies on the compact real component with \(-6\le x\le0\), separated by a positive distance \(c_E\) from \(O\). This component is the nonidentity coset in the two-component real group. For each Gaussian integer \(\alpha\) of odd norm, \([N\alpha]G\) belongs to that same component, whence
\[
 c_E\le d([N\alpha]G,O)\le |\alpha|\,d([\alpha]G,O).
\]
The abscissa has a double pole at \(O\) and is bounded on compact sets away from \(O\). Consequently \(\log^+|x([\alpha]G)|_\infty\le\log N\alpha+O_E(1)\), including when both Gaussian coefficients have a large common divisor.

## Exact annihilators and heights

For a prime ideal \(\mathfrak p\nmid6\) let \(\mathfrak a_{\mathfrak p}\) be the ideal of Gaussian integers annihilating the reduction of \(G\). It is nonzero. At a generator \(\gamma\) of \(\mathfrak a_{\mathfrak p}\), let \(e_{\mathfrak p}\ge1\) denote the formal depth of \([\gamma]G\), measured by the integral parameter \(-x/y\). The depth is independent of multiplying \(\gamma\) by a unit. Write
\[
 L(\mathfrak a)=\sum_{\mathfrak a_{\mathfrak p}=\mathfrak a} e_{\mathfrak p}\log N\mathfrak p .
\]
Annihilators, depths, and norms refer to prime ideals of \(K\) in this formula. At a good prime \(p\ge5\), \(K\) is unramified and the formal logarithm is an isometry on the maximal ideal. If \(\gamma\mid\alpha\), the depth of \([\alpha]G\) is \(e_{\mathfrak p}+v_{\mathfrak p}(\alpha/\gamma)\); otherwise \([\alpha]G\) is outside the formal group at \(\mathfrak p\). The sum of all additional depths weighted by \(\log N\mathfrak p\) is between zero and \(\log N\alpha\).

Write \(H=\widehat h(G)>0\), with convention \(h(x(G'))=2\widehat h(G')+O_E(1)\). Since \(\widehat h([\alpha]G)=N\alpha\,H\), the log norm of the denominator ideal of the *point* \([\alpha]G\) (half the log norm of the abscissa denominator ideal) equals \(2H N\alpha-\log^+|x([\alpha]G)|_\infty+O(1)\). The factor two comes from \([K:\mathbf Q]=2\). At each prime over 2 or 3, fix \(m\) so that \(mG\) belongs to an isometric formal-logarithm neighborhood. Then \(m[\alpha]G=[\alpha]mG\) has depth \(v_{\mathfrak p}(\alpha)+O_E(1)\), by applying the formal logarithm. Integral formal multiplication by \(m\) cannot decrease a positive depth of \([\alpha]G\). These assertions apply on the given integral model; the automorphism \([i]\) preserves its formal group. The omitted primes therefore cost \(O_E(\log(2N\alpha))\) in total.

For every odd-norm \(\alpha\) we have proved
\[
 \sum_{\mathfrak a\mid(\alpha)} L(\mathfrak a)
 = 2H N\alpha+O_E(\log(2N\alpha)).
\]
Every divisor also has odd norm. Möbius inversion on ideals gives
\[
 L((\alpha)) =
  2H N\alpha\prod_{\mathfrak q\mid(\alpha)}(1-1/N\mathfrak q)
  + O_E\!\left(2^{\omega((\alpha))}\log(2N\alpha)\right).
 \tag{2}
\]
Here \(\omega((\alpha))\) counts distinct Gaussian prime ideals. In particular \(L((\alpha))>0\) for all sufficiently large odd norms, uniformly over the ideals: the main term is \((N\alpha)^{1-o(1)}\) and the error is \((N\alpha)^{o(1)}\). These elementary estimates follow by separating off the finitely many prime ideals of norm below any fixed bound. Formula (2) is an asymptotic for the actual first depths, including repetitions.

## Counting distinct rational primes

The rational order is the positive generator of \(\mathfrak a_{\mathfrak p}\cap\mathbf Z\). An annihilator of order \(r\) therefore divides \((r)\) and has norm at least \(r\), since \(\mathcal O/\mathfrak a_{\mathfrak p}\) contains the cyclic subgroup \(\mathbf Z/(r)\). For each \(\ell^k\parallel r\) that splits in \(K\), the exponents of the two prime ideals can be any pair \(0\le i,j\le k\) with \(\max(i,j)=k\). This gives \(2k+1\) choices. An inert \(\ell\) requires exponent \(k\) at its single prime ideal. Thus exactly the product in (1) Gaussian ideals contract to \((r)\). Conjugation fixes only the ideal \((r)\) in this list. Every one of the ideals occurs for large \(r\), by (2). A rational prime can realize at most one conjugate pair of ideals because \(G\) is rational. This proves (1).

At any good prime of odd order, \(G\bmod p\) is a double. On \(y^2=x(x-6)(x+6)\) the abscissa differences \(x,x-6,x+6\) of a double are all squares, by the full rational two-torsion descent (or by duplication after translating each root to zero). At \(G\) these values are \(-3,-9,3\). This makes \(-1\) and \(3\) quadratic residues and forces \(p\equiv1\bmod12\).

At rational order 1105 the four choices having Gaussian norm 1105 give, respectively, the prime witnesses 4549, 4701941281, 35593, and 181957. For each witness the modular calculation checks \([1105]G=O\) and \([1105/\ell]G\ne O\) for \(\ell=5,13,17\), along with its Gaussian annihilator. [Exact prime certificates](abc_gaussian_order_witness.md)

## Relation to abc

At \(x([n]G)=A/B^2\) in lowest terms, the identity
\[
 \min\{(A-6B^2)^2,(A+6B^2)^2\}+24|A|B^2
       =\max\{(A-6B^2)^2,(A+6B^2)^2\}
\]
gives a positive integer abc triple after division by the common gcd. This gcd divides \(144\): it is the gcd of the two squares, and \(\gcd(A-6B^2,A+6B^2)\mid12\) by \((A,B)=1\). Its largest term has logarithm \(4Hn^2+O(1)\). At \(p\ge5\) the three terms together have support exactly where \([n]G\) reduces to one of the four rational two-torsion points (including \(O\)). This is the good-prime support of \(B_{2n}\).

For any sequence \(n\to\infty\), the archimedean elliptic Siegel estimate gives \(\log B_{2n}=4Hn^2+o(n^2)\). For instance, divide the index by a fixed integer \(m\), approximate the finitely many translated \(m\)-division points of \(O\) with rational abscissas, and apply Roth's theorem; the resulting upper limit for the archimedean proximity divided by \(n^2\) is \(O(1/m^2)\). Letting \(m\) grow proves the estimate. The finitely many bad primes contribute \(O(\log(2n))\) to the denominator by formal multiplication.

Put \(W_r=\sum_{p\ge5,\ r_p=r}(v_p(B_r)-1)\log p\). Ordinary formal lifting gives
\[
 \log(B_m/\operatorname{rad} B_m)=\sum_{r\mid m}W_r+O(\log(2m)).
\]
Thus abc for this family for every positive exponent is equivalent to \(W_r=o(r^2)\) for all integer indices. One direction uses \(\sum_{r\mid 2n}r^2\le4\zeta(2)n^2\). For the reverse, take \(n=r\), so \(W_r\) is one nonnegative term of the sum. Positive density or large cardinality of first-appearance primes supplies no bound on \(v_p(B_r)-1\) at the other primes of the same index. A fixed positive lower bound on \(W_r/r^2\) at unbounded indices would give rational abc counterexamples.
