# Three disjoint sets of prime divisors on the orbit through (7,4)

Let \(\ell>3\) be prime. In the full parametrization write \(Y_N=s_N^2+2t_N^2\) and \(V_N=(s_N-t_N)^2+t_N^2\), and put \(b=\sqrt{Y_\ell},\ v=\sqrt{V_\ell}\). The prior orbit through \((7,4)\) at multiplier \(\ell\) is the full index \(3\ell\). There is a factorization
\[
 \frac{\sqrt{Y_{3\ell}}}{9}=b\,C_1 C_2,\qquad
 C_1=\frac{b^4-4b^2v^2+6v^4}{3},\quad
 C_2=\frac{b^4+4b^2v^2-2v^4}{3}.
\]
All three factors are positive, pairwise coprime integers prime to 6. For every prime \(\ell\equiv5\pmod8\), **each factor has at least one prime divisor of odd exponent**. Thus \(Y_{3\ell}\) has at least three distinct new primes with valuation congruent to two modulo four. Each of these primes is at least \(2\ell^2+1\). If this value of \(Y_{3\ell}\) is cubeful, each of the three exponents is at least six. At all sufficiently large primes \(\ell\), the same multiplicity conclusion holds without the residue-class condition, with an ineffective threshold and without the quadratic lower bound for split \(\ell\).

## Division by three on the elliptic curve

On \(E':y^2=x^3+16x^2+32x\), put \(R_0=(-8,16)\), and let \(B_j\) be the positive square root of the reduced denominator of \(x([j]R_0)\). At every positive odd full index \(N\),
\[
 x([N]R_0)=-8V_N/Y_N,\qquad B_N=\sqrt{Y_N}.
\]
Indeed the branch \(W=(-2\sqrt{-2},8)\) on the mixed elliptic model satisfies \(2W=A=(1,1)\). Under the 2-isogeny to \(E'\), \(W\) maps to \(R_0\). At \(Q=[(N+1)/2]A\), the translated point \(Q-W=NW\). The abscissa after this isogeny as a function of the slope of \(Q\) is \(-8V_N/Y_N\). The two norms are odd coprime squares. [Isogeny calculation](abc_octic_mixed_denominator_characters.md) · [Full index parametrization](abc_octic_full_mixed_orbit.md)

The third division polynomial is \(\psi_3(x)=3x^4+64x^3+192x^2-1024\). At an odd prime, the homogeneous multiplication map has good reduction and no cancellation; consequently \(v_p(B_{3\ell}/B_\ell)=v_p(b^8\psi_3(-8v^2/b^2))\). Substitution gives the product in the statement up to sign and a power of two. The two proposed quartics are odd, as are both denominators, which fixes the power of two. Both quartics are positive since \(2-\sqrt2\le b^2/v^2\le2+\sqrt2\), by \(V_\ell/Y_\ell=1-2st/(s^2+2t^2)\). They are each comparable to \(b^4\) with absolute comparison constants.

The ordinate of \(R_0\) is nonzero modulo 3. Its order there is 3, with \(v_3(B_3)=2\) from \(B_3=9\). Thus \(3\nmid b\), while \(v_3(B_{3\ell})=2\) by formal lifting. Also \(3\nmid v\) since \(3\nmid (s-t)^2+t^2\) for primitive inputs. Both quartic numerators are divisible by 3, so their 3-adic valuations are exactly one. Any common odd prime of the two numerators divides \(8v^2(b^2-v^2)\). Since \(b,v\) are coprime, such a prime must divide 3. Any odd prime dividing \(b\) and either numerator must divide 3 as well. This proves integrality and pairwise coprimality. The last two factors are supported on primes of exact reduction order \(3\ell\) of \(R_0\): their order divides \(3\ell\); orders one, three and \(\ell\) are eliminated by integrality of \(R_0\), \(B_3=9\), and coprimality with \(B_\ell\). The first factor is supported on primes of exact order \(\ell\).

## Proving odd exponents separately

The full fourth-power classification gives that \(b\) is never a square here. The only admissible slope for which \(Y_N\) is a fourth power and \(V_N\) a square is \(7/4\), which corresponds to \(N=3\). [Complete classification](abc_octic_mixed_elliptic_chabauty_11.md)

At \(N=5\) one has \(s/t=-119/180,\ b=281,\ v=349\). This gives
\[
 C_1=18{,}925{,}875{,}361,\qquad C_2=5{,}011{,}329{,}121.
\]
Both are quadratic nonresidues modulo 31. The point \(A\) has order four modulo 31, as follows from \(2A=(49/4,217/8)\). Its doubled ordinate vanishes there, whereas its own ordinate is one. For every \(N=\ell\equiv5\bmod8\), \([(N+1)/2]A\) has the same reduction as \([3]A\). Thus its primitive slope pair is a nonzero scalar multiple of \((-119,180)\) modulo 31. Both \(C_1,C_2\) are homogeneous **quartics** in the original pair \((s,t)\), divided by the unit 3. Their quadratic characters are unchanged by this scalar. Each therefore contains an odd exponent at some prime. Disjointness proves that the witnesses are different. The quadratic lower bound on the three primes follows from the inert-index CM norm formula for primes of \(Y_{3\ell}\) outside 3. [Frobenius norm bound](abc_octic_mixed_seed_prime_orbit.md)

For the eventual conclusion over all prime indices, put \(h=b/v\). The identity \((s^2-2t^2)^2=Y_\ell^2-8s^2t^2\) gives a rational square \(-h^4+4h^2-2=(D/V_\ell)^2\), with \(D=s^2-2t^2\). If \(C_1\) or \(C_2\) is a square, respectively \((h^4-4h^2+6)/3\) or \((h^4+4h^2-2)/3\) is another rational square. Each of these is a separable quartic whose roots are disjoint from those of \(-h^4+4h^2-2\): the first two numerators sum to four in the first case, and the two numerators differ by \(2h^4\) in the second. The normalized fiber product of the two double covers of the \(h\)-line has degree four, with eight simple disjoint branch values, hence genus five. Faltings gives only finitely many rational \(h\) in each case. Since \(x([\ell]R_0)=-8/h^2\) and \(R_0\) has infinite order, the positive prime indices give distinct \(h\). This proves the assertion.

## Fixed higher powers and varying prime multiplicities

For each fixed \(k\ge3\), only finitely many prime indices have either \(C_i\) a \(k\)-th power. Here is a direct covering argument. Factor the corresponding separable binary quartic in \(b,v\) into four monic linear forms over a fixed splitting field. Away from a fixed finite set of primes, containing those above 3 or the discriminant, at most one linear form can vanish on a primitive pair. If the quartic value is three times a \(k\)-th power, all four valuations are therefore divisible by \(k\) outside the fixed set. The possible classes of each value in \(K^\times/K^{\times k}\) with this property form a finite group, by the unit theorem for the fixed set and finiteness of the class group. On writing \(h=b/v\), extract \(k\)-th roots of the ratios of three linear factors to the fourth, after the finitely many constant twists just described. Over the algebraic closure the valuation at each of the first three roots makes the three classes independent. The resulting degree-\(k^3\) cover of the line has four branch values of ramification index \(k\). Its canonical degree is \(k^3(2-4/k)>0\), so Faltings gives finiteness. For the factor \(b\) itself, \(b=w^k\) forces \(s+t\sqrt{-2}\) to be a unit times a \(2k\)-th power by primitive coprimality, while the companion Gaussian norm is a square. The corresponding degree-\(2k\) and degree-two maps to the slope line have disjoint branch divisors, giving finitely many twists of a curve of bidegree \((2k,2)\) and genus \(2k-1\). This again gives finiteness. Together with the square case, these arguments handle every bounded set of exponents, with ineffective exceptional indices in general.

In logarithmic size the factors account for asymptotic fractions \(1/9,4/9,4/9\) of \(\log(\sqrt{Y_{3\ell}}/9)\), by their comparability to \(b,b^4,b^4\). Pairwise coprimality makes their logarithmic excesses \(\log(n/\operatorname{rad}(n))\) exactly additive. Therefore a positive fractional excess for their product infinitely often is equivalent to a positive fractional excess in at least one of the three factors infinitely often. The three forced odd exponents alone can still account for a vanishing fraction of the logarithm. [Radical calculation](abc_octic_mixed_radical_mass.md)
