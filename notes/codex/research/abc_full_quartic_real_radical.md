# A real-place certificate for the radical of the full quartic triple

Set \(C=4w^4\) and \(R=\operatorname{rad}(3B_{2n})\) for the primitive triple \(a^4+3b^2=4w^4\) at odd \(n\). Here \(P_n=nG\), \(G=(-3,9)\) on \(E:Y^2=X^3-36X\), and \(B_{2n}=2|abw|\). Writing \(D=3B_{2n}/R\) gives
\[
                 \frac CR=\frac {6D}{|Y(P_n)|}.
\]
This follows from \(Y(P_n)=9ab/w^3\). Since \(-6\le X(P_n)\le0\), the maximum of \(|Y|\) on this component is \(\sqrt{48\sqrt3}<10\). Thus any exhibited divisor \(L\mid D\) gives \(R\le C|Y(P_n)|/(6L)\), often without factoring a single coordinate. In particular \(L\ge2\) suffices for \(C>R\). [Parametrization](abc_full_quartic_signature.md) · [Valuations including 3 and 211](abc_full_quartic_first_depth_census.md)

| Odd index | Certified \(L\mid D\) | Bits in \(C\) | Lower bound for \(C/R\) |
|---:|---:|---:|---:|
| 9 | 9 | 207 | 145.497 |
| 27 | 27 | 1,869 | 145.869 |
| 53 | 211 | 7,202 | 138.930 |
| 159 | 633 | 64,822 | 1,209.819 |
| 891 | 891 | 2,035,537 | 6,001.264 |
| 1551 | 1551 | 6,168,039 | 75,401.973 |

For the entries above, \(3^{v_3(n)}\mid D\), the first-depth factor \(211\) occurs when \(53\mid n\), and \(11,47\mid B_6\), because \(|b_3|=1551=3\cdot11\cdot47\). At \(3\mid n\), formal lifting gives \(11^{v_{11}(n)}47^{v_{47}(n)}\mid D\) as well. These facts supply all displayed divisors. The integer verifier compares the square of the claimed ratio to \(4L^2w^6/[3a^2(4w^4-a^4)]\) by cross-multiplication. [Pointwise verifier](abc_full_quartic_real_radical.py)

## A density lower bound for full abc hits

Let \(K=K(1/2)\) denote the complete elliptic integral with parameter \(1/2\), and write \(F(z)=\int_0^z ((1-t^2)(1-t^2/2))^{-1/2}\,dt\). On the bounded real component the coordinate
\[
 X=-6+6\operatorname{sn}^2(u),\qquad
 Y=12\sqrt3\,\operatorname{sn}(u)\operatorname{cn}(u)\operatorname{dn}(u)
\]
uses that same parameter and period \(2K\). The origin of this coordinate is \((-6,0)\); the invariant differential is \(du/(2\sqrt3)\), so \(u(nG)=nF(1/\sqrt2)\bmod 2K\) at odd \(n\). Since \(G\) has infinite order, odd multiples equidistribute in this circle, including on every fixed arithmetic progression of odd indices.

Write \(v_1<v_2\) for the two positive roots of \(v-v^3=1/6\). The Haar measure \(\delta\) of \(|Y|<6\) is
\[
 \delta=\frac{F(\sqrt{1-v_2})+F(\sqrt{2v_1/(1+v_1)})}{K}
       =0.4892760168\ldots .
\]
Indeed \(v=-X/6=\operatorname{cn}^2(u)\) gives \(Y^2=216(v-v^3)\). The end intervals are \(v>v_2\) and \(v<v_1\). For the latter, use \(\operatorname{sn}(K-u)=\operatorname{cn}(u)/\operatorname{dn}(u)\). Every index in these intervals gives \(C>R\).

Independently, each odd multiple of 3, 53 or 65 has \(D>1\). For 65, the prime 13 divides \(B_5\) and gains valuation at a multiple of \(65\). The three moduli are pairwise coprime. Equidistribution on the complementary residue classes now gives
\[
 \liminf_{X\to\infty}
 \frac{\#\{n\le X:n\ {\rm odd},\,C_n>R_n\}}{\#\{n\le X:n\ {\rm odd}\}}
 \ \ge\ 1-\frac{2}{3}\frac{52}{53}\frac{64}{65}(1-\delta)
 =0.6710809064\ldots>\frac23.
\]
The strict rational comparison can be certified without numerical quadrature. Substitution in the cubic gives \(\sqrt{1-v_2}>31/100\) and \(\sqrt{2v_1/(1+v_1)}>54/100\). Three positive Taylor terms give \(F(z)\ge z+z^3/4+19z^5/160\). The arithmetic-geometric mean formula gives \(K<93/50\): use the second geometric mean as a lower bound for \(\operatorname{AGM}(1,1/\sqrt2)\) and \(\pi<22/7\). These elementary inequalities give \(\delta>19255601191/39680000000>247/512\), which suffices.

## A subsequence with a linear saving

Let \(\alpha=F(1/\sqrt2)/K\), which is irrational since \(G\) is nontorsion. The two zeros of \(Y(u)\) on its period are \(u=0,K\), with \(Y'=(3X^2-36)/(2\sqrt3)\), so \(|Y'|\le12\sqrt3\). Thus
\[
            \frac CR\ \ge\ \frac{D}{2\sqrt3\,K\|n\alpha\|}.
\]
Consecutive convergent denominators are coprime, so every irrational number has infinitely many odd convergent denominators \(k\), satisfying \(\|k\beta\|<1/k\). Apply this to \(\beta=53\alpha\) and set \(n=53k\). As \(D\ge211\), this yields infinitely many odd indices with
\[
                    \frac CR>\frac{211}{106\sqrt3\,K}\, n .
\]
The factor in front of \(n\) is about \(0.620\). This controls an unbounded ordinary ratio. The height \(\log C\) grows quadratically with \(n\), so this saving alone does not establish bounds above one by a fixed positive amount for the logarithmic abc quality.
