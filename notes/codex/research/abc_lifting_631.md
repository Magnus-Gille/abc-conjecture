# Lifting the 276-digit abc example

Use the coprime bases

~~~text
x = 188501707118483312662842033434214073534
y = 14106104618039134064040525112584509829903089804413987905
~~~

Put \(p=631,\ m_j=5p^j,\ C_j=y^{m_j},\ A_j=y^{m_j}-x^{m_j}\), and \(R_j=\operatorname{rad}(xy A_j)\). Then \(A_j+x^{m_j}=C_j\) is a primitive positive triple for every \(j\ge0\). The earlier finite certificate at \(j=0\) gives \(C_0>R_0^{1.01}\). [Numerical certificate](abc_joint_exponents.md)

## What the two known primes give at every height

Direct modular exponentiation gives \(v_p(y^5-x^5)=35\). The lifting-the-exponent formula therefore gives \(v_p(A_j)=35+j\). Also \(31^2\mid x\). Removing these known repetitions from \(xyA_j\) gives
\[
\frac{C_j}{R_j}\ \ge\
\frac{31p^{34+j}}{xy(1-(x/y)^{m_j})}
\ >\ K\log C_j,\qquad
K=\frac{31p^{34}}{5xy\log y}\approx 2.916829.
\]
The contribution explicitly shown, divided by \(\log C_j\), tends to \(K\). This gives infinitely many primitive triples with \(C_j/R_j>2.9\log C_j\). The numerical constant can also be certified by \(31p^{34}>1851xy\) and \(\log y<127\), the latter following by summing the first 181 terms of the exponential series at 127.

## What must happen at other primes

The complete prime factorizations of the two bases are
\[
\begin{aligned}
x&=2\cdot31^2\cdot1201\cdot2507448001\cdot32567690445263105263247,\\
y&=3\cdot5\cdot928053337\cdot1013311344341346052329355513653666210199948871 .
\end{aligned}
\]
The complete factorization of the original difference is
\[
A_0=631^{35}\,(11)(8307557244653)(10864612987094129)(14207799247875353644718653)
\,(21701)(56401)(48436313491)(13136166780592451)(4730638290164139976801)
\,(107219752254397244551864336100112594130900461678656905978204080241).
\]
The first four parenthesized primes multiply to \(y-x\). The remaining six multiply to \((y^5-x^5)/((y-x)631^{35})\). PARI's integer primality test and multiplication verified all three factorizations. Hence \(\operatorname{rad}(xy)=xy/31\), the only repeated prime of \(A_0\) is 631, and the exact quality \(\log C_0/\log R_0\) is approximately 1.011992237006627.

For **all** indices \(j\), 631 is the only prime \(q\le10^{10}\) for which \(q^2\mid A_j\). A prime dividing \(A_0\) other than 631 keeps its initial valuation by the lifting formula. A new prime must be 1 modulo 631, since its multiplicative order modulo \(q\) divides \(5\cdot631^j\) and does not divide 5. For any such prime, set \(d=5\cdot631^{v_{631}(q-1)}\). The order of \(y/x\) modulo \(q^2\) divides \(q(q-1)\). As \(q\nmid5\cdot631\), divisibility \(q^2\mid A_j\) for some \(j\) is equivalent to \(y^d\equiv x^d\bmod q^2\). The same test modulo \(q\) detects ordinary divisibility. Primes dividing a base never divide \(A_j\).

A sieve enumerated the 722,563 primes congruent to 1 modulo 631 through \(10^{10}\). Six new primes divide some \(A_j\). They are 2,025,511 and 1,055,139,271 at the first lift, and 1,007,347,331, 1,867,375,091, 4,447,458,371 and 8,807,321,321 at the second. Each has valuation one wherever it occurs. The residue tests cover every subsequent lift, independent of height. [Reproducible sieve](abc_631_prime_check.py)

Consequently the radical along the family satisfies the exact identity
\[
\frac{C_j}{R_j}
=\frac{31p^{34+j}}{xy(1-(x/y)^{m_j})}
\prod_{\substack{q>10^{10}\\ q^2\mid A_j}}q^{v_q(A_j)-1}.
\tag{1}
\]
Each prime in the product satisfies \(q^2\mid y^{q-1}-x^{q-1}\). Indeed its multiplicative order modulo \(q^2\) divides both \(m_j\) and \(q(q-1)\), and \(q\nmid m_j\).

More precisely, fix \(\eta>0\), and choose a fixed integer \(k\ge1\) with \(p^{-k}<\eta/4\). If \(C_j/R_j\ge C_j^\eta\) for arbitrarily large \(j\), then on those indices, once \(j\) is sufficiently large, repeats from primes in (1) satisfying
\[
q\equiv1\pmod {631^{\,j-k+1}},\qquad q\nmid A_{j-k}
\]
must have product \(\prod q^{v_q(A_j)-1}\ge C_j^{\eta/2}\). In fact a prime \(q>10^{10}\) dividing \(A_{j-k}\) has exactly the same valuation in \(A_j\) by lifting, since \(q\nmid631\). The product of all those inherited repetitions is at most \(A_{j-k}< C_j^{p^{-k}}\). The explicit prefactor in (1) is \(O(\log C_j)\). Finally any prime \(q\) dividing \(A_j\) but not \(A_{j-k}\) has order modulo \(q\) dividing \(5p^j\) but not \(5p^{j-k}\). Its order is therefore divisible by \(p^{j-k+1}\) and divides \(q-1\). This supplies the stated necessary condition. I have no estimate establishing or excluding such a product on infinitely many indices.

## An equivalent question about one factor per lift

Define \(B_i=A_i/(631 A_{i-1})\) for \(i\ge1\). This is an integer prime to \(631A_{i-1}\). Indeed \(A_i/A_{i-1}=(U^{631}-V^{631})/(U-V)\) with \(U=y^{m_{i-1}},\ V=x^{m_{i-1}}\). Modulo a prime divisor of \(U-V\), the quotient is \(631V^{630}\). The only possible common prime is 631 and lifting gives exactly one copy in the quotient. The \(B_i\) are thus pairwise coprime. Put
\[
t_i=\frac{\log(B_i/\operatorname{rad}(B_i))}{\log C_i},
\qquad
s_j=\frac{\log(C_j/R_j)}{\log C_j}.
\]
Since \(0\le t_i\le1\) and \(\log C_i/\log C_j=631^{i-j}\), (1) gives
\[
s_j=\sum_{i=1}^j 631^{i-j}t_i+O((j+1)/631^j).
\]
The initial fixed terms in this sum decay geometrically. Summing the resulting bounds for its tail gives
\[
\limsup t_i\ \le\ \limsup s_j\ \le\ \tfrac{631}{630}\limsup t_i.
\]
Consequently this particular sequence disproves abc if and only if \(\limsup t_i>0\). Equivalently, one needs a single new factor \(B_i\) with repeated-prime contribution at least \(C_i^\eta\) at infinitely many indices for a fixed \(\eta>0\). Every prime of \(B_i\) is 1 modulo \(631^i\) by its order, and every repeated prime of \(B_i\) additionally exceeds \(10^{10}\) by the sieve.

The squarefree part of every \(B_i\) has a prime divisor \(q\equiv3\pmod4\) of size at least \(1+631^i\). Indeed \(V=x^{m_{i-1}}\) is a multiple of eight and \(U\) is odd. Therefore \(631B_i\equiv U^{630}\equiv1\pmod8\), giving \(B_i\equiv7\pmod8\). At least one prime \(q\equiv3\pmod4\) occurs to an odd exponent and every prime of \(B_i\) is 1 modulo \(631^i\). Distinct indices give distinct primes by coprimality. This places an unconditional lower bound on the squarefree part, of logarithmic size in \(C_i\).

## Allowing both bases and the exponent to vary

There is a general obstruction to extending a certificate using only a fixed finite set of primes. Take arbitrary coprime \(1\le x<y\), \(m\ge2\), and put \(U_m=xy(y^m-x^m)\), \(C=y^m\). For a fixed finite set \(S\), write \(n_S=\prod_{q\in S}q^{v_q(n)}\) and \(G_S(n)=\prod_{q\in S}q^{\max(v_q(n)-1,0)}\). The upper bound \(U_m/G_S(U_m)\) for the radical uses all the repetitions at \(S\), along with the known powers \(x^m,y^m\). For every \(\epsilon>0\) one has, uniformly in \(x,y,m\),
\[
\frac{C}{U_m/G_S(U_m)}\ \ll_{S,\epsilon}\ m y^\epsilon.
\tag{2}
\]
In particular for each \(\eta>0\) this certified ratio is \(o(C^\eta)\) as \(C\) tends to infinity. Use (2) with a smaller \(\epsilon\) and \(m\ll_\eta 2^{m\eta/4}\).

To prove (2), fix \(L\) a positive common multiple of 2 and all \(q-1\) for \(q\in S\). For \(q\nmid xy\), \(q\mid y^L-x^L\). The integer \(y^m-x^m\) divides \(y^{Lm}-x^{Lm}\). Lifting from \(L\) to \(Lm\) gives \(v_q(y^{Lm}-x^{Lm})=v_q(y^L-x^L)+v_q(m)\), also for \(q=2\) since \(L\) is even. A prime dividing \(xy\) divides neither difference. Thus \((U_m)_S\le m(U_L)_S\).

For \(h=y-x\), the two-dimensional \(S\)-adic Subspace Theorem gives \((U_L)_S\ll_{L,S,\epsilon} xh\,y^\epsilon\). To check the application, \(XY(Y^L-X^L)\) has distinct projective roots in characteristic zero. At each \(q\in S\) factor this fixed form into linear forms over \(\overline{\mathbb Q}_q\), normalized up to fixed constants. For primitive \((x,y)\) at most one factor can be smaller than a fixed positive threshold, since any two factors have nonzero determinant and \(\max(|x|_q,|y|_q)=1\). Choose the smallest factor and complete it to an independent pair with \(X\) or \(Y\). Their product of local absolute values is at most a constant times \(|U_L|_q\). At the real place use \(X,Y-X\), whose product at \((x,y)\) is \(xh\). There are only finitely many choices of local forms. For each, the Subspace Theorem permits product less than \(y^{-\epsilon}\) only on finitely many proper rational lines, each containing at most one positive primitive pair. Absorbing their values into the constant gives the estimate. Lastly \(U_m/C=xh\sum_{i=0}^{m-1}(x/y)^i\ge xh\). Use \(G_S(U_m)\le (U_m)_S\) to obtain (2). [Bilu, *The Many Faces of the Subspace Theorem*](https://arxiv.org/abs/0907.2098)

This restriction on a certificate still allows repeated prime factors outside \(S\). In fact for every fixed \(m\ge2\), abc on the full class \((y^m-x^m,x^m,y^m)\) is equivalent to rational abc. To see the reverse implication take any primitive \(a+b=c\), set \(x=a,\ y=c\), and factor \(c^m-a^m=b\sum_{i=0}^{m-1}c^{m-1-i}a^i\). The output radical is at most \(m c^{m-1}\operatorname{rad}(abc)\). Thus any input ratio \(c/\operatorname{rad}(abc)\ge c^\eta\) gives output ratio at least \(C^{\eta/m}/m\) with \(C=c^m\). An unbounded sequence retains a fixed positive exponent after decreasing it slightly.
