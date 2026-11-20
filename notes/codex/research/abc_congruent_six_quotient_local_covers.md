# Uniform local obstructions to a square multiplication quotient

On \(E:y^2=x^3-36x\) take \(G=(-3,9)\), and write \(B_n^2\) for the reduced abscissa denominator of \([n]G\). For **every prime \(q<10{,}000\) and every positive odd \(m\)** the positive integer \(B_{qm}/B_m\) has a prime of odd valuation. For unbounded \(q\), three elementary criteria prove the same statement on a set of primes of relative density \(13/16\). [Finite certificates](abc_congruent_six_quotient_local_covers.csv) · [Standard-library verifier](abc_congruent_six_quotient_local_covers.py)

For \(q=2\) the duplication formula gives \(B_{2m}/B_m=2|ab|\), with \(a,b\) odd, so its 2-adic valuation is one. [Primitive duplication formula](abc_full_quartic_signature.md)

For odd \(q\) put \(D=(q^2-1)/2\) and \(\eta_q=(-1)^{(q-1)/2}\). The composition identity and the known sign of the odd normalized division sequence give
\[
   \frac{B_{qm}}{B_m}
       =\eta_q\,\psi_q([m]G)\,B_m^{2D}3^{-D}.
\]
Here \(D\) is divisible by four. In particular, the sign is independent of \(m\). [Composition and normalization](abc_congruent_six_smooth_odd_primitive.md) · [Sign proof](abc_gaussian_quartic_odd_cofactors.md)

At a good prime \(p>3\), if \([m]G\) is affine in reduction, a nonresidue value of \(\eta_q\psi_q([m]G)\) certifies nonsquareness. A zero is left undecided. If \([m]G\) reduces to the identity, write \(x([m]G)=A_m/B_m^2\) in lowest terms. The leading term \(qX^D\) of the odd division polynomial gives
\[
    B_{qm}/B_m\equiv\eta_q q A_m^D3^{-D}\pmod p.
\]
Thus its character is \((\eta_q q/p)\) for \(p\ne q\). When \(p=q\) at the identity the formal logarithm gives \(v_p(B_{qm}/B_m)=1\). All these tests depend only on \(m\bmod\operatorname{ord}_p(G)\) and are invariant under changing the sign of \(m\). In particular any \(p\mid B_m\), \(p\ne q\), gives a direct reciprocity obstruction if \((q/p)=-1\), since these \(p\) are 1 modulo 12.

The following three conditions on \(q\) suffice independently.

* If \(q\equiv3,5\pmod8\), the all-index identity \(B_n\equiv(-1)^{(n-1)/2}n\pmod8\) gives \(B_{qm}/B_m\equiv5\pmod8\).
* If \(q\equiv7,9\pmod{16}\), use \(p=31\). Here \(G\) has order 16, and for every odd \(m\) the table gives \((\eta_q\psi_q([m]G)/31)=-1\).
* If \((q/5)=(q/13)=-1\), use \(p=13\). Here \(G\) has order 5. On each of the four nonidentity multiples the character of \(\psi_q\) equals \((q/5)\), and in the identity disc the character is \((q/13)\).

The finite tables in the last two claims suffice for unbounded \(q\). For a point \(R\) of reduction order \(d\), set \(W_j=\psi_j(R)\). Ward's addition identity gives \(W_{j+d}W_{j-d}=-W_{d+1}W_{d-1}W_j^2\). For \(d\nmid j\) two applications show the Legendre symbol is periodic in \(j\) modulo \(4d\). For \(d\mid j\) the value is zero. The verifier checks the finite residue systems modulo 64 and 20. The first two bullets cover six of the eight reduced classes modulo 16. In each of the other two classes, the third bullet applies to a quarter of the primes, by independence modulo 5 and 13. This gives density \(13/16\).

For the finite range, the first bullet handles 625 primes and the certificate lists auxiliary primes for the other 603. Start from all odd \(m\bmod2\). For each auxiliary \(p\), lift the surviving classes to the least common multiple of the current modulus and \(\operatorname{ord}_p(G)\), then apply the local test. The survivors are empty for every one of the 603 listed multipliers. This proves the assertion for all odd \(m\), without any size bound on \(m\). The largest auxiliary prime is 63,421. For a general fixed multiplier the [division-polynomial argument](abc_congruent_six_smooth_odd_primitive.md) proves finiteness of the square exceptions. The computations here determine the empty exception sets for the stated prime multipliers.
