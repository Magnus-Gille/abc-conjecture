# An effective pointwise index bound from the full radical

Let \(a,w,c,d\) be the positive pairwise coprime odd coordinates of the congruent-six orbit. Write \(C=4w^4,\ R=\operatorname{rad}(6awcd)\). For all positive odd indices,
\[
 \log C\ll R^{2/9}(\log R)^3,\qquad
 n\ll R^{1/9}(\log R)^{3/2},
\]
with effective absolute constants. Direct application to the original triple gives only exponents \(1/3\) and \(1/6\), respectively. [Orbit and height](abc_full_quartic_signature.md)

Set \(U=2w-c,\ V=2w+c\). These are positive odd integers since \(c<\sqrt2\,w\), they are coprime since \((c,w)=1\), and \(UV=4w^2-c^2=3d^2\). Consider the three triples
\[
     a^2+c^2=2w^2,\qquad c^2+2a^2=3d^2,\qquad U+V=4w.
\]
They are primitive. Only \(d\) can be divisible by 3, so their radicals are \(R_1=\operatorname{rad}(2acw)\), \(R_2=\operatorname{rad}(6acd)\), and \(R_3=\operatorname{rad}(6wd)\). Every prime above 3 occurs exactly twice among these radicals. The prime 3 occurs in the last two and 2 occurs in all three. Therefore
\[
                 R_1R_2R_3=2R^2 .
\]
Each largest term has logarithm at least \(\tfrac14\log C\), since \(3d^2=2w^2+a^2\). Apply Stewart and Yu's effective estimate \(\log z\ll\operatorname{rad}(xyz)^{1/3}(\log\operatorname{rad}(xyz))^3\) for positive, coprime \(x+y=z\) to the triple with smallest radical. This gives the asserted height bound. The index estimate then follows from \(H n^2-2.2\le\log w\), with \(H=\widehat h(G)>1/3\). C. L. Stewart and K. Yu, *On the abc conjecture, II*, Duke Math. J. 108 (2001), 169–181.

## Limitation of the rational-function support argument

On the smooth complete intersection
\[
 \mathcal B:\quad a^2+c^2=2w^2,\qquad a^2+2w^2=3d^2
\]
the rational boundary consists of five Galois orbits. The three hyperplane sections \(A=\{a=0\},C_0=\{c=0\},W=\{w=0\}\) are each a single degree-four orbit. For instance at \(a=0\), \(c/w=\pm\sqrt2,\ d/w=\pm\sqrt{2/3}\), yielding all four conjugate sign pairs. At \(c=0\) the two independent radicals are \(\sqrt2,\sqrt3\), and at \(w=0\) they are \(i,\sqrt3\). The section \(d=0\) is the union of degree-two orbits \(D_+,D_-\), with \(c/w=2,-2\) respectively and \(a/w=\pm\sqrt{-2}\).

A nonconstant rational function \(f\) over \(\mathbf Q\) with \(f,1-f\) supported on the boundary must use at least three of these orbits in its three disjoint fibers over \(0,1,\infty\). It cannot use precisely \(A,W,D_+\), or the version with \(D_-\): permute the targets so its zeros and poles are \(A,W\), then \(f\) is constant times a positive power of \(a/w\) because these sections are reduced of equal degree. Its values on the two \(D\)-orbits are the same sets, contradicting the support assumption. The argument for \(A,C_0,D_\pm\) uses \(a/c\). For the last possible low-cost support \(A,D_+,D_-\), put \(s=(2w-c)/d\). The identity \(UV=3d^2\) gives \(\operatorname{div}(s)=D_+-D_-\), since \(V\) is nonzero on \(D_+\) and \(U\) is nonzero on \(D_-\). A function supported with zeros and poles on the two \(D\)-orbits is thus a constant times \(s^j,\ j\ne0\). At \(A\) the absolute values of \(s\) include both \(\sqrt3(\sqrt2+1)\) and \(\sqrt3(\sqrt2-1)\), precluding a single value on \(A\).

Consequently, assigning formal radical weights \(0,1/3,1/3,1/6,1/6\) to \(A,C_0,W,D_+,D_-\) gives weight at least \(2/3\) for every such three-fiber support. An argument that only takes the lightest support of rational unit equations on this fixed curve cannot improve the fraction \(2/3\) without further restrictions on the prime masses. This is a statement about the support method. It does not assert existence of indices attaining these formal weights.
