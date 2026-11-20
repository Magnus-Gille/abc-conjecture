# Prescribed prime powers on the conic \(u^2+2v^2=w^2\)

Write \(T(C)=\sqrt{\log C}/\log\log C\) and use natural logarithms. For every \(0<c<(\pi/e)^{1/4}\) and \(0<\rho<1/2\) there are infinitely many primitive triples
\[
                  A=u^2,\qquad B=2v^2,\qquad C=w^2,\qquad A+B=C
\]
of positive integers with both
\[
  \log\!\frac{C}{\operatorname{rad}(ABC)}\ge c\,T(C),\qquad
  p^{\lfloor\rho\log\log C\rfloor}\mid v
       \quad\text{for every prime }p\le c\,T(C).
\]
The specified prime powers alone pay for the radical estimate below. Their number tends to infinity. These are lower bounds at sublinear scale in \(\log C\), and do not establish a fixed abc exponent. The restriction to the displayed conic and the initial segment of prescribed primes is part of the assertion. For unrestricted triples stronger numerical constants for the size of the radical gain are known. [Comparison and literature](abc_smooth_congruences.md)

For a finite illustration write \(b+a\sqrt2=(9+7\sqrt2)^{294}\). This gives \(J=17^{294}\) and the identity below gives a primitive triple with 1,501 digits in \(C\). The valuations of \(a\) at \(3,5,7\) are all exactly three. Thus each has exponent six in \(B\), and these primes alone certify \(C/\operatorname{rad}(ABC)\ge11025S/(34|ab|)>917\). These integers can be reproduced by starting at \((b,a)=(1,0)\) and applying \((b,a)\mapsto(9b+14a,7b+9a)\) 294 times.

## Parameters and prime support

In \(\mathbf Z[\sqrt2]\) let \(\epsilon=1+\sqrt2\). Given a primitive pair \((b,a)\) with \(ab\ne0\), put \(J=b^2-2a^2\), \(S=b^2+2a^2\). The identity
\[
                         J^2+8a^2b^2=S^2
\]
gives a primitive triple on dividing by \(g^2\), where \(g=\gcd(J,S)\) is 1 if \(b\) is odd and 2 if \(b\) is even. Then \(u=|J|/g,\ v=2|ab|/g,\ w=S/g\). Indeed no odd prime can divide \(J,S\) simultaneously at a primitive pair. When \(b\) is even, \(a\) is odd and \(J,S\) both have exact 2-adic valuation one.

If \(M\) is a positive integer dividing \(a\) and \(D=\operatorname{rad}(M)\), then \(M\mid v\) and \(\operatorname{rad}(|a|)\le |a|D/M\). Since \(\operatorname{rad}(ABC)\le 2\operatorname{rad}(|J|)\operatorname{rad}(|a|)|b|S\) and \(S\ge2\sqrt2|ab|\), one has
\[
          \frac{C}{\operatorname{rad}(ABC)}
                    \ge \frac{\sqrt 2}{4}\frac{M}{D\operatorname{rad}(|J|)} .
\]

## A congruence lattice of growing rank

Take a large integer \(d\), set \(y=d\), and use every prime \(p\le y\) in \(D\). The prime number theorem gives \(\log D=d+o(d)\). Let \(\ell_1,\ldots,\ell_d\) be the first \(d\) rational primes above \(y\) that split in \(\mathbf Q(\sqrt2)\). Choose one prime ideal above each. This ring is norm Euclidean and each such ideal has a generator \(\eta_i\) of absolute norm \(\ell_i\). A power of \(\epsilon\) balances its two real embeddings so that both have absolute value at most \(\epsilon\sqrt{\ell_i}\). Put \(w_i=\log\ell_i+2\log\epsilon\).

For a modulus \(M\) supported on \(D\), map \(\mathbf Z^d\) into \((\mathcal O/M)^\times/(\mathbf Z/M)^\times\) by the projective classes of the \(\eta_i\). At an odd prime power \(p^j\), the projective group has order \(p^{j-1}(p-(2/p))\), by counting units in the split or unramified quadratic algebra. At \(2^j\) a quadratic element is a unit exactly when its scalar coefficient is odd, giving projective order \(2^j\) for the group. The kernel lattice therefore has determinant at most
\[
              M E,\qquad E=\prod_{p\mid D}(1+1/p).
\]
The bound \(\log E=O(\log y)=o(d)\) already follows by summing over all integers. Put \(\kappa=\sqrt{e/\pi}\) and define
\[
    H=2\kappa d^2(\log d)^2,\quad
    L_d=\sqrt{2d/\pi}\,\Gamma(2+d/2)^{1/d},\quad
    U=\frac{H^d}{L_d^d\prod_i w_i}.
\]
For sufficiently large \(d\), take \(k=\lfloor\log(U/(2E))/\log D\rfloor\) and then the largest \(t\ge0\) with \(M=D^k3^t\le U/(2E)\). Since \(3\mid D\), this gives \(\operatorname{rad}M=D\), \(ME<U\), and \(\log M=\log U-o(d)\).

There is a nonzero kernel vector \(z\) with \(\sum_i w_i |z_i|\le H\). Here is the Euclidean packing estimate that gives the constant. Scale coordinate \(i\) by \(w_i\), so the determinant of the scaled lattice is at most \(ME\prod_i w_i\). An arbitrary lattice of determinant \(\Delta\) has a nonzero vector of 1-norm at most \(L_d\Delta^{1/d}\). To see this, normalize its shortest Euclidean distance to 2 and put \(f(x)=\max(1-\|x\|_2^2/2,0)\). If \(m>0\) lattice points are within \(\sqrt 2\) of \(x\), the sum of their squared distances to \(x\) is at least \(2(m-1)\), by the centroid identity and pairwise separation. Thus \(\sum_v f(x-v)\le1\). Integrating over a fundamental domain gives determinant at least \((2\pi)^{d/2}/\Gamma(2+d/2)\). Rescale and use \(\|x\|_1\le\sqrt d\,\|x\|_2\) to get the inequality, which applies here since \(ME<U\).

Form an integral parameter \(\alpha=b+a\sqrt2\) using \(\eta_i^{z_i}\) for positive \(z_i\) and \(\bar\eta_i^{-z_i}\) for negative \(z_i\). This represents the same projective class modulo \(M\), since multiplication by \(\ell_i\) or \(-\ell_i\) is an invertible scalar there. The element is scalar modulo \(M\), so \(M\mid a\).

For each nonzero \(z_i\), exactly one of the conjugate prime ideals above \(\ell_i\) divides \(\alpha\). There are no other prime ideal factors. Thus the coordinate pair is primitive, and \(\operatorname{rad}(|J|)\le\prod_i\ell_i\). Both \(a,b\) are nonzero: a rational element or a rational multiple of \(\sqrt2\) has equal valuations at the two primes above any odd split prime. Both real embeddings of \(\alpha\) have absolute value at most \(e^{H/2}\). Since \(S\) is the average of the squares of these embeddings, \(\log C\le 2H\).

## Size calculation

The \(j\)-th odd split prime \(q_j\) satisfies \(q_j\sim2j\log j\) by the prime number theorem in the classes \(1,7\bmod8\). Consequently
\[
 \sum_{i=1}^d\log\ell_i
    =d(\log d+\log\log d+\log 2-1)+o(d),\qquad
 \sum_{i=1}^d\log w_i=d\log\log d+o(d).
\]
For the first estimate, summing \(\log q_j=\log j+\log\log j+\log2+o(1)\) gives the stated expansion for the first \(d\) split primes. Removing those at most \(d\) and replacing the same number at the far end changes the sum by \(o(d)\). Indeed their number is \((1+o(1))d/(2\log d)\), the removed sum is \(d/2+o(d)\) by the prime number theorem in the two classes, and each replacement contributes \((1+o(1))\log d\). For the second estimate all chosen \(\ell_i\) lie between \(d\) and \(O(d\log d)\).

Stirling's formula gives \(\log L_d=\log d-1+\log\kappa+o(1)\). Hence
\[
  \log U=d(\log d+\log\log d+\log2+1)+o(d),\qquad
  k=(1+o(1))\log d.
\]
The radical inequality yields \(\log(C/\operatorname{rad}(ABC))\ge (1+o(1))d\). In particular \(C\to\infty\). From \(\log C\le4\kappa d^2(\log d)^2\) and the eventual monotonicity of \(\sqrt x/\log x\), one obtains \(T(C)\le(\sqrt\kappa+o(1))d\) and \(\log\log C\le(2+o(1))\log d\). Thus every prime \(p\le cT(C)\) is in \(D\), and \(p^k\mid M\mid v\). These estimates give both inequalities in the statement on the same triples.

## What a fixed-power certificate would take here

For these same choices of modulus and primes, let \(z\ne0\) be any kernel vector and \(s=\#\{i:z_i\ne0\}\). The primes dividing \(J\) are exactly the \(\ell_i\) in that support. Uniformly over all such \(z\), the explicit certificate above therefore has
\[
 \log\!\left(\frac{M}{D\operatorname{rad}(|J|)}\right)
       =(d-s+o(d))\log d,\qquad
 \log C=(2+o(1))\|z\|_1\log d .
\]
The second equality follows by sandwiching \(S\) between \(|N(\alpha)|=\prod_i\ell_i^{|z_i|}\) and \(\exp(\sum_i w_i|z_i|)\); the odd norm implies \(g=1\). As \(M\mid a\ne0\), the inequality \(S\ge2M^2\) gives \(\|z\|_1\ge(2-o(1))d\). Thus this particular certificate would give a fixed-positive-power gain infinitely often **if and only if**, for some fixed \(K,\delta>0\), infinitely many of these lattices contain a nonzero \(z\) with \(\|z\|_1\le Kd\) and \(s\le(1-\delta)d\). The packing argument above does not establish this short, sparse relation. This equivalence is only about the displayed certificate and does not bound gains from uncounted prime powers.
