# Prime multiplicities at all odd indices of the two-square orbit

Let \(Y_N=s_N^2+2t_N^2\) on the full two-square orbit and let \(B_N=\sqrt{Y_N}\). For each odd \(N\ge3\), this is the positive square root of the reduced denominator of the abscissa of \([N]R\) on
\[
 E':y^2=x^3+16x^2+32x,\qquad R=(-8,16).
\]
The point has infinite order. Set \(B_1=1\). The curve has complex multiplication by \(\mathcal O=\mathbb Z[\sqrt{-2}]\) over \(K=\mathbb Q(\sqrt{-2})\). Indeed it is the \(-2\) twist of the full-orbit curve with its given degree-two endomorphism. Write \(e_p=v_p(B_N)\) and let \(t_K(N)\) be the number of integral ideals dividing \((N)\) in \(\mathcal O\). [Full orbit](abc_octic_full_mixed_orbit.md) · [Denominator identity](abc_octic_mixed_three_factors.md)

With constants depending only on the fixed curve and point, for all \(X\ge2\),
\[
\begin{split}
 \sum_{p\mid B_N,\; p e_p\le X} e_p\log p
    &\ll t_K(N)\sqrt X\log(2X)+\log(2N),\\
 \sum_{p\mid B_N,\; p\le X} e_p\log p
    &\ll t_K(N)X+\log(2N),\\
 \log\frac{B_N}{\operatorname{rad}(B_N)}
    &\le \log B_N-\tfrac12 t_K(N)\log N+O(t_K(N)).
\end{split}
\]
In particular \(t_K(N)\le\tau(N)^2=N^{o(1)}\). At every sufficiently large odd index, the primes with \(p e_p\le N^{4-\epsilon}\) or \(p\le N^{2-\epsilon}\) supply \(o(\log B_N)\) of total logarithmic mass, for any fixed \(\epsilon>0\). If \(B_N\) is squareful, the remaining primes must supply at least \((1/2-o(1))\log B_N\) of excess. These estimates allow the exponents of individual primes to vary.

## Denominator heights for complex multipliers

Every ideal of \(\mathcal O\) is principal. For a nonzero generator \(\alpha\) of odd norm \(M\), let \(D(\alpha)\) denote the sum of the formal depths of \([\alpha]R\) at odd finite places, weighted by the logarithms of their residue-field sizes. The depth on this integral model is \(\max(0,-v_{\mathfrak p}(x)/2)\). Write \(\widehat h\) for the absolute canonical height. Uniformly in \(\alpha\),
\[
 D(\alpha)=2\widehat h(R)M+O(\log(2M)).
\]

To check the infinite places, give the complex torus its flat distance. The point \(R\) is on the bounded real component of \(E'\), since its abscissa lies between the roots \(-8-4\sqrt2\) and \(-8+4\sqrt2\). Every odd multiple stays on that component, a fixed positive distance from the identity. Multiplication by \(\bar\alpha\) has Lipschitz constant \(\sqrt M\), and sends \([\alpha]R\) to \([M]R\). Thus \([\alpha]R\) is at least a constant times \(M^{-1/2}\) from the identity. The double pole of \(x\) gives \(\log^+|x([\alpha]R)|=O(\log(2M))\), also at the conjugate embedding.

At the dyadic place choose a sufficiently small neighborhood of the identity on which the formal logarithm identifies the group with an additive ideal. It can be chosen stable under every element of \(\mathcal O\). For the fixed endomorphism \(\sqrt{-2}\), shrink first into its logarithm domain and the inverse image of that domain. In logarithmic coordinates it multiplies by its integral differential. A sufficiently small ball is thus stable under it, under integers and consequently under their sums. Every rational point \([M]R\) of odd positive index has odd abscissa denominator by the full-orbit identity, including \(M=1\). Such a point avoids this neighborhood after it is made sufficiently small. Since \([\bar\alpha][\alpha]R=[M]R\), the dyadic depth of \([\alpha]R\) is uniformly bounded. Finally \(h(x([\alpha]R))=2\widehat h(R)M+O(1)\), since the degree of \([\alpha]\) is \(M\). In the absolute height over the quadratic field, each negative abscissa valuation contributes its formal depth times the log residue size. This proves the formula. For rational odd \(N\) it gives \(\log B_N=\widehat h(R)N^2+O(\log(2N))\).

## The contribution at an exact annihilator ideal

At an odd place \(\mathfrak p\) of good reduction, let \(\mathfrak a_{\mathfrak p}\) be the ideal of complex multipliers that kill the reduction of \(R\). If \([\alpha]R\) specializes to the identity then \(\mathfrak a_{\mathfrak p}\mid(\alpha)\). The underlying rational prime divides \(B_M\), since applying \([\bar\alpha]\) also gives the identity on reduction. Every such odd prime splits in \(K\). Indeed \(p\mid s_M^2+2t_M^2\) with \(s_M,t_M\) coprime, and hence \(-2\) is a square modulo \(p\). There are no primes when \(M=1\). The odd places that occur all have completion \(\mathbb Q_p\).

For an odd-norm ideal \(\mathfrak a=(\gamma)\) let \(F(\mathfrak a)\) be the sum over places with exact annihilator \(\mathfrak a\) of the formal depth of \([\gamma]R\) times \(\log p\). Changing the generator by a unit preserves this depth. For \(\alpha=\gamma\beta\), the depth of \([\alpha]R\) at such a place increases by \(v_{\mathfrak p}(d\beta)\), where \(d\beta\) denotes its differential. The formal logarithm is an isometry on the positive-depth group at these unramified odd primes. The differential embedding on \(\mathcal O\) is the identity or conjugation. Since \(d\beta\mid d\alpha\), the sum of all these increases weighted by \(\log p\) is at most \(\log M\), including both places over a split rational prime. Consequently
\[
 D(\alpha)=\sum_{\mathfrak a\mid(\alpha)}F(\mathfrak a)+O(\log(2M)).
\]
Ideal Möbius inversion shows, for \(M=\operatorname N\mathfrak a\),
\[
 F(\mathfrak a)=2\widehat h(R)M
     \prod_{\mathfrak q\mid\mathfrak a}\left(1-\frac1{\operatorname N\mathfrak q}\right)
     +O(\tau_K(\mathfrak a)\log(2M)),
\]
where \(\tau_K\) counts ideal divisors. In particular every sufficiently large odd-norm ideal occurs as an exact annihilator. For any \(\delta>0\) the product is \(\gg_\delta M^{-\delta}\) and \(\tau_K(\mathfrak a)\ll_\delta M^\delta\), by elementary ideal factorization and the rational divisor bound.

## Counting the possible rational primes

For a rational prime \(p\mid B_N\), choose one of its two places in \(K\). Its annihilator \(\mathfrak a\) divides \((N)\). At a split prime of good reduction the Frobenius endomorphism is given by \(\pi\in\mathcal O\) of norm \(p\). This follows from ordinary CM reduction: the endomorphisms of the maximal order are defined in the residue field and the ordinary endomorphism ring contains that maximal order. Equivalently Frobenius commutes with the CM action, so it lies in the quadratic centralizer and is an algebraic integer. The reduced rational point is fixed by Frobenius, whence \(\pi\in1+\mathfrak a\). In particular
\[
 \operatorname N\mathfrak a\le |\pi-1|^2\le(\sqrt p+1)^2.
\]
The lattice \(\mathfrak a\) is a rotated copy of \(\mathcal O\) scaled by \(\sqrt{\operatorname N\mathfrak a}\). For \(M=\operatorname N\mathfrak a\), its translate has \(O(1+Z/M)\) points of squared modulus at most \(Z\), by disk packing. Any relevant prime satisfies \(p\gg M\), and distinct rational primes give distinct values of \(\pi\). Summing on dyadic intervals gives
\[
 \sum_{p\le X,\;p\text{ assigned to }\mathfrak a}\frac1p
       \ll \frac{\log(2X)}M.
\]
Hence the eligible valuations with \(p e_p\le X\) in this class have total log mass at most \(O(X\log^2(2X)/M)\). Their mass after removing formal lifting increases is also at most \(F(\mathfrak a)\le D(\gamma)\ll M\). The smaller bound is \(O(\sqrt X\log(2X))\). Summing over the \(t_K(N)\) divisors and restoring at most \(2\log N\) of lifting proves the first inequality. For \(p\le X\) all relevant ideals have \(M\ll X\), giving the second inequality by the height bound alone.

For the radical lower bound, choose one place of exact annihilator \(\mathfrak a\) for each sufficiently large divisor ideal of \((N)\), using positivity of \(F(\mathfrak a)\). Its rational prime divides \(B_N\) and has \(\log p\ge\log\operatorname N\mathfrak a-O(1)\). A rational prime can be selected for at most two ideals, one per place. The product of the norms of all ideal divisors of \((N)\) is \(N^{t_K(N)}\), by pairing complementary divisors. Omitting the ideals below the fixed norm threshold changes the log sum by a bounded amount. This proves the third inequality. At a squarefree index made entirely of split primes, for example, \(t_K(N)=4^{\omega(N)}\). Its growth still allows a positive proportion of \(\log B_N\) in repetitions at larger primes.

## A divergent count of non-Wieferich primes at the abc threshold

Let \(E:v^2=u^3-8u^2+8u\), \(A=(1,1)\), and let \(W(X)\) count the odd good primes \(p\le X\) at which \([r_p]A\) has formal depth one, with \(r_p\) the order of \(A\) modulo \(p\). Write \(q_N=\log c_N/\log R_N\) for the quality of the octic abc triple at odd index \(N\). Then
\[
 \limsup_{N\to\infty,\;N\text{ odd}}q_N\le1
 \quad\Longrightarrow\quad
 \lim_{X\to\infty}\frac{W(X)}{\sqrt{\log X}}=+\infty .
\]
In particular the rational abc conjecture implies this divergence for the fixed pair \((E,A)\). [Octic quality and counting function](abc_octic_mixed_quality_dichotomy.md)

Use the notation \(D=s^2-2t^2\), \(U=(s+t)^2+t^2\), \(V=(s-t)^2+t^2\) and \(Y=s^2+2t^2\) at index \(N\). The integer \(T_N=2|stDU|\sqrt{YV}\) is divisible by \(B_N\) and has radical \(R_N\). Also \(T_N\ll H_N^8\asymp c_N\) and \(\log c_N\asymp N^2\). Under the quality hypothesis,
\[
 0\le \log(B_N/\operatorname{rad}(B_N))
 \le \log(T_N/R_N)\le \log c_N-\log R_N+O(1)=o(N^2).
\]
In the last equality the upper bound follows from the quality hypothesis and the lower bound from \(R_N\le T_N\ll c_N\).

Fix \(L\ge3\). For each odd rational prime \(\ell\le L\) split in \(K\), choose one of the two primes \(\lambda\mid\ell\). For every odd multiple \(N\) of \(\ell\), form the integral ideal
\[
 \mathfrak a=(N)/\lambda,\qquad \operatorname N\mathfrak a=N^2/\ell.
\]
Its intersection with \(\mathbb Z\) is \(N\mathbb Z\). Indeed the conjugate prime \(\bar\lambda\) still has exponent \(v_\ell(N)\) in \(\mathfrak a\), and the exponents above every other rational prime agree with those in \((N)\). Thus a rational prime arising at this exact annihilator has reduction order exactly \(N\) for the point \(R\).

Set \(g(N)=\prod_{\mathfrak q\mid(N)}(1-1/\operatorname N\mathfrak q)\), and fix a constant \(c_0>0\) as specified below. If \(g(N)\ge c_0\), the exact-annihilator formula gives \(F(\mathfrak a)\gg_{L,c_0}N^2\) for all sufficiently large \(N\). Here the product in that formula is at least \(g(N)\), and its error is \(N^{o(1)}\). Some place in this group must lie over a rational prime with \(v_p(B_N)=1\). Otherwise its entire mass is at most
\[
 2\sum_{p\mid B_N,\ e_p\ge2}e_p\log p
 \le 4\log(B_N/\operatorname{rad}(B_N))=o(N^2).
\]
The first factor of two allows both places over a rational prime, and the formal depth at first occurrence is at most that at \(N\).

These primes are distinct for different pairs \((N,\ell)\). Their reduction orders for \(R\) distinguish the indices \(N\). At a fixed \(N\), the annihilator ideals at the two places over a split prime are conjugate and have the same norm. This follows by conjugating the relation \([\alpha]R=O\) in the residue group, since \(R\) is rational and conjugation on complex multipliers sends \(\alpha\) to \(\bar\alpha\). Their norm \(N^2/\ell\) therefore distinguishes \(\ell\).

The same witnesses are counted by \(W\). The rational two-isogeny \(\phi:E\to E'\) has coordinates \((u-8+8/u,(1-8/u^2)v)\), so \(\phi(A)=(1,-7)=[2]R\). At \(p\ge7\) the curves have the same good reduction cardinality \(h_p\). It is even from rational two-torsion and smaller than \(2p\) by Hasse, so \(p\nmid h_p\). Since the order of \(R\) is \(N\), depth one of \([N]R\) gives depth one of \([2h_p]R\). The isogeny has unit differential at odd good primes, so \([h_p]A\), whose image is \([2h_p]R\), has depth one. As \(r_p\mid h_p\), this gives depth one of \([r_p]A\). The finitely many primes below seven have fixed reduction orders and cannot occur for large \(N\).

It remains to count the qualifying indices. At odd \(N\), \(-\log g(N)\le3\sum_{q\mid N}1/q\), with \(q\) running over rational primes. For \(N=\ell k\) this last sum is at most \(1/\ell+\sum_{q\mid k}1/q\). The latter sum has uniformly bounded mean over odd \(k\) in any sufficiently large dyadic interval \([Z,2Z]\), by summing over all \(k\le2Z\) and using \(\sum_q q^{-2}<\infty\). Hence Markov's inequality gives absolute constants \(c_0,c_1>0\) such that at least \(c_1 M/\ell\) odd multiples \(N\in[M,2M]\) have \(g(N)\ge c_0\), whenever \(M/\ell\) is sufficiently large.

Every prime counted this way satisfies \(p\le B_N\le\exp(CM^2)\) with a fixed \(C>0\). For each fixed \(L\) and all sufficiently large real \(M\), summing over split primes gives
\[
 W(\exp(CM^2))\ \ge\ c_1 M
       \sum_{\substack{3\le\ell\le L\\ \ell\ \mathrm{split\ in}\ K}}\frac1\ell .
\]
The reciprocal sum diverges as \(L\) grows, since these primes occupy the classes \(1,3\bmod8\). Taking \(M=\sqrt{\log X/C}\), then letting \(L\) grow, proves the limit. Its proof gives no rate of divergence under the stated limsup hypothesis.
