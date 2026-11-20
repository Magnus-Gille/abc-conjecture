# The sharp exponent at a fixed set of primes

Fix $n\ge3$ and a prime $p\equiv1\bmod n$. For coprime positive $B<A$ for which $B/A$ has order $n$ modulo $p$, let $e=v_p(A^n-B^n)$. Then
$$
             \limsup_{A\to\infty}\frac{(e-1)\log p}{\log A}=2.          \tag{1}
$$
The same limsup holds if the real ratio $B/A$ is confined to any prescribed nonempty open subinterval of $(0,1)$. Thus a fixed prime can supply enough repeated multiplicity for the abc quality of $B^n+(A^n-B^n)=A^n$ to have lower limit at least one along infinitely many pairs. For this prime alone to certify quality greater than a fixed $1+\varepsilon$, using $R\le A^{n+2}/p^{e-1}$, it would suffice to have $p^{e-1}>A^{2+n\varepsilon/(1+\varepsilon)}$. By (1) there are only finitely many such pairs for each fixed $p$. The constants in the argument depend on $p$.

## Prescribing the local contributions

In fact take any nonempty finite set $S$ of primes $p\equiv1\bmod n$, and at each $p$ choose a primitive $n$-th root $\alpha_p\in\mathbf Z_p$. These exist by simple-root lifting from $\mathbf F_p$. For any nonnegative real weights $\beta_p$ of sum one and any real interval as above, there is a sequence of primitive positive pairs in that interval, of order $n$ at all those primes, with
$$
        \frac{v_p(A^n-B^n)\log p}{\log A}\longrightarrow 2\beta_p
                  \qquad(p\in S).                                      \tag{2}
$$

The finite-place Subspace Theorem gives the following inequality for every $\eta>0$ and every primitive pair of integers $(a,b)$ of height $h=\max(|a|,|b|)$:
$$
              \prod_{p\in S}|b-\alpha_p a|_p^{-1}
                        \ll_{S,n,\eta} h^{2+\eta}.                      \tag{3}
$$
Indeed, use the two independent forms $a,b-\alpha_p a$ at $p$ and $a,b$ at the real place. A primitive pair has local maximum one at each finite prime. The additional local factors $|a|_p$ are at most one, while $|ab|\le h^2$. Violation of (3) beyond the indicated exponent puts the points in finitely many rational lines by the Subspace Theorem. Each line has at most two primitive integer representatives. As the targets have order $n\ge3$, they are irrational and none of the local differences vanishes at a nonzero rational point. The two coordinate axes contain only finitely many primitive pairs as well. This is the two-variable $p$-adic form of Schmidt's Subspace Theorem due to Schlickewei. [Related height argument](abc_eisenstein_24_factor_layers.md)

## An elementary construction with bounded error

The prescribed masses in (2) can in fact be attained with bounded additive errors:
$$
          v_p(A^n-B^n)\log p=2\beta_p\log A+O_{S,n,I}(1)
             \qquad(p\in S),                                           \tag{4}
$$
where $I$ is the chosen open interval. For the construction no Diophantine approximation estimate is needed. Let $j$ run over positive integers, set $k_{p,j}=\max(1,\lfloor j\beta_p/\log p\rfloor)$ and put $D_j=\prod_{p\in S}p^{k_{p,j}}$. Thus $\log D_j=j+O_S(1)$, the integers $D_j$ form a divisibility chain and $D_{j+1}/D_j$ stays bounded. The lattice
$$
 L_j=\{(a,b)\in\mathbf Z^2:b\equiv\alpha_p a\bmod p^{k_{p,j}}
                                      \text{ for every }p\in S\}
$$
has determinant $D_j$ by the Chinese remainder theorem. Write $\lambda_1,\lambda_2$ for the successive minima in the maximum norm.

There are infinitely many $j$ at which $\lambda_1(L_j)$ and $\lambda_2(L_j)$ are both comparable to $\sqrt{D_j}$ with constants depending only on $S$. To see this choose a shortest nonzero vector of each lattice. On a fixed rational line with primitive direction $(a,b)$, all $v_p(b-\alpha_p a)$ are finite. Its shortest nonzero vector in $L_j$ has length at least a line-dependent constant times $D_j$, since its scalar multiplier is divisible by $\prod_{p\in S}p^{\max(0,k_{p,j}-v_p(b-\alpha_p a))}$. On the other hand $\lambda_1(L_j)\ll\sqrt{D_j}$. The shortest direction must therefore change at infinitely many consecutive indices. At each change, the two chosen vectors lie in $L_j$ and are independent. Writing $Q=D_{j+1}/D_j$, we have $QL_j\subset L_{j+1}$, so $\lambda_2(L_j)\le \lambda_1(L_{j+1})\le Q\lambda_1(L_j)$. Minkowski's second theorem gives $\lambda_1(L_j)\lambda_2(L_j)\asymp D_j$, proving the claim.

On these indices put $M=\prod_{p\in S}p$ and choose $w=(1,b_0)$ by imposing $b_0\equiv\alpha_p+p^{k_{p,j}}\bmod p^{k_{p,j}+1}$ at every $p$. The coset $w+ML_j$ has a point within $O_S(\lambda_2(L_j))$ of every point of the real plane. Round the coefficients in two independent lattice vectors of maximum norm at most $\lambda_2(L_j)$, after scaling by $M$ and translating by $w$. Take a point on a ray of slope inside $I$ at distance a sufficiently large fixed multiple of $\lambda_2(L_j)$ from the origin. Rounding gives $0<b<a\ll_{S,I}\sqrt{D_j}$ with $b/a\in I$. The coset forces $a\equiv1\bmod p$ and $v_p(b-\alpha_p a)=k_{p,j}$ for every $p\in S$. Division by the common gcd preserves those valuations and gives a primitive pair $(A,B)$ still belonging to $L_j$. Consequently $A\ge\lambda_1(L_j)\gg_S\sqrt{D_j}$ as well. This proves $\log A=\tfrac12\log D_j+O_{S,I}(1)$.

The reduction of $B/A$ is a simple root of order $n$ at each $p$. Thus $v_p(A^n-B^n)=v_p(B-\alpha_p A)=k_{p,j}$, proving (4). For (1) take a single prime, and for its upper bound apply (3) to the finitely many possible primitive roots. Subtracting one from the exponent changes the ratio by $o(1)$.

Along the constructed sequence, $\sum_{p\in S}(v_p(A^n-B^n)-1)\log p=2\log A+O_{S,n,I}(1)$. It follows that $\operatorname{rad}(AB(A^n-B^n))\ll_{S,n,I} A^n$. A fixed-exponent disproof by this local mechanism would require a positive proportional excess over $2\log A$, or additional repeated multiplicity at other primes.

## The contribution that must escape every fixed set

There is an upper bound for the portion accounted for by **any** fixed finite set of primes $S$, without order restrictions. Put $F=AB(A^n-B^n)$. For every $\rho>0$,
$$
              \prod_{p\in S}p^{v_p(F)}
              \ll_{S,n,\rho} A^\rho A\min(B,A-B).                       \tag{5}
$$
At each $p$ consider the projective roots of $F$, with linear forms $A,B$ and $B-\zeta A$ for $\zeta^n=1$. They are distinct in characteristic zero. If $p$ divides either coordinate then the other factors are units. If both coordinates are units, all distances except the smallest to the finitely many roots of unity are bounded below by a positive constant depending only on $p,n$, by their pairwise separation. Thus at each prime one form has absolute value $\ll_{p,n}|F|_p$, and a second independent form can be chosen with absolute value at most one. At the real place use the forms $A,B$ or $A,A-B$, according as $B$ or $A-B$ is smaller. Applying the same Subspace Theorem to the finitely many systems gives (5). None of the permitted pairs has $F=0$, so the finitely many exceptional primitive pairs can be absorbed in the constant.

At an exception $A^n>\operatorname{rad}(F)^{1+\varepsilon}$, write $t=n\varepsilon/(1+\varepsilon)$. Since $F\ge A^nB(A-B)\ge\tfrac12 A^{n+1}\min(B,A-B)$, equation (5) gives
$$
              \prod_{p\notin S}p^{(v_p(F)-1)_+}
                        \gg_{S,n,\rho} A^{\,t-\rho}.                    \tag{6}
$$
Thus for fixed $n$ a fixed-exponent counterexample sequence must accumulate a positive power of its base height in repeated factors outside every prescribed finite set of primes. Equation (4) describes how close the fixed-prime contribution alone can come to the boundary.

## An exhaustive search by prime and exponent

At $n=7,9$ we tested the sufficient condition
$$
     p^e\mid A^n-B^n,\qquad \operatorname{ord}_p(B/A)=n,\qquad
                           p^{21(e-1)}>A^{42+n}.
$$
It guarantees $A^n>R^{21/20}$ from this prime alone. Each of the following search ranges, independently, contained exactly the three listed tuples. The bounds include every eligible prime, both indices and all $2\le e$ through the specified maximum. There is no imposed cutoff on $A$ or $B$ beyond the inequality being tested.

| Maximum prime | Maximum exponent |
|---:|---:|
| 2,000 | 300 |
| 200,000 | 120 |
| 2,000,000 | 12 |

| $n$ | $p$ | Qualifying $e$ | $A$ | $B$ | Actual quality |
|---:|---:|---|---:|---:|---:|
| 7 | 71 | 4, 5 | 150 | 43 | 1.3926186962 |
| 9 | 19 | 3 | 11 | 6 | 1.0857000085 |

For the second seed $11^9-6^9=19^3\cdot5\cdot223\cdot307$ and the radical of the triple is $429250470$. The $p=71$ search alone through $e=500$ returned just the two displayed exponents. A search with fixed $p,e$ is finite because every solution has $A^2<p^{e-1}$. The verifier lifts all primitive residue roots from $p$ to $p^e$ and uses the Euclidean algorithm to recover every possible reduced fraction. An independent direct enumeration through $p=73$, $e=5$ verifies the small cases. The search leaves open larger primes and exponents and contributions from several primes insufficient on their own. [Verifier and reproduction commands](abc_cyclotomic_hensel_search.py) · [Complete small-height counts](abc_sextic_power_exception_count.md)
