# A Bombieri–Vinogradov bound for the radical on the elliptic slice

There are absolute constants $c>0$ and $D>0$ and a single infinite sequence of primitive positive triples
\[
              U^2+3V^2=W^{12},\qquad C=W^{12},\qquad R=\operatorname{rad}(3UVW)
\]
for which
\[
 \frac C R\gg\sqrt{\log C}\,
       \exp\!\left(c\,\frac{(\log_3 C)^{4/3}}{(\log_4 C)^D}\right).
 \tag{1}
\]
Here $\log_1 t=\log t$ and $\log_{j+1}t=\log(\log_j t)$, using natural logarithms. In particular every fixed exponent below $4/3$ can replace $4/3$ in (1) with the denominator omitted for sufficiently large members of the same sequence. The primes producing the gain arise in the actual radical on the original rank-one slice. [Slice parametrization and denominator identities](abc_eisenstein_twelfth_elliptic_slice.md)

## The order and the local gains

On $E:Y^2=X^3+36X^2+36X$ use $P=(-2,8)$ and write $B_n$ for the positive square root of the reduced denominator of $X(nP)$. For odd $n\ge3$, write $X(nP)=-2(x/y)^2$ with coprime positive $x,y$. The slice supplies an integer $D_n$ divisible by $|x^2-y^2|$ and satisfying
\[
   \log C\asymp n^2,\qquad C/R\gg D_n/\operatorname{rad}(D_n).
\]
Indeed $C\asymp\max(x,y)^{24}$, $D_n\ll\max(x,y)^{24}$, and its radical agrees with $R$ away from 2 and 3. At each good prime $p\ge5$ one has
\[
              v_p(x^2-y^2)=v_p(B_{n-1})+v_p(B_{n+1}).
\]
The map $X$ is unramified at $\pm P$ at these primes since $2Y(P)=16$ is a unit. [Local calculations on the slice](abc_eisenstein_twelfth_elliptic_slice.md)

Let $Y$ tend to infinity, set $k=\operatorname{lcm}(1,\ldots,\lfloor Y\rfloor)$ and take $n=2\cdot3^k-1$. At 3, $X(3P)=-242/9$ puts $3P$ at formal depth one. Multiplication by $2\cdot3^{k-1}$ puts $(n+1)P$ at depth at least $k$. Translating to $-P$ gives $v_3(X(nP)+2)\ge k-O(1)$ and $y$ is a 3-adic unit. This gives $v_3(x^2-y^2)\ge k-O(1)$ and a factor $\gg3^k\asymp n$ in $D_n/\operatorname{rad}(D_n)$.

We use primes $p\equiv7\bmod12$. The rational 2-isogenous curve has model $v^2=u^3-576u$. For $p\equiv3\bmod4$ its trace is zero by pairing $u$ with $-u$ in the quadratic character sum. Thus if $M_p$ denotes Frobenius on a prime-to-$p$ Tate module, the determinant needed for the group order is
\[
        \det(1-M_p)=1-\operatorname{tr}(M_p)+\det(M_p)=1-0+p=p+1.
\]
In particular $\operatorname{ord}_p(P)\mid p+1$ and $3\nmid p+1$.

Suppose $p-1$ is the product of two coprime positive integers at most $Y$, and the same holds for $p+1$. The first factorization gives $p-1\mid k$, hence $p\mid3^k-1$. Both factors of $p+1$ are prime to 3. Each of their Euler totients is at most $Y$ and divides $k$, so both factors divide $3^k-1$. Their coprimality gives $p+1\mid3^k-1$. Since $(p,p+1)=1$,
\[
          p\,\operatorname{ord}_p(P)\mid n-1=2(3^k-1).
\]
The first multiple at the reduction order is in the formal group. The additional multiple $p$ raises its depth by at least one, proving $p^2\mid B_{n-1}$ and $p^2\mid D_n$. Each such prime therefore supplies its own factor $p$ in $D_n/\operatorname{rad}(D_n)$, independently of the factor at 3.

## Two shifted factorizations at the distribution endpoint

We use Bombieri–Vinogradov for the Chebyshev function $\vartheta(u;m,a)$ of rational primes in the residue class $a\bmod m$. Take $b_4>0$ large enough that
\[
 \sum_{m\le T^{1/2}/(\log T)^{b_4}}
 \max_{(a,m)=1}\max_{u\le T}
 \left|\vartheta(u;m,a)-\frac{u}{\varphi(m)}\right|
       \ll\frac{T}{(\log T)^4}.
 \tag{2}
\]
The usual theorem for the von Mangoldt function gives this version on enlarging $b_4$, since prime powers of exponent at least two have weight $O(T^{1/2}\log^2 T)$ per modulus. [Iwaniec and Kowalski, *Analytic Number Theory*, Chapter 17](https://doi.org/10.1090/coll/053)

Fix $B>2b_4/3$ and write
\[
       T=\frac{Y^{4/3}}{(\log Y)^B},\qquad Z=T/Y,\qquad I=[2Z,4Z].
\]
Count $T/2<p\le T$, with weight $\log p$, subject to $p\equiv7\bmod12$, $q\mid p-1$ and $r\mid p+1$ for ordered distinct primes $q,r\in I$. For large $Y$ all of $12,q,r$ are pairwise coprime. The three congruences fix one reduced residue modulo $m=12qr$, whose Euler totient is exactly $4(q-1)(r-1)$. Equivalently the diagonal congruence lattice in the three residue coordinates has determinant $12qr$, and the Chinese remainder map from the single $p$ coordinate is surjective. The modulus satisfies
\[
  m\le192 Z^2,\qquad
  \frac{192Z^2(\log T)^{b_4}}{\sqrt T}
     =\frac{192T^{3/2}(\log T)^{b_4}}{Y^2}
     \ll(\log Y)^{b_4-3B/2}=o(1).
\]
Thus (2) applies even though the residue class varies with the ordered pair. Each modulus occurs for at most two ordered pairs, by unique factorization of $m/12$. Passing from $[1,T]$ to $(T/2,T]$ costs another factor of at most two in the error. The sum over pairs is consequently
\[
 \frac{T}{8}\left[
       \left(\sum_{q\in I}\frac1{q-1}\right)^2
          -\sum_{q\in I}\frac1{(q-1)^2}\right]
      +O\!\left(\frac T{(\log T)^4}\right)
        \asymp \frac T{(\log T)^2},                         \tag{3}
\]
where both sums are over primes. The prime number theorem and partial summation give the first inner sum asymptotic to $\log 2/\log Z$; the second is $O(1/(Z\log Z))$. Also $\log Z\sim(\log T)/4$. This is why averaging over a fixed multiplicative interval at the endpoint costs two logarithms in prime weight.

A prime $p$ occurs only $O(1)$ times in (3). For all large $Y$, each eligible $q,r$ exceeds $T^{1/5}$, so each of $p-1,p+1$ has at most five such distinct prime factors. Discard primes for which $s^2\mid p-1$ or $s^2\mid p+1$ for some prime $s\in I$. The number discarded is at most $O(T/Z+Z)$ by summing the elementary residue-class count $T/s^2+1$. Even with the bounded multiplicity and the factor $\log T$, their contribution is $o(T/(\log T)^2)$.

Every retained prime has a factorization $p-1=q((p-1)/q)$ into coprime factors at most $Y$. Indeed $q\le4Z<Y$ and the cofactor is at most $Y/2$. Likewise $p+1=r((p+1)/r)$ has coprime factors at most $Y$, since $(T+1)/(2Z)<Y$ for large $Y$. Removing the multiplicity in (3) leaves a set $\mathcal P_Y$ with
\[
             \sum_{p\in\mathcal P_Y}\log p
                    \gg T/(\log T)^2
                    \gg \frac{Y^{4/3}}{(\log Y)^{B+2}}.       \tag{4}
\]

For a finite check of the divisibility step, take $Y=1000$, $T=10000$ and $I=[20,40]$. The prime $p=9547\equiv7\bmod12$ has $p-1=37\cdot258$ and $p+1=31\cdot308$, with both pairs coprime. Direct modular exponentiation gives $3^{\operatorname{lcm}(1,\ldots,1000)}\equiv1\bmod 9547\cdot9548$. The prime 9859 likewise uses $9858=31\cdot318$ and $9860=29\cdot340$. These examples illustrate the local step with the chosen finite interval; formula (3) supplies the asymptotic endpoint count.

## Conversion to the triple height

The local gains give $C/R\gg 3^k\prod_{p\in\mathcal P_Y}p$. Since $\log C\asymp n^2$ and $n=2\cdot3^k-1$, one has $3^k\asymp\sqrt{\log C}$ and
\[
   \log_2 C=2\log n+O(1)=2k\log3+O(1),\qquad
   \log_3 C=\log k+\log(2\log3)+o(1).
\]
The logarithm of the least common multiple is the Chebyshev function $\psi(Y)\sim Y$. Hence $\log_3 C\sim Y$ and $\log_4 C\sim\log Y$. Substituting (4) proves (1) with $D=B+2$. The index and the height tend to infinity, so the sequence contains infinitely many distinct triples. The earlier least-common-multiple construction and (1) mark primes only at subpower scale in $C$. [Earlier construction and its scope](abc_eisenstein_twelfth_elliptic_slice.md)
