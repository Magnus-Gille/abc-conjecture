# Effective exclusion of perfect powers outside any prescribed primes on the Pell orbit

Write \(b_n+a_n\sqrt2=\epsilon^n\), with \(\epsilon=1+\sqrt2\), and \(M_n=|F_{11}(a_n,b_n)|\). For every finite set \(S\) of rational primes there is an **effectively computable** \(N(S)\) such that

\[
       \gcd\{v_p(M_n):p\mid M_n,\ p\notin S\}=1
       \qquad(n>N(S)).
\]

The set in the gcd is then nonempty. Thus there are only effectively finitely many perfect powers on the orbit, with the exponent allowed to vary. More generally put

\[
       P_{n,k}=\max\{p\mid M_n:k\nmid v_p(M_n)\},\qquad k\ge2,
\]

with maximum 1 for an empty set. Then \(\inf_{k\ge2}P_{n,k}\to\infty\) effectively. The same lower bound applies to the \(k\)-th-power-free part and to the product of primes having exponent nonzero modulo \(k\). There is also the following quantitative estimate, with an effective absolute constant for this fixed orbit,

\[
 P_{n,k}\gg \frac{\log T\,\log\log T}{\log\log\log T},
 \qquad T=\min(n,k)
\]

for sufficiently large \(T\). Taking \(k\) larger than all valuations gives this bound with \(T=n\) for the greatest prime factor of \(M_n\). A gcd of one allows all individual exponents to exceed one.

## Reducing the index modulo the putative power

Let \(L(X)\in\mathbb Z[\sqrt2][X]\) be the degree-50 polynomial obtained by taking the full torsion abscissa factor \(G\) and forming

\[
 L(X)=(X+1)^{50}G\left(\frac{(-8-4\sqrt2)X-8+4\sqrt2}{X+1}\right).
\]

The Möbius substitution preserves separability since its determinant is nonzero. It preserves degree 50 since \(G(-8-4\sqrt2)\ne0\), and \(L(0)=G(-8+4\sqrt2)\ne0\). Indeed the two arguments of \(G\) are two-torsion abscissas whereas its roots come from order 11. The Pell parametrization and the primitive normalization give

\[
 F_{11}(a_n,b_n)=-2^{-175}\epsilon^{-100n}L(\epsilon^{4n}).
\]

In particular there is a fixed positive \(A=2^{-175}|\operatorname{lc}(L)|\) and an effective constant \(c_0\) such that for all sufficiently large \(n\)

\[
           0<\left|M_n/(A\epsilon^{100n})-1\right|\le c_0\epsilon^{-4n}.
                                                              \tag{1}
\]

The sign stabilizes by dominance. The difference on the left could vanish only at a root of \(L(X)-\operatorname{lc}(L)X^{50}\). Its nonzero constant coefficient and Cauchy's root bound give an effective starting index. [Torsion polynomial construction](abc_cm_twist_depth_example.py) · [Pell specialization](abc_cm_pell_target_gcd.md)

Suppose all valuations outside \(S\) are multiples of \(k\). By taking the exponents at \(S\) modulo \(k\) one obtains

\[
          M_n=y^k\prod_{p\in S}p^{u_p},\qquad 0\le u_p<k,
          \qquad y\in\mathbb Z_{\ge1}.
\]

If \(y\ge2\), then \(k\ll n\) and \(\log y\ll n/k\), with constants depending only on \(L\). Write \(n=tk+r\) with \(0\le r<k\), and put \(\beta=y\epsilon^{-100t}\). The ratio appearing in (1) is exactly

\[
       A^{-1}\beta^k\epsilon^{-100r}\prod_{p\in S}p^{u_p}.
\]

All factors are positive at the chosen real embedding of \(\mathbb Q(\sqrt2)\). The absolute logarithmic height of \(\beta\) is \(O(1+n/k)\). Every exponent on the right has absolute value at most \(100k\), because the quotient \(t\) has been absorbed in \(\beta\). Apply Matveev's real multiplicative lower bound to this product minus one, omitting factors equal to one and using coefficient 1 for the fixed factor \(A^{-1}\). Comparison with (1) gives

\[
             n\ll C(S)(1+n/k)\log(2k),\qquad
             k\ll C(S)\log(2k).                              \tag{2}
\]

Here and below the constants are effective. The second inequality uses \(k\ll n\). In particular (2) gives an effectively computable upper bound \(K(S)\) on all possible exponents in this case. If \(y=1\), the value is \(S\)-smooth. In (1) use only the fixed numbers \(A^{-1},\epsilon,p\ (p\in S)\), and the actual valuations \(v_p(M_n)\ll n\) as exponents. The same theorem gives \(n\ll C(S)\log(2n)\), which bounds all these indices. [Matveev, *An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers II*](https://doi.org/10.1070/IM2000v064n06ABEH000314)

## Effective enumeration of the remaining indices

For each \(2\le k\le K(S)\) and each of the finitely many choices of \(r,(u_p)_{p\in S}\), use \(x=\epsilon^{4n}\) and \(z=\epsilon^{100t}y\). Both are algebraic integers in \(\mathbb Q(\sqrt2)\). The Laurent identity and the sign of the original value give the equation

\[
          L(x)=b z^k,\qquad
          b=\pm 2^{175}\epsilon^{100r}\prod_{p\in S}p^{u_p}.
\]

The coefficient \(b\) is one of an explicit finite list of nonzero algebraic integers. The explicit hyperelliptic and superelliptic height bounds of Bérczes, Evertse and Győry apply over \(\mathbb Q(\sqrt2)\) with just its archimedean places. The polynomial is separable of degree 50, so it meets the degree requirement both for squares and for higher powers. For each entry, take the given upper bound for \(h(x)\) and divide by \(4h(\epsilon)=2\log\epsilon\). The maximum of these results together with the earlier bounds is an effective \(N(S)\). If an odd or even common divisor of all the positive valuations outside \(S\) existed past this index, one could take its prime divisor for \(k\). The \(S\)-smooth case also cannot occur, proving the gcd assertion. [Bérczes, Evertse and Győry, *Effective results for hyper- and superelliptic equations over number fields*](https://arxiv.org/abs/1301.7168)

## Dependence on the size of the exceptional primes

For rational primes \(S=\{p:p\le P\}\), put \(s=|S|\). In the degree-two real case the factor from Matveev's bound with at most \(s+3\) logarithms is \(O(30^{s+6}(s+3)^{4.5})\) times the product of the logarithmic heights or logarithmic absolute values, each enlarged by a fixed positive minimum. The factors from the primes can be taken as \(\max(1,2\log p)\). Those from \(A,\epsilon\) are fixed, and the factor from \(\beta\) was displayed separately in (2). The elementary estimate \(s\ll P/\log P\) now gives, for \(P\ge3\),

\[
              \log C(S)\ll 1+P\frac{\log\log(3P)}{\log(3P)} .
\]

Choose \(P=\max(3,P_{n,k})\). In the case \(y\ge2\), (2) bounds \(\log k\) by \(O(1+\log C(S))\). In the case \(y=1\), the smooth-value inequality gives the same bound for \(\log n\). Inverting the resulting inequality for \(\log\min(n,k)\) proves the quantitative assertion. For fixed small \(k\), the effective bound \(N(S)\) in the preceding section gives a computable threshold for each desired \(P\).
