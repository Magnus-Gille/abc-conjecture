# Which prime powers could change the abc exponent on the orbit of (7,4)?

Let \(x=s/t\) be the signed reduced slope at a prime index \(\ell\) on the orbit of \((7,4)\), with \(t>0\) and \(H=\max(|s|,t)\). Write
\[
Y=s^2+2t^2=81A_\ell^2,\qquad V=(s-t)^2+t^2=B_\ell^2,
\]
where \(A_\ell,B_\ell>0\). Assume \(\ell>3\) is inert in \(\mathbb Q(\sqrt{-2})\). The height satisfies \(\log H\asymp\ell^2\), and \(3\nmid A_\ell\). Every prime of \(A_\ell\) has the form
\[
p=(1+a\ell)^2+2b^2\ell^2,\qquad a,b\in\mathbb Z,\quad b\ne0.
\]
The companion note proves the norm formula using the elliptic curve and its complex multiplication. It states the construction for the inert class \(5\bmod8\). The same norm proof applies to \(7\bmod8\), since parity holds at every odd index and the only property of \(\ell\) used in that proof is inertness. [Orbit and small-prime bound](abc_octic_mixed_seed_prime_orbit.md) · [Parity at every odd index](abc_octic_mixed_prime_indices.md)

## A bound for the contribution of smaller prime powers

Put \(e_p=v_p(A_\ell)\), and let \(X\ge2\). Then
\[
\sum_{p\mid A_\ell,\;p e_p\le X}e_p\log p
\ll \frac{X}{\ell^2}\log(2X)\log(2+X/\ell^2).
\]
Indeed, select one pair \((a,b)\) in the formula for each eligible prime. Distinct primes have distinct selected pairs. By the triangle inequality and \(b\ne0\),
\(
\sqrt p\ge\ell\sqrt{a^2+2b^2}-1\ge\ell\sqrt{a^2+2b^2}/2.
\)
Thus \(p\le X\) implies \(a^2+2b^2\le 4X/\ell^2\). In the sum, replace \(e_p\) by \(X/p\) and \(\log p\) by \(\log(2X)\). In a disk of radius \(r\ge1\) there are \(O(r^2)\) integer pairs. Summing \((a^2+2b^2)^{-1}\) in dyadic annuli therefore gives the asserted logarithm. All constants in the bound can be absolute.

Since \(Y\asymp H^2\), we have \(\log A_\ell=\log H+O(1)\). For any fixed \(\eta>0\), choose
\[
X=\frac{\ell^4}{(\log\ell)^{2+\eta}}.
\]
The displayed sum is \(O_\eta(\ell^2/(\log\ell)^\eta)=o(\log A_\ell)\). Thus the primes with \(p e_p>X\) account for a proportion tending to one of \(\log A_\ell\). The product \(p e_p\) here means the prime multiplied by its exponent.

## How a repeated factor would affect abc

The triple has entries \((2st)^4,(s^4-4t^4)^2,(s^4+4t^4)^2\). The first two sum to the third. The entries are coprime because \(s,t\) are coprime with \(s\) odd, \(t\) even. Put \(c=(s^4+4t^4)^2\asymp H^8\) and let \(R\) be the product of the distinct primes of the three entries. Factoring the entries gives
\[
R=\operatorname{rad}\left(2|st(s^2-2t^2)Y V ((s+t)^2+t^2)|\right).
\]
Here \(\operatorname{rad}(V)\le B_\ell\ll H\) and \(\operatorname{rad}(Y)=3\operatorname{rad}(A_\ell)\). The four remaining factors \(s,t,s^2-2t^2,(s+t)^2+t^2\) have product \(O(H^6)\) in absolute value. Consequently
\[
R\ll H^8\,\frac{\operatorname{rad}(A_\ell)}{A_\ell}.
\]
If \(\sum_{p\mid A_\ell}(e_p-1)\log p\ge\delta\log H\) infinitely often for a fixed \(\delta>0\), these triples disprove abc. The smaller prime powers in the previous section contribute \(o(\log H)\) even when their entire valuations are counted. Any fixed positive fraction of excess in this factor must therefore come from the complementary range. Repetitions in other factors of the triple would offer additional ways to lower the radical.

In particular, if every prime dividing \(A_\ell\) occurs to exponent at least two, then every prime of \(Y\) occurs to exponent at least four. This gives \(R\ll H^{15/2}\). Infinitely many such indices would violate abc for every fixed \(0<\varepsilon<1/15\).

## Why a single fourth power cannot supply an infinite family

Only finitely many of these slopes have \(Y\) a fourth power. In each of the two norm-Euclidean rings \(\mathbb Z[\sqrt{-2}]\) and \(\mathbb Z[i]\), the element giving the corresponding norm is coprime to its conjugate. This follows from oddness of the norms and coprimality of the two integer coordinates. If \(Y\) is a fourth power and \(V\) a square, then \(s+t\sqrt{-2}\) is a unit times a fourth power, and \((s-t)+it\) is a unit times a square. There are finitely many choices of units. On projective slopes, taking the indicated powers gives maps to \(x=s/t\) of degrees four and two. Each is a power map in the ratio of the two conjugate embeddings. Their branch values are respectively the two roots of \(x^2+2\) and the two roots of \((x-1)^2+1\). These branch sets are disjoint. Over the algebraic closure the two cyclic covers have no common nontrivial subcover, because the projective line has no connected unramified cover of degree greater than one. Their fiber product is smooth, connected, and of bidegree \((4,2)\), hence has genus three. Faltings' theorem gives finiteness on each of the finitely many curves. The slopes on the orbit are distinct for distinct positive odd indices, by the infinite order of the seed difference and the degree-two quotient involution. [Related fixed-power argument](abc_octic_power_patterns.md)

Since \(v_3(Y)=4\) and all exponents in \(Y\) are even, at every sufficiently large inert prime index some new prime has exponent congruent to two modulo four in \(Y\). For \(Y\) to be cubeful that exponent would have to be at least six. Whether such indices yield a positive fraction of repeated prime factors in \(A_\ell\) remains open.

The genus-three fourth-power curve has Jacobian rank at least three over the rationals. [Quotients and rank certificate](abc_octic_mixed_fourth_power_quotients.md)

The calculation at 11 now gives all rational slopes. The only nondegenerate signed slope in this fourth-power case is \(7/4\). [Complete rational-point classification](abc_octic_mixed_elliptic_chabauty_11.md)
