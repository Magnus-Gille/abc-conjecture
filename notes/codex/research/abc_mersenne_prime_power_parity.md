# An odd-multiplicity primitive divisor at every odd prime power in the Mersenne sequence

Let \(p\) be any odd prime and \(k\ge1\). At each order \(p^k\) and \(2p^k\), the Mersenne difference \(2^m-1\) has a prime of exact order \(m\) occurring to odd exponent, with the sole exception \(m=6\). The prime \(p\) and its exponent \(k\) may both vary. This conclusion follows from an elementary estimate for a square root.

## A gap between the value of a cyclotomic form and squares

Put \(p=2s+1\), \(F(t)=\sum_{j=0}^{2s}t^j\), and
\[
  c_j=\binom{2j}{j}/4^j,\qquad P(t)=\sum_{j=0}^s c_jt^j .
\]
The square of the full power series \(\sum_{j\ge0} c_jt^j=(1-t)^{-1/2}\) has all coefficients one. Consequently \(F-P^2\) has zero coefficients through degree \(s\); its coefficients from \(s+1\) to \(2s\) are positive and at most one. The first of these is \(2c_{s+1}\), at least \(2/(2s+3)\) since the central binomial coefficient dominates the mean in its row.

For any positive integers \(X,Y\) satisfying
\[
                         X>4^sY^{s+1}+Y ,
\]
neither \(\Phi_p(X,Y)\) nor \(\Phi_{2p}(X,Y)\) is a square. To see this take \(t=\pm Y/X\). The coefficient of \(t^{s+1}\) in \(F-P^2\) dominates its higher terms in absolute value: their contribution after dividing by \(|t|^{s+1}\) is at most \(Y/(X-Y)<4^{-s}<2/(2s+3)\). Thus \(F(t)\ne P(t)^2\). Moreover \(|t|<1/4\), \(F(t)\ge1-|t|\), and \(P(t)\ge1-|t|/2\) by the alternating series bound for negative \(t\), with both inequalities immediate at positive \(t\). This gives
\[
  0< \left|X^s\sqrt{F(t)}-X^sP(t)\right|
      \le X^s\frac{|t|^{s+1}}{1-|t|}
      =\frac{Y^{s+1}}{X-Y}<4^{-s}.
\]
Here \(\sqrt{F(t)}+P(t)>1\). The rational \(X^sP(t)\) belongs to \(4^{-s}\mathbf Z\). Since any integer is in the same lattice, the strictly positive distance displayed is too small for \(X^s\sqrt{F(t)}\) to be integral. Its square is exactly the corresponding cyclotomic value.

In particular, for **every** integer \(A\ge2\), prime \(p\ge3\), and \(k\ge2\), the values \(\Phi_{p^k}(A,1)\) and \(\Phi_{2p^k}(A,1)\) are nonsquares: substitute \(X=A^{p^{k-1}}\ge2^p=2\cdot4^s,\ Y=1\). The values are odd. Any prime factor other than \(p\) gives the exact order, by separability. The prime \(p\) divides the first form only when \(A\equiv1\bmod p\), and the second only when \(A\equiv-1\bmod p\), by reducing \(\Phi_p(X,\pm1)\) modulo \(p\). Thus each nonsquare supplies an odd-valuation primitive divisor except possibly in its stated congruence class. For a fixed \(A\), only finitely many primes divide \(A^2-1\). Applying the smooth-order theorem to those primes and 2 proves that at most finitely many \(p^k,2p^k\) with \(k\ge2\) fail to have such a divisor. [All-heights smooth-order theorem](abc_cyclotomic_smooth_order_parity.md)

## Completing the base-two classification

At \(k=1\) the two forms are \(2^p-1\equiv7\bmod8\) and \((2^p+1)/3\equiv3\bmod8\). Neither is a square. At \(k\ge2\) use the square-root estimate. In the first form \(p\nmid2-1\), so a prime of odd valuation gives the required order for every \(p,k\). In the second, the only possible obstruction is \(p=3\) since \(p\mid2+1\) is necessary. For \(k=1\) one has \(\Phi_6(2,1)=3\), and \(2^6-1=3^2\cdot7\) has no prime of order six. For \(k\ge2\), the explicit classification at all orders \(2\cdot3^k\) excludes both squares and three times squares and supplies the required prime. [Explicit order theorem](abc_cyclotomic_odd_primitive_grid.md)
