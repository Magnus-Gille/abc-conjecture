# A power saving for exceptional seventh- and ninth-power triples

Fix $n=7$ or $9$. For coprime integers $1\le B<A$ put $V=A^n-B^n$ and $R=\operatorname{rad}(ABV)$. For every fixed $\varepsilon>0$ and every $\xi>0$,
$$
 \#\{1\le B<A\le H:\gcd(A,B)=1,\ A^n>R^{1+\varepsilon}\}
                   \ll_{n,\varepsilon,\xi} H^{2-s+\xi}.                 \tag{1}
$$
Writing $t=n\varepsilon/(1+\varepsilon)$, one can take
$$
 s=\min\left\{\frac{2t}{3},\frac23,\max\left(\frac12,\frac{3t-2}{5}\right)\right\}.
$$
There are $\asymp H^2$ primitive pairs in the box. At $\varepsilon=1/20$ the exceptional counts are $O_\xi(H^{16/9+\xi})$ for seventh powers and $O_\xi(H^{12/7+\xi})$ for ninth powers. These bounds include all prime multiplicities. A proof of abc on all triples of either fixed power would imply rational abc. The estimates still allow unbounded sequences of exceptional pairs. [Transfer to the general conjecture](abc_cyclotomic_large_square_twists.md)

## Removing primes below the height cutoff

Work first on $H/2<A\le H$. Choose $0<u<s$ and put $\theta=\min(B,A-B)/H$. Write $F=ABV$, and let $D_{\rm small}$ be the product of $p^{(v_p(F)-1)_+}$ over $p\le H^{2-u}$. Except on $O_{n,u,\xi}(H^{2-u+\xi})$ pairs, one has $\theta\ge H^{-u}$ and $D_{\rm small}\ll H^u\theta$. This simultaneous estimate comes from applying determinant spacing to the ratios $B/A$ in intervals of length $O(\theta)$. [Small-prime estimate, equation (3)](abc_binary_power_small_prime_excess.md)

The larger of $B,A-B$ is at least $A/2$, and $V\ge A^{n-1}(A-B)$. Hence $F\ge A^nB(A-B)\gg_n H^{n+2}\theta$. At an exception $R<A^{n/(1+\varepsilon)}\le H^{n-t}$. Outside the set just removed, the contribution of primes $p>H^{2-u}$ to the repeated part is therefore
$$
                      D_{\rm large}=\frac{F}{R D_{\rm small}}
                                      \gg_n H^{2+t-u}.                   \tag{2}
$$

## The sextic factor accounts for the large repeated primes

At $n=7$ the factors of $F$ are $A,B,A-B$ and $\Phi_7(A,B)$. At $n=9$ there is also $\Phi_3(A,B)=A^2+AB+B^2$. In both cases $S=\Phi_n(A,B)$ is the unique sextic factor and $S\le(2H)^6$. For large $H$ a prime $p>H^{2-u}$ is coprime to $n$, and it divides at most one factor by coprimality and separability of $X^n-1\bmod p$. The linear and quadratic factors are at most $3H^2$, so every repeated prime above the cutoff occurs entirely in $S$.

For any $Y\ge1$, the number of primitive pairs **over all heights** satisfying $S=bz^2$ for some squarefree $1\le b\le Y$ is $O_n(Y(1+\log Y)^{C_n})$. A bound of the same form holds for $S=bz^3$ with any integer $1\le b\le Y$. These estimates follow from uniform Mordell–Lang and rank bounds on the genus-two quadratic twists and genus-four cubic twists, respectively. A cofactor below 1 makes the corresponding case empty. [Quadratic twists](abc_cyclotomic_large_square_twists.md) · [Cubic twists](abc_cyclotomic_cube_twist_count.md)

* If all the repeated primes above the cutoff occur to exponent two, $D_{\rm large}^2$ divides $S$. Its squarefree cofactor is at most $S/D_{\rm large}^2\ll_n H^{2-2t+2u}$ by (2). Since $3u<2t$, the quadratic-twist bound gives $O_{n,u}(H^{2-u})$ pairs, absorbing the logarithmic factor.
* If a prime above the cutoff occurs at least four times, the squarefree cofactor of $S$ is at most $S/p^4\ll H^{4u-2}$. Again the quadratic-twist bound suffices because $u<2/3$ gives $4u-2<2-u$.
* Otherwise some prime $p>H^{2-u}$ occurs exactly three times. A second repeated prime $q$ above the cutoff would give $p^3q^2>H^{5(2-u)}>(2H)^6$ for all sufficiently large $H$. Consequently $D_{\rm large}=p^2$, and $p\gg_n H^{1+(t-u)/2}$ by (2). In $S=bp^3$ we have
  $$
                        b\ll_n\min\{H^{3u},H^{3-3(t-u)/2}\}.
  $$
  If $u<1/2$ then $3u<2-u$. If $u\ge1/2$ then $u<s$ implies $u<(3t-2)/5$, so $3-3(t-u)/2<2-u$. In both cases the cubic-twist count gives $O_{n,u}(H^{2-u})$ pairs.

Combine these estimates, take $u$ arbitrarily close to $s$, and choose the exponent loss in the small-prime estimate arbitrarily small. Summing over doubling intervals proves (1).

## Complete counts through height 500

With $1\le B<A\le500$ there are 76,115 primitive pairs for each exponent. The thresholds below use integer inequalities, including $A^{20n}>R^{21}$ for quality greater than $21/20$.

| Power $n$ | Quality above $1$ | Quality above $21/20$ | Highest-quality $(A,B)$ | Radical at the maximum | Quality |
|---:|---:|---:|---|---:|---:|
| 7 | 90 | 21 | $(150,43)$ | 86,721,350,370 | 1.392618696210 |
| 9 | 321 | 49 | $(28,1)$ | 96,230,268,582 | 1.185837445052 |

The two maximizing differences are $150^7-43^7=71^5\cdot107\cdot8849$ and $28^9-1=3^5\cdot19^2\cdot271\cdot444979$. The seventh-power example has its largest loss at a prime far below the base height squared. Independent complete factorizations verified every radical in both rows of the table. [Reproduce the quality census](abc_sextic_power_quality_scan.py) · [Large-square census](abc_cyclotomic_large_square_scan.py)
