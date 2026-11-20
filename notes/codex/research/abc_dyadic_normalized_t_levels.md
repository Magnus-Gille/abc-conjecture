# Residual level and traces for the 17-free packet

**For every dyadic \(n\ge8\), the positive integer \(t_n/17\) is not a proper power.** The unique exceptional initial cofactor is \(t_4/17=1\).

At a dyadic index \(n\ge4\) let \(t_n=u_n^2+16v_n^2\), and set \(T_n=t_n/17\). One has \(v_{17}(t_n)=1\) throughout. Thus \(T_4=1\) and \(T_8=241\). For \(n\ge8\), every prime exponent \(q\le151\) is already excluded from dividing all valuations of \(T_n\) by finite quotient-character checks. [Valuation proof and small-exponent certificates](abc_dyadic_t_simple_cover.md)

Since \(T_8=241\) is prime, take \(n\ge8\). For a putative \(T_{2n}=z^q\) with prime \(q>5\) and \(q\notin\{7,17,23,31,47\}\), the Frey representation constructed for the unnormalized third packet has exact prime-to-\(q\) level \(17408=17\cdot2^{10}\) if absolutely irreducible. Indeed use \(F=\mathbb Q(s),s^2=2\), \(a=w_n,b=2u_nv_n\), \(g=a^2+(4+2s)b^2\), \(A=4sb,B=sg\), and \(C:y^2=x^3+Ax^2+Bx\). Its discriminant and invariant are \(64B^2B^\sigma\) and \(16(B+4B^\sigma)\). At all odd places the fundamental relation \(gg^\sigma=17z^q\) and the coprimality away from 2 of the conjugate factors give good or multiplicative reduction. At 17 the two places of this split prime have minimal discriminant valuations one and two, since \(v_{17}(t_{2n})=1\). The residual Tate representation is therefore ramified with conductor exponent one. At every other odd place away from \(q\) it is unramified, and at \(q\) it is finite flat as in the unnormalized proof. [Isogeny, representation and finite-flat descent](abc_octic_dyadic_single_powers.md)

At the dyadic prime \(v_s(\Delta_C)=15\), \(v_s(B)=1\), and the singular point and its tangent are at the origin. Since \(a_6=0\) and \(v_s(b_8)=v_s(-B^2)=2\), Tate's algorithm terminates at III on this model. This gives a minimal model. Ogg's formula gives \(f_{(s)}(C)=15+1-2=14\). The induction conductor exponent is \(2\cdot3+14=20\), with the two constituent exponents equal by the duality argument for the Frey curve. Each is ten. Since \(v_s(c_4)=9\), the local \(j\)-invariant is integral and remains so on conjugation. Over \(F\) the potentially good inertia image has order dividing 24. Over \(\mathbb Q_2\) the quotient by this inertia subgroup has order at most two, so the image order divides 48. For \(q>5\) the conductor is preserved by reduction. For an absolutely irreducible residual representation, Serre's weight and conductor theorem gives a weight-two newform at the asserted exact level. The determinant character is \(\chi_8\epsilon_q\). The characteristic-zero nebentypus is \(\chi_8\) since the group of Dirichlet characters of the level has 2-power order.

Reducible representations are excluded independently of the modular forms calculation. The two residual Dirichlet characters after removing a cyclotomic factor have product \(\chi_8\). They are both unramified at 17. Ramification of either would force ramification of both because the product is unramified. Their total conductor exponent would then be at least two, exceeding the upper bound of one for the semisimplification. Their dyadic conductor exponents sum to at most ten, and if either exceeded five they would be equal because \(\chi_8\) has conductor exponent three. Hence they both have conductor dividing 32. At 47 they give equal signs since \(47^2\equiv1\bmod32\) and \(\chi_8(47)=1\). The reducible trace \(\pm48\) differs from the actual trace \(\pm12\) by a divisor of \(36\cdot60\), excluding all the prime exponents under consideration.

## Fixed trace constraints

Let \(P=[n/2]R\), and \(x(P)=(u_n/v_n)^2\). At a prime with \(b\) a unit the quadratic twist by \(1/b\) has coefficients
\[
       4s,\quad s(h+4+2s),\qquad
       h=(a/b)^2=\frac{x(P)^2+16x(P)+32}{4x(P)} .
\]
For split primes the invariant relevant below is the absolute trace, which is unchanged by quadratic twisting. For inert primes \(p\) in \(F\), every nonzero rational residue is a square over \(\mathbb F_{p^2}\), so this twist leaves the extension-field trace unchanged. If this trace is \(c_p\), then the trace of the two-dimensional descended representation obeys \(a_p^2=c_p-2p\), since its determinant at \(p\) is \(-p\).

| \(p\) | Dyadic abscissas modulo \(p\) starting with \(4R\) | Constraint |
|---:|---|---|
| 3 | 1 | \(a_3^2=-2\) |
| 5 | 1 | \(a_5=0\) |
| 7 | infinity | \(a_7=0\) |
| 23 | 13 | \(a_{23}^2=16\) |
| 31 | 0, infinity | \(a_{31}=0\) |
| 47 | 32 | \(a_{47}^2=144\) |

The equations in this table hold for the Frey characteristic-zero traces, and give congruences for any associated residual newform. At 3 and 5 one has \(h=1\), and counting on the normalized model gives traces 4 over \(\mathbb F_9\), 10 over \(\mathbb F_{25}\). At 7 and 31 the raw parameter \(b\) vanishes, and division of the twist coefficients by \(a,a^2\) gives \(y^2=x^3+sx\), of trace zero since the primes are three modulo four. At 23 one has \(h=3\), at 47 one has \(h=24\), giving absolute traces 4 and 12 by direct point count. The reduced curves are good at all six primes.

## Two exact Hecke eliminations

On the 512-dimensional exact-level newspace \(S^{\mathrm{new}}_2(17408,\chi_8)\), the dimensions after successive intersections with the kernels of \(T_3^2+2,T_5,T_7\) are \(20,4,0\). Thus no newform has even these first three traces exactly. As \(\chi_8(3)=\chi_8(5)=-1\) and \(\chi_8(7)=1\), its eigenvalues at 3 and 5 are purely imaginary, and at 7 are real, under every complex embedding. The operator
\[
             (T_3^2+2)^2-T_5^2+T_7^2
\]
has strictly positive eigenvalues, each at most \(100+20+28=148\) by the weight-two bound. Its determinant is a positive integer because it is the product of the norms of simultaneous integral eigenvalues. Write \(Z=(T_3^2+2)^2,\ V=-T_5^2,\ W=T_7^2\). For \(q>151\) any qualifying residual eigenform forces \(q\) to divide the determinants of both \(Z+V+W\) and \(Z+2V+3W\), since these operators vanish on its eigenline modulo a prime above \(q\). The exact rational-space matrix calculation gives
\[
\gcd\bigl(\det(Z+V+W),\det(Z+2V+3W)\bigr)
=2^{364}3^{28}5^4 7^{28}11^4 71^4 83^4 97^4 .
\]
This excludes every such \(q\). The finite quotient-character checks linked above handle all smaller primes.

An independent calculation on the same exact-level newspace uses only the split primes 7, 23, 31 and 47. For a normalized newform \(f\), with coefficient field \(K_f\), put
\[
M_f=\gcd\bigl(|N_{K_f/\mathbf Q}(a_7)|,|N(a_{23}^2-16)|,
                         |N(a_{31})|,|N(a_{47}^2-144)|\bigr).
\]
Congruence at a prime above \(q\) implies \(q\mid M_f\), even when \(q\) ramifies in the coefficient field. Every orbit gives \(M_f=2^e\). The table lists each pair \(([K_f:\mathbf Q],e)\) with its multiplicity.

| Degree | Exponent \(e\) | Number of orbits |
|---:|---:|---:|
|2|2|8|
|2|4|2|
|4|2|2|
|8|2|5|
|12|6|1|
|16|10|2|
|20|8|1|
|24|4|2|
|30|10|2|
|32|12|2|
|40|20|2|
|64|24|1|
|64|28|1|

The 31 degrees with multiplicities sum to 512. Consequently the argument with the split primes alone leaves only \(q=2,3,5,7,17,23,31,47\). Simple finite-orbit power characters at respective auxiliary primes \(7,7,31,127,103,47,9239,473479\) exclude all eight for every dyadic index \(n\ge8\). This completes the proof. [Trace and Hecke verifier](abc_dyadic_normalized_t_levels.py) · [Elementary residue certificate](abc_dyadic_t_simple_cover.py)
