# Quality two from a small denominator radical at a multiple of three

Let \(R=(-8,16)\) on \(E':y^2=x^3+16x^2+32x\). Write \(h=\widehat h(R)>0\) and let \(B_n\) be the positive square root of the reduced denominator of \(x([n]R)\). Along any sequence of odd multiples \(r=3m\) tending to infinity for which \(\log\operatorname{rad}(B_r)=o(r^2)\), an explicit sequence of primitive triples has lower limiting abc quality at least **two**. This also follows if the largest prime factor of \(B_r\) is at most \(r^{4-\delta}\) there for a fixed \(0<\delta<4\), by the [truncated radical estimate](abc_odd_rank_truncated_radical.md). Neither hypothesis is established on an infinite sequence.

Write \(b=B_m\) and \(x([m]R)=-8v^2/b^2\), with \(v,b\) coprime, positive and odd. This is the [odd-index square-norm parametrization](abc_octic_mixed_three_factors.md). One can also get the squareclass directly since the two-isogeny descent map sends a point to its abscissa modulo squares and \(m\) is odd. There is an odd positive integer \(w\) satisfying
\[
   w^2=-b^4+4b^2v^2-2v^4.
\]
Indeed \(w=|y([m]R)|b^3/(16v)\) is rational with integral square. Every odd prime dividing \(b\) is coprime to \(w\) by this identity.

Set
\[
 F_+=b^4+4b^2v^2-2v^4,qquad F_-=b^4-4b^2v^2+6v^4.
\]
Both are positive and odd. The first equals \(2b^4+w^2\), and the second equals \((b^2-2v^2)^2+2v^4\). At **every** odd \(m\) the denominator identity
\[
                      B_{3m}=bF_+F_-
\]
holds, including the entire 3-part when \(3\mid m\). To check this, use \(\psi_3(x)=(x^2+16x-32)(3x^2+16x+32)\). Substitution gives \(b^8\psi_3(-8v^2/b^2)=-1024F_+F_-\). At each odd prime of good reduction the homogeneous abscissa multiplication map has no cancellation. Its homogeneous denominator at the primitive abscissa \((X:Z)=(-8v^2:b^2)\) is \(Z\,(Z^4\psi_3(X/Z))^2\), so the two sides of the asserted identity agree in odd valuation. Both sides are odd. This extends the calculation previously used at a prime input. [Third division polynomial calculation](abc_octic_mixed_three_factors.md)

The triple is
\[
                           2b^4+w^2=F_+=c.
\]
It is primitive because \(w\) is odd and coprime to \(b\). Completing the square gives \(w^2=b^4-2(b^2-v^2)^2\le b^4\). Consequently
\[
  2b^4\le c\le3b^4,\qquad
  \operatorname{rad}(2b^4 w^2F_+)
      \le 2w\operatorname{rad}(bF_+)
      \le 2b^2\operatorname{rad}(B_{3m}).
\]
The odd multiples stay on the bounded real component, whence \(\log b=hm^2+O(1)\). Thus \(\log c=4hm^2+O(1)\). More quantitatively, if \(\rho=\limsup\log\operatorname{rad}(B_{3m})/\log B_{3m}\), these triples satisfy \(\liminf q\ge4/(2+9\rho)\). It suffices for the bound two that \(\log\operatorname{rad}(bF_+)=o(m^2)\), which leaves the remaining factor \(F_-\) unrestricted. For \(m=3\) the triple is \(13122+289=13411\), and \(B_9=9\cdot 13411\cdot2211\).

The companion identity
\[
       b^4+2(b^2-3v^2)^2=3F_-
\]
gives the same lower bound two if \(\log\operatorname{rad}(bF_-)=o(m^2)\). Divide all terms by \(9\) when \(3\mid b\); in this case \(v_3(b^2-3v^2)=1\). Otherwise the triple is already primitive. These are the only cancellations because \((b,v)=1\) and \(b\) is odd. The real bound \(w^2=b^4-2(b^2-v^2)^2>0\) gives \(v^2\le(1+1/\sqrt2)b^2\), so the largest term has log size \(4hm^2+O(1)\). Its radical is at most a constant times \(b^2\operatorname{rad}(bF_-)\).

At every odd prime other than 3, the three factors \(b,F_+,F_-\) have disjoint support. For the pair \(F_+,F_-\), subtract them to obtain \(8v^2(b^2-v^2)\); a common prime cannot divide \(v\), and at \(b^2\equiv v^2\) the two quartics reduce to \(3v^4\). For the other pairs, reduce the quartics at a prime dividing \(b\). Hence choosing the larger quality at each index gives the refinement
\[
    \liminf \max(q_+,q_-)
      \ \ge\ \frac{4}{2+(9\rho+\min(1,9\rho))/2}.
\]
Indeed the smaller of \(\log\operatorname{rad}(bF_+)\) and \(\log\operatorname{rad}(bF_-)\) is at most \((\log\operatorname{rad}(B_{3m})+\log\operatorname{rad}(b))/2+O(1)\), and \(\operatorname{rad}(b)\le\min(b,\operatorname{rad}(B_{3m}))\).

If just one of \(F_+,F_-\) has \(\log\operatorname{rad}(F_\pm)=o(m^2)\), its own triple has lower limiting quality at least \(4/3\), with \(b\) unrestricted. Indeed \(\operatorname{rad}(b)\le b\) gives a log radical of at most \(3hm^2+o(m^2)\). Both of these single-quartic hypotheses are open. [Unconditional restrictions on each quartic's prime support](abc_odd_rank_tripling_primitive_factors.md)
