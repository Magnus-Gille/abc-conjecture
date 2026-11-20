# Fibonacci radicals and the Pell equation

Write \(F_0=0,F_1=1,L_0=2,L_1=1\) for the Fibonacci and Lucas sequences, and put \(\alpha=(1+\sqrt5)/2,\ \beta=(1-\sqrt5)/2\). For a positive integer \(m\), set \(E(m)=\log(m/\operatorname{rad}(m))\), with \(\operatorname{rad}(1)=1\). All logarithms are natural.

## An exact test family for rational abc

For every \(n\ge1\), the equation \(L_n^2-5F_n^2=4(-1)^n\) gives a positive integer sum. Divide its three terms \(4,L_n^2,5F_n^2\) by their gcd \(g\). The gcd is 4 if \(3\mid n\) and 1 otherwise, since \(L_n\) is even exactly when \(3\mid n\). Write \(c_n\) for the greatest of the three normalized terms and \(R_n\) for the radical of their product. The duplication formula \(F_{2n}=F_nL_n\) gives

\[
\log c_n=2n\log\alpha+O(1),\qquad
\log R_n=\log\operatorname{rad}(F_{2n})+O(1).
\]

Only 2 and 5 can change the second logarithm, by at most \(\log 10\). Also \(\log F_{2n}=2n\log\alpha+O(1)\). Consequently

\[
\log c_n-\log R_n=E(F_{2n})+O(1).
\]

Thus rational abc holds on these particular triples for every fixed exponent \(1+\varepsilon\) exactly when \(E(F_k)=o(k)\) for all Fibonacci indices. The even indices already suffice because \(F_k\mid F_{2k}\) and \(E\) increases under divisibility. In one direction, \(E(F_{2n})=o(n)\) gives \(\log R_n/\log c_n\to1\). In the other, \(E(F_k)\ge\delta k\) infinitely often for some fixed \(\delta>0\) gives \(\log R_k\le\log c_k-\delta k+O(1)\). Choosing \(\varepsilon>0\) small enough gives \(c_k/R_k^{1+\varepsilon}\to\infty\) on that subsequence.

For example, call \(m\) *powerful* if each of its prime divisors occurs at least twice. If \(F_k\) were powerful for infinitely many \(k\), then \(E(F_k)\ge\tfrac12\log F_k\) on those indices. Their normalized Pell triples would satisfy

\[
\liminf\frac{\log c_k}{\log R_k}\ \ge\ \frac{2}{2-1/2}=\frac43.
\]

This is a sufficient condition for a counterexample sequence. Its hypothesis is unproved here.

## A bound for the full contribution of small and medium primes

For sufficiently large \(n\), write \(H(n)=\log n/\log\log n\). For each fixed \(0<\gamma<1/103.8\), there is a constant \(c_\gamma>0\) such that at every sufficiently large index

\[
\sum_{p\le n\exp(\gamma H(n))} v_p(F_n)\log p
\ \ll_\gamma\ n\exp(-c_\gamma H(n)).
\tag{1}
\]

In particular for every fixed \(A>0\), primes \(p\le n(\log n)^A\), counted with their full multiplicities, contribute \(o(n)\). The proof below uses an unconditional theorem of Stewart.

**Group by the index where a prime first appears.** For \(p\ge7\), let \(r=\rho(p)\) be its first Fibonacci index and let \(w_p=v_p(F_r)\). In the residue field at \(p\), \(r\) is the multiplicative order of \(\alpha/\beta\). If 5 is a square modulo \(p\), this order divides \(p-1\). Otherwise Frobenius exchanges \(\alpha,\beta\), so it divides \(p+1\). Thus \(p\equiv\pm1\bmod r\) and \(p\nmid r\). Binet's formula and binomial lifting in the unramified local field give

\[
 p\mid F_n\quad\Longleftrightarrow\quad r\mid n,\qquad
 v_p(F_n)=w_p+v_p(n)\quad(r\mid n).
\]

The extra \(v_p(n)\log p\) terms sum to at most \(\log n\). The primes \(2,3,5\) also contribute \(O(\log(2n))\) altogether. In detail, \(v_5(F_n)=v_5(n)\), and \(v_3(F_n)=1+v_3(n)\) when \(4\mid n\) and zero otherwise. The valuation at 2 is zero for \(3\nmid n\), one for \(n\equiv3\bmod6\), and \(2+v_2(n)\) for \(6\mid n\). The odd-prime formulas follow by lifting from \(F_4=3\) and \(F_5=5\), using the binomial expansion of \((\beta^r+\sqrt5 F_r)^k\) also at the ramified prime 5. For 2, reduction modulo 4 gives the odd-index cases. Duplication gives the successive valuations at \(2^j m\) for odd \(3\mid m\), since \(L_m\equiv4\bmod8\) and \(L_{2^i m}\equiv2\bmod4\) for \(i\ge1\). Both congruences follow from the Lucas recurrence modulo 8 (period 12).

**Bound the total prime mass at one rank.** Put \(U_r=\prod_{\rho(p)=r,\ p\ge7}p^{w_p}\). For \(r>1\) let \(J_r=\Phi_r(\alpha,\beta)\) with \(\Phi_r(X,Y)\) the homogeneous cyclotomic polynomial. This is a positive integer. Integrality follows from algebraic integrality and symmetry under exchange of \(\alpha,\beta\), and positivity from the product formula below. The cyclotomic factorization gives \(F_n=\prod_{r\mid n,\,r>1}J_r\). A prime first appearing at \(r\) occurs in none of the factors \(J_d\) with \(d\) a proper divisor of \(r\). Hence \(U_r\mid J_r\). Möbius inversion and Binet give

\[
\log J_r=\sum_{d\mid r}\mu(r/d)\log F_d
        =\phi(r)\log\alpha+O(1).
\]

Indeed the constant \(-\log\sqrt5\) cancels, and \(\sum_{d\ge1}|\log(1-(-\alpha^{-2})^d)|<\infty\). In particular \(\log U_r\ll\phi(r)\). Set \(U_1=1\).

**Small divisors of the index carry little weight.** The weights \(\phi(r)/n\) for \(r\mid n\) describe \(n/\gcd(m,n)\) for uniform \(1\le m\le n\). By the Chinese remainder theorem,

\[
\frac1n\sum_{m=1}^n\sqrt{\gcd(m,n)}
=\prod_{p^e\parallel n}\left(1+
  \sum_{j=1}^e\frac{p^{j/2}-p^{(j-1)/2}}{p^j}\right)
\le \exp(O(\sqrt{\log n})).
\]

Each local logarithm is \(O(1/\sqrt p)\). Ordering the distinct primes as \(p_i\ge i+1\) bounds their sum of inverse square roots by \(O(\sqrt{\omega(n)})=O(\sqrt{\log n})\). For fixed \(s>0\), Markov's inequality gives

\[
\sum_{\substack{r\mid n\\ r\le n e^{-sH(n)}}}\phi(r)
\le n\exp(-sH(n)/2+O(\sqrt{\log n})).
\tag{2}
\]

This controls the full mass \(\sum\log U_r\) at small ranks even when \(n\) has many divisors.

**Large divisors of the index restrict the candidate primes.** Let \(a=1/51.9\), \(Y=n e^{\gamma H(n)}\), and take \(s=(a-2\gamma)/8>0\). Stewart's valuation lemma for the fixed Lucas pair \((\alpha,\beta)\) gives, for all sufficiently large \(p\ge7\) of rank \(r\),

\[
w_p\ll p\exp(-a\log p/\log\log p)\log r.
\]

Here \(p\) is unramified, and \(\sqrt5,\beta\) are local units, so \(w_p\) equals the valuation of \((\alpha/\beta)^r-1\). [Stewart, Lemma 4.3 in the published paper](https://doi.org/10.1007/s11511-013-0105-y) · [Preprint, Lemma 8](https://arxiv.org/abs/1008.1274)

For \(r\mid n\) with \(r>n e^{-sH(n)}\), there are \(O(Y/r+1)\) candidate integers \(p\le Y\) in the two classes \(\pm1\bmod r\). Also \(p\ge r-1\), and \(\log p/\log\log p=(1+o(1))H(n)\) uniformly over this range. Since \(Y/r\le e^{(\gamma+s)H(n)}\), the full mass from these primes at this rank is at most

\[
 r\exp\bigl((2\gamma+2s-a+o(1))H(n)\bigr).
\]

Factors \(\log p\) and \(\log r\) are absorbed by the \(o(1)H(n)\) term. We have \(r/\phi(r)\le1+\omega(r)\ll\log(2r)\) by bounding \(\prod_{p_i\mid r}p_i/(p_i-1)\) with \(\prod_{i=1}^{\omega(r)}(i+1)/i\). Replace the leading \(r\) by \(\phi(r)\) with the same type of error, and sum using \(\sum_{r\mid n}\phi(r)=n\). The large-rank exponent is strictly negative. Combining this with (2) and the logarithmic cost of lifting proves (1), for instance with \(c_\gamma=s/4\).

## Which primes could disprove abc on this family?

The valuation formulas give the exact integer identity, written as a rational product,

\[
\frac{F_n}{\operatorname{rad}(F_n)}
=\frac{2^{\mathbf{1}_{6\mid n}}}{5^{\mathbf{1}_{5\mid n}}}
  \gcd(n,F_n)\prod_{\substack{p\ge7\\\rho(p)\mid n}}p^{w_p-1}.
\]

Combining this with (1), the Pell family disproves abc if and only if some fixed \(\delta>0\) and infinitely many indices \(n\) satisfy

\[
\sum_{\substack{p\mid F_n,\ p>n e^{\gamma H(n)}\\w_p\ge2}}
   (w_p-1)\log p\ \ge\ \delta n .
\]

These are Fibonacci–Wieferich primes, at which \(p^2\) already divides the first Fibonacci number divisible by \(p\). The estimate leaves the displayed large-prime sum uncontrolled. Riasat's November 2026 abstract gives estimates for repeated primitive divisors of Lucas sequences assuming rational abc. That assumption prevents using the reported estimates to settle this sum unconditionally. Grell and Peng earlier deduced infinitude of non-Fibonacci–Wieferich primes from number-field abc. [Riasat](https://arxiv.org/abs/2611.20650) · [Grell and Peng](https://arxiv.org/abs/1511.01210)

## Connection with the larger polynomial family

The same Fibonacci obstruction occurs within a single progression of the triples \(1728t+5(F_nB)^2=A^3\), where \(t=L_n-11,\ A=t^2+10t+5,\ B=t^2+4t-1\). Take \(n=12j+5\), \(j\ge1\). Binet's product identity gives

\[
t=5F_{6j}F_{6j+5}.
\]

Here \(t\) is even and \(5\mid t\). We have \(v_5(A)=1\), \(A\) odd, \(3\nmid A\), and \(\gcd(t,A)=5\). Thus dividing the triple by \(\gcd(t,125)\) makes it primitive. This divisor is 5 for \(5\nmid j\) and 125 otherwise, since 5 divides \(F_k\) exactly when \(5\mid k\). The three Fibonacci indices \(6j,6j+5,12j+5\) have pairwise gcd \(\gcd(j,5)\). Strong divisibility of the Fibonacci numbers shows that their values have pairwise gcd 1 or 5, respectively. Therefore

\[
E(tF_n)=E(F_{6j})+E(F_{6j+5})+E(F_n)
          +3\mathbf{1}_{5\mid j}\log5.
\]

Every \(F_k\) divides some such \(t\) with \(n\le12k+5\), by taking \(j=k/\gcd(k,6)\). Hence \(E(tF_n)=o(n)\) on this progression exactly when \(E(F_k)=o(k)\) over all indices. The two quadratic factors \(A,B\) present additional possibilities for radical loss. [Polynomial identity and its other progression](hall_pell_direction.md)
