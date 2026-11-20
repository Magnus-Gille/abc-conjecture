# The squarefree part of an odd scalar denominator

Let \(B_r\) be the positive abscissa denominator square root of \(rR\), for \(R=(-8,16)\) on \(y^2=x^3+16x^2+32x\). Write \(d_r\) for the squarefree integer with \(B_r=d_r b_r^2\). Then **\(d_r\) tends to infinity at all odd indices**. Its largest prime factor does too. On every squareful subsequence these odd-valuation primes occur to order at least three.

## One explicit plane quartic for each square class

Scale the coordinates by \(x_{\rm old}=4x,\ y_{\rm old}=8y\), giving \(E:y^2=x^3+4x^2+2x\) and \(P=(-2,2)\). This preserves odd local denominator depths. Since \(2P=(1/4,-7/8)\), every even multiple of \(P\) lies in the formal group at 2. An odd multiple cannot also belong to that group since \(P\) does not. All odd multiples therefore have integral abscissa at 2 on both models. The point \(P\) has infinite order, for example because \(x(4P)=961/784\) has negative valuation at the good prime 7, whose formal logarithm is injective on the formal group over \(\mathbb Q_7\).

For odd \(r\ge3\), put \(Q=[(r+1)/2]P\). The line from \(-P\) to \(Q\) has equation \(y=t(x+2)-2\); it meets \(E\) again at \(P-Q\). The two abscissas \(x(Q),x(Q-P)\) are the roots of

\[
x^2+(2-t^2)x-2(t-1)^2=0.
\]

Put \(f(Q)=x(Q)-x(Q-P)\). Then \(f(Q)^2=t^4+4t^2-16t+12\). As a rational function of \(Q\) on \(E\), the divisor of \(f\) consists of four simple zeros at \(2Q=P\) and double poles at \(O,P\). Indeed equality of the two abscissas at a finite regular point amounts to \(Q=P-Q\), and the four distinct zeros account for the pole degree. The same calculation applies at every odd prime \(p\), since the reduction is good, \(P\ne O\) modulo \(p\), and multiplication by 2 is étale. At a pole, the valuation of \(f(Q)\) is even. At a zero its valuation equals the formal depth of \(2Q-P\). For instance lift the reduction of \(Q\) to the unique root \(T\) of \(2T=P\) in its residue disk. Both \(f(T+S)\) and the formal parameter of \(2S\) have unit linear term in the parameter of \(S\). At the other reductions both valuations are zero. At 2 precisely one of \(Q,Q-P\) has negative abscissa valuation, which is even. Thus

\[
|f(Q)|=d_r z^2,\qquad z\in\mathbb Q^\times.
\]

Consequently each \(r\ge3\) with \(d_r=d\) gives a rational point on

\[
C_d:\qquad d^2 z^4=t^4+4t^2-16t+12 .
\]

The quartic polynomial has discriminant \(2^{17}\), and the smooth projective plane quartic has genus three. Each \(t\) yields at most two points \(Q\), and distinct positive \(r\) give distinct \(Q\). Faltings' theorem proves that each \(d\) occurs at finitely many indices. Only finitely many squarefree integers have all prime divisors in any fixed finite set, proving the assertion about the largest prime of odd valuation. This direct Faltings argument supplies no effective threshold. The [finite-support algorithm](abc_odd_rank_squareclass_support.md) computes the exceptional indices for any prescribed finite support and gives all exceptions when the largest allowed prime is ten million.

More precisely, writing \(t=T/S\) in lowest terms with \(S>0\) gives the exact integer identity

\[
B_r^2=T^4+4T^2S^2-16TS^3+12S^4.
\]

Indeed \(S^2 f\) is an integer, since its square is the displayed integral binary quartic. It is a unit at every \(p\mid S\) by the monic leading coefficient. At odd \(p\), if \(Q\) reduces to \(O\) or \(P\), exactly one of the two abscissas has negative valuation, so their sum \(t^2-2\) has negative valuation and \(p\mid S\). At every other odd reduction the two abscissas are integral and \(t\) is integral by their sum. The positive valuations of \(S^2 f\) are thus exactly the formal depths of \(rP\) at odd primes. At 2 the unique negative-valuation abscissa likewise implies \(2\mid S\). Hence \(|S^2f|=B_r\). When \(B_r\) is squareful, its prime valuations give \(B_r=d_r^3 h^2\) with integral \(h\), and the displayed primitive quartic value is exactly \(d_r^6 h^4\).

## Inheritance gives a lower bound at every index with inert prime factors

A rational prime is called inert or split in this section according to its behavior in \(\mathbb Q(\sqrt{-2})\). Choose \(q_0\) so large that every prime \(q\ge q_0\) has \(d_q>1\). The [complete fourth-power classification](abc_odd_rank_squareclass_support.md) and Hasse inequality below allow the explicit choice \(q_0=7\). For each such \(q\) fix a prime \(p_q\) of odd valuation in \(B_q\). Its order of apparition is exactly \(q\), as \(P\) is integral and nonzero modulo all odd primes. Thus \(q\mapsto p_q\) is injective. The rational point of order two on \(E\) and the point of order \(q\) modulo \(p_q\) imply \(2q\mid\#E(\mathbb F_{p_q})\), and Hasse gives \(p_q\ge(\sqrt{2q}-1)^2>q\). Also \(p_q\) splits, because \(P\) in the odd-order subgroup is a double modulo \(p_q\); the abscissa of a nonzero double is a square by the duplication formula, and \(x(P)=-2\). If \(q\) is inert its sole possible nonunit annihilator divisor of \((q)\) is \((q)\). Consequently \(p_q=(1+aq)^2+2b^2q^2\) with \(b\ne0\), so \(p_q\ge2q^2+1\). This last step uses the CM Frobenius description. [Exact annihilators and reduction](abc_odd_rank_truncated_radical.md)

The same duplication argument proves that all prime divisors of \(B_r\) are \(1,3\bmod8\). Thus \(B_r\) is itself \(1\) or \(3\bmod8\). The exact quartic identity, in which \(S\) is even and \(T\) is odd, gives \(B_r^2\equiv1\bmod16\), so \(B_r\equiv d_r\equiv1\bmod8\). The number of prime divisors of \(d_r\) in the class \(3\bmod8\) is even.

At each sufficiently large inert prime index \(q\), this improves the product bound to \(d_q\ge8q^2+1\). If any \(p\mid d_q\) is \(1\bmod8\), the expression \(p=(1+aq)^2+2b^2q^2\) forces \(b\) even, hence \(|b|\ge2\). If there is no such prime, at least two different primes of \(d_q\) exceed \(2q^2\).

For \(q\mid r\), \(p_q\nmid r\) implies \(v_{p_q}(B_r)=v_{p_q}(B_q)\) by multiplication by the \(p_q\)-adic unit \(r/q\) on the formal group. Starting at any inert \(q\mid r\) above \(q_0\), follow \(q\mapsto p_q\) as long as the image still divides \(r\). The primes strictly increase, so the path ends. The terminal prime lies outside the divisors of \(r\) and divides \(d_r\). Injectivity and the fact that all successors split show that distinct inert starting primes have disjoint paths. Hence for every odd \(r\)

\[
d_r\ \ge\prod_{\substack{q\mid r,\ q\ge q_0\\ q\ {\rm inert}}}(2q^2+1).
\]

The number of prime factors of \(d_r\) is at least the number of factors in this product. Also \(d_r\ge(\sqrt{2P^+(r)}-1)^2\) if \(P^+(r)\ge q_0\), because the selected image of the largest prime factor cannot divide \(r\).

## Growth in density

In the following bounds average uniformly over positive odd \(r\le X\). Write \(L(r)=\sum_{q\mid r,\ q\ {\rm inert}}\log q\). There exists a nonnegative \(E(r)\) of bounded mean, uniformly in \(X\), with

\[
\log d_r\ge \log r+L(r)-E(r).
\]

In fact take

\[
E(r)=2\sum_{q<q_0}\log q+\log(r/\operatorname{rad}r)
+2\sum_{\substack{q\ge q_0\\q p_q\mid r}}\log q.
\]

For \(q\mid r\) large with \(p_q\nmid r\), each distinct \(p_q\mid d_r\) exceeds \(q\), or \(q^2\) when \(q\) is inert. Summing these contributions gives the bound. The middle error has mean \(O(\sum_q\log q/[q(q-1)])\). The last has mean \(O(\sum_q\log q/(q p_q))\) since \(q\ne p_q\). Both sums converge. In particular \(d_r\ge r^{1-o(1)}\) off a density-zero set of odd indices. The count of prime divisors of \(d_r\) is at least \((1-o(1))\log\log r\) off another density-zero set, by the normal order of \(\omega(r)\), since the count of lost \(q\)'s has bounded mean. Also \(d_r/r\to\infty\) in density. Indeed the count of inert prime divisors of \(r\) goes to infinity in density by the usual second moment for prime divisibility and the divergence of the inert reciprocal-prime sum, so \(L(r)\to\infty\) in density, whereas \(E(r)\) is bounded in probability. At squareful indices the exact representation \(B_r=d_r^3 a_r^2\) follows prime by prime.

For every fixed positive \(L_0(t)=o(\log t)\), relative density one of inert prime indices \(q\) have an odd-valuation prime \(p>q^2 L_0(q)\). The [prime-index sieve](abc_odd_rank_quadratic_prime_barrier.md) excludes all prime divisors below that threshold for almost all inert prime indices, since they have only the full annihilator. The argument leaves open whether any of the forced odd valuations is one.

## The ranks of the realized twists

Every twist \(C_d\) with a rational point has Jacobian rank at least three over \(\mathbb Q\). To see the two extra rank directions, put \(u=t-1\), \(U=u+i,\ V=u-i,\ A=(-1-i)/2\), and \(K=\mathbb Q(i)\). The quartic on the right is \(A U^4+2U^2V^2+\bar A V^4\). Thus

\[
(A U^2+V^2)^2=A d^2 z^4+\tfrac12 V^4 .
\]

It gives a nonconstant map over \(K\) to

\[
G_d:\quad Y^2=X^3-\tfrac{1+i}{4}d^2 X,\qquad
X=V^2/(2z^2),\quad Y=V(AU^2+V^2)/(2z^3).
\]

In homogeneous coordinates \(U,V,z\), the three nontrivial sign changes modulo the simultaneous sign give the three involutions of a Klein four group. The quotient by the whole group is a conic in \(U^2,V^2,z^2\). Each involution fixes four points and has genus-one quotient. The three resulting lines of differentials are the three distinct nontrivial character spaces of the Klein four group: a common invariant differential for two involutions would descend to the conic. The involution at \(z\) gives \(E\) via \(d z^2=f\) with \(f^2=t^4+4t^2-16t+12\); this last quartic is birational to \(E\) by the line construction. The involution at \(U\) gives the map to \(G_d\), and its conjugate is the quotient at \(V\), both up to isogeny. Descent of the pair yields the rational isogeny

\[
\operatorname{Jac}(C_d)\ \sim_{\mathbb Q}\ E\times
\operatorname{Res}_{K/\mathbb Q}G_d .
\]

For every nonzero rational \(d\), the torsion subgroup of \(G_d(K)\) consists of \(O,(0,0)\). To check this, untwist over \(M=K(\sqrt d)\) and use the fixed integral model \(G_1:y^2=x^3-4(1+i)x\). The following reductions are all good. The base counts follow from \(1+\sum_{x\in\mathbb F_p}(1+\chi(x^3-4(1+i)x))\). The counts in the quadratic residue extension are \((p+1)^2-(p+1-\#G_1(\mathbb F_p))^2\).

| \(p\) | image of \(i\) | \(\#G_1(\mathbb F_p)\) | \(\#G_1(\mathbb F_{p^2})\) |
|---:|---:|---:|---:|
| 5 | 2 | 10 | 20 |
| 5 | 3 | 8 | 32 |
| 29 | 17 | 34 | 884 |

At each of these places any residue extension to \(M\) has degree at most two. Injectivity of prime-to-residue-characteristic torsion under reduction makes its order divide the last entry. The first two rows bound the prime-to-five part by \(\gcd(20,32)=4\); the last row excludes five-torsion. Thus \(G_d(K)\) has torsion order dividing four. On its model \(y^2=x^3+bx\) with \(b=-4(1+i)d^2\), the valuation of \(b\) at \(1+i\) is odd. Hence there is just one nonzero two-torsion point over \(K\). A half of \((0,0)\) would satisfy \(x^2=b\) by the duplication formula, which this odd valuation excludes.

At any rational projective point of \(C_d\), the homogeneous \(V=u-iv\) is nonzero. Also \(z\ne0\), since the homogeneous quartic \((T^2-2S^2)^2+8S^2(T-S)^2\) is strictly positive at real projective points. The elliptic image therefore has finite nonzero \(X\), and the torsion result makes it nontorsion. Multiplication by \(i\) supplies an independent point on \(G_d(K)\), since \(G_d\) has Gaussian complex multiplication over \(K\). Together with \(P\) on \(E\) this proves the stated rank bound, which equals the genus. Thus no twist with a rational point satisfies the ordinary Chabauty rank inequality. The base-twist quotient and its exact rank also arise in the earlier [fourth-power analysis](abc_octic_mixed_fourth_power_quotients.md).

For \(d=1\) the Jacobian rank is exactly three. Use the elementary two-isogeny descent on \(H:y^2=x^3+ax^2+bx\). Its abscissa square classes include \(1\) at \(O\) and \(b\) at \((0,0)\); the dual model has coefficients \((-2a,a^2-4b)\). The rank of \(H\) is the sum of the two square-class image dimensions minus two. Outside the prime factors of \(b\) every abscissa valuation is even: this follows by inspecting the equation at positive and negative valuations. On \(E/\mathbb Q\) the points \(P,(0,0)\) give all four allowed classes \(\{\pm1,\pm2\}\). On the dual \(y^2=x^3-8x^2+8x\), every abscissa is nonnegative, and the torsion point gives the class of 8, so the image is \(\{1,2\}\). Thus the rational rank is one.

Over \(\mathbb Q(i)\), scale \(G_1\) to \(Y^2=X^3-4(1+i)X\), whose dual has coefficient \(16(1+i)\) at \(X\). Both square-class images are supported at \(1+i\); since the Gaussian integers form a PID with unit group generated by \(i\), each dimension is at most two. Hence the rank is at most two. The point \(S=(-2,2+2i)\) on this model satisfies \(x(3S)=(5390+4704i)/73^2\) by the chord law. This is nonintegral at a place over 73, where the model has good reduction and the local field is \(\mathbb Q_{73}\), so the formal logarithm excludes torsion. Therefore \(S,[i]S\) are independent and the rank is two, giving the claimed Jacobian rank. As additional checks the quartic discriminant and both polynomial identities over \(\mathbb Q(i)\) were verified exactly, as was the rational square class of \(|f(Q)|/B_r\) for every odd \(r\) from 3 through 101 by the chord law.

For any positive odd squarefree \(d\), let \(s(d)\) be the number of distinct prime ideals of \(\mathbb Z[i]\) above the divisors of \(d\). The same descent on \(G_d\) has image dimensions at most \(2+s(d)\), giving
\[
\operatorname{rank}\operatorname{Jac}(C_d)(\mathbb Q)\le3+2s(d).
\]
If \(C_d(\mathbb Q)\ne\varnothing\), its rank is an odd integer between 3 and this upper bound, since the free part of \(G_d(K)\) has even integral rank under multiplication by \(i\).
