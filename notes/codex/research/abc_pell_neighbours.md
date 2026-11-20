# Which repeated factors survive a Pell transformation?

For positive coprime \(x>y\) of opposite parity, put
\[
d=x^2-2xy-y^2,\qquad
A(x,y)=xy(x-y)(x+y)(x^2+y^2)(x^2+2xy-y^2).
\]
The associated primitive fourth-power abc triple has height \(C=(x^2+y^2)^4\) and radical \(R=\operatorname{rad}(|d|A(x,y))\). All seven displayed factors are pairwise coprime in absolute value. Consider the integral map
\[
T(x,y)=(5x+2y,\,2x+y).
\]
It is unimodular, preserves the parity condition and preserves \(d\) exactly. Write \(A_k=A(T^k(x,y))\). [Fourth-power construction](abc_quadratic_maps.md) · [The preceding single-term Pell family](abc_quadratic_exceptions.md)

## An exact common-divisor formula

Let \(U_0=0,U_1=1,\ U_{j+2}=2U_{j+1}+U_j\) be the Pell numbers. For \(k\ge1\) define
\[
I_k=\{4k-2,\,4k+2,\,8k-2,\,8k,\,8k+2\}.
\]
The largest possible \(\gcd(A_0,A_k)\), as the initial admissible pair varies, is
\[
G_k=2^{1+v_2(k)}\;\operatorname{oddpart}\!\left(\operatorname{lcm}_{i\in I_k}U_i\right).
\tag{1}
\]
Every common divisor divides \(G_k\), and one initial pair can attain the entire integer \(G_k\).

In particular \(G_1=2\cdot3\cdot5\cdot7\cdot17\cdot29\cdot41=4244730\) is squarefree. **No prime square divides both consecutive values of \(A\)**, even if one switches which of the six factors it divides. The input \((998761,998760)\) attains \(G_1\). A square can recur two steps later: the initial factor \(x\) at \((169,2)\) contains \(13^2\), and the factor \(x^2+y^2\) at \(T^2(169,2)=(4925,2038)\) also contains it.

### Proof

Write \(\alpha=1+\sqrt2,\ \beta=1-\sqrt2,\ g=\alpha/\beta,\ \epsilon=\alpha^2=3+2\sqrt2\). For \(u=x-y,\ v=y\), let \(\gamma=u+v\sqrt2\), with conjugate \(\bar\gamma\). Its norm is \(d\). The map \(T\) multiplies \(\gamma\) by \(\epsilon\), and thus multiplies \(z=\gamma/\bar\gamma\) by \(g^2\). The rational and \(\sqrt2\) coordinates of
\[
\gamma,\qquad \alpha\gamma,\qquad \alpha\gamma^2
\]
are respectively \((x-y,y),\ (x+y,x),\ (x^2+2xy-y^2,x^2+y^2)\). Work modulo \(p^e\) in \((\mathbb Z/p^e\mathbb Z)[\sqrt2]\) for an odd \(p\mid A_0\). Since \(p\nmid d\), all the conjugates used as denominators are units. A coordinate vanishes exactly when the corresponding quotient by its conjugate is \(1\) or \(-1\). Therefore \(p^e\mid A_0\) is equivalent to at least one of
\[
 z=\pm1,\qquad gz=\pm1,\qquad gz^2=\pm1
\tag{2}
\]
modulo \(p^e\). Pairwise coprimality ensures that divisibility by \(p^e\) is concentrated in one factor. Use the same alternatives with \(z'=g^{2k}z\) for \(A_k\).

If both alternatives are linear in \(z\), division and squaring give \(g^i=1\) for some \(i\in\{4k-2,4k,4k+2\}\). If both are quadratic, \(g^{8k}=1\). In the mixed case, squaring the linear relation and eliminating \(z^2\) gives \(g^{8k-2}=1\) or \(g^{8k+2}=1\). For odd \(p\), \(g^i=1\bmod p^e\) exactly when \(p^e\mid U_i=(\alpha^i-\beta^i)/(2\sqrt2)\). Since \(U_{4k}\mid U_{8k}\), this proves the odd upper bound.

For the converse at odd \(p\), every norm-one power of \(g\) whose square is 1 modulo \(p^e\) equals \(1\) or \(-1\). At an inert prime the ring is local with 2 invertible; at a split prime the two components are inverses, so their signs agree. Consequently all odd prime powers in \(U_{4k-2},U_{4k},U_{4k+2}\) can be realized by choosing \(z=1\) or \(z=g^{-1}\) and using the two linear alternatives of (2). These choices are obtained from \(y=0\) or \(x=0\) locally. The same two choices, with the quadratic target at the end, realize \(U_{8k+2}\) and \(U_{8k-2}\), respectively.

For \(p^e\mid U_{8k}\), the quadratic alternative can be realized at the start whenever \(x^2+y^2\) or \(x^2+2xy-y^2\) has a primitive zero modulo \(p^e\). This holds if \(p\equiv1\bmod4\) or \((2/p)=1\), by simple-root lifting. It remains true at the end because \(g^{4k}=\pm1\). The only omitted primes are \(p\equiv3\bmod8\). Their order modulo \(p\) divides \(p+1\), and modulo \(p^e\) divides \(p^{e-1}(p+1)\), by Frobenius and binomial lifting. Its 2-part therefore divides 4. If the order divides \(8k\), it already divides \(4k\), covered by a linear alternative.

At 2, \(d\) is odd and the even coordinate of \((x,y)\) stays the same coordinate modulo 2 under \(T\). Only that coordinate contributes to \(v_2(A)\). If it is divisible by \(2^e\) at both ends, then \(2^e\mid xy'-x'y\), where \((x',y')=T^k(x,y)\). The determinant equals \(dU_{2k}\) by multiplying \(\gamma\) by \(\epsilon^k\). We have \(v_2(U_{2k})=1+v_2(k)\), by duplication and the oddness of \(U_j\) at odd indices. This bound is attained locally by \(y=0,\ x=1\bmod 2^e\).

Combine the local maximizing pairs by the Chinese remainder theorem. A primitive lift is always available. Choose a positive \(y\) in its residue class, then choose \(x>y\) in its required class and congruent to 1 modulo every prime of \(y\) outside \(G_k\). The local pairs already secure primitivity at primes in \(G_k\), including opposite parity at 2. This proves attainment in (1).

### Consequence for multiplicities

For odd \(p\) let \(r_p\) be its first Pell index and \(w_p=v_p(U_{r_p})\). Put \(w_2=1\) and \(c_p=v_p(\gcd(A_0,A_k))\). Then
\[
\prod_p p^{(c_p-w_p)_+}\ \mid\
\operatorname{lcm}(2k-1,\,2k+1,\,4k-1,\,4k,\,4k+1).
\tag{3}
\]
Indeed \(r_p\mid p-(2/p)\), and binomial lifting gives \(v_p(U_i)=w_p+v_p(i)\) for \(r_p\mid i\). Apply (1) prime by prime; the 2-part follows from its separate bound. Thus the product of all common excess powers at ordinary primes (\(w_p=1\)) is \(O((k+1)^5)\). This is uniform even for primes dividing different factors at the two endpoints.

## A stronger height gap away from norms \(1\) and \(-1\)

For \(|d|>1\) there is an absolute bound
\[
\log\gcd(A_0,A_k)\ \ll\ \sqrt{k\log(2|d|)}.
\tag{4}
\]
In particular, for \(d\) fixed with \(|d|>1\), a common divisor at least \(x^\eta\) requires \(k\gg_d\eta^2(\log x)^2\). As the height parameter of the new pair is comparable to \(x\epsilon^k\), this precludes carrying such a divisor to another member of polynomially bounded height in that orbit.

For (4), divide the odd prime powers of the gcd into at most nine groups by the alternatives in (2) at both ends, and write \(D\) for the product of a group. For some \(a,b\in\{0,1,2\}\) we have \(z^4=g^{-2a}\) and \((g^{2k}z)^4=g^{-2b}\bmod D\). It follows that \(g^{8k+2b-2a}=1\bmod D\). Replace \(\gamma\) by \(\gamma_*=\gamma\epsilon^{-h}\) so that \(\sqrt{|d|}\le|\gamma_*|<\epsilon\sqrt{|d|}\) in the real embedding, and put \(z_*=\gamma_*/\bar\gamma_*\). Since \(z_*\) differs from \(z\) by a power of \(g\), the group generated by \(g,z_*\bmod D\) has at most \(4(8k+4)\) elements.

The numbers \(g,z_*\) are multiplicatively independent. At each odd \(p\mid d\), the coprime coefficients \(u,v\) give \(p\nmid v\) and \(u^2\equiv2v^2\bmod p\). Thus \(p\) splits and at one of its places exactly one of \(\gamma,\bar\gamma\) has positive valuation. The same holds after multiplication by a unit. At that place \(z_*\) has nonzero valuation and \(g\) is a unit of infinite order.

Let \(h_0=\log(2|d|)\). For \(k\ge h_0\), pigeonholing \(g^i z_*^j\bmod D\) in a rectangle with sides \(\lceil10\sqrt{k h_0}\rceil,\ \lceil10\sqrt{k/h_0}\rceil\) supplies a nonzero exponent difference in those bounds with \(g^i z_*^j=1\bmod D\). Clearing denominators gives the nonzero element \(d^{|j|}(g^i z_*^j-1)\in D\mathbb Z[\sqrt2]\). Its two archimedean absolute values are at most \(2\epsilon^{|i|+2|j|}|d|^{|j|}\), by the choice of \(\gamma_*\). Its absolute norm is at least \(D^2\), proving \(\log D\ll\sqrt{k h_0}\). For \(k<h_0\), the relation for \(g\) alone gives \(O(k)\). Sum over the groups and use the 2-part of (1).

The norm hypothesis matters for the full gcd. On the norm-one orbit \(\gamma=\alpha^{2k}\), after \(k\) steps it becomes \(\alpha^{4k}\). The starting \(y=U_{2k}\) divides the ending \(y'=U_{4k}\); its logarithm is of order \(k\). The ordinary-prime excess bound (3) still applies.

## Growing runs with separately forced prime powers

There is an absolute constant \(c>0\) and arbitrarily high starting heights \(C\) on the norm \(-1\) Pell orbit for which at least \(c\sqrt{\log\log C}\) consecutive \(T\)-iterates satisfy
\[
 C_j/R_j\ \ge\ \exp(c\sqrt{\log\log C_j}).
\tag{5}
\]
Each member of the constructed run has its own designated prime divisor. This gives simultaneous savings; their proven logarithms are sublinear in \(\log C_j\).

Use the parametrization \((x,y)=(U_{t+1},U_t)\) at odd \(t\), so \(x^2-2xy-y^2=-1\). One \(T\)-step increases \(t\) by 2. Uniformly \(|d|A\ll x^8\le C\) and \(\log C=8t\log\alpha+O(1)\).

For any sufficiently large block length \(b\), take \(r_j=2b+1+2j\) for \(0\le j<b\). Every sufficiently large odd \(r\) has a prime of first Pell index \(r\). Here is a short verification. For \(r>1\), the cyclotomic value \(J_r=\prod_{s\mid r}U_s^{\mu(r/s)}\) satisfies \(\log J_r=\phi(r)\log\alpha+O(1)\) by Binet's formula and the summability of the exponentially small errors. For odd \(r\) there is no factor 2, and Möbius inversion of \(v_p(U_s)=w_p+v_p(s)\) on multiples of \(r_p\) gives valuation \(w_p\) at \(r=r_p\), valuation 1 at \(r=r_pp^a\) with \(a\ge1\), and zero otherwise. Without a prime of first index \(r\), this would give \(J_r\le\operatorname{rad}(r)\le r\), impossible for large odd \(r\) since \(\phi(r)\ge\sqrt r\).

Choose such a prime \(p_j\) at each \(r_j\). The \(p_j\) are distinct. They satisfy \(p_j\equiv\pm1\bmod r_j\) and, by oddness, \(p_j\ge2r_j-1>\max_i r_i\). Also \(p_j\le U_{r_j}\le\exp(O(b))\). Take the least \(e_j\ge1\) with \(p_j^{e_j}\ge e^b\), and put
\[
 N=\operatorname{lcm}(2,r_0,\ldots,r_{b-1})\prod_{j<b}p_j^{e_j}.
\]
We have \(b^2\le\log N\ll b^2\). Choose \(n\in[N,2N)\) congruent to \(r_0\) modulo the initial lcm and to \(-2j\bmod p_j^{e_j}\) for each \(j\). The moduli are coprime. Then \(r_j\mid n+2j\) and \(p_j^{e_j}\mid n+2j\). Lifting gives \(p_j^{e_j+1}\mid U_{n+2j}\), so the corresponding triple satisfies \(C_j/R_j\gg p_j^{e_j}\ge e^b\). Finally \(\log\log C_j=\log n+O(1)\asymp b^2\) uniformly in the block, proving (5).

For a finite check, at \(n=462137765\), modular powering confirms \(29^2\mid U_n,\ 13^3\mid U_{n+2},\ 197^2\mid U_{n+4}\). They have first indices \(5,7,9\), respectively. Independently, for every \(1\le k\le8\), all prime-power components of (1) were checked for local attainment and for failure one power higher; the global divisibility was also checked on all admissible starting pairs with \(x<90\).

## A spacing test without choosing a Pell orbit

Let \(P=dA\). For fixed \(\delta>0\) and modulus \(m\ge1\), put \(q=m/\operatorname{rad}(m)\). Among **all heights**, there are at most \(O_\delta(10^{\omega(m)})\) admissible pairs for which
\[
m\mid P(x,y),\qquad |P(x,y)|/q\le x^{8-\delta}.
\]
This tests whether the repetitions guaranteed by \(m\) are sufficient on their own. The implicit constant is independent of \(m\).

Indeed, put \(t=y/x\), and let \(\alpha\) be the closest of \(0,1,\sqrt2-1\). The simple real roots give \(|P(x,y)|\asymp x^{10}|t-\alpha|\). We also have \(|t-\alpha|\gg x^{-2}\) by the reduced fraction bound at the rational roots and the nonvanishing integer \(x^2-2xy-y^2\) at the quadratic root. Thus \(x\gg m^{1/10}\) and \(x\ll_\delta m^{1/\delta}\). Partition pairs by \(\alpha\) and by their projective root class modulo \(m\); there are at most \(3\cdot10^{\omega(m)}\) choices.

For distinct pairs in a class, order their heights \(x\le x'\). Their nonzero determinant is divisible by \(m\). The two bounds on \(|P|/q\) give
\[
m\le xx'|t-t'|\ll q\left(\frac{x'}{x^{1+\delta}}+\frac{x}{(x')^{1+\delta}}\right).
\]
At sufficiently large \(x\) this implies \(x'\gg\operatorname{rad}(m)x^{1+\delta}\), and hence \(x'\ge x^{1+\delta/2}\). Iterating within the stated polynomial interval of heights leaves \(O_\delta(1)\) pairs per class. The bounded initial heights also contribute \(O_\delta(1)\).

For example, the number of pairs with \(x\le H,\ R\le x^{8-\delta}\), and product of distinct repeated primes at most \(B\), is \(O_{\delta,\eta}(B H^\eta)\) for every \(\eta>0\). Choose \(m=\prod_{p^e\parallel P,\,e\ge2}p^e\). Then the bound on \(|P|/q\) holds with equality to \(R\), and \(m\ll H^{10}\). Sum the preceding estimate using \(\operatorname{rad}(m)\le B\) and convergence of \(\sum_m 10^{\omega(m)}/(m^s\operatorname{rad}(m))\) for \(s>0\). This leaves open exceptional pairs with a changing set of moduli.
