# A lower bound for the squarefree part at two near-axis representations

Fix \(K>0\). If two distinct primitive triangles with hypotenuse \(u\) have smaller leg at most \(K\sqrt u\), then for sufficiently large \(u\)
\[
 \operatorname{sf}(u)\gg_K\frac{\log u}{(1+\log\log u)^4}.
\]
For the particular Pell family \(u_n=x_n^2+1\) with \(k_n+x_n\sqrt2=(3+2\sqrt2)^n\), the stronger bound
\[
 \operatorname{sf}(u_n)\gg\frac{(\log u_n)^2}{(1+\log\log u_n)^8}
\]
holds. These estimates constrain a possible source of repeated divisibility at the sharp small-leg scale. The squarefree part \(\operatorname{sf}(x)\) records the primes of odd valuation; primes of even positive valuation also belong to \(\operatorname{rad}(x)\).

## Comparing two nearby square roots

Use the [classification of the two triangles](abc_two_small_legs_and_pell_radicals.md). Write \(D=\operatorname{sf}(u),\ u=DZ^2,\ X^2=u-a^2,\ Y^2=2u-b^2\) with \(a,b\) bounded in terms of \(K\), both nonzero. The integers \(b^2\) and \(2a^2\) differ. In the real number field \(F=\mathbb Q(\sqrt D,\sqrt2)\) put
\[
 V=\frac{\sqrt2\,(\sqrt u+X)}{\sqrt{2u}+Y}.
\]
The elements \(\sqrt u+X\) and \(\sqrt{2u}+Y\) are algebraic integers dividing the rational integers \(a^2\) and \(b^2\), respectively, by multiplying by the corresponding differences. Consequently \(V\) is a unit outside primes over \(2ab\), and has absolute logarithmic height \(h(V)=O_K(\log u)\). At the displayed real embedding,
\[
 0<|V-1|=\frac{|b^2-2a^2|}{(\sqrt2 X+Y)(\sqrt{2u}+Y)}
 \asymp_K u^{-1}.
\]
The degree is at most four and the field discriminant has absolute value \(O(D^2)\): over \(\mathbb Q(\sqrt2)\) the relative discriminant divides \(4D\) when the extension is quadratic, by the discriminant of \(T^2-D\).

## Uniformity of the logarithmic-form bound

Here is the precise standard estimate being used. In any number field \(F\subset\mathbb R\) of degree at most four, fix a finite set of rational primes \(\mathcal P\). For an \(S\)-unit \(V\), with \(S\) the infinite places and the places over \(\mathcal P\), and \(0<|V-1|<1/2\) at the chosen embedding, one has
\[
 -\log|V-1|\ll_{\mathcal P}
 (1+\sqrt{|\Delta_F|}\log^3(2|\Delta_F|))\log(2+h(V)).
\]
For detail, the \(S\)-unit rank is bounded in terms of \(\mathcal P\). Minkowski's successive-minima theorem on the logarithmic \(S\)-unit lattice gives independent \(g_i\) of bounded index \(I\) with \(\prod_i(1+h(g_i))\ll_{\mathcal P}1+R_S\), where \(R_S\) is the \(S\)-regulator. The lower bound for each nonzero minimum is uniform by Northcott's theorem in bounded degree. Cramer's rule then writes \(V^{2I}=\prod_i(g_i^2)^{b_i}\) with \(\max |b_i|\ll_{\mathcal P} 1+h(V)\); the square removes the possible torsion signs. For the determinant details see the [small-generator argument](abc_repeated_primes_and_squares.md); at complex places use doubled archimedean logarithms in the regulator coordinates. Matveev's real logarithmic-form estimate applied at the real embedding gives \(-\log|1-V^{2I}|\ll_{\mathcal P}(1+R_S)\log(2+h(V))\). Since \(I\) is bounded and \(V\) is real and close to 1, \(|1-V^{2I}|\ll_{\mathcal P}|1-V|\). Finally the valuation lattice of the finite \(S\)-places has index at most the class number \(h_F\), so \(R_S\ll_{\mathcal P}h_F R_F\). The classical fixed-degree class number–regulator upper bound is \(h_F R_F\ll\sqrt{|\Delta_F|}\log^3(2|\Delta_F|)\) in degrees at most four.

Applying the estimate gives \(\log u\ll_K D\log^3(2D)\log(2+\log u)\). If \(D>\log u\) the first assertion already holds; otherwise bound \(\log(2D)\) by \(\log(2+\log u)\).

## Pell numbers individually

Write \(P_m=s y^2,\ s=\operatorname{sf}(P_m)\), and set \(\lambda=1+\sqrt2,\ m=2l+e,\ e\in\{0,1\}\). Let \(\theta^2=2\sqrt2\,s\lambda^e\), choosing the positive root at the standard real embedding. In \(F=\mathbb Q(\sqrt2,\theta)\), the algebraic integer \(W=\theta\lambda^l y\) satisfies \(W^2=\lambda^{2m}-(-1)^m\). Therefore \(\lambda^m+W\) and \(\lambda^m-W\) are units, since their product is \((-1)^m\). Put \(V=(\lambda^m+W)/(2\lambda^m)\). It has \(h(V)=O(m)\), is a unit outside the primes over 2, and satisfies \(0<|1-V|\asymp\lambda^{-2m}\) at the specified real embedding. This field has degree at most four and \(|\Delta_F|\ll s^2\); the quadratic relative discriminant divides \(4\theta^2\), of absolute norm \(O(s^2)\) in \(\mathbb Q(\sqrt2)\).

The preceding estimate now gives \(m\ll s\log^3(2s)\log(2m)\), so
\[
 \operatorname{sf}(P_m)\gg m/\log^4(2m).
\]
In the explicit family \(u_n=P_{2n-1}P_{2n+1}\) the factors are coprime, and \(\log u_n\asymp n\). Multiplication of the two individual lower bounds gives the second assertion. Neither estimate gives the near-exponential lower bound for the Pell radicals needed by the abc test in this family.
