# Factor layers and moving prime squares in the modulus-24 transfer

Let \(s=x^4,t=y^4\) for coprime positive \(x,y\) with \(x\) odd, \(y\) even. Put \(\omega=(-1+\sqrt{-3})/2\), \(\alpha=s+\omega t\), \(\alpha^{12}=P+Q\sqrt{-3}\), \(W=s^2-st+t^2\), \(C=W^{12}\), and \(R=\operatorname{rad}(3PQW)\) with absolute values understood. The [transfer construction](./abc_eisenstein_power_conic.md) gives positive primitive coordinates \((|P|,|Q|,W)\). Write \(h=\max(x,y)\).

## Exact support

The following forms have arguments \(s,t\):
\[
\begin{split}
 A&=s^4-8s^3t+6s^2t^2+4st^3-2t^4,\\
 B&=s^4+4s^3t-12s^2t^2+4st^3+t^4,\\
 K&=2s^4-4s^3t-6s^2t^2+8st^3-t^4,\\
 E&=s^2-4st+t^2,\qquad J=s^2+2st-2t^2,\qquad G=2s^2-2st-t^2 .
\end{split}
\]
Direct expansion gives
\[
 2P=ABK,\qquad
 2Q=3st(s-t)(s+t)(s-2t)(2s-t)EJG.
\]
Let \(F\) be the product of the following fifteen homogeneous forms, each taken once.

| Degree | Factors in \(x,y\), with \(s=x^4,t=y^4\) |
|---|---|
| 1 | \(x,y,x-y,x+y\) |
| 2 | \(x^2+y^2\) |
| 4 | \(s-2t,s+t,2s-t\) |
| 8 | \(E,J,G,W\) |
| 16 | \(A,B,K\) |

Then \(\deg F=98\), \(R=\operatorname{rad}(F(x,y))\), and exactly
\[
            \prod_{f\mid F\ {\rm in\ table}}\operatorname{rad}(f(x,y))=8R.
\]
For odd \(p>3\), a projective input modulo \(p\) belongs to at most one of the fifteen factors. Indeed the target directions correspond to the distinct roots of \(z^{24}=1\), together with \(z=0,\infty\), by the Möbius change \(z=(s+\omega t)/(s+\bar\omega t)\) of determinant a unit there. Pulling back by the fourth power is separable away from \(0,\infty\), and its reduced fibers at those two points are simple singletons. Thus \(F\bmod p\) is geometrically squarefree. At 3 exactly one of \(x,y,x-y,x+y\) is divisible by 3, and every other factor is a unit, as is seen at \((s,t)\bmod3=(0,1),(1,0),(1,1)\). At 2 exactly \(y,2s-t,G,K\) are even, the last three to depth one. The denominators of 2 in the formulas for \(P,Q\) do not remove 2 from \(R\).

Before the fourth-power substitution the reduced support \(F_0(s,t)\) consists of six linear forms \(s,t,s-t,s+t,s-2t,2s-t\), four quadratic forms \(E,J,G,W\), and three quartics \(A,B,K\). Its degree is 26 and \(\operatorname{rad}(F_0)=\operatorname{rad}(3PQW)\) on primitive integral admissible inputs with \(s\) odd, \(t\) even and \(3\nmid W\).

## Orders and root fields

Away from the characteristic primes \(2,3\), the order of \(z\) selects the factor of \(P\) or \(Q\) as follows:

| Order | Homogeneous layers before substitution |
|---|---|
| 1, 2 | \(t,\ 2s-t\), respectively |
| 3, 6 | \(s(s-t),\ (s-2t)(s+t)\), respectively |
| 4, 12 | \(G,\ EJ\), respectively |
| 8, 24 | \(K,\ AB\), respectively |

The roots of \(W\) are the zero and pole of \(z\). For \(\zeta\ne1\) in \(\mu_{24}\), the corresponding target coordinate is
\[
 u=\frac{s}{t}=\frac{\omega-\zeta\bar\omega}{\zeta-1}.
\]
It is real and \(\mathbf Q(\omega,u)=\mathbf Q(\omega,\zeta)\). For orders 4 or 12 its root field is \(\mathbf Q(\sqrt3)\), and for orders 8 or 24 it is \(\mathbf Q(\zeta_{24})^+=\mathbf Q(\sqrt2,\sqrt3)\). This proves the indicated degrees before substitution. After substitution the root fields of \(E,J,G,A,B,K\) are \(\mathbf Q(u)(\sqrt[4]{u})\), with degree four over \(\mathbf Q(u)\), using a root \(u\) of the associated lower-degree form. For \(J,G,A,B,K\) the conjugates have both signs. Indeed \(J,G,A,K\) have negative product of conjugates, and \(B(t,1)\) changes sign in both the positive and the negative real half-lines. Hence \(u\) is neither a square nor minus four times a fourth power in its totally real field. For \(E\) take \(u=2+\sqrt3>0\): if \((a+b\sqrt3)^2=u\) with \(a,b\in\mathbf Q\), then \(a^2=(2\pm1)/2\), impossible. The quartic binomial irreducibility criterion applies in each case. The factors \(s-2t,2s-t\) have root fields obtained from a fourth root of \(2\) or \(1/2\), the factor \(s+t\) is \(\Phi_8(x,y)\), and \(W=\Phi_{24}(x,y)\).

## Removing the extra real loss by choosing the odd input entry

For a primitive \(a+b=c\), fix its unique even entry \(y\) and let \(x\) be either odd entry. The original three entries up to signs are \(x,y,x\pm y\). Denote these three corresponding factors of \(F\) by \(I_x\), and the degree-95 product of the remaining factors by \(K_x\). Either odd choice supplies an admissible transfer. At least one has
\[
 |K_x|\asymp h^{95}.
\]
For that choice the exact comparison, with an absolute bounded error, is
\[
 \log(C/R)=\log\frac{c}{\operatorname{rad}(abc)}
       +\sum_{f\notin I_x}\log\frac{|f(x,y)|}{\operatorname{rad}(f(x,y))}+O(1).
\]
Indeed each complementary factor then has absolute value comparable to \(h^{\deg f}\), \(C\asymp h^{96}\), \(c\asymp h\), and the three input entries are pairwise coprime.

To verify the choice, let \(\Psi(T)\) be the degree-94 product of all eleven nonlinear factors, at \((T,1)\). It is even. Exact polynomial division gives
\[
   \gcd_{\mathbf F_{19}[T]}(\Psi(T),\Psi(T+1))=1,\qquad
       (\Psi(0),\Psi(1),\Psi(2))\equiv(8,3,10)\pmod {19}.
\]
These computations can be reproduced by multiplying the last four rows of the factor table, reducing coefficients modulo 19 and applying the Euclidean algorithm. If \(y\) is the largest entry of the additive triple, the two odd parameters have ratios \(T\) and \(1-T\); their complementary products are \((T+1)\Psi(T)\) and \((2-T)\Psi(1-T)\). When \(y\) is a summand, take the two ratios to be \(T\) and \(T+1\); the products are \((T-1)\Psi(T)\) and \((T+2)\Psi(T+1)\). In either case the two homogeneous products have no common projective zero even modulo 19, including at infinity by their nonzero leading coefficients. On the real projective line compactness gives the claim. The same resultant argument shows that the gcd of the two complementary products is bounded by a fixed constant at every primitive input.

There are three possible unordered coordinate pairs from the three input entries. The pair consisting of both odd entries is also admissible. In that case \(s,t\equiv1\bmod16\), \(\alpha\) can be half-integral in the basis \(1,\sqrt{-3}\), and \(\alpha^{12}\equiv1\bmod 2\mathcal O\) since \((\mathcal O/2\mathcal O)^\times\) has order 3. Thus \(P,Q\) are integers. From \(16\mid s-t\), \(2\mid s+t\), and the factor formula, \(48\mid Q\). The other transfer properties persist, including \(W=\Phi_{24}(x,y)\). Now the six even factors are \(x-y,x+y,x^2+y^2,s+t,E,B\), so the product of all factor radicals is \(32R\).

The set of nonlinear factors is invariant under exchange of the two variables (reciprocity exchanges \(A,K\), and \(J,G\), for example) and under sign changes. Thus the mod-19 shift verification applies to any two of the three complementary products by keeping their shared input entry as denominator. Every two products have bounded gcd, and at least two of the three orientations simultaneously have all their complementary factors of full archimedean size. At any prime outside a fixed finite set, a complementary factor occurs in at most one of the three orientations.

## Which prime squares can account for an exceptional gain?

Average over coprime pairs in \(H/2<h\le H\) with the admissible parity and congruence conditions; their number is \(\asymp H^2\). For every fixed \(A_0>0\),
\[
 \frac1{H^2}\sum_{x,y}
   \sum_{p\le A_0 H^2}(v_p(F(x,y))-1)_+\log p=O_{A_0}(1).       \tag{1}
\]
For any \(p>3\) and \(j\ge2\), a root line modulo \(p^j\) lifts uniquely from a simple root modulo \(p\), so there are at most 98 such lines. Its lattice has determinant \(p^j\). Distinct primitive slopes in this lattice have angular separation \(\gg p^j/H^2\) by their cross determinant. Its number of primitive points in the box is consequently \(O(1+H^2/p^j)\), identifying opposite signs if necessary. Summing the main term uses \(\sum_{p,j\ge2}\log p/p^j<\infty\). The contribution of the \(+1\) is \(O_{A_0}(H^{-2}\pi(A_0H^2)\log H)=O_{A_0}(1)\) since \(\log|F(x,y)|=O(\log H)\). At 2,3 the explicit factor calculation above reduces high valuations to those of a single linear form. Alternatively, fixed separability in characteristic zero bounds the number of root tubes at every level by a constant for each exceptional prime.

The same spacing argument at the real place gives a bounded mean absolute value for \(\log(H^{98}/|F(x,y)|)\). Near a real projective zero, all other linear factors over the algebraic closure are bounded away from zero in normalized coordinates. The count of primitive slopes within distance \(\varepsilon\) of that root is \(O(1+H^2\varepsilon)\). Integrating up to \(O(\log H)\), using that nonzero integer \(F\) has absolute value at least one, proves the bound. For sufficiently large \(H\) none of the primitive admissible pairs is a rational zero of \(F\).

Choose an absolute \(A_0\) large enough that no square of \(p>A_0H^2\) divides a nonzero factor of degree at most four. Combining these estimates gives
\[
 \log(C/R)=-2\log H+
       \sum_{p>A_0H^2}(v_p(F(x,y))-1)_+\log p+\mathcal E_H(x,y),
 \qquad \frac1{H^2}\sum_{x,y}|\mathcal E_H(x,y)|=O(1).          \tag{2}
\]
Thus outside \(O_\delta(H^2/\log H)\) inputs, an output fixed-power gain requires a prime \(p>A_0H^2\) squared in one of precisely the seven degree-8 or degree-16 layers. Pointwise, \(\mathcal E_H\) is bounded below by an absolute negative constant, since the archimedean size of \(F\) is \(O(H^{98})\) and ordinary excess is nonnegative. Hence even a single squared prime \(p>H^{2+\delta}\) forces \(\log(C/R)\ge\delta\log H-O(1)\). Two distinct squared primes exceeding \(A_0H^2\), or one such prime to exponent at least three, force \(\log(C/R)\ge2\log H-O(1)\).

For the general primitive coefficient inputs \(s,t\) before substitution, replace \(F\) by \(F_0\), heights by \(H/2<\max(|s|,|t|)\le H\), and degrees \(98,96\) by \(26,24\). Every irreducible factor now has degree at most four. The moving-prime sum in (2) vanishes identically. In particular \(\log(C/R)+2\log H\) has bounded mean absolute value, the output quality tends to \(12/13\) in density, and \(O_\delta(H^2/\log H)\) inputs can produce a fixed positive exponent. These estimates concern density, and leave exceptional sparse sequences unresolved.

For individual inputs, the Subspace Theorem gives a complementary unconditional bound. For every fixed finite set \(S\) of primes and every \(\varepsilon>0\),
\[
 \log(C/R)\ \le\ \sum_{p\notin S}(v_p(F)-1)_+\log p
                  +\varepsilon\log h+O_{S,\varepsilon}(1).
\]
Indeed at each fixed place in \(S\cup\{\infty\}\), the local logarithmic deficiency of a squarefree binary form is, up to a bounded error, no greater than proximity to one fixed algebraic projective root. A finite choice of root systems and two-dimensional Schmidt approximation bound the sum of these proximities by \((2+\varepsilon)\log h+O(1)\) for primitive rational points; the exceptional projective lines contribute only finitely many primitive inputs. This absorbs the archimedean loss and every multiplicity at the fixed finite primes into the height margin. The same argument applies to \(F_0\).

## Squarefree coordinates for general primitive parameters

For the degree-26 support before the fourth-power substitution, \(U,W\) are simultaneously squarefree with relative natural density
\[
 \prod_{p>3}\left(1-\frac{12{\boldsymbol 1}_{p\equiv\pm1\ ({\rm mod}\ 24)}
                 +2{\boldsymbol 1}_{p\equiv1\ ({\rm mod}\ 3)}}{p(p+1)}\right)>0
\]
among primitive pairs with \(s\) odd, \(t\) even, \(3\nmid W\). The relative density with no repeated prime \(p>3\) anywhere in \(U,V,W\) equals
\[
 \prod_{p>3}\left(1-\frac{\gcd(24,p-\chi_p)+1+\chi_p}{p(p+1)}\right)>0,
 \qquad \chi_p=(-3/p).
\]
Indeed away from 2 and 3 the projective map \(z\) gives \(\gcd(24,p-\chi_p)\) roots of unity lines and \(1+\chi_p\) extra norm-zero lines. The twelve solutions of \(z^{12}=-1\) occur exactly at \(p\equiv\pm1\bmod24\), with none in the remaining classes. Each simple root line modulo \(p^2\) has conditional frequency \(1/(p(p+1))\) among primitive pairs. The finite prime events are independent in the limit by the Chinese remainder theorem and the ordinary coprimality sieve. The omission of primes beyond \(Y\) costs upper density \(O(\sum_{p>Y}p^{-2}+\limsup_{H\to\infty}\pi(A_0H^2)/H^2)=O(1/Y)\) by the same slopes argument, since all factors have degree at most four. The finite-product limit gives both formulas. No congruence restriction on all primes of \(W\) is used in this paragraph beyond their necessary splitting.

Truncating the first product at \(10^6\) gives the certified interval \([0.9074003,0.9074131]\); for the second it gives \([0.4823199,0.4823325]\). Directed decimal products to 45 places suffice. Relative to the partial product, the omitted product is between 1 and \(1-B/(10^6+1)\), with \(B=14,26\) respectively, using the union bound and \(\sum_{n>Y}1/(n(n+1))=1/(Y+1)\).

## Constraints on sparse exceptional sequences

Fix any finite prime set \(S\) and write \([n]_{S^c}\) for the part of \(|n|\) prime to \(S\). For a subproduct \(F'\) of the fifteen layers, of degree \(d'\), the same Subspace Theorem argument on \(F'\) gives \([F'(x,y)]_{S^c}\gg_{F',S,\varepsilon} h^{d'-2-\varepsilon}\). In particular every one of the ten factors of degree at least four has a largest prime factor tending to infinity with the input. For every fixed bound \(B_0\), at most two factors can simultaneously have all prime divisors at most \(B_0\) once \(h\) is sufficiently large, by using the estimate on any three-factor product. The qualitative conclusion also follows from the Thue–Mahler theorem for forms with at least three distinct geometric roots. Since the large primes in distinct layers are disjoint, \(U\) has at least three distinct primes above \(B_0\), \(V\) has at least nine, and \(W\) has at least one. These further restrictions hold eventually in the equivalence transfer.

For any subproduct of even degree \(d'\ge6\), its squarefree kernel tends to infinity along every unbounded primitive sequence. Otherwise a fixed twist of the smooth hyperelliptic model \(Z^2=F'(T,1)\) would have infinitely many rational points: divide the homogeneous equation by \(y^{d'}\), a rational square. This curve has genus \((d'-2)/2\) (including the case where an \(F'\)-root lies at infinity). Faltings's theorem excludes that possibility. It follows that each of the seven high layers individually has largest square divisor \(o(h^{\deg f})\). Two distinct quartic layers cannot both have bounded squarefree kernel on any infinite sequence.
