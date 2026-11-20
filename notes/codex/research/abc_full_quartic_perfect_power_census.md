# Perfect powers in the primitive quartic family

For every integer \(2\le k\le10^9\), the only primitive integer solutions of
\[
                 a^4+3b^2=4z^{4k},\qquad a,z>0,
\]
are \((a,b,z)=(1,\pm1,1)\). Here primitive means \(\gcd(a,b,z)=1\). The same conclusion holds if the integer \(k\) has any prime divisor at most this cutoff. The computation bounds the exponent only. There is no size cutoff on the solutions. Two modular tests cover every prime exponent through 31,904,497. A separate trace calculation extends the range to one billion. [Trace argument](abc_congruent_six_exponent_trace_sieve.md) · [Independent full-range audit](abc_congruent_six_exponent_trace_audit.txt)

## From a denominator at an arbitrary index to a single prime index

Let \(E:Y^2=X^3-36X\), \(G=(-3,9)\), and write \(B_m^2\) for the reduced positive denominator of \(X(mG)\). Primitive solutions of \(a^4+3b^2=4w^4\) have \(w=B_n\), \(X(nG)=-3a^2/w^2\), \(Y(nG)=9ab/w^3\) for an odd index \(n\), with the sign of \(n\) accounting for the sign of \(b\). We may take \(n>0\). The entries are odd and pairwise coprime, and \(3\nmid aw\). The completed square and cube arguments exclude exponents 2 and 3 at all odd \(n>1\). Also \(B_1=1\) and \(B_n>1\) for every odd \(n>1\), by the height estimate below. [Parametrization](abc_full_quartic_signature.md) · [Square proof](abc_full_quartic_square_classification.md) · [Cube proof](abc_full_quartic_cube_classification.md)

Suppose \(B_n\) is an \(\ell\)-th power for prime \(\ell\ge5\), and take \(q\) to be the largest prime divisor of \(n>1\). Every \(p\mid B_q\) has good reduction since \(B_q\) is coprime to 6. The reduction of \(G\) has order \(q\) since \(G\) is integral and \(q\) is prime. The subgroup it generates together with the full rational two-torsion has order \(4q\). Hasse's bound gives \(p\ge(2\sqrt q-1)^2>2q\) for odd \(q\ge3\). In particular \(p\nmid n\). The formal group formula gives
\[
              v_p(B_n)=v_p(B_q)+v_p(n/q)=v_p(B_q).
\]
Thus \(B_q\) is an \(\ell\)-th power as well.

## The exponent determines the prime index

Write \(B_q=z^\ell>1\), and let \((a,b,w)\) be its primitive quartic solution with \(w=B_q\). In the Eisenstein integers set \(j=\sqrt{-3}\) and \(\alpha=(a^2+bj)/2\). Then \(N\alpha=z^{4\ell}\). The ideals of \(\alpha\) and \(\bar\alpha\) are coprime, since any common prime ideal would divide \(a^2=\alpha+\bar\alpha\) and lie over a divisor of \(z\). This ring is a PID and the \(\ell\)-power map on its six units is bijective. Hence \(\alpha=\gamma^\ell\) with \(N\gamma=z^4\) and \((\gamma,\bar\gamma)=1\). Write
\[
 U=\gamma+\bar\gamma,\quad V=(\gamma-\bar\gamma)/j,\quad
 L=(\gamma^\ell+\bar\gamma^\ell)/U .
\]
The integers \(U,V\) have the same parity. They are odd since \(\alpha+\bar\alpha=a^2\) is odd, while at the inert prime 2 an even trace would put \(\gamma\bmod 2\) in \(\mathbf F_2\), which also forces its power to have even trace. Since \(a\ne0\), we have \(U\ne0\). The integer \(L\) is the conjugation-invariant alternating sum of the degree \(\ell-1\) monomials, and \(UL=a^2\). For any prime ideal over a rational divisor of \(U\), both \(\gamma,\bar\gamma\) are units there and \(L\equiv\ell\gamma^{\ell-1}\pmod U\). Consequently only \(\ell\) can divide both \(U\) and \(L\).

If \(\ell\nmid U\), coprimality and \(UL=a^2\) give \(|U|=s^2\). The norm identity reads
\[
                 s^4+3V^2=4z^4 .
\]
We have \(\gcd(s,z)=1\), since a prime of the Eisenstein ring over a divisor of \(z\) dividing one of \(\gamma,\bar\gamma\) cannot divide their sum. Hence this solution is primitive. Its denominator \(z\) is \(B_m\) for a positive odd \(m\). Pick any \(p\mid z\). Since \(p\mid B_q\) and \(p\mid B_m\), the exact reduction order implies \(q\mid m\). Formal group divisibility at every prime of \(B_q\) now gives \(B_q\mid B_m=z\). This contradicts \(B_q=z^\ell>z\).

Thus \(\ell\mid U\), forcing \(\ell\mid a\). On \(E\) this gives \(qG=(0,0)\bmod\ell\), since \(\ell\nmid w\). The order of \(G\bmod\ell\) is exactly \(2q\), since its ordinate 9 is nonzero there. This leaves at most one \(q\) for each exponent \(\ell\). Moreover \(2w^2-a^2=c^2\) and \(2w^2+a^2=3d^2\) for coprime integers \(c,d\), by factoring \(3b^2\). Reducing at \(\ell\) shows that both 2 and 3 are quadratic residues. This implies \(\ell\equiv\pm1\pmod{24}\). The proof uses only these two residue classes for the finite calculation. [Further restrictions on the exponent](abc_full_quartic_prime_exponents.md)

## Two certificates through 31,904,497

The C++ sieve passes through every prime \(\ell\equiv\pm1\pmod{24}\) up to the cutoff. It verifies an annihilating multiple of \(G\) by multiplication in \(E(\mathbf F_\ell)\), factors the multiple and tests each odd prime divisor \(q\) for \(qG=(0,0)\). The complex multiplication formula supplies candidate multiples. Completeness only requires the checked annihilation, since the exact order divides every annihilator. Among 491,809 primes in these two residue classes there are 23,883 candidate pairs. The largest candidate exponent is 31,903,633.

Write \(f_q=3^{-(q^2-1)/2}\psi_q(G)\); at odd indices \(|f_q|=B_q\). The normalization follows by scaling the division polynomial to \(y^2=x^3-4x\), where the odd-index values are integral and coprime to 6. Good reduction prevents cancellation away from 6. The verifier evaluates the recurrence in residue rings. [Normalization proof](abc_gaussian_quartic_odd_cofactors.md) · [Recurrence](abc_congruent_six_quotient_local_covers.py)

Every candidate is excluded by both of the following tests.

1. The residue \(f_q\) is a unit modulo \(\ell^2\) and \(f_q^{\ell-1}\ne1\bmod\ell^2\). An \(\ell\)-th power unit must give 1 by Euler's theorem, since \(\varphi(\ell^2)=\ell(\ell-1)\).
2. An even multiplier \(j\le168\) gives \(h=j\ell+1\) and \(t=f_q^j\bmod h\) with \(t^\ell=1\bmod h\), \(\gcd(t-1,h)=1\), and \(h<(\ell+1)^2\). At each prime divisor of \(h\), the order of \(t\) is exactly \(\ell\), so the prime divisor is at least \(\ell+1\). The size bound certifies that \(h\) is prime. An \(\ell\)-th power unit in \(\mathbf F_h\) would have \(j\)-th power 1. Both tests are unchanged when the sign of \(f_q\) is reversed.

To reproduce the census from the directory containing the files, use Python 3 and a C++17 compiler.

```sh
c++ -O3 -std=c++17 abc_full_quartic_prime_rank_scan.cpp -o /tmp/abc-quartic-power-scan
python abc_full_quartic_perfect_exponents.py /tmp/abc-quartic-power-scan
```

[C++ enumeration](abc_full_quartic_prime_rank_scan.cpp) · [Two modular checks](abc_full_quartic_perfect_exponents.py) · [Sieve dependency](abc_congruent_six_smooth_odd_support.py)

PARI independently computed the order of \(G+(0,0)\) at every eligible prime, recovering the same 23,883 pairs. A second division-polynomial computation recovered all their residues modulo \(\ell^2\). The SHA-256 digest of the list in scanner order is `83917e8c564853dd46af78905ee4d0b95696aaa01fa77021522b6a85e884f312`. [Audit](abc_full_quartic_perfect_exponents_audit.py) · [Output](abc_full_quartic_perfect_exponents_audit.txt)

## Extension through one billion

In the trace descent, \(U=\sigma\ell u^2\) with \(\sigma=(-1)^{(\ell-1)/2}\). Reduce the norm-one element \(\gamma/z^2\) at an auxiliary prime \(r\). Its \(\ell\)-th power has trace \(-X(qG)/3\), and \(q\) is coprime to the order of \(G\bmod r\) for the chosen auxiliary primes, by the height bound on \(B_q\). Inverting \(\ell\) in the norm-one group lets one compute the possible traces of \(\gamma/z^2\). Their quadratic characters must agree with that of \(\sigma\ell\). The primes \(r\le251\) leave only ten possible prime exponents through \(10^9\). For each of the ten a further prime \(r\le1249\) gives a contradiction. The independent verifier sweeps every integer \(24j\pm1\) in the required range, computes the elliptic orders and slopes in PARI, and checks each surviving prime using the original trace recurrence. [Derivation and ten witnesses](abc_congruent_six_exponent_trace_sieve.md) · [Trace sieve](abc_congruent_six_exponent_trace_sieve.py) · [Independent verification](abc_congruent_six_exponent_trace_audit.py) · [Direct scan](abc_congruent_six_exponent_trace_audit.cpp)

## A result with no bound on the exponent

For any odd \(n>1\) such that every prime divisor of \(n\) is at most 150,000, \(B_n\) is never a perfect power. Indeed \(\log B_q\le0.52q^2+1.5\) by the duplication height estimate, and \(\log B_q\ge\ell\log(2q)\) if \(B_q\) is an \(\ell\)-th power, by the lower bound on its prime factors. The function \((0.52q^2+1.5)/\log(2q)\) is increasing for \(q\ge3\), and at 150,000 it is less than \(10^9\). This result covers arbitrarily large indices. [Height bounds](abc_full_quartic_prime_exponents.md)

For all other indices there is also a structural restriction. Every nontrivial perfect-power index is a power of a single prime \(q\equiv3\pmod4\). At a composite such index each prime exponent \(\ell\) must satisfy \(2^{\ell-1}\equiv1\pmod{\ell^2}\). [Prime-index shape](abc_full_quartic_prime_power_indices.md) · [Wieferich condition](abc_full_quartic_wieferich_exponents.md)

For every fixed \(k\ge2\), even beyond the census, one can effectively enumerate the indices whose exponents outside a prescribed finite set of primes are all divisible by \(k\). The prime-index bound above makes the largest possible index prime computable; finiteness of the auxiliary higher-genus curves makes the search for prime-power index bounds terminate. [Algorithm and proof](abc_congruent_six_all_power_cofactors.md)

## Relation to abc

An infinite sequence of the remaining nontrivial perfect powers would disprove rational abc already at \(\varepsilon=1/4\). Indeed \(a<\sqrt2\,w\) and \(|b|\le2w^2/\sqrt3\) follow from the defining equation. If \(w=z^\ell\), then \(\operatorname{rad}(w)\le w^{1/\ell}\), and the primitive triple \((a^4,3b^2,C=4w^4)\) has \(R=\operatorname{rad}(6abw)\ll w^{3+1/\ell}\). Consequently \(C/R^{5/4}\gg w^{1/4-5/(4\ell)}\), which tends to infinity along any such sequence since \(\ell>10^9\) and \(w\to\infty\). No such infinite sequence has been found. A small radical can also come from mixed valuations of \(a,b,w\). The perfect-power exclusion gives no general bound on their total contribution. [Mixed-valuation criterion](abc_full_quartic_twin_and_mixed_valuations.md)
