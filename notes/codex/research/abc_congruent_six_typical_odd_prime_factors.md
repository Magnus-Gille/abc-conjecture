# Odd-exponent prime factors at a typical index

Let \(B_n\) be the positive square root of the reduced denominator of \(x([n](-3,9))\) on \(y^2=x^3-36x\). Fix \(\epsilon>0\) and any nondecreasing function \(L(t)\to\infty\). For **density one of the odd positive integers** \(n\), the denominator \(B_n\) has at least
\[
                     (\log n)^{\log 2-\epsilon}
\]
distinct prime divisors \(p>n^{1/L(n)}\) of **odd exponent**. Density one here means that the proportion of exceptions among odd indices through \(X\) tends to zero as \(X\to\infty\). The theorem concerns one denominator at a time; the primes counted at different indices can overlap.

In particular, for every \(\epsilon>0\) the squarefree kernel satisfies
\[
       \log\operatorname{sf}(B_n) \ \ge\
                     (\log n)^{1+\log 2-\epsilon}
\]
for density one of the odd indices. The exponent follows by choosing \(L(t)=\log\log(3t)\) and allowing a smaller loss in the first estimate. Thus the squarefree kernel on a typical index grows faster than every fixed power of the index. The full denominator has logarithm of order \(n^2\), so this still allows a large square part.

## A set of Gaussian prime divisors

Ignore the rational primes \(2,3,13\), and let \(m\) be the product of the other distinct rational primes dividing \(n\). The Gaussian ideal \((m)\) is squarefree. For its prime ideals take generators \(a+bi\) with \(a\) odd and \(b\) even. Define \(u,v\in\mathbf F_3\) by the base-2 discrete logarithms modulo 13 of \(a+5b,a-5b\), reduced modulo 3. These labels are unchanged by negation, add under multiplication, and interchange under conjugation. Let \(K(n)\) count the prime ideals of \((m)\) with \(u\ne0\).

For density one of the odd integers one has \(K(n)=(1+o(1))\log\log n\). In detail, a split rational prime contributes between zero and two according to its two Gaussian primes. Over the split primes the mean is \(4/3\) since the two labels are uniform in \(\mathbf F_3^2\), by the fixed Gaussian ray-class prime number theorem. An inert prime contributes one if its rational residue modulo 13 is a noncube, and zero otherwise, giving mean \(2/3\) over inert primes by Dirichlet's theorem in progressions. The two types have density \(1/2\) each. The resulting bounded strongly additive function has mean \((1+o(1))\log\log X\) and variance \(O(\log\log X)\) around its prime-sum mean by the Turán–Kubilius inequality. Restriction to odd integers preserves exceptional density zero. The same argument gives \(\omega(n)=O(\log\log n)\) on density one.

Two additional prime ideals can be prescribed on this density-one set.

* A split prime divisor of \(m\) has a place \(\lambda_*\) with \(u\ne0,v=0\). Indeed the split primes admitting such a place have positive fixed density in the same ray-class calculation, so their divisor count on a typical integer tends to infinity. The conjugate \(\bar\lambda_*\) has \(u=0\).
* There is a large inert prime divisor \(\ell_*\) with \(u=v\ne0\). To quantify this, in a block \(X<n\le2X\) take \(L_0=\min(L(X)/2,\sqrt{\log X})\). Consider the inert primes of noncube residue in \(X^{1/L_0}<\ell\le X^{1/4}\). Their reciprocal sum tends to infinity. Indeed these primes form a fixed union of rational residue classes of density \(1/3\), and Mertens in progressions gives \((1/3)\log(L_0/4)+O(1)\). Their count as divisors has variance at most its mean plus \(o(1)\) by summing the one- and two-prime divisibility indicators, using \(\ell\le X^{1/4}\) to bound rounding errors. Thus all but \(o(X)\) integers in the block contain one. The lower bound on \(\ell_*\) ensures \((\ell_*-1)^2>n^{1/L(n)}\) for large \(X\).

The two prescribed places are distinct by their splitting types.

## A quadratic nonresidue detects odd exponents

Use all squarefree Gaussian ideals \(I\mid(m)\) formed from the \(K(n)\) places with \(u\ne0\), requiring \(\lambda_*,(\ell_*)\mid I\). No two ideals selected are conjugate, since each contains \(\lambda_*\) and omits \(\bar\lambda_*\). Let \(X_I,Y_I\in\mathbf F_3\) be their label sums, and let \(h(x)=\mathbf1_{\{x=1\}}\) as an \(\mathbf F_2\)-valued function on \(\mathbf F_3\). The verified [quadratic character modulo 193](abc_congruent_six_cubic_packet_character.md) gives the sign bit of \(D_I\) as \(h(X_I)+h(Y_I)\). Here \(D_I\) is the norm of the denominator ideal for the Gaussian multiple. For \(U_I=\prod_{J\mid I}D_J^{\mu(I/J)}\) the sign bit is the mixed finite difference of this function, one difference per prime ideal dividing \(I\).

The second term disappears because \(v_{\lambda_*}=0\). For nonzero \(u\) the difference \(h(x)+h(x-u)\) is \(1+h(x+u)\). On a function whose three values sum to zero in \(\mathbf F_2\), taking the same difference translates the function by \(u\). Since \(h+1\) has that property, the resulting bit is \(1+h(2X_I)\). Exactly two of the three values of \(X_I\) give a negative symbol. Across the \(2^{K(n)-2}\) allowed ideals each sum occurs \(2^{K(n)-2}/3+O(1)\) times: multiplying the factors \(1+\zeta_3^u\) gives an absolute value of one at either nontrivial character of \(\mathbf F_3\). Hence \(\gg 2^{K(n)}\) selected ideals have a negative symbol.

The [local Möbius formula](abc_congruent_six_odd_primitive_counts.md) shows that \(U_I\) is the exact first-depth product for this annihilator, except for factors from formal lifting. Since \(I\mid(m)\) is squarefree, an affected ideal must be exactly \(I_{\mathfrak p}\mathfrak p\), for some prime ideal \(\mathfrak p\mid(m)\). There are at most \(2\omega(n)\) such ideals. Discard also the at most \(2\omega(n)\) ideals that actually occur as annihilators at places over \(p\mid n\). Since all selected ideals are distinct even up to conjugation, the remaining negative symbols give distinct rational primes \(p\nmid n\) of odd first depth. Their rational orders divide \(m\), and their depths in \(B_n\) stay odd because \(p\nmid n\). Each \(p\) splits because its rational order is odd. Its reduction group contains the Gaussian module \(\mathcal O/I\), so Hasse gives \(p\ge(\sqrt{NI}-1)^2\ge(\ell_*-1)^2\).

Subtracting \(O(\omega(n))\) from a positive constant times \(2^{K(n)}\) leaves at least \((\log n)^{\log 2-\epsilon}\) primes on density one. This proves both assertions.
