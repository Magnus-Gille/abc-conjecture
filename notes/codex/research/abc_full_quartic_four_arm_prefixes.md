# Four odd-depth primes at each certified prime-factor step

Let $G=(-3,9)$ on $E:Y^2=X^3-36X$. Write $w_n,a_n,c_n,d_n$ for the four positive coprime arms of the primitive quartic at odd $n>0$, and $D_n=\operatorname{sf}(w_na_nc_nd_n)$, the product of the primes of odd valuation. Set
$$
 M=11\,210\,216\,592\,196\,440,\qquad
 \mathcal S=\{q\text{ odd prime}:q\not\equiv\pm1\bmod M\}.
$$
For $e_q=v_q(n)$ and $\iota(q)={\bf1}_{q\equiv3\bmod4}$, every positive odd index satisfies
$$
 D_n\ \ge\
 3^{e_3\bmod2}\prod_{\substack{q\mid n\\q\in\mathcal S}}
           16^{e_q}\,q^{(4+\iota(q))e_q(e_q+1)/2}.
$$
For each $q\in\mathcal S$ and $1\le j\le e_q$, each arm contains its own good prime of odd valuation whose translated-generator reduction order is divisible by $q^j$. All selected primes are distinct, so $\omega(D_n)\ge4\sum_{q\in\mathcal S} e_q+{\bf1}_{e_3\ {\rm odd}}$.

If every prime divisor of $n$ lies in $\mathcal S$, then $D_n\ge16^{\Omega(n)}n^4$. If they are also all $3\bmod4$, then $D_n\ge16^{\Omega(n)}n^5$. For an arbitrary $n$ the product above uses just its certified prime factors. The excluded prime classes have relative prime density $2/\varphi(M)=1/979425684357120$. Their reciprocal sum diverges, so integers supported entirely on $\mathcal S$ have natural density zero.

There is also an explicit range where no condition on index support is needed. From the denominator square classification and the two-square-arm theorem, the largest prime divisor of $n>1$ has two distinct surviving witnesses exceeding twice its size. Thus $P^+(n)<\sqrt{D_n}/2$. If $D_n\le Y\le4(M-1)^2$, about $5.03\cdot10^{32}$ at the upper endpoint, all its index primes are below $M-1$ and are certified. Every such index $n>1$ therefore satisfies $n\le Y^{1/4}/2$. [Proof of the largest-prime estimate](abc_full_quartic_pointwise_total_kernel.md)

## Local computation

On $E_0:y^2=x^3+36x^2+36x$, let $P=(-2,8)$. For positive odd $m$, the [isogenous parametrization](abc_full_quartic_signature.md) gives $z=x(mP)=-2u^2/v^2$, $(u,v)=1$, $w_m=(u^2+3v^2)/4$, and $X=x(mG)=6+288z/(6-z)^2$. At a good probe $h\equiv1\bmod4$ where $mP$ is affine and $z\ne6$, the quadratic character satisfies $\chi_h(w_m)=\chi_h(8(6-z))$, since $8(6-z)=64w_m/v^2$. For $F=a,c,d$ take $t=0,-6,6$, respectively. The identities $(F_m/w_m)^2=(X-t)/(-3-t)$ give
$$
       \chi_h(F_m)=\chi_h(w_m)((X-t)/(-3-t))^{(h-1)/4}
$$
in $\mathbf F_h$ whenever the entries are units.

The [standard-library verifier](abc_full_quartic_four_arm_prefixes.py) generates probes $h\le100000$ with $4<\operatorname{ord}_h(P)\mid L$, and retains only tables defined and nonzero in all four arms at every unit residue. Because the formulas use the abscissa, opposite residues give the same result. For each listed $L$, the vectors are injective on $(\mathbf Z/L)^\times/\{\pm1\}$ for each arm separately.

| $L$ | Classes up to sign | Retained probes |
|---:|---:|---:|
| 8 | 2 | 2 |
| 72 | 12 | 10 |
| 120 | 16 | 31 |
| 312 | 48 | 33 |
| 408 | 64 | 28 |
| 696 | 112 | 25 |
| 840 | 96 | 47 |
| 984 | 160 | 24 |
| 2520 | 288 | 61 |
| 4440 | 576 | 67 |
| 6360 | 832 | 68 |
| 10680 | 1408 | 60 |
| 10920 | 1152 | 126 |
| 11640 | 1536 | 59 |

Run the complete verification with

    python3 abc_full_quartic_four_arm_prefixes.py

## From character changes to four distinct witnesses

Append the prime factors of $n$ in descending order with repetition, passing from a prefix $m$ to $mq$. For $q\in\mathcal S$ above 97, both prefixes are units at all the moduli. If $q\equiv\pm1$ at every modulus, the signs agree since the moduli share 8, and their lcm is $M$. Thus some $L$ separates the two prefixes up to sign, and the character vector in each arm changes. For $7\le q\le97$ take $L=120$; for $q=3,5$ take $L=8$.

Write $H=G+T_F$ for the integral translated generator whose denominator root at odd $m$ is $F_m$. One has $F_m\mid F_{mq}$. If a good $p\mid F_m$, its reduction order $s>1$ divides $m$. Every prime factor of $s$ is at least $q$. Full rational two-torsion gives $4s\mid\#E(\mathbf F_p)$ and $p\ge(2\sqrt s-1)^2>2s$. Thus $p>q$ and the old depth is unchanged. The only bad prime possible is 3, in $d_m$, with valuation $v_3(m)$. [Denominators and lifting](abc_full_quartic_signature.md) · [Bad-prime valuation](abc_full_quartic_total_kernel.md)

The changing character makes $F_{mq}/F_m$ nonsquare. This provides a new good odd-depth prime except potentially at $F=d,\ q=3$. In this case $h=1249$ has $\operatorname{ord}_h(P)=8,\ \chi_h(3)=1$, and $\chi_h(d_m)=+,-,-,+$ at $m=1,3,5,7\bmod8$. Consequently $d_{3m}/(3d_m)$ is nonsquare and supplies a new good prime as well.

At the new prime, $s\mid mq$ and $s\nmid m$, so $q^j\mid s$ when $q^j\parallel mq$. Thus $p>2q^j$; every later multiplier is at most $q$ and preserves the odd depth. The witnesses differ at different steps in the same arm, and across arms by coprimality at $n$.

In the $w$ arm $p\equiv1\bmod12$, so Gaussian multiplication is defined over $\mathbf F_p$. If $q\equiv3\bmod4$, it is inert in $\mathbf Z[i]$. Since the additive order is divisible by $q^j$, the cyclic Gaussian module generated by $G\bmod p$ has annihilator divisible by $(q^j)$. Hence $q^{2j}$ divides the group order, and full rational two-torsion supplies another factor 4. This yields $p\ge(2q^j-1)^2>2q^{2j}$. Multiplying all selected primes and including the separate 3-adic parity gives the bound.
