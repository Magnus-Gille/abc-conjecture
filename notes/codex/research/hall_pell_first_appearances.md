# Can a prime first appear squared in a Pell quadratic?

For $n=7+12j$, $j\ge0$, put $t_n=L_n-11$, $z_n=F_n$, $A_n=(L_n-6)^2-20$, $B_n=(L_n-9)^2-5$ and $M_n=t_nz_nA_nB_n$. A prime first appears at $n$ if $p\mid M_n$ and $p\nmid M_m$ at every earlier index in the progression. The associated primitive abc triple has height $c=A_n^3$ and radical $R=\operatorname{rad}(30M_n)$. Infinitely many indices with $p^2\mid A_nB_n$ and $\log p\ge\delta n$ for fixed $\delta>0$ would disprove abc. The shared-divisor bound implies that such a prime would first appear at $n$ for all sufficiently large indices. [Construction](hall_pell_direction.md) · [Shared-divisor bound](hall_pell_shared_divisors.md)

## Three exhaustive checks

| Domain | Result |
|---|---|
| Every prime, all 18 indices from $7$ through $211$ | The only repeated prime in $A_nB_n$ is $31^2\mid A_{163}$. Already $31\mid A_{19}$. |
| $p\le10^9$, all 1,667 indices through $19{,}999$ | There are 47 pairs $(p,n)$ with $p^2\mid A_nB_n$, using nine primes. All nine appeared at earlier indices. |
| $p\le10^8$, all indices with no upper bound on $n$ | No prime first appears squared in either quadratic. |

There is a stronger numerical conclusion valid at every index. Whenever $p\le10^8$ and $p^2\mid A_nB_n$,

$$\frac{p}{n}\le\frac{42961}{56827}=0.755996\ldots.$$

The upper bound is attained. The seven rows below give every square hit with $p\le10^8$ and $0\le j<p$. Each listed valuation is exactly two, checked modulo $p^3$. If $j\ge p$ then $p/n<1/12$, which certifies the global maximum. The fourth column gives the earliest occurrence of that prime in any of the four factors.

| $p$ | $n$ with a square | Factor | First index and factor |
|---:|---:|---|---|
| 29 | 223 | $A$ | 19, $t$ |
| 31 | 163 | $A$ | 19, $A$ |
| 59 | 523 | $B$ | 67, $B$ |
| 641 | 2,035 | $B$ | 115, $B$ |
| 42,961 | 56,827 | $B$ | 10,735, $t$ |
| 1,554,559 | 6,523,831 | $B$ | 305,599, $B$ |
| 38,611,649 | 225,992,239 | $A$ | 57,917,467, $t$ |

In the second range the primes are $29,31,41,59,79,101,269,641,881$. Three valuations exceed two. The valuation of $A_n$ is three at $(n,p)=(2023,31),(5095,29),(19339,31)$. These 47 hits also agree with the earlier independent computation of all square classes for primes up to $10{,}000$. [Earlier square classes](hall_pell_classes.csv)

The quantity relevant to an exponential-size prime admits an exact maximum over the larger prime range. For all $p\le10^9$ and all indices with $p^2\mid A_nB_n$,

$$\frac{\log p}{n}\le\frac{\log31}{163}\simeq0.0210674.$$

For $n\le19{,}999$ the comparisons reduce to the integer inequalities $p^{163}\le31^n$ for the 47 hits. The equality occurs only at $(p,n)=(31,163)$. For all larger indices use $p\le10^9$ and $(10^9)^{163}<31^{20000}$.

For the first range, each prime factor of each of $t_n,z_n,A_n,B_n$ was checked using both FLINT and PARI, and each factorization multiplied back to the original integer. At $n=163$ the full abc quality $\log c/\log R$ is about $1.010925$. Its maximum over these 18 indices is about $1.128519$ at $n=7$, where $c=131872229$ and $R=15682290$. Exact integer comparisons give $c^{10}>R^{11}$ only at $n=7$, which certifies the maximum without a floating-point comparison. The full radical computation ends at $211$. At $223$, $29^2\mid A_{223}$ is certified, and the complete factorization of its remaining 89-digit composite cofactor was not obtained here. [Complete early factorizations](hall_pell_early_factors.jsonl)

For the second range let $P$ be the product of the primes up to $10^9$. For each $H=A_nB_n$ compute $D=\gcd(H,P)$. Then $\gcd(D,H/D)$ is exactly the product of the primes up to $10^9$ whose squares divide $H$. Computing $P$ modulo a product tree of the integers $H$ gives all these gcds with one primorial. The quadratics are coprime on this progression. Direct division gives the valuations once a repeated prime is found. [Census and verification code](hall_pell_square_census.py)

## A prime-by-prime criterion valid at arbitrarily large indices

For $p\ge7$ a divisor of $A_nB_n$ requires $5$ to be a square modulo $p$. The primes 2 and 3 divide neither quadratic, and 5 occurs to exponent one in $B_n$. Choose a square root $s$ of 5 modulo $p^2$ and let $\alpha=(1+s)/2$ there. For odd $n$ one has $L_n=\alpha^n-\alpha^{-n}\pmod{p^2}$. For $A$ the two target values of $L_n$ are $u=6\pm2s$, and for $B$ they are $u=9\pm s$. For each target take the roots $\beta$ of $X^2-uX-1$ modulo $p^2$. All existing roots modulo $p$ lift uniquely, since the products of the conjugate discriminants are 720 and 6480 respectively. The condition $p^2\mid A_nB_n$ is exactly $\alpha^n=\beta\bmod p^2$ for at least one target root.

For a unit $v$ modulo $p^2$ write $q_p(v)=(v^{p-1}-1)/p\bmod p$. The Fermat quotient adds under multiplication. If $v=1+ph$ then $q_p(v)=-h\bmod p$, by the binomial theorem. It follows that

$$\alpha^n=\beta\bmod p^2\quad\Longleftrightarrow\quad
  \alpha^n=\beta\bmod p\quad\text{and}\quad n q_p(\alpha)=q_p(\beta)\bmod p.$$

If $q_p(\alpha)\ne0$, the second equation determines **one candidate** $0\le j<p$ per root, namely

$$j=\frac{q_p(\beta)-7q_p(\alpha)}{12q_p(\alpha)}\bmod p.$$

Testing the first equation then decides whether this candidate is a square hit. If $q_p(\alpha)=0$, one can check the first $p$ index residues directly. No split prime in the checked range had zero $q_p(\alpha)$. The two roots for one $u$ are $\beta,-1/\beta$ and have opposite Fermat quotients.

The step $\alpha^{12}$ modulo $p$ has order dividing $h=(p-1)/\gcd(12,p-1)$. All four factors modulo $p$ are functions of $\alpha^n$ on the progression. Therefore a first appearance, if there is one, must have $0\le j<h<p$. This explains why the third check covers arbitrarily large indices. A direct enumeration modulo $p^2$ independently checked every $j<p$ at split primes through $10{,}000$. [Fermat-quotient verifier](hall_pell_first_square.py)

For an unbounded search, fix $\delta>0$ and consider the split primes with $q_p(\alpha)\ne0$. For a sufficiently large prime $p$, a square hit with $p\ge e^{\delta n}$ occurs exactly when some target root satisfies the following test. The least nonnegative residue of $q_p(\beta)/q_p(\alpha)$ must be an integer $n$ in $[7,\delta^{-1}\log p]$ congruent to $7\bmod12$, and $\alpha^n=\beta\bmod p$ must hold. The interval is shorter than $p$ for large $p$, so this gives the actual index. For the exceptional primes with zero $q_p(\alpha)$ the target also needs zero $q_p(\beta)$ and the mod-$p$ equation. The available results do not settle the infinitude of such primes or the combined contribution of many smaller prime powers.

## Reproduction

Run from the directory containing the files. The first command uses only Python's standard library. The second uses python-flint, tested with version 0.9.0.

    python3 -B hall_pell_first_square.py --prime-limit 100000000 --direct-check-through 10000
    python3 -B hall_pell_square_census.py --last-n 20000 --prime-limit 1000000000
