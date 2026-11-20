# Many Pythagorean triples at one hypotenuse with separately prescribed prime divisors

Fix \(0<\eta<1\). There are arbitrarily large square integers \(C=u^2\) with the following property. Write \(L=\log\log C\). At least
\[
 c_\eta\,\frac{L}{(\log L)^3}
\]
distinct primitive pairs \(v^2+w^2=C\), with \(0<v\le u/2<w\), each satisfy
\[
 \frac{C}{\operatorname{rad}(uvw)}
 \ \ge\ \exp\!\left(c_\eta\,\frac{L^2}{(\log L)^4}\right).
\]
For each selected pair there is a prime \(q\) such that \(q^{v_q(v)-1}\ge(\log C)^\eta\), and \(q\) divides none of \(u\) or the legs of any other selected pair. The constants can be decreased to use the same \(c_\eta>0\) in both displays. The total saving here exceeds every fixed power of \(\log C\). Its guaranteed logarithm is still \(o(\log C)\).

The proof uses Linnik's theorem on the least prime in a reduced residue class and the symmetric Lovász local lemma. The remaining estimates are elementary.

For a finite example take the 3,637-digit hypotenuse \(u=205^{1573}\). The smaller and larger absolute coordinates of \((-133-156i)^{1573}\) give \(v_1,w_1\); those of \((187+84i)^{1573}\) give \(v_2,w_2\). Both base norms are \(205^2\). Exact integer exponentiation gives \(2v_j\le u\), \(\gcd(v_j,w_j)=1\), \(v_{13}(v_1)=2\), and \(v_{11}(v_2)=3\). The prime 13 is absent from \(uv_2w_2\) and 11 is absent from \(uv_1w_1\). The inequalities \(5\cdot13u^2>7\cdot205v_1w_1\) and \(5\cdot121u^2>9\cdot205v_2w_2\) certify radical savings greater than \(7/5\) and \(9/5\) respectively without factoring the large legs. This example illustrates separate prime contributions at one exact height; the following construction proves the asymptotic bounds.

## Specifying the residues of Gaussian integers

Take a large integer \(d\). Fix \(\eta<\eta'<1\) and a small \(\kappa>0\) with \((1+\kappa)\eta'<1\). Set \(n=\lfloor\kappa d\rfloor,\ m=d+n-1,\ r=1+\lceil\log_2 m\rceil\). Choose \(m\) sign vectors \(\sigma_h\in\{-1,1\}^r\) distinct up to reversal, and a prime \(\ell>m+1\) of size \(O(m)\). Choose distinct nonzero \(a_h\in\mathbb F_\ell\). For each \(h\) there is \(c_h\in\mathbb F_\ell^r\) with
\[
 c_h\cdot\sigma_h=0,\qquad c_h\cdot\sigma_i\ne0\quad(i\ne h).
\]
No two rows are proportional over \(\mathbb F_\ell\). The unwanted \(m-1\) hyperplane sections each cover only \(1/\ell\) of \(\sigma_h^\perp\).

Choose distinct primes \(q_h\equiv1\bmod 4\ell\) with \(q_h\ll m^{O(1)}\). For this step take a second prime \(\ell'>m+1\) of size \(O(m)\), different from \(\ell\), and assign distinct nonzero residues modulo \(\ell'\). The Chinese remainder theorem and Linnik's theorem for modulus \(4\ell\ell'\) give the required distinct primes. Write \(Q=\prod_h q_h\), so \(\log Q=O(d\log d)\). For each \(h\) choose \(s_h\in\mathbb F_{q_h}\) with \(s_h^2=-1\) and \(g_h\in\mathbb F_{q_h}^\times\) of order \(\ell\).

For \(0\le j<d,\ 1\le b\le r\), construct \(\gamma_{jb}=1+iK_{jb}\) with positive even \(K_{jb}\), and put \(A_{jb}=1+K_{jb}^2,\ \alpha_{jb}=\gamma_{jb}/\bar\gamma_{jb}\). In the split coordinate \(i\mapsto s_h\bmod q_h\), prescribe
\[
 \alpha_{jb}\equiv g_h^{a_h^j c_{hb}}\pmod {q_h}.
\]
For target \(\xi\), solve \(K\equiv(\xi-1)/(s_h(\xi+1))\); the denominator is nonzero since \(\ell\) is odd. Neither \(1+s_hK\) nor \(1-s_hK\) vanishes, so these norms are coprime to all the \(q_h\).

We need pairwise coprime norms with \(\log R_0=O_\eta(d^2(\log d)^2)\), where \(R_0=\prod_{j,b}A_{jb}\). Here are details of the size bound. Put \(J=dr\), let \(Y=C_0J\) for a sufficiently large absolute constant \(C_0\), and let
\[
 W=Q\prod_{p\le Y,\ p\nmid Q}p .
\]
Require each \(K\) to be zero mod the extra primes and take its prescribed residues mod \(Q\). Independently for each index sample \(K\) from \(W\) positive consecutive representatives of its residue class in an arithmetic progression of step \(W\), choosing them all at most \(2W^2\). Chebyshev's bound \(\sum_{p\le Y}\log p=O(Y)\) gives \(\log W=O_\eta(d\log d)\).

For a pair of indices the probability of a common prime divisor of the norms is \(O(1/Y)\). Primes of \(W\) cannot divide any norm. For \(Y<p\le W\), each norm is divisible with probability at most \(2/p+2/W\), since the quadratic congruence has at most two roots. Summing squares of these bounds gives \(O(1/Y)\). For \(p>W\), condition on the first norm: it is at most \(1+4W^4\) and hence has at most five such prime factors for large \(W\). Each divides the second norm with probability at most \(2/W\). A given pair event shares indices with at most \(2J-4\) others and is independent of the collection of all disjoint events. The symmetric local lemma therefore permits simultaneous avoidance when \(C_0\) is sufficiently large. This proves the norm budget since \(J=O_\eta(d\log d)\). Each \(\gamma_{jb}\) is also coprime to its conjugate, by its odd norm and real part 1.

## Simultaneous approximation

Fix principal arguments \(\theta_{jb}=\arg\alpha_{jb}\) and put \(\beta_{hj}=\prod_b\alpha_{jb}^{\sigma_{hb}}\). At \(q_h\), \(\beta_{hj}\equiv1\) in both split coordinates. Choose a fixed small \(s>0\) with \(s+(1+\kappa)\eta'<1\). Let \(B=\lceil\exp(C_1 d(\log d)^3)\rceil\), where the constant \(C_1\) will be chosen large, and put
\[
 T=\eta'\log B,\qquad S=(sd/r)\log B,\qquad
 t_h=1+\left\lceil T/\log q_h\right\rceil.
\]
There is a nonzero integer vector \(z=(z_0,\ldots,z_{d-1})\), \(|z_j|\le B\), satisfying
\[
 \prod_j\beta_{hj}^{z_j}\equiv1\bmod q_h^{t_h}\quad(1\le h\le m),\qquad
 \left|\sum_j z_j\theta_{jb}\right|<e^{-S}\quad(1\le b\le r).
\]
In fact take vectors from \(\{0,\dots,B\}^d\). For row \(h\) record the residue of its product in one split coordinate; the other coordinate is its inverse because the norm is one. Since the product is already 1 mod \(q_h\), there are at most \(q_h^{t_h-1}\) choices. For each \(b\), record the bin of width \(e^{-S}\) containing the unwrapped real sum \(\sum_jz_j\theta_{jb}\). This takes \(O(dB e^S)\) choices. The logarithm of the total number of records is at most
\[
 mT+\log Q+r(\log B+S+O(\log d))<d\log B
\]
for all sufficiently large \(d\). A difference of two vectors in one cell gives the desired \(z\).

Divide \(z\) by the highest common power of \(\ell\) in its entries. The real bounds persist, as do the residue conditions: the products lie in finite groups of \(q_h\)-power order, with \(q_h\ne\ell\). The polynomial \(F(X)=\sum_j z_jX^j\bmod\ell\) is now nonzero. Its degree is at most \(d-1\), so \(F(a_h)\ne0\) for at least \(m-d+1=n\) indices. Retain those rows.

## The common hypotenuse

Set
\[
 u=\prod_{j,b}A_{jb}^{|z_j|},\qquad Z_h=u\prod_j\beta_{hj}^{z_j}.
\]
At each active index \((j,b)\), the factor in \(Z_h\) is either \(\gamma_{jb}^{2|z_j|}\) or its conjugate. The disjoint, odd norm supports imply \(\gcd(Z_h,\bar Z_h)=1\) in \(\mathbb Z[i]\), so the two integer coordinates are coprime and neither is zero. The norm is \(u^2\). The unwrapped angle has absolute value at most \(r e^{-S}\). Thus \(v_h=|\operatorname{Im}Z_h|\le r e^{-S}u<u/2\), \(w_h=\operatorname{Re}Z_h>0\), and \(v_h^2+w_h^2=u^2\).

At its own prime, \(Z_h\equiv u\bmod q_h^{t_h}\), so \(q_h^{t_h}\mid v_h\). For row \(i\ne h\) the residue of \(Z_i/u\) in the first split coordinate at \(q_h\) is \(g_h^{(c_h\cdot\sigma_i)F(a_h)}\), of order \(\ell>4\). A norm-one element with vanishing real or imaginary coordinate has order dividing 4. Hence \(q_h\) divides neither leg of row \(i\); it also does not divide \(u\). In particular the retained pairs are distinct.

Since \(\operatorname{rad}(u)\le R_0\), we have
\[
 \log\frac{u^2}{\operatorname{rad}(uv_hw_h)}
 \ge S+T-\log(rR_0).
\]
The norm budget has an absolute implied constant once \(\eta,\kappa\) have been fixed. Choosing \(C_1\) sufficiently large ensures that \(S-\log(rR_0)\gg_\eta d^2(\log d)^2\). Moreover \(\log u\le B\log R_0\), while \(u\ge v_h\ge q_h^{t_h}\ge e^T\), so the heights escape to infinity. Writing \(L=\log\log C\) gives \(L\le\log B+O_\eta(\log d)\ll_\eta d(\log d)^3\), and hence \(d\gg_\eta L/(\log L)^3\) by monotonicity. The same monotonicity applied to \(L^2/(\log L)^4\) bounds that quantity by \(O_\eta(d^2(\log d)^2)\). Finally \(q_h^{t_h-1}\ge e^T\ge(\log C)^\eta\) for large \(d\). This proves all the assertions.

The construction obtains part of the saving from a small real leg and part from divisibility at the selected prime. The lower bound on the individual prime's contribution is smaller than the bound on their combined effect.

The height estimate \(\log u\le M(S+T)\) for a fixed \(M\), previously proposed as a way to turn this construction into a disproof, is impossible. For each column let \(G_b\) be the product of \(\gamma_{jb}^{|z_j|}\) or \(\bar\gamma_{jb}^{|z_j|}\) according to the sign of \(z_j\). These nonunits are coprime to their conjugates, so \(|\operatorname{Im}G_b|\ge1\). If \(\theta_b=\sum_jz_j\theta_{jb}\), then \(G_b/\bar G_b=e^{i\theta_b}\). With \(D_b=N(G_b)\), this gives
\[
 1\le\sqrt{D_b}\,|\sin(\theta_b/2)| < \tfrac12\sqrt{D_b}\,e^{-S}.
\]
Consequently \(\log u=\sum_b\log D_b>2r(S+\log2)\). Here \(r\to\infty\) and \(T/S=\eta' r/(sd)\to0\). Thus the saving proved in the construction, \(S+T-\log(rR_0)\) on the logarithmic scale, cannot reach a positive multiple of \(\log C\). Additional prime powers in the actual legs remain possible. A [bound allowing different axes for each triangle](abc_gaussian_height_obstruction.md) limits the corresponding geometric alternative.

## Why varying the exponents helps

For comparison, take finitely many fixed non-torsion Gaussian rotations \(\beta_h\) with denominator \(A>1\) and normalized legs from \(\beta_h^E\) at \(u=A^E\), which are assumed primitive. Choose distinct fixed odd primes \(q_h\nmid A\). At a prime above \(q_h\), the order \(o_h\) of \(\beta_h^4\) modulo that prime is coprime to \(q_h\). If \(q_h\mid v_hw_h\), then \(o_h\mid E\), and lifting at this unramified odd prime gives
\[
 v_{q_h}(v_hw_h)=v_{\mathfrak q_h}(\beta_h^{4o_h}-1)+v_{q_h}(E).
\]
Indeed \(\beta_h^{4E}-1\) differs from \(4iv_hw_h/u^2\) by a unit, and the standard binomial lifting formula applies after the first occurrence. Thus the product of the \(n\) fixed-prime contributions \(q_h^{\max(v_{q_h}(v_hw_h)-1,0)}\) is \(O(E)\), since the distinct \(q_h^{v_{q_h}(E)}\) have product dividing \(E\). At least one contribution is \(O((\log u)^{1/n})\). The implicit constants here depend on the fixed rotations and primes. The construction above varies many exponents at once.
