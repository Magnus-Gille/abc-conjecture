# An abc-equivalent eighth-power family with many small primes of even multiplicity

Fix $Y\ge2$, $\eta,\delta>0$ and an integer $M\ge1$. There is a single rational Belyi map whose image gives primitive eighth-power triples

$$
                  B^8+(A^8-B^8)=A^8,\qquad A>B>0,
$$

with the following properties at every sufficiently large source height. Write $v_p=v_p(A^4+B^4)$ and $\mathcal P=\{Y<p<A^\eta:v_p>0\text{ is even}\}$. Then

$$
             \#\mathcal P\ge M,\qquad \prod_{p\in\mathcal P}p^{v_p-1}\ge A^{2-\delta}.       \tag{1}
$$

Rational abc is equivalent to its restriction to this image. The exponents in (1) can exceed two. The base map also preserves the entire squarefree kernel: for a primitive source slope $x/y$ and the corresponding positive output pair,

$$
                    \operatorname{sf}(A^4+B^4)=\operatorname{sf}(x^4+y^4).                     \tag{2}
$$

Here $\operatorname{sf}(m)$ is the product of primes of odd valuation in the positive integer $m$.

## The marked map and its critical divisor

The curve $u^2=t^4+1$ has an elliptic model

$$
 E:\quad v^2=z^3-4z,\qquad z=2(u+t^2),\quad v=2zt,\quad t=v/(2z).
$$

The quotient $\pi:E\to\mathbf P^1$ with coordinate $t$ has involution $P\mapsto T-P$, where $T=(0,0)$. Indeed the two points above $t=\infty$ are $O,T$; every degree-two fiber is linearly equivalent to $O+T$. Its four branch values are the primitive eighth roots, and the points above them satisfy $2P=T$. For any odd $N$, multiplication by $N$ commutes with this involution. It descends to $f_N\in\mathbf Q(t)$ with $\pi([N]P)=f_N(\pi(P))$ and degree $d=N^2$.

At $t=0$ the points $(2,0),(-2,0)$ are fixed by $[N]$, as are the two points above infinity. At $t=1$, the two points have $z=2(1\pm\sqrt2)$ and $v=2z$, and the doubling formula gives $2P=(2,0)$. Consequently $f_N(1)=\pm1$ since $t(-P)=-t(P)$. Thus $\beta=f_N^8$ sends $0,1,\infty$ into $0,1,\infty$.

Write $\mathcal B$ for the degree-four branch divisor on the $t$-line. Since $[N]$ is étale in characteristic zero, the local degree of $f_N$ at $\pi(P)$ is the local degree of $\pi$ at $[N]P$ divided by that at $P$. Multiplication by $N$ permutes the four solutions of $2P=T$, which have order four. Therefore

$$
                f_N^*\mathcal B=\mathcal B+2\mathcal C_N,
                \qquad \deg\mathcal C_N=2d-2,                                               \tag{3}
$$

where $\mathcal C_N$ is reduced and disjoint from $\mathcal B$. Its points are exactly $\pi(P)$ with $[N](2P-T)=O$ and $2P\ne T$. These are all the critical points of $f_N$, with local degree two; their images become $1$ under the eighth power. Thus $\beta$ is Belyi of degree $8d$. No real $t$ lies in $\mathcal C_N$: every real $t$ lifts to a real point of $E$, and all four branch values are nonreal. This also holds at infinity.

Choose coprime integral homogeneous coordinate forms $U,V$ of degree $d$ for $f_N$. There is an integral homogeneous form $C_N$ of degree $2d-2$, cutting out $\mathcal C_N$, such that

$$
             U(X,Z)^4+V(X,Z)^4=(X^4+Z^4) C_N(X,Z)^2.                                      \tag{4}
$$

To see that the constant in (3) is a rational square, the function $u([N]P)/u(P)$ is invariant under $P\mapsto T-P$, hence lies in $\mathbf Q(t)$. Its square is $(f_N(t)^4+1)/(t^4+1)$. On clearing denominators, (3) gives (4) with a rational polynomial square. The quotient by the monic $X^4+Z^4$ has integral coefficients, so Gauss's lemma gives an integral square root. For primitive $0<x<y=H$, let $g=\gcd(U(x,y),V(x,y))$. The homogeneous resultant bounds $g$ by a constant depending on $N$. Take $A,B$ to be the larger and smaller of $|U|/g,|V|/g$, omitting the finitely many slopes mapping to $0,\infty,\pm1$. Then $A\asymp_N H^d$ and (4) proves (2) exactly. The kernel identity holds in arbitrary primitive projective coordinates, including zero and infinity. Thus the inverse image in $\mathbf P^1(\mathbf Q)$ of the locus with any specified squarefree kernel is exactly that same locus. Also $|C_N(x,y)|\asymp_N H^{2d-2}$ by the absence of real zeros.

## Keeping individual primes small

Every point above $\mathcal C_N$ belongs to $E[4N]$. The endomorphism $(z,v)\mapsto(-z,iv)$ is defined over $\mathbf Q(i)$ and gives the action of $\mathbf Z[i]$. The complex period lattice is a rank-one module over this principal ideal domain, so $E[4N]$ is free of rank one over $\mathbf Z[i]/4N$. Galois over $\mathbf Q(i)$ commutes with this action. Hence every rational irreducible factor of $C_N$ has degree at most $2|(\mathbf Z[i]/4N)^\times|$. For $N$ a squarefree product of primes $\ell\equiv1\bmod4$, this gives the bound

$$
                      r_N=16d\prod_{\ell\mid N}(1-1/\ell)^2.                               \tag{5}
$$

Indeed $|(\mathbf Z[i]/4)^\times|=8$, and each $\ell$ splits into two residue fields of order $\ell$. The reciprocal sum of these split primes diverges after any fixed finite set is removed. We can thus require simultaneously $2/d<\delta$, $r_N<\eta d$, and $(2d-2)/r_N\ge M$. For every integral irreducible factor $C_i$ of $C_N$, each prime dividing $C_i(x,y)$ is $O_N(H^{\deg C_i})<A^\eta$ for all sufficiently large $H$.

For the lower cutoff, omit from $N$ all the odd primes $p\le Y$ and all prime divisors of $\#E(\mathbf F_{p^2})$ for those $p$. The curve has good reduction at every odd prime. If $\pi(P)\in\mathcal C_N$ were in $\mathbf P^1(\mathbf Q_p)$ at such a $p$, the two-point fiber would put $P$ in an extension of degree at most two. The nonzero odd-order point $Q=2P-T\in E[N]$ would reduce over $\mathbf F_{p^2}$. The reduction is injective on $E[N]$ since $p\nmid N$, contradicting the choice of $N$. Hence $v_p(C_N(x,y))$ is bounded uniformly on primitive pairs by compactness of the normalized projective coordinates over $\mathbf Z_p$. At $p=2$, the valuation of a sum of two coprime fourth powers is at most one. Applying this at the source and target of (4), with $g$ bounded, gives the same boundedness. These omissions leave the split-prime construction in (5) available.

## Keeping the contributing valuations even

An output prime of odd valuation divides $x^4+y^4$ to odd valuation by (2). By (3), the homogeneous resultant of $C_N$ and $X^4+Z^4$ is nonzero. Hence only finitely many fixed primes can contribute both to $C_N(x,y)$ and to the odd output support. We must also bound their valuations in $C_N$, since a resultant only bounds the smaller of two valuations.

For odd $p$ with $v_p(x^4+y^4)$ odd, the two coordinates are units and $p\equiv1\bmod8$. At a $p$-adic slope $t$ with $v_p(t^4+1)$ odd the quadratic field $L=\mathbf Q_p(\sqrt{t^4+1})$ is ramified. Its nontrivial automorphism exchanges $P$ and $T-P$. If $t\in\mathcal C_N$, the point $Q=2P-T$ would be nonzero of odd order dividing $N$, and this automorphism would send $Q$ to $-Q$. The residue field of $L$ is unchanged, so $2\bar Q=O$; the odd order forces $\bar Q=O$. But the formal group of this good elliptic curve over $L$ is torsion-free because $e(L/\mathbf Q_p)=2<p-1$: its formal logarithm preserves valuation and is injective on the maximal ideal. This contradiction proves that $\mathcal C_N$ has no such local point.

If the $C_N$-valuations in the odd-output locus were unbounded at a fixed such $p$, compactness would give a subsequence converging to a $p$-adic critical slope. The branch and critical divisors are disjoint, so $t^4+1$ is nonzero at the limit and its valuation is locally constant there. The limit would have odd valuation, just excluded. Together with the calculation at two, this bounds uniformly the entire part of $C_N(x,y)$ coming from odd output valuations.

For the remaining primes put $c_p=v_p(C_N(x,y))$ and $a_p=v_p(g)$. If $c_p>0$, (4) gives $(v_p-1)_+\ge c_p-4a_p$. The small-prime and odd-valuation bounds, the upper cutoff (5), and the bounded $g$ now give

$$
                \prod_{p\in\mathcal P}p^{v_p-1}\gg_N |C_N(x,y)|
                  \gg_N A^{2-2/d}.
$$

For distinctness, assign each prime dividing $\prod_i C_i(x,y)$ to a factor where its valuation is largest. Pairwise nonzero homogeneous resultants bound, uniformly in $(x,y)$, the unassigned part of each $C_i(x,y)$. The preceding bounds also control its part coming from $p\le Y$, odd output valuations, and primes where division by $g^4$ leaves zero output valuation. Each $|C_i(x,y)|\gg_N H^{\deg C_i}$ since it has no real zero. Thus eventually every factor supplies a distinct member of $\mathcal P$. There are at least $(2d-2)/r_N$ factors by (3) and (5). This proves (1).

## Transfer of the abc inequality

For source radical $R_0=\operatorname{rad}(xy(y-x))$, the image has height $A^8\asymp_N H^{8d}$ and radical $R=\operatorname{rad}(AB(A^8-B^8))\ll_N R_0 H^{8d-1}$. Indeed a degree-$q$ Belyi map on $\mathbf P^1$ has $q+2$ distinct geometric points over its three boundary values by Riemann–Hurwitz. Three of these points for $\beta$ are the marked $0,1,\infty$, leaving a homogeneous factor of degree $q-1$ for the extra boundary support, here $q=8d$. Resultants absorb the fixed primes of bad reduction. A bound $A^8\ll_e R^{1+e}$ on the image therefore gives $H^{1-(q-1)e}\ll_e R_0^{1+e}$. Choosing $e=\varepsilon/(q+(q-1)\varepsilon)$ recovers the usual exponent $1+\varepsilon$ at the source. The forward implication applies abc to the primitive image triples. [Marked-map transfer](abc_marked_rational_radical_bounds.md)

## An exact check at $N=3$

The tripling map on this model gives

$$
 f_3(t)=\frac{t(t^8-6t^4-3)}{3t^8+6t^4-1},\qquad C_3(t,1)=t^{16}+28t^{12}+6t^8+28t^4+1.
$$

Direct expansion gives (4). At $t=1/2$ the reduced ratio is $863/314$ and $863^4+314^4=17\cdot182209^2$. At $t=2/3$ it is $-54406/5949$ and $54406^4+5949^4=97\cdot300565249^2$. These preserve the source squarefree kernels $17$ and $97$. At $t=1/16410$, the source quartic is prime to $193$, the value of the homogeneous $C_3$ has $193$-adic valuation two, and the reduced output quartic has valuation four. This illustrates the distinction between geometric ramification index and integer valuation.
