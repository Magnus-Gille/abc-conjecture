# Projective orders for growing conductors in varying quadratic fields

The short-relation criterion on the conic \(u^2+2v^2=w^2\) uses moduli \(M_d\) divisible by \(p^{k_d}\) for every prime \(p\le d\), where \(k_d=(1+o(1))\log d\). For each fixed \(A,\sigma>0\) and all sufficiently large \(d\), the following assertion holds uniformly in the quadratic field \(K\). Take a quadratic algebraic integer \(\gamma\) of norm coprime to \(M_d\), write \(\lambda=\gamma/\bar\gamma\), and form its rational trace
\[
 t=\lambda+\lambda^{-1}
   =\frac{(\operatorname{Tr}\gamma)^2}{N\gamma}-2.
\]
If \(\lambda\) is not a root of unity and \(H(t)\le d^\sigma\), no positive exponent \(n\le d^A\) makes \(\gamma^n\) scalar modulo \(M_d\mathcal O_K\). Here \(H(t)\) is the maximum of the denominator and absolute numerator in lowest terms. The same assertion holds for scalarity in any quadratic order containing \(\gamma\), since it implies scalarity in the maximal order. [Conic construction and short-relation criterion](abc_square_conic_growing_primes.md)

## A bound independent of the field

Fix any finite nonempty set \(S\) of odd primes and write \(P=\prod_{p\in S}p\). Suppose \(P^k\mid M\), \(\gcd(N\gamma,M)=1\), and \(\gamma^n\) is scalar modulo \(M\). Then for every \(\epsilon>0\)
\[
 n\gg_{S,\epsilon}\frac{P^k}{H(t)^{2+\epsilon}}.                       \tag{1}
\]
There is no discriminant in the implied constant. Choose \(T\) divisible by \(p(p^2-1)\) for all \(p\in S\). For a place above \(p\), use the valuation normalized by \(v_p(p)=1\). The residue field of the quadratic completion has at most \(p^2\) elements, and the order of its multiplicative group divides \(p^2-1\). Thus \(v_p(\lambda^{p^2-1}-1)\ge1/2\), allowing ramification. The binomial expansion after taking the \(p\)-th power gives valuation at least \(\min(1+1/2,p/2)>1/(p-1)\) for odd \(p\). The usual lifting formula consequently gives
\[
 v_p(\lambda^{Tn}-1)=v_p(\lambda^T-1)+v_p(n).
\]
Scalarity of \(\gamma^n\) and the unit norm give \(\lambda^n\equiv1\bmod p^k\mathcal O_K\), so the left side is at least \(k\).

Define the integral trace polynomial \(P_T\) by \(P_T(z+z^{-1})=z^T+z^{-T}\) and let \(G_T\) be the monic squarefree part of \(P_T(X)-2\). Its roots are \(\zeta+\zeta^{-1}\) with \(\zeta^T=1\). Roots different from \(\pm2\) have multiplicity two in \(P_T(X)-2\), and the endpoints present have multiplicity one. This follows from \(z^T+z^{-T}-2=(z^T-1)^2/z^T\) and the ramification of \(z\mapsto z+z^{-1}\) at \(z=\pm1\). In particular the irreducible monic factors of \(G_T\) lie in \(\mathbb Z[X]\). The rational \(t\) is integral at each \(p\in S\), so all local valuations of these factors are nonnegative. Since \(\lambda\) is nontorsion, none vanishes. Therefore
\[
 v_p(\lambda^T-1)=\tfrac12 v_p(P_T(t)-2)\le v_p(G_T(t)).
\]

For a fixed squarefree integral polynomial \(G\) and fixed finite \(S\), the finite-place Subspace Theorem in dimension two gives
\[
 \prod_{p\in S}p^{v_p(G(t))}\ll_{G,S,\epsilon}H(t)^{2+\epsilon}
 \quad\text{when }G(t)\ne0\text{ and }t\text{ is integral on }S.
\]
For detail, use the primitive pair of numerator and denominator of \(t\), whose denominator is a unit on \(S\). At each prime a small value of \(G\) is, within constants, proximity to one of its finitely many simple algebraic roots. Use the corresponding linear form and an independent coordinate form of size at most one there. At infinity the coordinate product is at most \(H(t)^2\). The projective Subspace Theorem bounds the product of the normalized local distances below by \(\gg H(t)^{-2-\epsilon}\). There are only finitely many assignments of the forms, and each exceptional rational line has just one primitive direction. This proof is ineffective in its constants. Multiplying the local lower bounds for \(p^{v_p(n)}\) proves (1). In the growing-modulus application, choose \(S\) with \(\log P>A+3\sigma+1\) and use \(\epsilon=1\).

## Consequences for the conic lattice

The \(d\) generators \(\eta_i\) in \(\mathbb Z[\sqrt2]\) have distinct split prime norms \(\ell_i\ll d\log d\) and both real embeddings of absolute value at most \((1+\sqrt2)\sqrt{\ell_i}\). Consequently \(t(\eta_i)\) has multiplicative height \(d^{1+o(1)}\). The same calculation gives \(H(t(\gamma))\le d^{L+o_L(1)}\) for any product \(\gamma\) of at most \(L\) of the generators and their conjugates. A nonzero exponent direction gives a nontorsion ratio by taking valuations at a split prime ideal unique to a coordinate. Replacing inverse powers by conjugates changes only a rational scalar, a unit modulo \(M_d\).

Thus each generator has projective order exceeding every fixed power of \(d\), uniformly in its index. More generally, for any short kernel relation \(z\ne0\) with \(\|z\|_1\le d^A\), its primitive direction \(w=z/\gcd_i(|z_i|)\) must satisfy \(\|w\|_1\to\infty\) as \(d\to\infty\). This excludes one-coordinate relations of polynomial length and all their bounded-direction analogues.

For every fixed \(r,A\), choose any \(r\) coordinates. The index of the relation lattice on these coordinates is at least the projective order of any one generator, hence eventually exceeds \(d^{rA}\). There cannot be \(r\) independent relations of 1-norm at most \(d^A\) in these same coordinates, by the determinant bound for an integral matrix with such rows. One primitive relation of unbounded direction in two or more coordinates is still possible.

There is also an archimedean restriction on a ring-class test. Fix an integral principal ideal of positive norm coprime to \(M_d\) in \(\mathbb Z[\sqrt2]\). Two generators differ, up to sign, by \(\varepsilon^j\), \(\varepsilon=1+\sqrt2\). If both are scalar modulo \(M_d\), the projective order of \(\varepsilon\) divides \(j\). The rational trace of \(\varepsilon/\bar\varepsilon\) is fixed, so (1) makes that order larger than every fixed power of \(d\). If the generator coefficients have absolute values at most \(\exp(O(d\log d))\), the two real embeddings and the nonzero integral norm bound \(|j|=O(d\log d)\). Eventually such an ideal has at most one scalar generator at these heights, up to sign. Ordinary ring-class principality, which permits multiplication by units of any height, alone does not provide a short relation.

## A single extra prime excludes all short relations

There is a different, elementary obstruction when the conductor is allowed to vary slightly. Let \(X=\exp(2d\log\log d)\). For a proportion tending to one of the primes \(X<q\le2X\), the projective relation lattice modulo \(q\) for the same \(d\) conic generators has **no** nonzero vector of 1-norm at most \(d\log d\). The same holds after adjoining \(q\), or \(q^2\), to the original \(M_d\). Here \(\log q=o(\log M_d)\). For the modulus \(qM_d\), the expression \(M/\operatorname{rad}(M)\) occurring in the certificate keeps exactly its previous value.

Indeed, for each nonzero exponent vector of length at most \(L=\lfloor d\log d\rfloor\), use conjugates for negative exponents and write \(\alpha\) for the resulting integral element. Its conjugate ratio is nontorsion, so its discriminant \(\Delta_\alpha=(\operatorname{Tr}\alpha)^2-4N\alpha=(\alpha-\bar\alpha)^2\) is a nonzero rational integer. The embedding bounds give \(\log|\Delta_\alpha|=O(L\log d)\). A prime of scalar reduction divides this integer and therefore at most \(O(1+L\log d/\log X)\) primes in the interval can arise from any one vector. There are at most \(2^d\binom{L+d}{d}\le[2e(1+L/d)]^d=\exp(d\log\log d+O(d))\) such vectors, by counting absolute values and signs. The prime number theorem gives \(\gg X/\log X\) available primes. Thus the exceptional proportion is at most \(\exp(-d\log\log d+O(d))\). The discriminant argument also applies to other varying quadratic fields provided the embeddings have size \(d^{O(1)}\) and nonzero exponent vectors have nonscalar products. This count concerns the enlarged moduli. The original initial-segment modulus could have a relation lost upon enlarging it.

## An effective estimate for a single generator in the original field

Even without the Subspace Theorem, for a conic generator \(\eta=b+a\sqrt2\) one obtains
\[
 \operatorname{ord}_{M_d}(\eta)
 \ge d^{\log(2310)-11/2-o(1)}.
\]
In particular the exponent exceeds two. The norm is an odd prime and both embeddings are of size \(d^{1/2+o(1)}\). At 2 the scalar coefficient of every positive power is odd. The valuation of the other coefficient of \(\eta^n\) equals \(v_2(a)+v_2(n)\): expansion proves it at odd \(n\), and squaring multiplies that coefficient by twice the odd scalar coefficient. Here \(v_2(a)\log2\le(1/2+o(1))\log d\).

At \(p=3,5,7,11\) the order \(m\) of the projective class divides \(4,6,6,12\), respectively. For \(m>1\) only the factor \(\Phi_m(\eta,\bar\eta)\) of \(\eta^m-\bar\eta^m\) can vanish modulo \(p\), since \(p\nmid m\). This homogeneous cyclotomic value is a rational integer and its absolute value is at most \(d^{\varphi(m)/2+o(1)}\). For \(m=1\) use \(2a\sqrt2\). The respective first-depth bounds after multiplication by \(\log p\) are at most \((1,1,1,2)\log d+o(\log d)\). Odd-prime lifting shows that the order contains at least \(p^{k_d-w_p}\) at each prime, where \(w_p\) is the first depth there. Multiplying these four divisibilities and the contribution from 2 gives the asserted exponent.
