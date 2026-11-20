# A quadratic prime-factor test for Mersenne abc counterexamples

Put $M_n=2^n-1$ and $R_n=2\operatorname{rad}(M_n)$. At a prime-power index $n=q^k$ let $P_n$ be the largest prime divisor of $\Phi_n(2)$. This is the largest prime appearing for the first time at index $n$. Rational abc on $1+M_n=2^n$ implies
$$
        \liminf_{q^k\to\infty}\frac{P_{q^k}}{\varphi(q^k)^2}
                 \ \ge\ \frac{\log 2}{2}.
$$
Thus an infinite sequence below any fixed smaller constant would disprove rational abc. There is also a sufficient smoothness condition on unrestricted indices below. The computations in this note do not exhibit either infinite sequence.

## Counting primes of the specified order

For $n=q^k$, the quotient $\Phi_n(2)=(2^n-1)/(2^{n/q}-1)$ is $1$ modulo $q$ (for odd $q$ use $2^{q^{k-1}}\equiv 2\pmod q$; it is odd at $q=2$). Every prime divisor $p$ therefore has exact order $n$: if the order divided $n/q$, the sum of the $q$ terms in the geometric series would be $q$ modulo $p$.

Such primes have $p\equiv1\pmod n$ with an additional restriction. For odd $n$, the element 2 has odd order and hence is a square modulo $p$. Thus $p\equiv1$ or $7\pmod8$, and there are just two reduced classes modulo $8n$. For $n=2^k\ge8$, the first congruence already gives $p\equiv1\pmod8$, hence 2 is a square. Its order divides $(p-1)/2$, so $p\equiv1\pmod{2n}$.

Fix $\alpha>0$ and set $X=\alpha\varphi(n)^2$. The Brun–Titchmarsh inequality bounds the number of primes in a reduced class modulo $m<X$ by $2X/(\varphi(m)\log(X/m))$. Use $m=8n$ and two classes in the odd case, $m=2n$ and one class otherwise. Multiplying by $\log X$ yields in both cases
$$
 \sum_{\substack{p\mid\Phi_n(2)\\p\le X}}\log p
     \ \le\ \frac{X\log X}{\varphi(n)\log(X/m)}
      =(2+o(1))\alpha\varphi(n).
$$
The error is uniform over prime powers since $n/2\le\varphi(n)<n$. On the other hand $\log\Phi_n(2)=\varphi(n)\log2+O(1)$. Hence if $P_n\le X$, then
$$
 \log\frac{M_n}{\operatorname{rad}(M_n)}
 \ \ge\ \log\frac{\Phi_n(2)}{\operatorname{rad}(\Phi_n(2))}
 \ \ge\ (\log2-2\alpha-o(1))\varphi(n).                          \tag{1}
$$
For $\alpha<(\log2)/2$ this gives a fixed positive proportion of $n$ on the right, exactly what a counterexample subsequence needs. For instance at $\alpha=(\log2)/4$ the limiting lower bound on the quality $n\log2/\log R_n$ on such a sequence is $4/3$. Equivalently, if abc holds on these inputs, primes above $\alpha\varphi(n)^2$ occurring to exponent one must contribute at least $(\log2-2\alpha-o(1))\varphi(n)$ in log mass to $\Phi_n(2)$: the total mass from powers of exponent at least two is at most twice the excess in $M_n$, which is $o(n)$ under this hypothesis. The sieve used here is H. L. Montgomery and R. C. Vaughan, *The large sieve*, Mathematika **20** (1973), 119–134.

## An absolute cutoff for the whole radical at prime powers

For each prime $q$ and real $X\ge2$,
$$
  \sum_{\substack{p\le X\\ \operatorname{ord}_p(2)=q^j\ \text{for some } j\ge1}}
       \log p\le 5\sqrt X .
$$
Choose $m\in\{1,q,q^2,\ldots\}$ nearest on the logarithmic scale to $u=\sqrt{8X/((q-1)\log2)}$. If $u<1$ then $q>X$ and the sum is empty. Otherwise $1/\sqrt q\le m/u\le\sqrt q$. All primes of orders up to $m$ together divide $2^m-1$, at a cost of at most $m\log2$. All remaining orders are multiples of $d=qm$, so their primes are $1\pmod d$.

If $d\le X^{3/4}$, Brun–Titchmarsh bounds this latter cost by $8X/\varphi(d)=8X/((q-1)m)$. Adding the two bounds gives at most
$$
 \sqrt{8X\log2}\,\frac{\sqrt q+1/\sqrt q}{\sqrt{q-1}}\le6\sqrt{X\log2}<5\sqrt X .
$$
The ratio squared is $(q+1)^2/(q(q-1))$, largest at $q=2$. If $d>X^{3/4}$, the congruence alone bounds the large-order cost by $(X/d)\log X\le(4/e)\sqrt X$. The small-order cost is at most $4\sqrt{X\log2}$ by $m\le u\sqrt q$, which again gives the claim.

In particular, if the largest prime of the **entire** $M_n$ satisfies $P^+(M_n)/n^2\to0$ on a sequence of prime powers, then $\log R_n=o(n)$ and the abc quality tends to infinity.

## Unrestricted indices

For **each** fixed $a>0$, infinitely many $n$ with
$$
                         P^+(M_n)\le \frac{n^2}{(\log n)^a}             \tag{2}
$$
would suffice for a fixed-exponent disproof. Here the hypothesis is on the largest prime of the entire $M_n$. To see this, take $y=\log n$, $0<b<a/2$, and consider ranks $d\mid n$ with coindex $n/d\le y^b$. A fixed positive fraction (depending only on $b$) of the totient weight $\sum_{d\mid n}\varphi(d)=n$ lies in these ranks, uniformly for large $n$.

Indeed, choose $U$ uniformly modulo $n$ and let $G=\gcd(U,n)$. Then $\Pr(n/G=d)=\varphi(d)/n$. Write $G$ as the product of the prime powers from primes at most $z=y^{b/2}$ and those from primes above $z$. The two portions are independent by CRT. The mean logarithm of the first is at most $\sum_{p\le z}(\log p)/(p-1)=\log z+O(1)$, giving probability at least $1/2-o(1)$ that it is at most $y^b$. The probability that the second portion is 1 is at least $\min(1,b/2)-o(1)$, by Mertens' product theorem on $(z,y]$ and $\sum_{p\mid n,\,p>y}1/p=o(1)$. This proves the positive-fraction assertion.

At rank $d$ the total first-occurrence prime-power mass is $\varphi(d)\log2+O(1+\log d)$. Use $\log\Phi_d(2)=\varphi(d)\log2+O(1)$ by Möbius inversion. Its imprimitive prime factors occur to exponent one and divide $d$, as in the [rank calculation](abc_mersenne_short_rank_window.md). The error summed over any collection of divisors of $n$ is $O(\tau(n)\log(2n))=o(n)$. The selected ranks therefore contribute at least $c_b n$ in total log mass for some $c_b>0$ depending only on $b$.

Now put $X=n^2/y^a$. The log mass from distinct primes **up to $X$** in all selected ranks together is, by Brun–Titchmarsh and $p\equiv1\pmod d$,
$$
 \ll X\sum_{\substack{d\mid n\\ n/d\le y^b}}\frac1{\varphi(d)}
 \ll \frac{X\log\log(3n)}n\sum_{j\le y^b}j=o(n).
$$
Here $\log X/\log(X/d)$ is bounded for all these $d$ and large $n$. Under (2) the difference between the two masses is a fixed positive fraction of $n$ coming from repeated prime factors, so (1)'s conclusion about a counterexample subsequence follows. No hypothesis is imposed on the number of prime factors of $n$.

## Exact check through 10,000

For all 1,280 prime-power indices $2\le n\le10000$, the minimum of $P_n/\varphi(n)^2$ is **$89/100$ at $n=11$**. At 1,274 indices the verifier certifies $P_n>n^2$; the six exceptions are fully factored below.

| $n$ | $\Phi_n(2)$, factored |
|---:|---:|
| 2 | 3 |
| 3 | 7 |
| 4 | 5 |
| 8 | 17 |
| 9 | 73 |
| 11 | $23\cdot89$ |

The program computes the cyclotomic quotient exactly, tests the candidates $p\le n^2$ in the order congruence, and removes all such prime powers. A residual integer greater than one certifies the existence of a larger prime divisor without factoring that residual. Complete trial factorization of $2^n-1$ supplies a separate check through $n=25$. Run `python3 abc_mersenne_quadratic_prime_scan.py` from this directory. [Verifier](abc_mersenne_quadratic_prime_scan.py)
