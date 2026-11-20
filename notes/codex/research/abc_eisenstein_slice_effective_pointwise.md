# Effective large-prime mass at every elliptic index

Let \(F\) be either of the two marked quartic forms \(F_+,F_-\) on the [fixed elliptic square slice](abc_eisenstein_twelfth_elliptic_slice.md). For an odd \(n\ge3\), write \(F_n=|F(x_n,y_n)|\). For a finite rational prime set \(S\), let \(M_S\) denote the largest divisor of \(F_n\) prime to all of \(S\). There are effectively computable constants \(c,C>0\), depending only on the fixed slice, for which the following hold at **every** such index.
\[
\begin{aligned}
 \log(2M_{\{p\le Y\}})&\ge c n^2e^{-CY} &&(Y\ge2),\\
 \log(2M_{\{p\}})&\ge \frac{c n^2}{p(\log(2p))^5} &&(p>3,\ p\mid F_n),\\
 \operatorname{rad}(F_n)&\ge c n^{1/C}. &&
\end{aligned}                                                     \tag{1}
\]
Thus any \(Y=o(\log n)\), even unbounded, leaves logarithmic factor mass at least \(n^{2-o(1)}\) above \(Y\) in each quartic separately. This is a lower bound for weighted prime powers. When \(Y\) tends to infinity it gives no fixed positive fraction of the full logarithm. The last inequality is a lower bound directly for the radical.

## Reduction to a classical S-unit equation

The splitting field \(K=\mathbb Q(\sqrt2,\sqrt3)\) is fixed. The roots of \(F_0(X,1)=X^4-18X^2+9\) are \(\pm(\sqrt6\pm\sqrt3)\). The forms \(F_\pm\) are carried to \(F_0\) up to scalar by fixed invertible rational linear substitutions, so their Galois group is again the regular Klein four group on the roots. For either monic quartic, let \(\alpha_i\) be its four roots and \(\gamma_i=x_n-\alpha_i y_n\) its integral linear factors. The quartic discriminants have no prime divisor above 3. Every \(p>3\) dividing \(F_n\) gives a projective affine root modulo \(p\), since \(x_n,y_n\) are coprime and the quartic is monic. Its Frobenius fixes a root and hence is trivial, so all these primes split completely in \(K\).

Use all places over \(S\), the archimedean places, and a fixed set of places containing the supports of integral representatives of all ideal classes of \(K\). Write \(\mathcal S\) for this set and \(s_K=|\mathcal S|\). For each \(\gamma_i\) write \(\mathfrak a_i\) for the portion of its integral ideal away from \(\mathcal S\). Its absolute norm is at most \(M_S^4\): it divides the outside-\(\mathcal S\) portion of the rational ideal \((F_n)\). Choose the fixed ideal class representative \(\mathfrak c_i\) making \(\mathfrak c_i\mathfrak a_i\) principal. Its generator \(\eta_i\) can be chosen with \(h(\eta_i)\ll_K\log(2M_S)\). Indeed multiply any generator by a unit to place the centered vector of its archimedean logarithms in a fixed bounded fundamental domain of the Dirichlet unit lattice. The remaining mean is determined by the ideal norm. Thus \(v_i=\gamma_i/\eta_i\) is an \(\mathcal S\)-unit.

Three distinct roots satisfy
\[
 \frac{\alpha_2-\alpha_3}{\alpha_2-\alpha_1}\frac{\gamma_1}{\gamma_3}
 +\frac{\alpha_3-\alpha_1}{\alpha_2-\alpha_1}\frac{\gamma_2}{\gamma_3}=1 .
\]
Substitution gives \(a(v_1/v_3)+b(v_2/v_3)=1\), with nonzero coefficients satisfying \(\max(1,h(a),h(b))\ll_K\log(2M_S)\). Use Győry–Yu's classical effective unit-equation bound. Its fixed-field specialization bounds the heights of both unknown units by
\[
 (C_Ks_K)^{C_Ks_K}\,P_{\mathcal S} R_{\mathcal S}
 \left(1+\frac{\log^* R_{\mathcal S}}{\log^*P_{\mathcal S}}\right)
                 \max(1,h(a),h(b)).
\]
Here \(\log^* u=\max(1,\log u)\), \(P_{\mathcal S}\) is the maximal norm of a finite prime in \(\mathcal S\) or a fixed lower cutoff, and \(R_{\mathcal S}\) is its regulator. The constants depend only on the fixed field. This is a coarse specialization of Theorem 1 of K. Győry and K. Yu, *Bounds for the solutions of S-unit equations and decomposable form equations*, Acta Arith. 123 (2006), 9–41. The multiplicative method here is also used in the literature on [S-parts of binary form values](https://arxiv.org/abs/1708.08290).

The ratio \(\gamma_1/\gamma_3=(x_n-\alpha_1 y_n)/(x_n-\alpha_3 y_n)\) is a fixed Möbius function of \(x_n/y_n\), so its height differs by \(O_K(1)\) from \(h(x_n:y_n)=\widehat h(P)n^2+O(1)\). The regulator satisfies \(R_{\mathcal S}\ll_K\prod_{\mathfrak q\in\mathcal S_{\rm fin}}\log N\mathfrak q\). This follows from the usual exact sequence for the valuations of the \(\mathcal S\)-units, whose image has index dividing the fixed class number in the free lattice on these primes.

For all rational primes up to \(Y\), we may omit those not dividing \(F_n\) from \(S\), and obtain \(s_K\ll 1+Y/\log(2Y)\), \(P_{\mathcal S}\ll_K Y\) and \(\log^*R_{\mathcal S}\ll_K1+(Y/\log(2Y))\log\log(3Y)\). All the multipliers cost at most \(e^{CY}\). For one prime \(p>3\) dividing \(F_n\), there are four degree-one places, so \(s_K\) is bounded, \(P_{\mathcal S}\ll_K p\), \(R_{\mathcal S}\ll_K(\log(2p))^4\). This gives the weaker round factor \(p(\log(2p))^5\) in (1). Finally take all primes dividing \(F_n\). If \(R=\operatorname{rad} F_n\), then \(M_S=1\), \(s_K\log(2s_K)\ll\log(2R)\) by the bound \(\prod_{j\le t}p_j\ge t!\), and \(P_{\mathcal S}\) and \(R_{\mathcal S}\) are both bounded by a fixed power of \(2R\). This proves (1). If the quartic value has at most a fixed number b of distinct prime factors, the same argument is sharper. Then the cardinality of the place set is bounded in terms of b, all large primes split completely, and the regulator is at most a b-dependent constant times the 4b-th power of the logarithm of the largest prime. It follows that the largest prime is at least a b-dependent positive constant times \(n^2/(\log(2n))^{4b+1}\).

## Uniform count over all heights for a single deep prime

Write \(J_n=|F_+F_-|\), up to its fixed power of two. For every \(\delta>0\) there is an effectively bounded \(C_\delta\), independent of the good rational prime \(p\), such that
\[
 \#\{n\ge3\text{ odd}: v_p(J_n)\log p\ge\delta n^2\}\le C_\delta. \tag{2}
\]
This counts the entire infinite orbit separately at each prime. Its proof uses the quantitative two-dimensional Subspace Theorem, rather than an effective last exceptional height. See Evertse–Schlickewei, *A quantitative version of the absolute Subspace Theorem*, J. Reine Angew. Math. 548 (2002), 21–127.

Use the curve \(E':v^2=u^3-576u\), its rational point \(Q=(-8,-64)\), and the four [independent marked sections](abc_eisenstein_slice_marked_divisors.md). A prime-power hit gives local logarithmic proximity to one mark \(S_i\) of at least \(\delta n^2\). Fix a sufficiently large integer \(m\) depending only on \(\delta,Q\) and write \(n=ma+j\), \(0\le j<m\). At all but finitely many explicitly determined places, the map \([m]\) is étale on the good model and the four marked sections and the distinct preimages of \(S_i-jQ\) remain disjoint. A hit to depth \(t\) therefore puts \(aQ\) to the same depth at one of the algebraic points \(T\) with \([m]T=S_i-jQ\), in a fixed normal field containing them. At the finitely many exceptional places the required local proximity inequality has an effectively bounded additive correction, since the multiplication map is étale in characteristic zero and the finitely many distinct preimages have finite mutual distances. This follows also by a finite covering with formal parameter charts and the fixed differential \(m\).

The abscissa map is a fixed morphism to the projective line. Near each \(T\), logarithmic projective proximity of \(u(aQ)\) to \(u(T)\) is at least the group proximity, up to a bounded correction. For large \(p\) the correction is zero by good reduction. The global height of \(u(aQ)\) is \(2\widehat h(Q)a^2+O(1)\). Choosing \(m\) large makes the projective proximity exceed \(3h(u(aQ))\) for all sufficiently large \(n\), with uniform and effective small-index cutoff. There are only finitely many algebraic targets and their degrees and heights are fixed in terms of \(m\).

Quantitative nonarchimedean Roth, equivalently the quantitative Subspace Theorem for two linear forms in dimension two, bounds the number of rational approximants giving exponent 3 in terms of these fixed data, independently of the prime. In applying the number-field form, use all places in the splitting field over \(p\), assigning the transported conjugate target to each; rationality of \(u(aQ)\) then preserves the full normalized proximity after summing, with no degree loss. The number of places and the heights of all forms are bounded independently of \(p\). One-dimensional exceptional subspaces give just one rational direction each. Small-height rational approximants give a uniformly finite effective count as well. For fixed \(j\), a rational abscissa determines at most two possible \(a\), since \(Q\) is nontorsion. Summing gives (2). In particular there are at most \(C_\delta\pi(Y)\) indices, over all heights, with any prime \(p\le Y\) contributing \(\delta n^2\) on its own.

The numerical exponent in the proposed finite-place elliptic-logarithm refinement is not needed for (1) or (2). Direct access to the Bosser–Surroca paper was unavailable during this check, including an approved direct arXiv request. Its [bibliographic record](https://arxiv.org/abs/1208.2693) establishes its title and authors.
