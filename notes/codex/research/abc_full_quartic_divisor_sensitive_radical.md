# A divisor-sensitive bound for the full radical

Let \(n>1\) be odd and use the positive coprime odd coordinates \(a,w,c,d\) of the congruent-six orbit. Set \(C=4w^4,\ R=\operatorname{rad}(6awcd)\), and let \(\tau(n)\) be the number of positive divisors. Then
\[
             R(\log R)^{27/2}\gg n^{9+\tau(n)/4}.                         \tag{1}
\]
In particular \(R\gg n^{19/2}/(\log n)^{27/2}\) and \(\log C\ll R^{4/19}(\log R)^{54/19}\). For varying \(\tau(n)\), set \(k=9+\tau(n)/4\). The inversion of (1) is uniform in the form
\[
                 R\gg n^k/(k\log n)^{27/2}.
\]
Indeed if \(R\ge n^k\) the conclusion is immediate, and otherwise \(\log R\le k\log n\). For the fixed-exponent special case one first replaces \(k\) in (1) by \(19/2\).

Put \(U=2w-c\), \(V=2w+c\). The three coprime triples
\[
               a^2+c^2=2w^2,\qquad U+V=4w,\qquad U+2c=V
\]
are positive and have radicals
\[
            \operatorname{rad}(2acw),\quad
            \operatorname{rad}(6wd),\quad
            \operatorname{rad}(6cd).
\]
Here \(UV=3d^2\), \((U,V)=1\), and \((U,c)=1\). The prime 2 occurs three times, and 3 occurs only in the last two, including if \(3\mid d\). The product is therefore exactly \(2R^2/\operatorname{rad}(a)\). The maximum term in each triple exceeds \(w\). Apply the Stewart–Yu theorem to the smallest radical to obtain
\[
          (\log w)^9\operatorname{rad}(a)\ll R^2(\log R)^{27}.
\]
[Height, coprimality and effective Stewart–Yu normalization](abc_full_quartic_stewart_yu_radical.md)

At index 3 the coordinates are \((a,w,c,d)=(23,37,47,33)\), so \((U,V)=(27,121)\). The radicals of the three triples are \(79{,}994\), \(2{,}442\) and \(3{,}102\). Their product is \(605{,}961{,}269{,}496=2(2{,}639{,}802)^2/23\). Here \(3\mid d\), which illustrates why 3 appears twice in the radical product.

The \(a\)-arm is the denominator sequence of the integral nontorsion point \(G+(0,0)=(12,36)\) on \(E:y^2=x^3-36x\) at odd indices. Silverman's elliptic primitive-divisor theorem gives a primitive good prime \(p_j\) at every sufficiently large \(j\). Such a prime has exact order \(j\) on this generator. Thus at odd \(j\), \(4j\mid\#E(\mathbf F_{p_j})\), implying \(p_j\ge(2\sqrt j-1)^2>j\). At every \(j\mid n\) the prime divides \(a_n\). Different qualifying divisors give distinct primes. If \(J\) bounds the exceptional indices, the omitted small divisors have product at most \(J!\), uniformly for all \(n\). Therefore
\[
 \operatorname{rad}(a_n)\ \ge\ \frac1{J!}\prod_{j\mid n}j
        =\frac{n^{\tau(n)/2}}{J!}.
\]
Combining this with \(\log w\asymp n^2\) proves (1). The theorem invoked is J. H. Silverman, *Wieferich's criterion and the abc-conjecture*, Journal of Number Theory 30 (1988), 226–237. Equivalently, eventual primitivity follows directly from the four-arm asymptotic \(\log a_j=Hj^2+o(j^2)\) and the divisor argument for odd \(j\), since \(\sum_{\ell\ge3,\ \ell\ {\rm prime}}\ell^{-2}<1/4\). The fixed exceptional threshold is not evaluated here. [Four-arm asymptotics and divisibility](abc_full_quartic_signature.md)

Separately, [three uniformly primitive arms](abc_full_quartic_pointwise_index_bounds.md) give \(R>n^{3\tau(n)/2}\) at every odd \(n>1\) with no unknown constant. This furnishes a stronger numerical exponent than (1) when \(\tau(n)\ge8\).

For all four arms the same finite-exception argument gives \(R\gg n^{2\tau(n)}\), since primitive witnesses in different arms are disjoint at \(n\). This has a larger power of \(n\) than (1) when \(\tau(n)\ge6\).

The finite thresholds can also be made effective on this fixed curve. Take a real elliptic logarithm \(z\) of \(2G\) and a real period \(\omega\). David's lower bound for nonzero complex linear forms in elliptic logarithms of algebraic points gives
\[
  -\log |mz+k\omega|\ll_{\rm eff}(\log(2m))^B
\]
for the integer \(k\) minimizing the absolute value, with a fixed effective \(B\), since \(|k|=O(m)\) and \(\omega/2\) is the logarithm of an algebraic two-torsion point. Nonvanishing follows from nontorsion. The double pole of the Weierstrass function at the period lattice gives \(\log^+|x(2mG)|\ll_{\rm eff}(\log(2m))^B\). Near infinity the duplication function satisfies \(x(2S)\sim x(S)/4\), so \(\log^+|x(S)|\le\log^+|x(2S)|+O(1)\). Apply this to \(S=m(G+T)\) for every rational two-torsion point \(T\). The uniform global comparison with \(2\widehat h\) gives \(\log B(m(G+T))=Hm^2+O_{\rm eff}((\log(2m))^B)\). In the no-primitive-divisor inequality one only needs this effective lower estimate at \(m\); the upper bounds \(\log F_j\le H j^2+1.85\) at odd proper divisors were already explicit. Hence the last possible exceptional index is effectively bounded. S. David, *Minorations de formes linéaires de logarithmes elliptiques*, Mémoires de la Société Mathématique de France, Sér. 2, no. 62 (1995).
