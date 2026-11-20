# Quadratic reciprocity and odd prime divisors at every divisor rank

Let \(G=(-3,9)\) on \(E:Y^2=X^3-36X\). For positive odd \(j\), write \(X(jG)=-3a_j^2/B_j^2\) in lowest terms, with \(a_j,B_j>0\). Extend \(B_{-j}=B_j\). Every prime divisor of \(B_j\) is \(1\bmod12\). For such a prime \(p\), let \(r_p\) be the order of \(G\) modulo \(p\), and let \(e_p=v_p(B_{r_p})\). The formal group gives \(v_p(B_j)=e_p+v_p(j/r_p)\) if \(r_p\mid j\), and zero otherwise. Since \(G\) is integral and \(E[2]\) is rational, the odd order \(r_p\) satisfies \(r_p>1\) and \(4r_p\mid\#E(\mathbf F_p)\). In particular \(p\ge(2\sqrt{r_p}-1)^2>r_p\). We use the established classification that \(B_j\) is nonsquare for every positive odd \(j>1\). [Orbit and valuations](abc_full_quartic_signature.md) · [Square classification](abc_full_quartic_square_classification.md)

**Theorem.** Fix any reduced residue class \(c\bmod M\). There are effectively constructible, arbitrarily long chains of squarefree odd indices \(N_k=s_1\cdots s_k\), with increasing primes \(s_i\equiv c\bmod M\), such that for each nontrivial divisor \(d\mid N_k\) there is a prime \(p_d\nmid M N_k\) of exact order \(r_{p_d}=d\), with \(v_{p_d}(B_d)=v_{p_d}(B_{N_k})\) odd. All previously chosen witnesses persist. Thus
\[
 \omega(\operatorname{sf} B_{N_k})\ge 2^k-1,\qquad
 \operatorname{sf} B_{N_k}\ge\prod_{1<d\mid N_k}(2\sqrt d-1)^2>N_k^{2^{k-1}}.
\]
Here \(\operatorname{sf}\) is the product of the primes of odd valuation. The construction also prescribes \(s_i\equiv1\bmod 2N_{i-1}\).

## Two local character formulas

Set \(W_j=\psi_j(G)\), where \(\psi_j\) is the signed division polynomial. At odd positive \(j\),
\[
 W_j=3^{(j^2-1)/2}f_j,\qquad f_j=(-1)^{(j-1)/2} B_j .
\]
Indeed the scaling from \((-1,\sqrt3)\) on \(y^2=x^3-4x\) gives the first equality, the normalized recurrence has \(f_j\equiv(-1)^{(j-1)/2}\bmod3\), and \(|f_j|=B_j\equiv1\bmod3\). [Normalization, signs and prime support](abc_gaussian_quartic_odd_cofactors.md)

For positive odd \(m,t\), set \(D=(t^2-1)/2\). Composition \(W_{mt}=\psi_t(mG)W_m^{t^2}\) gives
\[
 f_{mt}/f_m=3^{-D}\psi_t(mG) f_m^{2D}.
\]
The odd division polynomial for \(t\) is an integer polynomial in the abscissa, with leading term \(t X^D\). Substitution of \(X(mG)=-3a_m^2/B_m^2\) and multiplication by \(f_m^{2D}=B_m^{2D}\) makes every term below the leading one divisible by \(B_m^2\) in \(\mathbf Z[1/3]\). Since \(D\) is even and \(3\nmid B_m\), restoring the explicit sign gives the integer congruence
\[
 \frac{B_{mt}}{B_m}\equiv (-1)^{(t-1)/2}\,t\,a_m^{t^2-1}
                   \pmod{B_m^2}.                                      \tag{1}
\]
Consequently for every \(p\mid B_m\), including when \(p\mid t\),
\[
 \left(\frac{B_{mt}/B_m}{p}\right)=\left(\frac{t}{p}\right).          \tag{2}
\]
In the zero case, formal lifting gives \(v_p(B_{mt}/B_m)=v_p(t)\).

For positive odd \(d\) and \(p\mid B_d\), the sequence \(j\mapsto(B_j/p)\) on odd indices is even and has period \(2d\). Indeed the standard division-polynomial abscissa identity gives, for \(\phi_j(G)=X(jG)W_j^2\),
\[
 W_{j+2d} W_j=\phi_d(G)W_{j+d}^2-\phi_{j+d}(G)W_d^2.
\]
Here \(p\mid W_d\), whereas \(\phi_d(G)=-3a_d^2\,3^{d^2-1}\) is a nonzero square modulo \(p\), since \(p\equiv1\bmod12\). If \(p\nmid W_j\), then \(p\nmid W_{j+d}\) because \(r_p\mid d\) and \(r_p\nmid j\). Taking quadratic characters gives equality at \(j\) and \(j+2d\). If \(r_p\mid j\), both symbols vanish. At all odd \(j\), switching from \(W_j\) to \(B_j\) preserves the character as both the sign and the scaling factor are squares modulo \(p\). This argument allows \(j+d\) even. [Abscissa difference identity](abc_gaussian_odd_square_sieve.md)

As a separate geometric verification, on the isogenous model \(E_0:y^2=x^3+36x^2+36x\) the point \(P=(-2,8)\) maps to \(G+(6,0)\). Thus \([2d]P\) reduces to the identity or \((0,0)\). Translation by \((0,0)\) sends \(x\) to \(36/x\). At odd \(j\), \(x(jP)=-2u^2\), so the quotient of \(6-36/x\) by \(6-x\) is \(3/u^2\), a square modulo \(p\). The signs at the identity and at \(x=0\) both equal \(+1\). This also proves the \(2d\) period from the local character formula for \(8(6-x)\). [Local character formula](abc_full_quartic_square_denominators.md)

## A Jacobi identity for coprime indices

For coprime positive odd \(u,v\),
\[
                         \left(\frac{B_u}{B_v}\right)=1.                \tag{3}
\]
The supports are disjoint by the reduction orders. Both denominators are \(1\bmod4\), so rational quadratic reciprocity makes the symbol symmetric in \(u,v\). The period and evenness just proved allow one to replace \(u\) by the absolute value of its least absolute residue modulo \(2v\). If \(v>1\), that residue is odd, positive after taking the absolute value, and strictly smaller than \(v\) by coprimality. Interchanging \(u,v\) and descending ends at \(B_1=1\).

In particular, let \(q,s\) be distinct odd primes and put \(C_{qs}=B_{qs}/(B_qB_s)\). For \(s\nmid B_q\) and \(q\nmid B_s\), (2) and (3) give
\[
 \left(\frac{C_{qs}}{B_q}\right)=\left(\frac{B_q}{s}\right),\qquad
 \left(\frac{C_{qs}}{B_s}\right)=\left(\frac{B_s}{q}\right).
\]
A negative value of either character certifies an odd-exponent prime of exact order \(qs\), by the valuation computation below. For every fixed \(q\), the first character is negative at exactly half of primes \(s\) in natural relative density, since \(B_q\) is nonsquare. Only finitely many primes need exclusion. The same relative density holds in every reduced progression of modulus coprime to the squarefree kernel of \(B_q\).

## Density of detectable multipliers at a fixed prefix

Suppose the odd prefix \(m\) has distinct prime divisors \(s_1,\ldots,s_h\). For a prime multiplier \(q\nmid B_m\), if \((B_{s_i}/q)=-1\) at any \(i\), reciprocity shows that some \(p\mid B_{s_i}\) has \((q/p)=-1\). Formula (2) forces \(B_{mq}/B_m\) to be nonsquare. Each prime in this quotient is new because \(q\nmid B_m\). The quadratic characters \((B_{s_i}/\,\cdot\,)\) are independent because the \(B_{s_i}\) are nonsquares on disjoint prime supports. Therefore these tests together detect a new odd-valuation prime of \(B_{mq}\) for a set of prime multipliers of relative natural density exactly \(1-2^{-h}\). The same class fraction applies to every prefix divisible by \(s_1\cdots s_h\), with the exceptions \(q\mid B_m\) removed for each prefix. This refers to all prime multipliers, or equivalently the reduced classes modulo the product of the squarefree kernels. A fixed descending prefix restricts \(q\) to a finite interval. In that interval \(q\nmid B_m\) follows automatically from \(p>r_p\), since every odd prime rank dividing \(m\), or prime factor of a composite rank dividing \(m\), is at least \(q\). Each newly occurring rank is divisible by \(q\), so the witness is larger than \(q\) and survives all subsequent multipliers at most \(q\).

## Proof of the theorem

For odd squarefree \(n>1\) introduce the integer
\[
 C_n=\prod_{b\mid n} B_b^{\mu(n/b)}.
\]
To verify integrality and identify the possible surplus primes, fix \(p\mid B_n\) with \(r=r_p\mid n\). Write \(h=n/r\). The exponent of \(p\) is
\[
 \sum_{a\mid h}\mu(h/a)\bigl(e_p+v_p(a)\bigr)
 =
 \begin{cases}
 e_p & h=1,\\
 1 & h=p,\\
 0 & \text{otherwise}.
 \end{cases}
\]
Here \(h\) is squarefree, and the convolution of \(v_p\) with \(\mu\) on squarefree integers is supported at \(p\) with value one. A prime outside \(B_n\) occurs in none of the factors defining \(C_n\). Thus the only possible primes in \(C_n\) beyond the exact-order primes are index primes \(p\mid n\) with \(r_p=n/p\).

Choose \(s_1>\max(5,M)\) in the required reduced class. Since \(B_{s_1}\) is nonsquare, it has an odd-valuation prime \(p_{s_1}\), necessarily of order \(s_1\) and larger than \(s_1\). Inductively let \(N=s_1\cdots s_k\). For each \(1<d\mid N\), the selected \(p_d\) are distinct and coprime to \(2MN\). Choose a prime \(s>\max(M,N,B_N)\) such that
\[
 s\equiv c\pmod M,\qquad s\equiv1\pmod{2N},\qquad
 \left(\frac{s}{p_d}\right)=-1\quad(1<d\mid N).
\]
The first two conditions agree at their possible common factor 2. Each other condition may be imposed by one nonzero residue at a new prime. The Chinese remainder theorem and Dirichlet's theorem supply infinitely many \(s\), and a direct search terminates.

For fixed \(1<d\mid N\), Möbius inversion gives
\[
 C_{ds}=\prod_{e\mid d}(B_{es}/B_e)^{\mu(d/e)}.
\]
For \(e<d\), neither \(B_e\) nor \(B_{es}\) is divisible by \(p_d\): its order is \(d\), and \(s\) is prime to \(d\). Since \(es\equiv e\bmod 2d\), the period formula makes the character of each quotient at \(p_d\) equal to \(+1\). The \(e=d\) factor is a unit with character \((s/p_d)=-1\) by (2). Thus \(C_{ds}\) is an integer with character \(-1\) at \(p_d\).

Every prime dividing \(C_{ds}\) has exact order \(ds\). Indeed, the only other possibilities are \(\ell\mid ds\) of order \(ds/\ell\). The possibility \(\ell=s\) would require \(s\mid B_d\mid B_N\). For \(\ell\mid d\), that order is at least \(s>\ell\), contradicting \(\ell>r_\ell\). This proves that \(C_{ds}\) contains an odd-valuation prime \(p_{ds}\) of exact order \(ds\). Its character at \(p_d\) can also be required negative by selecting a prime contributing to the negative product. For \(d=1\), the square classification gives \(p_s\). The new primes exceed \(s\), so are coprime to \(MNs\). The old selected primes divide \(B_N<s\) and are different from \(s\), so their valuations persist. This proves the induction.

Finally the selected primes have pairwise different orders. Their product is at least the product of the Hasse lower bounds stated above. Since the product of all divisors of a squarefree \(N_k\) is \(N_k^{2^{k-1}}\), the asserted bound follows. When all chosen index primes are \(3\bmod4\), the Gaussian annihilator of a point of order \(d\mid N_k\) is precisely \((d)\), forcing \(E[d]\subset E(\mathbf F_{p_d})\) and \(4d^2\mid\#E(\mathbf F_{p_d})\). One then has \(p_d\ge(2d-1)^2>d^2\) and \(\operatorname{sf} B_{N_k}>N_k^{2^k}\). [Gaussian annihilator](abc_full_quartic_signature.md)

## Direct finite check

The first possible squarefree odd index with three distinct prime factors, \(N=105\), already has an odd prime at every nontrivial divisor rank. Here \(f_j\) is the signed sequence above. Each \(f_d\bmod p^2\) is a nonzero multiple of \(p\). The last column lists \(f_{d/\ell}\bmod p\) for prime \(\ell\mid d\) in ascending order, verifying exact rank. Since no listed \(p\) divides \(105\), the odd valuation persists.

| \(d\) | \(p\) | \(f_d\bmod p^2\) | \(f_{d/\ell}\bmod p\) |
|---:|---:|---:|---|
| 3 | 37 | 1332 | 1 |
| 5 | 13 | 13 | 1 |
| 7 | 14281 | 33717441 | 1 |
| 15 | 157 | 11618 | 67, 120 |
| 21 | 15877 | 244061244 | 5118, 15840 |
| 35 | 4789 | 10430442 | 756, 2261 |
| 105 | 44101 | 379003994 | 4772, 11962, 14817 |

The entries follow from \(f_1=f_2=1,\ f_3=-37,\ f_4=-70\) and the division recurrences. With \(A=f_{m+2}f_m^3,\ C=f_{m-1}f_{m+1}^3\), these read \(f_{2m+1}=A-144C\) for odd \(m\) and \(144A-C\) for even \(m\), and
\[
 f_{2m}=f_m(f_{m+2}f_{m-1}^2-f_{m-2}f_{m+1}^2).
\]
