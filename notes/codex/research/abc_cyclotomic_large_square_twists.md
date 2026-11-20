# Large prime squares in binary cyclotomic values

Fix \(n\) with \(D=\varphi(n)\ge6\), and let \(F(A,B)=\Phi_n(A,B)\) be the homogeneous cyclotomic polynomial. For all coprime positive integers \(A>B\), the value \(F(A,B)\) is positive. For each squarefree \(b\ge1\), the number of such pairs, over all heights, with \(F(A,B)=bz^2\) is at most
\[
                            K_n^{1+\omega(b)}                             \tag{1}
\]
for a constant \(K_n\) depending only on \(n\). At the sextic indices \(n=7,9,14,18\), it follows that for every fixed \(0<\delta<1\) the number of pairs with \(A\le H\) for which some prime \(p\ge A^{2+\delta}\) satisfies \(p^2\mid F(A,B)\) is
\[
                         O_{n,\delta}\big(H^{2-2\delta}
                                           (\log(2H))^{c_n}\big).        \tag{2}
\]
Both estimates are unconditional. Examples below show that individual sextic values can have a squared prime greater than \(A^2\).

## Point counts on the quadratic twists

Write \(f(x)=\Phi_n(x)\). It has \(D\) distinct roots and even degree. The smooth projective curve \(C_b\) with affine equation \(y^2=b f(x)\) has genus \(g=(D-2)/2\ge2\). A pair counted in (1) yields the rational point
\[
                     (x,y)=(A/B,\ bz/B^{D/2})
\]
by choosing \(z>0\). Its reduced abscissa recovers the pair. The Jacobian \(J_b\) is the quadratic twist of \(J_1\) by \([-1]\), since the hyperelliptic involution acts as \([-1]\) on the Jacobian.

Take the fixed number field \(L=\mathbf Q(J_1[2])\). The twist acts trivially on the two-torsion, so \(J_b[2]\) is constant over \(L\) for every \(b\). Let \(S\) be the finite places of \(L\) above \(2b\) and above the primes of bad reduction of \(J_1\). At every place outside \(S\) the quadratic twist is unramified and has good reduction. The Kummer map sends \(J_b(L)/2J_b(L)\) injectively into \((L^\times/L^{\times2})^{2g}\). The image is unramified outside \(S\), because multiplication by 2 on the abelian scheme at a good odd place is finite étale. Each of these squareclasses therefore has even valuation outside \(S\). Their space in a single copy of \(L^\times/L^{\times2}\) has dimension at most \(|S|+O_L(1)\), by the unit theorem and the two-torsion of the ideal class group. Since \(|S|=O_n(1+\omega(b))\), this bounds \(\operatorname{rank}J_b(\mathbf Q)\) by \(O_n(1+\omega(b))\).

The uniform rational-point bound of Dimitrov, Gao and Habegger gives \(\#C_b(\mathbf Q)\le c(g,1)^{1+\operatorname{rank}J_b(\mathbf Q)}\), proving (1). This use of their theorem supplies a cardinality bound. The estimate does not compute all the rational points or their heights. [Dimitrov, Gao and Habegger, *Uniformity in Mordell–Lang for curves*, Ann. of Math. 194 (2021), 237–298](https://arxiv.org/abs/2001.10276)

If \(A\le H\) and \(p^2\mid F(A,B)\) for some \(p\ge Z\), its squarefree kernel \(b\) is at most \(Y=(2H)^D/Z^2\), by factoring \(F\) over the complex numbers. There are no pairs if \(Y<1\). For \(Y\ge1\), sum (1) over squarefree \(b\le Y\). With an integer \(m\ge K_n\), the weight \(m^{\omega(b)}\) on squarefree integers equals the number of ordered factorizations into \(m\) positive integers. The sum of those counts over all integers through \(Y\) is at most \(Y(1+\log Y)^{m-1}\), by summing over the first \(m-1\) factors. This proves a bound \(O_n(Y(1+\log Y)^{c_n})\). For \(D=6\) in a shell \(H/2<A\le H\), use \(Z=(H/2)^{2+\delta}\). Summing the resulting geometric series gives (2).

## Two exact sextic examples

The following identities have primes of exact exponent two, with orders \(14\) and \(18\) for \(AB^{-1}\) in the respective residue fields.
\[
 \begin{aligned}
  \Phi_{14}(223,181)&=83\,634\,890\,075\,227=547\cdot391021^2,
          &391021/223^2&=7.8630\ldots,\\
  \Phi_{18}(184,101)&=33\,449\,976\,035\,913=3\cdot739\cdot122833^2,
          &122833/184^2&=3.6281\ldots.
 \end{aligned}
\]
The factors follow from \(\Phi_{14}(A,B)=(A^7+B^7)/(A+B)\) and \(\Phi_{18}(A,B)=A^6-A^3B^3+B^6\). The primes in question divide neither index, so divisibility of the cyclotomic value forces the displayed exact order. The complete factorization for the first power triple is
\[
 223^{14}-181^{14}
   =2^3\cdot3\cdot7^2\cdot29\cdot101\cdot547\cdot391021^2
       \cdot2470081367111 .
\]
All displayed prime factors, including the bases \(181,223\), can be checked by trial division through their square roots. The largest such bound is \(1\,571\,649\). The primitive triple with largest term \(223^{14}\) has radical \(2623316965929399432747280839438\), giving quality \(1.0807860012\ldots\) and gain \(223^{14}/R=286.69314885\ldots\).

These are the only two instances with $p>A^2$ in all 304,460 rows for $1\le B<A\le500$, $(A,B)=1$, $n\in\{7,9,14,18\}$. There are 76,115 pairs at each index. Independent complete factorizations through $A=250$ reproduced both hits. The verifier uses $\Phi_n(A,B)<K A^6$ with $K=7,3,1,1$, respectively. After stripping the eligible primes through $KA^2$, any remaining squared prime must constitute the entire residual integer, since its complementary factor is smaller than $KA^2$. [Exact census](abc_cyclotomic_large_square_scan.py)

For any fixed \(n\), infinitely many pairs with a squared prime \(p\ge A^{2+\delta}\) in \(A^n-B^n\) would disprove rational abc at a fixed positive exponent: the triple radical is at most \(AB(A^n-B^n)/p\le A^{n-\delta}\), while its largest term is \(A^n\). Bound (2) leaves that infinitude open.

## A twelfth-power family excluding every such square

For every coprime \(A>B\ge1\), set \(H=A\). There is **no** prime \(p>H^2\) with \(p^2\mid A^{12}-B^{12}\). Indeed \(p\ge5\) and \(p\nmid12\). If it divides the difference it divides exactly the cyclotomic factor of order \(\operatorname{ord}_p(AB^{-1})\), by separability of \(T^{12}-1\bmod p\). Among the factors at orders \(1,2,3,4,6,12\), the only quartic is
\[
                     \Phi_{12}(A,B)=A^4-A^2B^2+B^4<H^4 .
\]
The remaining linear and quadratic factors are at most \(3H^2<H^4\), since \(H\ge2\). All are therefore smaller than \(p^2\).

Rational abc is equivalent to its restriction to the primitive triples \(B^{12}+(A^{12}-B^{12})=A^{12}\). To prove the reverse implication, start with the arbitrary primitive triple \(B+(A-B)=A\), and write \(R_0=\operatorname{rad}(AB(A-B))\). The new radical satisfies
\[
 R_{12}=\operatorname{rad}\big(AB(A^{12}-B^{12})\big)
 \le R_0\frac{A^{12}-B^{12}}{A-B}\le 12R_0 A^{11}.
\]
A restricted bound \(A^{12}\ll_\eta R_{12}^{1+\eta}\) gives \(A^{1-11\eta}\ll_\eta R_0^{1+\eta}\). For the desired exponent \(1+\varepsilon\) choose \(\eta=\varepsilon/(12+11\varepsilon)\). The forward implication applies abc directly to each primitive power triple. Thus every failure of rational abc would also produce an infinite sequence of failures in a family where all repeated primes are at most the square of the base height.

## Making every prime in all three terms small

Fix any exponent \(n\ge2\) and any real \(\eta>0\). Rational abc is equivalent to its restriction to a subfamily of \(B^n+(A^n-B^n)=A^n\) in which **every prime factor of all three terms is less than \(H^\eta\)**, with \(H=A\).

Choose a squarefree \(k\) coprime to \(n\) so that \(2\varphi(n)\varphi(k)<\eta k\). Products of the primes outside the finite support of \(n\) work, since \(\prod_{p\mid k}(1-1/p)\) can be made arbitrarily small. Keep this \(k\) fixed after choosing \(n,\eta\). For any coprime \(s>t\ge1\), put \(A=s^k\), \(B=t^k\), \(m=nk\). The primes of \(A^n=s^m\) and \(B^n=t^m\) are at most \(s=H^{1/k}<H^\eta\). Every prime of the remaining term \(s^m-t^m\) divides some \(\Phi_d(s,t)\) with \(d\mid m\). Since \(\varphi(d)\le\varphi(m)\), \(s\ge2\) and \(\varphi(m)=\varphi(n)\varphi(k)\), each such factor satisfies
\[
          |\Phi_d(s,t)|\le (2s)^{\varphi(d)}
                 \le s^{2\varphi(m)} < s^{\eta k}=H^\eta .
\]
For the arbitrary primitive source \(t+(s-t)=s\), the height of the image is \(s^m\) and its radical is at most \(m s^{m-1}\operatorname{rad}(st(s-t))\). The preceding endpoint calculation, with \(12\) replaced by the fixed \(m\), recovers ordinary abc. Here \(H=s^k\) is the base height in the stated exponent-\(n\) family; the underlying coprime pair has height \(s\).
