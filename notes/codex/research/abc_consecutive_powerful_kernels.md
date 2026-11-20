# Consecutive powerful integers and the coefficients of Pell units

A positive integer is powerful if every prime dividing it occurs at least twice. Write \(\operatorname{sf}(t)\) for the squarefree positive integer \(d\) such that \(t/d\) is a square. Among three consecutive positive integers with center \(n\ge2\), at least one fails to be powerful whenever all three squarefree parts are at most **500**. The calculation below covers every integer height. There is also a restriction on any hypothetical larger examples in terms of three fundamental Pell units.

Put \(H=\log n\), \(L=\log(2+H)\), and \(d_i=\operatorname{sf}(n+i)\) for \(i=-1,0,1\). If all three integers are powerful, write \(n+i=d_i^3z_i^2\). This representation is possible and unique because all odd positive prime valuations are at least 3. The \(d_i\) are pairwise coprime, since a common prime cube would divide a difference of 1 or 2. Two cannot both equal 1, since two distinct positive squares differ by at least 3. Put \(D_e=d_i d_j>1\) for each pair \(e=\{i,j\}\). In the order \(\mathbb Z[\sqrt{D_e}]\), write the least positive Pell solution as \(\varepsilon_e=x_e+y_e\sqrt{D_e}>1\), of norm one with \(x_e,y_e>0\). Set \(g_e=\gcd(D_e,y_e)\). For **every** two different pairs \(e,f\),

\[
 g_e g_f \gg H/L^7.
\tag{1}
\]

In particular at least two of the three gcds are \(\gg \sqrt H/L^{7/2}\). The product \(D=d_{-1}d_0d_1\) also satisfies \(D\gg H^{3/2}/L^{9/2}\). In a putative infinite sequence, \((1,n^2-1,n^2)\) would have radical at most \(\sqrt{(n-1)n(n+1)/D}\), since \(\operatorname{rad}(d_i^3z_i^2)\le d_i z_i\). In fact every such run would give quality strictly greater than \(4/3\), because its radical is less than \(n^{3/2}\). The existence of even one such run is the Erdős–Mollin–Walsh problem. For comparison, Mian and Siddique report a Lean verification for all centers below a height cutoff of \(10^{14}\). [Erdős Problem 364](https://www.erdosproblems.com/364) · [Mian and Siddique, abstract](https://arxiv.org/abs/2609.25011)

## Comparing the three positive units

Let \(i<j\), \(\Delta=j-i\), and put

\[
 U_e=\frac{(\sqrt{n+i}+\sqrt{n+j})^2}{\Delta}
     =\varepsilon_e^{m_e},\qquad R_e=\log\varepsilon_e.
\]

For the adjacent pairs the rational part is \(2n-1\) or \(2n+1\) and the radical part is \(2\sqrt{(n+i)(n+j)}\). For the outer pair the expression is \(n+\sqrt{n^2-1}\). These units have norm one and integer coefficients in the displayed orders. In each, the coefficient of \(\sqrt{D_e}\) is divisible by \(D_e\). For any positive Pell unit \(x+y\sqrt{D_e}\), the corresponding coefficient in its \(m\)-th power is congruent to \(m x^{m-1}y\bmod D_e\). Since \(x_e\) is coprime to \(D_e\), the positive exponent \(m_e\) is a multiple of \(D_e/g_e\). Also \(m_eR_e=H+O(1)\), giving

\[
 R_e D_e \ll (1+H)g_e.
\tag{2}
\]

For different pairs, the two positive quantities \(\Delta_e U_e\), \(\Delta_f U_f\) are strictly ordered and differ by \(O(1)\). Indeed the three sums of two square roots are strictly ordered, of size \(\asymp\sqrt n\), and their pairwise differences are \(O(n^{-1/2})\). Thus the absolute value of the nonzero linear form \(m_e\log\varepsilon_e-m_f\log\varepsilon_f+\log(\Delta_e/\Delta_f)\) is \(O(1/n)\). Use the Baker–Wüstholz bound in their common real field of degree at most four. It uses either two logarithms or three with the additional constant \(\log2\). The modified heights are \(O(R_e),O(R_f)\), and the exponents are \(O(1+H)\). It follows, with absolute constants and for sufficiently large \(n\), that

\[
 R_e R_f\gg H/L.
\tag{3}
\]

The real quadratic class number formula and \(L(1,\chi_\Delta)\ll\log(2|\Delta|)\) give \(R_e\ll\sqrt{D_e}\log(2D_e)\). In detail the maximal order has discriminant at most \(4D_e\) and positive class number. When the integer order has index two, the maximal order modulo 2 is either \(\mathbb F_4\) or \(\mathbb F_2\times\mathbb F_2\), so the sixth power of a fundamental unit is an integer-order unit of norm one. These facts bound the ratio between the two regulators by 6. Combining the squared regulator estimate with (2) gives \(R_e^3\ll H g_e\log^2(2D_e)\) for \(n\ge3\). If either gcd in (1) exceeds \(H\), (1) follows. Otherwise (2) and \(R_e,R_f>1\) give \(D_e,D_f\ll H^2\). Multiplying the two cubic estimates and using (3) proves (1).

For the bound on \(D\), take the two pairs meeting at the smallest \(d_i\). Their regulators have product \(\ll\sqrt{D d_i}\log^2(2D)\le D^{2/3}\log^2(2D)\). Equation (3) gives the assertion, on first disposing of \(D>H^2\). [Baker and Wüstholz](https://doi.org/10.1515/crll.1993.442.19) · [Verification of constants and height conventions](../../claude/reference-audit.md)

## An all-heights calculation for the squarefree parts up to 500

The verifier uses integer arithmetic and outward enclosures of real logarithms. It first enumerates the kernel triples and intersects the possible residue sets of \(n+i=d_i^3 z_i^2\) modulo \(512,81,25,49,121,169\) and the primes from 17 through 500. This leaves 21,953 triples. For each put \(u=\varepsilon_{-1,0}\), \(v=\varepsilon_{0,1}\). The Pell continued fraction gives their integer coefficients. The verifier checks that \(2x<2^{10000}\) for each unit \(x+y\sqrt d\) used. The largest observed bit length of \(2x\) is 1,610. In particular \(1<\log u,\log v<10000\).

If the two adjacent pairs are realized at the same \(n\), their powers \(u^m,v^l\) have rational parts \(2n-1,2n+1\). Therefore

\[
 0< l\log v-m\log u
 =\operatorname{arcosh}(2n+1)-\operatorname{arcosh}(2n-1)\le2/n,
\]

by integrating \(1/\sqrt{t^2-1}\). The two-logarithm Baker–Wüstholz bound gives \(H\le\log 2+7\cdot10^{11}(\log u)(\log v)\log\max(e,m,l)\). The stated constant bounds \(18\cdot 3!\cdot2^3\cdot128^4\log16\) in degree at most four. Both exponents are at most \(H+\log5\). For \(H\ge10^{25}\) the resulting inequality is impossible, by monotonicity of \(H/\log(H+2)\). In particular \(m,l<M=10^{30}\).

The verifier then encloses \(t=\log u/\log v\) between two rational numbers and uses the continued fraction of their midpoint to find coprime \(p,q\) with \(q>2M\) and \(2M|qt-p|<1\), checking the inequality at both interval endpoints. Since \(m<M<q\), \(mp-lq\) is a nonzero integer. Thus \(q|mt-l|>1/2\), which implies \(n<4q\) by the preceding archimedean upper bound and \(\log v>1\). A direct recurrence for the rational part of \(u^m\) now recovers every possible \(n\). At each odd rational part \(X\), it tests whether \(n=(X+1)/2\) has all three required square co-factors. The largest bound \(4q\) was 499861463004769142165334647918725220. Testing 55,796 recurrence terms gave zero hits. Python's decimal square root and natural logarithm are correctly rounded to nearest. The verifier widens every interval endpoint one adjacent representable number at each rounded operation, then checks the convergents with exact fractions. [Verifier](abc_consecutive_powerful_kernels.py) · [Python decimal arithmetic](https://docs.python.org/3/library/decimal.html)

## An exact criterion for the saving from two consecutive powerful integers

For squarefree \(d>1\), write \(x+y\sqrt d=\varepsilon_d\) for the least positive integral Pell unit of norm one and put \(k_d=d/\gcd(d,y)\). The following conditions are equivalent.

1. There are unbounded consecutive powerful pairs \(N,N+1\) with \(d=\operatorname{sf}(N)\operatorname{sf}(N+1)\ge N^\eta\) for one fixed \(\eta>0\).
2. Infinitely many squarefree \(d\) satisfy \(k_d\le K\) and \(\varepsilon_d\le d^C\) for fixed constants \(K,C\).

For the forward direction, \(2N+1+2\sqrt{N(N+1)}=\varepsilon_d^m\) with \(k_d\mid m\) as above. The unit exceeds \(\sqrt d\), so \(m\le 2\log(4N+2)/\log d=O_\eta(1)\). The same identity bounds \(\varepsilon_d\) by a fixed power of \(d\). Conversely \(\varepsilon_d^{k_d}=X+Y\sqrt d\) has \(d\mid Y\). The consecutive integers \(N=dY^2\) and \(N+1=X^2\) are powerful and \(N+1\le d^{2CK}\). Their squarefree parts are \(d,1\). Such an infinite family would disprove rational abc since \(\operatorname{rad}(N(N+1))\le \sqrt{N(N+1)/d}\). This characterizes the saving certified by the two squarefree parts. Other repeated prime factors can affect the actual radical. The earlier square-ending construction already described the forward implication from special fundamental units to an abc counterexample and the elementary congruence on their powers. [Earlier unit calculation](abc_quadratic_units.md)
