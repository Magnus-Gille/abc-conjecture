# Odd first depths at every large Gaussian ideal on a fixed prime support

Let \(K=\mathbf Q(i)\), \(\mathcal O=\mathbf Z[i]\), \(E_6:y^2=x^3-36x\), and \(G=(-3,9)\). Given a finite set of odd Gaussian primes, **every sufficiently large ideal \(J\) supported on them** is the exact Gaussian annihilator of the reduction of \(G\) at some good prime ideal of \(K\) at which the corresponding first denominator depth is odd. The place can avoid any additional fixed finite set. Here the first depth is the local formal depth of \([\gamma]G\) with \((\gamma)=J\). The threshold from Faltings's theorem is ineffective in this proof.

For an odd rational prime \(q\equiv1\pmod4\), it follows that at least \(e+1\) distinct rational primes of exact reduction order \(q^e\) have odd first depth, for all sufficiently large \(e\). The full \(B_{q^e}\) has at least \((e+1)(e+2)/2-O_q(1)\) distinct primes to odd exponent. This applies to every split \(q\) irrespective of cubic character conditions. The following version also gives primes in every odd index with a prescribed collection of small-prime factors of its reduction orders.

Fix a finite set \(S\) of odd rational primes. For any odd positive \(n\), put \(n_S=\prod_{q\in S}q^{v_q(n)}\), \(d_n=\operatorname{sf}(B_n)\), where \(B_n^2\) is the reduced abscissa denominator of \(nG\). Define
\[
   H_S(n)=\frac{\tau(n_S)+\tau_{\mathcal O}((n_S))}{2},\qquad
   \tau_{\mathcal O}((n_S))=
      \prod_{q^e\parallel n_S,\ q\equiv1\ (4)}(e+1)^2
      \prod_{q^e\parallel n_S,\ q\equiv3\ (4)}(e+1).
\]
Then
\[
       \omega(d_n)\ge H_S(n)-O_S(1),\qquad
       \log d_n\ge H_S(n)\log(2n_S)-O_S(1).                         \tag{1}
\]
The proof uses CM on the two-isogenous curves, geometric branch divisors and Faltings over a fixed number field. It does not require the prime-index square classification. [Rational-index version](abc_congruent_six_all_indices_odd_support.md) · [Local Gaussian annihilators](abc_congruent_six_odd_primitive_counts.md)

## A function which detects the parity of a Gaussian denominator ideal

Let \(E_0:Y^2=X^3+36X^2+36X\), \(P=(-2,8)\), and use the rational two-isogeny \(\phi:E_0\to E_6\) with coordinates \(((X+12+36/X)/4,\ Y(1-36/X^2)/8)\). Then \(\phi(P)=G+T_+\) for \(T_+=(6,0)\), and \(\phi^{-1}(T_+)=\{T,-T\}\) for \(T=(6,24\sqrt3)\). The latter has order four; doubling gives the nonidentity point \((0,0)\). Thus \(6-X\) has divisor \(T+(-T)-2O\). [Quartic parametrization](abc_full_quartic_signature.md)

Every odd Gaussian ideal \(A\) has a generator \(\alpha=a+bi\) with \(a\) odd and \(b\) even, unique up to sign. On \(E_0\) it acts via \([a]+[b/2]\widehat\phi[i]\phi\), where \(\widehat\phi\) is the dual and \([i](x,y)=(-x,iy)\) on \(E_6\). This action intertwines \(\phi\) with the Gaussian action. It has degree \(N\alpha\), as is clear by composing with \(\phi\) and using its degree two. It also permutes \(T,-T\), since \([\alpha]\) acts as the identity on \(E_6[2]\), and its kernel has odd order. For every odd generator \(\beta\) of the same parity convention, one has
\[
                 \phi([\beta]P)+T_+=[\beta]G.
\]
Over any prime \(\mathfrak p\nmid6\) of \(K\), the reduction of the isogeny is étale. If \([\beta]G\) is formal, the point \([\beta]P\) is near exactly one of \(\pm T\); their abscissa difference from 6 is an étale parameter because their ordinates are units. A finite unramified extension adjoining \(\sqrt3\) preserves the valuation when needed. Thus \(v_{\mathfrak p}(6-X([\beta]P))\) equals the formal depth of \([\beta]G\). Otherwise this valuation is zero except when \([\beta]P\) is formal, in which case it is even from the double pole. In all cases
\[
       v_{\mathfrak p}(6-X([\beta]P))\equiv
                v_{\mathfrak p}\mathfrak B([\beta]G)\pmod2.            \tag{2}
\]
Here \(\mathfrak B\) is the denominator ideal with the square-root convention. Formula (2) retains parity at a single Gaussian place even when the total rational norm has even valuation.

## The double covers

For an odd ideal \(I\ne\mathcal O\) choose the stated generators \(\alpha_A\) at its divisors and let
\[
       F_I(R)=\prod_{A\mid I}(6-X([\alpha_A]R))^{\mu(I/A)}
                 \in K(E_0)^\times .
\]
Generator signs do not affect this formula. In characteristic zero the odd branch divisor is exactly the collection
\[
        \{\ T+U,-T+U:\ U\text{ has exact Gaussian annihilator }I\ \}.
\]
Indeed the zeros for a single divisor \(A\) are those translates of \(\ker[\alpha_A]\), all simple. Its poles are double at odd-order torsion points, disjoint from the translated zeros. On odd torsion, \(\phi\) is an isomorphism onto the odd torsion of \(E_6\), so one may use its full \(\mathcal O\)-module structure. The torsion killed by \(A\) is \(\mathcal O/A\); this follows, for example, from complex uniformization by a lattice homothetic to \(\mathcal O\). Möbius inversion selects exact annihilator \(I\). Thus there are \(2\varphi_K(I)\) branch points, with \(\varphi_K(I)=N I\prod_{\lambda\mid I}(1-1/N\lambda)\). The translates are disjoint since \(2T\) has order two. For each \(D\in K^\times/K^{\times2}\) the smooth projective double cover \(z^2=D F_I(R)\) is geometrically connected of genus \(1+\varphi_K(I)>1\) by Riemann–Hurwitz. Therefore only finitely many \(K\)-points of \(E_0\) give a nonzero finite value of \(F_I\) in any prescribed finite collection of squareclasses. [Faltings](https://doi.org/10.1007/BF01388432)

Fix any finite set of places containing the bad primes, all primes above \(NI\), and any desired exclusions. The squareclasses with even valuations outside this set form a finite group by the unit theorem and the finiteness of the class group. Hence for all but finitely many odd Gaussian generators \(\beta\), some \(\mathfrak p\) outside this set has \(v_{\mathfrak p}(F_I([\beta]P))\) odd. The base points are distinct for distinct \(\beta\), since a nonzero endomorphism has finite kernel and \(P\) is nontorsion. None of these evaluations meets a zero or pole, which are torsion.

For such a place the exact Gaussian annihilator of \([\beta]G\) modulo \(\mathfrak p\) is \(I\). To check this, let \(J_0\) be that annihilator. For \(A\mid I\) with \(J_0\nmid A\), the denominator depth is zero. If \(J_0\mid I\) the depth at all \(A\mid I\) divisible by \(J_0\) is the same, because the Gaussian scalar given by the quotient \(A/J_0\) has degree prime to the residue characteristic, and preserves formal depth. In this situation \(J_0\) has odd norm and its generator may use the same convention as the others. Formula (2) and ideal Möbius inversion now show that the odd valuation is possible only for \(J_0=I\), with odd depth at \([\alpha_I\beta]G\).

Let \(J\) vary over ideals supported on a fixed finite set of odd Gaussian primes. Set \(I=\operatorname{rad}(J)\) and take \((\beta)=J/I\). There are only finitely many possible \(I\), so the same conclusion holds for every sufficiently large \(J\), with the excluded places including all its fixed support. If \(L\) denotes the annihilator of \(G\) at the selected place, the annihilator of its \(\beta\)-multiple equals \(L/\gcd(L,(\beta))\). The equality with \(I\) forces \(L=J\), by comparing valuations one prime ideal at a time. Since \((\alpha_I\beta)=J\), the first depth at \(J\) is odd, proving the first assertion.

## Rational primes and growing multiplicities

Every resulting rational prime is split in \(K\). Indeed an odd Gaussian generator annihilating \(G\) at the place also yields an odd **integer** annihilator by multiplying by the Gaussian conjugate. Hence the rational prime divides an odd scalar denominator and is \(1\bmod12\). The two places of \(K\) over such a prime have conjugate annihilator ideals since \(G\) is rational. Thus realizing two nonconjugate ideals requires different rational primes. For an \(S\)-smooth rational rank \(n\), the odd ideals \(J\) with \(J\cap\mathbf Z=(n)\) give precisely \(\prod_{q^e\parallel n,\ q\equiv1\ (4)}(2e+1)\) choices: at split \(q\) the larger of the two exponents is \(e\), and at inert \(q\) the exponent must be \(e\). Only \((n)\) is fixed by conjugation. Each \(J\) has \(N J\ge n\), so for all sufficiently large \(n\) they are all eligible for the theorem. Their conjugacy classes give at least
\[
     \frac{1+\prod_{q^e\parallel n,\ q\equiv1\ (4)}(2e+1)}2
\]
primitive odd-valuation rational primes of exact order \(n\). The additional multiplier between \(J\) and \((n)\) is a local unit at the selected place since all places above \(S\) were excluded.

For arbitrary odd \(n\), put \(u=n/n_S\) and take every nonunit ideal \(J\mid(n_S)\). With \(I=\operatorname{rad}(J)\), use \((\beta)=(u)J/I\) and exclude all places over \(6\prod_{q\in S}q\). The argument yields a good place where the part of the annihilator of \(G\) supported above \(S\) is exactly \(J\), by comparing valuations in \(L/\gcd(L,(\beta))=I\). All remaining factors of \(L\) divide \((u)\). The depth at \([\alpha_I\beta]G\) is odd. The extra multiplier leading to \(nG\) generates \((n_S)/J\) and is prime to this place. Thus its rational prime actually divides \(B_n\) to odd exponent, and different ideal conjugacy classes of \(J\) require different primes. Only bounded \(J\) can be missed, because \(I\) ranges over a finite list and the exceptional \(\beta\) in each list form a finite set. When \(u\) tends to infinity all nonunit \(J\) are covered.

The rational reduction group at the selected split prime contains the module \(\mathcal O/L\), of odd order \(NL\ge NJ\), together with its disjoint rational two-torsion of order four. Hence \(p\ge(2\sqrt{NL}-1)^2>2NJ\), since \(NJ\ge3\). Conjugation on divisors of \((n_S)\) fixes precisely the \(\tau(n_S)\) rational ideals, giving \(H_S(n)\) conjugacy classes. The involution \(J\mapsto(n_S)/J\) on these classes pairs norms with product \(n_S^2\), including any fixed classes of norm \(n_S\). Therefore their total weight \(\sum\log(2NJ)\) is \(H_S(n)\log(2n_S)\). The missed classes have bounded total weight, proving (1).
