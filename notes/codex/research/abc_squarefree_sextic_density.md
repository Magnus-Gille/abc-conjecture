# Simultaneously squarefree power triples and the large-square tail

There is a constant $c>0$ such that, for every sufficiently large $H$, at least $cH^2$ primitive pairs $1\le B<A\le H$ make **each** of the integers

$$
                 AB(A^n-B^n),\qquad \varphi(n)\le6,
$$

squarefree. One can require $A$, $B$ and $A-B$ all to be comparable to $H$. In particular the total log radical on these pairs is $(n+2)\log H+O(1)$ simultaneously for $n=7,9,14,18$.

For a proportion tending to one, the relevant quantity is a different count. For any fixed $n\ge1$ let $T_n(H)$ count the primitive pairs in the same box such that $p^2\mid AB(A^n-B^n)$ for some prime $p>H^2$. Write $R_n=\operatorname{rad}(AB(A^n-B^n))$. Then

$$
 \begin{aligned}
 \log R_n/\log H\longrightarrow n+2\text{ in probability}
      &\ \Longleftrightarrow\ T_n(H)=o(H^2),\\
 \mathbb E\big[(n+2)\log H-\log R_n\big]=O_n(1)
      &\ \Longleftrightarrow\ T_n(H)=O_n(H^2/\log H).
 \end{aligned}                                                        \tag{1}
$$

The probability and expectation are uniform over primitive pairs. The first condition even makes the unnormalized deficit tight in probability. Both equivalences concern the full integer radical with its actual prime multiplicities.

## Using the distinct-value theorem

Stewart and Xiao prove an asymptotic $C_{G,k} Z^{2/D}$, with $C_{G,k}>0$, for the number of distinct $k$-free integers of absolute value at most $Z$ represented by an integral binary form $G$ of degree $D\ge3$ and nonzero discriminant, with no fixed prime $k$th-power divisor. Their hypotheses on $k$ and the largest irreducible factor degree $r$ include $(k,r)=(2,6)$. [Stewart and Xiao, *On the representation of $k$-free integers by binary forms*](https://arxiv.org/abs/1612.00487)

Use the single form

$$
 G(X,Y)=XY\prod_{\varphi(d)\le6}\Phi_d(X,Y),\qquad D=\deg G.
$$

The indices are $1,2,3,4,5,6,7,8,9,10,12,14,18$. All factors are distinct and the largest degree is six. For each prime $p$ the pair $(p,1)$ gives $v_p(G(p,1))=1$, so the fixed-divisor condition holds. Replacing a primitive root of unity by its inverse preserves its order. Replacing it by its negative preserves the degree of its minimal polynomial since it generates the same number field. Thus the complete root set of $G$ on the projective line is stable under interchanging $X,Y$ and under sign changes. These operations preserve $|G|$ since the cyclotomic factors are monic with constant term $\pm1$.

To pass from a bound on values to a bound on the base height, write $T<\max(|X|,|Y|)\le2T$. The only real root directions of $G$ are the four lines $X=0$, $Y=0$, $X=Y$ and $X=-Y$, all simple. On a nonzero value in this shell,

$$
 |G(X,Y)|\gg T^{D-1}\min(|X|,|Y|,|X-Y|,|X+Y|).
$$

Indeed each nonreal cyclotomic factor, divided by $T^{\varphi(d)}$, is bounded away from zero on the compact unit shell. Of the four linear factors the three largest are $\gg T$, since no two of the four lines intersect on that shell. Each possible positive value of their minimum occurs on $O(T)$ pairs by counting the lines on which it is attained. Hence $0<|G|\le Z$ costs $O(Z/T^{D-2})$ pairs in that shell. Summing over doubling shells above $H$ costs $O(Z/H^{D-2})$.

Take $H=K Z^{1/D}$ for a sufficiently large fixed $K$. The last count is smaller than half the distinct-value main term, so $\gg H^2$ pairs of height at most $H$ represent squarefree values. Such pairs are primitive by homogeneity. Using signs and interchange puts them in $1\le B<A\le H$, with multiplicity at most eight. Each $AB(A^n-B^n)$ in the statement divides $G(A,B)$ since $d\mid n$ implies $\varphi(d)\le\varphi(n)$. Finally, pairs with $\min(B,A-B)<\eta H$ number $O(\eta H^2)$ for $H$ large. For a sufficiently small fixed $\eta>0$ this leaves the asserted positive proportion with all three lengths comparable to $H$.

## Which tail controls the mean

Let $F_n=AB(A^n-B^n)$. Each linear form $A,B,A-B$ takes a fixed positive value on at most $H$ pairs. Integrating $\Pr(U\le He^{-t})\ll e^{-t}$ shows that $\mathbb E\log(H/U)=O(1)$ for each of these forms. From $A^nB(A-B)\le F_n\le H^{n+2}$ it follows that $\mathbb E[(n+2)\log H-\log F_n]=O_n(1)$.

The expected repeated-prime loss from $p\le H^2$ is $O_n(1)$. For the details, at each $p^j$ the condition $p^j\mid F_n$ uses $O_n(1)$ projective classes. Determinant spacing within each class bounds the number of pairs by $O_n(1+H^2/p^j)$. For all levels $j\ge2$ with $p^j\le H^2$, dividing by the $\asymp H^2$ pairs and summing gives $O_n(\sum_p\log p/(p(p-1)))=O_n(1)$. For each $p\le H^2$ let $j_p$ be the least $j$ with $p^j>H^2$. Only $O_n(1)$ pairs have $p^{j_p}\mid F_n$. Taking the union over $p\le H^2$ gives exceptional probability $O_n(1/\log H)$ by Chebyshev, and the entire repeated-prime loss on any such pair is at most $(n+2)\log H$. [Projective classes and spacing](abc_binary_power_small_prime_excess.md)

The remaining loss vanishes off the $T_n(H)$ pairs. On each of them it is between $2\log H$ and $(n+2)\log H$. This proves (1) by taking expectations or applying Markov's inequality to the bounded-mean part. The bound $T_n(H)=o(H^2)$ alone suffices for tightness, because the remaining loss then vanishes outside a set of probability tending to zero.

At $n=7,9,14,18$, the only irreducible factors that can account for $p^2$ with $p>H^2$ are sextic. A linear or quadratic cyclotomic factor is too small; for these indices the other factors all have degree at most two. For $H$ large, $p\nmid n$ and a prime cannot divide two different factors since $X^n-1$ is separable modulo $p$. Estimates for squarefree values with a specified density can therefore be applied to (1) when they control **all lattice pairs carrying a large prime square**, including pairs already divisible by a small prime square. The positive constant in the distinct-value asymptotic suffices for the simultaneous positive-proportion statement above. An error exponent in a sextic large-square estimate would need separate verification before using it for the bounded-mean assertion. [Xiao, *Power-free values of binary forms and the global determinant method*](https://arxiv.org/abs/1505.05587)

The available source records confirm the statement about distinct values in the Stewart–Xiao abstract and the separate density focus in Xiao’s abstract. The full texts of Greaves and Stewart–Xiao could not be inspected in this audit. Consequently no numerical large-square error term is attributed here to either paper. [Greaves, *Power-free values of binary forms*](https://doi.org/10.1093/qmath/43.1.45) · [Stewart–Xiao abstract record](https://github.com/guanqun-yang/ArxivDB/blob/33098fc296f82f103a8c99a6957e20a52884c589/data/2016/1612.0xxxx.jsonl)
