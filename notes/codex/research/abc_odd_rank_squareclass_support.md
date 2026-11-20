# Odd valuations above ten million in elliptic denominators

Let \(B_r^2\) be the reduced denominator of the abscissa of \([r]R\) on \(E:y^2=x^3+16x^2+32x\), where \(R=(-8,16)\). Write \(\operatorname{sf}(b)=\prod_{v_p(b)\ {\rm odd}}p\). **For every positive odd \(r\) except \(1,3,5,7,9,11\), there is a prime \(p>10^7\) for which \(v_p(B_r)\) is odd.** The exceptional values are

| \(r\) | \(1\) | \(3\) | \(5\) | \(7\) | \(9\) | \(11\) |
|---:|---:|---:|---:|---:|---:|---:|
| \(\operatorname{sf}(B_r)\) | 1 | 1 | 281 | 117041 | 29651721 | 2797478818681 |

All primes dividing the six displayed squareclasses are at most \(10^7\). At every other odd index, squarefulness of \(B_r\) would require \(p^3\mid B_r\) for a prime above this cutoff. The result allows odd valuations greater than one. [Self-contained Python verifier](abc_odd_rank_squareclass_support.py)

## Descent from the largest prime of the index

The model has good reduction at every odd prime. At such a prime \(p\), let \(t_p\) be the order of \(R\bmod p\). Then \(p\mid B_r\) exactly when \(t_p\mid r\), and for \(p\mid B_j\) one has
\[
v_p(B_{jk})=v_p(B_j)+v_p(k).
\]
Indeed the denominator exponent is the valuation of the formal parameter \(-x/y\) in the identity disk. Over \(\mathbb Q_p\) for odd \(p\), the formal logarithm preserves that valuation and takes multiplication by \(k\) to ordinary multiplication. All \(B_r\) for odd \(r\) are odd. The earlier rational-point classification gives \(\operatorname{sf}(B_r)=1\) precisely at \(r=1,3\), using \(B_r=\sqrt{s^2+2t^2}\) on the full slope parametrization. [Formal groups and reduction, Silverman, Chapters IV and VII](https://doi.org/10.1007/978-0-387-09494-6) · [Denominator identity](abc_octic_mixed_skew_denominator.md) · [Full orbit of slopes](abc_octic_full_mixed_orbit.md) · [Fourth-power classification](abc_octic_mixed_elliptic_chabauty_11.md)

Suppose \(L\ge5\) is the largest prime divisor of \(r\). Every \(p\mid B_L\) has \(t_p=L\), since \(R\) is affine integral. The rational point of order two and Hasse's inequality give \(2L\le\#E(\mathbb F_p)\le(\sqrt p+1)^2\). For \(L\ge7\) this implies \(p>L\). For \(L=5\) it rules out \(p=3\), and direct reduction gives \(\#E(\mathbb F_5)=6\). Hence \(p\nmid r\) and **every valuation in \(B_L\) persists unchanged in \(B_r\)**. In particular \(\operatorname{sf}(B_L)>1\) and \(\operatorname{sf}(B_L)\mid\operatorname{sf}(B_r)\). [Hasse's theorem, Silverman, Chapter V](https://doi.org/10.1007/978-0-387-09494-6)

## Exhausting the small primes

Put \(M=10^7\). If \(\operatorname{sf}(B_r)\) is supported on primes through \(M\) and \(L\ge5\), at least one \(p\le M\) has \(t_p=L\). Every odd-denominator prime splits in \(K=\mathbb Q(\sqrt{-2})\). Indeed an odd-order \(R\bmod p\) is a double, and \(x(2P)=(x(P)^2-32)^2/(4y(P)^2)\), so \(-8\) is a square modulo \(p\). The curve has CM by \(\mathbb Z[\sqrt{-2}]\), defined over \(K\). At a split \(p=a^2+2b^2\) the Frobenius has norm \(p\) in this ring, hence trace \(2a\) or \(-2a\). The norm-Euclidean ring has units \(\pm1\), so a split odd prime has a unique such representation with \(a,b>0\). Thus every eligible \(L\) is a prime divisor of one of \(p+1\pm2a\). [Splitting and CM Frobenius for this model](abc_odd_rank_quadratic_large_gaps.md) · [Explicit CM map](abc_octic_mixed_skew_denominator.md)

The verifier enumerates these norm representations and the prime divisors \(L\ge5\) of both candidate orders. It keeps exactly the pairs with \(\psi_L(R)=0\bmod p\), where \(\psi_L\) is the division polynomial. At good reduction the homogeneous multiplication formulas have no common zero. Since \(R\) is integral, \(v_p(\psi_L(R))=v_p(B_L)\) at every odd \(p\). Of the \(24{,}813\) pairs kept, all have \(\psi_L(R)\ne0\bmod p^2\). They cover \(22{,}716\) distinct prime indices, the largest \(4{,}999{,}529\). [Division polynomial identities](https://math.mit.edu/classes/18.783/2023/LectureNotes5.pdf) · [Recurrences and finite certificate](abc_odd_rank_squareclass_support.py)

For each retained \(L\), let \(c_L\) be the product of the retained \(p\) for that index. If \(B_L\) has no odd valuation above \(M\), its squareclass is exactly \(c_L\). For an auxiliary prime \(h\equiv1\bmod8\), both \(-1\) and 2 are squares. The equality at odd primes therefore implies that \(c_L\psi_L(R)\) must reduce to zero or a square modulo \(h\). Tests through \(h=433\) eliminate all but \(L=5,7,11\); direct evaluation confirms their displayed squareclasses.

It follows that every prime of \(r\) belongs to \(\{3,5,7,11\}\). Strip all prime factors at most \(M\) from \(B_j\) at each of the following divisors. An exact integer square-root check gives a nonsquare residual in every column.

| \(j\) | 15 | 21 | 25 | 27 | 33 | 35 | 49 | 55 | 77 | 121 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Residual bit length | 33 | 46 | 209 | 157 | 264 | 400 | 815 | 976 | 1933 | 5018 |

Each nonsquare supplies a prime \(p>M\) with odd valuation at \(j\). If \(j\mid r\), this valuation persists because \(p\nmid r\). The six products of two distinct primes from \(\{3,5,7,11\}\) consequently exclude every \(r\) having two different prime divisors. The divisors \(27,25,49,121\) cut off the four remaining prime-power cases. This leaves exactly the six indices displayed above. The argument covers unbounded \(r\). [Verification program](abc_odd_rank_squareclass_support.py)

## The quotient curve and its rational points

For \(Q\in E\) put \(f(Q)=x(Q)-x(Q-R)\), and let \(\lambda=(y(Q)+16)/(x(Q)+8)\) be the slope of the chord through \(-R\). The other abscissas \(x(Q),x(R-Q)\) solve \(X^2+(8-\lambda^2)X-8(\lambda-2)^2=0\). Its discriminant gives
\[
f^2=\lambda^4+16\lambda^2-128\lambda+192=16G((\lambda-2)/2,1),
\qquad
G(m,n)=m^4+4m^3n+10m^2n^2-4mn^3+n^4.
\]
For \(Q=[k]R,\ k\ge2,\ r=2k-1\), the division-polynomial addition identity gives \(f=-\psi_r(R)/(\psi_k(R)^2\psi_{k-1}(R)^2)\). Hence \(v_p(f)\equiv v_p(B_r)\bmod2\) at every odd \(p\). At 2, write \(m/n=(\lambda-2)/2\) in lowest terms; \(G(m,n)=(fn^2/4)^2\) is an integer square. Odd \(m,n\) would give \(G\equiv12\bmod16\), so \(G\) is odd, and \(v_2(f)=2-2v_2(n)\) is even. Thus \(|f([k]R)|\) has the positive rational squareclass of \(B_{2k-1}\). [Division polynomial addition identity and its sign convention](https://doi.org/10.1007/978-0-387-09494-6)

Consequently \(z^2=df(Q)\) has smooth projective model \(D_d:d^2w^4=G(m,n)\), by \(m/n=(\lambda-2)/2,\ w/n=z/(2d)\). The inverse recovers \(f=z^2/d\) and \(x(Q)=(\lambda^2-8+f)/2\). The rational elliptic quotient is \(y_0^2=G(m,n)\). Over \(\mathbb Q(i)\), set \(U=m+in,\ V=m-in,\ A=-(1+i)/2\). Then \(G=AU^4+2U^2V^2+\bar A V^4\). In the \(V=1\) chart put \(h=w/V,\ C=1+A(U/V)^2\), so \(C^2=Ad^2h^4+1/2\). Mapping by \(X=Ad^2h^2,\ Y=Ad^2 h C\) gives \(Y^2=X^3+(Ad^2/2)X\), whose two-isogenous curve has coefficient \((1+i)d^2\). The sign changes of \(U,V,w\) supply the three independent elliptic differential lines. The two quotients over \(\mathbb Q(i)\) are conjugates. [Quotient decomposition for the underlying forms](abc_octic_mixed_fourth_power_quotients.md)

For a positive squarefree \(d\) supported through \(10^7\), the following table gives **all** \(D_d(\mathbb Q)\). Each representative \((m,n,w)\) stands for the four projective points \([m:n:\pm w]\), \([-n:m:\pm w]\). All other such \(d\) have empty rational locus.

| \(d\) | Representatives \((m,n,w)\) |
|---:|---|
| 1 | \((1,0,1),\ (2,1,3)\) |
| 281 | \((5,18,1)\) |
| 117041 | \((155,252,1)\) |
| 29651721 | \((-10819,7868,3)\) |
| 2797478818681 | \((-1853539,429930,1)\) |

To see completeness, scale \(m,n\) to coprime integers. Since \(dw^2\) is a rational square root of the integer \(G\), it is an integer, and squarefreeness of \(d\) makes \(w\) integral. Odd \(m,n\) give \(G\equiv12\bmod16\), so \(m,n\) have opposite parity. Away from \(mn=0\), put \(s=m^2+2mn-n^2,\ t=2mn\), allowing a simultaneous change of sign for \(t>0\). These are primitive, and
\[
(s-t)^2+t^2=(m^2+n^2)^2,\qquad s^2+2t^2=G(m,n)=d^2w^4 .
\]
The full-orbit theorem gives exactly one positive odd index \(r\ge3\) for each such signed slope, with \(B_r=\sqrt{s^2+2t^2}=dw^2\). Each slope occurs at most twice on the parameter line since \(u=m/n\) satisfies \(u^2+2(1-s/t)u-1=0\), with roots \(u,-1/u\). Each parameter gives at most two choices of \(w\). The table attains these bounds by substitution; the two degenerate parameter values \(mn=0\) require \(d=1\). [Complete slope parametrization](abc_octic_full_mixed_orbit.md) · [Denominator formula](abc_octic_mixed_skew_denominator.md) · [Coordinate checks](abc_odd_rank_squareclass_support.py)

## A terminating algorithm for every finite support

Given any finite set \(S\) of rational primes, the set of positive odd indices with \(\operatorname{sf}(B_r)\) supported on \(S\) is effectively computable. Take \(M=\max(\{3\}\cup S)\). The largest-prime argument gives \(P^+(r)\le M\) for \(r>1\). For every odd prime \(\ell\le M\), successively compute \(B_{\ell^e}\), starting at \(e=1\), and strip the primes through \(M\). Stop that search at the first exponent \(e_\ell\) for which the residual is nonsquare.

Each search terminates. Otherwise infinitely many different slopes would have \(\operatorname{sf}(B_{\ell^e})\) among the finitely many squarefree products of primes through \(M\). The full-orbit theorem and the Pythagorean parametrization would put infinitely many rational points on one \(D_d\). These plane quartics are smooth of genus three, since \(G(m,1)\) has discriminant \(2^{17}\) and \(G(1,0)=1\). Faltings's theorem gives finiteness. The nonsquare residual at the stopping index has an odd-valuation prime \(p>M\) whose valuation persists in every \(M\)-smooth multiple. Accordingly \(v_\ell(r)<e_\ell\) for every sought \(r\). Enumerate this finite exponent box, testing membership by removing the primes of \(S\) and checking the residual for squareness; a specific class inside the same support is tested by requiring its valuations modulo two as well. [Faltings, finiteness of rational points](https://doi.org/10.1007/BF01388432) · [Quartic twists and orbit lifts](abc_octic_mixed_parity_kernel.md)

This algorithm provides a computable bound on the last exceptional index at each given cutoff. Faltings supplies termination of a search whose steps are decidable. No effective height bound from Faltings, running-time estimate in \(M\), or new effective Mordell conjecture is required.

There is also an asymptotic lower bound for the largest odd-valuation prime \(M_r=P^+(\operatorname{sf}(B_r))\) itself. At large \(r\) one has \(P^+(r)\le M_r\), since \(r=3^a\) with \(a\ge2\) inherits \(11\mid\operatorname{sf}(B_9)\). For every \(j\mid r\), all valuations of \(B_j\) above \(M_r\) must then be even, by the lifting formula. Distinct \(j\ge3\) give distinct slopes. The uniform point bound \(\#D_d(\mathbb Q)\le C^{1+\omega(d)}\) for these twists therefore gives
\[
\tau(r)-1\le \sum_{d\mid\prod_{p\le M_r}p} C^{1+\omega(d)}
       = C(1+C)^{\pi(M_r)}.
\]
Since \(\log r\le(\tau(r)-1)\log M_r\), the elementary prime-counting upper bound yields
\[
P^+(\operatorname{sf}(B_r))\gg(\log\log r)(\log\log\log r).
\]
The implied constant uses the uniform Mordell–Lang bound for curves and the rank bound for the twists. The terminating algorithm above supplies a separate effectivity statement for individual cutoffs. [Uniform bound and rank proof for these twists](abc_octic_mixed_parity_kernel.md) · [Dimitrov, Gao and Habegger](https://arxiv.org/abs/2001.10276)
