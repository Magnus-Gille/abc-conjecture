# A 3-adic density bound for primes in the two residual quartics

On the elliptic slice \(F_0(x,y)=-2z^2\), let \(\mathcal P\) be the primes that occur in \(F_+F_-\) at any odd index of the chosen orbit. Their upper natural density is at most
\[
                        \frac{53787}{378560}=0.1420831572\ldots .
\]
The displayed fraction is the density of a necessary local test, incorporating all powers of 3 in two rational elliptic groups. Realization by an actual index imposes conditions at the other prime powers dividing the group orders. [Marked divisors and the two rational points](abc_eisenstein_slice_marked_divisors.md)

Use \(E':v^2=u^3-576u,\ P'=(-8,-64)\) and \(E_*:v^2=u^3-192u,\ Q_*=(49,-329)\). For each \(p\in\mathcal P\), \(p\ge5\), one has \(p\equiv\pm1\bmod24\) and there is a fourth root \(h\) of 3 in \(\mathbb F_p\) with
\[
              [2n]P'=\iota_h(Q_*)\pmod p,\qquad
              \iota_h(u,v)=(h^2u,h^3v).
\]
We retain the necessary condition on the 3-primary parts of the two points, allowing an arbitrary integral multiple of \(P'\) there. At \(p\equiv-1\bmod24\) an \(h\) always exists, and the two choices give opposite points. At \(p\equiv1\bmod24\) the fourth-root condition means splitting completely in \(B=\mathbb Q(i,\sqrt2,\sqrt[4]3)\), of degree 16, and the four choices differ by units \(\{\pm1,\pm i\}\). Indeed \(\mathbb Q(i,\sqrt[4]3)\) has dihedral group of order eight and maximal abelian subfield \(\mathbb Q(i,\sqrt3)\). In particular it does not contain \(\sqrt2\).

## The simultaneous translation groups

Put \(K_1=B(E'[3],E_*[3])\). This is \(B(E'[3])\), since the curves are isomorphic over \(B\). Write \(h=\sqrt[4]3>0\) and \(\mu=(\sqrt3+1)/(\sqrt2h)\). The third division polynomial shows that \(24\mu\) is a 3-torsion abscissa: \(\mu^2=1+2/\sqrt3\). At this abscissa the ordinate square is \((32h^5)^2\mu\). If \(\mu\) were a square in \(B\), its square root at the chosen embedding would be real and in \(\mathbb Q(\sqrt2,h)\). The real embedding \(h\mapsto-h\) fixing \(\sqrt2\) takes \(\mu\) to a negative number, excluding this. Applying \([i]\) to the chosen point gives a second independent 3-torsion point, as \(X^2+1\) is irreducible over \(\mathbb F_3\). Thus \(K_1=B(\sqrt\mu)\) has degree 32 over \(\mathbb Q\) and the nonidentity automorphism over \(B\) acts as \(-1\) on both torsion modules.

Let \(M_1/K_1\) adjoin the two fibers of multiplication by three above \(P'\), \(Q_*\). Its Galois group acts by translations and is the full product
\[
                 E'[3]\times E_*[3]\simeq\mathbb F_3^4 .
                 \tag{1}
\]
Here are explicit checks of the independence needed for (1). At 11 both curves have 12 points and \([4]P'=(3,2)\), \([4]Q_*=(5,1)\) modulo 11. Thus neither rational point is three times a rational point. They remain indivisible over \(K_1\): tracing a hypothetical third part down to \(\mathbb Q\) would divide \([K_1:\mathbb Q]P'\) or \([K_1:\mathbb Q]Q_*\) by three, and the degree is coprime to three. Both projections of the translation group are therefore nonzero. They are invariant under the full rational Galois action, since both points are rational. At 5 the two Frobenius traces are \(-2,-4\), respectively, with both characteristic polynomials irreducible modulo three and with different traces modulo three. The two modules are consequently irreducible and nonisomorphic. An invariant subspace of their product that surjects onto both must be the product: otherwise the kernels of both projections are zero, giving an equivariant isomorphism. This proves (1).

Let \(K_\infty=B(E'[3^\infty],E_*[3^\infty])=B(E'[3^\infty])\). Over \(B\) this is abelian: the action on the Tate module commutes with \([i]\) and is by units in \(\mathcal O_3=\mathbb Z_3[i]\), the unramified quadratic integer ring. The intersection \(M_1\cap K_\infty\) is \(K_1\). Indeed its Galois group over \(B\) is abelian, whereas a lift of the nonidentity element of \(\operatorname{Gal}(K_1/B)\) conjugates all translations in (1) to their negatives. No nonzero quotient of this elementary 3-group permits both actions. It follows that over \(K_\infty\) the simultaneous Kummer translations on the Tate modules still surject modulo three. Their image is a closed additive subgroup of \(\mathbb Z_3^4\); reduction and Nakayama's lemma therefore give the full product at every depth. In particular conditional on any allowed linear actions and on the action on \(B\), the two translation vectors are independent and uniform at every finite level.

## The linear action at split primes

The linear image over \(B\) is exactly \(\{\pm1\}(1+3\mathcal O_3)\). The calculation of \(K_1\) gives the two possible residues. The prime 313 splits completely in \(B\), as \(313\equiv1\bmod24\) and \(3^{78}\equiv1\bmod313\). Counting the points on \(E'\bmod313\) gives trace 26. Thus the two conjugate Gaussian Frobenius scalars \(13+12i,13-12i\), of norm 313, occur in the image. Normality of \(B/\mathbb Q\) allows conjugation by complex conjugation. Under the 3-adic logarithm the two scalars give, after dividing by 3 and reducing modulo 3, the two independent vectors \(4+4i,\ 4-4i\). They generate \(3\mathcal O_3\) topologically before the division. This proves the claim.

## Counting the surviving primes

For a good prime \(p\ne3\), on the fixed linear Frobenius fiber \(\sigma\) the Kummer translation vector represents the reduction of the point in \(T_3E/(\sigma-1)T_3E\). This quotient identifies with the 3-primary group of the finite reduction. One can see the finite-level version from the connecting map for multiplication by \(3^j\): over a finite field the first Galois cohomology of the elliptic curve vanishes, and for its finite torsion the Frobenius cohomology is the cokernel of \(\sigma-1\). The two uniform vectors project independently to their respective quotients by (1) and its lift. These identifications are natural for the twist isomorphism and the CM action. Chebotarev on each finite affine torsion extension therefore computes the probabilities below from the indicated uniform distributions.

At \(p\equiv-1\bmod24\) both curves have trace zero by pairing \(u,-u\) in their character sums. The 3-torsion Frobenius eigenvalues are \(1,-1\bmod3\), so the 3-primary groups are cyclic, of common order \(3^a\), \(a=v_3(p+1)\). Independent uniform points in a cyclic group of this order satisfy \(\operatorname{ord}(Q_*)\mid\operatorname{ord}(P')\) with probability
\[
              \frac34+\frac{1}{4\cdot9^a}.
\]
Indeed, for a given \(P'\) the favorable subgroup has order \(\operatorname{ord}(P')\); sum this over the numbers \(\varphi(3^j)\) of elements of each order. Conditional on this prime class, the prime number theorem in fixed progressions gives \(\Pr(a=k)=2/3^k\), \(k\ge1\). The resulting survival fraction within the class is \(10/13\).

At \(p\) split completely in \(B\), the linear image calculation gives \(a=v_3(\sigma-1)=0\) with probability \(1/2\). Conditional on \(a\ge1\), \(\Pr(a=k)=8/9^k\), \(k\ge1\), since each next congruence condition in \(\mathcal O_3\) has index nine. The quotient group for a given \(a\) is \(\mathcal O_3/(3^a)\simeq(\mathbb Z/3^a)^2\). Given the two independent uniform vectors \(t,q\) after one twist identification, the necessary condition is
\[
                  q\in\langle t\rangle\ \cup\ i\langle t\rangle .
\]
When \(t\) has order \(3^j\), these two subgroups intersect only at zero: after removing the common 3-power from \(t\), its leading vector and its \(i\)-multiple are independent modulo 3. Their union therefore has \(2\cdot3^j-1\) elements. There are \(8\cdot9^{j-1}\) possible vectors of order \(3^j\) for each \(j\ge1\), and one zero vector. Averaging gives the survival probability
\[
        \frac{24}{13}3^{-a}-9^{-a}+\frac{2}{13}81^{-a}.
\]
It equals one for \(a=0\). Its average over \(a\ge1\) is
\[
           \frac{192}{13\cdot26}-\frac8{80}
                 +\frac{16}{13\cdot728}=\frac{5557}{11830}.
\]
In both prime classes the tail with \(a\) above a fixed cutoff has density tending to zero, by the displayed geometric laws. Finite-level Chebotarev therefore gives natural density for the full 3-primary test. The two disjoint classes contribute in total
\[
          \frac18\frac{10}{13}
             +\frac1{32}\left(1+\frac{5557}{11830}\right)
          =\frac{53787}{378560}.
\]
This constrains the possible prime support of the independent quartic layer; it does not bound the heights or valuations of its individual prime factors.
