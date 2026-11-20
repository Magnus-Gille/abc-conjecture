# An unbounded gain over the square root of the logarithmic height

Write \((A,B,C)=(a^4,3b^2,4w^4)\) for the primitive quartic triple at an odd index \(n\) on \(E:y^2=x^3-36x\), with \(G=(-3,9)\). Set \(R=\operatorname{rad}(ABC)\). Along indices of the form \(n=3^{i+1}11^j\),
\[
 \limsup_{i,j\to\infty}\frac{C}{nR}=\infty,\qquad
 \limsup_{i,j\to\infty}\frac{C}{R\sqrt{\log C}}=\infty.
\]
Both exponents can be required to exceed any prescribed bound. For every such index \(n>1\), the elliptic denominator \(w\) also fails to be a perfect power of any exponent. [Perfect-power exclusion at smooth indices](abc_full_quartic_perfect_power_census.md)

For any \(T>0\) and fixed nonnegative integers \(I,J\), the inequality \(C/(nR)>T\) can hold throughout an entire translate of the integer rectangle \([0,I]\times[0,J]\) in the exponent pair. Indeed the finitely many multiplication maps \([3^u11^v]\) with \(0\le u\le I,0\le v\le J\) are continuous and fix the circle identity. Choose a common neighborhood of that identity mapped into \(\{P:|Y(P+(0,0))|<6/T\}\) by all these maps, then apply the same density theorem there.

## Repeated primes at indices supported on a finite set

Write \(B_m\) for the square root of the reduced denominator of \(X(mG)\), and put \(D=3B_{2n}/R\). The identities \(B_{2n}=2|ab|w\) and \(Y(nG)=9ab/w^3\) give
\[
                      C/R=6D/|Y(nG)|.
\]
At \(n=3\) one has \(B_6=2\cdot23\cdot1551\cdot37\) and \(1551=3\cdot11\cdot47\). The formal group at each of \(p=3,11,23,37,47\) gives \(v_p(B_{6m})=v_p(B_6)+v_p(m)\). Indeed \(6G\) is in the kernel of reduction and the formal logarithm preserves the valuation of its formal parameter at these odd primes. The extra factor of 3 in \(3B_{2n}\) accounts for the initial 3 in \(n=3m\). Thus \(n\mid D\) whenever \(3\mid n\) and the prime factors of \(n\) all belong to \(\{3,11,23,37,47\}\). [Coordinates and bad-prime calculation](abc_full_quartic_first_depth_census.md)

## A real return with both prime exponents growing

Take the real identity component of \(E\) with its circle group structure. The point \(H=G+(0,0)=(12,36)\) has infinite order, hence its circle coordinate is irrational. At odd \(n\) the point \(nG\) equals \(nH+(0,0)\). By Furstenberg's topological theorem, for multiplicatively independent integers \(r,s>1\) and irrational \(\xi\), the set \(\{r^is^j\xi\bmod1:i,j\ge0\}\) is dense. Apply it with \(r=3,s=11\) and initial point \(3^{I+1}11^J H\) for any \(I,J\). This proves that in every such tail \(nG\) comes arbitrarily close to \((0,0)\), where \(Y\) vanishes. Using \(n\mid D\) proves the first limsup. The second follows since \(\log C=4\widehat h(G)n^2+O(1)\). See H. Furstenberg, *Disjointness in ergodic theory, minimal sets, and a problem in Diophantine approximation*, Math. Systems Theory **1** (1967), 1–49. [Quartic height comparison](abc_full_quartic_signature.md)

## Explicit certificates

For numerical lower bounds one can use the real coordinate from the finite-index calculations. Write \(K=K(1/2)\) for the complete elliptic integral with parameter \(1/2\) and \(\alpha=F(\pi/4\mid1/2)/K\) for the corresponding rotation. The inequality obtained by bounding \(|Y'|\) between a point of the real orbit and the nearest zero is
\[
                \frac{C}{nR}\ge\frac{D/n}{2\sqrt3 K\|n\alpha\|}.
\]
Here \(\|\cdot\|\) is the distance to the nearest integer. The examples below use exact factorization of the index and interval arithmetic for the two elliptic integrals. They need no factorization of a coordinate of the triple. [Derivation of the derivative bound](abc_full_quartic_real_radical.md) · [Real-ball verifier](abc_full_quartic_smooth_index_radical.py)

| Index \(n\) | Certified strict lower bound for \(C/(nR)\) |
|---|---:|
| \(3^{13}11\) | 138 |
| \(3^5 23^3 37^2 47^4\) | 9,857 |
| \(3\cdot11^5 23^5 47^8\) | 15,297 |
| \(3^{20}23^3 47^{13}\) | 142,685 |

The proof supplies no positive constant \(\delta\) with \(C/R\ge C^\delta\) infinitely often. The local factors accounted for by multiplying the index contribute only \(\log n\) in log scale. A fixed-exponent abc violation in this family requires positive-proportion losses in the prime radicals relative to the quadratic height. [Exact criterion for the four coordinates](abc_full_quartic_twin_and_mixed_valuations.md)
