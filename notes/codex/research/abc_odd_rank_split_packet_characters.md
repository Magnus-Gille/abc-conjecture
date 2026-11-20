# Two distinct odd prime valuations at split prime indices

On \(E:y^2=x^3+16x^2+32x\) let \(R=(-8,16)\), and let \(B_q\) be the positive square root of the reduced denominator of \(x([q]R)\). For every split prime \(q>3\) with \(q\equiv5,6\bmod7\), **\(B_q\) has two distinct primes of odd valuation**. One prime has full CM annihilator \((q)\); the other has an annihilator of norm \(q\). This includes all primes \(q\equiv41\bmod56\) and \(q\equiv27\bmod56\), for example. More generally the conclusion holds on an explicit set of relative natural density \(0.99999997475492\ldots\) among primes split in \(\mathbf Q(\sqrt{-2})\). On a squareful \(B_q\), both exponents are at least three. [Standard-library verifier](abc_odd_rank_split_packet_characters.py)

## The proper and full annihilators

Set \(\tau=\sqrt{-2}\), \(\mathcal O=\mathbf Z[\tau]\), and write \(q=a^2+2b^2\) with \(\alpha=a+b\tau\), an odd prime element. Let \(\mathfrak B(P)\) denote the odd integral ideal of local abscissa denominator exponents after taking square roots. Put
\[
 M_q=N_{K/\mathbf Q}\mathfrak B([\alpha]R),\qquad C_q=B_q/M_q.
\]
All denominator primes at odd scalar indices split in \(K=\mathbf Q(\tau)\). For \(p\mid B_q\), \(R\bmod p\) has exact order \(q\), since \(R\) is integral. At \(q\ge7\), Hasse and the rational two-torsion imply \(p\ne q\), as \(2q>(\sqrt q+1)^2\). Every split prime \(q>3\) is at least 11. At either place above \(p\), the possible annihilator ideals are \((\alpha),(\bar\alpha),(q)\), since \((q)=(\alpha)(\bar\alpha)\) is squarefree. The two places have conjugate ideals. In the first two cases exactly one place divides \(\mathfrak B([\alpha]R)\), and the differential of \([\bar\alpha]\) is a unit there since \(p\ne q\). This makes its exponent equal to \(v_p(B_q)\). In the third case both places have zero exponent in \(\mathfrak B([\alpha]R)\). Consequently \(M_q,C_q\) are coprime positive integers with the respective annihilators stated above. This also shows that choices of sign and conjugation for \(\alpha\) preserve both integers. [CM endomorphism and local denominator calculations](abc_octic_mixed_skew_denominator.md) · [Full annihilator characterization](abc_odd_rank_quartic_cutoff.md)

Write \(P=[a]R,\ Q=[b\tau]R\) and \(\delta=x(P)-x(Q)\in\mathbf Q^\times\). At every odd prime,
\[
                          v_p(\delta)\equiv v_p(M_q)\pmod2.
\]
Indeed on \(E\times E\) the divisor of \(x(P)-x(Q)\) is the diagonal plus the anti-diagonal minus twice each of \(O\times E,E\times O\). The identity holds over the local ring of every odd place, since reduction is good and the function remains nonzero on the generic point of the special fiber. Pull back by the sections \(P,Q\). At the place in question the valuations at the two diagonals are the formal depths of \(P-Q,P+Q\), respectively, and the axes have even coefficients. The points \(P+Q,P-Q\) are conjugates. At a split prime the sum of their depths at a chosen place equals the rational valuation of \(N\mathfrak B(P+Q)\); at an inert prime the common depth is doubled, again giving the rational norm valuation. This proves the parity identity, including primes where one or both arguments enter the formal group. Thus \(\delta/M_q\) is a rational square times a signed power of two.

## A test depending only on the rational prime modulo seven

Take the auxiliary prime \(h=117041\equiv1\bmod8\). Both \(-1\) and 2 are squares in \(\mathbf F_h\). The reduction of \(R\) has order 7. Since \(q\ne7\), all \(B_q,M_q,C_q\) are units here. At finite unequal abscissas, therefore,
\[
  \left(\frac{M_q}{h}\right)=
  \left(\frac{x([a]R)-x([b\tau]R)}h\right).
\]
In the table below the indices \(i,j\in\{1,2,3\}\) represent nonzero residues modulo seven up to sign. The abscissas are \(x([i]R)=-8,1,44791\) and \(x([j\tau]R)=-2,58496,3352\), respectively. Taking quadratic characters of their differences gives
\[
 \begin{pmatrix}-1&-1&-1\\-1&-1&-1\\1&1&-1\end{pmatrix}.
\]
If \(q\equiv5\bmod7\), the possible \((i,j)\) are \((1,3),(2,2)\); at \(q\equiv6\bmod7\), they are \((2,1),(3,3)\). In both fibers every entry is \(-1\).

To find the character of \(B_q\), put \(W_n=\psi_n(R)\bmod h\). The rational integer \(\psi_q(R)\) differs from \(B_q\) only by sign and a power of two at odd \(q\), by integrality and good reduction away from 2. The addition identity at order \(t\) gives \(W_{n+t}W_{n-t}=-W_{t+1}W_{t-1}W_n^2\) at every \(t\nmid n\). Thus the quadratic character has period dividing \(4t\) on nonzero terms. Here \(t=7\); every one of the odd entries prime to 7 in a period 28 has character \(+1\). We get \((M_q/h)=(C_q/h)=-1\) on both rational classes. Each factor therefore contains a prime of odd exponent, and their coprimality proves the claim.

## One smaller auxiliary prime detects half the split primes

At \(h=281\equiv1\bmod8\), the order of \(R\) is 5. For absolute residues \(i,j=1,2\bmod5\), the abscissas are \((-8,1)\) and \((-2,116)\), with difference characters
\[
 \begin{pmatrix}-1&1\\-1&-1\end{pmatrix}.
\]
Again \(\psi_q(R)\) has character one for all odd \(q\) prime to 5, checked in a period 20. The three negative pairs give 12 of the 24 elements in \((\mathcal O/(5))^\times=\mathbf F_{25}^\times\), including both signs of each nonzero coordinate. A generator modulo 5 is counted up to the units \(\{\pm1\}\); these conditions are also invariant under conjugation. The prime ideal theorem in the fixed ray classes of this class-number-one field gives relative density \(1/2\) among rational split primes. Combining just \(h=281\) and \(117041\) gives \(19/24\), by independence at the coprime ray moduli 5 and 7. The test at \(117041\) here uses all its negative entries, which include the two entire fibers above.

## Combining 27 tests

Each row of the verifier specifies a different odd prime \(t\) and a prime \(h\equiv1\bmod8\) at which \(R\) has order \(t\). Exclude the finitely many index primes equal to any \(t\). The verifier checks primality by trial division and verifies \(W_t=0\), sufficient for the order because \(t\) is prime and \(R\) is affine. It tests \(W_n\) on every odd \(n\bmod4t\) and checks that its character there depends only on \(n\bmod t\).

For every \(a+b\tau\in(\mathcal O/(t))^\times\) set \(n=a^2+2b^2\bmod t\). When \(a,b\ne0\bmod t\), the two abscissas are finite; equality would imply \([a\pm b\tau]R=O\) on reduction and hence \([n]R=O\), impossible since \(t\nmid n\). Their difference gives the sign of \(M_q\). The abscissas follow from
\[
 x([j]R)=-8-\frac{W_{j-1}W_{j+1}}{W_j^2},\qquad
 x(\tau P)=-\tfrac12\bigl(x(P)+16+32/x(P)\bigr).
\]
If exactly one of \(a,b\) vanishes modulo \(t\), exactly one point is a pole, as \(\tau\) is invertible on odd torsion. The leading coefficient of \(x\) in a formal parameter at \(O\) is one, so the unit squareclass of \(\delta\) there is \(+1\), including a pole in the second term since \(-1\) is a square at \(h\). This gives the \(M_q\) character in that case too. Multiplying by the character of \(W_q\) gives the \(C_q\) character.

For each \(t\), write \(N_t=|(\mathcal O/(t))^\times|\) and \(u_t,v_t,w_t\) for the fractions of residues giving a positive \(M_q\) character, a positive \(C_q\) character, or both positive characters, respectively. Enumerating both coordinate signs up to abscissa symmetry counts every unit, and the verifier checks the totals \(N_t=(t-1)^2\) for split \(t\), \(N_t=t^2-1\) for inert \(t\). The CRT and prime ideal theorem in the single fixed ray modulus \(\prod t\) make the coordinates at the different \(t\)'s independent in natural density. Sign and conjugation preserve every tested condition, allowing passage from prime generators to rational split primes; prime ideals of residue degree two contribute zero density. The density of the set witnessing both nonsquares, possibly at different auxiliary primes, is exactly
\[
                     1-\prod_tu_t-\prod_tv_t+\prod_tw_t.
\]
Exact rational evaluation places it strictly between \(0.9999999747549\) and \(0.9999999747550\). The bounds apply to this finite set of tests. For the whole split-prime set where both nonsquares occur they give a lower density. [Prime ideal theorem application to signed generators](abc_odd_rank_quadratic_large_gaps.md) · [Verifier and complete list of tests](abc_odd_rank_split_packet_characters.py)
