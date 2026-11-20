# A small leg and prescribed growing prime powers on the square conic

Let \(c_*=(\pi/e)^{1/4}\) and \(T(C)=\sqrt{\log C}/\log\log C\). Fix \(0<c<c_*\), \(0<\rho<1/2\), and \(0<\gamma<c_*(1-2\rho)\). There are infinitely many primitive positive triples
\[
             A=u^2,\qquad B=2v^2,\qquad C=w^2,\qquad A+B=C
\]
with all three properties
\[
 \log(C/\operatorname{rad}(ABC))\ge cT(C),\qquad
 p^{\lfloor\rho\log\log C\rfloor}\mid v\quad(p\le cT(C)),\qquad
 \log(C/B)\ge\gamma\sqrt{\log C}.
\]
The last inequality places the two square entries within \(C\exp(-\gamma\sqrt{\log C})\) of each other. It is compatible with the leading radical-gain and prescribed-prime constants of the earlier construction. [Conic identity, congruence lattice and packing estimate](abc_square_conic_growing_primes.md)

## Reserving one real direction in the packing argument

Use a large integer \(d\), the primorial \(D=\prod_{p\le d}p\), and the first \(d\) primes \(\ell_i>d\) splitting in \(\mathbb Q(\sqrt2)\). Choose generators \(\eta_i\) of one prime ideal above each, balanced by the unit \(\epsilon=1+\sqrt2\) so that both absolute real embeddings are at most \(\epsilon\sqrt{\ell_i}\). Set \(w_i=\log\ell_i+2\log\epsilon\), \(v_i'=\log|\eta_i/\bar\eta_i|\), and \(v'=(v_i'/w_i)_{i=1}^d\). Each \(|v_i'|\le2\log\epsilon\), since the absolute norms equal \(\ell_i\), and \(v'\ne0\). In fact equality of the absolute values of the two embeddings would make a generator rational or a rational multiple of \(\sqrt2\), impossible at an odd split prime.

Write \(\kappa=\sqrt{e/\pi}\), \(H=2\kappa d^2(\log d)^2\), \(L_d=\sqrt{2d/\pi}\,\Gamma(2+d/2)^{1/d}\), and \(U=H^d/(L_d^d\prod_i w_i)\). Choose \(\gamma/c_*<\theta<1-2\rho\) and set \(\lambda=\exp(\theta d\log d)\). With \(E=\prod_{p\le d}(1+1/p)\), choose \(M=D^k3^t\) using the largest \(k\) for which \(D^k\le U/(2E\lambda)\), then the largest \(t\ge0\) still satisfying \(M\le U/(2E\lambda)\). Thus
\[
   \log(M\lambda)=\log U-o(d),\qquad
   k=(1-\theta+o(1))\log d,\qquad \operatorname{rad}M=D .
\]
These estimates use \(\log D=d+o(d)\), \(\log E=o(d)\), and the size calculation for \(U\) in the linked note.

Let \(\Lambda\subset\mathbb Z^d\) be the kernel of the projective map given by the \(\eta_i\) modulo \(M\). Its index is at most \(ME\). For \(z\in\Lambda\) put \(x=(w_i z_i)\). Apply the linear map \(P\) that expands the direction \(v'\) by \(\lambda\) and fixes its orthogonal complement. The lattice of vectors \(Px\) has determinant at most \(ME\lambda\prod_iw_i\). The Euclidean packing proof in the earlier note gives a nonzero vector of Euclidean length at most
\[
 \frac{L_d}{\sqrt d}\left(ME\lambda\prod_iw_i\right)^{1/d}
       \le H/\sqrt d .
\]
In fact that proof bounds the Euclidean length before its final conversion to the 1-norm. Undoing \(P\) gives both
\[
    \sum_i w_i|z_i|\le H,\qquad
    \left|\sum_i v_i'z_i\right|
        =|\langle v',x\rangle|
        \le \frac{\|v'\|_2 H}{\lambda\sqrt d}
        \ll \frac{H}{\lambda\log d}.
\]

## The archimedean contribution to the radical

Build the integral element \(\alpha=b+a\sqrt2\) from the \(\eta_i^{z_i}\) when \(z_i>0\) and \(\bar\eta_i^{-z_i}\) when \(z_i<0\). Then \(M\mid a\); the pair \((b,a)\) is primitive, \(b\) is odd, and \(ab\ne0\). Indeed only one prime above each \(\ell_i\) can divide \(\alpha\), and its absolute norm is odd. Write \(J=b^2-2a^2\), \(S=b^2+2a^2\), and \(\xi=\log|\alpha/\bar\alpha|=\sum_i v_i'z_i\). The conic triple has \(A=J^2,\ B=8a^2b^2,\ C=S^2\). Directly from the two real embeddings,
\[
        B/C=\tanh^2\xi,\qquad
        \frac{S}{2|ab|}=\frac{\sqrt2}{|\tanh\xi|}.
\]
The norm radical divides \(\prod_i\ell_i\). Since \(\operatorname{rad}(a)\le |a|D/M\), the whole radical satisfies
\[
  \frac{C}{\operatorname{rad}(ABC)}
      \ge \frac{M}{D\operatorname{rad}|J|}
                 \frac{S}{2|ab|}
      \gg \frac{M\lambda\,\log d}{H D\prod_i\ell_i}.
\]
Thus the reduced finite modulus and the archimedean gain occur as the product \(M\lambda\). The earlier asymptotics \(\log U=d(\log d+\log\log d+\log2+1)+o(d)\) and \(\sum_i\log\ell_i=d(\log d+\log\log d+\log2-1)+o(d)\) give \(\log(C/\operatorname{rad}(ABC))\ge d+o(d)\). Also
\[
       \log(C/B)\ge2\theta d\log d-O(\log d),\qquad
       \log C\le2H=4\kappa d^2(\log d)^2 .
\]
The second inequality uses the bounds on the embeddings of \(\alpha\). Therefore \(T(C)\le(\sqrt\kappa+o(1))d\) and \(\log\log C\le(2+o(1))\log d\). As \(c_*=1/\sqrt\kappa\), the choices of \(c,\rho,\gamma,\theta\) prove all three assertions. The heights are unbounded by the radical gain.

## Allowing different constants for the radical and the prime range

More generally, fix positive \(G,P,\rho,\Gamma\) satisfying
\[
                   G+P<2c_*,\qquad 2\rho P+\Gamma<c_*.
\]
There are infinitely many triples on the same conic for which
\[
 \log(C/\operatorname{rad}(ABC))\ge G T(C),\qquad
 p^{\lfloor\rho\log\log C\rfloor}\mid v\quad(p\le P T(C)),\qquad
 \log(C/B)\ge\Gamma\sqrt{\log C}.
\]
In particular the coefficient \(\rho\) of the prescribed depths can be any positive fixed number; for such \(\rho\) the marked initial prime interval still has length a positive constant times \(T(C)\).

To see this, take \(D=\prod_{p\le\lambda_0 d}p\), with a fixed \(\lambda_0>P/c_*\) chosen small enough that \(G/c_*<2-\lambda_0\) and \(2\rho\lambda_0+\Gamma/c_*<1\). Use the first \(d\) split primes above \(\lambda_0 d\). All earlier prime-generator asymptotics are unchanged to \(o(d)\): the removed split primes have sum of logarithms \(\lambda_0 d/2+o(d)\), and the same number of replacements at the far end have this same log sum up to \(o(d)\). Now \(\log D=(\lambda_0+o(1))d\). Choose \(\Gamma/c_*<\theta<1-2\rho\lambda_0\). With the previous \(H\) and stretch, the certified gain is \((2-\lambda_0+o(1))d\), the marked cutoff is \(\lambda_0d\), and \(k=((1-\theta)/\lambda_0+o(1))\log d\). These three inequalities prove the assertion.

If an equal constant \(c\) is required for the gain and marked cutoff, and no separate real gap is required, a further rescaling gives, for every \(\rho>0\),
\[
    c<c_*\lambda_0 e^{1-\lambda_0},\qquad
             \lambda_0=\min(1,1/(2\rho)).
\]
For the proof use a parameter \(\lambda<\lambda_0\) near \(\lambda_0\), take the primorial through \(\lambda d\), omit the stretch, and replace \(H\) by \(H e^{2\lambda-2}\). The term \(d\log H\) in \(\log U\) changes by \((2\lambda-2)d\) relative to its original value. The gain and cutoff both equal \((\lambda+o(1))d\); the upper bound for \(T(C)\) becomes \((\sqrt\kappa e^{\lambda-1}+o(1))d\). Also \(k=(1/\lambda+o(1))\log d\), sufficient for the given \(\rho\). Letting \(\lambda\) approach the indicated value proves the claim.
