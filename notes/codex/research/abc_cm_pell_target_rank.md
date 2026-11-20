# The multiplicative rank of the 50 Pell targets for full 11-torsion

Let \(g=(1+\sqrt2)^4\), \(E:y^2=x^3+16x^2+32x\), and \(\theta_\pm=-8\pm4\sqrt2\). For a full-annihilator 11-torsion abscissa \(x\), put \(u=(\theta_+-x)/(x-\theta_-)\) and let \(U\) be the set of 50 such targets. The 50 elements of \(U\) are multiplicatively independent modulo roots of unity. On adjoining \(g\) there is exactly one independent relation, generated integrally by
\[
                            g^{12}\prod_{u\in U}u=1.                       \tag{1}
\]
In particular, every proper subset of \(U\), together with \(g\), remains multiplicatively independent modulo torsion. The target set arises when the conic parameter runs through powers of \(1+\sqrt2\). [Pell orbit and common factors](abc_cm_pell_target_gcd.md)

## Normalization and complex uniformization

Let \(G\) be the primitive degree-50 abscissa factor of the 11-division polynomial. The monic target polynomial is
\[
 P(z)=\frac{(z+1)^{50}G((\theta_- z+\theta_+)/(z+1))}{G(\theta_-)}.
\]
The product of the targets is \(P(0)=G(\theta_+)/G(\theta_-)=g^{-12}\). This last equality uses only arithmetic in \(\mathbf Q(\sqrt2)\) on the coefficients of \(G\). The certifier recomputes \(G\) by factoring the division polynomial from its recurrence. [Exact and interval verifier](abc_cm_pell_target_rank.py)

The real period lattice is rectangular because the cubic has three distinct real roots. Write its generators as a positive real \(\Omega\) and \(\rho\Omega\) on the positive imaginary axis. Complex multiplication by \(\tau=\sqrt{-2}\) of positive imaginary part sends the first generator to \(m\rho\Omega\) and the second to \(-n\Omega\), with \(m,n\) positive integers and \(mn=2\). The real half-period corresponds to \((0,0)\), the two-torsion point on the identity component. It belongs to the kernel of \([\tau]\), so \(m\) is even. This gives \(m=2,n=1\) and \(\rho=i/\sqrt2\).

For \(z\bmod(\mathbf Z+\rho\mathbf Z)\) the abscissa is
\[
 x(z)=\wp(z;\rho)/\Omega^2-16/3,
 \qquad \Omega^2=3\wp(1/2;\rho)/16 ,
\]
from the Weierstrass-to-short-model translation and \(x(1/2)=0\). Take the real point with parameter \(1/11\). Its annihilator is full because a proper CM prime annihilator would also have its conjugate annihilating that real point. Multiplication by \(a+b\tau\) therefore gives all full abscissas for invertible classes, with parameter \((a+2b\rho)/11\). Represent the two scalar coordinates in \(\mathbf F_{11}^\times\) as \(a+3b=2^j\) and \(a-3b=2^k\). Negation adds \((5,5)\), and \(0\le j<10\), \(0\le k<5\) gives all 50 quotient classes. The corresponding group
\[
                    H=(\mathbf F_{11}^\times)^2/\{\pm(1,1)\}
\]
acts regularly on the abscissas by Galois automorphisms fixing both \(\sqrt2\) and \(\tau\), by the ray-class argument in the common-factor proof.

## A full-rank logarithm matrix

Put \(L_h=\log|u_h|\) at the chosen complex embedding. A multiplicative relation modulo torsion would, after applying every \(h\in H\), yield a vector in the real kernel of the group matrix \((L_{hk})_{h,k\in H}\). Column inversion changes this into the convolution matrix \((L_{hk^{-1}})\). Its eigenvalues, up to character conjugation, are
\[
  \sum_{j=0}^9\sum_{k=0}^4 L_{j,k}\exp(2\pi i(rj+sk)/10),
     \quad 0\le r,s<10,\quad r+s\text{ even}.
\]
The verifier evaluates all 50 using Arb complex and real balls at 192 bits. Every modulus interval lies strictly above 2, and at least one lies below 2.013. Its comparisons use the full ball enclosures. Thus the convolution matrix is invertible and the 50 targets are multiplicatively independent modulo torsion. Finally, raising any putative relation involving \(g\) to power 12 and substituting (1) gives identical exponents on all targets. Their independence forces each exponent to equal one twelfth the exponent of \(g\). This proves the integral generator assertion.

## Exact certificate from reduction at one prime

The rank also has a proof using finite-field arithmetic alone. The field \(L'=\mathbf Q(\sqrt2,\sqrt{-2},E[11])\) is unramified at 5 by good reduction and the prime-to-5 torsion criterion. Every root of unity in \(L'\) thus has order prime to 5, since adjoining a primitive fifth root ramifies at 5.

Use \(p=9241\), \(\sqrt2=2863\), \(\tau=3220\) in \(\mathbf F_p\) and \(T=(2122,2151)\). Then \([11]T=O\), \([\tau]T=(1091,4736)\), and both \([3\pm\tau]T\) are nonzero. Therefore \(T\) lifts to a full 11-torsion point, and the 50 abscissas of the scalar translates give the reductions of the 50 targets. Set \(\xi=13^{1848}\bmod p\), of order five. For each \(h\in H\) write \(u_h^{1848}=\xi^{b_h}\) in the residue field with \(b_h\in\mathbf F_5\). In the ordering \((j,k)\) used above, with \(j\) first and \(k\) second, direct elimination gives
\[
                           \det(b_{hk})_{h,k\in H}=1\pmod5 .
\]
The verifier checks primality, the two square roots, the CM formula, the exact order and proper annihilators, all 50 distinct targets and the determinant using Python's standard library. [Exact finite-field verifier](abc_cm_pell_target_rank_mod.py)

Any relation up to torsion could be taken with primitive integer exponent vector, since dividing a vector by its coefficient gcd preserves membership in the relation lattice modulo torsion. Apply every scalar automorphism over \(\mathbf Q(\sqrt2,\sqrt{-2})\), reduce at the chosen place and apply the order-five character. All the root-of-unity factors map to 1, so this primitive vector lies in the kernel of the displayed invertible matrix modulo 5. Its entries would all be multiples of 5, a contradiction.

## A positive density of fully split primes omitted by the Pell sequence

The same finite-field certificate proves that the 50 elements \(u_h\) are linearly independent in \(L'^\times/L'^{\times5}\). Indeed a fifth-power relation reduces to a fifth-power residue at each of the 50 Galois translates at 9241. The determinant forces all its exponents to be zero modulo 5. Adjoining \(\mu_5\) preserves the assertion by norm and the fact that \([L'(\mu_5):L']\) divides four. Write \(M=L'(\mu_5)\). Kummer theory gives
\[
 \operatorname{Gal}\big(M(u_h^{1/5}:h\in H)/M\big)\simeq (\mathbf F_5)^{50}.
\]
Both fields are Galois over \(\mathbf Q\): every conjugation of \(\sqrt2\) either fixes the two parameters \(\theta_\pm\) or interchanges them, so it permutes the targets or their reciprocals. Fix a primitive fifth root of unity to label the Frobenius coordinates \(b_h\in\mathbf F_5\). For good rational primes splitting completely in \(M\), \(u_h\bmod p\) is a fifth power exactly when \(b_h=0\). By (1) and the invertibility of 12 modulo 5, \(g\bmod p\) is a fifth power exactly when \(\sum_h b_h=0\). Choosing another place or another primitive root merely permutes the entries and scales them all by a common nonzero scalar.

Condition on a rational prime splitting completely in \(M\) and \(g\) being a fifth power. The relative natural density of primes for which exactly \(k\) of the 50 targets are fifth powers, for \(0\le k\le50\), is
\[
              \binom{50}{k}\frac{4^{50-k}+4(-1)^{50-k}}{5^{50}}.          \tag{2}
\]
Indeed the count of vectors of length \(r=50-k\) of nonzero entries summing to zero is \((4^r+4(-1)^r)/5\) by additive-character orthogonality. Chebotarev gives the relative density as the corresponding proportion out of the \(5^{49}\) zero-sum vectors. All the conditions used are stable under conjugation over \(\mathbf Q\), so the same count applies to rational primes.

In particular the fraction \((4^{50}+4)/5^{50}\) has no fifth-power target at all, and therefore never divides a Pell term \(D_{11,n}\), even though every geometric target reduces rationally and the generating unit is a fifth power. A fixed finite set of primes in normalizations and discriminants has density zero. The fraction with exactly 49 eligible targets is zero. For the other cases the fifth-power condition is a necessary condition for an actual Pell hit. This density statement does not require a conjecture on orders of a fixed unit modulo varying primes.

The calculation extends to every \(Q=5^m\). Let \(M_m=L'(\mu_Q)\). Because \(L'\) is unramified at 5 and the cyclotomic extension is totally ramified there, \(M_m/L'\) has the full abelian cyclotomic Galois group. Restriction on \(H^1(L',\mu_5)\) to \(M_m\) is injective. Its kernel inflates from the cohomology of this abelian Galois group with coefficients in \(\mu_5\), and a central element acts nontrivially on \(\mu_5\), forcing the degree-one cohomology to vanish. Thus the mod-5 independence persists over \(M_m\). It implies full independence modulo \(Q\)-th powers there. If a product of targets is a \(5^m\)-th power, its exponents are all divisible by 5. On dividing exponents by 5 the resulting product differs from a \(5^{m-1}\)-th power by a fifth root of unity, itself a \(5^{m-1}\)-th power in \(M_m\). Iterating proves the assertion.

The Kummer group now equals \((\mathbf Z/Q\mathbf Z)^{50}\). The relative density in (2), conditional on complete splitting in \(M_m\) and \(g\) being a \(Q\)-th power, becomes
\[
              \binom{50}{k}\frac{(Q-1)^{50-k}+(Q-1)(-1)^{50-k}}{Q^{50}}.
\]
The character-orthogonality count is valid on any finite cyclic group. Thus the conditional fraction with no eligible target tends to one as \(m\to\infty\). Already at \(Q=25\), the fraction of **all primes splitting completely in \(L'\)** known to miss every Pell term by this test is at least
\[
                     \frac{24^{50}+24}{500\cdot25^{50}}>\frac1{4000}.
\]
Here \(1/20\) imposes splitting in \(M_2\) and a further fraction \(1/25\) imposes the power condition on \(g\); 12 is invertible modulo 25. The conditional families for larger \(m\) each have positive density and their densities decrease with \(m\).

## Both splitting types of the real quadratic field

The same \(1/4000\) lower bound holds relative to **all good rational primes at which all 50 abscissas are rational**. Let \(A=\mathbf Q(\sqrt2,x(T):T\text{ full})\), a Galois subfield of \(L'\). Independence modulo fifth powers descends to \(A\), so the argument for complete splitting applies directly there. At a prime with all abscissas rational and \(\sqrt2\notin\mathbf F_p\), the Frobenius on \(A\) is the central involution \(\sigma\) fixing every abscissa and interchanging \(\theta_-,\theta_+\). It sends each \(u_h\) and \(g\) to its inverse. This case occurs at 683, where the full factor has 50 distinct residue roots and 2 is a quadratic nonresidue.

For \(Q=5^m\), impose \(p\equiv-1\bmod Q\) on this class of primes. Cyclotomic disjointness gives relative density \(1/\varphi(Q)\). On the compositum \(A(\mu_Q)\), Frobenius acts as \(\sigma\) and inversion on \(\mu_Q\). In the Kummer extension the simultaneous inversion on the targets and on their \(Q\)-th roots of unity makes its conjugation action on \(\Delta=(\mathbf Z/Q\mathbf Z)^{50}\) trivial. There is a lift \(s\) of order two acting on every chosen target root \(u_h^{1/Q}\) by inversion. For example define this action on the monomial basis with exponents from 0 to \(Q-1\), using the independent Kummer generators and the relations \((u_h^{1/Q})^Q=u_h\). It respects multiplication and squares to identity.

Write a rational Frobenius lift as \(\kappa s\). At the residue-degree-two place over \(p\) the relative Frobenius is \((\kappa s)^2=\kappa^2\). Squaring permutes \(\Delta\) as \(Q\) is odd. Consequently the same character-vector proportions apply by Chebotarev. Each \(u_h\) and \(g\) reduces in the norm-one torus of \(\mathbf F_{p^2}^\times\). Its \(Q\)-th powers are exactly its elements that are \(Q\)-th powers in the whole residue field: the norm of a chosen root lies in \(\mathbf F_p^\times[Q]=1\). Thus the conditional fraction with no eligible targets is identical in this class. Taking \(Q=25\) gives the same lower bound separately in both splitting types, hence also in their union.
