# Odd prime valuations in the proper CM factor at split prime indices

Let \(K=\mathbb Q(\tau)\), \(\tau^2=-2\), \(\mathcal O=\mathbb Z[\tau]\). On \(E:y^2=x^3+16x^2+32x\), take \(R=(-8,16)\). For \(\alpha\ne0\) in \(\mathcal O\), write \(\mathfrak B_\alpha\) for the odd abscissa denominator ideal of \([\alpha]R\), with exponent \(\max(0,-v_{\mathfrak p}(x([\alpha]R))/2)\) at each odd place. Put \(M(\alpha)=N\mathfrak B_\alpha\). A primitive multiplier \(\alpha=a+b\tau\) has \(\gcd(a,b)=1\).

**Fix \(k\ge2\) and a finite set \(S\) of rational primes. For all sufficiently large norms of primitive multipliers of odd norm, there are two distinct rational primes \(p\notin S\) with \(k\nmid v_p(M(\alpha))\).** In fact \(M(\alpha)\) splits into two explicit coprime factors with asymptotically equal logarithms, and each supplies one prime. The threshold can depend on \(k,S\) and is ineffective. In particular the two largest primes occurring to odd exponent in \(M(\alpha)\) tend to infinity over all primitive odd-norm multipliers. Both coordinates \(a,b\) may vary without restriction.

For each split prime \(q>3\), choose \(\lambda\bar\lambda=q\) in \(\mathcal O\). Its proper CM factor is \(M_q=M(\lambda)=M(\bar\lambda)\). At **every sufficiently large split prime \(q\)**, \(M_q\) has two distinct primes \(p\) of odd valuation, each satisfying
\[
                    p\ge(\sqrt{2q}-1)^2,\qquad p>q.
\]
Thus \(\operatorname{sf}(M_q)\ge(\sqrt{2q}-1)^4=(4-o(1))q^2\). The exact annihilator at one place over each \(p\) is \((\lambda)\) and at the conjugate place it is \((\bar\lambda)\). The same exponents occur in the full scalar denominator \(B_q\). If \(B_q\) is squareful, each of these primes occurs to exponent at least three. For every fixed \(k\ge2\), the corresponding assertion holds with exponents nonzero modulo \(k\). Whether the complementary factor \(C_q=B_q/M_q\) must also have an odd exponent for all sufficiently large split \(q\) is a separate question. [Full and proper factors](abc_odd_rank_quartic_cutoff.md) · [Explicit CM multiplication and denominator conventions](abc_octic_mixed_skew_denominator.md)

## Why the ideal norm preserves individual exponents

For primitive \(\alpha\) of odd norm, \((\alpha,\bar\alpha)=(1)\). A common prime ideal would divide \(2a\) and \(2b\tau\); being away from 2, it would place its underlying rational prime in both \(a\) and \(b\). The CM action over \(K\) extends at every odd prime of good reduction, and conjugation sends the endomorphism \([\alpha]\) to \([\bar\alpha]\). If \(\mathfrak p\) and its conjugate both occurred in \(\mathfrak B_\alpha\), then both \(\alpha\) and \(\bar\alpha\) would annihilate the reduction of \(R\) at \(\mathfrak p\). Bézout's identity in \(\mathcal O\) would force that reduction to be the origin. The affine integral coordinates of \(R\) rule this out. This also excludes an inert prime, which is its own conjugate. Hence every rational prime in \(M(\alpha)\) splits, and just one degree-one place occurs. Its ideal exponent equals \(v_p(M(\alpha))\) exactly. [CM action and good reduction](abc_octic_mixed_cm_prime_mass.md)

## A fixed genus-three cover over the CM field

First take \(k=2\). The first coordinate \(a\) of \(\alpha\) is odd. Choose \(\beta=1\) or \(1+\tau\) according as \(b\) is even or odd. Then \(Q=[(\alpha+\beta)/2]R\) belongs to \(E(K)\); put \(T=[\beta]R\). These points satisfy \(2Q-T=[\alpha]R\). Consider the \(K\)-rational function
\[
               f_T(X)=x(X)-x(X-T).
\]
The four halves of \(T\) are distinct simple zeros, and \(O,T\) are double poles. Indeed \(T\) is nontorsion, equality of the finite abscissas forces \(X=T-X\), and the pole degree is four. After excluding finitely many places depending only on \(T\), these assertions hold on the special fibers, with simple zeros because the residue characteristic is odd. At a pole, the valuation of \(f_T(Q)\) is even. At a zero, the valuation is the intersection multiplicity with the divisor of the halves of \(T\). Since doubling is étale, this equals the formal depth of \(2Q-T=[\alpha]R\). Everywhere else the valuation is zero. Thus outside the fixed exceptional places,
\[
 v_{\mathfrak p}(f_T(Q))\equiv v_{\mathfrak p}(\mathfrak B_\alpha)\pmod2 .
\]
Points at the zeros or poles on the generic fiber account for only finitely many \(\alpha\). [Local abscissa-difference argument on the scalar orbit](abc_odd_rank_squareclass_cover.md)

If the asserted prime were absent, all valuations of \(f_T(Q)\) outside the fixed exceptions and the places over \(S\) would be even, by the one-place property. There are only finitely many such classes in \(K^\times/K^{\times2}\). Indeed \(\mathcal O\) is a PID with units \(\pm1\); one may take representatives comprising a unit times a squarefree product of generators of the finitely many prime ideals. Therefore \(Q\) lifts to one of finitely many fixed covers \(z^2=d f_T(X)\) over \(K\). Each cover branches at four simple zeros over the elliptic base, so it is geometrically connected of genus three. Faltings gives finitely many \(K\)-points on each cover. Distinct \(\alpha\) in a fixed class modulo 2 give distinct \(Q\), since \(R\) is nontorsion and nonzero CM endomorphisms are isogenies. There are only two choices of \(\beta\), proving the assertion. [Faltings's finiteness theorem over number fields](https://doi.org/10.1007/BF01388432)

## Every fixed exponent

Fix \(\alpha\bmod k\mathcal O\), choose a representative \(\beta\), and take \(Q=[(\alpha-\beta)/k]R,\ T=-[\beta]R\), so \([k]Q-T=[\alpha]R\). The divisor \(D=[k]^*(T)\) is reduced of degree \(k^2\) and its elliptic group sum is \([k]T\). Indeed each preimage of \(T\) is a translate of one selected preimage by \(E[k]\), whose elements sum to zero. Thus
\[
           D-k\big((T)+(k-1)(O)\big)=\operatorname{div}(f)
\]
for a \(K\)-rational function \(f\), by the divisor class criterion on an elliptic curve with origin. The \(k\)-th power cover \(z^k=d f\) has full ramification at the \(k^2\) points of \(D\); there its order is \(1\bmod k\), including any coincident pole from the subtracted divisor. All other points are unramified. This gives geometric connectedness, degree \(k\), and genus \(1+k^2(k-1)/2\).

Away from a fixed finite set of places, including those dividing \(k\), the model of the function has trivial vertical divisor and \([k]\) is étale. The valuation of \(f(Q)\) modulo \(k\) therefore equals the intersection multiplicity with \(D\), i.e. the formal depth of \([\alpha]R\) at the identity, interpreted as zero outside the identity disk. Only finitely many \(K^\times/K^{\times k}\) classes have valuations divisible by \(k\) outside the fixed places and the places above \(S\). The genus bound and Faltings again give finiteness, taking all classes of \(\alpha\bmod k\mathcal O\). [Divisor and covering argument](abc_primitive_denominator_twists.md)

## Exact proper factor at a split prime

Set \(J=(0,0),\ W=(4\tau,-16\tau)\). The CM formulas
\[
x([\tau]P)=-\frac{x(P)+16+32/x(P)}2,\quad
y([\tau]P)=\frac{\tau y(P)}4\left(1-\frac{32}{x(P)^2}\right)
\]
give \([\tau]W=R\) and \(\ker[\tau]=\{O,J\}\). Translation by \(J\) gives \(W+J=(-4\tau,-16\tau)=-\bar W\). Write \(U(\alpha)=N\mathfrak B_\alpha(W)\) for the corresponding odd denominator norm based at \(W\). For every primitive odd-norm multiplier one has
\[
          M(\alpha)=U(\alpha)\,U(\bar\alpha),\qquad
          \gcd\big(U(\alpha),U(\bar\alpha)\big)=1.
\]
Indeed \([\alpha]R\) reduces to the origin precisely when \([\alpha]W\) reduces to \(O\) or \(J\). The étale degree-two isogeny \([\tau]\) preserves the depth at both preimages at every odd place. Also \([\alpha]J=J\) since \(a\) is odd and \([\tau]J=O\). Thus the \(J\)-residue contributes the denominator of \([\alpha](W+J)\). Conjugating and negating this point gives the same norm as the denominator of \([\bar\alpha]W\). The reductions \(O,J\) are distinct, and the one-place property for \(M(\alpha)\) promotes disjointness over places to coprimality of the rational integers.

Apply the fixed-exponent covering argument above with nontorsion base point \(W\), then with \(W+J\), in place of \(R\). In either application the odd ideal valuations are carried unchanged into the exponent of just one rational prime, by the factorization and the one-place property for \(M(\alpha)\). Hence each of \(U(\alpha),U(\bar\alpha)\) supplies a prime with exponent nonzero modulo \(k\) outside any fixed \(S\), for all sufficiently large primitive \(\alpha\) of odd norm. Their coprimality makes these primes distinct.

Writing \(N=N\alpha\) and \(h=\widehat h(R)\), the two sizes satisfy
\[
             \log U(\alpha)=hN+O(\log(2N)),\qquad
             \log U(\bar\alpha)=hN+O(\log(2N)).
\]
In fact \(\widehat h(W)=h/2\), so \(h(x([\alpha]W))=hN+O(1)\) for the absolute logarithmic height \(h(x)\). At the complex place, \([\tau\bar\alpha][\alpha]W=[N]R\) stays a fixed positive distance from \(O\) on the bounded real component at odd \(N\). The map \([\tau\bar\alpha]\) scales the flat metric by \(\sqrt{2N}\), so the positive archimedean log of the abscissa is \(O(\log(2N))\), also at the conjugate embedding. At the dyadic place, the fixed sufficiently small formal logarithm ball stable under \(\mathcal O\) excludes \([N]R\) for odd \(N\), hence also \([\alpha]W\). Thus its dyadic abscissa denominator depth is uniformly bounded. The absolute height formula over the imaginary quadratic field now gives the first equality; conjugating \(\alpha\) gives the second. [Height and formal-ball details on this model](abc_octic_mixed_cm_prime_mass.md)

Since \((\lambda)\) is prime, a place counted by \(\mathfrak B_\lambda\) has exact annihilator \((\lambda)\); an annihilator equal to \(\mathcal O\) would make \(R=O\) on reduction. The reduction of \(R\) has ordinary order \(q\), because \(\mathcal O/(\lambda)\) is the field of order \(q\). Together with rational two-torsion this gives \(2q\le\#E(\mathbb F_p)\le(\sqrt p+1)^2\). For split \(q>3\) one has \(q\ge11\), hence \(p>q\). In particular \([\bar\lambda]\) has unit differential at this place and preserves the formal depth of \([\lambda]R\) when applied to give \([q]R\). All other prime divisors of \(B_q\) have exact annihilator \((q)\), since the only remaining candidate proper annihilator is the conjugate prime already detected by the norm. Thus \(B_q=M_q C_q\) with coprime factors and exact valuations throughout. [Annihilator and height formulas](abc_octic_mixed_cm_prime_mass.md) · [Hasse's bound and formal groups](https://doi.org/10.1007/978-0-387-09494-6)

For example direct CM chord arithmetic gives the following factors, taking \(\lambda=a+b\tau\) with \(a,b>0\). The first row exhibits a small exception to the two-prime conclusion.

| \(q\) | \(a,b\) | \(U(\lambda)\) | \(U(\bar\lambda)\) |
|---:|---:|---:|---:|
| 11 | 3, 1 | 1 | 19 |
| 17 | 3, 2 | 43 | 83 |
| 19 | 1, 3 | 73 | 107 |
| 41 | 3, 4 | 29137 | 11777 |

These entries can be obtained by adding \([a]W\) to \([\pm b]R\) and taking the odd square root of the norm of the abscissa denominator ideal. For \(x=(u+v\tau)/w\) with coprime \(u,v,w\) and \(w>0\), that ideal has norm \(w^2/\gcd(w,u^2+2v^2)\). [Norm formula and exact multiplication](abc_odd_rank_quartic_cutoff.md)

## A lower bound at every odd scalar index

Let \(K_k(B_r)=\prod_{p\mid B_r,\ k\nmid v_p(B_r)}p\). Write \(r_s,r_i\) for the products of the distinct split and inert rational prime divisors of \(r\) in \(K\), and \(\omega_s(r),\omega_i(r)\) for their respective counts. For every fixed \(k\ge2\) and \(1<c<4\), uniformly in positive odd \(r\),
\[
 K_k(B_r)\gg_{k,c} c^{\omega_s(r)}\,2^{\omega_i(r)}r_s r_i^2,
 \qquad
 \omega(K_k(B_r))\ge \omega(r)-O_k(1).
\]
In particular \(\operatorname{sf}(B_r)\gg 2^{\omega(r)}\operatorname{rad}(r)\), giving \(\operatorname{sf}(B_r)\gg2^{\omega(r)}r\) at every squarefree odd index.

Indeed for each sufficiently large split prime \(q\mid r\) the two witnesses just constructed have product at least \((\sqrt{2q}-1)^4\ge c q^2\). At every sufficiently large inert \(q\mid r\), apply the scalar covering lemma to obtain one prime \(p\) with \(k\nmid v_p(B_q)\). All these denominator primes split in \(K\); the odd-order reduction of \(R\) is a double, and the duplication formula makes \(-8=x(R)\) a square modulo \(p\). When \(q\) is inert, the exact annihilator over \(K\) is \((q)\), since this ideal is prime and \(R\) is affine integral. Its Frobenius is \(1\bmod(q)\) and has norm \(p=(1+q a)^2+2q^2 b^2\) with \(b\ne0\). Thus \(p\ge2q^2+1\). Across different \(q\), all selected primes are distinct since the ordinary order of \(R\) is exactly \(q\). A selected prime \(p\) either divides \(r_s\) or keeps its original valuation on passage from \(B_q\) to \(B_r\), by formal lifting at the good prime \(p\). Hence their product divides \(r_sK_k(B_r)\). Multiplication gives the first estimate after absorbing the finitely many omitted small \(q\) into the constant. Counting the same primes gives at least \(2\omega_s(r)+\omega_i(r)-O_k(1)\) before subtracting the at most \(\omega_s(r)\) possible divisors of \(r\), which gives the second. [Scalar covering lemma](abc_primitive_denominator_twists.md) · [CM Frobenius and annihilators](abc_odd_rank_quadratic_large_gaps.md)

Likewise for a primitive odd-norm multiplier \(\alpha\) and \(N=N\alpha\),
\[
 K_k(M(\alpha))\gg_{k,c} c^{\omega(N)}\operatorname{rad}(N),
 \qquad \omega(K_k(M(\alpha)))\ge\omega(N)-O_k(1).
\]
Each \(q\mid N\) is split, and exactly one of its conjugate prime ideals \((\lambda)\) divides \((\alpha)\). For large \(q\) its two selected proper primes occur in \(M(\lambda)\); outside \(p\mid N\) the multiplier \([\alpha/\lambda]\) has unit differential and preserves both original depths. These depths carry to the rational norm by the one-place property. Across different \(q\) the scalar orders of \(R\) distinguish the pairs, so their product divides \(\operatorname{rad}(N)K_k(M(\alpha))\). Multiplying the lower bounds \(cq^2\) and counting the pairs give the claims.
