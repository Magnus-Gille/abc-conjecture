# An upper bound for one prime at any index

On \(E:y^2=x^3-36x\), take \(G=(-3,9)\) and write \(B_m\) for the square root of the reduced abscissa denominator of \([m]G\). For a positive integer \(m\), put
\[
 D(m)=\prod_{\substack{\ell\mid m\\\ell\equiv1\bmod4}}
             (1-1/\ell)^{-2}.
\]
Uniformly in \(m\ge2\),
\[
 \boxed{\quad \max_{p\mid B_m}v_p(B_m)\log p\ll_E m^2/D(m).\quad}
 \tag{1}
\]
Use zero for the empty maximum. In particular, if \(r\) is the product of the primes \(1\bmod4\) through \(X\), then \(D(2r)\asymp\log X\asymp\log\log r\). The entire support of the primitive signature \(a^4+3b^2=4w^4\) at odd index \(r\) is captured by \(B_{2r}=2|abw|\), and the largest term has \(\log(4w^4)=4\widehat h(G)r^2+O(1)\). No single prime in this denominator can contribute a positive limiting fraction of that logarithm along these indices. The same conclusion holds for any choice of \(o(D(2r))\) primes together. [Signature and exact denominator](abc_full_quartic_signature.md)

## Lifting a reduction point to torsion

For any Gaussian ideal \(I\ne(1)\), let \(L(I)\) sum the initial formal depths, weighted by \(\log N\mathfrak p\), over good Gaussian prime ideals \(\mathfrak p\) where the reduction of \(G\) has exact annihilator \(I\). There is a uniform upper bound
\[
 L(I)\ll_E\Phi(I),\qquad \Phi(I)=|(\mathbf Z[i]/I)^\times|.
 \tag{2}
\]
To prove it, form the product
\[
 F_I=\prod_{\substack{T\in E(\overline{\mathbf Q})_{\rm tors}\\
                        \operatorname{Ann}(T)=I}}
                          (x(G)-x(T)).
\]
The action of \(\mathbf Z[i]\) is defined over \(K=\mathbf Q(i)\), so \(F_I\in K\); it is nonzero because \(G\) is nontorsion. Via complex uniformization \(E[I]\) is a free rank-one \(\mathbf Z[i]/I\)-module. The number of factors is \(\Phi(I)\). Each torsion abscissa has bounded absolute logarithmic height by the canonical height comparison on the fixed curve. Hence \(h(F_I)\ll_E\Phi(I)\).

At a contributing place \(\mathfrak p\) above \(p\ge5\), let \(s\) be the order of \(G\bmod p\). This order is prime to \(p\), since \(4\mid\#E(\mathbf F_p)<4p\). Also \(I\mid(s)\). Thus all nonzero torsion points used in the product have \(p\)-integral abscissas: prime-to-\(p\) torsion specializes injectively. Reduction on \(E[s]\) is an isomorphism over algebraic closures, commuting with the Gaussian action. Consequently the reduction of \(G\) has a unique lift \(T\in E[s]\) with the same annihilator \(I\). The formal depth of \(G-T\) is that of \(sG\), because \(s\) is a unit at \(\mathfrak p\). This equals the first depth \(e_{\mathfrak p}\) at a generator of \(I\), as its complementary factor in \(s\) is also a unit at \(\mathfrak p\). The two integral abscissas agree modulo \(\mathfrak p^{e_{\mathfrak p}}\). Every other factor is integral at this place, so \(v_{\mathfrak p}(F_I)\ge e_{\mathfrak p}\). Summing these positive valuations with their norm weights costs at most \([K:\mathbf Q]h(F_I)\) by the product formula. This proves (2) and applies equally to the integral rational point \(Q\) on the scaled model used below.

At a good prime \(p\mid B_m\), its Gaussian annihilator \(I\) divides \((m)\). First depth times \(\log p\) is at most \(L(I)\), and further lifting costs at most \(\log m\). The ideal totient is monotone under divisibility, so
\[
 \Phi(I)\le\Phi((m))\le m^2/D(m).
\]
Since \(D(m)\ll\log\log(3m)\) by Mertens in progressions, the lifting term and the \(O_E(\log(2m))\) contribution of each bad prime are absorbed, proving (1).

There is a stronger bound on the combined weight of any \(k\ge1\) rational primes:
\[
 \sum_{p\in S}v_p(B_m)\log p
       \ll_E \frac{m^2}{D(m)}\log(2k)+\log(2m),
       \qquad |S|=k .
 \tag{3}
\]
Indeed write \(J=(m)/I\). Multiplicativity and the common-prime factors of the ideal totient give \(\Phi((m))\ge\Phi(I)\Phi(J)\). Among any \(k\) distinct Gaussian ideals \(J\), the sum of \(1/\Phi(J)\) is \(O(\log(2k))\). To see this, the count with \(\Phi(J)\le x\) is \(O(x)\). The second moment \(\sum_{NJ\le Z}(NJ/\Phi(J))^2\ll Z\) follows by expanding over squarefree divisor ideals, since the coefficient at a prime ideal of norm \(q\) is \((1-1/q)^{-2}-1=O(1/q)\), and the number of multiples of a divisor \(\mathfrak d\) is \(O(Z/N\mathfrak d)\). The resulting Euler product converges. Among \(2^jx<NJ\le 2^{j+1}x\), the second moment bounds the count with \(\Phi(J)\le x\) by \(O(2^{-j}x)\); the smaller ideals contribute \(O(x)\). Ordering the totients now proves the reciprocal-sum bound.

At most \(2k\) ideals \(I\) arise from primes in \(S\). Apply (2) and the reciprocal-sum bound to their distinct complementary \(J\)'s. The sum of all further formal lifting contributions is \(O(\log(2m))\), since each good \(p\) adds at most \(v_p(m)\log p\), proving (3). On the split primorial sequence a fixed positive fractional excess in \(B_{2r}\) consequently requires at least \((\log r)^{c_\delta}\) distinct primes of exponent at least two, for some \(c_\delta>0\) depending on that fraction.

## Simultaneous control on the twelfth-power family

On the earlier orbit giving \(U^2+3V^2=W^{12}\), let \(A_n\) denote the good-prime part of the support integer after removing the independent quartics \(F_+F_-\). There is an explicit sequence of odd \(n\to\infty\) on which
\[
 \max_{p\mid A_n} v_p(A_n)\log p
        \ll \frac{n^2}{(\log\log n)^{1/5}} .
 \tag{4}
\]
Its good-prime factors come from ordinary denominators at \(2n,n-1,n+1\) and the Gaussian denominator of \([n+i]Q+T_0\) at the rational point \(Q=(-8,-64)\) on \(v^2=u^3-576u\), with \(T_0=(0,0)\). These supports are disjoint. Doubling removes the torsion translate and preserves good formal depth; the corresponding annihilator then divides \((2(n+i))\) at a chosen Gaussian place. Ordinary indices satisfy the same assertion with their own ideals. For a Gaussian multiplier \(\gamma\), the local bound from (2) is \(O_E(\Phi((\gamma)) + \log(2N\gamma))\), including further lifting. The Gaussian factor is a norm and at a contributing prime only one conjugate place occurs. This proves that it is enough to make the four ratios \(\Phi((\gamma))/N\gamma\) simultaneously small. [Exact denominator assignments and disjointness](abc_eisenstein_slice_marked_divisors.md)

Partition the ten reduced residue classes modulo 44 that are \(1\bmod4\) into four fixed groups of sizes \(2,2,2,4\). For each prime \(\ell\le X\) in the first three groups prescribe \(n\equiv0,1,-1\bmod\ell\), respectively. In the last group prescribe one root of \(n^2\equiv-1\bmod\ell\), choosing the least positive root for definiteness. By the Chinese remainder theorem take odd \(n\in[M,2M)\), where \(M\) is twice the product of all the primes used. Then \(\log n\asymp X\). For each of \(2n,n-1,n+1\), both Gaussian primes above each assigned rational prime divide its ideal; for \(2(n+i)\) at least one does. Each class has reciprocal-prime sum \((1/20)\log\log X+O(1)\). In all four cases the assigned factors thus give \(\Phi((\gamma))/N\gamma\ll(\log X)^{-1/5}\). Each norm is \(O(n^2)\), giving (4). The finitely many bad-prime contributions elsewhere in the original support integer are \(O(\log(2n))\) at these indices. Applying the same complementary-ideal sum as in (3) to each of the four divisors bounds the combined mass of any \(k\) primes in \(A_n\) by \(O(n^2\log(2k)/(\log\log n)^{1/5}+\log(2n))\). A fixed fractional loss from those factors requires at least \(\exp(c_\delta(\log\log n)^{1/5})\) distinct repeated primes. The independent mark underlying \(F_+F_-\) lies outside this argument.
