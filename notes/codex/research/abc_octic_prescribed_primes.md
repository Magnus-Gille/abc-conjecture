# How many octic exceptions can rely on a prescribed set of primes?

Put \(F=st(s^8-16t^8)\) and \(h=\max(s,t)\), with \(s,t>0\) coprime, \(s\) odd and \(t\) even. Fix \(0<\epsilon<\eta<1\). For any set \(S\) of \(r\) rational primes consider the pairs satisfying
\[
 \operatorname{rad}(|F|)<h^{8-\eta},\qquad
 \prod_{p\notin S}p^{\max(v_p(F)-1,0)}\le h^{\eta-\epsilon}.
\]
There are at most \(C_\epsilon^{r+1}\) such pairs, over all heights. The constant is independent of the primes in \(S\). An elementary determinant argument already gives this bound in each interval \(H\le h\le H^{1+\epsilon/16}\). The assertion over all heights uses the quantitative Subspace Theorem. [Equivalence with rational abc](abc_rational_pell_transfer.md)

## Local contacts and a finite list of choices

There are ten distinct projective roots, all in \(K=\mathbb Q(i,\sqrt2)\). They are \(0,\infty,\pm\sqrt2,\pm i\sqrt2,1\pm i,-1\pm i\). At any odd prime the roots have distinct reductions in the splitting field: the eight roots of \(z^8-16\) are simple nonzero roots in odd characteristic. When \(p\mid F\), a unique projective root at each place above \(p\) accounts for the full valuation, using that \((s,t)\) is primitive. At 2 the even coordinate \(t\) alone accounts for \(v_2(F)\).

For a real linear form \(L_\alpha\) defining one of the four real roots use \(L_\alpha=s-\alpha t\) at finite roots and \(L_\infty=t\). Put \(d=\min_\alpha |L_\alpha|/h\) and \(a_\infty=-\log d/\log h\). Then \(0<d\le1\) and \(|F|/h^{10}\asymp d\), by simplicity of the real roots and compactness on the real projective line. Put \(a_p=v_p(F)\log p/\log h\) for \(p\in S\). The stated pair of inequalities gives
\[
 a_\infty+\sum_{p\in S}a_p\ \ge\ 2+\epsilon-O(1/\log h).
\]
Indeed division of \(|F|\) by its radical removes just the repeated factors, and \(p^{v_p(F)}\) bounds the repeated part at \(p\).

Ignore \(h\) below a sufficiently large constant depending on \(\epsilon\). Choose numbers \(b_j\le a_j\) for \(j\in S\cup\{\infty\}\) by first choosing a nonnegative allocation of total \(2+\epsilon/2\) and then rounding each coordinate down to a multiple of \(\epsilon/(16(r+1))\). Their total \(B\) lies between \(2+7\epsilon/16\) and \(2+\epsilon/2\). By stars and bars there are \(C_\epsilon^{r+1}\) possible rounded vectors. Record also the nearest root at infinity and the roots at the places over \(S\), arbitrarily when there is no contact. There are at most \(10^{4(r+1)}\) choices. In what follows a class fixes both the vector and these roots.

Two distinct pairs of respective heights \(h_1\le h_2\) in the same class have nonzero integer determinant \(D=s_1t_2-s_2t_1\). Common projective root contacts at \(p\) imply \(v_p(D)\ge\min(v_p(F_1),v_p(F_2))\) when both contacts are positive and use the same root, by subtracting the primitive projective congruences. The assertion also holds for the root at infinity. Thus \(|D|\ge h_1^{\sum b_p}\). Their distances to the same real root give \(|D|\ll h_1h_2h_1^{-b_\infty}\). It follows that \(h_2\gg h_1^{1+7\epsilon/16}\). In particular each class has at most one sufficiently large point in \([H,H^{1+\epsilon/16}]\). This proves the interval bound and, by summing intervals, an elementary bound \(O_\epsilon(C_\epsilon^{r+1}(1+\log\log(3X)))\) up to height \(X\).

## The height-independent bound

The input from the quantitative parametric Subspace Theorem is the following standard consequence in dimension two. Fix a number field \(K\), a finite collection of \(K\)-linear forms, and \(0<\delta<1\). At each place use two of these forms with determinant of absolute value one, using coordinates outside a finite set of places. Choose real weights \(c_{1v}+c_{2v}=0\), vanishing outside finitely many places, with \(\sum_v\max_i c_{iv}\le1\). For \(Q\) above a threshold depending on the field, the collection and \(\delta\), the points satisfying
\[
 \prod_v \max_i\bigl(|L_{iv}(\mathbf x)|_v Q^{-c_{iv}}\bigr)\le Q^{-\delta}
\]
belong, for the union over all such \(Q\), to a bounded number of proper linear subspaces depending in number only on those same fixed data. Absolute values are product-formula normalized. Uniformity in the identities of the finite places is essential here: the number and heights of the distinct linear forms and the determinant product stay bounded as the prime set changes. This is the large-solutions statement; no bound on the heights of the individual exceptional lines is used. Direct access to the primary PDFs returned HTTP 403. I checked the stated parameter dependence against the linked transcription of the survey's large-solutions result. [Evertse, *On the Quantitative Subspace Theorem*](https://arxiv.org/abs/1008.2268) · [Evertse and Ferretti, parametric theorem](https://arxiv.org/abs/1008.2340) · [Parameter and threshold comparison](https://github.com/rwst/Subspace-Theorems/blob/2fc7bea12d398fbc8ea758ecb8516efe8e3ef33d/QuantitativeSubspace/README.md#L2125-L2131)

For a fixed class take \(Q=h^{B/2}\). At each place \(v\) over \(j\in S\cup\{\infty\}\) write \(\kappa_v=[K_v:\mathbb Q_j]/[K:\mathbb Q]\). Use the selected linear form \(L_{1v}\) and a complementary coordinate \(L_{2v}\) with determinant \(\pm1\). The root is interpreted at that particular embedding, including at infinite places. Assign \(c_{1v}=-\kappa_v b_j/B,\ c_{2v}=\kappa_v b_j/B\). At all other places use the coordinates with zero weights. These choices have \(\sum_v\max_i c_{iv}=1\). At a finite place over \(p\in S\) the maximum in the product is at most \(h^{-\kappa_v b_p/2}\), by the contact recorded at \(p\) and integrality of the other coordinate. At an infinite place the bound is \(O(h^{\kappa_v(1-b_\infty/2)})\). The constants are absolute since the forms come from a fixed finite list. Hence the twisted height is \(O(h^{1-B/2})\), at most \(Q^{-\epsilon/16}\) for \(h\) above an \(\epsilon\)-dependent threshold. The Subspace Theorem now bounds the number of lines per class by a constant depending on \(\epsilon\). A line contains at most one positive primitive pair. Smaller heights can be included in \(C_\epsilon\), proving the all-heights bound.

In particular, among all such exceptional pairs the number for which the product of the distinct repeated primes is at most \(Z\) is \(O_\epsilon(Z(1+\log(2Z))^{C_\epsilon})\). Apply the theorem with \(S\) equal to the set of prime divisors of that product and sum over squarefree products up to \(Z\). The sum of \(C_\epsilon^{\omega(n)}\) over squarefree \(n\le Z\) is bounded by the summatory divisor function of any fixed integral order above \(C_\epsilon\). This argument leaves open an infinite family using successively different prime sets with growing products.

## The local threshold of two is attained

Write \(s_j+t_j\sqrt2=(3+2\sqrt2)^{2^j}\), \(j\ge0\). These pairs are primitive with \(s_j\) odd, \(t_j\) even, and \(s_j^2-2t_j^2=1\). Their heights are \(h_j=s_j\). The other factors have full order in \(h_j\), so \(|F_j|\asymp h_j^8\). Doubling gives \(t_{j+1}=2s_jt_j\), hence \(v_2(F_j)=v_2(t_j)=j+1\) and \(2^{v_2(F_j)}\asymp\log h_j\). It follows both that \(\operatorname{rad}(|F_j|)\ll h_j^8/\log h_j\) infinitely often and that the archimedean and 2-adic contacts together can reach \(h_j^2\log h_j\). The logarithmic gain is compatible with abc at every fixed positive exponent.
