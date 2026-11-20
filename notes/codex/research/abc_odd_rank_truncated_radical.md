# A quartic prime-size test at arbitrary odd ranks

On \(E:y^2=x^3+16x^2+32x\), put \(R=(-8,16)\) and let \(B_r^2\) be the reduced denominator of \(x([r]R)\). Write \(H=\widehat h(R)>0\). For odd \(r\), \(\log B_r=Hr^2+O(1)\), since all odd multiples lie on the bounded real component. For \(X\ge2\) write \(S_r(X)=\sum_{p\mid B_r,\,p\le X}\log p\). Then
\[
 S_r(X)\ll \tau(r)^2\,\sqrt{X\log(2X)}
\]
uniformly in every odd \(r\) and \(X\ge2\). Thus \(S_r(r^{4-\delta})=o(r^2)\) for every fixed \(0<\delta<4\). In particular, if \(P^+(B_r)\le r^{4-\delta}\) at infinitely many odd ranks, then there is a sequence of primitive rational abc triples of lower limiting quality at least \(8/7\).

## Two bounds for each annihilator

The denominators \(B_r\) at odd ranks are odd. At an odd divisor \(p\) of \(B_r\), the order of \(R\bmod p\) is odd. Thus the reduced \(R\) is twice a point in the same odd-order subgroup. The duplication formula \(x(2Q)=(x(Q)^2-32)^2/(4y(Q)^2)\) makes \(x(R)=-8\) a square modulo \(p\). It follows that \(p\) splits in \(K=\mathbb Q(\sqrt{-2})\).

The full complex multiplication ring \(\mathcal O=\mathbb Z[\sqrt{-2}]\) acts over \(K\). Fix one place above each split \(p\), and define \(I\) to be the annihilator ideal of the reduced point. It divides \((r)\), and the number of possible ideals is at most \(\tau(r)^2\) by prime-ideal factorization. The ring is norm Euclidean, so \(I=(\gamma)\). Write \(D=\operatorname N I\).

Every prime assigned to \(I\) makes \([\gamma]R\) reduce to the identity at the chosen place. Consequently the sum of the distinct \(\log p\) at this ideal is at most the finite denominator contribution to the height of \(x([\gamma]R)\), including both embeddings. The height relation \(h(x([\gamma]R))=2HD+O(1)\) bounds this sum by \(O(D)\). The factor from normalizing the height over the quadratic field is exactly compensated by the double pole of the abscissa.

Alternatively, at ordinary split reduction Frobenius is a multiplier \(\pi\in\mathcal O\) of norm \(p\). It fixes \(R\bmod p\), so \(\pi-1\in I\). The lattice \(I\) is a rotated copy of \(\sqrt D\,\mathcal O\), and the disk \(|\pi|\le\sqrt X\) therefore contains \(O(1+X/D)\) such multipliers, uniformly in the rotation and translation. Distinct primes have different norms. This gives the second bound \(O((1+X/D)\log(2X))\) per ideal. Use the first bound up to \(D=\sqrt{X\log(2X)}\) and the second bound above it. Summing proves the stated estimate. [CM action, heights and ordinary reduction](abc_octic_mixed_cm_prime_mass.md)

## From an odd rank to a primitive triple

Choose \(m=r-1\) or \(r+1\) divisible by four. For large \(r\) this is a positive even index. Write \(x(mR)=u^2/v^2\), with \(u,v\) positive coprime integers. Duplication gives the square abscissa, and the curve equation gives \(w^2=u^4+16u^2v^2+32v^4\) with \(w\) a positive integer. Since \(4R\) has abscissa \(961/196\), it lies in the 2-adic formal group on the displayed integral equation (or in the depth-at-least-two group on the model scaled by 4). Its multiples have even \(v\) and odd \(u,w\). The quartic gives \((v,w)=1\). With \(s=u^2+8v^2\), \(t=u^2+16v^2\), the triple \(1024v^8+u^2s^2t=w^4=c\) is primitive.

The proof of \(s=B_{m-1}B_{m+1}\) uses only that \(m\) is even: a prime of \(s\) has \(mR\) at one of the two distinct reductions \(\pm R\), with depth measured by the abscissa difference. In particular \(B_r\mid s\). The radical estimate for the primitive triple gives
\[
 \log\!\left(\frac{c}{\operatorname{rad}(abc)}\right)
 \ge \log(B_r/\operatorname{rad}(B_r))-O(1),\qquad
 \log c=8Hr^2+O(r).
\]
Indeed the product estimate retains \(s/\operatorname{rad}(s)\), and \(\log w=h(x(mR))+O(1)=2Hm^2+O(1)\) by the positive quartic. Thus any subsequence with \(\log\operatorname{rad}(B_r)=o(r^2)\) gives lower limiting quality at least \(8/7\). Rational abc, conversely, implies \(\log(B_r/\operatorname{rad}(B_r))=o(r^2)\) at all odd ranks. [Primitive triple and product inequality](abc_dyadic_direct_triple.md) · [Exact scalar factorization](abc_dyadic_shifted_rank_mass.md)

Combining this implication with the truncated radical bound shows that, under rational abc, \(\sum_{p\parallel B_r,\ p>r^{4-\delta}}\log p=Hr^2+o(r^2)\). The contribution at exponents \(e\ge2\) is at most twice the excess because \(e\le2(e-1)\). Restricting to primes of exact reduction order \(r\) gives \(H J_2(r)+o(r^2)\) by the scalar Möbius formula.

There is also a consequence specifically for the dyadic factor \(s_n\). If \(P^+(s_n)\le n^{4-\delta}\) along a subsequence, factorization into \(B_{n/2-1}B_{n/2+1}\) gives \(\log\operatorname{rad}(s_n)=o(n^2)\) (one can use \(\delta/2\) at the two nearby ranks). Put \(n=2m\). The separate primitive triple \(w_m^4+128(u_mv_m)^4=s_n\) has radical at most \(2u_mv_m w_m\,\operatorname{rad}(s_n)\le \sqrt{s_n}\,\operatorname{rad}(s_n)/2\). Thus its lower limiting quality is at least two under the stated hypothesis.

## The constant at prime ranks

For an odd prime \(\ell\), at most two proper nontrivial ideals divide \((\ell)\), each of norm \(\ell\); their total log radical is \(O(\ell)\). For \(I=(\ell)\), choosing \(\pi=1+\ell(x+y\sqrt{-2})\) of odd prime norm forces \(x\) even and \(y\ne0\). Thus \(p=(1+2\ell a)^2+2\ell^2 b^2\). For every fixed \(c>0\), the ellipse sieve yields
\[
 \limsup_{\ell\ \mathrm{prime}\to\infty}\frac{S_\ell(c\ell^4)}{c\ell^2}\le8.
\]
To see the constant, set \(B=\sqrt{c\ell^4}/\ell\). The ellipse has area \(\pi B^2/(2\sqrt2)\). At every odd sieve prime \(q\ne\ell\) the local zero density is the same as in the dyadic sieve: the affine linear change of coordinates modulo \(q\) is invertible. The omitted prime \(\ell\) exceeds the sieve cutoff \(B^{1/2-\eta}\), for fixed \(\eta>0\). Counting residue classes, bounding the remainder and evaluating the Selberg sum therefore follows the same proof with half the ellipse area. Every prime gives two choices for the sign of \(b\) and survives the sieve since \(p\ge2\ell^2\). In the limit \(\log(c\ell^4)/\log B\to4\), so the resulting log mass is at most \((8+o(1))B^2\). [Full ellipse sieve calculation](abc_octic_dyadic_fermat_audit.md)

In particular rational abc implies \(\liminf_{\ell\ {\rm prime}}P^+(B_\ell)/\ell^4\ge H/8\). Without invoking abc, any subsequence with \(P^+(B_\ell)/\ell^4\to0\) has negligible radical by taking each fixed \(c>0\) in the sieve estimate, and hence yields the \(8/7\) quality bound. None of these smooth subsequences is established.
