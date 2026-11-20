# Dyadic congruences for packets with few prime divisors

Write \(n=2^k\ge8\), \(\tau=\sqrt{-2}\), and \(w_n=\prod_{p\mid w_n}p^{e_p}\). Then a prime-power packet \(w_n=p^e\) satisfies, for every \(e\),
\[
                p\ \ge\ \frac{n^6}{128}+\left(\frac{n^2}{4}-1\right)^2 .
\]
There is equality at \(n=8\), with \(p=2273=15^2+2\cdot32^2\). The result also excludes prime-power packets at all sufficiently large indices satisfying \(P^+(w_n)=O(n^4)\). A separate conclusion concerns any \(n\ge16\) at which precisely one prime \(p\) has odd depth: all of \(E'[4n]\) is rational over \(\mathbf F_p\), even when there are other primes of positive even depth.

An unconditional consequence for squareful and squarefree packets alike is
\[
                    \operatorname{rad}(w_n)\ge n^6/128 .
\]
Three distinct prime divisors already give \((8n^2+1)^3\). The two-prime case uses both coordinates of the primitive CM norm, as proved below.

## Two integer coordinates

Set \(u=u_{n/2},v=v_{n/2}\), and define
\[
   C=u^4+16u^2v^2-32v^4,\qquad D=32uv^3,\qquad
   \Gamma=C+D\tau,\qquad w_n=C^2+2D^2 .
\]
The representation is primitive at all odd primes: an odd divisor of \(D\) divides \(u\) or \(v\) and cannot divide \(C\), since \(\gcd(u,v)=1\). Both \(u\) and \(w_{n/2}\) are odd, and \(v_{2m}=2u_mv_mw_m\) with \(v_4=1\). Therefore
\[
    v_2(v)=k-3,\qquad v_2(D)=3k-4,\qquad C\equiv1\bmod 4.
\]
Also \(v_2(w_n-1)=2k-1\). At \(n=8\) this follows from \(w_8=2273\). For the induction use \(w_{2n}=w_n^4-128(u_nv_n)^4\). The difference \(w_n^4-1\) has valuation \(2k+1\), while the subtracted term has valuation \(4k-1>2k+1\). As \(v_2(2D^2)=6k-7>2k-1\), the norm identity now gives
\[
                       v_2(C-1)=2k-2.
\]
In particular \(\Gamma\equiv1\bmod 2n\), and \(\Gamma\equiv1\bmod4n\) for \(n\ge16\). [Dyadic identities and CM Frobenius](abc_octic_dyadic_fermat_audit.md)

All prime divisors \(p\) of \(w_n\) split in the norm-Euclidean ring \(\mathbf Z[\tau]\). Their CM Frobenius generators, up to conjugation, satisfy
\[
             \pi_p=A_p+B_p\tau
                 =1+2n(a_p+b_p\tau),\qquad \pi_p\overline{\pi}_p=p .
\]
Here \(b_p\ne0\). Because the representation of \(w_n\) is primitive and the only units are \(\pm1\), choose the orientation of each \(B_p\) so that \(\Gamma=\prod_p\pi_p^{e_p}\). The unit is \(+1\) by reduction modulo \(2n\). Any congruence \(\pi_p\equiv1\bmod m\) for rational \(m\) is invariant under the choice of conjugate.

## One prime divisor

If \(w_n=p^e\), then \(e\) is odd since \(w_n\) is a nonsquare. In the imaginary coordinate of \((A_p+B_p\tau)^e\), the quotient by \(B_p\) is odd: its first term \(eA_p^{e-1}\) is odd and every subsequent term contains a factor 2. Thus \(v_2(B_p)=3k-4\). Oddness of \(e\) also gives \(v_2(p-1)=v_2(w_n-1)=2k-1\). Since \(v_2(2B_p^2)>2k-1\), \(A_p\equiv1\bmod 4\), and \(p=A_p^2+2B_p^2\), we get \(v_2(A_p-1)=2k-2\). The least possible absolute values are consequently \(|B_p|\ge n^3/16\) and \(|A_p|\ge n^2/4-1\), proving the claimed bound. [All-index nonsquareness](abc_octic_dyadic_parity_quartic.md)

In this case \(\pi_p-1=2^{2k-2}\lambda\) for a \(\lambda\in\mathbf Z[\tau]\) of odd norm, since the real coordinate of \(\lambda\) is odd. Thus the full 2-primary subgroup of \(E'(\mathbf F_p)\) is exactly \(E'[n^2/4]\). Indeed rational points are killed by \(\pi_p-1\), and \(\lambda\) is invertible on all 2-primary torsion.

## Two prime divisors

Suppose \(w_n=p_1^{e_1}p_2^{e_2}\), and put \(\delta_i=a_i+b_i\tau=(\pi_{p_i}-1)/(2n)\). The two valuations of \(C-1,D\) show \(\Gamma\equiv1\bmod n^2/4\). Expanding the product of the two powers therefore gives \(e_1\delta_1+e_2\delta_2\equiv0\bmod n/8\). Some \(e_i\) is odd, so
\[
                       (n/8)\mid a_1b_2-a_2b_1 .
\]
If the determinant is nonzero, the determinant inequality applied to \((a_i,\sqrt2 b_i)\) yields
\[
     \frac n8\le |a_1b_2-a_2b_1|
       \le \frac{(\sqrt{p_1}+1)(\sqrt{p_2}+1)}{4\sqrt2\,n^2}
       \le \frac{\sqrt{p_1p_2}}{\sqrt2\,n^2}.
\]
The middle step uses \(|\delta_i|=|\pi_{p_i}-1|/(2n)\) in the complex embedding. It follows that \(p_1p_2\ge n^6/32\).

If the determinant vanishes write \(\delta_i=h_i(a+b\tau)\) for a primitive direction \((a,b)\) and nonzero integers \(h_i\). We have \(b\ne0\). Put \(T=e_1h_1+e_2h_2\). Binomial expansion of the product yields
\[
     \frac{C-1}{2n}\equiv aT\bmod 2n,\qquad
     \frac{D}{2nb}\equiv T\bmod 2n .
\]
Indeed in all positive powers of \(a+b\tau\) the imaginary coordinate is divisible by \(b\). The first congruence gives \(v_2(aT)=k-3\), so \(v_2(T)<k+1\). The second gives \(3k-4=k+1+v_2(b)+v_2(T)\). Subtracting the valuations gives \(v_2(b)-v_2(a)=k-2>0\), and primitivity forces \(a\) odd, \(v_2(b)=k-2\). Thus \(|B_{p_i}|\ge2n(n/4)=n^2/2\), each \(p_i\ge1+n^4/2\), and \(p_1p_2\ge(1+n^4/2)^2\).

## Odd-depth primes and the first two CM coordinates

For \(n\ge16\), multiplication modulo \(4n\) gives two necessary congruences
\[
              \sum_{\substack{p\mid w_n\\ e_p\ {\rm odd}}}
                        (a_p,b_p)=(0,0)\quad\text{in }\mathbf F_2^2 .
\]
At \(n=8\) the right side is \((1,0)\). Signs of the \(b_p\) do not affect these identities. If exactly two primes have odd depth their two vectors coincide. If exactly one prime \(p\) has odd depth then \(\pi_p\equiv1\bmod 4n\). All points of \(E'[4n]\) are then fixed by Frobenius, and \(p\ge32n^2+1\), since its nonzero imaginary coordinate is divisible by \(4n\).

More generally, assume \(p\) is the only odd-depth prime and \(2^h\) divides every other depth for an integer \(h\ge1\). Each other prime factor in \(\Gamma\) is \(1\bmod 2^{k+1+h}\) after raising it to its depth, by iterated squaring in \(\mathbf Z[\tau]\). With
\[
           j=\min(k+1+h,\,2k-2)
\]
we obtain \(\pi_p^{e_p}\equiv1\bmod2^j\). In the finite 2-group of units congruent to \(1\bmod 2n\) modulo \(2^j\), taking an odd power is an automorphism (the ring is commutative). Thus \(\pi_p\equiv1\bmod2^j\) and all of \(E'[2^j]\) is rational at \(p\).

For \(n\ge16\) the first modulus \(4n\) is the exact local square constraint when the square multiplier is unrestricted. Namely \((1+2n\mathcal O_2)^2=1+4n\mathcal O_2\) in \(\mathcal O_2=\mathbf Z_2[\tau]\): the convergent logarithm on this ball turns squaring into multiplication by 2. If a primary unit \(\pi\) is \(1\bmod4n\), then \(\Gamma/\pi\) can be absorbed in such a square over \(\mathcal O_2\). Imposing that a square come from prime divisors of the actual packet is a further global condition.

There is an exact test using all the mixed depths. Define
\[
       t_p=v_2(B_p)+v_2(e_p),\qquad t=\min_{p\mid w_n}t_p .
\]
Then \(t\le3k-4\). The number of primes attaining \(t\) is even if \(t<3k-4\), and odd if \(t=3k-4\). Indeed the imaginary coordinate of \(\pi_p^{e_p}\) has valuation \(t_p\). Raising to an odd exponent preserves the imaginary valuation as above, and each squaring increases it by exactly one because the real coordinate stays odd. In the product of these powers modulo \(2^{t+1}\), each term with at least three imaginary factors vanishes. Each term with one imaginary factor of minimal valuation contributes \(2^t\bmod2^{t+1}\). Comparing with \(v_2(D)=3k-4\) proves both claims.

In particular if \(p\) uniquely minimizes \(t_p\), then
\[
            p\ \ge\ 1+\frac{n^6}{128\,4^{v_2(e_p)}} .
\]
This also applies to a packet with many prime factors. For example, if there is just one odd-depth prime \(p\) and \(p<1+n^6/128\), there must be an even-depth prime \(r\) with \(v_2(B_r)<v_2(B_p)\). Otherwise \(p\) uniquely minimizes \(t_p\), contradicting the inequality.

## A bound in terms of normalized multiplicities

Put \(g=\gcd_{p\mid w_n}e_p\), \(m_p=e_p/g\), and \(M=\sum m_p\). Nonsquareness makes \(g\) odd. Then \(w_n^{1/g}\) has distance from 1 of exact 2-adic valuation \(2k-1\). Taking norms gives \(p\equiv1+4na_p\bmod 4n^2\). Multiplying these congruences with exponents \(m_p\) yields
\[
          \sum m_p a_p\equiv n/8\pmod {n/4}.
\]
In particular the absolute value of this sum is at least \(n/8\). Since \(|a_p|\le (\sqrt{p-8n^2}+1)/(2n)\) for every divisor, this gives
\[
     P^+(w_n)\ \ge\ 8n^2+
        \left(\max\left\{0,\frac{n^2}{4M}-1\right\}\right)^2 .
\]
This applies to mixed valuations regardless of their common scale. For example a packet with depths \(2g,3g\) must satisfy \(P^+(w_n)\ge8n^2+(\max\{0,n^2/20-1\})^2\). Squarefulness alone puts no upper bound on \(M\).

## Growth of the base of a maximal power

Write \(\Lambda=\prod_p\pi_p^{e_p/g}\); then \(\Gamma=\Lambda^g\) and \(\operatorname N\Lambda=w_n^{1/g}\). The proof for an odd power above gives the imaginary coordinate of \(\Lambda\) exact 2-adic valuation \(3k-4\). Fix an odd positive integer \(H\) dividing any earlier \(v_{2^j}\). For all sufficiently late \(n\) it divides \(v_{n/2}\), so \(\Gamma\equiv\bar\Gamma\bmod H^3\) by the formula for \(D\), and \(\Gamma\) is a unit modulo \(H^3\) by primitivity. For every fixed integer \(q\ge3\), only finitely many \(w_n\) are \(q\)-th powers, by Darmon–Granville applied to the primitive equation \(X^4-8Y^4=Z^q\). Squares never occur. Hence for all sufficiently large \(n\), \(g\) is coprime to the fixed order of \((\mathcal O/H^3\mathcal O)^\times\). Raising to the \(g\)-th power is an automorphism there, and \(\Lambda\equiv\bar\Lambda\bmod H^3\). As \(2\tau\) is a unit at odd \(H\), its imaginary coordinate is divisible by \(H^3\). Its absolute value is at least \(H^3n^3/16\), giving \(w_n^{1/g}\ge H^6n^6/128\). The odd parts of the \(v_{2^j}\) are unbounded: they accumulate all earlier odd packets \(w_{2^i}\) via the duplication recurrence. It follows that
\[
                        w_n^{1/g}/n^6\longrightarrow\infty .
\]
In particular \(p/n^6\to\infty\) on any sequence of prime-power packets \(w_n=p^e\). This last limit has no effective cutoff from the finiteness theorem. [Fixed-exponent finiteness](abc_octic_dyadic_parity_quartic.md)

Some multipliers are effective at every relevant index. For \(n\ge32\), \(v_{16}=2\cdot31\cdot14\cdot2273\) divides \(v_{n/2}\). The ring-unit orders modulo \(7^3\) and \(31^3\) have prime factors among \(2,3,5,7,31\), since these two inert primes have respective residue sizes \(7^2,31^2\). The split prime 2273 gives unit-group order \((2273-1)^2=(32\cdot71)^2\) modulo 2273. The all-index perfect-power exclusions through 150 thus make \(g\) coprime to all three orders. The same argument yields the all-index lower bound
\[
           w_n^{1/g}\ge 2\left((7\cdot31)^3\cdot2273\,n^3/16\right)^2
                 \qquad(n\ge32).
\]
[Exact modular exclusion of exponents through 150](abc_dyadic_cm_power_characters.md)
