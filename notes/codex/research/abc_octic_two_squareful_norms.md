# Infinitely many simultaneous squareful norms, with higher multiplicity at small primes

Write \(U_\pm=(s\pm t)^2+t^2,\ H=\max(s,t)\), for positive coprime \(s,t\), \(s\) odd and \(t\) even. Both norms can be squareful simultaneously at arbitrarily large heights. More precisely, fix an integer \(k\ge3\) and a real \(0<\theta<1/2\). There are \(c_k'>0\) (also depending on \(\theta\) and the chosen seed) and infinitely many such pairs with all three properties

* Every prime dividing either norm occurs to exponent at least two.
* Every such prime at most \(c_k'\log\log H\) occurs to exponent at least \(k\).
* \(\operatorname{rad}(|st(s^8-16t^8)|)\ll H^8/(\log H)^\theta\).

With no growing cutoff, the logarithmic exponent in the last bound can be \(1/2\). Thus even eventually requiring cubefulness at each individual prime is compatible with an infinite squareful family. Requiring cubefulness at all primes of one norm at the same parameter value is still open here. [Upper bound and search for that condition](abc_octic_powerful_count.md)

## The elliptic curve and the seed

Start from any admissible \((s_0,t_0)\), put \(x_0=s_0/t_0\), and let \(d=\operatorname{sf}(s_0^4+4t_0^4)>0\), the squarefree part. The smooth genus-one curve \(C_d:d y^2=x^4+4\) has a rational point \(P\) above \(x_0\). Let \(\iota(x,y)=(x,-y)\), and let \(T=[P-\iota P]\) be a rational point of the Jacobian. Put \(M=\operatorname{rad}(U_+(s_0,t_0)U_-(s_0,t_0))>1\). Every prime of \(M\) is \(1\bmod4\) and at least five, since both seed norms are odd primitive sums of two squares.

After adjoining \(\sqrt d\), the curve identifies with \(C_1\), which is birational to \(E:V^2=X^3-X\) by \(X=(y+x^2)/2,\ V=xX\) on \(C_1\). This extends to an isomorphism of smooth projective curves. The elliptic curve has good reduction at all primes \(p\ge5\). For \(p\mid M\) the reduction of the untwisted \(P\) is a branch point of the double cover: \(p\nmid t_0\), the four roots of \(x^4+4\) remain distinct modulo \(p\), and its value vanishes. Therefore the nonzero difference \(T\) belongs to the kernel of reduction over a local extension of degree at most two. The formal logarithm is injective and preserves the valuation of a formal parameter in this kernel since the ramification index is at most two, less than \(p-1\). Thus \(T\) has infinite order.

For odd \(m\ge1\), let \(P_m=P+[(m-1)/2]T\), a rational point of \(C_d\). At any branch point \(W\) of the cover over the algebraic closure, the involution \(\iota\) is negation with \(W\) as origin. Consequently, in the group with that origin, \(P_m-W=[m](P-W)\). By the quadratic height law and comparison with the height of the nonconstant map \(x\), the reduced slope \(x(P_m)\) has \(\log H_m\asymp m^2\) as \(m\to\infty\). Here \(H_m\) is the maximum of the absolute values of its primitive integer coordinates. The finitely many occurrences of zero or infinity can be discarded.

## Parity at 2

The seed satisfies \(d\equiv1\bmod8\), since \(s_0^4+4t_0^4\equiv1\bmod8\) and its square part is odd. Thus \(d\) is a square in \(\mathbb Q_2\), so locally its Jacobian is isomorphic to \(E\). The group \(E(\mathbb Q_2)\) has only 2-groups as finite continuous quotients. For an explicit check, the displayed Weierstrass equation is minimal (its discriminant has valuation 6). The quotient of the nonsingular-reduction subgroup by the formal subgroup has order two: the nonsingular points of the reduced cubic are the origin and \((0,0)\). The formal subgroup is pro-2. A point with singular reduction has odd \(X\) and even \(V\); unless it is already 2-torsion, choose \(a=1\) or \(-1\) with \(v_2(X-a)=1\). Translating by \((a,0)\) gives \(X'=a+2/(X-a)\), which is even and hence nonsingular. This proves the finite-quotient assertion.

The parity \(s\) odd, \(t\) even is an open condition on a primitive slope near the seed over \(\mathbb Q_2\). Thus for some power of two \(N\), translation by \(N T\) and all its multiples stays in this neighborhood when starting at \(P\). Every odd \(m\equiv1\bmod 2N\) preserves the required parity. Negative slopes can be made positive by taking absolute values, which at most swaps \(U_+\) and \(U_-\).

## Deepening the valuations

At \(p\mid M\) choose the branch \(W\) with the same reduction as the seed. Its slope lies in \(\mathbb Q_p\), as \(p\equiv1\bmod4\). A formal parameter at the branch has positive valuation at \(P\); its square equals the distance in the \(x\)-coordinate up to a unit. Since multiplication by \(m\) adds \(v_p(m)\) to the valuation of the formal logarithm, the seed norm meeting the branch acquires exactly \(2v_p(m)\) additional factors of \(p\) at \(P_m\). The denominator of that slope is a \(p\)-adic unit. Thus for \(m\) divisible by \(M\) each such valuation reaches at least three. At every \(p\notin M\), \(p\) odd, the identity \(U_+U_-=d\cdot\text{square}\) on \(C_d\) forces even valuations because the two norms are coprime at odd primes. Together with parity at 2 this proves simultaneous squarefulness.

For a direct numerical check take \((s_0,t_0)=(1,2)\), \(M=d=65\), \(m=65\). On \(E\) the seed has coordinates \(((1+\sqrt{65})/8,(1+\sqrt{65})/16)\). The involution is \(P\mapsto(0,0)-P\), so \(P_{65}\) corresponds to \([65]P\) because \((65-1)/2\) is even. Exact doubling six times and adding the seed gives a positive reduced \(s/t\) with 1,963 decimal digits in each coordinate. The two integer square-root checks give \(U_+/13\) and \(U_-/5\) both squares, with \(v_{13}(U_+)=v_5(U_-)=3\). These tests certify squarefulness without factoring the large norms.

Now fix \(Y_0\ge5\) and a prime \(p\le Y_0,\ p\equiv1\bmod4\). If \(p\) divides a norm of the output, its slope meets some branch \(W\) modulo a place of \(\mathbb Q_p(\sqrt d)\). Let \(r\) be the order of the reduction of \(P-W\) on the good elliptic curve there. Then \(r\mid m\). The residue degree is at most two, and Hasse's bound gives \(r\le(p+1)^2<p^3\), hence \(v_p(r)\le2\). The point \([r](P-W)\) is nonzero and in the formal subgroup. Multiplication by \(m/r\) there adds at least \(v_p(m)-2\) to its parameter valuation, so if \(v_p(m)\ge k+2\), the output norm has valuation at least \(k\). This reasoning covers every prime up to \(Y_0\) that can occur in either output norm.

Choose a fixed large \(A>0\), put \(J=\lceil A Y_0\rceil\), and set
\[
 m_0=M^J\prod_{\substack{p\le Y_0\\p\equiv1\bmod4}}p^{\,k+2},
 \qquad m=m_0^{\,\varphi(2N)} .
\]
This gives \(m\equiv1\bmod2N\). Chebyshev's estimate \(\sum_{p\le Y_0}\log p\ll Y_0\) gives \(\log m\ll Y_0\), hence \(Y_0\gg\log\log H_m\). Increase \(A\), depending on the fixed \(\theta\), to have \(M^{J\varphi(2N)}\ge m^{2\theta}\). The exact growth at the seed primes and even valuations everywhere else give
\[
 \operatorname{rad}(U_+U_-)
 \ \le\ M\left(\frac{U_+U_-}{\prod_{p\mid M}p^{v_p(U_+U_-)}}\right)^{1/2}
 \ \ll\ H_m^2 M^{-J\varphi(2N)}
 \ \ll\ H_m^2/(\log H_m)^\theta .
\]
Multiplying by the radicals of \(s,t,s^2-2t^2,s^2+2t^2\), whose product is \(O(H_m^6)\), proves the claimed radical estimate. If only squarefulness is required, take \(m=M^{j\varphi(2N)}\); all its factors then contribute at seed primes and the same calculation gives \(H_m^8/\sqrt{\log H_m}\).
