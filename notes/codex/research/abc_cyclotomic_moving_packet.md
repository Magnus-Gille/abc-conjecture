# Nearly quadratic repeated factors from one moving interval of primes

Fix \(n\ge3\), a nonempty open interval \(I\subset(0,1)\) and \(\delta>0\). For **every sufficiently large \(Y\)** there are coprime \(0<B<A\), \(B/A\in I\), with
\[
 \log A\asymp_{n,I,\delta}Y,\qquad
 \prod_{\substack{Y<p\le2Y\\p\equiv1\bmod n}}
                   p^{\,v_p(\Phi_n(A,B))-1} > A^{\,2-\delta}.
 \tag{1}
\]
Every prime in that progression and interval occurs; its exact order for \(B/A\bmod p\) is \(n\). Their valuations are bounded in terms of \(n,\delta\) alone and take at most two consecutive values on each pair. One can independently prescribe the root of order \(n\) at each prime. For \(n=9\), all the certified multiplicity is in \(A^6+A^3B^3+B^6\).

A fixed \(1+\varepsilon\) violation would require more than (1). Indeed the full radical \(R=\operatorname{rad}(AB(A^n-B^n))\) is at most \(A^{n+2}\) divided by this product. The product \(A^{2+n\varepsilon/(1+\varepsilon)}\) would ensure \(A^n>R^{1+\varepsilon}\) by itself. Conversely, assuming rational abc, the full repeated part is \(O_{n,\eta}(A^{2+\eta})\) for every \(\eta>0\), by applying abc to the power triple. Thus the coefficient two of \(\log A\) can be approached using only primes comparable to \(\log A\), even in any fixed interior interval of base ratios. The known construction at a fixed prime set has constants depending on that set; (1) explicitly relates the moving primes to the resulting height. [Fixed-prime theorem](abc_fixed_prime_power_approximation.md)

## A lattice transition at bounded depth

Write \(S=\{Y<p\le2Y:p\equiv1\bmod n\}\), \(\Pi=\prod_{p\in S}p\), and \(d=\varphi(n)\). All logarithms are natural. By the prime number theorem in a fixed arithmetic progression, \(\log\Pi\sim Y/d\), and \(|S|\ll_n Y/\log Y\). At each \(p\in S\), prescribe a primitive \(n\)-th root \(\alpha_p\in\mathbf Z_p\) by lifting a simple root from \(\mathbf F_p\). Fix an integer \(L\ge2\). For exponents \(k_p\ge L\) put
\[
 M=\prod_{p\in S}p^{k_p},\qquad
 \Lambda=\{(a,b)\in\mathbf Z^2:b-\alpha_p a\equiv0\bmod p^{k_p}
                                                  \text{ for all }p\in S\}.
\]
The determinant of \(\Lambda\) is \(M\). Start all exponents at \(L\), increment one at a time in successive full rounds, and finish at \((d-1)L\) full levels followed by one additional increment. Here the final exponents are \((d-1)L\) and \((d-1)L+1\); for \(d=2\) only one increment is needed. Choose a shortest nonzero vector in the maximum norm at each step.

Some successive shortest directions must differ. Otherwise let \((a,b)\) be their common **primitive integer** direction and \(h=\max(|a|,|b|)\). At the start Minkowski gives \(h\le \Pi^{L/2}\). At the last modulus \(M_f\), a vector \(g(a,b)\in\Lambda_f\) requires
\[
 |g|\ \ge\ M_f\big/\prod_{p\in S}p^{v_p(b-\alpha_p a)}
       \ \ge\ M_f/|\Phi_n(b,a)|.
\]
The polynomial on the right is a nonzero integer, since a primitive \(n\)-th root is not rational. Each local linear factor divides its value in \(\mathbf Z_p\), so the inequality also holds when one coordinate vanishes. As \(|\Phi_n(b,a)|\le(2h)^d\), the length on that line is at least \(2^{-d}M_f/h^{d-1}\). A shortest vector has length at most \(\sqrt{M_f}\), so this would give \(M_f\le 4^d\Pi^{(d-1)L}\). The final additional prime exceeds \(4^d\) for large \(Y\). This contradiction proves the transition, uniformly in \(L\) and in the chosen roots.

Use the earlier lattice at a transition and denote its determinant by \(M\). If the next step increments the prime \(q\), then \(q\Lambda\subseteq\Lambda_{\rm next}\). In the maximum norm its successive minima satisfy \(\lambda_2\le q\lambda_1\): the two shortest vectors at the transition are independent in \(\Lambda\). Minkowski's second theorem gives \(M/2\le\lambda_1\lambda_2\le M\). Thus
\[
      \sqrt{M/(2q)}\le\lambda_1\le\lambda_2\le\sqrt{qM},
          \qquad \Pi^L\le M\le\Pi^{(d-1)L}.
\]
There is a lattice basis of size at most \(2\lambda_2\) in this norm. A shortest vector \(v\) is primitive in the lattice. Complete it to a basis \(v,b\); an independent vector of length \(\lambda_2\) has form \(s v+t b\), \(t\ne0\). Dividing by \(t\) and rounding the coefficient of \(v\) supplies the asserted second basis vector.

## Enforcing positive coordinates, units and exact valuations

In this basis choose a translate of an integer coefficient box of side \(J=\lceil Y\rceil\) all of whose lattice points lie inside \(0<b<a,\ b/a\in I\) with \(a\ll_I J\lambda_2\). This is possible by centering the box on a ray strictly inside the interval, at a sufficiently large fixed multiple of \(J\lambda_2\) from the origin, and rounding the center to the lattice. The basis bound controls the displacement of every point of the box.

At each \(p\in S\) the two linear functions on \(\Lambda/p\Lambda\) are
\[
             a\bmod p,\qquad (b-\alpha_p a)/p^{k_p}\bmod p .
\]
Together they give an isomorphism to \(\mathbf F_p^2\). Indeed, their common kernel in \(\Lambda\) is \(p\Lambda\), since dividing both coordinates by \(p\) preserves all the other congruences. Discard the zeros of either function. Each excluded line modulo \(p\) takes at most \(J(J/p+1)\) points of our coefficient box, by solving for a coordinate with nonzero coefficient. The total fraction removed is at most \(2\sum_{p\in S}(1/p+1/J)=O_n(1/\log Y)\). Hence there is a remaining pair. Its gcd is prime to \(\Pi\); divide both coordinates by that gcd to obtain \(A,B\). The pair stays in \(\Lambda\), so the lower height bound is still \(\lambda_1\). Each local exponent is exactly \(k_p\), by simple-root factorization over \(\mathbf Z_p\), and \(\Phi_n(B,A)=\Phi_n(A,B)\).

The height estimates and the exact product now read
\[
 \log A=\tfrac12\log M+O_I(\log Y),\qquad
 \log\prod_{p\in S}p^{v_p(\Phi_n(A,B))-1}
                =\log M-\log\Pi=2\log A-\log\Pi+O_I(\log Y). \tag{2}
\]
Choose a fixed \(L\) with \(2/L<\delta\). Since \(\log M\ge L\log\Pi\), (2) proves (1). Varying the local roots gives at least \(d^{|S|}\) distinct primitive pairs for each \(Y\): reduction of \(B/A\) recovers each chosen root.

The construction is uniform in \(L\). For \(0<\gamma<1\), take \(L=\lceil Y^{1/\gamma-1}\rceil\). Then \(Y\asymp_n(\log A)^\gamma\) and the product is \(A^2\exp(-\Theta_n((\log A)^\gamma))\), since \(\log\Pi\sim Y/d\). Consequently its logarithm divided by \(\log A\) tends to two while all contributing primes tend to infinity and lie in a single interval at that sublogarithmic scale.
