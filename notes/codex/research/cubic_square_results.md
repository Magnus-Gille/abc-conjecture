# Square factors along the cubic orbit of 4

Let $c_n=4^{3^n}$ and $U_n=(c_n^2+c_n+1)/3$, starting at $n=0$.
Write $U_n=D_ns_n^2$ with $D_n$ squarefree. The candidate abc triples are
$(1,c_n-1,c_n)$.

## What the finite search decides

Every prime $p$ dividing $U_n$ is greater than 3. Its multiplicative order
for the base 4 is exactly $3^{n+1}$. Indeed, $c_n^3=1$ modulo $p$, whereas
$c_n=1$ modulo $p$ would imply $p$ divides 3. The converse follows by
factoring $c_n^3-1$. Consequently a prime occurs in at most one layer.

Run `python3 cubic_square_search.py` from this directory. It sieves all
50,847,534 primes through one billion. For each eligible prime it cubes
4 successively modulo $p$, up to the exponent permitted by the power of
3 in $p-1$. At the unique matching index it evaluates the numerator of
$U_n$ modulo $p^2$. There are 32 matching primes and zero square hits.
This bound on primes covers every index. An independent sieve looping
over indices first, checking the order by binary exponentiation and
testing $2^{p-1}$ modulo $p^2$, returned the same 32 pairs and zero hits.
For an odd prime of the required order these square tests agree by lifting
the exponent. The Python program also checks exact small layers and a
positive control, $18^2+18+1=7^3$.

Complete factorizations show that $U_0$ through $U_4$ are squarefree,
including factors above the sieve bound. The eight distinct primes in
$U_4$ are 487, 1459, 139483, 16753783618801, 192971705688577,
3712990163251158343, 10429407431911334611 and 918125051602568899753.
Their product was checked against $U_4$. Each primality check used
the complete factorization of $p-1$, recursively certified down to 2,
and a Lucas witness for each distinct prime divisor of $p-1$.

## Two restrictions on a recurring square

**Two primes must survive to odd exponent.** Put $y=2^{3^n}$. Then

$$U_n=(y^2+y+1)\frac{y^2-y+1}{3}.$$

The second factor is integral since $y=-1$ modulo 3. The factors are
coprime because a common prime would divide $2y$ and also the odd number
$y^2+y+1$, which is coprime to $y$. For $n\ge 1$, the first factor is
strictly between $y^2$ and $(y+1)^2$, and the second is 3 modulo 8.
Each therefore contains a distinct prime to odd exponent. Both primes
are 1 modulo $2\cdot 3^{n+1}$ by the order condition and oddness. Hence

$$D_n\ge (2\cdot3^{n+1}+1)^2\quad(n\ge1).$$

**A fixed polynomial in an earlier orbit value cannot supply a recurring
square divisor.** Fix $r\ge0$ and put $t=2^{3^{n-r}}$ for $n\ge r$.
Then $3U_n=P_r(t)$, where

$$P_r(T)=T^{4\cdot3^r}+T^{2\cdot3^r}+1.$$

This polynomial divides $T^{6\cdot3^r}-1$, which has only simple roots
in characteristic zero. For any nonconstant $G\in\mathbb Z[T]$, divide
$P_r$ by $G^2$ over the rationals and clear denominators to obtain
$aP_r=QG^2+R$ with integer coefficients. The remainder $R$ is nonzero
and has degree less than $2\deg G$. For all sufficiently large $t$,
$0<|R(t)|<|G(t)|^2$. Thus $G(t)^2$ cannot divide $P_r(t)$ or $U_n$
at infinitely many indices. This holds even on an arbitrary subsequence
for each fixed choice of $r$ and $G$.

## Relation to abc

The exact factorization $c_n-1=3^{n+1}\prod_{j<n}U_j$ has pairwise coprime
layers, each coprime to 3. For each layer,
$\log s_j\le\log(U_j/\operatorname{rad}(U_j))\le2\log s_j$.
Since $\log U_j$ grows geometrically and $\log c_n=3^n\log4$,
the triples disprove abc exactly if $s_n\ge U_n^\eta$ for some fixed
$\eta>0$ infinitely often. More explicitly, if $\log s_j=o(3^j)$,
then $\sum_{j<n}\log s_j=o(3^n)$ by bounding the tail by a geometric
sum. If $\log s_j\ge\delta 3^j$ infinitely often, that single term
already accounts for a positive fraction of $\log c_{j+1}$.
The size bound for $D_n$, the polynomial argument, and the prime search
leave this criterion open.
