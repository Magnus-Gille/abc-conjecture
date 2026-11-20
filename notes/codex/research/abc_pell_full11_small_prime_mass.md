# Pointwise bounds for prime powers in the full rank-eleven factor on the Pell orbit

Put \(\varepsilon=1+\sqrt2\), \(b_n+a_n\sqrt2=\varepsilon^n\), and \(F_n=|F_{11}(a_n,b_n)|\), for the definite degree-100 homogeneous full CM rank-eleven form. Then \(\log F_n=100n\log\varepsilon+O(1)\). The following conclusions hold at **every** sufficiently large \(n\), without averaging.

* Some constant \(c>0\) gives \(\sum_{p\le n^{1/3}\exp(c\log n/\log\log n)}v_p(F_n)\log p=o(n)\).
* Restricting to \(p\equiv1\bmod8\), one may use \(n^{1/2}\exp(c\log n/\log\log n)\) instead, after reducing \(c\). Apart from finitely many exceptions all remaining contributing primes are \(3\bmod8\).
* For \(p\nmid2\), let \(r_{p,j}\) be the projective order of \(\varepsilon\) modulo \(p^j\), meaning its order in \((\mathbb Z[\sqrt2]/p^j)^\times/(\mathbb Z/p^j)^\times\). Ignoring finitely many fixed primes, the combined weight of **all** pairs \((p,j)\) with \(p^j\mid F_n\) for some \(n\), and \(r_{p,j}\le R\), is \(O(R^{3/2})\), each pair weighted by \(\log p\). Thus \(r_{p,j}=o(n^{2/3})\) gives an additional pointwise negligible range at arbitrary prime sizes, in the sense that every prescribed cutoff \(R(n)=o(n^{2/3})\) contributes \(o(n)\).

These bounds include the first copy of each prime. They apply in particular to repeated-prime mass on the bare Pell orbit, for which \(J(a_n,b_n)=(-1)^n\). [Whole primitive triple](abc_cm_pell_whole_triple.md) · [Underlying form](abc_cm_twist_sharp_depth.md)

## A fixed multiplicative target

Use the two conjugates \(\alpha=\varepsilon\), \(\alpha'=1-\sqrt2\), put \(g=\alpha/\alpha'=-\varepsilon^2\), and set
\[
    P(Z)=F_{11}\big((Z-1)/(2\sqrt2),(Z+1)/2\big).
\]
Then \(F_{11}(a_n,b_n)=(\alpha'^n)^{100}P(g^n)\). The linear change of projective coordinates preserves separability. The leading and constant coefficients are nonzero since the two parameter directions with \(J=0\) are disjoint from the full factor. Outside finitely many primes \(P\) is integral with unit leading and constant coefficients, and has separable reduction. Write \(\beta\) for any one of its finitely many roots.

At a prime dividing \(F_n\), choose a place of \(\mathbb Q(\sqrt2)\) and remove the finite exceptional set. Hensel's lemma applied to \(g^n\bmod p\) lifts a unique simple root \(\beta\) into the completion at this place. Every other root differs from \(g^n\) by a unit. Hence
\[
               v_p(F_n)=v_p(g^n/\beta-1),\qquad v_p(p)=1.
\]
The chosen completion of \(K=\mathbb Q(\sqrt2,\beta,i)\) embeds into the unramified extension of \(\mathbb Q_p\) of degree at most two. If \(p\equiv1\bmod8\), the completion is \(\mathbb Q_p\) itself. A denominator prime of odd reduction order splits in \(\mathbb Q(\sqrt{-2})\), so the other residue class is \(3\bmod8\); there \(\sqrt2\) has local degree two. In both classes \(g^n/\beta\ne1\), by definiteness. At each omitted fixed prime the valuation of \(F_n\) is \(O_p(\log(2n))\): factor \(P\) over a fixed splitting field, use Yu's fixed-place estimate on the unit roots, and observe that the other roots have constant distance valuation from the unit \(g^n\). Leading coefficients contribute only a fixed constant. Enlarge the field by the required roots of unity at small residue characteristic if necessary.

## The explicit \(p\)-dependence

We use Theorem 1 of K. Yu, *p-adic logarithmic forms and group varieties III*, Forum Math. **19** (2007), 187–280, including its explicit height product and rank constant. For the chosen \(K\) and unramified place, let \(f\in\{1,2\}\) be the residue degree. Uniformly over sufficiently large \(p\),
\[
       v_p(g^n/\beta-1)
         \ll p^f\exp\!\left(-c_0\frac{\log p}{\log\log p}\right)
                     \log(2n)
       \tag{1}
\]
for some \(c_0>0\). Only finitely many \(K,\beta\) occur. The following rank calculation gives (1), using Yu directly rather than presuming that a Lucas-sequence bound holds for a second algebraic target. [Yu constants and height product in SageMath](https://github.com/sagemath/sage/blob/develop/src/sage/rings/number_field/S_unit_solver.py#L462-L607) · [Specialization at fixed rank](hall_pell_valuation_bounds.md)

The numbers \(g,\beta\) are multiplicatively independent, as checked below. Choose distinct rational primes \(l_1,\ldots,l_k\), disjoint from a fixed finite set supporting \(g,\beta\) and excluding \(p\). The first \(k\) such primes satisfy \(l_i\ll k\log(2k)\) in the range used here. The \(k+2\) elements
\[
     g_0=g/(l_1\cdots l_k),\quad \beta,\quad l_1,\ldots,l_k
\]
are multiplicatively independent. Indeed the primes above the \(l_i\) first force their exponents to equal the exponent of \(g_0\); independence of \(g,\beta\) finishes the argument. Express \(g^n/\beta\) using these elements with exponents \(n,-1,n,\ldots,n\). Include a torsion generator of \(K\) with exponent equal to its order, so the other elements form an independent subset of size one less than the total \(m=k+3\). All inputs are local units. The inclusion of \(i\) ensures hypothesis (1.15) for odd \(p\).

In Yu's \(C_1^*\Omega\log B\) upper bound take \(B\gg_K n+1\). For fixed global degree and unramified \(p\ge7\), formulas (1.21)–(1.23) give
\[
 C_1^*\ll (Cm)^m m^C\,p^f(\log p)^{-m-1}.
\]
Indeed \(m^m(m+1)^{m+1}/m!\le (Cm)^m m^C\), the local factor \(a^{(1)}\) is bounded, and the final maximum in the formula costs \(O_K(\log p+\log(m+1))=O_K(\log p)\). The product of the ordinary heights of the independent inputs and the one modified torsion height bounds \(\Omega\). Here \(h(g_0)\ll k\log(2k)\), \(h(\beta)\) is fixed, each \(h(l_i)\ll\log(2k)\), and the torsion height is \(O_K(\log p)\). Thus the resulting right side is bounded by
\[
 C p^f\log(2n)(m\log p)^C
              \left(\frac{C m\log(2m)}{\log p}\right)^m .
\]
Choose \(k=\lfloor c_1\log p/\log\log p\rfloor\) with \(c_1>0\) sufficiently small for the parenthesized base to be at most \(1/2\) at large \(p\). The factor polynomial in \(m,\log p\) is absorbed by decreasing the exponential constant, giving (1).

For primes of residue degree at most \(f\), splitting the range \(p\le Y\) at \(\sqrt Y\) yields
\[
 \sum_{p\le Y}v_p(F_n)\log p
   \ll \log(2n)\,Y^{f+1}
            \exp\!\left(-c_2\frac{\log Y}{\log\log Y}\right).
\]
One can bound \(\sum_{p\le Y}p^f\log p\ll Y^{f+1}\) by Chebyshev. Inserting \(Y=n^{1/(f+1)}\exp(c\log n/\log\log n)\) with \(c>0\) sufficiently small gives the first two assertions.

## Why the two bases are independent

In the coordinate \(Z=(b+a\sqrt2)/(b-a\sqrt2)\) the underlying elliptic abscissa is
\[
    x=-8\left(1+\frac{Z^2-1}{\sqrt2(Z^2+1)}\right).
\]
Thus \(\beta^2\) is a fixed invertible fractional linear transform over \(\mathbb Q(\sqrt2)\) of a root of the irreducible degree-50 rational division factor \(G_{11}(x)\). This factor stays irreducible over \(\mathbb Q(\sqrt2)\). Otherwise its two conjugate factors there have degree 25 each. The rational prime 17 splits in \(\mathbb Q(\sqrt2)\), but modulo 17 the factor degrees of \(G_{11}\) are \(10,10,10,10,10\). The leading coefficient is a unit there, so the monic factors would preserve their degrees on reduction, which cannot give degree 25. The signs of \(G_{11}(0),G_{11}(1),G_{11}(2),G_{11}(5)\) after normalization to positive leading coefficient are respectively \(-,+,-,+\). In particular there are three distinct positive real conjugate roots. The inverse Möbius transform is finite and injective there. [Division polynomial recurrence for \(G_{11}\)](abc_cm_twist_depth_example.py)

The modular degrees can be checked using only polynomial gcds: for \(j=1,2,5,10\) the degrees of \(\gcd(G_{11},x^{17^j}-x)\) over \(\mathbb F_{17}\) are \(0,0,0,50\), respectively. It follows that \(\beta^2\) has at least three distinct real conjugates over \(\mathbb Q(\sqrt2)\). A relation \(g^u\beta^v=1\) with \(v\ne0\) would make all those conjugates roots of \(X^{|v|}-g^{\pm2u}\), which has at most two real roots. A relation with \(v=0\) is impossible because \(g\) has infinite order. This also excludes relations up to roots of unity by taking a power.

## Projective orders at arbitrary prime sizes

At odd unramified primes and away from the fixed bad set, the projective order \(r_{p,j}\) equals the multiplicative order of \(g=\varepsilon/\varepsilon'\) modulo \(p^j\) in a completion of \(\mathbb Q(\sqrt2)\). Equality of an element and its conjugate modulo \(p^j\) is precisely scalarness when 2 and the discriminant are units; at split primes the two multiplicative orders agree by inversion. Whenever \(p^j\mid F_n\), the congruence \(\beta\equiv g^n\bmod p^j\) shows that the subgroup generated by the two reductions has size \(r_{p,j}\).

If \(r_{p,j}\le R\), the \((\lfloor\sqrt R\rfloor+1)^2>R\) elements \(g^u\beta^v\) with \(0\le u,v\le\lfloor\sqrt R\rfloor\) cannot all differ modulo \(p^j\). Thus some nonzero difference of exponent vectors with both coordinates at most \(\sqrt R\) in absolute value gives \(g^u\beta^v\equiv1\bmod p^j\). By independence \(g^u\beta^v-1\) is nonzero. Its height is \(O(\sqrt R)\); the absolute norm of its integral numerator ideal has logarithm \(O(\sqrt R)\) in the fixed field. This norm is divisible by \(p^j\). The product of these norms over the \(O(R)\) nonzero exponent vectors and the finitely many \(\beta\) has log size \(O(R^{3/2})\). It absorbs the largest qualifying power of each prime even if the indices are allowed to vary. All the counted copies at that prime weigh at most its largest qualifying exponent times \(\log p\). This proves the final assertion.

There is a complementary average result. For any \(Y=o(N\log N)\), the full mass at all primes through \(Y\) is \(o(n)\) outside a relative \(o(1)\) set in the block \(N\le n<2N\), in the sense of convergence in density. At each good prime set \(r=r_{p,1}\), \(w=v_p(g^r-1)\). Then \(w\log p\ll r\) by the global height of \(g^r-1\), and \(r_{p,j}=r p^{\max(0,j-w)}\) by binomial lifting. At most 100 residue classes modulo \(r_{p,j}\) hit the simple roots at depth \(j\). In the levels with \(r_{p,j}\le N\), the contributions through \(w\) cost \(O(Nw\log p/r)=O(N)\); higher levels cost \(O(N\log p/[r(p-1)])=O(N)\). At the first level with period \(>N\), at most 100 indices in the block remain. Each of these has total valuation times \(\log p\) at most \(\log F_n=O(N)\). Thus the entire block costs \(O(N)\) per good prime, independent of its size. The finitely many other primes contribute \(O(N\log N)\) together. Sum over \(p\le Y\), divide by \(N^2\), and use Markov's inequality and \(\pi(Y)=o(N)\).

The projective order at an inert hit divides \(p+1\) modulo \(p\). In the version of Yu's inequality used in (1), the prime-dependent numerator is \(p^f\); simply substituting the order for this numerator would not follow from that theorem. The separate proof for \(r_{p,j}\) retains this arithmetic information without this substitution.
