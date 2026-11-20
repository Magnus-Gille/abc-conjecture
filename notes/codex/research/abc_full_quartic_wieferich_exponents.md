# A Wieferich condition at every composite perfect-power index

Suppose \(n>1\) is odd and composite and \(B_n\) is an \(\ell\)-th power for a prime \(\ell\), where \(B_n^2\) is the reduced denominator of \(X(nG)\) on \(E:Y^2=X^3-36X\), \(G=(-3,9)\). Then
\[
                         2^{\ell-1}\equiv1\pmod{\ell^2}.
\]
The same conclusion holds for every prime divisor of any perfect-power exponent at this index. By the prime-index restrictions, \(\ell>10^9\), \(\ell\equiv-1\pmod{48}\), and \(n=q^a\) for a prime \(q\equiv3\pmod4\) with \(a\ge2\). [Index classification](abc_full_quartic_prime_power_indices.md) · [Finite exponent bound](abc_congruent_six_exponent_trace_sieve.md)

The same index prime already satisfies \(q>220,000\) and \(48q\mid\ell+1\) even when the original index is prime. Indeed any prime \(h\mid B_q\) splits in the Gaussian integers. Its Frobenius \(\pi\) fixes the order-\(q\) point \(G\) and its Gaussian orbit, which is the entire \(E[q]\) because \(q\) is inert. It also fixes \(E[2]\). Thus \(\pi=1+2q(A+Bi)\) with \(B\ne0\) and \(h=N\pi\ge4q^2+1\). The earlier height estimate now gives \(\ell<(0.52q^2+1.5)/(2\log(2q))\). This increasing upper bound is below \(10^9\) at \(q=220,000\). Finally combine \(4q\mid\ell+1\), \(48\mid\ell+1\) and \(q>3\).

Every prime divisor of \(B_n\) is 1 modulo 12, whereas \(q\) is 3 modulo 4. Consequently in passing from \(B_q\) or \(B_{q^2}\) to \(B_n\), all valuations already present are unchanged. Both smaller denominators are therefore \(\ell\)-th powers. The trace descent gives \(\ell\mid a_q\), \(\ell\nmid B_q\) and \(\ell>2q\), where \(X(qG)=-3a_q^2/B_q^2\). In particular \(X(qG)\equiv0\pmod{\ell^2}\). [Prime-index descent](abc_full_quartic_perfect_power_census.md)

For odd indices define \(f_j=3^{-(j^2-1)/2}\psi_j(G)\), where \(\psi_j\) is the division polynomial on \(E\). Its absolute value is \(B_j\). The composition identity gives the exact equality
\[
             f_{q^2}/f_q^{q^2}=3^{-(q^2-1)/2}\psi_q(qG).
\]
The odd division polynomial is an integral polynomial in \(X\), so on the right one can replace \(qG\) with \((0,0)\) modulo \(\ell^2\). For \(y^2=x^3+A x\) and odd \(j\),
\[
              \psi_j(0,0)=(-1)^{(j-1)/2} A^{(j^2-1)/4}.
\]
Indeed \(\psi_1=1,\ \psi_3(0)=-A^2\); all even division polynomials vanish at \((0,0)\). In \(\psi_{2m+1}=\psi_{m+2}\psi_m^3-\psi_{m-1}\psi_{m+1}^3\) exactly the term involving only odd indices survives, giving this formula by induction. Inserting \(A=-36\) yields
\[
                f_{q^2}/f_q^{q^2}\equiv\pm2^{(q^2-1)/2}\pmod{\ell^2}.
\]
The left side is an \(\ell\)-th power in the unit group since both denominators are \(\ell\)-th powers and \(\ell\) is odd. Raising to \(\ell-1\) gives \((2^{\ell-1})^{(q^2-1)/2}\equiv1\pmod{\ell^2}\). Fermat's theorem puts \(2^{\ell-1}\) in the subgroup \(1+\ell\mathbf Z/\ell^2\mathbf Z\), which has order \(\ell\). Since \(q+1<\ell\), the exponent \((q^2-1)/2\) is coprime to \(\ell\). This proves the claimed congruence. The argument does not assert any distribution theorem for Wieferich primes. [Normalization proof](abc_gaussian_quartic_odd_cofactors.md)
