# How large the two extra radicals can be

For coprime $0<x<z$ put $R=\operatorname{rad}(x(z-x)z)$. Let $R'$ be the radical after dividing the cubic identity
$$
27x^2(z-x)+(3x-2z)^2(3x+z)=4z^3
$$
by its common gcd. Omit $3x=2z$. The two extra linear forms are $L=3x-2z$ and $M=3x+z$. The general transfer bound is $R'\ll Rz^2$. Its factor $z^2$ is sharp on a positive proportion of inputs. There is a different difficulty on inputs with small $R$: an improvement in the lower bound on $R'/R$ on a specific such sequence would imply the infinitude of non-Wieferich primes to base 2. [Cubic reduction](abc_marked_rational_radical_bounds.md)

## Positive density with maximal extra radical

Fix an interval $I$ of positive length whose closure lies in $(0,1)$ and avoids $2/3$. Take $x/z\in I$, $x\equiv3\pmod6$, $z\equiv2$ or $4\pmod6$, $\gcd(x,z)=1$. These inputs have positive density among pairs $0<x<z\le H$. The normalized image equals the displayed triple, since its common gcd divides a power of 6 and its first term is odd while $3\nmid z$. The numbers $|L|,M$ are coprime to 6, to each other, and to the input product. Indeed the pairwise determinants of the five forms have no prime factors outside 2 and 3. Thus $R'/R=\operatorname{rad}(|LM|)$.

Within this class the proportion for which both extra forms are squarefree tends to
$$
 \prod_{p\ge5}\left(1-\frac{2}{p(p+1)}\right)>0.
$$
At $p\ge5$ there are $p(p+1)$ projective primitive residue classes modulo $p^2$. Vanishing of either form singles out one such class, and the classes differ because the determinant is 9. CRT and lattice counting in the fixed sector give the product through any fixed prime cutoff. To remove the cutoff $T$, each $p^2\mid LM$ with $p>T$ to be excluded divides one of the individual forms twice, by their coprimality. For each $x\le H$ there are $O(H/p^2+1)$ choices of $z$ per form and $p\ll\sqrt H$. This costs $O(H^2/T+H^{3/2})$ pairs. The primitive condition itself has a tail of size $O(H^2/T)$ by summing $\lfloor H/p\rfloor^2$. This proves the limiting density. On the indicated squarefree inputs,
$$
 \frac{R'}{R}=|3x/z-2|(3x/z+1)z^2\asymp_I z^2 .
$$

## A near-hit sequence that detects non-Wieferich primes

For odd $n\ge3$ divisible by 3, put $x=2^n$, $z=x+1$. Define $A=2^{n-1}-1$, $B=2^{n+2}+1$. Both have 3-adic valuation one by lifting the exponent, and $B=8A+9$ gives $\gcd(A,B)=3$. The primitive image is
$$
 2^{2n-2}+(A/3)^2(B/3)=(z/3)^3 .
$$
Here $9\mid z$. The integers $A/3,B/3$ are odd and coprime to $z$, since common primes of $A$ or $B$ with $z$ divide 3. Consequently
$$
 \frac{R'}R=\operatorname{rad}(A/3)\operatorname{rad}(B/3).
$$
Already at $n=3^k$, $k\ge1$, the input gain satisfies $z/R\ge 3^k/2$, because $v_3(z)=k+1$.

Let $W$ be the product of the distinct primes occurring to exponent one in $(A/3)(B/3)$. Then
$$
 (R'/R)^2\le (A/3)(B/3)\,W\ll z^2W.
$$
Every prime of $W$ is a base-2 non-Wieferich prime. Indeed, if an odd prime $p$ satisfies $2^{p-1}\equiv1\pmod{p^2}$, then the orders of 2 modulo $p$ and $p^2$ coincide. Whenever $p\mid 2^j-1$ it follows that $p^2\mid 2^j-1$. If $p\mid 2^j+1$, apply the same argument at $2j$ and use $p\nmid 2^j-1$. Thus even the unboundedness of $R'/(Rz)$ on this sequence would imply infinitely many base-2 non-Wieferich primes. For a gain $R'/R\ge z^{1+\delta}$, the necessary product satisfies $W\gg z^{2\delta}$. For comparison, Silverman deduced results on non-Wieferich primes from abc in *Wieferich's criterion and the abc-conjecture*, J. Number Theory **30** (1988), 226–237. [Paper](https://doi.org/10.1016/0022-314X(88)90019-4)

One can simultaneously remove all small primes from $A/3,B/3$. For large $Y$ let $m$ be the odd part of $\operatorname{lcm}(1,\ldots,\lfloor Y\rfloor)$. Take $n=3^e m$, with $e$ one of $\lceil Y^2\rceil,\lceil Y^2\rceil+1$, chosen so $n\equiv3\pmod4$. Then $z/R\ge3^{v_3(n)}/2=(\log z)^{1-o(1)}$ in the sense of a lower bound, since $\log m=O(Y\log Y)$. For $5\le p\le Y$, the odd part of the order of 2 modulo $p$ divides $m$, since the order divides $p-1$. A prime dividing $A$ would have this odd part dividing $n-1$; a prime dividing $B$ would have it dividing $n+2$. In both cases the odd part would be 1. The 2-adic valuations of $n-1$ and $2(n+2)$ are both one, so the order would divide 2, which forces $p=3$. Thus testing any fixed finite set of primes for square divisibility eventually gives no obstruction along this sequence. The large-prime condition expressed by $W$ remains.
