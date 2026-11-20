# A fixed elliptic curve giving repeated factors on the twelfth-power conic

Put \(C=W^{12}\) and \(R=\operatorname{rad}(3UVW)\). On the single curve described below, for every fixed \(A>0\) there are infinitely many primitive triples \(U^2+3V^2=C\) with
\[
              \frac{C}{R}>\sqrt{\log C}\,(\log\log C)^A.
\]
The same sequence works for every \(A\). Its construction ensures a large power of a fixed prime at one neighboring elliptic index and a square for each of many distinct primes at the other. In the base-3 construction the latter primes include a set of density \(11/16\). The proof gives a subpower guarantee. A separate criterion below identifies exactly what would yield a violation of abc on this orbit.

## The quartic square and the primitive triples

Take the point \(P=(-2,8)\) on \(E:Y^2=X^3+36X^2+36X\). One has
\[
  2P=(4,28),\quad 3P=(-242/9,2024/27),\quad
  4P=(25/196,-6245/2744).
\]
Translation of \(X\) by 12 puts the equation in integral short Weierstrass form. The nonintegral abscissa of \(3P\) proves by Nagell–Lutz that \(P\) has infinite order. For each odd \(n\ge3\), the squareclass map from rational 2-isogeny descent gives \([X(nP)]=[-2]\), since it sends \(P\) to \([-2]\) and is a homomorphism. Write \(X(nP)=-2(x/y)^2\) with \(x,y\) relatively prime and positive. Put \(v=Y(nP)/(4x/y)\). Then \(z=y^2v\) satisfies
\[
             F_0=x^4-18x^2y^2+9y^4=-2z^2.
\]
The rational number \(z\) is an integer, since its reduced denominator squared divides 2. Both \(x,y\) are odd by reducing this identity modulo 2. At 3 the reduction of \(P\) is a nonsingular affine point and \(3P\) is in the formal group. Multiples with \(3\nmid n\) thus reduce to \(\pm P\), with unit abscissa, and those with \(3\mid n\) have abscissa of negative valuation. In both cases \(3\nmid x\).

With \(d=\sqrt{-3}\), put \(\beta=(x+yd)/2\), \(W=(x^2+3y^2)/4\), and take \(U,V\) as the absolute values of the two coefficients of \(\beta^{12}\) in the basis \(1,d\). Here \(\beta\) is an Eisenstein integer and \(W\) is odd and prime to 3. Since \(\beta^{12}\equiv1\) in the residue field at 2, these coefficients are integers. The ideals of \(\beta,\bar\beta\) are coprime by \((x,y)=1\) and \((W,6)=1\). Consequently these triples are primitive. The case \(W=1\) would force \(x=y=1\), and \(nP=\pm P\), impossible for \(n\ge3\). Coprimality of the ideals then excludes \(UV=0\).

Let \(H=\max(x,y)\). The canonical height and the equality \(X(nP)=-2(x/y)^2\) give
\[
       \log H=n^2\widehat h(P)+O(1),\qquad
       \log C=24n^2\widehat h(P)+O(1).
\]
For example \(3P\) gives \((x,y,z)=(11,3,46)\) and
\[
                1413128809^2+3\cdot1236395160^2=37^{12}.
\]
The prime factors of \(W\) in this construction are unrestricted among the primes split in the Eisenstein field.

## The remaining factors

Define \(F_\pm=F_0\pm(12x^3y-36xy^3)\), and let \(Q\) be the coefficient of \(d\) in \((x+yd)^{12}\). Its real part is \(F_0F_+F_-\), and \(Q/12\) is a degree-12 integral binary form divisible by \(x^2-y^2\). The [full factorization](abc_eisenstein_twelfth_large_squares.md) gives the positive integer
\[
             D_n=|z F_+ F_- (Q/12)(x^2+3y^2)|.
\]
For \(p>3\), the support of \(D_n\) is exactly that of \(3UVW\), as follows directly from \(F_0=-2z^2\) and the powers of 2 in the normalization. Both 2 and 3 divide \(D_n\). Indeed \(2\mid x^2-y^2\), and one of \(y,x-y,x+y\) is divisible by 3. Both also divide \(3UVW\), since a primitive solution has even \(V\). Thus \(\operatorname{rad}(D_n)=R\). Since \(|z|\ll H^2\), the other factors have total degree 22, and \(C\asymp H^{24}\), one has pointwise
\[
                 \frac C R\gg\frac{D_n}{\operatorname{rad}(D_n)}.       \tag{1}
\]
In particular, any square divisor \(q^2\mid D_n\) gives \(C/R\gg q\).

## The two neighboring indices

Write the reduced denominator of \(X(mP)\) as \(B_m^2\), \(B_m>0\). At each \(p\ge5\) the curve has good reduction, \(P\) and \(-P\) are distinct modulo \(p\), and \(X\) is unramified at both since \(2Y(P)=16\) is a unit. The formal group coordinate at \(mP\) has valuation \(v_p(B_m)\) when \(mP\) reduces to the identity. It follows that for odd \(n\ge3\)
\[
             v_p(x^2-y^2)=v_p(B_{n-1})+v_p(B_{n+1}).                \tag{2}
\]
Indeed, on the unit locus \(x^2-y^2=-(X(nP)+2)y^2/2\). A zero modulo \(p\) means \(nP\) reduces to \(P\) or \(-P\), and translation by that point preserves the depth by the unit derivative. When \(p\mid y\) neither side is positive. These alternatives exhaust the rational inputs.

There is an upper limit to the gain supplied by raising the index. Set \(r_p=\operatorname{ord}(P\bmod p)\), \(e_p=v_p(B_{r_p})\), and let \(L\) be the part of \(|x^2-y^2|\) prime to 6. The two divisibility conditions \(r_p\mid n-1\) and \(r_p\mid n+1\) are disjoint, since \(2P\) is affine at every good prime. The formal logarithm is an isometry on the formal group at each \(p\ge5\), so for \(r_p\mid m\) the valuation is exactly \(v_p(B_m)=e_p+v_p(m/r_p)\). Consequently
\[
 0\le \log\frac{L}{\operatorname{rad}L}-
       \sum_{\substack{p\ge5\\ r_p\mid n-1\ \mathrm{or}\ r_p\mid n+1}}(e_p-1)\log p
       \le\log(n^2-1).
\]
Thus summing ordinary lifting gains at these two indices can supply a factor of at most \(n^2-1\). A fixed-exponent gain from this part would require repeated primes already at their first index of occurrence. There is a second exact denominator identity, since duplication gives
\[
       X(2nP)=\left(\frac{x^4-9y^4}{2xyz}\right)^2 .
\]
For \(p\ge5\) the numerator and denominator are coprime: for \(p\mid z\) a common zero would give \(x^4=9y^4\) and \(x^4-18x^2y^2+9y^4=0\), hence \(x^2=y^2\) and \(8y^4=0\), impossible. The cases \(p\mid xy\) follow from primitivity. Therefore \(B_{2n}\) agrees with \(|xyz|\) away from 2 and 3.

Choose \(n=2^{k+1}-1\). At 2 the displayed value of \(4P\) lies in the formal group with parameter of valuation 1. Doubling in the integral formal group increases a positive valuation by at least 1. Hence \(2^{k+1}P\) has parameter of valuation at least \(k\). Translation to \(-P\), followed by the regular local coordinate function \(X-X(-P)\), is 2-adically analytic near the identity. Its expansion has zero constant term, so \(v_2(X(nP)+2)\ge k-O(1)\). As \(y\) is odd,
\[
                         v_2(x^2-y^2)\ge k-O(1).                    \tag{3}
\]

For \(Y\ge11\) take
\[
               k=k(Y)=\operatorname{lcm}\{\varphi(m):1\le m\le Y,\ m\ {\rm odd}\}.
\]
Every \(p\le Y\) with \(p\equiv3\bmod8\), \(p>3\), supplies an additional square in (2). To see this, the 2-isogenous curve of \(E\) is \(Y'^2=X'^3-72X'^2+1152X'\), which becomes \(Y'^2=u^3-576u\) after \(X'=u+24\). At \(p\equiv3\bmod4\), the terms of its quadratic character sum cancel between \(u\) and \(-u\); both curves have \(p+1\) points. For \(p\equiv3\bmod8\), the other two geometric 2-torsion abscissas of \(E\) are conjugate since \((2/p)=-1\). There is a unique subgroup of index 2 in \(E(\mathbf F_p)\), namely \(2E(\mathbf F_p)\). By 2-isogeny descent this is the kernel of the squareclass character of \(X\): the dual isogeny has a rational kernel of size 2 and its image has index 2. As \((-2/p)=1\), the order \(m_p\) of \(P\bmod p\) divides \((p+1)/2\).

Euler's theorem applied to \(p\) and to the odd integer \((p+1)/4\) now shows \(p\mid 2^k-1\) and \((p+1)/4\mid 2^k-1\). Thus \(p\,m_p\mid 2(2^k-1)=n-1\). Since \(m_pP\) is in the formal group and multiplication by \(p\) raises its depth, \(p^2\mid B_{n-1}\). Equations (1)–(3) give
\[
     \frac C R\gg 2^k \prod_{\substack{3<p\le Y\\p\equiv3\bmod8}}p
        = 2^k\exp\big((1/4+o(1))Y\big)
\]
by the prime number theorem in the progression \(3\bmod8\).

For clarity, \(\log k(Y)=o(Y)\). For a prime power \(q^a\le Y\), the totient contributes only \(q-1\) and \(q^{a-1}\). The lcm of all \(q^{a-1}\) contributes \(O(\sqrt Y\log Y)\) to the logarithm. The remaining lcm divides that of \(q-1\) over primes \(q\le Y\). Its higher prime powers contribute \(O(\sqrt Y\log Y)\) beyond the first powers. For any fixed integer \(J>1\), primes \(\ell\le Y/J\) contribute \(O(Y/J)\). A larger prime factor has \(q=a\ell+1\) with \(a\le J\). For each fixed \(a\), Brun's upper-bound sieve for the two linear forms \(t,at+1\) gives \(O_a(Y/\log^2Y)\) possibilities for \(\ell\) (odd \(a\) allows only the bounded parity exceptions). Thus these primes contribute \(O_J(Y/\log Y)\). First let \(Y\) grow, then \(J\). As \(k(Y)\to\infty\), \(\log\log C\asymp k(Y)\), and \(\sqrt{\log C}\asymp 2^k\), this proves the stated lower bound.

## Using the prime 3 and a set of density eleven sixteenths

Instead take \(k=\operatorname{lcm}\{\varphi(m):m\le 2Y,\ 3\nmid m\}\), \(n=2\cdot3^k-1\). The same proof gives \(\log k=o(Y)\). Since \(3P\) has formal depth one at 3, multiplication by \(3^{k-1}\), then by 2, gives \(v_3(x^2-y^2)\ge k-O(1)\) by translation to \(-P\). Its abscissa is a 3-adic unit, so \(y\) is a unit. For every sufficiently large prime \(p\le Y\) with \(3\nmid\#E(\mathbf F_p)\), the group size \(M_p\) is at most \(2Y\) by Hasse. Also \(p\nmid M_p\), since \(M_p<2p\), \(M_p\) is even and \(p\) is odd. Hence \(p\) and the order of \(P\bmod p\) are coprime divisors of \(3^k-1\). As before \(p^2\mid B_{n-1}\).

These primes have natural density \(11/16\). To compute it, use the 2-isogenous curve \(E':v^2=u^3-576u\), whose 3-torsion representation is isomorphic to that of \(E\). The automorphism \(J(u,v)=(-u,iv)\) has \(J^2=-1\), giving \(E'[3]\) the structure of a one-dimensional space over \(\mathbf F_9\). Galois over \(\mathbf Q(i)\) acts through \(\mathbf F_9^\times\). Frobenius at 5 belongs to this subgroup and has determinant \(5\bmod3=-1\) by the Weil pairing. A scalar of norm \(-1\) has order 8, so this subgroup is all of \(\mathbf F_9^\times\). Complex conjugation sends \(J\) to \(-J\). Thus the full image consists of the eight scalars and eight maps \(z\mapsto a z^3\). Exactly one scalar fixes a nonzero vector. Such a semilinear map fixes a nonzero vector precisely when \(a\) is a square in \(\mathbf F_9^\times\), giving four more elements. Chebotarev yields the claimed density, because \(3\mid M_p\) exactly when Frobenius fixes a nonzero vector. Partial summation yields the same constant for the logarithm of the prime product. Consequently this construction gives
\[
                C/R\gg 3^k\exp\big((11/16+o(1))Y\big).
\]
Here \(k\ge 2^{\lfloor\log_2(2Y)\rfloor-1}\) by the totient of a power of 2. In particular \(Y=O(k)\). The logarithm of the certified gain is \(O(k)\), whereas \(\log C\asymp 3^{2k}\).

## What would decide this orbit

Let \(q_n\) be the largest integer such that \(q_n^2\mid D_n\). Abc holds on this orbit for every fixed positive exponent if and only if
\[
                                \log q_n=o(n^2).
\]
One direction follows from (1). For the other, \(\log |D_n|=24\log H+o(n^2)\). Indeed \(2D_n^2=|F_0|\{F_+F_-(Q/12)(x^2+3y^2)\}^2\), the absolute value of a degree-48 binary form, whose finitely many projective zero directions are algebraic. The logarithmic proximity of \(X(nP)\) to any fixed algebraic real projective point is \(o(n^2)\), and the finite map \(x/y\mapsto-2(x/y)^2\) transfers this bound to the directions of \((x,y)\).

Here is a proof of the proximity estimate. For a fixed integer \(m\) write \(n=ma+j\), \(0\le j<m\). The map \(T\mapsto X([m]T+jP)\) has local degree at most 2, since multiplication is étale. Its finitely many preimages of the fixed target are algebraic. Near each real preimage \(T_0\), logarithmic proximity to the target is at most twice logarithmic proximity to \(T_0\), up to an \(m\)-dependent additive constant. The latter is at most the logarithmic proximity of \(X(aP)\) to \(X(T_0)\) plus a constant, using projective distance at infinity. Roth's theorem for irrational algebraic targets and rational height separation for rational targets bound this by \(3h(X(aP))+O_m(1)\); exact coincidences have only finitely many indices for fixed \(m\). Dividing by \(n^2\) gives an upper limit \(O(\widehat h(P)/m^2)\). Let \(m\) grow. Compactness away from the finitely many zeros then proves the asserted size of \(D_n\).

Finally \(q_n\le D_n/\operatorname{rad}(D_n)\le q_n^2\). Together with the size estimate and \(\operatorname{rad}(D_n)\asymp R\), this proves the equivalence. The constructed lower bound does not establish that \(\log q_n\) reaches a positive multiple of \(n^2\).

A sufficient test involving just a prime is now available. If infinitely many \(p\ge5\) have \(e_p\ge2\) and \(\log p\ge\delta r_p^2\) for some fixed \(\delta>0\), this orbit disproves abc. When \(r_p\) is odd take \(n=r_p\): the denominator \(B_n\) equals \(y\), and \(y\mid D_n\). When \(r_p\) is even take \(n=r_p+1\) and use (2). In both cases \(p^2\mid D_n\), so (1) gives the required fixed-exponent gain. As \(p\) varies, \(r_p\) is unbounded because each fixed denominator has finitely many prime factors.

The [compiled scan](abc_eisenstein_slice_denominator_scan.cpp) found exactly one such first-occurrence square among all 664,577 good primes through ten million: \(p=211\), \(r_p=53\), \(e_p=2\). The [scan output](abc_eisenstein_slice_denominator_scan.txt) includes checksums. For this prime, \(B_{53}/211^2\equiv149\bmod 211\). At \(n=53\) the height \(C\) has 6,502 decimal digits. The valuations of \(D_{53}\) at \(2,3,211\) are \(25,3,2\). With \(K=2^{24}3^2\cdot211\), exact integer arithmetic gives \(\lfloor CK/D_{53}\rfloor=138132\), certifying \(C/R>138132\) without factoring the remaining cofactor. The [standard-library verifier](abc_eisenstein_twelfth_slice_check.py) checks the example, denominator identities at 30 odd indices, and 207 forcing congruences. An [independent division-polynomial scan](abc_eisenstein_twelfth_first_squares.py) found the same single prime among the 22,042 good primes through 250,000. It checks an annihilating index \(m\) prime to \(p\) for every prime. At good reduction \(p\mid\psi_m(P)\) is equivalent to \(r_p\mid m\), and \(v_p(\psi_m(P))=v_p(B_m)\) when \(p\mid\psi_m(P)\), since the numerator and denominator of the multiplication map have no common projective zero modulo \(p\).
