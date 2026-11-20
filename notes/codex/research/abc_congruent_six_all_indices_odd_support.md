# Pointwise odd-valuation primes from the ordered divisors of an elliptic index

Take \(G=(-3,9)\) on \(E_6:Y^2=X^3-36X\). For \(n>0\) odd let \(B_n^2\) be the reduced denominator of \(x(nG)\), and let \(d_n=\operatorname{sf}(B_n)\) be the squarefree product of its odd-valuation prime factors. All such primes are \(1\bmod12\). The prime-index nonsquare theorem says \(d_q>1\) for every odd prime \(q\). [Square classification](abc_full_quartic_square_classification.md) · [Orbit and prime support](abc_full_quartic_signature.md)

There are absolute constants \(c>0,C>1\) for this orbit such that for every odd \(n>1\), letting \(k=\omega(d_n)\),
\[
  \Omega(n)\ll C^k,\qquad \log n\ll C^k\log d_n,
  \qquad \log d_n\gg (\log\log n)(\log\log\log n)
\]
where the last estimate is for large \(n\). In particular, for each fixed bound on \(\omega(d_n)\), the squarefree kernel grows at least as a fixed positive power of the index. For every **fixed** odd prime \(q\) the stronger inequality
\[
                   \log d_n\gg_q v_q(n)^2\log q                    \tag{1}
\]
holds at every index divisible by \(q\). Thus for each fixed finite set of primes \(S\), the \(S\)-smooth odd indices satisfy \(\log d_n\gg_S(\log n)^2\). The constants in (1) can be constructed independently of uniform Mordell–Lang. Here \(\Omega\) counts primes with multiplicity and \(\omega\) counts distinct primes.

## Descending prime factors

For a good prime \(p\mid B_m\) at an odd index let \(r_p=\operatorname{ord}(G\bmod p)\). It is an odd divisor of \(m\) greater than one, since \(G\) is finite and integral at every good prime. The four rational two-torsion points give \(4r_p\mid\#E_6(\mathbf F_p)\). Hasse gives \(p\ge(2\sqrt{r_p}-1)^2>2r_p\), the last inequality holding for \(r_p\ge3\). At a multiple of \(m\) the formal logarithm gives
\[
              v_p(B_{mh})=v_p(B_m)+v_p(h).
\]
The primes 2 and 3 do not occur at odd indices.

Write out \(q_1\ge q_2\ge\cdots\ge q_s\), the prime divisors of \(n\) with all multiplicities, and set \(m_j=\prod_{a=1}^j q_a\), including \(m_0=1\). Every \(p\mid B_{m_j}\) exceeds \(2q_j\), since every factor of \(r_p\) divides \(m_j\). All primes in \(n/m_j\) are at most \(q_j\). Hence \(\gcd(B_{m_j},n/m_j)=1\) and every valuation already seen along this chain survives unchanged. Consequently
\[
                          1=d_{m_0}\mid d_{m_1}\mid\cdots\mid d_n.    \tag{2}
\]

There are at most \(A^{1+\omega(D)}\) positive odd indices with \(d_m=D\), for a constant \(A>1\) independent of \(D\). In the [fixed-squareclass calculation](abc_full_quartic_square_denominators.md) the corresponding positive slope \(r\) gives a rational point on
\[
 Z^2=-2D(r^2+3)(r^4-18r^2+9).
\]
The right side has six distinct roots. Distinct positive indices produce distinct \(r\), since \(X(mP)=-2r^2\) for the original infinite-order point \(P\). This genus-two Jacobian is isogenous over \(\mathbf Q\) to \(A_D\times A_{3D}\) where \(A_t:Y^2=X^3+48tX^2+288t^2X\); its two quotient maps and independence of the pullback differentials are given in the cited calculation. On each of the two elliptic curves the ordinary two-isogeny descent bounds both abscissa squareclass images by signed squarefree products of primes dividing \(6D\), since the original and dual final coefficients are \(288t^2\) and \(1152t^2\). Thus the Jacobian rank is \(O(1+\omega(D))\). The uniform Mordell–Lang bound for curves with a rational point bounds the number of their rational points by a genus-dependent constant raised to one plus the rank. [Dimitrov, Gao and Habegger](https://arxiv.org/abs/2001.10276)

Distinct squareclasses in (2) have distinct values of \(\omega\). Therefore \(s+1\le\sum_{i=0}^{k} A^{1+i}\ll A^k\). The term \(d_{q_1}>1\) has a prime greater than \(2q_1\); in particular \(\log n\le s\log q_1\ll A^k\log d_n\). Put \(x=\log d_n\); the factorial lower bound for a product of \(k\) distinct primes gives \(k\ll x/\log(2+x)\). Thus \(\log\log n\ll x/\log(2+x)+\log(2+x)\), yielding the stated lower bound on \(x\).

At each \(j\ge1\), applying the same chain estimate to \(m_j\), using \(d_{m_1}>1\) for small \(j\), gives at least \(c\log(j+1)\) primes in \(d_n\) exceeding \(2q_j\). Integrating this tail with respect to logarithmic size, or summing over the successive intervals between \(\log q_j\), gives
\[
 \log d_n \gg \sum_{j=1}^s (\log q_j)\log(1+1/j)
       \gg\sum_{j=1}^s\frac{\log q_j}{j}
       \ge \frac{\log n}{s}\sum_{j=1}^s\frac1j.
\]
The last inequality is Chebyshev's sum inequality for two decreasing sequences.

## A new prime at each multiplication in the classes 3 and 5 modulo 8

At every positive odd index, \((2/B_m)=(2/m)\). [Character identity and proof](abc_gaussian_quartic_odd_cofactors.md) When \(q_j\equiv3,5\bmod8\), the positive quotient \(B_{m_j}/B_{m_{j-1}}\) has character \(-1\) at 2. The valuations of every old prime have been preserved, so a new prime \(p_j\equiv13\bmod24\) occurs to odd exponent and persists unchanged to \(B_n\). On the \(h\)-th occurrence of the prime \(q=q_j\) the order \(r_{p_j}\) divides \(m_j\) but not \(m_{j-1}\), hence \(q^h\mid r_{p_j}\), and \(p_j>2q^h\). The primes thus selected at the different steps are distinct. Consequently one has the elementary pointwise bound
\[
       d_n\ge \prod_{\substack{q^e\parallel n\\q\equiv3,5\ (8)}}
                     2^e q^{e(e+1)/2}.                               \tag{3}
\]
For \(q\equiv3\bmod8\) one may replace \(q^{e(e+1)/2}\) by \(q^{e(e+1)}\). In fact \(p_j\) splits in \(\mathbf Q(i)\), and the Gaussian annihilator \(I\) of the reduced \(G\) has \(I\cap\mathbf Z=(r_{p_j})\). As \(q\) is inert, \(q^{2h}\mid NI\). The odd-order Gaussian module \(\mathbf Z[i]/I\) and rational two-torsion give \(4NI\mid\#E_6(\mathbf F_{p_j})\). Hence \(p_j\ge(2q^h-1)^2>2q^{2h}\). [Gaussian annihilator computation](abc_congruent_six_gaussian_first_primes.md)

## Extending prime-power growth to all prime bases

First fix any odd prime \(q\). Choose a rational prime \(\ell>3\) with
\[
      \ell\equiv3\pmod4,\qquad \ell\equiv1\pmod q,
              \qquad (d_q/\ell)=-1.
\]
Such primes exist by Dirichlet and CRT. The squarefree \(d_q>1\) is prime to \(q\) with every prime divisor \(1\bmod4\). Prescribe a nonresidue at one prime dividing \(d_q\) and units of square character at the others, then use reciprocity. Linnik gives an effective size estimate \(\ell\ll(4q d_q)^L\) with an absolute exponent. All odd denominators are units at \(\ell\). On the original model \(E:Y^2=X^3+36X^2+36X\), put \(T=\operatorname{ord}(P\bmod\ell)\), \(P=(-2,8)\). Because this curve is isogenous to \(E_6\), its order over \(\mathbf F_\ell\) equals \(\ell+1\) by the trace-zero character sum for primes \(3\bmod4\). In particular \((T,q)=1\).

The sign \((B_m/\ell)\) at an odd index depends only on \(m\bmod T\). At finite \(X(mP)\) it equals the character of \(8(6-X(mP))\), using the primitive-slope formula \(B_m=(x^2+3y^2)/4=y^2(6-X(mP))/8\). No odd index at this prime has \(X=6\), since \(\ell\nmid B_m\); at the identity its character is one. These tests are proved in the [squareclass-sieve calculation](abc_full_quartic_square_denominators.md). Since \((B_1/\ell)=1\), \((B_q/\ell)=-1\), one has \(T>1\) and \(t=\operatorname{ord}_{T}(q)\ge2\). For each \(h\equiv1\bmod t\), the two values at \(q^{h-1}\) and \(q^h\) again have opposite signs. The integer \(B_{q^h}/B_{q^{h-1}}\) therefore has an odd-valuation prime. All prime valuations from the previous term have been preserved by (2), hence each such prime is new and of exact order \(q^h\). Distinct \(h\) give distinct primes, each greater than \(2q^h\). Their product through \(h\le e\) yields
\[
              \log d_{q^e}\ge(\log q)\sum_{\substack{h\le e\\h\equiv1\ (t)}}h
                            \gg_t e^2\log q.
\]
For example the last implicit constant may be taken as \(1/(4t^2)\) uniformly for \(e\ge1\), by putting \(H=\lceil e/t\rceil\) and using that the sum is at least \(H(H+1)/2\).

Finally \(d_n\ge d_{q^e}\) as positive integers whenever \(q^e\mid n\). To prove this, choose once for each odd prime \(u\) some prime \(f(u)\mid d_u\). Its reduction order is exactly \(u\), so \(f\) is injective and \(f(u)>2u\). For each \(p\mid d_{q^e}\), start a path at \(p\). If \(p\nmid d_n\), its odd depth must have changed between \(q^e\) and \(n\), which requires \(p\mid n\). Advance to \(f(p)\). If this new prime is also absent from \(d_n\), it divides \(n\) by the same lifting formula, now applied from index \(p\). Continue until a vertex in \(d_n\) is reached. This terminates since every nonterminal vertex divides \(n\) and the path increases. No path can meet another: injectivity would make one start a downstream vertex of the other, but every start has \(q\)-power order and exceeds \(q\), while every downstream vertex has reduction order equal to its preceding prime, which exceeds \(q\). Thus the distinct terminals in \(d_n\) dominate all the initial prime factors and give the claimed product bound. This proves (1). If \(n\) has fixed finite prime support \(S\), sum the resulting inequalities \(v_q(n)\log q\ll_q\sqrt{\log d_n}\) over \(q\in S\) to obtain the stated smooth-index consequence.

## Every sufficiently large fixed-support rank has a primitive odd-valuation divisor

Fix an odd integer \(s>1\), write \(P=(-2,8)\) on the original curve \(E:Y^2=X^3+36X^2+36X\), and put
\[
        H_s(R)=\prod_{a\mid s}(6-X([a]R))^{\mu(s/a)}\in\mathbf Q(E)^\times.
\]
For each fixed nonzero squarefree \(D\), the smooth projective curve obtained from \(z^2=D H_s(R)\) has genus \(1+J_2(s)\), where \(J_2(s)=s^2\prod_{q\mid s}(1-q^{-2})\). Indeed the divisor of \(6-X\) is \(T+(-T)-2O\), where \(T=(6,24\sqrt3)\) has order four: its double has abscissa zero by duplication and is the nonidentity two-torsion point. Odd multiplication permutes \(T,-T\), so the zeros of \(6-X([a]R)\) are exactly \(\{T,-T\}+E[a]\), with simple multiplicity. Its poles have even multiplicity. The two translates of \(E[s]\) are disjoint since \(2T\) has order two. At a point \(\pm T+U\) with \(U\in E[s]\) of order \(v\), the net zero multiplicity after Möbius inversion is \(\sum_{v\mid a\mid s}\mu(s/a)=\mathbf1_{v=s}\). These points cannot also be poles since they have even order whereas \([a]^{-1}O\) has odd order. Thus the double cover branches at exactly \(2J_2(s)\) geometric points and is connected. Riemann–Hurwitz over the elliptic base gives the asserted genus.

For positive odd \(m\) the value \(H_s(mP)\) has squareclass equal to that of
\[
                  U_s(m)=\prod_{a\mid s} B_{am}^{\mu(s/a)}.
\]
This follows from \(6-X(jP)=8B_j/y_j^2\) in primitive slope coordinates, and \(\sum_{a\mid s}\mu(s/a)=0\). All evaluations are finite and nonzero since the orbit is nontorsion. Faltings's theorem on each of the finitely many twists with squareclasses supported on a fixed prime set implies that only finitely many such \(m\) have \(U_s(m)\) in those squareclasses. Distinct \(mP\) are distinct base points. [Faltings's theorem](https://doi.org/10.1007/BF01388432)

For \(p\nmid 6s\), let \(v=\operatorname{ord}(mG\bmod p)\). If \(v\nmid s\) all terms in the valuation of \(U_s(m)\) vanish. If \(v\mid s\), at precisely the \(a\) divisible by \(v\) one has \(v_p(B_{am})=v_p(B_{vm})\), since \(p\nmid a/v\); this includes \(v=1\). Möbius inversion now gives
\[
                v_p(U_s(m))=\mathbf1_{v=s}\,v_p(B_{sm}).
\]
Exclude the fixed primes dividing \(6s\). Faltings therefore shows that every sufficiently large \(m\) supplies a prime of odd valuation in \(B_{sm}\) with \(\operatorname{ord}(mG\bmod p)=s\). The squarefree product of such prime factors outside any fixed finite set tends to infinity, by the same argument with a larger excluded set. In the prime case \(s=q\) the genus is \(q^2\) and the conclusion says the quotient \(B_{qm}/B_m\) is a square at only finitely many \(m\). This stronger, ineffective conclusion contrasts with the explicit period mechanism in (1).

Let \(S\) be any fixed finite set of odd primes and let \(v>1\) have all prime factors in \(S\). Set \(s=\operatorname{rad}(v)\), \(m=v/s\). Only finitely many \(s\) can occur. A prime with \(\operatorname{ord}(mG\bmod p)=s\) has \(r_p=v\): for every \(q\mid v\), the identity \(r_p/\gcd(r_p,m)=s\) forces \(v_q(r_p)=v_q(m)+1\); other prime factors cannot occur in \(r_p\) since \(r_p\mid v\). Hence every sufficiently large \(S\)-smooth \(v\) has a prime \(p_v>2v\) of exact rank \(v\) with **odd first depth**. The squarefree product of such primitive odd-valuation primes tends to infinity on these ranks. The finite exceptional ranks need not have been identified for this conclusion.

This yields distinct actual odd-valuation primes on every odd index, independently of the prime-index square classification. Put \(n_S=\prod_{q\in S}q^{v_q(n)}\), \(u=n/n_S\). For each \(d\mid n_S\), \(d>1\), use the same construction at \(s=\operatorname{rad}(d)\) and \(m=ud/s\), excluding all primes in \(S\). Once \(m\) exceeds the finite threshold, there exists \(p_d\notin S\) with odd exponent in \(B_{ud}\) and \(\operatorname{ord}(mG\bmod p_d)=s\). Since \(u\) is prime to every \(q\in S\), the **part supported on \(S\)** of \(\operatorname{ord}(G\bmod p_d)\) is exactly \(d\). This follows at \(q\mid d\) as in the preceding paragraph and at the other primes from \(r_{p_d}\mid ud\). Thus the selected primes are distinct for different divisors. Passing from \(ud\) to \(n\) preserves their odd valuations since the extra multiplier is supported on \(S\). The finite exceptional \(m\) can affect only bounded \(d\), as \(d\le sm\) and \(s\mid\prod_{q\in S}q\). If \(u\) is sufficiently large every \(d>1\) is available. Hasse gives \(p_d>2r_{p_d}\ge2d\), so uniformly in \(n\),
\[
 \omega(d_n)\ge\tau(n_S)-O_S(1),\qquad
 \log d_n\ge\tfrac12\tau(n_S)\log n_S+\tau(n_S)\log2-O_S(1).          \tag{4}
\]
The omitted divisors have bounded total count and logarithmic weight and \(\prod_{d\mid n_S}d=n_S^{\tau(n_S)/2}\).

There is also a refinement of the weight in (4). Write \(v_{\mathrm{in}}=\prod_{q^a\parallel v,\ q\equiv3\bmod4}q^a\) and similarly for \((n_S)_{\mathrm{in}}\). For every selected prime whose rank is divisible by \(v\), the same Gaussian annihilator argument used for (3) gives \(NI\ge v v_{\mathrm{in}}\). Indeed the rational order divides the norm, with an additional full copy of each inert rational prime power. Hasse gives \(p_v>2v v_{\mathrm{in}}\), and thus the right side of the logarithmic bound in (4) gains \(\tfrac12\tau(n_S)\log (n_S)_{\mathrm{in}}\), up to an additive constant depending only on \(S\). None of these lower bounds is on the full logarithmic scale \(\log B_n\asymp n^2\).
