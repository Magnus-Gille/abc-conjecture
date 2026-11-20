# Large simple primes of high order in Mersenne numbers

Write \(M_n=2^n-1\), \(h=\log 2\), and \(D_n=\log(M_n/\operatorname{rad}(M_n))\). Call a prime factor of \(M_n\) simple if its valuation in \(M_n\) is one. For \(C>0\) define
\[
 T_C(n)=\min\left\{t\ge1:\sum_{\substack{p\mid n\\p>t}}\frac1p\le C\right\}.
\]
Assume abc on the primitive triples \(1+M_n=2^n\), equivalently \(D_n=o(n)\). For every fixed \(C>0\) and \(0<\alpha<h/4\), all sufficiently large \(n\) satisfy
\[
 \sum_{\substack{v_p(M_n)=1,\ \operatorname{ord}_p(2)\ge n/T_C(n)\\
                   p>\alpha\varphi(n)^2/T_C(n)^2}}\log p
                  \gg_{C,\alpha} n .                                      \tag{1}
\]
In particular, if \(P_C(n)\) is the largest simple prime factor with order at least \(n/T_C(n)\), taking the maximum as 1 when the set is empty, then
\[
 \liminf_{n\to\infty}\frac{T_C(n)^2 P_C(n)}{\varphi(n)^2}
                \ge \frac{\log 2}{4}.
\]
These statements are conditional. The pointwise mass estimate (4) below is unconditional and records the dependence on the actual defect. The constant \(h/4\) uses the order congruence valid at every index. The prime-power estimate uses additional quadratic-residue information. [Prime-power and unrestricted smoothness tests](abc_mersenne_quadratic_prime_threshold.md)

## A uniform estimate for the coindex

Let \(U\) be uniform modulo \(n\), set \(G=\gcd(U,n)\), and put
\[
 F_n(t)=\Pr(G\le t)=\frac1n\sum_{\substack{g\mid n\\g\le t}}\varphi(n/g),
 \qquad B_n(t)=\prod_{\substack{p\mid n\\p>t}}(1-1/p).
\]
With \(H_j=\sum_{m=1}^j1/m\), for every \(n\ge1\) and real \(t\ge1\),
\[
 H_{\lfloor t\rfloor}\prod_{p\le t}(1-1/p)\,B_n(t)
                       \le F_n(t)\le B_n(t).                              \tag{2}
\]
Indeed, \(G\le t\) requires that no prime of \(n\) above \(t\) divide \(U\). This event has probability \(B_n(t)\) and is independent of the valuations at smaller primes by the Chinese remainder theorem. For each prime \(p\le t\) choose an independent random variable \(V_p\) with \(\Pr(V_p\ge j)=p^{-j}\) for integers \(j\ge0\). The small-prime part of \(G\) has the same distribution as \(\prod_{p\le t}p^{\min(V_p,v_p(n))}\), which is at most \(\prod_{p\le t}p^{V_p}\). The latter product equals any prescribed integer \(m\le t\) with probability \(m^{-1}\prod_{p\le t}(1-1/p)\). Summing proves (2).

The harmonic prefactor tends to \(e^{-\gamma}\) by Mertens' product theorem and has a positive absolute lower bound for all \(t\ge1\). Also \(\log B_n(t)=-\sum_{p\mid n,\ p>t}1/p+O(1)\) uniformly, since the errors are bounded by an absolutely convergent sum of \(O(p^{-2})\). Consequently \(F_n(t)\) stays bounded away from zero along a sequence exactly when the indicated reciprocal-prime sums stay bounded. In particular \(F_n(T_C(n))\gg e^{-C}\). For large \(n\) one has \(T_C(n)\le\log n\), since
\[
                 \sum_{\substack{p\mid n\\p>\log n}}\frac1p
                             \le\frac{1}{\log\log n}.
\]
Here each prime in the sum contributes more than \(\log\log n\) to \(\log n\), and its reciprocal is less than \(1/\log n\).

A second form of (2) is useful when only the height of the index is given. Uniformly for \(1\le t\le\log n\),
\[
          F_n(t)\ \ge\ (e^{-\gamma}-o(1))
                            \frac{H_{\lfloor t\rfloor}}{\log\log n}.
                                                                            \tag{3}
\]
Apply the same coupling with all primes up to \(y=\log n\) and condition on no larger prime dividing \(G\). The latter event has probability \(1-o(1)\) by the preceding reciprocal-prime estimate. Every \(m\le t\) has all its prime factors at most \(y\), so the model probability is exactly \(H_{\lfloor t\rfloor}\prod_{p\le y}(1-1/p)\). Formula (3) follows from Mertens' theorem.

## The pointwise mass estimate

For fixed \(\alpha>0\), let \(1\le t\le\log n\) and \(X=\alpha\varphi(n)^2/t^2\). Uniformly in this range,
\[
 \sum_{\substack{v_p(M_n)=1,\ \operatorname{ord}_p(2)\ge n/t\\p>X}}\log p
 \ \ge\ \left(h-4\alpha-O_\alpha\!\left(\frac{\log\log n}{\log n}\right)\right)
                 nF_n(t) -2D_n-O((\log n)^2).                            \tag{4}
\]

To prove it, take the rows \(d=n/g\) for \(g\mid n\), \(g\le t\). Their totients sum to \(nF_n(t)\). The log mass of the prime powers appearing for the first time at index \(d\) is \(h\varphi(d)+O(\log(2d))\). Indeed Möbius inversion on \(\log(2^m-1)\) gives \(\log\Phi_d(2)=h\varphi(d)+O(1)\), since \(\sum_{m\ge1}|\log(1-2^{-m})|<\infty\). A prime dividing \(\Phi_d(2)\) at an earlier order can occur only to exponent one and must divide \(d\). This follows by Möbius inversion on \(v_p(2^{rj}-1)=v_p(2^r-1)+v_p(j)\) with \(r=\operatorname{ord}_p(2)\). Its contribution is therefore at most \(\log d\) after summing all such primes in the row. There are at most \(\log n\) selected rows. Their primitive log mass is \(h nF_n(t)+O((\log n)^2)\). Each primitive prime belongs to exactly one row. [Mersenne rank and lifting identities](abc_mersenne_short_rank_window.md)

Every prime of exact order \(d\) is \(1\bmod d\). The Brun–Titchmarsh inequality bounds the log mass of all primes of exact order \(d\) through \(X\) by
\[
 \frac{2X\log X}{\varphi(d)\log(X/d)}
  \le \left(4\alpha+O_\alpha\!\left(\frac{\log\log n}{\log n}\right)\right)
             \varphi(d).
\]
Here \(\varphi(n)\gg n/\log\log n\) and \(n/\log n\le d\le n\) give \(\log X=2\log n+O_\alpha(\log\log n)\), \(X>d\) for large \(n\), and \(\log X/\log(X/d)=2+O_\alpha(\log\log n/\log n)\). Finally \(\varphi(d)\ge \varphi(n)/g\ge\varphi(n)/t\) follows by comparing the factors \(1-1/p\) for divisors of \(d\) and \(n\). Hence \(X\le\alpha\varphi(d)^2\). The sieve input is H. L. Montgomery and R. C. Vaughan, *The large sieve*, Mathematika **20** (1973), 119–134.

Subtract this small-prime bound over the selected rows. The entire contribution of primes occurring with exponent \(e\ge2\) in \(M_n\) is at most \(2D_n\), since \(e\le2(e-1)\). The first-occurrence exponent is at most the exponent in \(M_n\). Removing this contribution leaves only simple primes of the required size and order, proving (4). Taking \(t=T_C(n)\) now proves (1), and letting \(\alpha\) increase to \(h/4\) gives the liminf bound.

At \(t=1\), equation (4) isolates the single row of exact order \(n\), with \(nF_n(1)=\varphi(n)\). It gives positive simple-prime mass of order \(\varphi(n)\) along every sequence with \(D_n=o(\varphi(n))\). Mersenne abc gives this condition in particular when \(n/\varphi(n)\) stays bounded.

The prime support in (2) contains information beyond \(n/\varphi(n)\). For any increasing function \(b\ge1\), choose integers \(k\to\infty\) and \(z_k>b(2k)\) large enough that the integer \(n_k=\prod_{z_k<p\le z_k^k}p\) satisfies \(n_k/\varphi(n_k)=(1+o(1))k\). Mertens' theorem permits this choice by first fixing \(k\) and then increasing \(z_k\). Every nontrivial divisor of \(n_k\) exceeds \(b(n_k/\varphi(n_k))\), so \(F_{n_k}(b(n_k/\varphi(n_k)))=\varphi(n_k)/n_k\to0\).

## The factor of two from quadratic reciprocity

The constant in (1) improves to $h/2$ along all indices $n$ with $v_2(n)\ne2$. Equivalently the liminf over these indices is at least $h/2$. To see this, keep only odd coindices $g\le t$. Their totients still sum to at least $nF_n(t)/2$. Indeed write $\gcd(U,n)=2^jG'$ with $G'$ odd. The two factors are independent, $\Pr(j=0)\ge1/2$, and $\Pr(G'\le t)\ge\Pr(2^jG'\le t)$. In the selected rows $d=n/g$ has $v_2(d)=v_2(n)$.

For each of these rows, the order condition eliminates at least half the reduced classes that the congruence $p\equiv1\bmod d$ would permit.

* For $d$ odd, $2$ is a square modulo $p$, so $p\equiv1,7\bmod8$.
* For $d=2u$ with $u$ odd, $p\equiv1,3\bmod8$ is necessary. In the class $7\bmod8$ the order is odd since 2 is a square and $v_2(p-1)=1$. In the class $5\bmod8$ it is divisible by four since 2 is a nonsquare and $v_2(p-1)=2$.
* For $8\mid d$, $p\equiv1\bmod8$ makes 2 a square, so its order divides $(p-1)/2$, giving $p\equiv1\bmod 2d$.

The first two cases each use two reduced classes, with moduli $8d$ and $4d$, respectively. Both moduli have totient $4\varphi(d)$ in their corresponding case. In the last case $\varphi(2d)=2\varphi(d)$. Applying Brun–Titchmarsh to these classes bounds each row's small-prime sum by $(2\alpha+O_\alpha(\log\log n/\log n))\varphi(d)$. The factor of two saved is independent of $d$ and $t$. Subtracting $2D_n$ and the same row errors as in (4) proves (1) with every fixed $\alpha<h/2$ on this set of indices.
