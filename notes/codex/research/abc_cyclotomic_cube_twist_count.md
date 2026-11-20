# Primitive pairs with a small cofactor of a cube in a binary sextic

Let $F(X,Z)\in\mathbf Z[X,Z]$ be a fixed homogeneous sextic such that $f(x)=F(x,1)$ has degree six and six distinct roots. For $Y\ge1$, the number of primitive pairs of positive integers $A>B$ satisfying

$$
                     F(A,B)=b z^3,\qquad 1\le b\le Y,\quad z\in\mathbf Z_{>0},
$$

is $O_F(Y(1+\log Y)^{k_F-1})$ for some integer $k_F\ge1$. The count includes pairs of every height. In particular it applies to $F=\Phi_7=X^6+X^5Z+\cdots+Z^6$ and $F=\Phi_9=X^6+X^3Z^3+Z^6$, including when $z$ is required to be prime.

## The curve and the encoding

For $b\ge1$ take the smooth projective model $C_b$ of $b y^3=f(x)$. Over an algebraic closure its degree-three map to the $x$-line is totally ramified at each of the six roots of $f$. At infinity the order of the pole is six, divisible by three, so the cover is unramified there. Riemann–Hurwitz gives $2g-2=-6+6\cdot2=6$ and hence $g=4$.

For each fixed $b$ a solution gives the rational point

$$
                            (x,y)=(A/B,z/B^2)\in C_b(\mathbf Q).
$$

The reduced fraction $x$ determines its unique coprime numerator and positive denominator, and $yB^2$ recovers $z$. Thus this map is injective. Summing over $b$ gives an upper bound even if a pair occurs for several cofactors.

## Descent over a fixed field

Write $J_b=\operatorname{Jac}(C_b)$ and take the fixed number field $K=\mathbf Q(\zeta_3,J_1[3])$. On each $C_b$ over $K$ the deck transformation $\sigma(x,y)=(x,\zeta_3 y)$ has quotient $\mathbf P^1$. On $J_b$ the sum $1+\sigma+\sigma^2$ factors as pushforward and pullback through $\operatorname{Jac}(\mathbf P^1)=0$. Thus $\lambda=1-\sigma$ satisfies

$$
                   \lambda^2=-3\sigma,\qquad \deg\lambda=3^g.
$$

In particular $J_b[\lambda]\subset J_b[3]$ and $\sigma$ fixes $J_b[\lambda]$ pointwise. Over $K(\sqrt[3]b)$ the map $(x,y)\mapsto(x,\sqrt[3]b\,y)$ identifies $C_b$ with $C_1$. Its Galois conjugates differ by powers of $\sigma$, so the induced identification of the $\lambda$-kernels descends to $K$. The $\lambda$-kernel on every twist is therefore a constant group $(\mathbf Z/3\mathbf Z)^g$ over this single field.

Let $S$ consist of the finite primes of $K$ above $3b$ and the primes of bad reduction of $J_1$. At $v\notin S$ the algebra defined by $T^3-b$ is finite étale over the local integers. Hence the twist is unramified and $J_b$ has good reduction there, by the good reduction criterion for the Tate module. The isogeny $\lambda$ extends there to a finite étale isogeny of abelian schemes, since its degree is a unit. The inverse image of any local integral point is finite étale, and properness makes every local rational point integral. Consequently the Kummer classes in

$$
                  J_b(K)/\lambda J_b(K)\ \hookrightarrow\ H^1(K,J_b[\lambda])
$$

are unramified outside $S$. Since $\mu_3\subset K$ and the kernel is constant, this cohomology group identifies with $(K^\times/K^{\times3})^g$. An unramified class has valuation divisible by three at each $v\notin S$. The cubeclasses with this valuation property fit in the exact sequence

$$
 1\longrightarrow \mathcal O_{K,S}^{\times}/\mathcal O_{K,S}^{\times3}
 \longrightarrow \{a\in K^\times/K^{\times3}:3\mid v(a)\text{ for }v\notin S\}
 \longrightarrow \operatorname{Cl}(\mathcal O_{K,S})[3]\longrightarrow 1.
$$

Indeed the last map takes one third of the principal ideal divisor away from $S$. The $S$-unit theorem bounds the first group's dimension over $\mathbf F_3$ by $O_K(1+|S|)$, and the class group of the ring of $S$-integers is a quotient of the fixed class group of $K$, so its order is bounded. Since $|S|\ll_F1+\omega(b)$, this gives $\dim_{\mathbf F_3}J_b(K)/\lambda J_b(K)\ll_F1+\omega(b)$.

For $M=J_b(K)$ one has $3M=\lambda^2 M$, and multiplication by $\lambda$ maps $M/\lambda M$ onto $\lambda M/\lambda^2 M$. It follows that $[M:3M]\le[M:\lambda M]^2$, hence

$$
                      \operatorname{rank}J_b(\mathbf Q)
                      \le \operatorname{rank}J_b(K)\ll_F 1+\omega(b).
$$

## Summation over the cofactors

The uniform Mordell–Lang bound for curves over $\mathbf Q$ gives $\#C_b(\mathbf Q)\le c(4,1)^{1+\operatorname{rank}J_b(\mathbf Q)}$. In particular there is $M_F\ge1$ with $\#C_b(\mathbf Q)\le M_F^{1+\omega(b)}$ for every positive $b$. [Dimitrov, Gao and Habegger, *Uniformity in Mordell–Lang for curves*](https://arxiv.org/abs/2001.10276)

Choose an integer $k_F\ge M_F$. The number $d_{k_F}(b)$ of ordered factorizations of $b$ into $k_F$ positive factors is at least $k_F^{\omega(b)}$, by assigning each prime power exactly dividing $b$ to one of the factors. Summing over the first $k_F-1$ factors and bounding the remaining count by $Y$ divided by their product gives

$$
 \sum_{b\le Y}d_{k_F}(b)\le Y\left(\sum_{j\le Y}\frac1j\right)^{k_F-1}
                         \le Y(1+\log Y)^{k_F-1}.
$$

Together with the injective encoding this proves the asserted bound.
