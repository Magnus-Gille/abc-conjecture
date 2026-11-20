# A quadratic unit gives an explicit 1,529,207-digit abc example

Andreas Reinhart reported a counterexample to the Ankeny–Artin–Chowla conjecture on fundamental units of real quadratic fields. Hang Liu's 2026 abstract describes another application to Legendre-symbol determinants. A separate 2026 paper by Wouter van Doorn reports progressions of three powerful numbers with difference \(2\sqrt N+1\), suggesting a related norm-two search. These bibliographic claims were checked against the authors' abstracts in an arXiv metadata snapshot. Direct download of the van Doorn PDF returned HTTP 403. The numerical claims and implications for abc below were checked independently. [Reinhart](https://arxiv.org/abs/2410.21864) · [Liu](https://arxiv.org/abs/2609.23684) · [van Doorn](https://arxiv.org/abs/2605.06697)

## An exact example and what its powers give

Put \(p=331914313984493\), \(w=(1+\sqrt p)/2\). Write the positive fundamental unit returned by PARI as \(U=a+bw\) and put \(x=2a+b\). Exact checks give \(N(U)=-1\), \(b>0\) odd, \(x>0\), and \(p\mid b\). Consequently
\[
 4+x^2=p b^2=c
\]
is a primitive positive triple. Its radical \(R=\operatorname{rad}(4x^2p b^2)\) is at most \(2xb\). Thus \(c/R\ge pb/(2x)>\sqrt p/2>9\,109\,257\). The full height has 1,529,207 decimal digits and satisfies
\[
 c> R^{219730/219729}.
\]
Indeed the exact integer comparison \(p^{219730}>4^{219730}c^2\) gives \(\sqrt p/2>c^{1/219730}\). These bounds do not require factoring \(x\) or \(b\). The following PARI/GP commands reproduce the checks without printing their million-digit values.

~~~gp
default(parisize,128000000);
p=331914313984493; U=quadunit(p); w=quadgen(p);
a=component(U,2); b=component(U,3); x=2*a+b; c=p*b^2; K=219730;
[isprime(p), p%8==5, w^2-w+(1-p)/4==0, U==a+b*w, norm(U)==-1]
[x>0, b>0, b%p==0, b%2==1, gcd(4,x^2)==1, x^2+4==c]
[10^1529206<=c && c<10^1529207, p^K>4^K*c^2, p>4*9109257^2]
~~~

Every entry is one. For the construction, any \(U\) satisfying the checked algebraic identities and signs suffices.

Now take \(n=p^j\), \(j\ge0\), and write \(U^n=a_n+b_n w\), \(x_n=2a_n+b_n\). Its norm is still \(-1\). Since \(p\equiv5\bmod8\), reduction modulo 2 gives the field with four elements. The image of \(U\) is a nontrivial unit since \(b\) is odd. As \(3\nmid p^j\), its \(n\)-th power is still nontrivial, and \(b_n,x_n\) are odd. The triples \(4+x_n^2=c_n=p b_n^2\) are therefore primitive.

In fact \(v_p(b_{p^j})=v_p(b)+j\). If \(A=U^n,\ B=\bar U^n\), then \(A-B=b_n\sqrt p\). When \(p\mid b_n\), the integer \((A^p-B^p)/(A-B)\) is congruent to \(p B^{p-1}\) modulo \(p^2\) in the ring of integers. This follows by expanding \((B+(A-B))^p\) and using \(A-B\in p\mathcal O\), with \(p\) odd. As \(B\) is a unit, this integer is divisible by \(p\) exactly once. Since it is \(b_{pn}/b_n\), induction proves the formula.

Retaining just this known repetition in the radical gives
\[
 \frac{c_n}{\operatorname{rad}(4x_n^2c_n)}
 >\frac{\sqrt p}{2}\,p^{v_p(b_n)-1}\ \ge\ \frac{\sqrt p}{2}\,p^j.
\]
Also \(\log c_n=2p^j\log U+o(1)\), by \(b_n\sqrt p=U^n+U^{-n}\). The particular factor proved here grows on the scale of \(\log c_n\). Other primes could make the actual ratio larger. This argument gives no fixed positive power of \(c_n\) for infinitely many \(j\).

## What an infinite family of fields would have to supply

For squarefree \(D>1\) and positive integers \(x,y\) satisfying \(x^2-Dy^2=\pm1\), reorder \(1,x^2,Dy^2\) into a primitive sum and let \(C\) be the largest term. Put \(g=\gcd(D,y)\). Its radical is at most \(Dxy/g\); for both signs this gives \(C/\operatorname{rad}(Dxy)>g/\sqrt D\). In particular, if infinitely many distinct primes \(p\) admit such a solution with \(p\mid y\) and \(x\le p^L\) for some fixed \(L\), then \(C/\operatorname{rad}(pxy)>\sqrt p\) and \(C\le 2p^{2L}\). That would disprove rational abc. As \(p\) varies, knowing only that \(p\mid y\) gives no such size control.

For an odd prime \(p\equiv1\bmod4\), this condition would follow from a fundamental unit \(U=a+bw>1\) with \(p\mid b\) and \(\log U\le L_0\log p\), if it held for infinitely many \(p\) with fixed \(L_0\). The unit \(U^6\) has norm one and is \(1\) modulo \(2\mathcal O\), since \(\mathcal O/2\mathcal O\) is either the field with four elements or the product of two fields with two elements. Thus \(U^6=x+y\sqrt p\) with integral \(x,y\), \(x\le U^6\). Reduction modulo \(p\mathcal O\) in the basis \(1,w\) shows that \(p\mid 2y\), hence \(p\mid y\). Reinhart's single prime supplies no infinitude or uniform height estimate.

Taking powers of a small unit usually cannot enforce the missing condition cheaply. For the integer-coefficient order \(\mathbb Z[\sqrt D]\), let \(V=x_1+y_1\sqrt D>1\) be its least positive unit greater than one in the real embedding, of either norm. For \(V^m=x_m+y_m\sqrt D\) one has \(y_m\equiv m x_1^{m-1}y_1\bmod D\) by expansion, and \(\gcd(x_1,D)=1\). Since \(D\) is squarefree, \(\gcd(D,y_m)\le m\gcd(D,y_1)\). If \(x_m\le D^L\), then \(m\) is bounded in terms of \(L\), since \(V>\sqrt D\) and \(V^m\le 2x_m+1\). This distinguishes an exceptional base unit from divisibility forced by taking a high power.

As a finite test, continued fractions checked all odd primes \(p\le10^6\) and positive solutions \(x\le p^{10}\) of \(x^2-py^2\in\{-1,1,2\}\) with \(p\mid y\). The six hits are

| \(p\) | Norm | \(x\) | \(y\) |
|---:|---:|---:|---:|
| 3 | 1 | 26 | 15 |
| 3 | 1 | 1351 | 780 |
| 5 | −1 | 682 | 305 |
| 5 | 1 | 930249 | 416020 |
| 7 | 2 | 11427 | 4319 |
| 7 | 1 | 130576328 | 49353213 |

For \(p\ge5\), a positive solution in these three norms satisfies
\(\lvert x/y-\sqrt p\rvert=\lvert x^2-py^2\rvert/(y^2(x/y+\sqrt p))<1/(2y^2)\): for norm \(2\) use \(x/y>\sqrt p\), and norm \(\pm1\) has numerator one. The fraction is reduced. Legendre's criterion therefore puts it among the convergents of \(\sqrt p\). For \(p=3\), norm \(2\) is impossible modulo 3 and the same argument covers the other norms. The following snippet uses exact integer arithmetic.

~~~python
from math import isqrt
from sympy import primerange

for p in primerange(3, 1000001):
    root = isqrt(p)
    offset, divisor, term = 0, 1, root
    prev_x, x, prev_y, y = 0, 1, 1, 0
    while True:
        prev_x, x = x, term*x + prev_x
        prev_y, y = y, term*y + prev_y
        if x > p**10:
            break
        if y % p == 0 and x*x - p*y*y in (-1, 1, 2):
            print(p, x*x - p*y*y, x, y)
        offset = divisor*term - offset
        divisor = (p-offset**2)//divisor
        term = (root+offset)//divisor
~~~

Composite squarefree \(D\) can give larger shared factors with small units. For example, \(D=58254=2\cdot3\cdot7\cdot19\cdot73\),
\[
 x=322922845377070074305,\qquad y=1337937710702315016
\]
give \(x^2-Dy^2=1\) and \(D\mid y\). This is another finite input.

There is an elementary obstruction to constructing such examples by a fixed polynomial identity. Suppose \(X^2-HY^2=k\) in \(\mathbb Z[t]\), with \(k\) a nonzero constant, \(Y\ne0\) and \(H\) nonconstant and squarefree as a polynomial. Let \(G=\gcd(H,Y)\) over \(\mathbb Q[t]\). Differentiation gives \(2XX'=Y(H'Y+2HY')\). The right side is divisible by \(YG\), and \(\gcd(X,YG)=1\), so \(YG\mid X'\). Since \(2\deg X=\deg H+2\deg Y\), we obtain
\[
 \deg G\le \tfrac12\deg H-1.
\]
Taking \(G\) primitive integral, a Bézout identity for \(H/G,Y/G\) after clearing denominators bounds \(\gcd(H(t),Y(t))\ll |G(t)|\) at all sufficiently large integer \(t\). Hence \(\gcd(H(t),Y(t))/\sqrt{|H(t)|}=O(1/|t|)\). At specializations where \(H(t)\) is positive and squarefree, the common factor in this construction is too small even to exceed \(\sqrt{H(t)}\). This leaves nonpolynomial families and integer specializations where one first removes a varying square factor from \(H(t)\).
