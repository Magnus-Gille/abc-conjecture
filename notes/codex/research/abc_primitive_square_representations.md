# Simultaneous radical savings in every primitive square representation

Fix \(k\ge1\) distinct primes \(p_i\equiv1\bmod4\) and let \(P=\prod_i p_i\). There are arbitrarily large \(u\) with \(\operatorname{rad}(u)=P\) for which **every** primitive representation \(v^2+w^2=u^2\), with \(0<v<w\), satisfies
\[
 v\le u/2,\qquad
 \frac{u^2}{\operatorname{rad}(uvw)}
 \ge \frac{\log(u^2)}{64kP\log P}.
\]
There are exactly \(2^{k-1}\) such representations at each constructed height. All the smaller legs at a given height are divisible by the same specified power of 3, and those powers tend to infinity. Since the radical of \(v^2w^2u^2\) is \(\operatorname{rad}(uvw)\), these are primitive abc triples with all three terms squares.

## Construction

Write \(p_i=\pi_i\bar\pi_i\) in \(\mathbb Z[i]\), and set \(\alpha_i=\pi_i/\bar\pi_i\). In \(\mathbb F_9=\mathbb Z[i]/(3)\) this ratio lies in the norm-one subgroup, of order 4. For \(t\ge1\), put \(e=4\cdot3^{t-1}\). Binomial expansion, or induction on \(t\), gives \(\alpha_i^e\equiv1\bmod3^t\), using the localization at 3 to take the ratio.

For each \(i\), choose an integer \(1\le l_i\le16k\) for which the principal angle of \(\alpha_i^{e l_i}\) has absolute value at most \(2\pi/(16k)\). Pigeonholing the \(16k+1\) multiples of the angle of \(\alpha_i^e\) in \(16k\) equal arcs proves existence. Let \(u=\prod_i p_i^{e l_i}\). For every choice of signs \(\sigma_i=\pm1\),
\[
 Z_\sigma=u\prod_i\alpha_i^{\sigma_i e l_i}
\]
is a Gaussian integer of norm \(u^2\). At each split prime its factorization chooses exactly one of \(\pi_i,\bar\pi_i\), to exponent \(2e l_i\). Hence its real and imaginary parts are coprime. Conversely every primitive Gaussian integer of norm \(u^2\) has that form up to multiplication by a unit. Unique factorization identifies unordered positive pairs precisely under simultaneous reversal of all signs. Neither leg can be zero, since then the Gaussian integer would have both primes above each \(p_i\) as divisors.

The sum of the chosen signed angles has absolute value at most \(\pi/8\), so \(v=|\operatorname{Im}Z_\sigma|<u/2\) is the smaller leg in every case. Also \(Z_\sigma\equiv u\bmod3^t\), hence \(3^t\mid v\). With \(w=\operatorname{Re}Z_\sigma\),
\[
 \operatorname{rad}(uvw)\le P\,vw/3^{t-1}
 \le P u^2/(2\cdot3^{t-1}).
\]
Finally \(\log(u^2)\le2e(16k)\log P=128k\,3^{t-1}\log P\), proving the assertion. The height tends to infinity because \(u\ge P^e\).

## How much the prescribed primes can supply

For fixed \(P\), any fixed finite set of primes \(S\) accounts for at most \(O_{P,S}(\log u)\) of the factor \(vw/\operatorname{rad}(vw)\) along this construction. To verify this write \(\beta=\prod_i\alpha_i^{\sigma_i l_i}\). It ranges over a fixed finite set of non-roots of unity, by factorization. The equality
\[
 vw=\left|\frac{u^2}{4i}\,\beta^{-2e}(\beta^{4e}-1)\right|
\]
expresses the integer in absolute value (the sign depends on the angle). At a Gaussian prime over \(p\nmid P\), the other factors apart from 4 are units. For \(\eta=\beta^{16}\) one has \(\beta^{4e}=\eta^{3^{t-1}}\). If \(p\ne3\), the valuation of \(\eta^{3^j}-1\), once positive, stays constant: the cofactor at the next step reduces to 3. At the inert prime 3 the valuation starts positive and grows by exactly one at each step, since \((1+h)^2+(1+h)+1=3+3h+h^2\) has valuation 1 for \(3\mid h\). No prime of \(P\) divides either leg. Thus the contribution from primes of \(S\) other than 3 is bounded, and the contribution from 3 is \(O_P(3^t)=O_P(\log u)\). The lower bound construction guarantees logarithmic savings. Any fixed-power abc violation here would also require a much larger contribution from other sources.

## Prescribing a different prime to each representation

For any fixed \(n\ge2\), there are also arbitrarily large square heights with at least \(n/2\) distinct primitive square representations having smaller leg at most \(u/2\), all with savings tending to infinity, each certified by a prime absent from every other representation in the collection. In this construction the guaranteed saving is a power of \(\log u\) whose exponent is allowed to depend on \(n\).

Choose distinct primes \(q_1,\ldots,q_n\equiv1\bmod32\). In \(\mathbb Z[i]/q_h\simeq\mathbb F_{q_h}\times\mathbb F_{q_h}\) choose \(g_h\) of order 32 in the norm-one group. Construct \(\gamma_j=a_j+b_ji\) for \(0\le j\le n\) with \(b_0=1\) and \(b_j=\prod_{h\ne j}q_h\) for \(j>0\). For \(\alpha_j=\gamma_j/\bar\gamma_j\) require \(\alpha_0\equiv\alpha_h\equiv g_h\bmod q_h\) and \(\alpha_j\equiv1\) there when \(j\notin\{0,h\}\).

These choices are possible by elementary congruences. At an active \(q_h\), write \(g_h=(g,g^{-1})\) with \(g\ne1\), choose a root \(s^2=-1\) modulo \(q_h\) corresponding to the first factor, and solve \((a_j+s b_j)/(a_j-s b_j)=g\) uniquely. Both numerator and denominator are units. At inactive primes set \(a_j\equiv1\bmod b_j\). Choose even \(a_j\), divisible by all earlier norms \(A_m=a_m^2+b_m^2\). These moduli are compatible since the earlier norms are odd and coprime to all \(q_h\). The Chinese remainder theorem permits \(a_j\) arbitrarily large, giving pairwise coprime odd norms \(A_j>1\). Each \(\gamma_j\) is coprime to its conjugate, since \(\gcd(a_j,b_j)=1\) and its norm is odd.

Let \(A=\prod_{j=0}^n A_j,\ E=(\prod_{h=1}^n q_h)^t\), and \(\beta_h=(\prod_{j=0}^n\alpha_j)\alpha_h^{-2}\). For \(l=1,2\), at the common denominator \(u=A^{lE}\) each \(Z_h=u\beta_h^{lE}\) is a primitive Gaussian integer of norm \(u^2\). Factorization on the disjoint supports of the \(\gamma_j\) distinguishes the \(n\) rows even up to conjugation and units. At \(q_h\), \(\beta_h\equiv1\), so \(q_h^{t+1}\mid\operatorname{Im}Z_h\) by lifting. At every other \(q_i\), its residue is \(g_i^2\), whose order is 16. Raising to \(lE\) leaves order at least 8. A norm-one residue with a zero real or imaginary coordinate has order at most 4. Thus \(q_i\) divides neither leg of row \(h\), and none of the \(q_i\) divides \(u\).

For each row, either the angle of \(\beta_h^E\) or twice that angle is within \(\pi/6\) of a multiple of \(\pi/2\). Indeed, if its first distance is in \((\pi/6,\pi/4]\), the second is at most \(\pi/6\). At least half of the rows therefore give a smaller leg at most \(u/2\) for a common \(l\). Each retained row satisfies \(u^2/\operatorname{rad}(uvw)\ge 2q_h^t/\operatorname{rad}(A)\), because whichever leg contains \(q_h^{t+1}\) contributes the saving. Since \(\log u=lE\log A\), all these lower bounds diverge with \(t\). They do not give a fixed positive power of \(u\).
