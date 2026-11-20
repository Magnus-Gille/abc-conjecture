# The part of the denominator supported at valuations outside a fixed multiple

Let \(B_n\) be the positive abscissa denominator square root for \([n]G\), \(G=(-3,9)\), on \(E_6:y^2=x^3-36x\). For \(k\ge2\) define
\[
 R_k(B)=\prod_{k\nmid v_p(B)}p,\qquad
 D_k(B)=\prod_p p^{v_p(B)\bmod k}.
\]
The exponents in the second product lie in \(\{0,\ldots,k-1\}\), so \(D_k\) is the unique \(k\)-th-power-free cofactor with \(B=D_k(B)z^k\). For every fixed \(k\), throughout the sufficiently large odd indices,
\[
            \log R_k(B_n)\gg_k\log\log n\,\log\log\log n.                  \tag{1}
\]
In particular both \(R_k(B_n)\) and \(D_k(B_n)\) exceed every fixed power of \(\log n\) eventually. In addition,
\[
       (\log R_k(B_n))^2\ge 2\log4\,\big(\log\operatorname{rad}(n)-O_k(1)\big).\tag{2}
\]
The constants and thresholds here are not evaluated. When \(\ell\) is a prime factor of \(k\), one has \(R_\ell(B)\mid R_k(B)\) and \(D_\ell(B)\mid D_k(B)\), by comparing valuations modulo \(\ell\) and \(k\). It suffices to prove everything for a fixed prime \(\ell\). One can use the same constants for all \(k\) divisible by that \(\ell\).

## A bounded number of indices for each cofactor

For each \(\ell\)-th-power-free \(d\) there are at most \(A_\ell^{1+\omega(d)}\) positive odd integers \(n\) with \(D_\ell(B_n)=d\), where \(A_\ell>1\) is independent of \(d\).

To see this write \(w=B_n=dz^\ell\); the [quartic parametrization](abc_full_quartic_signature.md) gives primitive odd \(a,b,w\) with \(a^4+3b^2=4w^4\). In the Eisenstein integers, with \(h=\sqrt{-3}\), the conjugates \(\alpha=(a^2+bh)/2\) and \(\bar\alpha\) generate coprime ideals because a common prime divides their sum \(a^2\) and their product \(w^4\). Since the Eisenstein integers are principal, \((\alpha)=(\gamma)^4\) with \(N\gamma=w\). No prime over a rational prime dividing \((\gamma)\) divides its conjugate. Thus each prime of \(w\) is split and precisely one of its two orientations occurs in \((\gamma)\). Factor the exponent at that place modulo \(\ell\). This gives \((\gamma)=(\lambda)(\kappa)^\ell\) with \(N\lambda=d\), \(N\kappa=z\). For each \(d\) there are at most \(2^{\omega(d)}\) possible ideals \((\lambda)\); fix one generator for each. The finitely many unit choices are absorbed in \(\eta\in\mu_6\) to give \(\alpha=\eta\lambda^4\kappa^{4\ell}\).

Writing \(\kappa=u+vh\), the index supplies a rational point \((u:v:a)\) on the weighted projective curve
\[
 C_{\eta,\lambda}:\qquad Y^2=
     \eta\lambda^4(U+hV)^{4\ell}+\bar\eta\bar\lambda^4(U-hV)^{4\ell},
       \qquad \mathrm{wt}(U,V,Y)=(1,1,2\ell).
\]
The right side is rational by conjugation, and over the quadratic field it is the sum of two nonzero pure powers in independent linear forms. It therefore has \(4\ell\) distinct geometric projective zeros. The smooth hyperelliptic curve has genus \(g=2\ell-1\). A point representing an index determines \(a^2/w^2=Y^2/[d^2(U^2+3V^2)^{2\ell}]\). Hence it determines the abscissa of \([n]G\), and thus at most one positive index since \(G\) is nontorsion. Overcounting points or unit choices is harmless.

Fix a number field \(F_0\) containing the Eisenstein field, \(\mu_\ell\), and all \(\ell\)-torsion of the Jacobians of the six base curves \(C_{\eta,1}\). Changing \(U+hV,U-hV\) by the respective scalars \(\lambda^{1/\ell},\bar\lambda^{1/\ell}\) identifies \(C_{\eta,\lambda}\) with \(C_{\eta,1}\) over \(F'=F_0(\lambda^{1/\ell},\bar\lambda^{1/\ell})\). The Galois group of \(F'/F_0\) is an \(\ell\)-group. Consequently \(J[\ell]\), for \(J=\operatorname{Jac}(C_{\eta,\lambda})\), has a filtration with trivial one-dimensional factors as a Galois module over \(F_0\). Indeed every simple representation of a finite \(\ell\)-group in characteristic \(\ell\) is trivial.

Take \(S\) to contain the infinite places and all places of \(F_0\) above \(6\ell d\). Away from \(S\) the linear coordinate change diagonalizing the binary form has unit determinant, its coefficients are units, and the residue characteristic is prime to \(4\ell\). The branch divisor is étale there and the hyperelliptic curve and its Jacobian have good reduction. The division fiber of a rational point under multiplication by \(\ell\) extends to a finite étale fiber over the local abelian scheme at each such place. Hence
\[
 J(F_0)/\ell J(F_0)\hookrightarrow H^1(G_{F_0,S},J[\ell]).
\]
The long exact cohomology sequence along the filtration bounds the dimension by \(2g\dim H^1(G_{F_0,S},\mathbf F_\ell)\). Since \(\mu_\ell\subset F_0\), Kummer theory bounds the latter dimension by \(O_{F_0,\ell}(1+|S|)\) from the units outside \(S\) and the \(\ell\)-torsion of the class group of the \(S\)-integers. That class group is a quotient of the fixed class group. There are \(O_\ell(1+\omega(d))\) places in \(S\). This proves \(\mathrm{rank}\,J(\mathbf Q)\ll_\ell1+\omega(d)\).

The uniform Mordell–Lang theorem bounds \(\#C_{\eta,\lambda}(\mathbf Q)\) by \(c_g^{1+\mathrm{rank}\,J(\mathbf Q)}\), with the base field fixed to \(\mathbf Q\). Summing over the at most \(6\cdot2^{\omega(d)}\) choices proves the claimed index bound after increasing \(A_\ell\). This step controls the number of indices for each twist and imposes no hypothesis on their heights. [Dimitrov, Gao and Habegger, *Uniformity in Mordell–Lang for curves*](https://arxiv.org/abs/2001.10276)

## An ordered divisor chain

Let \(q_1\ge\cdots\ge q_t\) list the prime factors of the odd index \(n>1\) with multiplicity, where \(t=\Omega(n)\). Set \(m_0=1\), \(m_j=q_1\cdots q_j\). At any \(p\mid B_{m_j}\), the elliptic reduction order \(s\) of \(G\) is a divisor of \(m_j\) greater than one, since \(B_1=1\). Such a prime is good (the odd scalar denominator is prime to 6). Therefore \(s\ge q_j\). Full rational two-torsion and the odd order \(s\) give \(4s\mid\#E_6(\mathbf F_p)\); Hasse yields \(p\ge(2\sqrt s-1)^2>s\). Hence \(p\) is prime to every remaining multiplier \(q_{j+1},\ldots,q_t\). These multipliers preserve the full formal depth, so the valuations at previously occurring primes stay fixed.

The cofactors \(D_\ell(B_{m_j})\) consequently form a nested divisor chain in which a strict increase introduces a previously absent prime. If \(k'=\omega(R_\ell(B_n))\), at most one distinct cofactor in the chain has any given number \(i\) of prime divisors. The preceding count now gives
\[
              1+\Omega(n)\le\sum_{i=0}^{k'} A_\ell^{1+i}
                              \ll_\ell A_\ell^{k'}.                       \tag{3}
\]
In particular a fixed bound on \(k'\) bounds the total number of prime factors of \(n\), counted with multiplicity, independently of their sizes.

There is an explicit bound \(Q_\ell\) for every odd prime index \(q\) at which \(B_q\) is an \(\ell\)-th power. Set \(Q_2=Q_3=1\) by the [square classification](abc_full_quartic_square_classification.md) and [cube classification](abc_full_quartic_cube_descent.md). For prime \(\ell\ge5\) take
\[
                     Q_\ell=\left\lfloor\frac{(\sqrt\ell+1)^2}{4}\right\rfloor.
\]
Indeed, the [Eisenstein descent for perfect powers](abc_full_quartic_prime_exponents.md) gives \(\ell\mid a_q\), \(\ell\nmid B_q\) at such an index. Then \(x([q]G)=-3a_q^2/B_q^2\) reduces to zero, so \([q]G=T=(0,0)\) in \(E_6(\mathbf F_\ell)\). The order of \(G\) there is \(2q\): it divides \(2q\) but not \(q\), and its ordinate 9 is nonzero modulo \(\ell\), excluding order two. Its cyclic group meets the full rational two-torsion in precisely \(\{O,T\}\), so \(4q\mid\#E_6(\mathbf F_\ell)\). Hasse gives the displayed bound. More precisely, \(q\) must equal the order of \(G+T\) modulo \(\ell\), since \(q\) is odd and \(G+T\ne O\). Thus one may compute that order and test the single candidate when it is an odd prime.

If \(q_1>Q_\ell\), there is a prime \(p\mid R_\ell(B_{q_1})\) with exact order \(q_1\), and \(p>q_1\). It survives in \(R=R_\ell(B_n)\) by the ordered chain. If \(q_1\le Q_\ell\) then \(q_1\) is already bounded. It follows that \(\log n\ll_\ell\Omega(n)\log(2R)\). In combination with (3) this also gives \(R\gg_{\ell,s} n^{c_{\ell,s}}\) whenever \(k'\le s\), for some \(c_{\ell,s}>0\).

Put \(H=\log(2R)\). Distinct prime factors give \(R\ge(k'+1)!\), so \(H\gg k'\log(2k')\) for \(k'\ge1\). If \(H\ge(\log\log n)^2\), (1) already follows. Otherwise (3) and the preceding bound for \(\log n\) give \(\log\log n\le O_\ell(1)+k'\log A_\ell+\log H\); the last term is \(O(\log\log\log n)\), forcing \(k'\gg_\ell\log\log n\). This proves (1), and also excludes bounded \(R\) at unbounded indices.

## A bound in terms of the radical of the index

For each prime \(q>Q_\ell\) choose a witness \(p(q)\mid R_\ell(B_q)\). Its order is exactly \(q\), so different \(q\)'s have different witnesses, and \(p(q)\ge(2\sqrt q-1)^2>2q\) for odd \(q\ge3\). On the vertices \(q\mid n\), \(q>Q_\ell\), taking the next vertex \(p(q)\) therefore gives disjoint strictly increasing chains, ending at distinct terminal primes \(p\nmid n\). The terminal prime belongs to \(R\), since its positive valuation in the preceding prime-index denominator is preserved under multiplication of the index by \(n/q\).

For a chain \(q_1<\cdots<q_s<p=q_{s+1}\), put \(L=\log p\), \(c=\log4\). Hasse gives \(\log(q_{i+1}/q_i)\ge c-O(1/\sqrt{q_i})\). Summing backwards yields
\[
   \sum_{i=1}^s\log q_i
   \le sL-\frac{c}{2}s(s+1)+O\!\left(\sum_{i=1}^s\frac{i}{\sqrt{q_i}}\right)
   \le\frac{L^2}{2c}-\frac L2+O(1).
\]
The error is absolute because the chain at least doubles at each step. For large terminal primes the right-hand side is at most \(L^2/(2c)\); bounded terminals contribute a bounded total since they are distinct. The excluded rational prime divisors \(q\le Q_\ell\) contribute \(O_\ell(1)\) to \(\log\operatorname{rad}(n)\). Summing the squared logarithms of the remaining distinct terminal primes gives at most \((\log R)^2\), proving (2).

## A terminating census for every exponent

Given integers \(k\ge2\) and \(X\ge1\), choose any prime factor \(\ell\mid k\) and set \(T=\max(X,Q_\ell)\). The following algorithm returns exactly the positive odd indices with \(R_k(B_n)\le X\). If \(n>1\) qualifies and its largest prime factor \(q_1\) exceeds \(Q_\ell\), the ordered chain gives a prime \(p>q_1\) in \(R_\ell(B_n)\mid R_k(B_n)\), hence \(q_1<X\). Otherwise \(q_1\le Q_\ell\). Therefore every prime factor of a qualifying index is at most \(T\).

1. For each odd prime \(q\le T\), compute \(B_{q^e}\) for successive \(e\ge1\). Strip the full prime powers at **all** primes through \(T\). Stop at the first \(e=e_q\) for which the remaining positive integer fails the exact \(\ell\)-th-power test. This certifies a prime \(p>T\) with \(\ell\nmid v_p(B_{q^{e_q}})\) without factoring the remaining integer.
2. Each search terminates. If every test for a fixed \(q\) passed, the infinitely many distinct indices \(q^e\) would have \(\ell\)-th-power-free cofactor supported on the finite set of primes through \(T\). Their exponents in that cofactor are at most \(\ell-1\), so there are finitely many possible cofactors, each realized by only finitely many indices. For this termination argument Faltings' theorem on the finitely many genus-\(2\ell-1\) twists above already suffices.
3. If \(q^{e_q}\mid n\) for a qualifying index, the witness \(p>T\) cannot divide \(n\). The multiplier \(n/q^{e_q}\) preserves its positive formal depth; thus \(p\mid R_\ell(B_n)\mid R_k(B_n)\), contradicting \(p>X\). Enumerate the finite products over odd primes \(q\le T\) with \(0\le v_q(n)< e_q\), including the empty product \(n=1\). Compute \(B_n\) by rational elliptic addition and retain exactly those with \(R_k(B_n)\le X\), for example by trial division. The same index bounds apply to the census with \(D_k(B_n)\le X\), since \(R_k\le D_k\); use that cofactor in the final test.

All searches have explicit stopping tests. Finiteness guarantees that the prime-power loops reach those tests, without a numerical height bound for the curves. Using \(T\) also in the stripping step ensures that the witness is prime to every candidate index when \(Q_\ell>X\).
