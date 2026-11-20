# No dyadic packet is a proper perfect power

Let \(R=(-8,16)\) on \(E':y^2=x^3+16x^2+32x\). At each power of two \(n\ge4\), write \(x([n/2]R)=u_n^2/v_n^2\), \(|y([n/2]R)|=u_nw_n/v_n^3\), with the positive, pairwise coprime integers of the dyadic recurrence. Then
\[
              \gcd\{v_p(w_n):p\mid w_n\}=1
                    \qquad\text{for every }n=4,8,16,\ldots .
\]
In particular every prime-power value of \(w_n\) is prime. The proof gives a finite certificate for all exponents and indices. It leaves open whether a packet can have all its prime exponents at least two with gcd one. [Packet construction and recurrence](abc_octic_dyadic_fermat_audit.md) · [Exact finite verifier](abc_octic_dyadic_single_powers.py)

## One packet and a quadratic Frey curve

The initial packets are \(w_4=7,w_8=2273\), both prime. Suppose \(n\ge8\) and \(w_{2n}=z^q\), with \(q\) prime and \(z>1\). Set
\[
       a=w_n,\qquad b=8u_n^2v_n^2,\qquad
       a^4-2b^2=z^q .
\]
Here \(a,z\) are odd and \(\gcd(a,b)=1\). Over \(F=\mathbb Q(s)\), \(s^2=2\), write \(\sigma s=-s\), \(g=a^2+bs\). The ideals \((g),(g^\sigma)\) are coprime away from 2 because any odd common divisor would divide both \(a\) and \(b\). Both elements are units at the unique prime over 2, and \(gg^\sigma=z^q\). Consider
\[
 C:\quad y^2=x^3+2as x^2+g x,\qquad
 \Delta_C=64g^2g^\sigma,\qquad c_4=16(8a^2-3g).
\]
At an odd divisor of \(g\), the discriminant valuation is a multiple of \(q\) and \(c_4\) is a unit. At an odd divisor of \(g^\sigma\), use \(g\equiv2a^2\) for the same conclusion. Thus all odd bad reductions are minimal multiplicative, with minimal discriminant valuation a multiple of \(q\); all remaining odd places are good. At the dyadic place the displayed integral discriminant has normalized valuation 12, giving \(f_{(s)}(C)\le12\) by Ogg's formula \(f=v(\Delta_{\min})+1-\#\{\text{geometric fiber components}\}\).

The two-isogeny with kernel \(\{O,(0,0)\}\) has target with coefficients \((-4as,4g^\sigma)\). Dividing the quotient abscissa and ordinate by \(s^2,s^3\) gives a degree-two isogeny \(\mu:C\to C^\sigma\) defined over \(F\). With invariant differentials \(dx/(2y)\) on the two displayed models, the normalized quotient pulls the target differential back with factor one, and the scaling contributes \(s\). Consequently \(\mu^\sigma\mu\) acts on the differential by \(s\sigma(s)=-2\); hence \(\mu^\sigma\mu=[-2]\) in characteristic zero.

## A two-dimensional representation over the rationals

Write \(\eta=\chi_8\) for the quadratic character of \(F/\mathbb Q\) and \(\epsilon_q\) for the \(q\)-adic cyclotomic character. For \(q>5\), choose \(\delta=\sqrt{-2}\in\overline{\mathbb Q}_q\). Extend \(V_q(C)\) after scalar extension from \(G_F\) to a two-dimensional representation \(\rho\) of \(G_{\mathbb Q}\). On \(G_F\) take the ordinary action. For \(h\notin G_F\), first apply \(h:V_q(C)\to V_q(C^\sigma)\), then apply \(\mu^\sigma/\delta\). This is a representation by \(\mu^\sigma\mu=[-2]=[\delta^2]\). The lattice \(T_q(C)\) after extending scalars to \(\mathcal O_{\mathbb Q_q(\delta)}\) is stable since \(2\) and \(\delta\) are \(q\)-units. Functoriality of the Weil pairing gives
\[
          \det\rho=\epsilon_q\eta .
\]
Indeed the degree-two isogeny multiplies the alternating form by two, and division by \(\delta\) scales it by \(1/\delta^2=-1/2\). The residual representation is odd because \(F\) is real.

At 2 the induction conductor formula for \(V_q(C)\) gives an exponent at most \(2\,v_2(\operatorname{disc} F)+f_{(s)}(C)\le6+12=18\); the residue degree at 2 is one. The induction decomposes as \(\rho\oplus(\rho\otimes\eta)\). As \(\rho\otimes\eta\simeq\rho^\vee\otimes\epsilon_q\), the two summands have equal conductor at 2. Thus \(f_2(\rho)\le9\), and the residual conductor exponent is bounded by nine as well. At odd \(p\ne q\), inertia lies in \(G_F\) because the quadratic extension is unramified. The Tate-curve criterion at multiplicative primes, using \(q\mid v(\Delta_{\min})\), and good reduction elsewhere give that the residual representation is unramified there.

The residual representation is finite flat at \(q\). Over \(F_v\) this follows from good reduction or the Tate-curve criterion \(q\mid v(\Delta_{\min})\) in the multiplicative case, after an unramified extension for nonsplit multiplicative reduction. In the latter case the class of the Tate parameter in \(F_v^\times/(F_v^\times)^q\) is represented by a unit. The descent to \(\mathbb Q_q\) is unramified: finite flat models killed by \(q\) over an unramified extension of \(\mathbb Q_q\) are fully faithful on the generic fiber for \(q>2\) by Raynaud's theorem (absolute ramification one is less than \(q-1\)). Thus the Galois descent data on the generic representation extend uniquely to the model, and finite flat descent applies. One can take two copies of the elliptic model when extending the residual scalars before descent. Only the prime 2 ramifies in the coefficient field \(\mathbb Q(\delta)\).

## The trace at 47

At the place \(s\equiv7\pmod {47}\), normalize the Frey curve by the quadratic twist by \(a\); this is a unit at 47. Indeed each prime in \(w_n\), for \(n\ge8\), is \(1\bmod8\), and the same holds for \(w_{2n}\). On this twist the coefficients at \(x^2,x\) are \(2s,1+(b/a^2)s\), after an integral unit scaling. Since
\[
           b/a^2=8(x(P)/y(P))^2,\qquad P=[n/2]R,
\]
one needs just two points of \(E'(\mathbb F_{47})\). Starting with \(4R=(32,11)\), doubling interchanges it with \((32,36)\). Both have \(b/a^2=4\) modulo 47. Counting on \(y^2=x^3+14x^2+29x\) gives trace \(-2\). The actual Frey curve therefore has trace in \(\{-2,2\}\). The prime 47 splits in \(F\), so the same is true of \(\rho(\operatorname{Frob}_{47})\). The comparison below assumes \(q\ne47\); exponent 47 is included in the final finite test.

If \(\bar\rho\) is reducible over \(\overline{\mathbb F}_q\), its semisimplification consists of two characters. Finite flatness at \(q\) gives inertia characters \(1,\bar\epsilon_q\) in the reducible case: a one-dimensional character of the local Galois group has niveau one, the finite flat tame inertia weights are zero or one, and their sum is one by the determinant. Thus the global characters can be written \(\theta_1,\bar\epsilon_q\theta_2\), where the \(\theta_i\) are unramified outside 2 and \(\theta_1\theta_2=\eta\). These are Dirichlet characters of 2-power conductor and their conductor exponents at 2 sum to at most nine. If one exponent exceeded four, it would exceed the exponent three of \(\eta\) and the other character would have the same exponent, giving a sum of at least ten. Hence the individual conductors divide 16. Since \(47\equiv-1\bmod16\) and \(\eta(47)=1\), the two finite character values are the same sign, giving residual trace \(\pm48\). Comparing with \(\pm2\) shows \(q\mid 46\cdot50\). For \(q>5\) this leaves only \(q=23\).

If \(\bar\rho\) is absolutely irreducible, the proved Serre modularity conjecture with its weight and level refinement gives a weight-two newform of prime-to-\(q\) level dividing \(2^9\). Weight two here uses finite flatness and determinant of cyclotomic weight one. The character is exactly \(\chi_8\): its reduction is fixed by the determinant, and all characters of 2-power conductor dividing 512 have 2-power order, so reduction at odd \(q\) is injective on them. Every compatible exact level is \(2^j, 3\le j\le9\). Form the absolute norms \(\left|\operatorname N(a_{47}(f)-t)\right|\), for \(t=-2,2\) and all Galois orbits of newforms at those levels and character \(\chi_8\). Exact modular-forms computation gives:

| Level | Galois orbits | Distinct absolute norms |
|---:|---:|---|
| 8, 16, 32 | 0 at each level | none |
| 64 | 1 | 4 |
| 128 | 2 | 4 |
| 256 | 3 | 4, 36, 100 |
| 512 | 5 | 4, 16, 15376 |

The verifier recomputes the newform dimensions and checks that their eigenfield degrees exhaust each dimension, including all nonrational forms. Since \(15376=2^4\cdot31^2\), the only possible irreducible exponent \(q>5\), apart from the separated 47, is 31. Divisibility of the integer norm by \(q\) is necessary even at a prime ramified in an eigenvalue field.

## Direct exclusion of the six remaining prime exponents

For \(q=2,3,5,23,31,47\), the following finite-field computation excludes every single term beginning with \(w_8\). Starting at \((31,14,2273)\) modulo the auxiliary prime \(\ell\), iterate
\[
       (u,v,w)\longmapsto
       (u^4-32v^4,\ 2uvw,\ w^4-128u^4v^4).
\]
The signed first-coordinate convention only changes signs of \(u,v\), and the third coordinate uses their fourth powers. Consequently it agrees with the actual positive packet modulo \(\ell\). At every state, \(w\ne0\) and \(w^{(\ell-1)/q}\ne1\bmod\ell\). Once a state repeats, determinism covers all later indices.

| \(q\) | 2 | 3 | 5 | 23 | 31 | 47 |
|---|---:|---:|---:|---:|---:|---:|
| \(\ell\) | 3 | 7 | 31 | 47 | 6449 | 636287 |
| Distinct states | 3 | 2 | 4 | 22 | 31 | 1936 |

These six tests account also for the ramified coefficient prime 2 and the exceptional test prime 47. Every proper-power exponent has a prime divisor, which proves the assertion. [Exact finite verifier](abc_octic_dyadic_single_powers.py)

## The complementary packet \(u_n\)

**Every \(u_n\) at a dyadic index \(n\ge8\) also has valuation gcd one.** At the omitted index \(u_4=1\), and \(u_8=31\) is prime. To treat \(u_{2n}\) for \(n\ge8\), put \(a=u_n,\ b=4v_n^2\). Its signed value is \(a^4-2b^2=u_n^4-32v_n^4\), whose absolute value is \(u_{2n}\). The two integers \(a,b\) are coprime with \(a\) odd and \(b\) even. If \(u_{2n}\) is a \(q\)-th power, all valuations of \((a^2+bs)(a^2-bs)\) are multiples of \(q\), regardless of its sign. Thus the identical Frey curve, descent, conductor bound and finite-flat argument apply for \(q>5\). A hypothetical value one is also ruled out by the residue tests below.

At 47 the same dyadic points have abscissa 32, which guarantees that \(u_n,v_n\) are both units. The normalized Frey ratio is now \(b/a^2=4/x(P)=6\bmod47\), giving the normalized curve \(y^2=x^3+14x^2+43x\) at \(s=7\). Its trace is 12, as it is at \(s=-7\). In particular the model has good reduction and the raw trace is \(\pm12\). In the reducible case \(\pm48\equiv\pm12\bmod q\) requires \(q\mid36\cdot60\). In the irreducible case the absolute norm sets for the differences from \(\pm12\) are as follows.

| Level | Distinct absolute norms |
|---:|---|
| 8, 16, 32 | none |
| 64, 128 | 144 at each level |
| 256 | 16, 144, 400 |
| 512 | 144, 256, 20736 |

Only 2, 3, 5 divide these norms or \(36\cdot60\). It remains to exclude \(q=2,3,5\) and the auxiliary characteristic \(q=47\). Iterate the same signed integer recurrence from index eight as above, now checking the value of the first coordinate at each state.

| \(q\) | 2 | 3 | 5 | 47 |
|---|---:|---:|---:|---:|
| \(\ell\) | 17 | 7 | 71 | 473479 |
| Distinct states | 3 | 2 | 7 | 100 |

In every state \(u\) is a nonzero non-\(q\)-th power. The sign is immaterial at odd \(q\); for \(q=2\) the auxiliary prime is \(17\equiv1\bmod4\), so a value and its negative have the same quadratic character. This completes the assertion for the absolute packet. [Joint finite verifier](abc_octic_dyadic_single_powers.py)

## The third packet \(t_n=u_n^2+16v_n^2\)

At every dyadic \(n\ge4\), \(t_n\) has valuation gcd one. Here \(t_n\) denotes the factor of the direct dyadic triple. Its initial values are \(t_4=17\), \(t_8=4097=17\cdot241\). Write \(a=w_n, b=2u_nv_n\). Direct substitution of the duplication formulas and \(w_n^2=u_n^4+16u_n^2v_n^2+32v_n^4\) gives
\[
                  t_{2n}=a^4+8a^2b^2+8b^4 .
\]
We use the same quadratic field \(F\), its conjugation \(\sigma\) and \(s^2=2\). Put
\[
 g=a^2+(4+2s)b^2,\quad A=4sb,\quad B=sg,\quad
 C:y^2=x^3+Ax^2+Bx.
\]
Then \(gg^\sigma=t_{2n}\), \(B+B^\sigma=8b^2=A^2/4\), and \(BB^\sigma=-2t_{2n}\). The ideals of \(g,g^\sigma\) share no odd prime: their difference is \(4sb^2\), and an odd divisor of \(b\) cannot divide \(a\). At an odd prime of \(B\) or \(B^\sigma\) the invariants
\[
        \Delta_C=64 B^2 B^\sigma,\qquad c_4=16(B+4B^\sigma)
\]
therefore give minimal multiplicative reduction. If \(t_{2n}\) is a \(q\)-th power, these odd discriminant valuations are multiples of \(q\). At all other odd primes the curve has good reduction. The conjugate quotient and its differential are the same as in the main proof: the normalized two-isogeny has target coefficients \((-2A,4B^\sigma)=(2A^\sigma,4B^\sigma)\), followed by dividing coordinates by \(s^2,s^3\), so \(\mu^\sigma\mu=[-2]\). At the dyadic prime \(B\) and \(B^\sigma\) each have valuation one, hence \(v_s(\Delta_C)=15\). Ogg's formula and conductor induction bound the sum of the two equal constituent exponents by \(6+15=21\). Each exponent is at most ten. The preceding determinant, residual finite-flatness and level-lowering reasoning now gives level dividing 1024 and character \(\chi_8\) for an irreducible characteristic \(q>5\).

At either of the two possible points \(P=[n/2]R\) modulo 47, \((a/b)^2=(y(P)/(2x(P)))^2=24\). Here \(n\ge8\), and \(b\) is a unit at 47. Twisting by the reciprocal of \(b\) normalizes the coefficients to \(4s,s(24+4+2s)\) modulo 47. Both \(s=7,-7\) give good reduction with trace \(+12\), so the raw trace is \(\pm12\). In the reducible case the finite characters have conductors dividing 32: if either exponent exceeds five, both exponents are equal and their sum exceeds ten. Since \(47^2\equiv1\bmod32\) and \(\chi_8(47)=1\), the finite character values at 47 are equal signs. Thus \(q\mid36\cdot60\) if \(q\ne47\).

For the irreducible case the verifier computes \(T_{47}\) on the entire 104-dimensional cusp space \(S_2(1024,\chi_8)\), which contains the oldforms from every compatible lower level. Its characteristic polynomial is
\[
 X^{60}(X^2-64)^{10}(X^2-128)^4(X^2-96)^4(X^4-64X^2+512)^2.
\]
At either \(12\) or \(-12\) its absolute value is \(2^{208}3^{64}5^{10}47^2\). With the auxiliary characteristic itself included, both cases leave only \(q=2,3,5,47\).

The signed doubling recurrence in the preceding section preserves the absolute packet \(u^2+16v^2\) modulo every auxiliary prime. The verifier checks the following complete orbits starting at index eight, confirming that the packet is nonzero and a non-\(q\)-th power in every inspected state. Together with \(t_4=17\), this finishes the third packet.

| \(q\) | 2 | 3 | 5 | 47 |
|---|---:|---:|---:|---:|
| \(\ell\) | 3 | 7 | 71 | 419429 |
| Distinct states | 3 | 2 | 7 | 1321 |

[Direct dyadic triple](abc_dyadic_direct_triple.md) · [Joint finite verifier](abc_octic_dyadic_single_powers.py)
