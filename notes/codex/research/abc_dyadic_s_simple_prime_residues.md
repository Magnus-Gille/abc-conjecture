# Prime divisors occurring exactly once in the shifted dyadic factor

Put \(R=(-8,16)\) on \(E':y^2=x^3+16x^2+32x\). For \(n=2^k\), \(k\ge3\), let \(M=2^{k-1}\), \(x([M]R)=u_n^2/v_n^2\) in lowest terms and \(s_n=u_n^2+8v_n^2\). Call a prime simple in \(s_n\) if its valuation is exactly one. Write \(P_1(s)=\prod_{p\parallel s}p\).

* The lower natural density of indices \(k\) with a simple prime in \(s_{2^k}\) is greater than **0.9015**.
* On a set of lower density greater than **0.09**, fourteen specified distinct primes are simultaneously simple, with product greater than \(2^{234}\).
* The lower mean of \(\log_2 P_1(s_{2^k})\) over the indices is greater than **153.45**. One arithmetic progression makes 1,113 specified primes simultaneously simple, with product exceeding \(2^{22079}\).

The finite certificate uses ordinary integer and modular arithmetic. These bounds concern density among the exponents \(k\), with equal weight per index. [Certificate rows](abc_dyadic_s_simple_prime_residues.csv) · [Python verifier](abc_dyadic_s_simple_prime_residues.py)

## Two periods for one prime

Let \(p>5\) be good, with odd reduction order \(r\) of \(R\), prime to \(p\). Suppose the formal depth of \([r]R\) is one. For any odd modulus \(d\), use the order of 2 in \((\mathbb Z/d\mathbb Z)^\times/\{1,-1\}\), namely the least positive \(j\) such that \(2^j\equiv\pm1\bmod d\). Denote this order by \(h\) at \(d=r\) and \(H\) at \(d=rp\). Then, with \(m=k-1\),
\[
 p\parallel s_{2^k}\quad\Longleftrightarrow\quad h\mid m\text{ and } H\nmid m.             \tag{1}
\]
Indeed \(p\mid s_n\) means \([2^m]R\) reduces to one of \(\pm R\), with the sign \(e\) determined by \(2^m\equiv e\bmod r\). At those points the ordinate is \(\pm16\), a unit. Thus \(x-x(R)\) measures the formal depth of the difference. The denominator \(v_n\) is a unit there. The formal logarithm on \(p\mathbb Z_p\) gives \(v_p(s_n)=1+v_p((2^m-e)/r)\). A contribution greater than one requires the *same* sign modulo \(r\) and \(p\). This proves (1).

The verifier checks primes, exact reduction orders, first depths one, and both exact periods for all 1,344 rows. For the rank it verifies \((r-1)R=-R\bmod p\) and finite affine multiples \((r/\ell)R\) for all prime divisors \(\ell\mid r\); at modulus \(p^2\) the first equality fails. Its affine operations have unit denominators throughout. Every residue-order candidate is checked against all its prime divisors. Among the witnesses, the row \((p,r,h,H)=(14149753,131073,17,20045482)\) was found by looking for a split CM Frobenius with norm \(p\). Its check uses only (1).

All 476 different \(h\) in the certificate are prime. For a fixed \(h\) write \(L_h=\operatorname{lcm}_{p:h_p=h}H_p\). If \(h\mid m\) but there is no simple prime from the table, then \(L_h\mid m\). In the \(h=2\) case \(L_2=140\) forces also \(5\mid m\), so such a missed index is divisible by \(\operatorname{lcm}(L_2,L_5)\). Write \(D_2\) for that lcm and \(D_h=L_h\) for every other \(h\). The Chinese remainder theorem and a union bound give the lower density
\[
 1-\prod_h(1-1/h)-\sum_h 1/D_h >0.90150214 .
\]
For example the rows at \(h=11\) give all fourteen primes simultaneously for \(11\mid m\) outside \(\bigcup_{p:h_p=11} H_p\mathbb N\). For the larger simultaneous result take \(m\equiv\prod_hh\bmod\operatorname{lcm}_pH_p\). Finally, the mean contribution of a certified prime to the base-two logarithm is exactly \((1/h-1/H)\log_2 p\). The program uses the rational lower bound \(\lfloor\log_2(p^{256})\rfloor/256\) to check the sum.

Every *fixed* finite list of primes misses a positive-density progression. At 2 the integers \(s_n\) are odd, and at a prime of even reduction order that order cannot divide either odd integer \(2^m\pm1\). At each remaining good odd prime, of odd order \(r\), choose \(m\) divisible by \(\varphi(rp^2)\). Then \(rp^2\mid 2^m-1\), so the formal depth is at least two. The single common progression is obtained by taking the lcm of these fixed moduli. It allows simple primes outside the chosen list.

## Transferring simple prime factors from prime-index denominators

Write \(m=k-1\), \(A_m=2^{2m}-1\) and let \(r\) run through the distinct prime divisors of \(A_m\). At an odd prime index \(r\) let \(B_r\) denote the positive square root of the reduced abscissa denominator of \([r]R\). Put \(E_r=\log(B_r/\operatorname{rad}B_r)\). The following inequality is unconditional:
\[
 \log P_1(s_{2^{m+1}})+2\sum_{r\mid A_m}E_r
 \ \ge\ \widehat h(R)\sum_{r\mid A_m}r^2-O(m).                                      \tag{2}
\]
Here every sum indexed by \(r\mid A_m\) is over primes. Since \(R\) is integral, every prime dividing \(B_r\) has reduction order exactly \(r\), so the different \(B_r\) are pairwise coprime. They are odd on this orbit. For each \(r\) there is a unique sign \(e\) with \(r\mid2^m-e\). If \(p\parallel B_r\), the local parameter computation above gives
\[
 v_p(s_{2^{m+1}})=1+v_p\big((2^m-e)/r\big).
\]
The exceptions to simplicity therefore all divide \(A_m\). At all odd indices \(\log B_r=\widehat h(R)r^2+O(\log(2r))\). The logarithm of the product of simple primes in any positive integer \(B\) is at least \(\log B-2\log(B/\operatorname{rad}B)\), term by term. Summing and subtracting at most \(\log A_m\) for the lost primes proves (2), since \(\sum_{r\mid A_m}\log r\le\log A_m=O(m)\). Equivalently \(s_{2^{m+1}}=B_{2^m-1}B_{2^m+1}\) with its two factors coprime. [Odd-index denominator estimates and octic comparison](abc_octic_mixed_cm_prime_mass.md) · [Exact shifted-denominator identity](abc_dyadic_shifted_rank_mass.md)

Suppose only that
\[
 E_r=o(r^2)\quad\text{as }r\text{ runs through the odd primes}.                       \tag{3}
\]
Rational abc would imply (3) by the octic height comparison. A failure of (3) would give infinitely many prime-index octic triples whose qualities exceed \(1+\delta\) for some fixed \(\delta>0\). For all sufficiently large \(m\), Bang–Zsigmondy gives a prime of \(A_m\) of multiplicative order exactly \(2m\), so \(\sum r^2\ge(2m+1)^2\). In particular (2) and (3) imply the pointwise bound
\[
 \log P_1(s_{2^{m+1}})\ \ge\ (\widehat h(R)-o(1))\sum_{r\mid A_m}r^2
 \ \gg\ m^2.                                                                         \tag{4}
\]
The \(o(1)\) is uniform in \(m\), since the finitely many small \(r\) contribute a bounded amount for each fixed cutoff. Stewart proves a stronger largest-prime-factor estimate for the fixed Lucas sequence \(2^j-1\). At \(j=2m\), (4) is at least a constant times \(m^2\exp\{2\log(2m)/(104\log\log(2m))\}\) for all sufficiently large \(m\). The natural height is \(\log s_{2^{m+1}}\asymp4^m\). [Stewart, *On divisors of Lucas and Lehmer numbers*](https://arxiv.org/abs/1008.1274)

In fact every lower bound below that uses only \(\log P_1(B_r)\gg r^2\) holds under the weaker hypothesis \(\limsup_{r\ {\rm prime}}q_r<16/15\), where \(q_r\) is the quality of the octic triple at prime rank \(r\). In this case the coefficient \(\widehat h(R)-o(1)\) in (4) is replaced by some fixed positive constant. Conversely, if the ratio of \(\log P_1(s_{2^{m+1}})\) to \(\sum_{r\mid A_m}r^2\) has lower limit zero, then
\[
  \limsup_{r\ {\rm prime}}q_r\ \ge\ \frac{16}{15}.                                  \tag{6}
\]
Indeed (2) forces \(\limsup E_r/\log B_r\ge1/2\) in this case. For the octic parameters \((s,t)\) at rank \(r\) one has \(B_r=\sqrt{s^2+2t^2}\asymp\max(|s|,|t|)\) and \(c_r=(s^4+4t^4)^2\), hence \(\log c_r=8\log B_r+O(1)\). The octic height comparison gives \(\log(c_r/\operatorname{rad}(a_rb_rc_r))\ge E_r-O(1)\). These imply (6). Conversely any upper quality bound strictly less than \(16/15\) gives \(E_r\le(1/2-\eta)\log B_r\) for some fixed \(\eta>0\) and all sufficiently large prime \(r\). This gives the positive simple-prime mass needed in (4) and (5). [Octic quality comparison](abc_octic_mixed_quality_dichotomy.md)

## How many distinct primes survive

Let \(N(m)\) count all primes \(p\parallel s_{2^{m+1}}\), let \(\tau(m)\) be the number of positive divisors of \(m\), and let \(m_{\rm odd}=m/2^{v_2(m)}\). Under the same prime-index hypothesis (3) one has both
\[
 \begin{split}
 N(m)&\ge \tfrac12\tau(m)-O(1)\qquad\text{for every }m\ge 2,\\
 \sup_{X\ge2}\frac1X\sum_{2\le m\le X}
      \big(\tau(m)+\tau(m_{\rm odd})-N(m)\big)_+ &<\infty.                             \tag{5}
 \end{split}
\]
In particular \(N(m)\ge(1-o(1))(\tau(m)+\tau(m_{\rm odd}))\) in natural density, in the sense that the relative shortfall converges to zero in density. This uses the elementary normal-order fact that \(\tau(m)\) tends to infinity in density.

For every sufficiently large integer \(d\), choose a prime \(r\) with \(\operatorname{ord}_r2=2d\). For every sufficiently large odd \(d\) choose a second prime \(r'\) with \(\operatorname{ord}_{r'}2=d\). Such primes exist by Bang–Zsigmondy and are distinct throughout both families by their ordinary orders. Both kinds have order \(d\) modulo signs. The primes simple in \(B_r\) have total logarithm \(\ge\log B_r-2E_r\gg r^2\) by (3). If \(d\mid m\), each chosen \(r\) divides \(A_m\). In the first family every divisor \(d\ge\sqrt m\) gives \(r>2d\). If every simple prime of \(B_r\) loses simplicity in \(s_{2^{m+1}}\), all those primes divide \(A_m\), consuming at least a constant times \(r^2\ge4m\) in its logarithm. The prime sets at different ranks are disjoint. Since \(\log A_m=O(m)\), this can happen for at most a bounded number of these divisors \(d\). At least half the divisors of \(m\) are \(\ge\sqrt m\). This proves the first inequality.

For the second inequality we choose one witness \(p\parallel B_r\) per chosen rank, with its second period \(H\) large. For \(r\) sufficiently large the prime \(p\) is good and \(p\ne r\). Indeed for \(p\ge7\) the curve has an even number of points mod \(p\) by its rational two-torsion, and fewer than \(2p\) by Hasse. The second period is defined as in (1) and is divisible by \(d\). The logarithms of all distinct such \(p\) with \(H\le Y\) sum to at most
\[
 \log\prod_{1\le j\le Y/d}(2^{2dj}-1)\ll Y^2/d+Y.
\]
For a fixed sufficiently small constant \(c>0\), choose \(Y=cr\sqrt d\). The right hand side is smaller than the simple-prime logarithm \(\gg r^2\) in \(B_r\). Some witness thus has \(H\gg r\sqrt d\gg d^{3/2}\). By (1) it contributes to \(N(m)\) whenever \(d\mid m\) and \(H\nmid m\). All selected witnesses are distinct by their reduction orders. The small omitted divisors cost a fixed constant. The rest of the average shortfall is at most the sum of \(1/H\) over all witnesses, which converges by comparison with \(2\sum_{d\ge1}d^{-3/2}\). This proves (5).
