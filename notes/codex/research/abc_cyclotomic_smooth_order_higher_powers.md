# Small products of primitive primes whose multiplicities are nonzero modulo an exponent

Fix a finite set of primes \(S\) and an integer \(e\ge3\). For coprime
positive integers \(A>B\) and an \(S\)-smooth integer \(m\), put
\[
 H_e(A,B;m)=\prod_{\substack{p\notin S\\ e\nmid v_p(\Phi_m(A,B))}}p .
\]
Each prime in the product gives exact order \(m\) for \(A/B\bmod p\).
Indeed \(p\nmid mAB\), and the cyclotomic factors of \(T^m-1\) have
disjoint roots modulo \(p\).

For \(Y\ge1\) there is an all-heights estimate
\[
 \boxed{\displaystyle
 \#\{(A,B,m):\ \varphi(m)\ge4,\ H_e(A,B;m)\le Y\}
       \ll_{S,e}Y(1+\log Y)^{C_{S,e}} .}
 \tag{1}
\]
Here and below the triples satisfy the coprimality, positivity and
smoothness conditions above. The count sums over every allowed order.
In particular, outside a finite set of orders depending only on \(S,e\),
every coprime base pair has a primitive prime of multiplicity
nonzero modulo \(e\). The linear exponent of \(Y\) in (1) comes from
counting the squarefree product of distinct primes directly. Four
cyclotomic roots suffice, even when \(e\nmid\varphi(m)\).

## A fixed cover with four branch points

Choose a prime power \(k=\ell^a\mid e\) with \(k\ge3\). One may take an
odd prime divisor of \(e\) if there is one, and \(k=4\) otherwise.
For the moment fix \(d\) supported on \(S\) with \(\varphi(d)\ge4\).
Choose four distinct primitive \(d\)-th roots \(\alpha_1,\ldots,\alpha_4\)
in \(K_1=\mathbf Q(\zeta_d,\zeta_k)\) and put
\[
 R(x)=\frac{(x-\alpha_1)(x-\alpha_2)}{(x-\alpha_3)(x-\alpha_4)}.
\]
Let \(C_1\) be the smooth projective model of \(y^k=R(x)\), and set
\(K=K_1(\operatorname{Jac}(C_1)[\ell])\). This is a fixed number
field for the chosen \(d,k\). For \(b\in K^\times\), let \(C_b\) be the
smooth projective model of \(b y^k=R(x)\), with Jacobian \(J_b\). Over
an algebraic closure the map to the \(x\)-line has degree \(k\), is
totally ramified at the two simple zeros and the two simple poles, and
is unramified elsewhere, including infinity. The simple zeros also give
geometric irreducibility. Riemann–Hurwitz gives
\[
            2g-2=-2k+4(k-1),\qquad g=k-1\ge2 .
\]

Fix a squarefree integer \(h\) supported outside \(S\). Consider
coprime \(U>V\ge1\) for which every \(p\notin S\) with
\(e\nmid v_p(\Phi_d(U,V))\) divides \(h\). Put \(x=U/V\). The four
linear factors give the identity
\[
   R(x)=\frac{(U-\alpha_1 V)(U-\alpha_2 V)}
                {(U-\alpha_3 V)(U-\alpha_4 V)}.
\]
In particular primes dividing the denominator \(V\) cause no local
condition. At a place of \(K\) of residue characteristic
\(p\notin S\), the distinct \(d\)-th roots remain distinct modulo that
place. At most one of the factors \(U-\alpha V\), over all primitive
\(d\)-th roots \(\alpha\), can have positive valuation. If \(p\mid V\)
they are all units, and if \(p\nmid V\) a vanishing factor specifies the
unique residue \(U/V\). Thus the valuation of any nonunit factor equals
the valuation of their product \(\Phi_d(U,V)\) at that place. For
\(p\nmid h\) the rational valuation of the product is divisible by
\(e\). Multiplication by the ramification index in \(K\) preserves
divisibility by \(k\). Hence \(v(R(x))\in k\mathbf Z\) away from places
above \(S\) and the prime divisors of \(h\).

## Counting the twists and their points

Let \(T\) consist of the archimedean places of \(K\), the places of bad
reduction of \(J_1\), and the finite places over \(S\), \(k\), or \(h\).
Then \(|T|\ll_{d,k,S}1+\omega(h)\). For \(q=k\) or \(q=\ell\) write
\[
 K(T,q)=\{b\in K^\times/K^{\times q}\mid
                       v(b)\equiv0\pmod q\text{ for }v\notin T\}.
\]
The sequence
\[
  1\longrightarrow \mathcal O_{K,T}^{\times}/\mathcal O_{K,T}^{\times q}
   \longrightarrow K(T,q)\longrightarrow
      \operatorname{Cl}(\mathcal O_{K,T})[q]\longrightarrow1
\]
is exact, by taking one \(q\)-th of the principal ideal divisor away from
\(T\). The unit theorem and the bound for the order of the localized
class group by the fixed class number give \(\#K(T,q)\le c_{K,q}^{1+|T|}\).
The class of \(R(x)\) lies in \(K(T,k)\). For a representative \(b\) in
that class there is a \(K\)-point on \(C_b\) above \(x\).

We next bound the rank of \(J_b(K)\) for every such class. The extension
\(K(\sqrt[k]{b})/K\) is a cyclic extension of \(\ell\)-power degree,
since \(\mu_k\subset K\). It is unramified outside \(T\). Indeed,
at \(v\notin T\) one may remove a \(k\)-th power of a uniformizer from
\(b\), after which a \(k\)-th root of the remaining unit generates an
unramified extension because \(k\) is invertible there. The map
\((x,y)\mapsto(x,\sqrt[k]{b}\,y)\) identifies the twist with \(C_1\)
over this extension. Consequently \(J_b\) has good reduction outside
\(T\), by the good reduction criterion for abelian varieties. As
\(J_1[\ell]\) is rational over \(K\), the action of Galois on
\(J_b[\ell]\) factors through a finite \(\ell\)-group. Its
\(2g\)-dimensional representation over \(\mathbf F_\ell\) has a
filtration by trivial one-dimensional quotients. This follows
inductively since a finite \(\ell\)-group acting on a nonzero vector
space in characteristic \(\ell\) has a nonzero fixed vector.

Write \(G_{K,T}\) for the Galois group of the maximal extension
unramified outside \(T\). At a good place away from \(\ell\), the
multiplication-by-\(\ell\) map on the abelian scheme is finite étale.
Lifts of local points therefore give unramified Kummer classes. The
global Kummer image of \(J_b(K)/\ell J_b(K)\) lies in
\(H^1(G_{K,T},J_b[\ell])\), by inflation. The preceding filtration and
the long exact sequences in cohomology give
\[
 \dim H^1(G_{K,T},J_b[\ell])\le 2g\dim H^1(G_{K,T},\mathbf F_\ell).
\]
Since \(\mu_\ell\subset K\), Kummer theory embeds the group on the
right in \(K(T,\ell)\). Hence \(\operatorname{rank}J_b(K)\ll_{d,k,S}
1+\omega(h)\). Uniform Mordell–Lang for curves bounds
\(\#C_b(K)\) by \(c(g,[K:\mathbf Q])^{1+\operatorname{rank}J_b(K)}\).
The coordinate \(x=U/V\) determines its positive coprime numerator
and denominator uniquely. Combining the twist count and the point
count proves
\[
  \#\{(U,V):\ H_e(U,V;d)\mid h\}\le c_{d,k,S}^{1+\omega(h)}.
  \tag{2}
\]
[Dimitrov, Gao and Habegger, *Uniformity in Mordell–Lang for curves*](https://arxiv.org/abs/2001.10276)

## Summing the orders and supports

For a general admissible \(m\), truncate each exponent at three and put
\[
       d=\prod_{p\mid m}p^{\min(v_p(m),3)},\qquad u=m/d .
\]
The finitely many possible \(d\) depend only on \(S\). If truncation
changes an exponent, then \(p^3\mid d\) for some \(p\), giving
\(\varphi(d)\ge4\). With no change this follows from the assumption on
\(m\). Since every prime of \(u\) divides \(d\), the cyclotomic
substitution identity gives \(\Phi_m(A,B)=\Phi_d(A^u,B^u)\).
Apply (2) to \(U=A^u,V=B^u\) and \(h=H_e(A,B;m)\).

For \(h=1\), (2) gives only finitely many decorated outputs \((d,U,V)\).
Each admits only finitely many \(u\), since \(U\ge2^u\), and each \(u\)
determines at most one original triple. This accounts for the empty
support. The proof gives no effective upper bound on the heights of
these finitely many outputs.

For \(h>1\), any \(p\mid h\) gives order \(m\), so \(m\mid p-1\) and
\(u\le m<p\le Y\). For each decorated output there are
\(O_S((1+\log Y)^{|S|})\) such smooth \(u\). For a fixed integer
\(L\ge c_{d,k,S}\) one has \(L^{\omega(h)}\le d_L(h)\), the number
of ordered factorizations of \(h\) into \(L\) factors. Summing the first
\(L-1\) factors against their reciprocal gives
\(\sum_{h\le Y}d_L(h)\le Y(1+\log Y)^{L-1}\). Summing (2) over
\(h\le Y\) and the finite set of \(d\) proves (1).

## Consequences and the degree threshold

For \(0<\delta<2\), all but
\(O_{S,e,\delta}(X^{2-\delta}(1+\log X)^{C_{S,e}})\) of the
coprime pairs \(1\le B<A\le X\) satisfy
\(H_e(A,B;m)>X^{2-\delta}\) simultaneously at every admissible order.
This follows by projecting (1) with \(Y=X^{2-\delta}\) to the base pair.

For \(S\)-smooth \(N\), let \(P_e\) be the product of primes outside
\(S\) whose valuations in \(A^N-B^N\) are nonzero modulo \(e\).
Then uniformly in the coprime bases,
\[
                        P_e\gg_{S,e}N^{\tau(N)/2}.
\]
Indeed, aside from a fixed finite set of divisors \(d\mid N\) (those
of totient below four and those allowing empty support), choose an
odd prime \(p\notin S\) of exact order \(d\) with
\(e\nmid v_p(\Phi_d(A,B))\). The valuation is the same in
\(A^d-B^d\) by separability, and the same in \(A^N-B^N\) by lifting
the exponent since \(p\nmid N\). The primes for different orders are
distinct and exceed their orders. Multiply them and use
\(\prod_{d\mid N}d=N^{\tau(N)/2}\).
[The quadratic case at degree at least six](abc_cyclotomic_smooth_order_parity.md)

The totient threshold cannot generally be lowered to two. For \(m=4\)
and even positive \(t\), write \((t+i)^e=A+iB\). For sufficiently
large \(t\) one has \(A>B>0\) from the leading terms, and
\(\Phi_4(A,B)=A^2+B^2=(t^2+1)^e\). The two coordinates are coprime.
The prime 2 is excluded by the odd norm. For an odd prime \(p\),
\(\mathbf F_p[i]\) is reduced, so if both coordinates vanished
modulo \(p\), the nonzero class \(t+i\) would be nilpotent. Thus
these infinitely many pairs all have empty support at this order.
