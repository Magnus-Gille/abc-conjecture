# How soon can a large prime recur in the Pell family?

Write $n=7+12j$, $j\ge0$, and put

$$t_n=L_n-11,\quad z_n=F_n,\quad A_n=(L_n-6)^2-20,\quad B_n=(L_n-9)^2-5.$$

Here $L_n$ and $F_n$ are the Lucas and Fibonacci numbers. These give the primitive abc triples $1728t_n+5(z_nB_n)^2=A_n^3$. A prime $p$ with $p^2\mid A_nB_n$ and $\log p\ge\delta n$ at infinitely many indices, for fixed $\delta>0$, would disprove abc. [Family and radical](hall_pell_direction.md)

## A bound for every pair of indices

Let $G_n$ be either $A_n$ or $B_n$. Let $H_m$ be any of $t_m,z_m,A_m,B_m$ at another index in the progression, or a different factor at the same index. With $N=\max(n,m)$,

$$\log\gcd(G_n,H_m)<51+25\sqrt N.$$

In particular, suppose $p\mid G_n$ and $\log p\ge\delta n$. For all sufficiently large $n$ depending on $\delta$, the prime has never appeared in any of the four factors at an earlier index. Its next occurrence at an index $m>n$ requires $m>((\delta n-51)/25)^2$. The assertion only needs $p$ to divide $G_n$ once, so it applies also to candidate prime squares.

### An integer divisible by the common divisor

Let $\alpha=(1+\sqrt5)/2$. For odd $n$, $L_n=\alpha^n-\alpha^{-n}$ and $\sqrt5F_n=\alpha^n+\alpha^{-n}$. Use the following monic polynomials.

| Factor | Polynomial |
|---|---|
| $t$ | $P_t(X)=X^2-11X-1$ |
| $z$ | $P_z(X)=X^2+1$ |
| $A$ | $P_A(X)=X^4-12X^3+14X^2+12X+1$ |
| $B$ | $P_B(X)=X^4-18X^3+74X^2+18X+1$ |

For each factor $G_n$, the rational integer $G_n$ divides $P_G(\alpha^n)$ in $\mathbb Z[\alpha]$. The extra factor is a power of the unit $\alpha$ and, for $z_n$, also $\sqrt5$.

Take nonnegative integers $r,s$ with $r+s>0$, and put $h=rn-sm$. Let $\beta,\gamma$ run through the roots of $P_G,P_H$, respectively. Form the algebraic integer

$$Z=\prod_{\beta,\gamma}(\beta^r-\alpha^h\gamma^s)\in\mathbb Z[\alpha].$$

To see that $D=\gcd(G_n,H_m)$ divides $Z$, consider the monic polynomials with roots $\beta^r$ and $\alpha^h\gamma^s$. Both have coefficients in $\mathbb Z[\alpha]$. At $T=\alpha^{rn}$ both values are divisible by $D$. For the first polynomial this follows from $X-\beta\mid X^r-\beta^r$ for $r>0$, followed by multiplication over the roots. For the second use $T=\alpha^h(\alpha^m)^s$ and the same argument. A zero exponent gives zero at the evaluation point on its respective side. Their resultant $Z$ is a polynomial combination of these two monic polynomials, proving the divisibility.

### Why the resultant is nonzero

Set $K=\mathbb Q(\sqrt5)$. Each root of a quartic is a solution of $\beta-\beta^{-1}=u$, where the possibilities are

$$u_{A,\pm}=6\pm2\sqrt5,\qquad u_{B,\pm}=9\pm\sqrt5.$$

The two discriminants $u_{A,\pm}^2+4$ have product $720=(12\sqrt5)^2$. For $B$ the product is $6480=(36\sqrt5)^2$. Neither discriminant of either type is a square in $K$, since its norm to $\mathbb Q$ is not a rational square. The two discriminants of each type generate the same quadratic extension of $K$ after taking a square root. Call that extension $K_A$ or $K_B$. It contains all four roots, and its involution over $K$ sends each root to $-1/\beta$. Also $\beta-\beta^{-1}$ generates $K$ over $\mathbb Q$, so each quartic is irreducible over $\mathbb Q$. All its roots are real, with absolute value different from one.

The fields $K_A$ and $K_B$ are distinct. The ratio $(u_{B,+}^2+4)/(u_{A,+}^2+4)$ equals $3\alpha^{-2}$ and $\sqrt3\notin K$. The two roots for $t$ belong to $K$, and those for $z$ to $K(i)$. The latter is a different quadratic extension from the totally real $K_A,K_B$.

If $G,H$ have different labels, there is consequently an automorphism fixing $\alpha,\gamma$ and sending $\beta$ to $-1/\beta$. For $r,s>0$ the equality $\beta^r=\alpha^h\gamma^s$ would force $\beta^{2r}=(-1)^r$, which is impossible. If $G,H$ have the same label, the involution flips both roots. Multiplication of the supposed equality by its image gives $(-1)^r=\alpha^{2h}(-1)^s$, so $h=0$. Also $\beta^r=\gamma^s$ forces $r=s$. Indeed both roots have the same largest absolute value among their conjugates, and that value exceeds one. Thus $n=m$, excluded for this label. Finally, if either exponent vanishes, equality would require a root to have absolute value $\alpha^n$ or $\alpha^m$ in the real embedding of $\alpha$. Every root has absolute value less than 12, while $\alpha^7>29$. This proves $Z\ne0$.

### Estimating its size

Since $D$ divides $Z$ in $\mathbb Z[\alpha]$, $D^2\le|N_{K/\mathbb Q}Z|$. In either embedding of $K$, bound each difference in $Z$ using $|a-b|\le2\max(1,|a|)\max(1,|b|)$. In each root set at most half the roots exceed one in absolute value, and they all have absolute value below 12. This follows from the reciprocal pairs $\beta,-1/\beta$ and the targets above. For $\alpha^h$ the average of $\log^+|\alpha^h|$ over the two embeddings is $|h|\log\alpha/2$, where $\log^+x=\max(0,\log x)$. There are at most 16 root pairs. These observations yield the more flexible bound

$$\log D\le16\left(\log2+\frac{r+s}{2}\log12+\frac{|rn-sm|}{2}\log\alpha\right).$$

For example a fixed relation $rn-sm=h$ with fixed $r,s,h$ gives an index-independent bound. For the uniform estimate take $Q=\lceil\sqrt{N/10}\rceil$. The pigeonhole principle applied to the fractional parts $k\min(n,m)/N$ for $0\le k\le Q$ gives $0\le r,s\le Q$, at least one nonzero, and $|rn-sm|\le N/Q$. Substitution yields

$$\log D\le16\log24+
16\left(\frac{\log12}{\sqrt{10}}+\frac{\sqrt{10}\log\alpha}{2}\right)\sqrt N < 51+25\sqrt N.$$

## Exact greatest common divisor at consecutive indices

Let $C_n=A_nB_n$. For $n=7+12j$ one always has

$$\gcd(C_n,C_{n+12})=5\!\!\prod_{\substack{(p,a,h)\text{ in the table}\\ j\equiv a\pmod h}}\!p.$$

| Prime $p$ | Residue $a$ | Period $h$ |
|---:|---:|---:|
| 59 | 14 | 29 |
| 79 | 12 | 13 |
| 197,699 | 44,283 | 98,849 |
| 14,119,141 | 222,004 | 1,176,595 |

Thus this gcd is always squarefree. Its exact maximum is $65\,052\,180\,018\,107\,495$. The first index attaining it is $j=30\,165\,452\,234\,189$, corresponding to $n=361\,985\,426\,810\,275$. The four periods are pairwise coprime.

For the proof put $x=L_n$ and $y=L_{n+12}$. The recurrence $u_{j+2}=322u_{j+1}-u_j$ starting at $29,9349$ preserves $x^2+y^2-322xy=103680$. Write $g_A(x)=(x-6)^2-20$ and $g_B(x)=(x-9)^2-5$. Taking successive integer polynomial resultants eliminates $x,y$ from $g_G(x),g_H(y)$ and the conic equation. The gcd of $g_G(x)$ and $g_H(y)$ divides the resulting nonzero integer, by the same resultant identity as above.

| Factor pair | Absolute double resultant |
|---|---|
| $A,A$ | $2^{24}3^45^5\cdot29\cdot61\cdot151^2$ |
| $A,B$ or $B,A$ | $2^83^4\cdot59\cdot61\cdot197699\cdot14119141$ |
| $B,B$ | $2^{20}3^85^5\cdot79^2\cdot2081$ |

Both factors are odd and neither is divisible by 3. They are coprime to each other because their polynomial resultant has absolute value 144. The progression gives $x\equiv9\pmod{10}$, so $5\mid B_n$ exactly once. For each candidate prime above 5, running the recurrence modulo the prime until the initial pair recurs gives exactly the four rows displayed. Of the surviving primes only 79 could occur squared according to the resultants. The full period modulo $79^2$ is 1027 and contains no shared square. The verifier computes both eliminations, every relevant modular period and the simultaneous residue for the maximum. Run it with Python and SymPy. [Exact certificate](hall_pell_adjacent_gcd.py)

These estimates describe factors shared between terms. A prime square can first occur within a single term, and that case still permits the proposed abc counterexample.
