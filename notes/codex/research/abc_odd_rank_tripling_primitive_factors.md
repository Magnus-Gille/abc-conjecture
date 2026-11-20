# Three separate sources of new primes at every large odd multiple of three

On \(E':y^2=x^3+16x^2+32x\), let \(R=(-8,16)\), \(h=\widehat h(R)\), and let \(B_j\) be the positive square root of the abscissa denominator of \([j]R\). At every sufficiently large odd \(m\), **three disjoint factors of \(B_{3m}\) each have a positive fraction of the whole denominator's logarithm in primes of exact reduction order \(3m\)**. The fractions have explicit asymptotics. At prime \(m=\ell\equiv5\pmod8\) four separate factors of \(B_{3\ell}/9\) have primes of odd valuation, three of exact order \(3\ell\) and one of order \(\ell\). The statements are unconditional.

## Factors and primitive mass

Write the signed primitive slope at odd index \(m\) as \((s:t)\), with \((s:t)=(1:0)\) at \(m=1\). Set \(b=B_m=\sqrt{s^2+2t^2}\) and \(v=\sqrt{s^2-2st+2t^2}\). The [tripling formula](abc_odd_rank_tripling_quality.md) becomes
\[
 \begin{aligned}
 B_{3m}&=b F_m L_m M_m,\\
 F_m&=3s^4+4s^2t^2+12t^4,\\
 L_m&=3s^2-4st+2t^2,\qquad M_m=s^2-4st+6t^2.
 \end{aligned}
\]
Indeed \(F_m=b^4+4b^2v^2-2v^4\), while the other quartic factors as
\[
 b^4-4b^2v^2+6v^4=4v^4-(s^2-2t^2)^2=L_m M_m.
\]
All four factors are odd and have mutually disjoint support outside 3. The only new gcd to check is \((L_m,M_m)=1\). A common odd prime would divide \(v\) and \(s^2-2t^2\). Their squares satisfy \((s^2-2t^2)^2=-b^4+4b^2v^2-2v^4\), contradicting \((b,v)=1\). Each form is positive definite. Thus \(\log T_m=\alpha h m^2+O(1)\) for \((T,\alpha)=(F,4),(L,2),(M,2)\), since \(\log b=hm^2+O(1)\).

Write \(m=3^a n\), \((n,3)=1\). For each of the three choices separately,
\[
  \sum_{\substack{p\mid T_m\\ \operatorname{ord}_p(R)=3m}}
            v_p(B_{3m})\log p
   = \alpha h m^2\prod_{q\mid n}(1-q^{-2})
                   + O(2^{\omega(n)}\log(2m)).                                      \tag{1}
\]
Here \(q\) runs over primes. In particular the lower limiting fraction of \(\log B_{3m}\) in (1) is at least \(\alpha/\pi^2\), since the product over all primes \(q\ge5\) is \(9/\pi^2\).

To prove inheritance in one factor, use \(E:y^2=x^3-8x^2+8x\), its 2-isogeny \(\phi:E\to E'\), the point \(A=(1,1)\) and \(W=(-2\sqrt{-2},8)\). They satisfy \(2W=A,\ \phi(W)=R\). The slope at odd \(j\) is evaluated at \(Q_j=[(j+1)/2]A=W+[j]W\). Its involution \(Q\mapsto2W-Q\) identifies the two signs of \(Q-W\). The slope map has good reduction at the odd primes, as is also seen on its double-cover model with branch polynomial \((x^2+2)((x-1)^2+1)\) of discriminant supported on 2. Alternatively a fixed finite set of primes can be omitted throughout at a cost \(O(\log(2m))\) by formal lifting. [Isogeny and slope reduction](abc_octic_mixed_skew_denominator.md)

If \(p>3\) divides \(B_{3j}\), reduce at a place over \(p\). The reduced \([3j]W\) belongs to \(\ker\phi\), so \([j]W\) has order dividing six. For any positive \((k,6)=1\) it follows that \([kj]W=\pm[j]W\) in reduction. Hence the slopes at \(j\) and \(kj\) coincide projectively modulo \(p\). If \(p\) belongs to a specified one of \(F,L,M\) at either index, it belongs to the same factor at the other. Its valuation increases by \(v_p(k)\) by the elliptic formal group and the disjointness of the factors. This comparison only concerns primes already dividing \(B_{3j}\).

For \(p>3\) dividing \(T_m\), its order divides \(3m\) and does not divide \(m\), because \(p\nmid b\). Its order therefore has the form \(3^{a+1}e\) for \(e\mid n\). If \(G_a(e)\) records the full logarithmic mass of the chosen factor at index \(3^a e\) coming from primes \(p>3\) of exactly that order, the comparison just proved gives
\[
  \log T_{3^a d}=\sum_{e\mid d}G_a(e)+O(\log(2m))
       \quad(d\mid n).
\]
The lifting increments across all primes cost at most \(\log d\), since each uses at most \(v_p(d)\). The discarded prime 3 has order three and \(v_3(B_{3m})=2+v_3(m)\). Möbius inversion and the real size of \(T\) prove (1); the isolated rank-three case is absorbed by the stated error. Since \(2^{\omega(n)}=n^{o(1)}\), (1) supplies three distinct primes of exact rank \(3m\) for all sufficiently large odd \(m\). In particular a fixed set of \(k\) primes can contain the support of \(B_{3m}\) at most \(\lfloor k/3\rfloor\) times beyond that threshold.

## Size and multiplicity of the new primes

Put \(r=3m\), \(e_p=v_p(B_r)\). A prime in each row simultaneously satisfies the displayed inequalities, with exact order \(r\):

| Factor | Lower bound for \(p\) | Lower bound for \(p e_p\) |
|---|---:|---:|
| \(F_m\) | \(\gg r^2/(\log r)^{5/2}\) | \(>r^4/(\log r)^6\) |
| \(L_m\) | \(\gg r^2/(\log r)^5\) | \(>r^4/(\log r)^{11}\) |
| \(M_m\) | \(\gg r^2/(\log r)^5\) | \(>r^4/(\log r)^{11}\) |

In fact these restrictions retain a positive fraction of the full log denominator in each factor. To see this, let \(I_p\) be the exact CM annihilator at a place over \(p\), and \(d=\operatorname N((r)/I_p)\). The total log mass at \(d>(\log r)^u\) is at most \((1/u+o(1))hr^2\). For \(d\le(\log r)^u\) and \(e_p p\le X=r^4/(\log r)^c\), the full mass is \(O(X(\log r)^{2u+1}(\log\log r)^2/r^2)=o(r^2)\) when \(c>2u+1\). Every remaining prime has \(p\gg r^2/(\log r)^u\), by the lattice bound for Frobenius. In (1) choose \(\pi^2/4<u<5/2\) for \(F\), and \(\pi^2/2<u<5\) for the others. The mass remaining after both exclusions is positive. [CM packet distribution and full-multiplicity sieve](abc_odd_rank_quartic_logarithm.md)

## Four odd-valuation witnesses at inert prime indices

If \(m=\ell>3\) is prime, then \(b\) is a 3-unit, and reduction of \(b^2=s^2+2t^2\) modulo 3 forces \(3\mid t\) and \(3\nmid s\). The factor \(M_\ell\) is a 3-unit, while both \(F_\ell\) and \(L_\ell\) are divisible by 3. Each has 3-adic valuation exactly one, since \(v_3(B_{3\ell})=2\). Thus the four factors \(b,F_\ell/3,L_\ell/3,M_\ell\) are pairwise coprime positive integers.

For \(\ell\equiv5\pmod8\), the existing square classification rules out a square for \(b\), and the character modulo 31 rules out a square for \(F_\ell/3\). For the other two factors, at \(\ell=5\) the slope is \((-119:180)\) and
\[
  L_5/3=64321\equiv27\pmod{31},\qquad M_5=294241\equiv3\pmod7 .
\]
These are nonresidues. At 31 and 7 the point \(A\) has order four: \(2A=(49/4,217/8)\) reduces in each case to a nonzero point of order two. Thus \([ (\ell+1)/2 ]A\) has the same reduction as \([3]A\) throughout this residue class. Both forms are homogeneous of degree two, so the projective rescaling of the slope does not affect either character. Each of the four factors therefore supplies a different prime of odd valuation. The prime in \(b\) has exact rank \(\ell\); the other three have exact rank \(3\ell\), by coprimality and \(B_3=9\). [Previous witnesses for the two unsplit factors](abc_octic_mixed_three_factors.md)

For any inert prime \(\ell>3\), every \(p\mid F_\ell/3\) satisfies \(p\ge18\ell^2+1\), and every \(p\mid (L_\ell/3)M_\ell\) satisfies \(p\ge6\ell^2-4\ell+1\). Indeed \(p\) splits in \(\mathbb Q(\sqrt{-2})\), and the inert \(\ell\) forces the full \(\ell\)-torsion to be rational in reduction by the CM action. Write Frobenius \(\pi=1+\ell(a+c\sqrt{-2})\); \(a\) is even and \(c\ne0\). Put \(P=[\ell]R\bmod p\), of order three. The formula \(x([\sqrt{-2}]P)=-(x+16+32/x)/2\) shows \([\sqrt{-2}]P=\pm P\) exactly when \(3x^2+16x+32=0\). This last polynomial vanishes when \(p\) divides \(L_\ell M_\ell\), by substituting \(x=-8v^2/b^2\). At a prime of \(F_\ell/3\), the other quadratic \(x^2+16x-32\) vanishes instead. The two are disjoint at \(p>3\). Then \(P,[\sqrt{-2}]P\) are independent 3-torsion points fixed by Frobenius; consequently \(3\ell\) divides \(\pi-1\) in the CM ring. Its norm formula gives \(p\ge18\ell^2+1\). For either other factor, \(\pi-1\) annihilates a nonzero 3-torsion point, so its norm is divisible by 3. Therefore \(3\mid a^2+2c^2\). If \(a=0\) then \(3\mid c\), and otherwise \(|a|\ge2\). The equality \(p=(1+\ell a)^2+2\ell^2 c^2\) gives the claimed bounds. [CM Frobenius argument](abc_octic_mixed_seed_prime_orbit.md)

At all odd indices tending to infinity, each of \(L_m,M_m\) also has squarefree part tending to infinity. If the squarefree part of one were fixed at \(D\), the slope would lift to the multiquadratic curve on which \(s^2+2t^2\), \(s^2-2st+2t^2\) and the selected quadratic divided by \(D\) are squares. Their three pairs of roots are disjoint: the roots of the first two belong to different imaginary quadratic fields, and the two marked quadratic choices have roots \((2\pm\sqrt{-2})/3\) and \(2\pm\sqrt{-2}\), respectively. These six branch points give an independent degree-eight cover of the slope line of genus five by Riemann–Hurwitz. Faltings gives finitely many rational slopes at each fixed \(D\); the positive odd indices give distinct slopes. A finite union proves the assertion. In particular a fixed finite set of primes cannot account for all the odd valuations in either factor at infinitely many indices. These parity facts allow odd exponents greater than one.

There is also an explicit positive-density set on which all four factors have a prime of valuation exactly one. At \(m=5\) their values are
\[
  b=281,\quad F_5/3=5011329121,\quad L_5/3=131\cdot491,\quad M_5=294241 .
\]
Every displayed factor on the right is prime; trial division through the integer square root suffices, with the largest cutoff 70790. For \(m=5k\) with \(k\) coprime to \(6\cdot281\cdot5011329121\cdot131\cdot294241\), the four primes \(281,5011329121,131,294241\) persist in their respective factors with valuation one. This follows from the slope inheritance for \(F,L,M\) and ordinary formal lifting for \(B_m\). Consequently these four factors simultaneously fail to be powerful for a set of relative density at least \(\frac{2}{15}\prod_{p\in\{281,5011329121,131,294241\}}(1-1/p)>0.13\) among the positive odd indices \(m\). The three inherited primes of the tripling factors here have order 15.
