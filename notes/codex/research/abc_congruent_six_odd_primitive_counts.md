# How many primes occur to odd exponent at the same elliptic index?

Take \(G=(-3,9)\) on \(E:y^2=x^3-36x\). Write \(B_n^2\) for the reduced denominator of \(x([n]G)\), and \(\operatorname{sf}(B_n)=\prod_{v_p(B_n)\text{ odd}}p\). Say that a prime first occurs at \(n\) if it divides \(B_n\) and divides no earlier term. These are the primes at which \(G\) has exact reduction order \(n\), away from 2 and 3. Those two primes do not divide odd terms. The associated primitive abc triples satisfy \(a^4+3b^2=4B_n^4\) at odd \(n\).

There is an explicit set \(\mathcal P\) of rational primes of density \(1/18\) with the following property. For **any** distinct \(q_1,\ldots,q_t\in\mathcal P\), put \(r=\prod q_j\). Then

* At least \(3^{t-1}\) distinct primes first occur at \(r\) with **odd** exponent.
* The entire denominator \(B_r\) has at least \((4^t-1)/3\) distinct prime factors with odd exponent. At least \((4^t-1)/6\) of them are \(\ge(\sqrt r-1)^2\).

Thus \(\log\operatorname{sf}(B_r)\gg4^t\log r\) for large \(r\). Taking the first \(t\) primes of \(\mathcal P\) gives
\[
 \log\log\operatorname{sf}(B_r)\ \ge\
  (\log 4-o(1))\,\frac{\log r}{\log\log r}.
\]
The bound concerns actual prime bases to odd exponent. It gives no upper bound for the square dividing \(B_r\).

For \(r=265=5\cdot53\), exact integer arithmetic exhibits five pairwise coprime nonsquare divisors of \(B_{265}\), each relatively prime to the complementary factor. Three are relatively prime also to \(B_5B_{53}\), forcing three odd-exponent primes of exact order 265. Those three divisors have lengths 269, 1064 and 13864 bits. [Independent integer check](abc_congruent_six_odd_counts_check.py)

## Separating the valuations

Over \(K=\mathbf Q(i)\), write \(D_I\) for the norm of the denominator ideal of \([\alpha]G\), where \(I=(\alpha)\) is a nonzero Gaussian ideal. Its value is independent of the choice of generator. Use only ideals of odd norm. For a good Gaussian place \(\mathfrak p\), let \(I_{\mathfrak p}\) be the annihilator of the reduction of \(G\). At any multiple \(I=(\alpha)\) of \(I_{\mathfrak p}=(\gamma)\), the local depth is exactly \(e_{\mathfrak p}+v_{\mathfrak p}(\alpha/\gamma)\), by the isometric formal logarithm; other ideals have zero depth. For the odd norms in this note all contributing rational primes are \(1\bmod12\). Indeed \([N\alpha]G\) is formal whenever \([\alpha]G\) is formal, and odd-order primes have this residue restriction by two-descent. Consequently all relevant places have residue degree one. At a prime of order \(s\), the first depth equals \(v_p(B_s)\) since \(p\nmid s\). This follows from \(4\mid\#E(\mathbf F_p)<4p\). These are also direct consequences of the [Gaussian denominator calculation](abc_congruent_six_gaussian_first_primes.md).

Let
\[
 U_I=\prod_{J\mid I}D_J^{\mu(I/J)},\qquad
 V_I=\prod_{I_{\mathfrak p}=I}(N\mathfrak p)^{e_{\mathfrak p}}.
\]
Then \(U_I\) is a positive integer. It equals \(V_I\) times the product of \(N\mathfrak p\) over \(\mathfrak p\) such that \(I=I_{\mathfrak p}\mathfrak p^j\) for some \(j\ge1\). To verify this, the first-depth part at a given place contributes to the Möbius transform just at \(I_{\mathfrak p}\). Its lifting term counts \(j\ge1\) for which \(I_{\mathfrak p}\mathfrak p^j\mid I\), giving precisely the stated factors after inversion. The fixed bad places contribute nothing for odd norm.

Choose \(\mathcal P\) as the primes \(q\equiv5\bmod12\) with opposite nonzero cubic labels at 13. Explicitly, for a Gaussian prime \(\lambda=a+bi\) above \(q\), choose \(a\) odd, \(b\) even, and compute the base-2 discrete logarithms of \(a+5b\) and \(a-5b\) in \(\mathbf F_{13}^\times\), modulo 3. They must be \(1,2\) in either order. The label is invariant under generator sign, and conjugating interchanges the entries. The calculation of the density, the positive denominator formula, and the residue check at 193 are given in the [character proof and 144-case verifier](abc_congruent_six_cubic_packet_character.md). No \(q\in\mathcal P\) divides an odd denominator, since \(q\not\equiv1\bmod12\). Thus for every \(I\mid(r)\) all the lifting corrections vanish: \(U_I=V_I\).

## Counting signs

Give the Gaussian factors \(\lambda,\bar\lambda\) over each \(q_j\) opposite signs \(\sigma=1,-1\) according to their first cubic label. For \(I=\prod \lambda^{a_\lambda}\), put \(C_I=\sum a_\lambda\sigma_\lambda\bmod3\). Its second label is \(-C_I\). The Legendre symbol of \(D_I\) modulo 193 is \(-1\) precisely when \(C_I\ne0\). The exponent of \(-1\) can be written as the trace of \(\zeta^{C_I}\) from \(\mathbf F_4\) to \(\mathbf F_2\), where \(\zeta\) has order three. In the Möbius transform signs of integer coefficients disappear modulo two. The bit for \(U_I\) is
\[
 \operatorname{Tr}\!\left(\zeta^{C_I}
    \prod_{\lambda\mid I}(1+\zeta^{-\sigma_\lambda})\right)
     = \operatorname{Tr}\!\left(\zeta^{C_I+\sum_{\lambda\mid I}\sigma_\lambda}\right).
\]
For a squarefree \(I\) this is \(\operatorname{Tr}(\zeta^{2C_I})\), equal to one exactly when \(C_I\ne0\).

For rational order \(r\), the annihilator must have \(I\cap\mathbf Z=(r)\). At each \(q_j\) the Gaussian prime choices in \(I\) are \(\lambda,\bar\lambda,\lambda\bar\lambda\). These contribute \(1,-1,0\) to \(C_I\) in some order, so exactly \(2\cdot3^{t-1}\) of the ideals have a negative symbol. Each \(V_I\) then has a rational prime to odd exponent. Every such \(I\) is distinct from its conjugate. A rational prime contributes at most one of its places to that \(I\), and its other place has annihilator \(\bar I\). Thus negated symbols in different conjugate pairs give different rational primes, of the stated first depth and rational order.

Allowing all rational orders dividing \(r\) adds a fourth choice at each \(q_j\), with contribution zero. Among the \(4^t\) ideals the number with \(C_I\ne0\) is \(2(4^t-1)/3\), by the elementary character sum \(2+\zeta_3+\bar\zeta_3=1\) for a complex primitive cube root \(\zeta_3\). These prime bases still have odd valuation in \(B_r\) since none divide \(r\). The involution \(I\mapsto(r)/I\) negates \(C_I\), commutes with conjugation, and pairs norms with product \(r^2\). At least half of the relevant conjugate pairs therefore have \(NI\ge r\). At a contributing split \(p\), \(E(\mathbf F_p)\) contains \(\mathcal O/I\) via the orbit of \(G\) under the Gaussian endomorphisms. Hasse's bound gives \(p\ge(\sqrt{NI}-1)^2\), proving the size assertion.

## Including prime powers

For \(n=\prod_{j=1}^t q_j^{e_j}\) with these same primes, the signs similarly force at least
\[
 \frac{\prod_j(2e_j+1)-\prod_j s_{e_j}}{3}
\]
distinct odd-exponent first occurrences at \(n\), where \(s_e\) is \(0,2,-2\) for \(e\equiv1,2,0\bmod3\), respectively. In the entire \(B_n\) they force at least
\[
 \frac{\prod_j(e_j+1)^2-\prod_j t_{e_j}}{3},
\qquad t_e=\begin{cases}3&e\equiv2\bmod3,\\1&\text{otherwise}.\end{cases}
\]
Indeed for exponents \(a,b\) at a conjugate pair, its contribution to the transformed trace argument is \(\pm(f(a)-f(b))\) with \(f(0)=0\), \(f(a)=a+1\) for \(a>0\). Summing the complex cubic character over \(0\le a,b\le e\) gives \(\left|\sum_{a=0}^e\zeta_3^{f(a)}\right|^2=t_e\). Restricting to \(\max(a,b)=e\) gives \(t_e-t_{e-1}=s_e\). The sums are real, and conjugation pairs the two nonzero total labels, yielding the formulas. For instance, at \(n=5^k\) the full denominator has at least \(((k+1)^2-3)/3\) distinct odd-exponent prime factors.
