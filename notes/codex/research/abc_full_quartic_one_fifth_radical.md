# An effective one-fifth exponent for the height in terms of the full radical

On the primitive congruent-six orbit at every positive odd index, let $C=4w_n^4$ and $R=\operatorname{rad}(6a_n c_n d_n w_n)$. Then, with effectively computable absolute constants,
$$
             \log C\ll R^{1/5}(\log(2R))^3,\qquad
             n\ll R^{1/10}(\log(2R))^{3/2}.
$$
Equivalently $R\gg n^{10}/(\log(2n))^{15}$. The additional input beyond the three primitive abc triples is the uniform lower bound
$$
                    \operatorname{rad}(a_n)\gg n^2/(\log(2n))^3.          \tag{1}
$$

## One large prime in the quartic form

The orbit supplies coprime odd integers $x,y$ with
$$
       w_n=(x^2+3y^2)/4,\qquad F(x,y)=x^4-18x^2y^2+9y^4=-8a_n^2.
$$
In particular $h(x:y)=\tfrac12\log w_n+O(1)\asymp n^2$ for large $n$, where $h$ is logarithmic projective Weil height. [Quartic and index normalization](abc_full_quartic_signature.md)

If $a_n=p^e$ for a single prime $p$, we claim
$$
                       n^2\ll p(\log(2p))^3.                              \tag{2}
$$
The case $a_n=1$ gives an effective absolute bound for $n$ by the same argument with no $p$. Any prime of $a_n$ is greater than 3. The splitting field of $F(X,1)$ is the totally real Galois field $K=\mathbf Q(\sqrt2,\sqrt3)$ of degree 4, with Galois group $C_2\times C_2$, acting regularly on the four roots $\alpha_i=\pm\sqrt6\pm\sqrt3$. The discriminant of the monic polynomial is $2^{14}3^6$. A prime $p>3$ dividing $F(x,y)$ does not divide $y$ by primitivity and monicity, and hence fixes a root on reduction. Regularity of the action shows that $p$ splits completely. The absolute norm of each of the four primes above it is $p$.

For each place $\mathfrak p$ above $p$, exactly one of the four integral factors $\gamma_i=x-\alpha_i y$ vanishes modulo $\mathfrak p$. Their product vanishes and their pairwise differences are units there, since $p\nmid y\operatorname{disc}(F)$. Each factor is assigned to exactly one of the four places, since the Galois group acts transitively on the factors and permutes the four places. Choose three distinct roots. Take $S$ to contain the four archimedean places, all places above 2 and 3, and only the three places assigned to these chosen factors. Their integral ideals then have support in $S$, since their product with the fourth factor is $-8p^{2e}$. In the unit case take only the fixed places. Its cardinality is at most 15. The elementary affine identity is
$$
    \frac{\alpha_2-\alpha_3}{\alpha_2-\alpha_1}\frac{\gamma_1}{\gamma_3}
    +\frac{\alpha_3-\alpha_1}{\alpha_2-\alpha_1}\frac{\gamma_2}{\gamma_3}=1 .
$$
The coefficients are nonzero fixed elements of $K$, and both unknowns are $S$-units. The effective input is Theorem 1 of K. Győry and K. Yu, *Bounds for the solutions of S-unit equations and decomposable form equations*, Acta Arith. 123 (2006), 9–41. For $\alpha U+\beta V=1$, in the notation $P_S=\max(2,\max_{\mathfrak p\in S_f}N\mathfrak p)$, $R_S$ the $S$-regulator, $H=\max(1,h(\alpha),h(\beta))$ and $\log^*(u)=\max(1,\log u)$, the fixed-field specialization used here is
$$
 \max(h(U),h(V))\ll_{K,|S|}
     P_S R_S\left(1+\frac{\log^*R_S}{\log^*P_S}\right)H .
$$
See also the [fixed-field unit-equation bound and regulator argument](abc_eisenstein_slice_effective_pointwise.md). Here $H$ is bounded effectively independently of $p,e,n$. Also $P_S\ll p$ and $R_S\ll_K(\log(2p))^3$. The valuation lattice of the $S$-unit group inside the free lattice on $S_f$ has index at most the fixed class number of $K$, so $R_S\ll_K\prod_{\mathfrak p\in S_f}\log N\mathfrak p$. Only three factors in this product vary with $p$. Since $P_S\ge p$, the quotient of starred logarithms stays bounded. The two heights are thus $O(p(\log(2p))^3)$. When $a_n=1$, all quantities on the right are fixed. Finally $\gamma_1/\gamma_3$ is a fixed invertible Möbius transformation of $x/y$, so $h(x:y)\le h(\gamma_1/\gamma_3)+O_K(1)$. This proves (2) without an assumption on the exponent $e$.

## From a prime index to every index

At prime index $q$, every $p\mid a_q$ is a good primitive divisor for the integral point $G+(0,0)=(12,36)$, as $a_q=B(q(G+(0,0)))$, $q$ is prime and the index-one denominator is 1. Hence $4q\mid\#E(\mathbf F_p)$ and $p>q$. Two distinct primes already give $\operatorname{rad}(a_q)>q^2$. For one prime, (2) gives $p\gg q^2/(\log(2q))^3$: if $p\ge q^2$ there is nothing to check, and otherwise $\log(2p)\ll\log(2q)$. The effective bounded-index unit case is absorbed in the constant. This proves (1) at every prime index.

There is a fixed effective cutoff beyond which every $a_j$ has a good primitive prime of order $j$ for $G+(0,0)$. One can use David's effective complex elliptic logarithm lower bound and the elementary primitive-divisor inequality as explained in the [divisor-sensitive bound](abc_full_quartic_divisor_sensitive_radical.md). Thus if $n=q^2$ is large, $\operatorname{rad}(a_n)$ contains the disjoint product of $\operatorname{rad}(a_q)$ and a prime exceeding $q^2$. This gives (1). At all other composite indices, $\tau(n)\ge4$ and the same primitive-divisor argument gives $\operatorname{rad}(a_n)\gg n^{\tau(n)/2}\ge n^2$; the constant covers all omitted small divisors independently of $n$.

In fact the enhanced prime-index bounds can be multiplied at all prime $q\mid n$, since their primes have different exact orders. Combining with one primitive at each remaining large divisor yields, for each $\eta>0$,
$$
       \operatorname{rad}(a_n)\gg_\eta n^{\tau(n)/2}\operatorname{rad}(n)^{1-\eta}.
$$
Indeed each prime divisor $q$ upgrades its factor $q$ by $\gg q/(\log(2q))^3$. Each such upgrade exceeds $q^{1-\eta}$ for all sufficiently large $q$, and the finitely many small primes cost a fixed overall constant.

## Full radical conclusion

Set $U=2w_n-c_n,\ V=2w_n+c_n$. The radicals of $a_n^2+c_n^2=2w_n^2,\ U+V=4w_n,\ U+2c_n=V$ have product $2R^2/\operatorname{rad}(a_n)$ exactly. Each largest term exceeds $w_n$, and $\log w_n\asymp n^2$. Applying Stewart–Yu to the smallest radical yields
$$
              n^{18}\operatorname{rad}(a_n)\ll R^2(\log(2R))^{27}.
$$
This already implies $\log(2n)\ll\log(2R)$. Substitution of (1) now gives $n^{20}\ll R^2(\log(2R))^{30}$, as claimed. [Primitive triples and Stewart–Yu calculation](abc_full_quartic_divisor_sensitive_radical.md)
