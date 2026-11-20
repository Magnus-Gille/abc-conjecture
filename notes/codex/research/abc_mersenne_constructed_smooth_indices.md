# An explicit sequence with a subexponential largest Mersenne prime factor

For every odd integer $m\ge1$,
$$
                         P^+(2^{4m}-1)\le e^2\,2^{\varphi(m)}.           \tag{1}
$$
Here $P^+(N)$ denotes the largest prime factor of $N$. In particular every $n\equiv4\bmod 8$ satisfies $P^+(2^n-1)\le e^2\,2^{\varphi(n)/2}$. Taking $m$ to be the product of the odd primes up to $y$ gives an explicit infinite sequence with
$$
 \log P^+(2^n-1)\le
    \left(\frac{e^{-\gamma}\log 2}{2}+o(1)\right)
                      \frac{n}{\log\log n},\qquad n=4m.                 \tag{2}
$$
The construction uses Aurifeuillian factorization. Its proven upper bound remains much larger than the polynomial cutoff in the abc counterexample criterion. [Quadratic cutoff](abc_average_order_radical.md)

## Factoring the cyclotomic values over the integers

For odd $u$ and $\sigma=\pm1$, define
$$
 G_\sigma(u)=2^u+1-\sigma\,2^{(u+1)/2},\qquad
 F_\sigma(u)=\gcd\big(\Phi_{4u}(2),G_\sigma(u)\big).
$$
The two $G$'s have product $2^{2u}+1$. They are odd and their difference is a power of two, hence they are coprime. Since $\Phi_{4u}(2)$ divides this product, its two positive integer factors are exactly $F_+(u)$ and $F_-(u)$.

Let $\chi(t)=(2/t)$, equal to $+1$ for $t\equiv1,7\bmod8$ and $-1$ for $t\equiv3,5\bmod8$. For odd $u,t$ the factors satisfy
$$
                        G_\sigma(u)\mid G_{\sigma\chi(t)}(ut).          \tag{3}
$$
Indeed put $Y=2^u$. Modulo $G_\sigma(u)$ one has $Y^2=-1$ and $1+Y=\sigma\,2^{(u+1)/2}$. For the four odd classes of $t\bmod8$, substitution of $Y^2=-1$ gives $1+Y^t=\chi(t)Y^{(t-1)/2}(1+Y)$. This proves (3) since $Y^{(t-1)/2}2^{(u+1)/2}=2^{(ut+1)/2}$.

Now $2^{2m}+1=\prod_{u\mid m}\Phi_{4u}(2)$. By (3), each factor $F_\sigma(u)$ belongs wholly to $G_{\sigma\chi(m/u)}(m)$. The two latter numbers are coprime, so the product identity gives the identity on each sign separately. Möbius inversion therefore yields
$$
  G_\sigma(m)=\prod_{t\mid m}F_{\sigma\chi(t)}(m/t),\qquad
  F_\sigma(m)=\prod_{t\mid m}G_{\sigma\chi(t)}(m/t)^{\mu(t)}.           \tag{4}
$$
For example $F_+(5)=25/5=5$ and $F_-(5)=41/1=41$, giving $\Phi_{20}(2)=205=5\cdot41$.

## Bounding the two factors

With $v=2^{-(u-1)/2}\in(0,1]$ we have $G_\sigma(u)/2^u=1-\sigma v+v^2/2$. The inequalities $1+v+v^2/2\le e^v$ and $e^{-v}\le1-v+v^2/2\le1$ give
$$
                       |\log G_\sigma(u)-u\log 2|\le v .
$$
Sum this error after taking logs in (4). The full sum over positive odd $u$ is $\sum_{j\ge0}2^{-j}=2$, whereas $\sum_{t\mid m}\mu(t)m/t=\varphi(m)$. Thus
$$
                    |\log F_\sigma(m)-\varphi(m)\log 2|\le2.            \tag{5}
$$

Every divisor of $4m$ has the form $u,2u$ or $4u$ with $u\mid m$. The order-$4u$ cyclotomic factors split as above. For the others use the elementary bound $\log\Phi_d(2)\le\varphi(d)\log2+2$. Indeed Möbius inversion on $\log(2^j-1)$ gives an error of absolute value at most $\sum_{j\ge1}-\log(1-2^{-j})\le\sum_{j\ge1}2^{1-j}=2$. Also $\varphi(2u)=\varphi(u)\le\varphi(m)$ by the prime-power totient formula. Every prime of $2^{4m}-1$ occurs in a factor bounded by $e^2\,2^{\varphi(m)}$, proving (1).

For $m=\prod_{3\le p\le y}p$, Mertens' product theorem gives $\varphi(m)/(4m)\sim e^{-\gamma}/(2\log y)$, and the prime number theorem gives $\log(4m)\sim y$. This proves (2). For any fixed $c>0$, one also gets $P^+(2^n-1)\le e^{cn}$ on a set of positive natural density. Choose one odd primorial $m_0$ with $(\log 2)\varphi(m_0)/(4m_0)<c$. Apply (1) to $n=4m$ for all sufficiently large odd multiples $m$ of $m_0$.
