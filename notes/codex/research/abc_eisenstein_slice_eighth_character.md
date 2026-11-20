# An eighth-power restriction on the paired quartic kernels

On the nontrivial elliptic slice use the [signed descent](./abc_eisenstein_slice_squareclass_descent.md) \(F_0=-8s^2,\ F_4=16kt^2,\ F_5=32l u^2\), with \(s,t,u>0\) odd. Then
\[
 s^2+kt^2+2lu^2=0,\qquad
 s^4+ks^2t^2+k^2t^4=3W^4.
\]
The three terms in the first relation are pairwise coprime at odd primes, including 3, and \(k,l\) are prime to 6. The odd primes in \(s,|kl|\) are all \(1\) or \(-1\bmod24\), since they divide the real twelfth-power coordinate. At \(p\equiv1\bmod24\) in \(|kl|\), 3 is a fourth power modulo \(p\).

Suppose every prime \(p\mid b=|kl|\) is \(1\bmod24\). There is a necessary condition determined by \(b\) alone:
\[
    \prod_{p\mid b}\chi(p)=1,\qquad
    \chi(p)\in\{1,-1\},\quad
    \chi(p)\equiv(-3)^{(p-1)/8}\pmod p.
\]
In particular the two signs must agree when \(b=pq\).

In \(\mathcal O=\mathbf Z[\omega]\), \(\omega=(-1+\sqrt{-3})/2\), the norm of \(s^2-\omega kt^2\) is \(3W^4\). Its ideal is coprime to its conjugate outside 3 by \((s,kt)=1\). At 3 it has valuation one at the ramified prime since \(3\nmid W\). As \(\mathcal O\) is principal,
\[
                 s^2-\omega kt^2=\varepsilon(1-\omega)\gamma^4
\]
for a sixth root of unity \(\varepsilon\) and an Eisenstein integer \(\gamma\).
At a prime over \(p\mid k\) the left side reduces to \(s^2\), and at a prime over \(p\mid l\) it reduces to \((1+\omega)s^2\). For \(p\equiv1\bmod24\), sixth roots of unity in the residue field are fourth powers. Raising modulo \(p\) to the \((p-1)/4\) power therefore gives
\[
        (s/p)=(1-\omega)^{(p-1)/4}
              =(-3\omega)^{(p-1)/8}=(-3)^{(p-1)/8}\pmod p.
\]
The expression is independent of the prime over \(p\). At each \(r\mid s\), including any large prime of either allowed sign, the first displayed relation gives \((kl/r)=(-2/r)=(-1/r)\). Multiply over \(r\), counted with \(v_r(s)\), to obtain \((-kl/s)=1\). More generally write \(p^*=(-1/p)p\). The signs fixed by reduction modulo 3 give \(k=\prod_{p\mid k}p^*\) and \(l=-\prod_{p\mid l}p^*\). Thus reciprocity yields
\[
                 \prod_{p\mid b}(s/p)=1.
\]
For all-split support this proves the asserted eighth-character condition.

The two signs occur with equal natural frequency among split primes passing the fourth-power condition. In \(F=\mathbf Q(\zeta_{24})\) the element \(-3\) is a square and is not a fourth power. Otherwise the abelian extension would contain \(\sqrt[4]3\) because \(\zeta_8\in F\). Its class has order four in \(F^\times/F^{\times8}\), so the splitting field \(F(\sqrt[8]{-3})\) is cyclic of degree four over \(F\). Its intermediate quadratic field is \(F(\sqrt[4]3)\), and splitting in that field is the existing condition. Hence Chebotarev gives both signs in equal proportions. For a fixed such \(p\), the same proportions continue after imposing \((p/q)=1\) on its partner \(q\), because \(\mathbf Q(\sqrt p)\) ramifies at \(p\) whereas the eighth-power field ramifies only at 2 and 3.

For illustration, the condition discards \(433\cdot577\), \(577\cdot769\), and \(193\cdot4441\), even though these products pass the nontrivial signed, mutual-Legendre, and three Tunnell conditions previously checked up to \(10^6\). These examples are local obstructions; the [separate sharp minimum on the orbit](./abc_eisenstein_slice_squareclass_min.md) already excludes smaller products.
