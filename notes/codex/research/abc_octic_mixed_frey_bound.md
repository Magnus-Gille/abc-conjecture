# Bounding the exponent in perfect powers of the normalized mixed elliptic denominator

In the signed primitive mixed family let \(Y=s^2+2t^2,\ V=(s-t)^2+t^2\), with \(s\) odd, \(t>0\) even. Suppose both are squares and \(Y=81w^{2q}\), where \(w>1\) and \(q\) is prime. Then
\[
                         q\le37.
\]
In particular there are only finitely many such slopes even when the exponent is allowed to vary. The exponent bound is explicit. Finiteness for each remaining fixed prime uses Faltings and gives no height bound here. This concerns a common divisor of the prime exponents of \(\sqrt Y/9\).

## Reduction to two coprime powers

Use the full odd index \(N\) and the curve \(E':y^2=x^3+16x^2+32x\) with \(R_0=(-8,16)\). Write \(B_k\) for the positive square root of the abscissa denominator at \(kR_0\). On the full family, \(B_N=\sqrt{Y_N}\). Reduction of \(R_0\) has order three modulo 3, so \(3\mid B_N\) implies \(N=3m\). Put \(A_m=B_{3m}/9\). [Full parametrization](abc_octic_full_mixed_orbit.md) · [Denominator identity](abc_octic_mixed_three_factors.md)

Write \(m=3^e n\), \(3\nmid n\). At each prime \(p\mid A_n\) the valuation is unchanged upon passing to \(A_m\): the denominators are odd, \(A_n\) is a 3-unit, and the good odd-prime formal lifting increments by \(v_p(3^e)=0\). Hence \(A_m\) a \(q\)-th power forces \(A_n\) a \(q\)-th power. The case \(n=1\) only gives a nontrivial index when \(e>0\). In that case \(A_3=B_9/9=2211\cdot13411\) has \(v_{11}=1\), unchanged at every \(3^e\) with \(e\ge1\). At \(m=1\) the normalized denominator is 1, outside the hypothesis.

For \(3\nmid n,\ n>1\) put \(b=\sqrt{Y_n}\), \(v=\sqrt{V_n}\). The three-factor identity yields \(A_n=bC_1C_2\), with positive, pairwise coprime factors prime to 6, where
\[
  3C_1=b^4-4b^2v^2+6v^4,\qquad 3C_2=b^4+4b^2v^2-2v^4 .
\]
The proof uses tripling and \(3\nmid n\); it does not require \(n\) to be prime for the displayed formulas or coprimality. Consequently \(b=u^q,\ C_2=z^q\) for coprime odd positive \(u,z\) prime to 3. Here \(b>1\) because the ambient index \(n>1\) has a nondegenerate primitive slope. With \(h=(b^2-v^2)/3\) we get
\[
                    u^{4q}-z^q=6h^2 .
\]
In the next paragraphs \(s,t\) denote the primitive coordinates at the **ambient index \(n\)**, so \(b^2=s^2+2t^2\), \(v^2=b^2-2st\) and \(3h=2st\).

## Exact level of the Frey representation

Suppose \(q>37\). Take the elliptic curve
\[
  F:\quad y^2=x^3+12h x^2-6z^q x .
\]
It has rational 2-torsion and hence a rational cyclic 2-isogeny. Write \(a_2=12h,\ a_4=-6z^q\). Then \(a_2^2-4a_4=24u^{4q}\), and \(\Delta=16a_4^2(a_2^2-4a_4)\). At \(p>3\) dividing \(uz\) the model is multiplicative and minimal: \(c_4=16(a_2^2-3a_4)\) is a unit by coprimality and the equation. Its discriminant valuation is a multiple of \(q\). At every \(p>3\) with \(p\nmid uz\) the curve has good reduction. As \(u>1\), a multiplicative prime exists and \(F\) cannot have complex multiplication, since CM \(j\)-invariants are algebraic integers.

At 2 and 3 the model is minimal since the discriminant valuations are 9 and 3, both below 12. Both \(a_2,a_4\) are divisible by the residue prime and \(a_6=0\); the singularity and tangent are already at the origin in Tate's algorithm. One has \(v_p(b_8)=v_p(-a_4^2)=2\), so the Kodaira type is III at each prime. Ogg's formula gives conductor exponents 8 and 2. The \(j\)-invariant is integral at both places: at 2, \(v_2(c_4)=5\); at 3, \(v_3(c_4)\ge2\). Thus the inertia actions are potentially good with finite inertia of order dividing 24. For \(q>37\) the mod-\(q\) representation retains the same conductor exponents. Indeed invariants of every ramification subgroup commute with reduction for an inertia action of order prime to \(q\).

Lemos's theorem gives that the mod-\(q\) representation of \(F\) is surjective: it applies to every non-CM elliptic curve over \(\mathbb Q\) with a nontrivial rational cyclic isogeny for all primes \(q>37\). In particular the representation is absolutely irreducible. Modularity and weight-two level lowering now give a trivial-character newform of exact level \(2^8 3^2=2304\) and a place over \(q\) giving the residual representation. More explicitly, the multiplicative primes away from \(q\) disappear because \(q\mid v_p(\Delta_{\min})\). At \(q\) the representation is finite flat if \(F\) has good reduction; the same finite-flat criterion holds for multiplicative reduction with \(q\mid v_q(\Delta_{\min})\), after an unramified extension in the nonsplit case. This gives Serre weight two. The exact prime-to-\(q\) Artin conductor comes from 2 and 3 as computed above. The determinant forces the character to be trivial on reduction, and a character of conductor dividing 2304 has order dividing \(\varphi(2304)=768\), prime to \(q\), so it is trivial in characteristic zero as well. [Lemos, *Serre's Uniformity Conjecture for Elliptic Curves with Rational Cyclic Isogenies*](https://arxiv.org/abs/1702.01985) · [Weight and level formulation used for Frey curves](abc_frey_fixed_primes.md)

## Four small primes determine the only possible form

In terms of the ambient pair the coefficients are \(a_2=8st,\ a_4=16s^2t^2-6(s^2+2t^2)^2\). Scaling \((s,t)\) by a residue-field unit gives an isomorphic curve because these two coefficients are homogeneous of degrees two and four. At each of the primes in the table enumerate the projective line, retaining slopes for which both \(s^2+2t^2\) and \(s^2-2st+2t^2\) are squares including zero. At every retained slope the reduced Frey curve is good. Counting its points gives the following complete trace sets. The last column counts surviving Galois orbits of newforms.

| Test prime | Possible Frey traces | Orbits remaining |
|---:|---|---:|
| 5 | \(-2,2\) | 8 |
| 7 | \(0\) | 4 |
| 17 | \(-6,4,8\) | 2 |
| 29 | \(-6,-2,6,10\) | 1 |

The weight-two newspace has dimension 38, with 16 rational Galois orbits, nine quadratic orbits, and one quartic orbit. For each candidate \(f\) and test prime \(p\) the verifier computes the algebraic integer \(V_f=\prod_{a}(a_p(f)-a)\) over the allowed traces. When \(V_f\ne0\), the prime \(q\) would have to divide the absolute field norm of \(V_f\); every eliminated orbit has this norm supported on primes at most 37. This computation includes the nonrational coefficient fields. The survivor agrees with the newform of \(F_0:y^2=x^3-6x\) through coefficient 768, the usual weight-two Sturm bound for \(\Gamma_0(2304)\). Its conductor is 2304 as well. [PARI/GP verifier](abc_octic_mixed_frey_bound.gp)

The curve \(F_0\) has complex multiplication by \(\mathbb Z[i]\). Its mod-\(q\) image lies in a Cartan normalizer for every \(q>37\), so it cannot be isomorphic to the surjective mod-\(q\) representation of \(F\). This proves the stated bound. For the resulting finite list of primes \(q\), the fixed-power equations \(Y=81w^{2q},\ V=v^2\) have weights \(2(1-1/(2q))+2(1-1/2)=3-1/q>2\). The disjoint-branch covering argument and Faltings give finiteness for each, hence also for their union. [Fixed-power finiteness](abc_octic_power_patterns.md)
