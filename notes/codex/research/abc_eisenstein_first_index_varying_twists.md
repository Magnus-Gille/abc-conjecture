# A prescribed prime at the first index of varying quartic twists

Fix \(\delta>0\). For every sufficiently large prime \(p\), there are a squarefree signed integer \(d\), a nontorsion rational point \(P_d\) on
\[
      E_d:Y^2=X^3-18dX^2+9d^2X ,
\]
and a primitive positive triple \(U^2+3V^2=C_{\rm out}=W^{12}\) represented by this point at **index one**, such that
\[
 \begin{gathered}
   \operatorname{ord}(P_d\bmod p)=1,\qquad
   v_p(B_1(P_d))\ge4k,\qquad k\sim\tfrac{1+\delta}{2}\log\log p,\\
   C_{\rm out}/\operatorname{rad}(3UVW)\gg p^\delta,\qquad
   \log C_{\rm out}\le(12(1+\delta)^2+o(1))
                         (\log p\,\log\log p)^2 .
 \end{gathered}
\]
Here \(B_1(P_d)\) is the positive square root of the reduced abscissa denominator. The prime \(p\) is a good prime of this twist. Every prime in \(W\) is \(1\bmod24\), every prime in \(U\) is \(\pm1\bmod24\), and \(24\mid V\). For almost every \(p\), every such height-bounded first-index witness on these twists requires \(|d|\ge p^{1-\epsilon}\), for each fixed \(\epsilon>0\). Thus the early occurrence is available by varying the point and curve, with an unavoidable twist cost at typical prescribed primes. The certified logarithmic gain is sublinear in \(\log C_{\rm out}\).

## Constructing the point and bounding the entire radical

The prescribed-prime smooth-endpoint construction supplies odd coprime integers \(B<C_0\), both prime to 3, with \(A=C_0-B\) satisfying
\[
       p^k\mid A,\qquad \operatorname{rad}(BC_0)\le p^{k-1-\delta},
       \qquad
       \log C_0\le\left((1+\delta)^2/8+o(1)\right)
                         (\log p\,\log\log p)^2.
\]
In the cited construction take its closeness parameter zero and start its set of prime bases after 2 and 3. Removing these two fixed primes changes the initial prime-sum asymptotics by \(o(1)\) in the limiting constants, so its lattice proof, including the displayed value of \(k\), applies. In particular \(A\) is even and \(\operatorname{rad}(A)\le A/p^{k-1}\), giving \(C_0/\operatorname{rad}(ABC_0)\ge p^\delta\). [Lattice estimate and proof](abc_every_prime_square_gain.md)

Let \(\omega=(-1+\sqrt{-3})/2\) and put
\[
  \alpha=B^4+\omega A^4=x+y\sqrt{-3},\qquad
  x=B^4-A^4/2,\quad y=A^4/2,\quad W=N(\alpha).
\]
Then \(x\) is odd, \(y\) is even, and \((x,y)=1\). The norm
\(W=B^8-B^4A^4+A^8\) is odd and prime to 3. It is \(\asymp C_0^8\) since \(A+B=C_0\) and the quadratic norm in \(B^4,A^4\) is positive definite. The ideals of \(\alpha,\bar\alpha\) are coprime. Their twelfth powers give the indicated primitive triple, with \(U,V\) absolute real and \(\sqrt{-3}\) coefficients. The fixed rational-map transfer proves
\[
       C_{\rm out}/\operatorname{rad}(3UVW)
               \gg C_0/\operatorname{rad}(ABC_0).
\]
In detail the degree-12 coefficient in the variables \(s=B^4,t=A^4\) is divisible (after clearing powers of two) by \(st(s-t)(s+t)\). Its evaluation is divisible by the three coprime input entries up to fixed powers of two. Charging radicals of \(s,t\) by \(AB\) and retaining one of \(B\pm A\) from \(s^2-t^2=B^8-A^8\) gives \(\operatorname{rad}V\ll \operatorname{rad}(ABC_0) C_0^{39}\). The bounds \(|U|\ll C_0^{48}\), \(W\ll C_0^8\) supply the full comparison. Here the retained factor is \(B+A=C_0\); the other seven degrees are charged at full multiplicity. Also \(\log C_{\rm out}=96\log C_0+O(1)\). The norm-prime and numerator-prime restrictions follow from the projective orders in the transfer and \(\alpha^{12}\). [Congruence-restricted transfer](abc_eisenstein_power_conic.md)

Write \(F_0(x,y)=x^4-18x^2y^2+9y^4=d z^2\) with signed squarefree \(d\). The form has no rational projective zero. Put
\[
    P_d=\left(d(x/y)^2,\quad d^2(x/y)z/y^2\right).
\]
Substitution gives the displayed equation of \(E_d\). Since \(p\mid y\) and \(p\nmid x\), \(F_0(x,y)\equiv x^4\ne0\bmod p\); thus \(p\nmid6d\) for these large primes. The abscissa of \(P_d\) has \(p\)-valuation \(-2v_p(y)\), and \(v_p(y)=4v_p(A)\). The point reduces to the identity and is nontorsion since the rational formal group at this good odd prime is torsion-free. This proves the first-index and whole-radical assertions. In terms of output height they give, for any \(c<1/\sqrt3\), a choice of fixed \(\delta\) for which \(\log(C_{\rm out}/\operatorname{rad}(3UVW))\ge c\sqrt{\log C_{\rm out}}/\log\log C_{\rm out}\) for all sufficiently large prescribed \(p\).

The exponent \(k\) can alternatively be fixed, even at two, with \(0<\delta<k-1\). The same argument with the fixed-exponent endpoint theorem gives \(v_p(B_1)\ge4k\), gain \(\gg p^\delta\), and \(\log C_{\rm out}\ll_{k,\delta}(\log p)^{1+k/(k-1-\delta)}\).

## How often a small twist can give so early a witness

For fixed \(\lambda>0,\ \beta>1,\ K>0\), among \(p\in[P,2P]\) the number admitting primitive \((x,y)\), \(y\ne0,\ p\mid y\), satisfying
\[
   F_0(x,y)=d z^2,\quad 0<|d|\le P^\lambda\text{ squarefree},\quad
   \log\max(2,|x|,|y|)\le K(\log P)^\beta
\]
is at most \(P^{\lambda\max(1,\beta-1)+o(1)}\). This count only needs first-power divisibility of \(y\).

Put \(L=\log P\). The 2-isogeny rank bound \(r_d\le2\omega(|d|)+O(1)\) and the uniform minimum positive canonical height \(\gg\log(2|d|)\) give the primitive-pair count per twist
\[
       \ll \left(1+O_K\!\left(\sqrt{L^\beta/\log(2|d|)}\right)\right)
                      ^{2\omega(|d|)+O(1)} .
\]
This follows by packing in the Mordell–Weil lattice and the bounded multiplicity of the map \((x:y)\mapsto d(x/y)^2\). [Uniform twist count](abc_eisenstein_twelfth_large_squares.md)

Fix \(\epsilon>0\). Twists with \(\log(2|d|)\le L^{1-\epsilon}\) contribute \(\exp(o(L))\) in total, using the elementary upper bound \(\omega(n)\ll\log(2n)/\log\log(3n)\). For the rest, the bound just displayed is at most \(L^{O(1)}(C L^{\beta-1+\epsilon})^{\omega(|d|)}\) with fixed \(C\). For any \(t>\max(1,\beta-1+\epsilon)\), summing this over squarefree \(|d|\le P^\lambda\) costs at most
\[
  O(L^{O(1)})\,P^{\lambda t}
           \prod_{\ell\ {\rm prime}}(1+ C L^{\beta-1+\epsilon}\ell^{-t}).
\]
The logarithm of the product is \(O_{t,C}(L^{(\beta-1+\epsilon)/t})=o(L)\), by splitting the sum at \(L^{(\beta-1+\epsilon)/t}\) and comparing to the sum over all integers. Each eligible nonzero \(y\) has \(O_K(L^{\beta-1})\) prime divisors in \([P,2P]\). Let \(t\) tend down and then \(\epsilon\) tend to zero to prove the count.

The constructed height has \(\log H\ll_\delta L^2(\log L)^2\), below \(L^\beta\) for every fixed \(\beta>2\). For \(\lambda<1\), take \(\beta\) so close to 2 that \(\lambda(\beta-1)<1\). The exceptional prime count is then \(o(P/\log P)\). In particular, infinitely many distinct twist classes are necessary on the constructed sequence.

## Scope of the first-index contribution

The prescribed moving power is carried by the denominator \(y\), also a linear factor of the \(\sqrt{-3}\) coefficient. The complete radical estimate additionally uses the small endpoint radicals. Any fixed rational map preserving one of the rational input zero directions has a direct obstruction to moving that **same** inherited prime to an irreducible quartic layer. For a fixed map \(f:\mathbb P^1\to\mathbb P^1\) over \(\mathbb Q\) and rational marked input \(\xi\), the value \(f(\xi)\) is rational and is not a root of any Eisenstein quartic \(F_i\). Outside the finite bad-reduction primes and primes dividing its fixed quartic value at \(f(\xi)\), input congruent to \(\xi\bmod p\) specializes to \(f(\xi)\bmod p\) and \(p\) cannot divide that quartic. This applies to any fixed finite list of such transfers. New arithmetic prime factors and transfers with changing coefficients remain possible.

For two distinct reduced even-degree factors of the original family, a proposal to vary them in a *common* squareclass also forces a fixed finite twist list: the evaluation gcd at a primitive pair divides a fixed homogeneous resultant supported at 2 and 3. Thus the signed squarefree kernels cannot share any other prime. More generally the simultaneous fixed squareclass cover for \(r\) such factors with pairwise disjoint geometric zero sets and total degree \(b\) has genus \(1+2^{r-2}(b-4)\) by Riemann–Hurwitz. Each branch point has inertia order two; distinct roots guarantee independent squareclasses over \(\overline{\mathbb Q}(t)\). A pair of quartics has genus five, as does a triple of quadratics. Faltings gives finiteness for each fixed twist. Two quadratics alone give genus one and can have positive rank. For instance, imposing \(x^2-3y^2=-2a^2,\ x^2+3y^2=b^2\) gives the squaring image \(t'=(t^2-3)/(2t)\) of the earlier slice \(F_0=-2z^2\); it therefore transports the original mechanism, yielding a twenty-fourth power as the largest term.
