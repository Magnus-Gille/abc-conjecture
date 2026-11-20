# Perfect powers in the fourth factor of the dyadic triple

Let \(s_n=u_n^2+8v_n^2\) in the dyadic recurrence with \(u_4=v_4=1,w_4=7\). Then \(s_4=9\). For **every** \(n=8,16,32,\ldots\), \(s_n\) is not a perfect power. Together with the other three cusp factors, this means that none of the four independent sources of radical loss in the primitive triple can be a perfect power at any index \(n\ge8\). A fixed fractional radical loss through mixtures of different exponents remains possible. [Triple and four-factor criterion](abc_dyadic_direct_triple.md) · [Proof for the other three factors](abc_octic_dyadic_single_powers.md)

## An imaginary quadratic Frey curve

The base case \(s_8=2529=3^2\cdot281\) follows directly. For \(m\ge8\), substitution gives \(s_{2m}=w_m^4+128(u_mv_m)^4\). Suppose \(s_{2m}=z^q\) for a prime \(q>5\). Put \(a=w_m,\ b=8u_m^2v_m^2\), so \(a^4+2b^2=z^q\), with \(a,b\) coprime, \(a\) odd and \(b\) even. Let \(F=\mathbb Q(\tau)\), \(\tau^2=-2\), let a bar denote conjugation, and set
\[
 g=a^2+b\tau,\qquad C:\quad y^2=x^3+4ax^2+2gx.
\]
The norm of \(g\) is \(z^q\). Away from 2 the ideals of \(g,\bar g\) are coprime. The invariants are
\[
 \Delta=2^9g^2\bar g,\qquad c_4=16(16a^2-6g).
\]
At a prime above an odd divisor of \(g\) or \(\bar g\), \(c_4\) is a unit, since \(g\equiv0\) or \(2a^2\), respectively. Thus every odd bad prime is multiplicative with minimal discriminant valuation divisible by \(q\). The quotient by \((0,0)\) has coefficients \(-8a,8\bar g\). Dividing its coordinates by \(\tau^2,\tau^3\) yields the conjugate curve. The resulting isogeny \(\mu:C\to\bar C\) has multiplier \(\tau\) on invariant differentials, so \(\bar\mu\mu=[2]\).

The construction over \(G_{\mathbb Q}\) in the companion proof applies with \(\delta=\sqrt2\). On \(G_F\) take the ordinary Tate-module action and on the other coset use the conjugate isogeny divided by \(\delta\) after the Galois action. Its determinant is the cyclotomic character: the isogeny multiplies the pairing by \(2\) and the scalar multiplies it by \(1/\delta^2=1/2\). This makes the two-dimensional representation \(\rho\) odd. The induced representation splits as \(\rho\oplus(\rho\otimes\chi_{-8})\). At odd primes away from \(q\), the residual representation is unramified by the discriminant valuation calculation. At \(q\), it is finite flat by good reduction or the multiplicative Tate-parameter test, since the parameter class modulo \(q\)-th powers is represented by a unit. These statements descend from the unramified local extension by the finite-flat descent argument in the companion proof. [Tate-module construction and finite-flat descent](abc_octic_dyadic_single_powers.md)

At the prime \((\tau)\) the displayed model has \(v_\tau(\Delta)=18,\ v_\tau(c_4)=10\), so inertia has finite image by potential good reduction. Its conductor exponent over \(F\) is at most 14. If the integral model is nonminimal, the minimal discriminant valuation is at most six and Ogg's formula suffices. For a minimal model the singular point and tangent are at the origin, with \(a_6=b_6=0,\ v_\tau(b_8)=v_\tau(-(2g)^2)=4\). The first tests of Tate's algorithm exclude types II, III, IV. All remaining additive types have at least five geometric components, giving the bound by Ogg's formula. Induction to the rationals gives the sum of the constituent conductor exponents at most \(2\cdot3+14=20\).

Each constituent has exponent at most ten. Their determinants are unramified on dyadic inertia, and their inertia images are finite. A nontrivial finite subgroup of \(\mathrm{SL}_2\) in characteristic zero has no invariant vector, since a matrix fixing such a vector would be both unipotent and of finite order. For either ramified constituent with last upper break \(h\ge0\), its Artin conductor is therefore \(2(1+h)\), including the tame case \(h=0\). The twisting character has last break two. If either last break exceeds two, both representations have the same last break, and their conductors are equal. Otherwise both exponents are at most six. Reduction modulo \(q\) does not increase the conductor.

## Two local traces and the complete modular space

At the inert prime 47 the orbit of \(P=[m/2]R\), for \(R=(-8,16)\), alternates between \((32,11)\) and \((32,36)\). Thus \(b/a^2=8(x(P)/y(P))^2=4\bmod47\), and \(a\) is a unit there. Over \(\mathbb F_{47^2}\) the residue of \(a\) is a square, and the good curve is isomorphic to \(y^2=x^3+4x^2+2(1+4\tau)x\). Its trace is \(4\) by counting points. Since the determinant at rational Frobenius is 47, the rational descended trace \(t\) satisfies \(t^2-94=4\), or \(t^2=98\).

For an absolutely irreducible residual representation, the weight and level form of Serre modularity gives weight two, level dividing \(1024\), and trivial character. Here finite flatness gives the weight, and all Dirichlet characters at this level have 2-power order, so an odd residual characteristic distinguishes them. Every possible system in characteristic zero occurs in the full 105-dimensional space \(S_2(\Gamma_0(1024))\). Its exact Hecke characteristic polynomial \(P_{47}\) satisfies
\[
 |\operatorname{Res}(P_{47},X^2-98)|
 =2^{105}3^8 5^8 7^{114}17^{24}31^8 .
\]
When \(q\ne47\), comparison of traces forces \(q\) to divide that integer.

In the reducible case the two characters are \(\theta,\epsilon_q\theta^{-1}\) by finite flatness at \(q\), with \(\theta\) of 2-power conductor. Its conductor exponent equals its inverse's exponent and their sum is at most ten. Thus \(\theta\) has conductor dividing 32. At 47 its value is a sign because \(47^2\equiv1\bmod32\). Comparing the squared trace gives \(q\mid48^2-98=2\cdot1103\) when \(q\ne47\). The remaining candidate 1103 is prime and is excluded at 17. Indeed 17 splits in \(F\), and all the \(s_{2m}\) are units there: the recurrence preserves \(u_m^2\equiv v_m^2\ne0\bmod17\), starting at \(m=4\). Thus the descended trace at 17 is an integer in \([-8,8]\) by good reduction and the Hasse bound. The reducible trace would be \(\pm18\bmod1103\) because \(17^2\equiv1\bmod32\). This is impossible.

It remains to test \(q=2,3,5,7,17,31,47\). Starting at \((31,14,2273)\), iterate the signed homogeneous doubling formula modulo the auxiliary prime until the first repeated state. The square-coordinate expression \(u^2+8v^2\) is unaffected by the signs. Every residue in each orbit is nonzero and has nontrivial \(q\)-th-power character. This covers every index, including any nonperiodic prefix.

| \(q\) | 2 | 3 | 5 | 7 | 17 | 31 | 47 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Auxiliary prime | 23 | 7 | 31 | 113 | 2687 | 311 | 473479 |
| Distinct states | 11 | 2 | 4 | 3 | 41 | 61 | 100 |

[Reproducible verifier for the trace, resultant and periodic tests](abc_dyadic_fourth_factor.py)
