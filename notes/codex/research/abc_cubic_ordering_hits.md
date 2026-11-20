# Six cubic images with large new radicals on the same abc hits

For a primitive positive triple of height $H$ (its largest term) and radical $R$ (the product of the distinct primes of the three terms), call $H/R$ its gain. Fix $0<\theta<2$. There are infinitely many inputs $1+(z-1)=z$ with gain $\gg_\theta(\log z)^\theta$ such that **all six orderings** used in the [cubic reduction](abc_marked_rational_radical_bounds.md) have the following properties simultaneously.

* Each primitive output has height $H_g\asymp z^3$ and gain $H_g/R_g\gg_\theta(\log H_g)^\theta$.
* Each of the two extra linear factors in **each** output contributes primes absent from the input and from the other eleven factors. Write $E$ for the product of the primes above 13 in any one of the twelve factors. Along the constructed sequence,
  $$
  \liminf_{z\to\infty}\frac{\log\log E\;\log\log\log z}{\log\log z}
      \ \ge\ \frac{(1-\theta/2)\log 2}{10}.
  $$
  In particular $E$ eventually exceeds $\exp((\log\log z)^B)$ for every fixed $B>0$. Even the ordering that adds the fewest primes by radical size has $R_g/R$ larger than any fixed power of $\log z$.

This rules out absorbing the extra radical with a polylogarithmic allowance on **all** abc hits. The displayed gain alone gives no fixed $\varepsilon>0$ for which $z/R^{1+\varepsilon}$ grows without bound.

## Which primes enter each image

Set $t=1/z$ and $f(s)=27s^2(1-s)/4$. For $g$ any of the six rational transformations permuting $0,1,\infty$, write $f(g(t))$ in lowest terms. The numerator, denominator and their difference give a primitive positive triple after taking absolute values and moving the largest term to the right. Omit boundary inputs. The extra roots are given in the **$z$ coordinate** by $g(1/z)=2/3,-1/3$.

| $g(t)$ | Roots $r_i$ in $z$ |
|---|---|
| $t$ | $3/2,-3$ |
| $1-t$ | $3,3/4$ |
| $1/t$ | $2/3,-1/3$ |
| $1/(1-t)$ | $-2,1/4$ |
| $t/(t-1)$ | $-1/2,4$ |
| $(t-1)/t$ | $1/3,4/3$ |

For $r=b/a$ in lowest terms with $a>0$, its integral linear factor is $az-b$. The twelve signed roots are distinct and have ten distinct absolute values, all of the form $2^i3^j$. Reducing the roots and $0,1,\infty$ modulo any prime $h>13$ preserves distinctness, by their pairwise determinants. For such $h$, reduction of the cubic is good, and a prime belongs to the output radical exactly when it divides the input or one of this ordering's two extra forms. Thus $R_g/R\asymp E_iE_j$ for the indicated pair, with bounded corrections at the six primes through 13. Each extra factor has size $O(z)$, so $R_g\ll Rz^2$. The fixed degree-three map has height $H_g\asymp z^3$ by its resultant and the usual projective height comparison. This proves the gain transfer once the input is constructed.

## Short exponents with specified residues

Use
$$
 \Lambda_k=\{(u,v)\in\mathbb Z^2:2^u3^v\equiv1\pmod{5^k}\},\qquad
 D_k=[\mathbb Z^2:\Lambda_k]=4\cdot5^{k-1}.
$$
Indeed 2 has order 4 modulo 5 and $v_5(2^4-1)=1$, so its order modulo $5^k$ is $D_k$. Infinitely many $k$ have the following property: every point of the plane is within $2\sqrt{D_k}$ of $\Lambda_k$.

To prove it, choose a shortest nonzero vector $v_k$ at each level. Its length is at most $2\sqrt{D_k/\pi}$ by Minkowski's disk bound. Its line must change infinitely often. For a fixed primitive direction $(a,b)$ put $w=2^a3^b\ne1$, $h=\operatorname{ord}_5(w)$ and $s=v_5(w^h-1)<\infty$. Lifting the exponent shows that the least positive multiplier placing this direction in $\Lambda_k$ is $h5^{\max(0,k-s)}$. Eventually any vector on that line is too long to be shortest. At a change of line, $v_k,v_{k+1}$ are independent vectors of $\Lambda_k$. Half the sum of their lengths bounds the covering radius of the lattice they span and is at most $(1+\sqrt5)\sqrt{D_k/\pi}<2\sqrt{D_k}$. The larger lattice $\Lambda_k$ inherits the bound.

Write $D=D_k$ at one of these levels and let $P$ be an integer coprime to 10. Since $D\mathbb Z^2\subseteq\Lambda_k$ and $(D,P)=1$, every pair of residues modulo $P$ occurs in $\Lambda_k$. The points in that residue class form a translate of $P\Lambda_k$ because multiplication by $P$ is invertible on $\mathbb Z^2/\Lambda_k$. Approximating the point $(4P\sqrt D,4P\sqrt D)$ gives positive exponents satisfying
$$
                  2P\sqrt D\le u,v\le 6P\sqrt D
$$
in any prescribed residue class.

## Arranging many distinct primes in every factor

Let $\alpha=1/\theta-1/2>0$. In increasing order, take the primes above 13 in complete batches of ten, stopping before their product $P$ would exceed $D^\alpha$. Distribute one prime from every batch to each of the ten absolute values in the table. Write $M_j$ for the product assigned to absolute value $s_j=2^{a_j}3^{b_j}$. The $M_j$ are pairwise coprime, odd and squarefree. Specify the simultaneous congruences
$$
           u\equiv a_j\pmod {M_j},\qquad v\equiv b_j\pmod {M_j}.
$$
Choose $u,v$ in $\Lambda_k$ as above. Put $z=2^u3^v$. Since $5^k\mid z-1$, one has
$$
  R=6\operatorname{rad}(z-1)\le\frac{6(z-1)}{5^{k-1}},\qquad
  \log z\asymp P\sqrt D\le D^{1/\theta}.
$$
In the last inequality the comparison for $\log z$ allows a fixed multiplicative constant. This gives the claimed gain. The switching levels are unbounded, so the inputs have unbounded height.

For each $j$, $z/s_j=B_j^{M_j}$ for an integer $B_j>1$. This uses positivity of $u-a_j,v-b_j$ at large levels. For each divisor $d>1$ of $M_j$:

* At a positive root, a primitive prime divisor of $B_j^d-1$ has order $d$ for the base $B_j$ and divides $B_j^{M_j}-1$.
* At a negative root, use a primitive prime divisor of $B_j^{2d}-1$. Its order is $2d$, and $M_j/d$ is odd, so it divides $B_j^{M_j}+1$.

The Bang–Zsigmondy theorem applies since $d>13$ and the other base is 1. Every selected prime exceeds $d$ and divides the intended integral form: for $r=b/a$, $az-b=|b|(z/|r|-\operatorname{sgn}(r))$. Distinct divisors give distinct orders within a factor. The determinant check makes all selected primes distinct between factors and coprime to $z(z-1)$. Opposite roots use the same exponent block and produce disjoint primes.

If there are $j_0$ complete batches, $\tau(M_j)=2^{j_0}$ and
$$
 \log E\ \ge\ \sum_{d\mid M_j}\log d
       =\tfrac12\,2^{j_0}\log M_j .
$$
The prime number theorem gives $\log P\sim \alpha\log D$ (one omitted batch has logarithmic size $O(\log\log D)$) and
$j_0=(1/10+o(1))\log P/\log\log P$. Since $\log\log z=(1/2+\alpha+o(1))\log D$, this yields the stated constant. The lower bound is still smaller than $z^\delta$ for every fixed $\delta>0$; it does not give the missing power comparison. K. Zsigmondy, *Zur Theorie der Potenzreste*, Monatsh. Math. Phys. **3** (1892), 265–284.

## A numerical instance of the order argument

For the single extra root $-3$, take $z=3^{176}$. Here $16\mid176$, $35\mid175$, and $v_2(z-1)=6$, so $z/R>32/3$. The factor $z+3=3(3^{175}+1)$ contains $61,547,374857981681$, of orders $10,14,70$ for the base 3. Their product is $12507886274749927$. All three are absent from the input radical. The verifier also computes the twelve roots and checks simultaneous CRT conditions at a switching level. [Standard-library verifier](abc_cubic_ordering_certificates.py)
