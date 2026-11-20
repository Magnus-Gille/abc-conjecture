# The three quartic triples and their Frey curves

For coprime \(x>y>0\) of opposite parity, let \(d=x^2-y^2,\ t=2xy,\ s=x^2+y^2\) and \(l=x-y,\ h=x+y\). The triples of heights \(x^4,s^2,h^4\) in the [quartic construction](abc_three_radicals.md) have the same radical \(R=\operatorname{rad}(xy d s)\). Their Frey curves may be written
\[
 E_A:\ Y^2=X(X+y^4)(X+x^4),\quad
 E_B:\ Y^2=X(X-d^2)(X-s^2),\quad
 E_C:\ Y^2=X(X-l^4)(X-h^4).
\]
Both outer curves are rational 2-isogenous to \(E_B\). Indeed the quotient of \(Y^2=X(X^2+AX+B)\) by \((0,0)\) has nonzero roots \(A\pm2\sqrt B\) when \(B\) is a square. On \(E_B\) quotienting at its first root 0 gives roots \(-(s-d)^2,-(s+d)^2\), which are \(-4y^4,-4x^4\); scaling coordinates by \(4,8\) gives \(E_A\). Translating \(s^2\) to zero and using \(s^2-d^2=t^2\) gives the second quotient roots \((s-t)^2=l^4,(s+t)^2=h^4\), giving \(E_C\). In particular the three curves have the same conductor and isomorphic Tate modules at every odd prime. This explains the dependence between their odd-prime modular constraints.

## An elementary restriction to three squares

For every fixed \(\eta>0\), abc is equivalent to its restriction to the quartic construction with \(x-y,x,x+y\) all squares and the squarefree part of \(y\) at most \(x^\eta\). Here squarefree part means the unique squarefree integer in the positive integer's square class. To see this, begin with the transfer in the linked note, which turns any fixed-power abc failure into infinitely many pairs with \(x^4/R\ge x^\gamma\) for some fixed \(\gamma>0\).

Write \(A=xy(x^2-y^2), W=x^2+y^2\), and \(D=x^4-6x^2y^2+y^4\). Make the substitution \(X=W^2,\ Y=4A\). The new pair is primitive and of opposite parity because \(W\) is odd and coprime to \(A\). The identities
\[
 X+Y=(x^2+2xy-y^2)^2,\qquad X-Y=(x^2-2xy-y^2)^2
\]
give three squares \(X-Y,X,X+Y\), with \(0<Y<X\). The second square cannot vanish at a rational ratio \(x/y\). Furthermore
\[
 A(X,Y)=A(2WD)^2,\qquad W(X,Y)=W^4+16A^2.
\]
Hence the square class of \(A\) is conserved, and the new common radical is at most \(R\,|D|\,W(X,Y)\ll R x^{12}\). Since \(x^4\le X\le 4x^4\), the ratio of the smallest quartic height to the radical satisfies \(X^4/R_{\rm new}\gg x^4/R\). Every fixed number \(j\) of iterations preserves a positive-power failure, with a smaller exponent. The squarefree part of the final \(Y\) equals the squarefree part of the original \(A\), which is at most \(x^4\le X_{\rm final}^{4/4^j}\). Choose \(j\) large enough for the stated \(\eta\).

This restriction is sparse. There are \(O(T^{2/4^j})\) image pairs with \(X_{\rm final}\le T\), since the original \(x\) was at most \(T^{1/4^j}\). The correspondence leaves open whether any of these pairs exhibit a fixed-power failure at arbitrarily large heights.
