# Counting small odd-multiplicity products simultaneously over smooth orders

Fix a finite set \(S\) of primes. For coprime positive \(B<A\) and an \(S\)-smooth order \(m\) with \(\varphi(m)\ge6\), let
\[
        K_S(A,B;m)=\prod_{\substack{p\notin S\\v_p(\Phi_m(A,B))\ {\rm odd}}}p.
\]
Every prime in this product has exact order \(m\) for \(A/B\bmod p\), since \(p\nmid mAB\) and \(T^m-1\) is separable modulo \(p\). We prove the all-heights estimate
\[
 \#\{(A,B,m):K_S(A,B;m)\le Y\}
       \ll_S Y(1+\log Y)^{C_S}\qquad(Y\ge1).
 \tag{1}
\]
The count includes every allowed order at once. In particular only finitely many triples have no such prime. For every sufficiently large \(S\)-smooth order, **every** coprime base pair has a primitive prime of odd multiplicity. The proof gives no numerical bound on this last threshold.

## Reduction to finitely many fixed curves

Set \(d=\prod_{p\mid m} p^{\min(v_p(m),4)}\) and \(u=m/d\). The possible \(d\) form a finite set depending only on \(S\), and \(\varphi(d)\ge6\). Indeed, whenever truncation changes an exponent, \(d\) has a divisor \(p^4\) with \(\varphi(p^4)\ge8\). Every prime of \(u\) divides \(d\). Repeated prime substitution in the cyclotomic polynomial gives the homogeneous identity
\[
                     \Phi_m(A,B)=\Phi_d(A^u,B^u).
\]
Put \(L=\prod_{p\in S}p\). If \(K_S(A,B;m)\le Y\), the whole squarefree part \(D\) of this integer satisfies \(D\le LY\). For each \(d\), the number of coprime outputs \(U>V\ge1\) with \(\Phi_d(U,V)=Dz^2\) is at most \(c_d^{1+\omega(D)}\). This follows from two-descent on the Jacobians of these fixed-form quadratic twists and uniform Mordell–Lang. Summing over squarefree \(D\le LY\) and the finitely many \(d\) bounds the number of decorated outputs \((d,U,V)\) by \(O_S(Y(1+\log Y)^{c_S})\). [Fixed-form twist bound and its proof](abc_cyclotomic_large_square_twists.md)

First take \(Y=1\). Each of the finitely many outputs gives finitely many input triples, since \(U=A^u\ge2^u\) bounds \(u\), and \(u\) determines \(m=du\) and the positive roots \(A,B\). This proves finiteness for the empty product. The maximal height of these outputs is not supplied by the point-count theorem. Its contribution to the constant in (1) is ineffective.

For all remaining triples choose any \(p\mid K_S(A,B;m)\). Its exact order implies \(m\mid p-1\), hence \(m<p\le Y\). Each decorated output can therefore arise from at most
\[
            \prod_{p\in S}\left(1+\left\lfloor\frac{\log Y}{\log p}\right\rfloor\right)
\]
choices of the \(S\)-smooth integer \(u\le Y\). Again, each \(u\) gives at most one triple. This proves (1).

## Consequences for full differences

For any \(0<\delta<2\), all but \(O_{S,\delta}(H^{2-\delta}(1+\log H)^{C_S})\) coprime pairs \(1\le B<A\le H\) have \(K_S(A,B;m)>H^{2-\delta}\) **simultaneously for every** \(S\)-smooth \(m\) with \(\varphi(m)\ge6\). Apply (1) with \(Y=H^{2-\delta}\) and project to the bases.

Write \(\operatorname{sf}_{S^c}(M)\) for the product of the primes outside \(S\) which occur in \(M\) to odd exponent. There is a constant \(c(S)>0\) such that, for every \(S\)-smooth \(N\) and all coprime \(A>B\ge1\),
\[
              \operatorname{sf}_{S^c}(A^N-B^N)\ \ge\ c(S)\, N^{\tau(N)/2}.
 \tag{2}
\]
Here \(\tau\) counts the positive divisors. Let \(E_S\) contain the finitely many orders with \(\varphi(d)<6\) and the orders in the finite list of empty-product exceptions. For every divisor \(d\mid N\) outside \(E_S\) there is an odd prime \(p_d\notin S\) of exact order \(d\) occurring to odd exponent. Distinct \(d\) give distinct primes. Since \(p_d\nmid N\), the valuation is unchanged in \(A^N-B^N\), by lifting the exponent. Multiply \(p_d\ge d+1\) over these divisors and use \(\prod_{d\mid N}d=N^{\tau(N)/2}\). One may take \(c(S)=(\prod_{d\in E_S}d)^{-1}\). Explicit uniform exclusions for several infinite sets of orders give numerical products in those cases. [Explicit order families](abc_cyclotomic_odd_primitive_grid.md)

For example, at \(N=6^k\), (2) gives a log squarefree-part lower bound of \(\frac12 k(k+1)^2\log6-O(1)\). Even for the fixed base \((2,1)\), the bound needed for abc is \((1-o(1))6^k\log2\) for the log radical.
