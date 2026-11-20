# The factor U as one CM denominator ideal

For an odd full index \(N\ge3\) put \(n=(N+1)/2\). On
\[
 E:v^2=u^3-8u^2+8u,\qquad A=(1,1),\qquad J=(0,0),
\]
take the signed reduced slope \(s/t=(v(nA)+u(nA))/(2(u(nA)-1))\), with \(s\) odd and \(t>0\) even. Write
\[
 Y=s^2+2t^2,\quad V=(s-t)^2+t^2,\quad U=(s+t)^2+t^2=2Y-V,\quad D=s^2-2t^2 .
\]
The two positive integers \(Y,V\) are coprime squares. The radical of the octic triple equals the radical of \(T_N=2|stDU|\sqrt{YV}\). The full-orbit index at the seed \((7,4)\) is \(N=3\). [Full orbit and slope identities](abc_octic_full_mixed_orbit.md)

Let \(K=\mathbb Q(\tau)\), \(\tau^2=-2\), and \(\mathcal O=\mathbb Z[\tau]\). Use the isogenous curve and rational points
\[
 E':v'^2=u'^3+16u'^2+32u',\qquad
 R=(-8,16),\quad J'=(0,0),\quad S=R+J'=(-4,-8).
\]
For \(\alpha\in\mathcal O\setminus\{0\}\), let \(\mathfrak B_\alpha\) be the *odd* denominator ideal of \([\alpha]S\). Its valuation at an odd place is \(\max(0,-v_{\mathfrak p}(u'([\alpha]S))/2)\). The model has good reduction at every such place. The following equality is exact, including prime multiplicities:
\[
                      U_N=\operatorname N_{K/\mathbb Q}\mathfrak B_{N-\tau}.                 \tag{1}
\]
Every prime on either side is \(1\bmod 8\). At each rational \(p\mid U_N\) exactly one of the two places over \(p\) occurs in the ideal in (1).

## The two elliptic points and their local distance

The rational isogeny \(\phi:E\longrightarrow E'\) has coordinates
\[
 (u-8+8/u,\ (1-8/u^2)v).
\]
It satisfies \(\phi(A)=(1,-7)=2R=2S\). In particular \(S\) is nontorsion, and \(2\widehat h(S)=\widehat h(A)>0\). The full-orbit denominator identity gives
\[
 u'([N]R)=-8V/Y,\qquad
 u'([N]S)=32/u'([N]R)=-4Y/V.
\]
The second equality uses that \(N\) is odd. For a direct check of the first equality take \(W=(-2\tau,8)\) on \(E\). Then \(2W=A\), \(\phi(W)=R\), and \(\phi(nA-W)=[N]R\). The function \(u'(\phi(Q-W))\) is unchanged by \(Q\mapsto A-Q\); it has simple poles as a function of slope at \(\pm\tau\). Its values at slopes \(\infty,0,7/4\) are \(-8,-8,-200/81\), determining the displayed quotient. [Derivation on the quartic](abc_octic_mixed_denominator_characters.md)

The complex multiplication map on \(E'\) is the quotient by \(J'\) followed by scaling from the quotient model \((a,b)=(-32,128)\) to \((16,32)\). Its abscissa formula is
\[
 u'([\tau]B)=-\tfrac12(u'(B)+16+32/u'(B)).
\]
Choose the sign of the endomorphism so that its ordinate scaling in the quotient is division by \(\tau^3=-2\tau\). Then \([\tau]S=(-2,2\tau)\). The conjugate endomorphism is its negative and its square is \([-2]\), as is also seen on the invariant differential. Hence
\[
 u'([N]S)-u'([\tau]S)=-2U/V.                                                   \tag{2}
\]
For primitive \(s,t\) the integers \(U,V\) are coprime. Indeed any common odd prime would divide \(U-V=4st\) and cannot divide either positive definite form at a primitive zero of \(st\). Both forms are odd. If \(p\mid U\), equation (2) makes \([N]S\) affine integral with abscissa \(-2\bmod p\). Its rational ordinate then reduces to a square root of \(-8\), a unit. Thus \(p\) splits in \(K\). Independently \(U=(s+t)^2+t^2\) primitively represents \(p\) as a divisor of a sum of squares, so \(p\equiv1\bmod4\), giving \(p\equiv1\bmod8\). Among the two places over \(p\), exactly one reduces \([N]S\) to \([\tau]S\), since \(2\tau\) and \(-2\tau\) are distinct modulo either place. At that place the abscissa difference in (2) is a local parameter difference with unit derivative because the ordinate is a unit. Translation by \(-[\tau]S\) identifies the two residue disks integrally. Consequently \([N-\tau]S\) has formal depth exactly \(v_p(U)\), and at the conjugate place it has depth zero. Conversely a positive denominator valuation of \([N-\tau]S\) requires these two points to coincide on reduction. Equation (2) then forces \(p\mid U\), since at a prime of \(V\) the point \([N]S\) reduces to the identity. This proves (1). For example \(U_3=137\) and \(\operatorname N(3-\tau)=11\), illustrating the distinct roles of the denominator prime and the index ideal.

## The positive mass at an exact annihilator

At an odd place \(\mathfrak p\) let \(I_{\mathfrak p}\) be the annihilator ideal of the reduction of \(S\) as an \(\mathcal O\)-module element. All CM endomorphisms are defined over \(K\) and extend at good reduction. The ring \(\mathcal O\) is norm-Euclidean, so one can write \(I_{\mathfrak p}=(\gamma_{\mathfrak p})\). Let \(e_{\mathfrak p}\) be the formal depth of \([\gamma_{\mathfrak p}]S\). Only signs are ambiguous in the generator and they preserve depth. Write, for odd-norm ideals,
\[
 F(I)=\sum_{I_{\mathfrak p}=I} e_{\mathfrak p}\log \operatorname N\mathfrak p,\qquad
 W(I)=\sum_{I_{\mathfrak p}=I} (e_{\mathfrak p}-1)\log \operatorname N\mathfrak p,\qquad
 \Phi_K(I)=\operatorname N I\prod_{\lambda\mid I}\left(1-1/\operatorname N\lambda\right).
\]
The product runs through distinct prime ideals. Uniformly for odd \(M=\operatorname N I\),
\[
 F(I)=2\widehat h(S)\Phi_K(I)
                +O\big(2^{\omega_K(I)}\log(2M)\big),                                    \tag{3}
\]
where \(\omega_K\) counts distinct prime ideal factors. In particular \(F(I)>0\) at every sufficiently large odd-norm ideal. Formula (3) concerns the full first multiplicity. It gives only \(0\le W(I)\le F(I)\) for the excess.

Here are the height and formal-group details for this particular point. If \((\alpha)=I\), the degree of \([\alpha]\) is \(M\), so \(h(u'([\alpha]S))=2\widehat h(S)M+O(1)\). Both \(R,S\) lie on the compact nonidentity real component of \(E'\), between the roots \(-8-4\sqrt2\) and \(-8+4\sqrt2\). For odd \(M\), \([M]S\) lies on that same component, at a fixed positive minimum distance from the identity in the flat metric on the complex torus. Multiplication by \(\bar\alpha\) has Lipschitz constant \(\sqrt M\) and takes \([\alpha]S\) to \([M]S\). Thus the latter distance bound gives \(\log^+|u'([\alpha]S)|=O(\log(2M))\) at both embeddings, using the double pole at the identity.

At the dyadic place choose a sufficiently small formal-logarithm ball stable under \(\mathcal O\). Such a ball exists since the differential of \(\tau\) is dyadically integral. In detail, first shrink the log chart into the inverse image of its domain under \([\tau]\), then in log coordinates take a sufficiently small additive ideal. Integers and \(\tau\) both preserve it. Every odd rational multiple \([M]S\) has odd abscissa denominator, by \(u'([M]S)=-4Y_M/V_M\) for \(M\ge3\) and \(u'(S)=-4\). No such multiple lies in a sufficiently small ball about the identity. Stability and \([\bar\alpha][\alpha]S=[M]S\) imply the same bound for \([\alpha]S\). This only uses bounded depth on this fixed dyadic model, irrespective of its minimality. The absolute height over the imaginary quadratic field now gives
\[
 \log\operatorname N\mathfrak B_\alpha=2\widehat h(S)M+O(\log(2M)).
\]

At every odd place the completion is unramified over \(\mathbb Q_p\). The elliptic formal logarithm is an isometry at positive depth, as \(p\ge3\). When \(I_{\mathfrak p}\mid (\alpha)\), the depth after multiplying by \(\alpha/\gamma_{\mathfrak p}\) increases by the valuation of its differential. The differential is given by one fixed embedding of \(\mathcal O\) and its values are integral. The sum of the weighted increases is therefore at most \(\log M\), by divisibility into the differential of \(\alpha\). There are no other denominator places. Subtracting these increases and applying ideal Möbius inversion proves (3). Positivity follows from \(\Phi_K(I)\gg_\epsilon M^{1-\epsilon}\), \(2^{\omega_K(I)}\ll_\epsilon M^\epsilon\), and \(\widehat h(S)>0\). Both elementary divisor bounds follow by splitting off the finitely many prime ideals of small norm.

## Which packets belong to globally new rational primes?

Set \(L=N^2+2\), \(\alpha=N-\tau\). The map \(\mathcal O/(\alpha)\to\mathbb Z/L\mathbb Z\) induced by \(\tau\mapsto N\) is an isomorphism, by its surjectivity and the norm of \(\alpha\). Thus each divisor \(r\mid L\) corresponds to exactly one divisor ideal of \((\alpha)\), namely
\[
 I_N(r)=(r,\tau-N),\quad \operatorname N I_N(r)=r,\quad
 I_N(r)\cap\mathbb Z=r\mathbb Z,\quad \Phi_K(I_N(r))=\varphi(r).
\]
An odd place with exact annihilator \(I_N(r)\) lies above a rational prime \(p\mid U_N\), and \(r\) is exactly the order of the point \(S\) modulo \(p\). At every such \(p\), equation (1) uses just one place. Therefore
\[
 \log U_N=\sum_{r\mid L} F(I_N(r))+O(\log L),\qquad
 \log\frac{U_N}{\operatorname{rad}U_N}
         =\sum_{r\mid L}W(I_N(r))+O(\log L).                                         \tag{4}
\]
The errors in (4) are nonnegative formal lifting increments of weighted total at most \(\log L\). In particular the full first multiplicity at the *individual* exact order \(r\) in \(U_N\) is
\(\widehat h(A)\varphi(r)+O(2^{\omega(r)}\log(2r))\), uniformly in \(r,N\).

Let \(f(p)\) be the least full odd index \(M\ge3\) for which \(p\mid T_M\), permitting any of the six factors. If \(r>2N\), *every prime in the packet \(I_N(r)\) has \(f(p)=N\)*. At an earlier \(U_M\) occurrence the reductions \([M]S\) and \([N]S\) at a common place have the same abscissa \(-2\). They agree up to sign, forcing \(r\mid N-M\) or \(r\mid N+M\). At an earlier ordinary factor the known good-reduction identities give \(\operatorname{ord}_p(A)\mid k\) for one of \(k=M,2M,M-1,M+1\). Indeed \(u([M]A)=D_M^2/(Y_M V_M)\) gives reductions \(O,J\) for \(p\mid Y_M V_M,D_M\) respectively, and abscissa one for \(p\mid s_M t_M\), hence reduction \(\pm A\). Here \(r\mid L\) is odd. Consequently
\[
 r=\operatorname{ord}_p(2S)=\operatorname{ord}_p(\phi(A))\mid\operatorname{ord}_p(A),
\]
so \(r\mid k\) and \(r\le2M\). The proof needs no equality of the two orders and no hypothesis on the parity of \(\operatorname{ord}_p(A)\). In general \(\operatorname{ord}_p(A)/r\in\{1,2\}\) whenever \(p\mid U_N\), since the kernel of \(\phi\) has order two.

The entire full logarithmic mass at orders \(r\le2N\) in \(U_N\) is \(O(N\,d(L)+L^{o(1)})=O(N^{1+o(1)})\), via (3), (4), and the divisor bound for \(L\). Removing these orders from either equality in (4) therefore costs only \(O(N^{1+o(1)})\). In particular
\[
 \sum_{p\mid U_N,\ f(p)=N} v_p(U_N)\log p
      =\widehat h(A)N^2+O(N^{1+o(1)}).
\]
Here one can use either the total denominator height above or the independent identity \(\log U_N=2\log\max(|s|,t)+O(1)=\widehat h(A)N^2+O(1)\). This first-appearance formula counts full multiplicities and leaves open how much of its mass exceeds multiplicity one. [Radical criterion using the first appearance in the entire triple](abc_octic_first_occurrence.md)

## Dispersion across divisors at highly composite values

The weights \(\varphi(r)/L\), \(r\mid L\), sum to one. With \(g_N(r)=W(I_N(r))/\varphi(r)\), equation (3) bounds \(g_N(r)\) uniformly. Thus a positive proportion of \(N^2\) in excess along a subsequence is equivalent to a positive total weight of divisors with \(g_N(r)\) bounded away from zero along that subsequence. These statements follow by boundedness and (4), in both directions.

One cannot extract a single divisor ideal carrying a fixed positive proportion of the total full mass uniformly. Impose \(N^2\equiv-2\bmod p\) for each odd \(p\le z\) split in \(K\), choosing either root independently. CRT permits arbitrarily large odd \(N\). The product \(\prod_{p\le z,\ p\text{ split}}(1-1/p)\) tends to zero by the divergence of reciprocal primes in the classes \(1,3\bmod8\). Since \(\varphi(r)\le\varphi(L)\) for \(r\mid L\), along such a diagonal sequence
\[
 \max_{r\mid L} F(I_N(r)) = o(L),\qquad
 \sum_{r\mid L} F(I_N(r)) = (\widehat h(A)+o(1))L .
\]
This is unconditional dispersion of full multiplicity. It does not assert any positive fixed proportion in excess on these CRT indices.

## A uniform count of global first appearances

For every sufficiently large odd \(N\), at least \(d(N^2+2)/4\) distinct rational primes first appear anywhere in \(T\) at \(U_N\). Here \(d\) is the ordinary divisor function. Their product has logarithm \(\gg d(N^2+2)\log N\).

Indeed the central interval \([L/(2N),2N]\) has endpoint ratio \(4N^2/L<4\). If a prime \(q\ge5\) divides \(L\), partition its divisors into chains of fixed prime-to-\(q\) part and varying \(q\)-adic exponent. At most one of each chain's at least two divisors is central. If \(L=3^e\), then \(e\ge3\) for the odd indices under consideration, and at most two of the \(e+1\) divisors are central. Pairing the other divisors by \(r\leftrightarrow L/r\) puts at least \(d(L)/4\) above \(2N\). For sufficiently large \(N\), (3) supplies a place in each corresponding packet. Distinct \(r\) give distinct rational primes by the unique-place property of (1). The first-appearance proof applies, and Hasse's inequality \(r\le(\sqrt p+1)^2\) gives the stated product bound.

Consequently the interval \([M,2M]\) contains first appearances of \(\gg M\log M\) distinct rational primes for all sufficiently large \(M\). Different first indices give disjoint prime sets. For the required lower bound on the average of \(d(N^2+2)\), count only odd divisors \(d\le M/4\). Each of the \(\rho(d)\) roots of \(-2\bmod d\) occurs at \(\gg M/d\) odd indices in the interval. With \(\chi=\chi_{-8}\), the Dirichlet series of \(\rho\) restricted to odd integers is
\[
 \sum_{d\text{ odd}}\rho(d)d^{-s}
 =\frac{\zeta(s)L(s,\chi)}{(1+2^{-s})\zeta(2s)} .
\]
This follows from the two roots at every positive power of a split odd prime and zero roots at inert primes. The hyperbola method and bounded partial sums of \(\chi\) give \(\sum_{j\le X}(1*\chi)(j)=L(1,\chi)X+O(\sqrt X)\). Convolving with the coefficients of \(1/\zeta(2s)\) and \((1+2^{-s})^{-1}\) gives \(\sum_{d\le X,\ d\text{ odd}}\rho(d)=cX+O(\sqrt X\log(2X))\), with \(c=L(1,\chi)/((1+1/2)\zeta(2))>0\). Partial summation gives \(\sum_{d\le X,\ d\text{ odd}}\rho(d)/d=c\log X+O(1)\). All these first primes satisfy \(p\equiv1\bmod8\) and \(p\le U_N\le\exp(CM^2)\); their first depths can be arbitrary.

## The five remaining rational factors

Write \(B_j(P)\) for the positive square root of the reduced rational denominator of the elliptic abscissa of \([j]P\), on the displayed model of its curve. For every odd full index \(N\ge3\),
\[
 \sqrt{Y_N}=B_N(R),\qquad \sqrt{V_N}=B_N(S),\qquad |D_N|=B_N(A+J).
\]
The first two follow from the two abscissa quotients above. For the third, oddness of \(N\) gives \(u([N](A+J))=8YV/D^2\), using translation by \(J\) and \(u([N]A)=D^2/(YV)\). The latter quotient is reduced since \(D\) is odd and coprime to \(YV\).

At the remaining two factors one has the identity of odd parts
\[
 (|s_Nt_N|)_{\mathrm{odd}}=
 \big(B_{N+1}(R)\,B_{N-1}(R)\big)_{\mathrm{odd}}.
\]
To see the local multiplicities, use \(Q=nA\). The slope as a function of \(Q\) has simple zeros at \(J=(0,0), A+J=(8,-8)\) and simple poles at \(O,A\). These four points stay distinct at every odd prime. The original slope expression gives a unit times a parameter at \(J\) and a unit times an inverse parameter at \(O,A\). At \(A+J\) use the equivalent expression \(u(u-8)/(2(v-u))\), whose denominator there is \(-32\). These formulas also cover reduction at 7. The degree-two slope has no further zero or pole on any good odd fiber. The depth at any of the four points is preserved under the isogeny \(\phi\), which is étale there since its degree is two. Near \(O,J\) it is exactly the formal depth of \(\phi(Q)=[N+1]R\); near \(A,A+J\) it is that of \(\phi(Q-A)=[N-1]R\). The two corresponding sets of odd primes are disjoint because \(\phi(A)=(1,-7)\) has finite affine reduction at every odd prime.
