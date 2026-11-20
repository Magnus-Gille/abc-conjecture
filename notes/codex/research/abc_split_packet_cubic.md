# Exact removal of the proper CM factors at a split prime index

At every prime \(q\equiv11\bmod24\), the full-annihilator packet \(C_q\) satisfies **\(C_q\equiv3\bmod7\)**. Consequently it has a prime of odd valuation and a prime whose valuation is nonzero modulo three. The two primes may coincide. In this statement \(C_q\) contains the exact prime powers of the scalar denominator at CM annihilator \((q)\); the individual primes have ordinary order \(q\) and size at least \(2q^2+1\). Their valuations can exceed one. The identities below also test characters of any other fixed order. [Packet definition and size of its primes](abc_odd_rank_quartic_cutoff.md)

## An integer determinant on two rational curves

Let \(q=a^2+2b^2>3\) be prime with \(a,b>0\). Scale the original curve and point to \(E:y^2=x^3+4x^2+2x,\ P=(-2,2)\). Write \(W=(1,1)\) on \(E_*:y^2=x^3-8x^2+8x\), and \(\tau=\sqrt{-2}\). Denote the division polynomials by \(\psi_j,\phi_j=x\psi_j^2-\psi_{j-1}\psi_{j+1}\), using the coefficients of the curve on which the point lies. Define the integer

\[
M=2\phi_a(P)\psi_b(W)^2+\phi_b(W)\psi_a(P)^2 .
\]

If \(B_q\) denotes the scalar abscissa denominator square root at \(qP\), then

\[
\frac{B_q}{C_q}=\frac{(-1)^b M}{2^{(a^2-1)/2}},
\qquad
C_q=\frac{\psi_q(P)}{2^{((q-1)/2)^2+b^2}M}.
\]

The second denominator divides the numerator in \(\mathbb Z\), with their signs equal. For example \(q=11,\ (a,b)=(3,1)\) gives \(M=-304\), \(B_q/C_q=19\), and \(C_q=147235727299\).

To isolate the local support, put \(S=[\tau]P=(-1/2,\tau/4)\) and \(\delta=x(aP)-x(bS)\in\mathbb Q\). The multiplier ideals \((a)\) and \((b\tau)\) are coprime, since \(\gcd(a,b)=1\) and \(a\) is odd. Thus these two points cannot both reduce to the identity at any odd prime: that would force \(P=O\) modulo that prime. If precisely one reduces to the identity the difference has negative valuation. Otherwise a positive valuation occurs exactly when the reductions agree up to sign, equivalently when one of \([a\pm b\tau]P\) reduces to the identity. Both signs cannot do so at one place, since that would similarly imply \([2]P=O\) there, contrary to \(y(P)=2\). Their common abscissa is consequently a uniformizing coordinate there, and \(v_p(\delta)\) is the formal depth of this proper CM multiple. These are exactly the primes of \(B_q\) having proper CM annihilator, since the only proper nonunit divisors of \((q)\) are \((a\pm b\tau)\). All such rational primes split in \(\mathbb Q(\tau)\).

At each of them \(p\ne q\) because \(q\ge11\) and rational two-torsion would give \(2q\mid\#E(\mathbb F_q)\), contrary to Hasse. The complementary CM multiplier is étale at \(p\), so the depth equals \(v_p(B_q)\). There is a genuine exception for \(q=3\), when \(|\operatorname{num}\delta|=3\) but \(B_3/C_3=9\).

At 2, \(x(aP)\) is integral for every odd \(a\): the even multiples are in the formal group since \(x(2P)=1/4\), and \(P\) is outside. The valuations of \(x(S)\) and \(x(2S)=-49/8\) are \(-1,-3\), with \(v_2(2)=1\). An odd formal multiplier preserves the depth, and \(2S\) is in the formal logarithm disk (parameter valuation \(3/2>1\)). Hence \(v_2(x(bS))=-1-2v_2(b)\). It follows that the positive integer \(B_q/C_q\) is exactly \(|\operatorname{num}\delta|\) in lowest terms. In original coordinates the corresponding difference equals \(4\delta\); its absolute numerator is \(2^{\mathbf1_{b\ {\rm odd}}}B_q/C_q\).

To pass to polynomials, write
\[
N=\phi_a(P)\psi_b(S)^2-\phi_b(S)\psi_a(P)^2=\delta\psi_a(P)^2\psi_b(S)^2.
\]
At odd primes, the inputs are integral points on a good model, and \(\phi,\psi^2\) have no common zero in reduction. The odd parts of the abscissa denominators of \(aP,bS\) are therefore the odd parts of \(\psi_a(P)^2,\psi_b(S)^2\), with relatively prime supports by the calculation above. Thus \(|N|\) has exactly the odd valuations of \(B_q/C_q\). For odd \(a\), \(v_2(\psi_a(P))=(a^2-1)/4\); this is the scalar odd-index normalization under the present coordinate scaling. Also \(v_2(\psi_b(S)^2)=1-b^2+2v_2(b)\), since \(\phi_b\) is monic of degree \(b^2\) in \(x\) with integral coefficients and \(v_2(x(S))=-1\). Combining with \(v_2(\delta)\) gives \(B_q/C_q=2^{b^2-(a^2-1)/2}|N|\). [Odd-index normalization and sign](abc_odd_rank_signed_frobenius.md)

In fact \(N<0\). The three cubic roots of \(E\) are \(e_1=-2-\sqrt2,\ e_2=-2+\sqrt2,\ 0\). The odd real multiple \(aP\) stays on the bounded component, with \(e_1<x(aP)<e_2\). The point \(S\) belongs to the bounded component of the negative real twist (its original abscissa lies between \(e_2\) and 0). For odd \(b\), \(x(bS)\) is in that same interval, and \(\psi_b(S)^2>0\). For even \(b\), \(x(bS)<e_1\) on the real identity component of the twist in the original abscissa, and \(\psi_b(S)^2<0\), since the even division polynomial is a real polynomial in the abscissa times a nonzero purely imaginary ordinate. None of the points here is torsion.

Scaling \(S\) by \((x,y)\mapsto(\tau^2x,\tau^3y)\) gives \(W\). Homogeneity yields \(\psi_b(S)^2=(-2)^{1-b^2}\psi_b(W)^2,\ \phi_b(S)=(-2)^{-b^2}\phi_b(W)\), hence \(N=(-1)^{b+1}2^{-b^2}M\). The sign of \(\psi_q(P)\) is \((-1)^{(q-1)/2}=(-1)^b\) on the bounded real oval and its 2-adic normalization gives \(B_q=|\psi_q(P)|/2^{(q^2-1)/4}\). Substitution proves both exact integer identities.

## A cubic character on half the split prime classes

Modulo seven the values \(\psi_n(P),\psi_n(W)\), starting at zero, respectively have period 8 and 24 with arrays

\[
(0,1,4,6,0,1,3,6),\quad
(0,1,2,4,0,6,6,6,0,4,2,1,0,6,5,3,0,1,1,1,0,3,5,6).
\]

These finite arrays match the first five division values and satisfy both standard division-polynomial recurrences cyclically for every residue \(n\). Strong induction proves them for all \(n\). Since \(2\) has order three modulo seven, the exact formula depends only on \((a,b)\bmod24\); the square of \((q-1)/2\) in the exponent requires only \(q\bmod6\). The 128 residue pairs for which \(\gcd(a^2+2b^2,24)=1\) give the following exhaustive table. In particular \(M\) is a unit modulo seven in every case.

| \(q\bmod24\) | condition | \(C_q\bmod7\) | number of pairs |
|---:|---|---:|---:|
| 1 | \(4\mid b\) | 1 | 16 |
| 1 | \(4\nmid b\) | 5 | 16 |
| 11 | all | 3 | 32 |
| 17 | \(4\mid b\) | 4 | 16 |
| 17 | \(4\nmid b\) | 6 | 16 |
| 19 | all | 6 | 32 |

Only 1 and 6 are nonzero cubes modulo seven. The cases with residues 3 and 5 are nonsquares as well. The table and both exact identities at 16 split prime indices from 11 through 139 were checked against the independent CM denominator implementation. [Standard-library verifier](abc_split_packet_cubic.py)

A second explicit calculation gives a fifth-power obstruction for every split prime \(q\) in any of the fourteen residue classes
\[
q\bmod45\in\{2,4,7,13,14,17,22,23,29,32,34,37,38,43\}.
\]
At these indices \(C_q^2\ne1\bmod11\). Both division sequences modulo eleven have period 45: the verifier obtains their first 45 terms by exact arithmetic and certifies that both Ward recurrences hold cyclically. In the squared determinant formula the factor \(4^{((q-1)/2)^2+b^2}\) depends only on the exponent modulo 5, so the entire squared residue depends only on \((a,b)\bmod45\). Enumerating these pairs gives the list above. In particular, **at every prime \(q\equiv59\bmod360\), the gcd of the positive valuations of the full CM packet is coprime to 30**. This statement permits two different primes with valuations two and three.

## Excluding any finite list of exponents simultaneously

For every finite set \(\mathcal L\) of rational primes there is a ray class giving a positive-density set of split prime indices \(q\) at which \(C_q\) is not an \(\ell\)-th power for any \(\ell\in\mathcal L\). Equivalently the gcd of its positive prime valuations is coprime to \(\prod_{\ell\in\mathcal L}\ell\). This permits squarefulness, since the positive valuations might include both two and three.

Let \(c=C_{11}=82633\cdot1781803\); the prime 82633 occurs exactly once. Fix \(\ell\in\mathcal L\setminus\{11\}\). Choose a prime \(h\equiv5\bmod8,\ h\equiv2\bmod11,\ h\equiv1\bmod\ell\) at which \(c\) is an \(\ell\)-th-power nonresidue. Avoid the finitely many bad places, including those dividing \(M(3,1)=-304\), \(c\), or \(2\ell\). To justify the choice, set \(F=\mathbb Q(\zeta_{\operatorname{lcm}(8,11,\ell)})\). The degree-\(\ell\) radical \(c^{1/\ell}\) does not lie in \(F\). Its minimal polynomial over \(\mathbb Q\) is Eisenstein at 82633. For odd \(\ell\) the field of the positive real root is nonnormal over \(\mathbb Q\), whereas \(F\) is abelian. For \(\ell=2\) the prime 82633 ramifies in the radical extension and is unramified in \(F\). Thus \(F(c^{1/\ell})/F\) is cyclic of degree \(\ell\). The specified cyclotomic automorphism fixes \(\zeta_\ell\), and its lifts can act on \(c^{1/\ell}\) by any desired \(\ell\)-th root of unity. Choose a nontrivial action. The Chebotarev density theorem gives the required \(h\), since the property of acting nontrivially on the \(\ell\)-th roots while fixing unity is invariant under conjugation.

Both rational curves in the determinant have CM by the order of discriminant \(-8\) and good reduction at \(h\); equivalently the second curve is a quadratic twist of the first. As \(h\) is inert in \(\mathbb Q(\sqrt{-2})\), their traces are zero, so the orders of their reduced points divide \(h+1\). For an integral point of order \(s>1\) modulo \(h\), its evaluated division sequence \(w_j\) vanishes exactly when \(s\mid j\). Ward's addition identity gives

\[
w_{j+s}w_{j-s}=-w_{s+1}w_{s-1}w_j^2 .
\]

On each nonvanishing residue class modulo \(s\) the consecutive ratios thus form a geometric progression over \(\mathbb F_h^\times\). After \(N=2(h-1)\) steps the net multiplier is \(r^N c_0^{N(N-1)/2}=1\), for the first ratio \(r\) and ratio multiplier \(c_0\). Therefore \(2(h^2-1)\) is a common period of both \(w\) sequences and their \(\phi\) sequences. This is also a valid period in \(a,b\) for the power of 2 in the denominator, since \(q=a^2+2b^2\) modulo \(2(h-1)\) determines the exponent modulo \(h-1\). If \(a+b\tau\equiv3+\tau\bmod 2(h^2-1)\), the exact integer formula consequently gives \(C_q\equiv C_{11}\bmod h\). Crucially \(11\nmid2(h^2-1)\), since \(h\equiv2\bmod11\). Thus the seed generator of norm 11 is a unit modulo this period. The congruence may be used with signed coordinates, as the \(\phi\)'s and the squares of the \(\psi\)'s are even under sign change in their indices.

For \(\ell=11\) the auxiliary \(h=23\) is inert, with common period \(1056=96\cdot11\). Take \(a\equiv3,\ b\equiv97\bmod1056\). Here \(q\equiv875\bmod1056\) is coprime to 1056. The determinant is \(4\bmod23\) and the exact formula gives \(C_q\equiv14\bmod23\); its square is \(12\bmod23\), so it cannot be an eleventh power. The verifier checks these residues from the integral recurrences. The chosen generator is congruent to \(3+\tau\) modulo 96.

For the specified finite \(\mathcal L\), take the lcm \(L\) of 96 and the periods for \(\ell\ne11\), so \(11\nmid L\). If the list contains 11, combine the generator congruence \(3+\tau\bmod L\) with \(3+97\tau\bmod1056\) by CRT, since their overlap divides 96. All resulting classes are units. As \(\mathbb Z[\sqrt{-2}]\) is principal, the prime ideal theorem in this ray class gives positive density of degree-one prime ideals having generators with exactly the prescribed congruences. Their rational prime norms give a positive-density family: the union of the ray class and its conjugate is stable under conjugation, and the degree-one ideals above a split rational prime occur in pairs. Every resulting rational prime satisfies all the selected character obstructions.
