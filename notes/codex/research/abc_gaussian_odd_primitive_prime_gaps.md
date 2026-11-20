# Prime indices with large odd-exponent primitive primes

Let \(G=(-3,9)\) on \(E:y^2=x^3-36x\), and write \(B_n^2\) for the reduced denominator of \(X(nG)\). Write \(\log_j\) for the \(j\)-fold natural logarithm. There exist infinitely many primes \(r\equiv3\bmod8\) for which
\[
    P^-(B_r)\gg r^2\log r\,\frac{\log_2 r\,\log_4 r}{(\log_3 r)^2}.       \tag{1}
\]
For each of these ranks, at least one prime of odd exponent exceeds this bound and is \(13\bmod24\). All primes in \(B_r\) are primitive at a prime index. There is also a density result. For every \(Y=Y(X)\ge1\), \(Y=o(\log X)\), all but \(O(XY/(\log X)^2)\) primes \(r\equiv3\bmod4\) in \([X,2X]\) have \(P^-(B_r)>r^2Y\). On the subclass \(r\equiv3\bmod8\) the odd-exponent conclusion needs no Diophantine finiteness theorem.

For odd \(r\) each denominator prime \(p\) satisfies \(p\equiv1\bmod12\). For prime \(r\equiv3\bmod4\) the Gaussian annihilator is \((r)\), and the Frobenius has the form \(1+r\alpha\) for \(\alpha=a+bi\). The prime norm is \(p=(1+ra)^2+r^2b^2\), with \(4\mid a\) and \(b\) even and nonzero. Conjugate to take \(b>0\). We use these as necessary conditions, so a proof of compositeness of the norms suffices. [CM and parity restrictions](abc_gaussian_scalar_prime_scan.md)

## The odd-exponent prime and its residue

For every positive odd \(n\),
\[
                       (2/B_n)=(2/n).                              \tag{2}
\]
Use the normalized division polynomials from the fourth-power scan. On \(y^2=x^3-4x\) at \(T=(-1,\sqrt3)\), let \(f_j=\psi_j(T)\) for odd \(j\), and \(f_j=\psi_j(T)/(2\sqrt3)\) for even \(j\). Their initial values are \(f_1=f_2=1,f_3=-37,f_4=-70\). For \(n=2m+1\), the division recurrence gives
\[
 f_n=\begin{cases}
 f_{m+2}f_m^3-144f_{m-1}f_{m+1}^3,&m\text{ odd},\\
 144f_{m+2}f_m^3-f_{m-1}f_{m+1}^3,&m\text{ even}.
 \end{cases}
\]
The even recurrence supplies integers throughout. Induction shows all odd \(f_n\) are units modulo 6. The identity \(X(nG)=-3-36f_{n-1}f_{n+1}/f_n^2\) has no cancellation at \(p\ge5\) dividing \(f_n\): reduction of \(T\) is nonidentity, the curve is good, \(2\sqrt3\) is a unit and \([n]T=O\) then precludes \([n\pm1]T=O\). Therefore \(B_n=|f_n|\). The even quadratic character modulo 8 is insensitive to the sign of \(f_n\). In the first recurrence its value is the product for indices \(m,m+2\); in the second it is the product for \(m-1,m+1\). The character \((2/n)\) satisfies both relations by the four odd residues modulo 8 and the four even residues for \(m\) when appropriate; it agrees at \(n=1,3\). This proves (2). Since every prime factor is \(1\bmod12\), the primes contributing the negative quadratic character in (2) are exactly those \(13\bmod24\) of odd valuation. [Division-polynomial normalization](abc_gaussian_quartic_prime_scan.md)

For \(r\equiv7\bmod8\), a negative character is unnecessary to prove eventual nonsquareness. The known parametrization gives \(B_r=(x^2+3y^2)/4\) and \(F_0(x,y)=x^4-18x^2y^2+9y^4=-2z^2\). A square value lifts \(x/y\) to the genus-two curve \(v^2=-2(X^2+3)F_0(X,1)\). Its six roots are distinct, as \(F_0\) is separable and \(F_0(X,1)=72\) when \(X^2=-3\). Positive odd indices have distinct slopes since \(X(rP)=-2(x/y)^2\) for a nontorsion point \(P\). Faltings therefore excludes square values for all sufficiently large \(r\). The stronger elliptic Chabauty classification excludes square values at *every* odd \(r>1\). [Square denominator classification](abc_full_quartic_square_chabauty5.md) This gives an odd-exponent prime in the density result for the entire class \(3\bmod4\), without determining its class modulo 24 for \(r\equiv7\bmod8\).

## Density among the prime ranks

Put \(f_\alpha(t)=N(1+\alpha t)\). A candidate \(p\le r^2Y\) requires \(N\alpha\ll Y\). For fixed \(\alpha=a+bi\) with \(b\ne0\), upper-bound sieve the integers \(t\in[X,2X]\) for simultaneous primality of \(t,f_\alpha(t)\). At an odd rational prime \(\ell\), the root \(t=0\) is distinct from any root of \(f_\alpha\). For split \(\ell\equiv1\bmod4\) with \(\ell\nmid bN\alpha\), the two additional roots are distinct and nonzero. At inert primes retain at least the single root \(0\). Thus the standard upper-bound sieve yields
\[
  \#\{X\le t\le2X:t,f_\alpha(t)\text{ prime}\}
   \ll \frac{X}{(\log X)^2}
       \prod_{\substack{\ell\mid bN\alpha\\\ell\equiv1(4)}}(1+C/\ell).        \tag{3}
\]
For explicit uniformity, sieve split primes not dividing \(bN\alpha\) on three residues and all other primes on one. The local density is at most \(3/\ell\). The integer interval has remainder \(O(3^{\omega(d)})\) for every squarefree modulus \(d\); taking level \(X^{1/4}\) and sieve cutoff \(X^{1/1000}\) makes the standard Selberg upper bound uniform. The error summed with the sieve weights is \(O(X^{1/4}(\log X)^{O(1)})\). The generic product over split primes with three excluded classes and inert primes with one is \(\asymp(\log X)^{-2}\) by Mertens in progressions. At exceptional split primes the ratio is at most \(1+C/\ell\) for an absolute \(C\). Prime values are larger than the sieve cutoff since \(b\ne0\).

Here \(W(t)=\prod_{\ell\mid t,\ \ell\equiv1(4)}(1+C/\ell)\) satisfies
\[
       \sum_{0<|b|\le\sqrt U}W(b)^2\ll\sqrt U,\qquad
       \sum_{0<N\gamma\le U}W(N\gamma)^2\ll U .
\]
For the first expand over squarefree divisors. For the second expand instead over the Gaussian prime ideals dividing \((\gamma)\), majorizing the local factor by \(1+C'/N\mathfrak p\) at each split ideal. The number of nonzero Gaussian integers of norm at most \(U\) divisible by an ideal \(\mathfrak d\) is \(O(U/N\mathfrak d)\) for \(N\mathfrak d\le U\), by principality and the disk lattice count. The resulting Euler product has local increments \(O((N\mathfrak p)^{-2})\). Cauchy–Schwarz now gives \(\sum_{N\alpha\le U,\ b\ne0}W(b)W(N\alpha)\ll U\). Summing (3) proves the claimed exceptional count. With \(Y=o(\log X)\) this is a relative density-zero subset of the primes in either fixed inert class modulo 8.

## An explicit larger gap on an infinite sequence

Fix a large real \(A\). Write \(L=\log A,\ l=\log L,\ l'=\log l\), and put
\[
      w=\exp(Ll'/(40l)),\qquad F=\log w/l,\qquad Z=A/F.
\]
In particular \(F\to\infty,\ \sqrt{2A}<Z\), and \(w=A^{o(1)}\). We impose a reduced congruence class for \(r\) which kills every candidate \(\alpha\) with \(N\alpha\le A\). Start with \(r\equiv3\bmod8\). At split rational primes \(q\le w\) put \(r\equiv-1\bmod q\); at split primes \(w<q\le Z\) and inert primes \(q\le\sqrt{2A}\) put \(r\equiv1\bmod q\).

For a survivor take \(\beta=1+\alpha\), of norm at most \(2A\), and at least four since \(b\ge2\). An even norm would make \(N(1+r\alpha)\) even as well. Every inert divisor of \(N\beta\) is at most \(\sqrt{2A}\), since it occurs to even exponent. Thus every surviving \(\beta\) has either \(w\)-smooth norm or
\[
             \beta=\gamma\lambda,\qquad N\gamma\le 2F,\qquad N\lambda=P>Z
\]
for a rational split prime \(P\) and a Gaussian prime \(\lambda\). There is at most one prime factor above \(Z\) in the norm, with multiplicity one. This factorization uses unique factorization in \(\mathbf Z[i]\).

The number of Gaussian integers of \(w\)-smooth norm up to \(2A\) is \(O(A/L^7)\). Here are details allowing \(w\) to grow. Put \(u=L/\log w=40l/l'\), \(\theta=(\log u)/(2\log w)\). Rankin's bound for ordinary smooth numbers gives
\[
 \Psi(2A,w)\le(2A)^{1-\theta}\prod_{q\le w}(1-q^{-1+\theta})^{-1}\ll A/L^{18}
\]
for large \(A\). Indeed \(\theta L=(20+o(1))l\), while the logarithm of the product is at most \(l+o(l)\). For that last bound the unshifted sum is \(\log\log w+O(1)\le l+O(1)\); the added first-power sum is at most \(\theta w^\theta\sum_{q\le w}\log q/q\ll\sqrt u\log u=o(l)\), and the higher powers are uniformly bounded. Now \(r_2(m)\le4\tau(m)\) and \(\sum_{m\le 2A}\tau(m)^2\ll A L^3\); Cauchy–Schwarz proves the stated smooth-norm count.

For the other survivors \(\lambda\) has prime norm and none of the split primes \(q\le w\) divides \(N(2-\gamma\lambda)=N(1-\alpha)\). Uniformly for \(0<N\gamma\le2F\), the number of such \(\lambda\) is at most
\[
       \ll \frac{A}{N\gamma}\frac{W_1(N\gamma)}{L\log w},
   \qquad W_1(m)=\prod_{\substack{q\mid m\\q\equiv1(4)}}(1+C_1/q).         \tag{4}
\]
For the lattice sieve work in the square containing the norm disk, of side \(O(T)\), \(T=\sqrt{2A/N\gamma}\). Under \(\mathbf Z[i]/(q)\simeq\mathbf F_q^2\) at split \(q\), a nonzero norm of \(\lambda\) excludes zero in each coordinate. At \(q\le w\) prime to \(N\gamma\), the second condition also excludes \(2/\gamma_j\) in coordinate \(j\). Thus the local surviving fractions are \((1-1/q)^2\) at the generic primes \(w<q\le z\) and \((1-2/q)^2\) at the small primes \(q\le w\). For \(q\mid N\gamma\) retaining only the first condition is sufficient for an upper bound. Take \(z=A^{1/1000}\) and level \(T^{1/4}\), so \(w<z<Z<P\) for large \(A\). For every squarefree modulus \(d\) built from these split sieve primes the number of bad residue pairs is at most \(4^{\omega(d)}d\). Counting the square modulo \(d\) gives remainder \(O(4^{\omega(d)}(T+d))\). The weighted remainder sum through level \(T^{1/4}\) is \(O(T^{5/4}(\log T)^{O(1)})\), negligible uniformly. The Euler product is \(O(W_1(N\gamma)/(\log z\log w))\) by Mertens in the split progression. This proves (4) by the ordinary upper-bound sieve.

The Gaussian divisor estimate used in (3) gives \(\sum_{N\gamma\le2F}W_1(N\gamma)/N\gamma\ll\log(2F)\) by partial summation. Hence the total number of survivors is
\[
      O\!\left(\frac{A}{L^7}+\frac{A\log(2F)}{L\log w}\right)
        =O\!\left(\frac{A}{FL}\right).
\]
Give each survivor its own split prime \(q\in[3A,6A]\). There are \(\gg A/L\) choices, more than needed. For any \(t^2=-1\bmod q\) prescribe \(r\equiv-(a+bt)^{-1}\bmod q\); the inverse exists since \(0<N\alpha\le A<q\). Then \(q\mid N(1+r\alpha)\). All imposed congruences are reduced. Their total modulus \(M\) satisfies \(\log M\ll Z+\sqrt A+(A/(FL))\log(6A)\ll A/F\).

Take the least prime \(r\) in this CRT class. Linnik's theorem gives \(\log r\ll A/F\). Also \(r\equiv1\) modulo the product of all split primes in \((w,Z]\), so \(\log r\gg A/F\) by the prime number theorem in the progression \(1\bmod4\). All the imposed divisors \(q\le6A\) are proper because the candidates have \(N(1+r\alpha)\ge r^2b^2\ge4r^2\). Therefore for every primitive denominator prime one has \(N\alpha>A\) and \(p>(r\sqrt A-1)^2\gg r^2A\). As \(\log r\asymp A/F\), the relation \(F=L l'/(40l^2)\) yields (1). Increasing \(A\) produces unbounded prime ranks \(3\bmod8\), and (2) supplies the required odd-exponent prime at each rank.

This is a logarithmic improvement of the quadratic cutoff. A fixed exponent \(2+\delta\) or a quartic cutoff for infinitely many ranks is unresolved here. The argument for (1) develops the norm covering for the other CM field by a second lattice sieve and a growing smoothness cutoff. [Previous norm cover](abc_odd_rank_quadratic_large_gaps.md)
