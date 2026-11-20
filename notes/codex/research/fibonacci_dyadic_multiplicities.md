# Multiplicities at Fibonacci indices that are powers of two

Let \(F_n,L_n\) be the Fibonacci and Lucas numbers, and \(\alpha=(1+\sqrt5)/2\). For \(j\ge2\), put \(r=2^j\) and
\[
J_j=\frac{F_{2^j}}{F_{2^{j-1}}}=L_{2^{j-1}}.
\]
The first value is \(J_2=3\), and \(J_{j+1}=J_j^2-2\). Hence the \(J_j\) are odd, are \(3\bmod4\), and are pairwise coprime. Indeed all subsequent terms are \(-2\) and then \(2\) modulo any earlier term. We have \(F_{2^k}=\prod_{j=2}^k J_j\).

## A prime of odd multiplicity in each term

Every prime \(p\mid J_j\) has first Fibonacci index \(r\). Its first index divides \(2^j\), and it cannot divide \(2^{j-1}\) because \(J_j\) is coprime to the earlier factors. Also \(p\ne2,5\). The order of \(\alpha/((1-\sqrt5)/2)\) in the residue field at \(p\) equals \(r\) and divides \(p-(5/p)\). Thus \(p\equiv\pm1\bmod r\) and \(p\ge r-1\). This includes \(p=3\), whose first index is 4. [Order argument](hall_pell_fibonacci_ranks.md)

Since \(J_j\equiv3\bmod4\), some \(p_j\equiv3\bmod4\) has odd valuation in \(J_j\). It satisfies \(p_j\equiv-1\bmod 2^j\). Define the squarefree part \(s(m)\) by \(m=s(m)y^2\) with \(s(m)\) squarefree. Pairwise coprimality gives the unconditional bound
\[
s(F_{2^k})\ \ge\ \prod_{j=2}^k(2^j-1).
\]
In particular, at \(n=2^k\) the logarithm of the squarefree part is at least \((\log n)^2/(2\log 2)+O(\log n)\). The prime \(p_j\) could occur to exponent \(3,5,\ldots\).

## What a powerful term would imply for abc

An integer is powerful if every prime dividing it occurs at least twice. Write \(E(u)=\log(u/\operatorname{rad}(u))\). Primitively normalize \(L_t^2-5F_t^2=4(-1)^t\) at \(t=2^{k-1}\), with \(c_k\) the largest term and \(R_k\) the radical of the product of the three terms. Then
\[
\log c_k=2^k\log\alpha+O(1),\qquad
\log c_k-\log R_k=E(F_{2^k})+O(1).
\]
This follows from \(F_{2t}=F_tL_t\); normalization and the primes \(2,5\) cost bounded logarithms. [Details of the Pell triple](hall_pell_fibonacci_ranks.md)

If the last \(b\ge1\) terms \(J_{k-b+1},\ldots,J_k\) are powerful, pairwise coprimality gives
\[
E(F_{2^k})\ \ge\ \tfrac12\log(F_{2^k}/F_{2^{k-b}})
=\tfrac12(1-2^{-b})\,2^k\log\alpha+O(1).
\]
Thus infinitely many such blocks, for a fixed \(b\), would give
\[
\liminf_{\text{those }k}\frac{\log c_k}{\log R_k}
\ \ge\ \frac{2}{1+2^{-b}}.
\]
For \(b=1\) the bound is \(4/3\), enough to disprove abc. Whether such blocks occur infinitely often remains undetermined here.

### What the perfect-power theorem decides

Bugeaud, Mignotte and Siksek proved that the only perfect powers among the Lucas numbers are 1 and 4. Every \(J_j\) is a Lucas number at least 3 and odd. Consequently, if one \(J_j\) were powerful, it would have at least two distinct prime divisors. A single prime divisor would make \(J_j=p^e\) with \(e\ge2\). Furthermore, the prime \(p_j\equiv3\bmod4\) above would occur with exponent at least 3. For each divisor \(p\) of a powerful term, \(p^2\mid F_{p-(5/p)}\) since \(r\mid p-(5/p)\) and \(F_r\mid F_{p-(5/p)}\). For \(p_j\) the divisibility strengthens to \(p_j^3\mid F_{p_j+1}\). Thus even one powerful term would exhibit two distinct Fibonacci–Wieferich primes, one satisfying this stronger cubic divisibility. [Bugeaud, Mignotte and Siksek](https://arxiv.org/abs/math/0403046)

In the other direction, infinitely many terms with an exponent-one prime divisor would give infinitely many distinct non-Fibonacci–Wieferich primes. Each prime occurs in a single \(J_j\), and the multiplier \((p-(5/p))/r\) is prime to \(p\), so lifting preserves the exponent one. This identifies the arithmetic issue even for a subsequence. Riasat's 2026 preprint abstract reports a bound on repeated primitive factors when \(\phi(r)/r\) is bounded below, which includes \(r=2^j\). That bound assumes rational abc. The independent local result in the abstract describes initial multiplicities and provides no asserted global frequency bound for this sequence. [Riasat](https://arxiv.org/abs/2611.20650)

## Powerful values of the quadratic in the same congruence classes

Fix \(j\ge3\), put \(r=2^j,\ x_0=J_{j-1}\), and write \(J_j=x_0^2-2=d y_0^2\) with \(d\) squarefree. For every positive modulus \(M\) whose prime factors are at most \(r-3\), there are infinitely many positive integers \(x\equiv x_0\bmod M\) for which \(x^2-2\) is powerful and has **the same squarefree part \(d\)**. The prime powers in \(M\) may have arbitrary exponents.

To prove this, work in \(\mathbb Z[\sqrt d]\). The integer \(d>1\) is odd, since \(J_j\equiv3\bmod4\). Set
\[
u=(x_0+y_0\sqrt d)^2/2=x_0^2-1+x_0y_0\sqrt d,\qquad
x_t+y_t\sqrt d=(x_0+y_0\sqrt d)u^t.
\]
The norm of \(u\) is 1. All these pairs are integral and satisfy \(x_t^2-2=d y_t^2\). Multiplication by \(u\) defines an invertible two-by-two matrix modulo \(M\); let \(h\) be its order, taking \(h=1\) for \(M=1\). For each \(\ell^a\parallel M\), the group order of \(\mathrm{GL}_2(\mathbb Z/\ell^a\mathbb Z)\) is \(\ell^{4(a-1)}(\ell^2-1)(\ell^2-\ell)\). By the Chinese remainder theorem every prime dividing \(h\) is at most \(\max_{\ell\mid M}(\ell+1)\le r-2\) when \(M>1\). Every prime dividing \(d\) is at least \(r-1\), by the Fibonacci order argument. Thus \(\gcd(h,d)=1\).

For every \(p\mid d\), reduction modulo \(p\) gives \((\sqrt d)^2=0,\ x_0^2=2,\ u=1+x_0y_0\sqrt d\). Expanding \(u^t\) in this quotient yields
\[
y_t\equiv y_0(1+2t)\pmod p.
\]
Choose \(t\equiv0\bmod h\) and \(2t+1\equiv0\bmod d\). There are infinitely many such positive \(t\). The first congruence preserves \(x_t\equiv x_0\bmod M\); the second gives \(d\mid y_t\). Every prime in \(d\) now occurs at least cubed in \(d y_t^2\), and every other prime divisor occurs at least squared. The \(x_t\) grow strictly. This proves the claim.

For example \(J_3=3^2-2=7\), whereas \(11427\equiv3\bmod16\) and \(11427^2-2=7^3\cdot617^2\). The constructed inputs need not themselves belong to the Lucas sequence. The result specifies precisely why congruences on the quadratic's input at the indicated primes, by themselves, cannot certify a factor of exponent one.

## Finite checks

For ranks \(4,8,16,32,64,128,256,512,1024\), respective prime divisors of exponent one are \(3,7,47,2207,1087,127,119809,34303,21503\). Each was checked by trial-division primality and exact reduction of \(J_j\) modulo \(p^2\). These nine terms are therefore excluded from the powerful-term criterion. The simultaneous congruences in the construction were also checked by modular powering for ranks \(8\) through \(256\).
