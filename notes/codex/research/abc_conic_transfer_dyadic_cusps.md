# Dyadic restrictions on a rational transfer to the conic divisor

Let \(D=\{0,\infty,\pm\sqrt2,\pm\sqrt{-2}\}\). For a nonconstant rational function \(f\in\mathbb Q(x)\) with all branch values in \(D\), let \(r\) count all geometric zeros and poles. If at least three of them are rational, then
\[
                               r\ge6 .
\]
This holds in every degree. Every finite nonzero member of \(D\) has dyadic valuation \(1/2\), and the identity below accounts for the obstruction.

More generally suppose the zeros and poles split over a tamely ramified finite extension of \(\mathbb Q_2\) (in particular this applies when they are all rational). Then \(r\equiv2\pmod4\). If \(r=6\), the four units of ramification away from \(0,\infty\) are four simple critical points in one Galois orbit, with two over each value of a single quadratic target pair. Their common degree is four, and their local field at 2 is totally ramified.

## A local multiplicity bound

Let \(L/\mathbb Q_2\) be a finite extension of odd ramification index \(e\) containing all finite zeros and poles of \(f\). Let \(\beta\) be a finite point away from them with \(v_2(f(\beta))\in\tfrac12+\mathbb Z\), and let \(m\) be the ramification index of the rational function at \(\beta\), taking \(m=1\) at an ordinary point. The field ramification index satisfies
\[
 2^{\,1+\lceil\log_2 m\rceil}\ \mid\ e(L(\beta)/\mathbb Q_2).               \tag{1}
\]
In particular a simple critical point requires a multiple of four. For tame \(L\) the same divisibility holds for \(e(\mathbb Q_2(\beta)/\mathbb Q_2)\), since the extension \(L(\beta)/\mathbb Q_2(\beta)\) is tame. Indeed an extension of local fields with perfect residue field becomes an unramified extension followed by adjoining a prime-to-2 root of a uniformizer after a further unramified extension; this description also shows that base change of a tame extension remains tame.

Write \(f(x)=c\prod_i(x-r_i)^{a_i}\) with distinct finite \(r_i\in L\), nonzero signed integers \(a_i\) and \(c\in L^\times\). Take a closest \(b=r_i\) to \(\beta\), and set \(h=v_2(\beta-b)\). The other distances have value either \(h\) or an element of \(v_2(L^\times)=\frac1e\mathbb Z\), by the nonarchimedean triangle inequality and maximality of \(h\). If \(h\) belonged to this group, the valuation of the entire product would belong to it, which is impossible for the specified half-integer. The factors in the cluster \(I=\{i:v_2(b-r_i)>h\}\) have value \(h\); all other factors have values in \(\frac1e\mathbb Z\). Hence for \(E=\sum_{i\in I}a_i\)
\[
                        v_2(f(\beta))\equiv Eh\pmod{\tfrac1e\mathbb Z}.
\]
In particular \(E\ne0\). Expand in a formal variable \(U\):
\[
 \frac{f(\beta+(\beta-b)U)}{f(\beta)}
    =\prod_i\left(1+\frac{\beta-b}{\beta-r_i}U\right)^{a_i}.
\]
All coefficients are integral in \(L(\beta)\), including for negative exponents. The displayed slopes reduce to one for \(i\in I\) and zero otherwise. The reduction therefore equals \((1+U)^E\). The first nonconstant term of the characteristic-zero series has degree \(m\), so its reduction has no nonconstant term below degree \(m\). In characteristic two the first nonconstant term of \((1+U)^E\) has degree \(2^{v_2(E)}\), including when \(E<0\). Thus \(v_2(E)\ge\lceil\log_2 m\rceil\). The reduced denominator of \(eh\) must have 2-part exactly \(2^{1+v_2(E)}\), because \(eEh\equiv1/2\pmod{\mathbb Z}\). This proves (1).

## Counting the critical points

Riemann–Hurwitz counts total ramification outside \(0,\infty\) as \(r-2\). Without a splitting assumption this is even, by Galois conjugation of every allowed nonrational branch value. If all zeros and poles split tamely, apply (1) at every place over 2 of the field of definition of every residual critical point. Its degree over \(\mathbb Q\) is a sum of local residue degrees times local ramification indices, hence divisible by four. Each Galois orbit of these points contributes a multiple of four to \(r-2\). The assertions for \(r=6\) follow immediately. Finally, if just three rational zeros or poles are required, the only even \(r<6\) compatible with that is four. Any fourth point left over after three rational ones must also be rational by Galois invariance, so the tame result excludes this case. [Degree-three covers](abc_conic_cubic_transfer_maps.md) · [Degree-four covers](abc_conic_quartic_transfer_maps.md)
