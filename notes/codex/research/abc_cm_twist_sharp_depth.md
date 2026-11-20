# A sharp repeated-prime proportion on rational quadratic twists

On the rational-parameter version of the [twist family](abc_cm_twist_repeat_density.md), a single prime can contribute a fixed fraction of the logarithm of a full CM denominator factor. For \(q=11,\ p=683\), the exact upper limit is **\(1/50\)**. More generally, at fixed split prime rank \(q>3\), the upper limit is \(2/(q-1)^2\) for any fixed finite set of primes containing a prime of norm form \(p=(1+qc)^2+2q^2d^2\), \(d\ne0\). These are unconditional statements across varying rational twists. The constants for the fixed-curve abc triples depend on fixing the original curve and its point.

Take \(k=a/b\) in lowest terms, \(H_0=\max(|a|,|b|)\), and put
\[
 S=b^2+2a^2,\quad H=b^2+2ab+2a^2,\quad J=b^2-2a^2,\quad D=SH.
\]
Use \(E_k:Y^2=X^3+16DX^2+32D^2X\) and \(R_k=(-8H^2,16H^2J)\). These formulas hold also at \(b=0\). Good reduction at 7 and the order-eight reduction argument in the density note hold at primitive rational parameters as well, since \(S,H\) have no projective zeros modulo 7. All \(R_k\) have infinite order. Let \(C_{k,q}\) collect the actual prime powers in the square root of the reduced denominator of \(X([q]R_k)\) at primes \(p\nmid2D\) where \(R_k\) has full CM annihilator \((q)\).

## Its logarithmic size

Take the primitive rational full-abscissa factor \(G_q(x)\) of the odd division polynomial \(\psi_q(x)\) on \(E:y^2=x^3+16x^2+32x\). Its roots are precisely the \((q-1)^2/2\) distinct abscissas of points whose two components in \(E[q]\simeq(\mathbb Z/q)^2\) are nonzero in the two CM eigenlines. This set is Galois stable, including under interchange of the eigenlines. Homogenize \(G_q\) in two variables and take the primitive integral form \(F_q(a,b)\) proportional to \(G_q(-8H,S)\) in this homogeneous notation. Its degree is \((q-1)^2\). The two quadratics \(H,S\) have no simultaneous projective zero in characteristic zero. The poles of \(-8H/S\) are not roots of \(F_q\). The degree-two map to the abscissa is ramified at \(h(t)=0\), where \(h(t)=t^2+16t+32\); these are two-torsion abscissas, so \(F_q\) is separable.

There is no real projective root. For real \(a,b\), \(S,H>0\) and \(t=-8H/S<0\) satisfies \(t^2+16t+32=-2(4J/S)^2\). Thus \(t\) lies on the bounded real component of \(E\), including its two-torsion endpoints. No point of odd order lies on that component. Compactness on the real unit circle and homogeneity give \(\log|F_q(a,b)|=(q-1)^2\log H_0+O_q(1)\).

At \(p\nmid2q\), the roots of the division polynomial are distinct on reduction, and the geometric \(q\)-torsion reduces isomorphically with its CM action. Up to the fixed normalization constants, the valuation at each root of \(F_q\) is exactly the denominator depth at that prime, by the local division-polynomial formula. More explicitly \(G_q\) and its complementary factor have unit leading coefficients and disjoint reductions there: the original leading coefficient is \(q\) and the reductions of \(\psi_q\) are separable of full degree. Also \((-8H:S)\) is primitive locally there. Primes dividing \(S,H\), or \(J\) in odd characteristic cannot hit these abscissas: these give the point at infinity or two-torsion. The substitution introduces no new content at such primes, since it is a nonconstant degree-two map modulo every odd \(p\). Thus \(v_p(C_{k,q})=v_p(F_q(a,b))\) at all \(p\nmid2q\).

The valuations at \(2,q\) of \(F_q(a,b)\) are uniformly bounded on primitive pairs. It suffices by compactness to exclude local projective zeros. Work over \(L=\mathbb Q_q\) at the split prime \(q\), or over \(L=\mathbb Q_2(\sqrt{-2})\) at 2. All the CM endomorphisms are defined over \(L\). A rational abscissa of a full point \(P\) would imply \(\sigma P=\pm P\) for every \(\sigma\) in the absolute Galois group of \(L\). Since \(P\) generates \(E[q]\) over \(\mathcal O/(q)\), every \(\sigma\) would act by a scalar sign on all of \(E[q]\). Its determinant would be one, so the Weil pairing would force \(\mu_q\subset L\). This fails both for \(\mathbb Q_q\) and for the dyadic field of residue size two. The poles of \(t\) give a nonzero value of the homogeneous form. The full packet contains neither \(2\) nor \(q\), by its definition and the Hasse bound at \(q\). In particular,
\[
                  \log C_{k,q}=(q-1)^2\log H_0+O_q(1).
\]

## Approximation to a torsion abscissa

For a fixed finite set \(L\) of primes,
\[
 \limsup_{H_0\longrightarrow\infty}
 \frac{\sum_{p\in L}v_p(C_{k,q})\log p}{\log C_{k,q}}
 \le \frac{2}{(q-1)^2}.
\]
Around a root \(\xi\) in the projective \(p\)-adic parameter line, the valuation of \(F_q(a,b)\) differs by a bounded amount from the valuation of the linear form for distance to \(\xi\), using either integral affine chart and a unit denominator. Away from such neighborhoods it is bounded by compactness. Every local root is algebraic and irrational over \(\mathbb Q\), since there is no real root. The Subspace Theorem gives at most \((2+o(1))\log H_0\) for the sum of local logarithmic distances at finitely many places. Explicitly choose the local approximation form and a complementary coordinate, normalized at a primitive pair, and use \(a,b\) as forms at infinity. If the local sum exceeds \((2+\epsilon)\log H_0\), the product in the Subspace Theorem is \(O(H_0^{-\epsilon})\). There are finitely many choices of roots and charts. The resulting finite union of rational lines contains only finitely many primitive pairs up to sign. The nonarchimedean theorem used here is H. P. Schlickewei, “The \(\mathfrak p\)-adic Thue–Siegel–Roth–Schmidt theorem,” *Archiv der Mathematik* 29 (1977), 267–270.

For the matching lower bound it suffices that one \(p\in L\) has a full-abscissa root modulo \(p\), as in the Frobenius norm condition. Such a prime is \(>q\), and a simple parameter root lifts to an algebraic \(\xi\in\mathbb Z_p\) in a suitable chart. For each \(m\), the lattice \(a-\xi b\equiv0\bmod p^m\) has determinant \(p^m\), so it has a nonzero vector of height \(O(p^{m/2})\). Divide by its coordinate gcd \(g\). The resulting primitive vector of height \(H_0\ll p^{m/2}/g\) retains depth at least \(m-v_p(g)\). This tends to infinity and satisfies \((m-v_p(g))\log p\ge2\log H_0-O(1)\). The reduced denominator in this chart is a \(p\)-unit. Heights tend to infinity since \(\xi\) is irrational. Therefore the upper limit is attained as a limit along a subsequence, and even one compatible prime suffices. Replacing \(v_p\) by \(\max(v_p-1,0)\) in the numerator leaves the limits unchanged.

For **integer parameters** \(b=1\), the exact upper limit at the same finite set is instead \(1/(q-1)^2\). In the upper bound the product of the two archimedean forms is now \(|a|\), so the Subspace Theorem applies above \((1+\epsilon)\log H_0\). For the lower bound take the least nonnegative integer representative of a parameter root modulo \(p^m\). A finite parameter root always exists: there are at least \((q-1)^2-1\) choices modulo \(p\). This yields height at most \(p^m\) and local depth at least \(m\). As the root is irrational, the heights tend to infinity. One can choose infinitely many distinct twist squareclasses on this integer sequence. For each fixed squarefree \(\delta\), the equation \((2a^2+1)(2a^2+2a+1)=\delta z^2\) defines a smooth genus-one affine curve with finitely many integral points by Siegel's theorem (the two quadratics have distinct disjoint zeros). This excludes each fixed squareclass outside finitely many parameters.

For \(q=11\) the first compatible prime is \(683=21^2+2\cdot11^2\). The sharp fractions are thus \(1/100\) at integer parameters and \(1/50\) at rational parameters. The full factor \(G_{11}\) is the degree-50 factor of \(\psi_{11}\), whose other rational factor has degree ten. For an integer example take \(k=3872\). Here \(S=29984769,\ H=29992513\), and \(v_{683}(B_{k,11})=2\). Evaluation of \(G_{11}(-8H/S)\) modulo \(683^3\), followed by division by \(683^2\), gives \(382\bmod683\). The [point arithmetic and polynomial verifier](abc_cm_twist_depth_example.py) also verifies this valuation using the actual reduced abscissa.

## Infinitely many moving primes of exact exponent two

One can also let the prime itself tend to infinity. Fix \(q\), put \(d=(q-1)^2\), and fix any exponent \(e\ge2\). There are infinitely many distinct primes \(p\to\infty\) and integer parameters \(k_p\) on distinct quadratic twists for which
\[
  v_p(C_{k_p,q})=e,\qquad
  \frac{e\log p}{\log C_{k_p,q}}\longrightarrow\frac1d,\qquad
  \frac{(e-1)\log p}{\log C_{k_p,q}}\longrightarrow\frac{e-1}{ed}.
\]
Indeed \(F_q(k,1)\) is a nonconstant integer polynomial and has infinitely many prime divisors of its integer values by Schur's theorem. For a direct proof, if all possible primes had product \(M\), choose an integer \(z\) with \(c=F_q(z,1)\ne0\). Then \(F_q(z+cMn,1)/c\) is an integer congruent to 1 modulo \(M\) whose absolute value grows unboundedly, an impossibility. Remove the finite set of bad primes and those dividing the discriminant. Each remaining \(p\) has a simple parameter root modulo \(p\). Lift it to a representative \(0\le r<p^e\) modulo \(p^e\). Of \(r+p^e,r+2p^e\) at most one still gives zero modulo \(p^{e+1}\), by simplicity. Choose the other as \(k_p\). Then \(p^e\le k_p<3p^e\) and the valuation in the actual full factor is exactly \(e\). Its logarithm is \(d\log k_p+O_q(1)=de\log p+O_q(1)\), giving the limits. Siegel's argument above permits passage to different twist squareclasses. At \(q=11,e=2\), these fractions are \(1/100\) for the squared prime and \(1/200\) for the loss on taking the radical.

## What transfers to rational abc triples

There is an obstruction to using this fixed prime on its own. Consider any fixed nonconstant rational-function construction of triples on the parameter line. Write it as \(A+B=C\) for pairwise coprime homogeneous polynomials of degree \(d\), after removing common polynomial factors and clearing constants. Let \(F\) be the primitive product of the distinct irreducible factors of \(ABC\), without exponents. Its degree \(N\) is the number of distinct geometric points above \(0,1,\infty\) for the map \(A/C\). Riemann–Hurwitz gives \(N\ge d+2\): ramification in the three fibers totals \(3d-N\), at most \(2d-2\). For fixed finite \(L\) set
\[
 F_{\rm out}=|F(a,b)|\prod_{p\in L} p^{-v_p(F(a,b))}.
\]
Then, on primitive rational parameters of height \(H_0\) with nonzero values,
\[
             \log F_{\rm out}\ge(N-2-o(1))\log H_0.
\]
Indeed the archimedean shortfall \(N\log H_0-\log|F(a,b)|\) is at most the negative log distance to the nearest real root on the projective line plus \(O(1)\), or \(O(1)\) if there is no real root. Separability gives the analogous closest-root formula at the finitely many finite places. The sum of all those proximities, now including the archimedean one, is at most \((2+o(1))\log H_0\) by the same two-variable Subspace Theorem. This argument also allows rational roots.

The primitive integer triple at the parameter, after division by the numerical gcd and appropriate signs and permutation, has largest entry \(c\asymp H_0^d\), by the height formula for a fixed map of projective lines. The triple radical differs from \(\operatorname{rad}|F(a,b)|\) by at most a fixed multiplicative factor in either direction, since the common numerical gcd divides a fixed resultant up to fixed coefficient factors. Therefore, if the quality is at least \(1+\epsilon\), then
\[
 \log\frac{F_{\rm out}}{\operatorname{rad} F_{\rm out}}
 \ge \left(\frac{N-2}{d}-\frac{1}{1+\epsilon}-o(1)\right)\log c
 \ge \left(\frac{\epsilon}{1+\epsilon}-o(1)\right)\log c .
\]
This necessary condition concerns repeated factors in the squarefree polynomial evaluated at integers, after removing every prescribed finite set of primes. It explains why lifting a single prime to arbitrary depth on the varying twists does not by itself provide a counterexample.

There is an explicit comparison for the moving-prime sequence above as well. At integer \(k=k_p\to+\infty\), the dehomogenized squarefree product for the rational map has degree at least \(N-1\ge d+1\), where \(d\) now denotes the degree of that map. At all sufficiently large selected \(p\), its valuation at \(k_p\) is either zero or exactly \(e\). Indeed distinct irreducible factors of the two fixed squarefree polynomials in \(k\) have nonzero resultants, and \(p\) hits exactly one simple factor of the twist polynomial. Thus the marked \(p\) contributes at most \((1-1/e)\log k_p+O(1)\) of radical loss. Quality \(1+\epsilon\) for this map requires at least \((1+d\epsilon/(1+\epsilon))\log k_p+O(1)\) of total radical loss from that dehomogenized product. Other primes would have to provide the difference.
