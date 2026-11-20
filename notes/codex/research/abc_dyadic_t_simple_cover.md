# The fixed simple prime in the shifted dyadic packet

Let \(n=2^k\), \(k\ge2\), and \(t_n=u_n^2+16v_n^2\) with the positive primitive coordinates of the dyadic family. Then **\(17\parallel t_n\) at every index**. Thus \(t_n\) has a valuation-one prime on a set of exponents of density one, and \(17\) alone suffices. Write \(T_n=t_n/17\). [Curve and coordinates](abc_octic_dyadic_fermat_audit.md) · [Standard-library verifier](abc_dyadic_t_simple_cover.py)

On \(E':y^2=x^3+16x^2+32x\), put \(R=(-8,16)\). The abscissa \(x=x([n/2]R)=(u_n/v_n)^2\) begins at \(x=1\), and doubling sends it to
\[
 f(x)=\frac{(x^2-32)^2}{4x(x^2+16x+32)}.
\]
Modulo 17, the initial abscissa is fixed, the denominator is a unit, and \(17\nmid v_n\). Put \(h=(x+16)/17\bmod17\). Since \(f(-16)=-49/2\) and \(f'(-16)\equiv-2\bmod17\), the next value is \(8-2h\). Starting at \(h=1\), one obtains \(h=(8-5(-2)^{k-2})/3\bmod17\). A zero would make \((-2)^{k-2}=8/5=5\bmod17\). But \(-2\) is a quadratic residue and 5 is a nonresidue. This proves the exact valuation. In particular \(\operatorname{rad}(t_n)=17\operatorname{rad}(T_n)\) and \(\log(t_n/\operatorname{rad}(t_n))=\log(T_n/\operatorname{rad}(T_n))\) exactly. Writing the original summand \(u_n^2s_n^2t_n=17(u_ns_n)^2T_n\) retains its primitive triple and radical.

An alternative primitive triple comes from cancelling the common divisor 17 in \((u_n^2-v_n^2)+17v_n^2=t_n\):
\[
             (u_n^2-v_n^2)/17 + v_n^2 = T_n .
\]
Move a negative summand to the other side. For \(k>2\) the first summand is nonzero because \(2R\) is nontorsion, and \(\gcd(v_n,T_n)=1\) proves primitivity. Cancellation preserves every prime other than 17. In fact the radical itself is unchanged on \(k\equiv2\pmod8\), and drops by exactly 17 otherwise. Quantitatively, on that progression the new first term has valuation \(1+v_{17}(k-2)\), and elsewhere it is a unit. To see this, \(B=2R=(1,-7)\) has order three modulo 17: doubling it fixes the abscissa and reverses the point. The abscissa difference from \(B\) is a simple local parameter at either lift of its reduction. Its valuation at \([2^{k-2}]B\) is consequently the depth of \([2^{k-2}-(-1)^{k-2}]B\). At \(k=3\) this depth is \(v_{17}(961/196-1)=1\), giving the depth of \([3]B\). Since \(3\mid(-2)^{k-2}-1\), the formal logarithm gives \(v_{17}(u_n^2-v_n^2)=1+v_{17}((-2)^{k-2}-1)\). Finally \(\operatorname{ord}_{17}(-2)=8\) and \((-2)^8-1=15\cdot17\), yielding the claimed valuation after division. This is a different triple from the degree-eight Belyi triple.

## Every finite cover requires 17

For an odd prime \(p\mid t_n\), \([m]R\), \(m=n/2\), has abscissa \(-16\) modulo \(p\). With \(J=(0,0)\) and \(\tau^2=-2\), these points are \(J\pm[\tau]R\). Indeed \([\tau]R=(-2,2\tau)\), and translation by \(J\) sends its abscissa to \(-16\). Thus \([m-\varepsilon\tau]R=J\) for one sign over the residue algebraic closure. Since \(m\) is even and \([\tau]J=O\), multiplication by \(m+\varepsilon\tau\) gives \([m^2+2]R=O\). The order \(r\) of \(2R\bmod p\) is odd because \(v_2(m^2+2)=1\). Hence doubling is periodic from \(2R=(1,-7)\), and returns to that point whenever \(k-2\) is a multiple of the order of 2 modulo \(r\) (use period one for \(r=1\)). For a finite set of occurring primes \(p\ne17\), take a common multiple of these periods. On the resulting progression starting at \(k=2\), the abscissa is 1 at all those primes, so \(t_n/v_n^2\equiv17\) is a unit at each. Primes never occurring can simply be dropped. Consequently every finite prime set misses the support of \(T_n\) on an entire arithmetic progression of exponents. For \(n\ge8\) the cofactor exceeds one since \(v_n\ge14\).

## Small powers and additional simple primes of the cofactor

At \(n=8\), the squared coordinates \((u_n^2,v_n^2)\bmod7\) equal \((2,0)\), fixed under doubling. Hence \(t_n\equiv2\pmod7\) and \(T_n\equiv3\pmod7\) for all \(n\ge8\). The latter residue has order six, proving that no such \(T_n\) is a square or cube. More generally, the verifier rules out all 36 prime exponents \(q\le151\). It divides the residue of \(t_n\) by 17 before testing \(q\)-th powers, and checks every state of the resulting finite orbit. For \(q=139\) the period classes allowed at 557 and 2503 are incompatible; the other tests use one prime each. The exceptional initial cofactor is \(T_4=1\).

There is a second simple prime on a set of exponents of density at least 0.7411228535. For each of 37 distinct odd primes \(d\) in the verifier's table, a prime \(p_d\ne17\) satisfies
\[
 p_d\parallel T_{2^k}\quad\Longleftrightarrow\quad d\mid2k-3 .
\]
For instance the first five pairs \((d,p_d)\) are \((3,241),(5,97),(7,37313),(11,6705793),(13,2820977)\). The verifier runs the abscissa orbit modulo \(p_d\) through \(d\) steps from 1. It returns to 1, and meets \(-16\) exactly in the specified exponent class. On that class the parameter \(h=(x+16)/p_d\bmod p_d\) evolves by an affine transformation \(h\mapsto ah+b\). Evaluating \(f^d\) at \(-16\) and \(-16+p_d\) modulo \(p_d^2\) gives the two coefficients. All denominators are checked to be units. For \(a\ne1\), translation by the fixed point makes this a multiplicative orbit, so a modular-order test decides exactly whether zero is reached. For \(a=1\), the verifier checks that the translation is zero. In every listed case the resulting depth is exactly one. The exact density of this certified union is \(1-\prod_d(1-1/d)\) by the Chinese remainder theorem, since the \(d\) are distinct odd primes. The presence of a simple cofactor prime on the remaining exponents is undetermined.

## Unbounded multiplicity at 12241

Set \(p=12241\) and \(L=2k-3\). For every \(k\ge2\),
\[
v_p(T_{2^k})=
\begin{cases}
0,&7\nmid L,\\
1,&7\mid L,\ 1785\nmid L,\\
2+v_p(L),&1785\mid L.
\end{cases}
\]
Thus for each \(e\ge2\) the exponents with \(p^e\mid T_{2^k}\) form exactly one residue class modulo \(1785p^{e-2}\), with first element \((1785p^{e-2}+3)/2\). The first exponents for depths two and three are 894 and 10,925,094.

The verifier checks that \(f\) modulo \(p\) has period seven at the initial abscissa 1 and encounters \(-16\) just at \(k=5\) on the first cycle. Setting \(h=(x+16)/p\bmod p\) there, the seven-step return is \(h\mapsto-128h+1556\), with initial value 9115. In the first 255 steps exactly step 127 hits zero and step 255 returns to the start. Hence \(p^2\mid t_{2^k}\) precisely when \(k\equiv894\pmod{1785}\).

For the full valuation formula, at a contact put \(m=2^{k-1}\) and choose the sign at a split place of \(\mathbb Q(\tau)\) above \(p\) such that \([m-\varepsilon\tau]R\) reduces to \(J\). The local uniformizer \(x+16\) at \(J+[\varepsilon\tau]R\) has unit derivative because the ordinate is a unit. Thus the depth at \(J\) equals \(v_p(t_n)\). The reduction order \(r\) of \(R\) divides 258 by the contact at \(k=5\); in particular \(p\nmid 2r\). Multiplication by \(2r\) preserves the depth and yields \([2(m-\varepsilon\tau)][r]R\). In the formal logarithm the resulting depth is \(d_p+v_p(m-\varepsilon\tau)\), taking the embedding on differentials, where \(d_p\) is the depth of \([r]R\). The calculation at \(k=5\) gives \(d_p=1\), as \(m^2+2=258\) is a unit. Whenever depth exceeds one, the conjugate multiplier is a unit, so \(v_p(t_n)=1+v_p(m^2+2)=1+v_p(2^L+1)\). The elementary finite checks \(\operatorname{ord}_p(2)=510\) and \((2^{255}+1)/p\equiv2714\pmod p\) give \(v_p(2^L+1)=1+v_p(L)\) by lifting the exponent on the deep progression. This proves the claim.
