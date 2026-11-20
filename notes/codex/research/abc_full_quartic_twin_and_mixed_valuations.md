# A same-radical twin and the mixed-valuation criterion

At each positive odd index \(n\) of \(G=(-3,9)\) on \(Y^2=X^3-36X\), choose \(a,w,c,d>0\) with \(w=B_n\), \(c^2=2w^2-a^2\), \(3d^2=2w^2+a^2\). These four integers are odd and pairwise coprime, and only \(d\) can be divisible by 3. Put \(P=awcd\). There are two primitive abc triples with exactly the same radical:
\[
 a^4+3(cd)^2=C=4w^4,\qquad
 c^4+8(aw)^2=C'=9d^4,\qquad R=\operatorname{rad}(6P).
\]
The second follows from \((3d^2-c^2)(3d^2+c^2)=(2a^2)(4w^2)\). Its first and second terms are coprime because \(c\) is odd and coprime to \(aw\). Its third term supplies 3, which does not divide \(caw\). The first triple supplies 2 from \(4w^4\) and 3 from its middle term. Thus both radicals include each of 2 and 3 exactly once, including when \(3\mid d\). [Orbit and coprimality](abc_full_quartic_signature.md)

Set \(t=a^2/w^2\), so \(0<t<2\). Then \(C'/C=(1+t/2)^2\) and
\[
 \left(\frac{C'}{6P}\right)^2=\frac{(2+t)^3}{12t(2-t)}
         \ \ge\ \sqrt3 .
\]
The derivative has the sign of \(8t-t^2-4\), giving the minimum at \(t=4-2\sqrt3\). In particular every twin has \(C'/R\ge3^{1/4}\). This constant is sharp for the real-variable inequality with denominator \(6P\), since odd multiples of \(G\) are dense on the bounded real component.

## How much cofactor loss gives a fixed quality gain?

For each integer \(F>0\) write \(s(F)=\prod_{v_p(F)\text{ odd}}p\). Put \(S=s(P)=s(a)s(w)s(c)s(d)\) and \(\eta=1-\log S/\log P\) for \(P>1\). Prime by prime,
\[
 S\le\operatorname{rad}(P)\le\sqrt{PS},\qquad
 R=\frac{6\operatorname{rad}(P)}{\gcd(3,P)} .
\]
For integer exponents \(e\ge1\), the upper bound says \(1\le (e+(e\bmod2))/2\). The four denominators satisfy \(\log F=Hn^2+o(n^2)\) individually, with the same \(H=\widehat h(G)>0\), and \(\log C=4Hn^2+O(1)\). Therefore with \(Q=\log C/\log R\), and equally with \(C'\) in place of \(C\),
\[
       1-\eta+o(1)\ \le\ \frac1Q\ \le\ 1-\frac{\eta}{2}+o(1).
\]
In particular abc restricted to this orbit is equivalent to \(\log s(F)/\log F\to1\) for **each** of \(a,w,c,d\). If \(Q\ge1+\epsilon\) infinitely often, one fixed arm on a subsequence has \(s(F)\le F^{1/(1+\epsilon)+o(1)}\), since \(\eta\) is the weighted average of the four individual logarithmic losses. Conversely, \(s(F)\le F^{1-\delta}\) on an infinite subsequence of one arm gives \(\liminf Q\ge(1-\delta/8)^{-1}\) there. For example \(s(w)\le\sqrt w\) infinitely often would give quality at least \(16/15\) in the limit. The latter example also follows directly from \(a,c<\sqrt2\,w,\ d<2w/\sqrt3\). These are implications for the stated orbit. [Four denominator heights](abc_full_quartic_signature.md)

## An infinite family with both even and odd positive valuations

Let \(m_0=3\) and \(m_{j+1}=m_j s(B_{m_j})\). All these odd indices are squarefree. Their multipliers are nontrivial and pairwise coprime, and
\[
 \gcd\big(B_{m_j},s(B_{m_{j+1}})\big)=1,\qquad
 (m_j/3)^2\ \mid\ B_{m_j}/s(B_{m_j}) .
\]
Indeed \(s(B_m)>1\) at every odd \(m>1\) by the square classification. All its primes are greater than 3. At each \(p\mid B_m\), multiplication of the index by \(s(B_m)\) raises an odd valuation by one and leaves an even valuation fixed. Hence all those valuations become even. They then remain even at every later step, since their primes never reappear in an odd-valuation multiplier. Every new multiplier therefore consists of entirely new primes, and each acquires exponent at least two in the next denominator. This proves both assertions. The first nontrivial index is \(3\cdot37=111\). All noninitial terms have even positive valuations at old primes and at least one odd positive valuation at a new prime. [Square classification](abc_full_quartic_square_classification.md) · [Formal valuation formula](abc_full_quartic_signature.md)

The same construction works in the full support: take \(m_0=5\) and \(m_{j+1}=m_j s(P_{m_j})\). Here \(P_m=B_{2m}/2\), and its odd support obeys the same lifting rule, including \(v_3(P_m)=v_3(m)\). The prime 5 divides no \(P_m\) at odd \(m\), because \(G\) has order four modulo 5. Also \(s(P_m)>1\) because \(B_m\) is nonsquare and the arms are coprime. Thus the indices are again squarefree, with
\[
 (m_j/5)^2\mid P_{m_j}/s(P_{m_j}),\qquad
 m_j/5\mid P_{m_j}/\operatorname{rad}(P_{m_j}),\qquad
 C'_{m_j}/R_{m_j}\ge 3^{1/4}m_j/5 .
\]
The forced square divisor grows quadratically in the index. A fixed logarithmic quality gain instead requires square-divisor mass of order \(\exp(c n^2)\) on this orbit. [Bad-prime valuations](abc_full_quartic_first_depth_census.md)
