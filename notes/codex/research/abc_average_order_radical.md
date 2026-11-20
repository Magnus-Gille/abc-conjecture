# Small primes in the radicals of differences of powers

Fix coprime integers $A>B\ge1$ and put $V_n=A^n-B^n$. For $X\ge2$ let
$$
 B_X(n)=\sum_{\substack{p\mid V_n\\p\le X}}\log p,\qquad
 \delta=1-\frac{1+\log\log 2}{\log 2}=0.0860713\ldots .
$$
For every fixed $0\le a<\delta$, put $W_n=n^2(\log n)^a$ for $n\ge2$. Then **unconditionally**
$$
                       B_{W_n}(n)/n\longrightarrow 0
                       \quad\text{in natural density}.                    \tag{1}
$$
Convergence in density means that for each $\eta>0$, the fraction of indices up to $N$ where the ratio exceeds $\eta$ tends to zero. All logs are natural. The primes counted by $B_X$ occur once in the sum regardless of their exponent in $V_n$.

Two implications address different routes to a counterexample.

* Suppose that for infinitely many $N$ there are $\gg N/(\log N)^\rho$ indices $N<n\le2N$ with $P^+(V_n)\le W_n$, for some fixed $0\le\rho<(\delta-a)/2$. Then the abc quality of $B^n+V_n=A^n$ tends to infinity along a subsequence.
* Suppose that on a set of positive upper density, $V_n$ has no prime $p>W_n$ that both occurs to exponent one and has multiplicative order $\operatorname{ord}_p(A/B)=n$. This also implies a fixed-exponent disproof of abc, even when earlier terms have large prime factors. Indeed, assuming abc, primes satisfying **all three** conditions carry $(1+o(1))\varphi(n)\log A$ in logarithmic mass in density.

Neither hypothesis is established. A finite test for $A=2,B=1,a=0$ appears below.

## The weighted order estimate

For $p\nmid AB$ let $r_p=\operatorname{ord}_p(AB^{-1}\bmod p)$, including $r_2=1$ when $A$ and $B$ are odd. Since $p\mid V_n$ exactly when $r_p\mid n$, one has the exact identity
$$
   \sum_{n\le N}B_X(n)
       =\sum_{\substack{p\le X\\p\nmid AB}}\left\lfloor\frac{N}{r_p}\right\rfloor\log p
       \le N S(X),\qquad S(X)=\sum_{\substack{p\le X\\p\nmid AB}}\frac{\log p}{r_p}. \tag{2}
$$
For every $0<b<\delta/2$,
$$
                     S(X)\ll_{A,b}\sqrt X/(\log(2X))^b.                  \tag{3}
$$
Consider the primes $x/2<p\le x$ and put $Z=(\log x)^b$. At each order $r\le\sqrt x/Z$ the product of all primes of that order divides $V_r$. Dividing its log by $r$ costs at most $\log A$ per order. At orders $r>\sqrt x Z$, Chebyshev's bound $\sum_{p\le x}\log p\ll x$ gives a total $O(\sqrt x/Z)$. The intermediate primes have a divisor $r_p$ of $p-1$ in $[\sqrt x/Z,\sqrt x Z]$. Their number is $O_{b,d}(x/(\log x)^{1+d})$ for every $2b<d<\delta$ by the rectangular sieve. Each weight is at most $Z\log x/\sqrt x$, giving $O(\sqrt x/Z)$ again. Sum over dyadic prime intervals to get (3). The proof of the shifted-prime estimate uses Brun–Titchmarsh, a truncated inclusion-exclusion in two variables, and Mertens' estimate. A shorter one-variable argument suffices throughout if $\delta$ is replaced by $1-(e/2)\log 2$. [Rectangular sieve](abc_shifted_prime_rectangular_sieve.md) · [One-variable argument](abc_balanced_shifted_primes.md)

Take $X=(2N)^2(\log(2N))^a$. By monotonicity and (2)–(3),
$$
          \sum_{N<n\le2N} B_{W_n}(n)
             \ll_{A,a,b} \frac{N^2}{(\log N)^{b-a/2}}.                  \tag{4}
$$
Choosing $b>a/2$ and applying Markov's inequality proves (1) on doubling intervals and hence up to $N$ by geometric summation. If such an interval has $\gg N/(\log N)^\rho$ smooth indices, take $a/2+\rho<b<\delta/2$. At least one of them has $\log\operatorname{rad}(V_n)/n\ll(\log N)^{\rho+a/2-b}$, which tends to zero. The triple is primitive and its radical equals $\operatorname{rad}(AB)\operatorname{rad}(V_n)$, so its quality $n\log A/\log\operatorname{rad}(ABV_n)$ tends to infinity on a subsequence. In particular $A^n/\operatorname{rad}(ABV_n)^2$ would already be unbounded for the single fixed exponent $\varepsilon=1$.

## What abc would require at the exact order

Let $D_n=\log(V_n/\operatorname{rad}(V_n))$. The abc inequalities on this family imply $D_n=o(n)$ by applying them for each fixed $\varepsilon>0$ and using $\log V_n=n\log A+o(1)$. All powers $p^e$ in $V_n$ with $e\ge2$ together have logarithmic mass at most $2D_n$, since $e\le 2(e-1)$. Thus under abc, primes bigger than $W_n$ occurring exactly once in the whole $V_n$ account for $(1+o(1))n\log A$ in density.

To localize to exact order $n$, let $L_n$ be the log of the product of the prime powers in $V_n$ whose primes have order $n$. Then
$$
                    L_n=\varphi(n)\log A+O_{A,B}(\log(2n)).             \tag{5}
$$
Indeed $\log\Phi_n(A,B)=\varphi(n)\log A+O_{A,B}(1)$ follows by Möbius inversion and the convergence of $\sum_{j\ge1}|\log(1-(B/A)^j)|$. For odd $p$ of order $r$, lifting gives $v_p(V_{rj})=v_p(V_r)+v_p(j)$. Inverting over divisors shows that $p$ contributes to $\Phi_n(A,B)$ only for $n=r$ and $n=rp^k$ with $k\ge1$, at which latter indices its exponent is one. These imprimitive contributions are bounded by $\log n$. If $A,B$ are odd, the prime 2 contributes at $n=1,2$ and at higher powers of two with exponent one, by the even-prime lifting formula. This establishes (5), including its fixed small-index exceptions in the error term.

Define $G_n$ as the sum of $\log p$ over the simple primes $p>W_n$ of exact order $n$. Then
$$
                 L_n-B_{W_n}(n)-2D_n\le G_n\le L_n.                    \tag{6}
$$
The factor $n/\varphi(n)$ is bounded in mean, since
$$
 \frac1N\sum_{n\le N}\frac n{\varphi(n)}
 \le\sum_{d\ge1}\frac{\mu^2(d)}{d\varphi(d)}
 =\prod_p\left(1+\frac1{p(p-1)}\right)<\infty .
$$
Here we used $n/\varphi(n)=\sum_{d\mid n}\mu^2(d)/\varphi(d)$. Given $\eta>0$, all but at most $\eta N$ indices have $n/\varphi(n)$ bounded by a constant depending only on $\eta$. Multiplying a sequence tending to zero in density by $n/\varphi(n)$ therefore preserves convergence to zero in density. Under abc this applies to $(B_{W_n}(n)+2D_n)/n$. Equations (5)–(6) now prove $G_n/\varphi(n)\to\log A$ in density. Consequently, if $G_n=0$ on a set of positive upper density, abc fails on this family for some fixed $\varepsilon>0$.

## Multiplicity required by positive-density smoothness

For $A=2,B=1$ the proposed smoothness condition makes a further unconditional prediction. Suppose $P^+(2^n-1)\le W_n$ on a set of positive upper density. Fix $0<\gamma<(\delta-a)/2$. On unbounded doubling intervals there must be $\gg N$ **distinct** primes $p\ll N^2(\log N)^a$ with
$$
 N<\operatorname{ord}_p(2)\le 2N,\qquad
                       v_p(2^{p-1}-1)\gg(\log N)^\gamma.                \tag{7}
$$
The constants can depend on the upper density and the fixed exponents. To see this, choose intervals $N<n\le2N$ in which a fixed positive fraction are smooth. Take $b>a/2+\gamma$ in (4). Markov's inequality excludes only $o(N)$ indices when imposing $B_{W_n}(n)\le n/(\log n)^\gamma$. The mean bound for $n/\varphi(n)$ permits the further restriction $\varphi(n)\gg n$ after sacrificing an arbitrarily small fixed fraction. By (5), the exact-order prime powers then have log mass $\gg n$, whereas their distinct primes have log mass at most $n/(\log n)^\gamma$. At least one exponent is $\gg(\log n)^\gamma$. For its prime, lifting gives $v_p(2^{p-1}-1)=v_p(2^n-1)$ because $n\mid p-1$ and $p\nmid(p-1)/n$. Different indices supply different primes by their exact orders. This establishes (7). No such supply of high valuations has been proved here.

## A test with complete coverage through 10,000

For $2\le n\le10{,}000$, precisely the following 20 indices have $P^+(2^n-1)\le n^2$:
$$
 2,\ 3,\ 4,\ 6,\ 8,\ 9,\ 10,\ 11,\ 12,\ 14,\ 15,\ 18,\ 20,\ 21,\ 24,\ 28,\ 30,\ 36,\ 48,\ 60 .
$$
Testing the primes of exact order $n$ alone adds three indices, $52,102,156$. The earlier-order primes $8191,131071,121369$, respectively, exceed the whole-term cutoff in these cases. The exact-order row at $n=6$ is empty. To certify the range, the program forms $\Phi_n(2)$, removes its prime factors dividing $n$, and strips every possible prime $p\le n^2$ in the class $1\bmod n$. A residual factor greater than one certifies a prime above $n^2$ without requiring its factorization. The whole term is tested whenever the exact-order row gives no such certificate. An independent enumeration by modular powering, trial primality and Möbius inversion reproduced both lists. [All-index census](abc_mersenne_all_indices_scan.py)

A separate verifier checks (2) by exact integer products for five pairs $A,B$ on 120 combinations of ranges, cutoffs and bases. At $n\le1000$, $p\le100{,}000$, it independently obtains 654 distinct primes and 5,407 incidences for $2^n-1$. These finite checks verify the arithmetic used in the experiment. The density bounds follow from the proof. [Exact counting identity](abc_average_order_check.py)
