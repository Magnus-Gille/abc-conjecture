# Combined prime powers on the Hall-type Pell progression

Let $n=7+12j$ and put

$$t=L_n-11,\quad z=F_n,\quad A=(L_n-6)^2-20,\quad B=(L_n-9)^2-5,\quad C_n=AB,\quad M_n=tzAB.$$

The triple $1728t+5(zB)^2=A^3$ is primitive. A counterexample sequence on this family would require $\log(M_n/\operatorname{rad}M_n)\ge\delta n$ for a fixed $\delta>0$ infinitely often. All estimates below also count the first copy of each prime. They therefore bound the excess from repeated copies. [Family and radical](hall_pell_direction.md)

## A prime pool of any size or location

For every integer $J\ge1$ and every rational prime $p$,

$$\sum_{J\le j<2J}v_p(M_{7+12j})\log p<1000J. \tag{1}$$

Consequently any set $S_J$ of $s$ primes, even one selected after examining the terms, contributes less than $1000Js$ to the whole block if $s>0$. In particular, for $s=o(J)$ and fixed $\delta>0$, the fraction of indices where these primes contribute at least $\delta n$ tends to zero. Taking all primes up to $P=o(J\log J)$ satisfies this condition by Chebyshev's estimate. Taking $P=J$ gives an exceptional fraction $O_\delta(1/\log J)$.

If at least $\eta J$ of the indices have $\log(M_n/\operatorname{rad}M_n)\ge\delta n$, their repeated prime divisors must include at least $12\eta\delta J/1000$ distinct primes. This follows by taking $S_J$ to be their union and using $n\ge12J$ on the block.

### Local periods and the proof of (1)

Write $\alpha=(1+\sqrt5)/2$ and $q=\alpha^{12}$. For $p\ge7$ work at a place over $p$ in $\mathbb Q(\sqrt5)$, with $v_p(p)=1$. The completion is unramified. Define $r_{p,e}$ as the multiplicative order of $q$ modulo $p^e$ in this completion. Equivalently, it is the least $r\ge1$ such that $p^e\mid F_{6r}$, because $q^r-1=\sqrt5\,\alpha^{6r}F_{6r}$. This description is independent of the choice of place.

For odd $n$, if $X=\alpha^n$, then $P(X)=\sqrt5\,X^6 M_n$ with

$$P(X)=(X^2-11X-1)(X^2+1)(X^4-12X^3+14X^2+12X+1)(X^4-18X^3+74X^2+18X+1).$$

Its discriminant is $-2^{54}3^{26}5^{23}$. For $p\ge7$, every root modulo $p$ is simple, so at most twelve residues modulo $p^e$ solve $P(X)=0$, by unique lifting. The values of $X=\alpha^7q^j$ are distinct during a period of length $r_{p,e}$. Thus there are at most twelve index classes modulo $r_{p,e}$ where $p^e\mid M_n$. For the two quadratics $C_n$ there are at most eight. [Polynomial and local factorization](hall_pell_valuation_bounds.md)

Put $r=r_{p,1}$ and $b=v_p(q^r-1)$. Binomial expansion at an odd unramified prime gives $r_{p,e}=r\,p^{\max(e-b,0)}$. Also

$$b\log p\le\log|N_{\mathbb Q(\sqrt5)/\mathbb Q}(q^r-1)|=\log(q^r+q^{-r}-2)<12r\log\alpha.$$

Count the valuation one exponent at a time, giving weight $\log p$ to each $e\ge1$ with $p^e\mid M_n$.

* If $r\le J$, the exponents $e\le b$ cost at most $24(J/r)b\log p<288J\log\alpha$ over the block. When $r>J$ these exponents are covered by the last item.
* For $e=b+k$, $k\ge1$, with $rp^k\le J$, the cost is at most $24J\sum_{k\ge1}\log p/(rp^k)\le24J$.
* Take the first $e$ with $r_{p,e}>J$. At this exponent at most twelve indices can occur in a block of $J$ consecutive indices. Every higher exponent is confined to those same indices. For each of them the entire valuation costs at most $\log M_n<6n\log\alpha<144J\log\alpha$. Indeed $t,z<\alpha^n$ and $A,B<\alpha^{2n}$.

The three bounds sum to at most $(2016\log\alpha+24)J<1000J$.

At 2, 3 and 5 the valuations on this progression are

$$v_2(M_n)=1,\quad v_3(M_n)=\begin{cases}2+v_3(j+1)&j \text{ even},\\0&j \text{ odd},\end{cases}\quad v_5(M_n)=1+v_5(n).$$

For 2, $L_n\equiv1\pmod4$ and $F_n$ is odd by their recurrences. For 3, use $t=L_{(n+5)/2}L_{(n-5)/2}$. The rank of 3 in the Fibonacci sequence is 4. Thus $3\mid L_m$ precisely for $m\equiv2\bmod4$, when $v_3(L_m)=v_3(F_{2m})=1+v_3(2m)$. Only the first Lucas index can qualify. Neither quadratic can vanish modulo 3. For 5, $L_n\equiv9\bmod10$ and $v_5(B)=1$. Writing $g=\alpha/\bar\alpha$ gives $v_5(g-1)=1/2>1/4$, so binomial lifting gives $v_5(F_n)=v_5(g^n-1)-1/2=v_5(n)$. The sums of $v_3(j+1)$ and $v_5(7+12j)$ on the block are bounded by $v_3((2J)!)$ and $v_5((24J)!)$, respectively. This proves (1) for these primes as well.

## Many primes with bounded multiplicities

For any $P\ge7$ and integer $K\ge1$,

$$\sum_{J\le j<2J}\ \sum_{p\le P}\min\{v_p(M_n),K\}\log p\ll J\sqrt{KP}+KP+J. \tag{2}$$

In particular, whenever $KP=o(J^2)$, the sum at a single index is $o(n)$ outside a set of indices of density zero. For instance this covers all primes $p\le J^{3/2}$ with up to $\lfloor J^{1/3}\rfloor$ copies of each. At primes with larger valuations the statement counts the first $\lfloor J^{1/3}\rfloor$ copies.

To prove (2), assign weight $\log p$ to every pair $(p,e)$ with $7\le p\le P$ and $1\le e\le K$. Their total weight $W$ is $O(KP)$. For any $R\ge1$, the weight of all pairs of order $r_{p,e}\le R$ is $O(R^2)$ even if both cutoffs are removed. Indeed the largest qualifying power of each prime divides

$$\prod_{1\le m\le R}|N_{\mathbb Q(\sqrt5)/\mathbb Q}(q^m-1)|,$$

whose logarithm is $O(R^2)$. The smaller exponents for this prime contribute just the logarithm of the largest power when added together. The sum of weights divided by order over the finite set is therefore

$$\sum_{p,e}\frac{\log p}{r_{p,e}}\le\int_1^\infty\frac{\min(W,c u^2)}{u^2}\,du\ll\sqrt W.$$

Each pair can hit at most $12(J/r_{p,e}+1)$ indices. Summing and adding the three fixed primes via (1) gives (2). The density assertion follows by Markov's inequality on dyadic blocks. More explicitly, if the block sum divided by $J^2$ tends to zero, taking the square root of that ratio as the threshold for the per-index sum divided by $J$ gives a vanishing exceptional fraction.

## A restriction at every index, without a prime-size cutoff

For $p\ge7$ count each copy of $p$ in $M_n$ by its exponent $e=1,\ldots,v_p(M_n)$. Uniformly in $R\ge1$, the copies for which $r_{p,e}\le R$ satisfy

$$\sum_{p\ge7}\ \sum_{\substack{1\le e\le v_p(M_n)\\r_{p,e}\le R}}\log p
\ll R^{3/2}+R\bigl(\tau(n-5)+\tau(n)+\tau(n+5)\bigr). \tag{3}$$

Here $\tau(k)$ is the number of positive divisors of $k$. Taking $R=n^{2/3}/\log(2n)$ gives $o(n)$ at **every** index, since $\tau(k)=k^{o(1)}$. Thus a counterexample on this progression must get a linear contribution from larger local periods even if its indices form a very sparse set.

### The two quadratic factors

The total weight of pairs $(p,e)$ with order at most $R$ that hit $C_n$ at **any** index in the progression is $O(R^{3/2})$. To see this, take a root $\beta$ of either quartic in $P$. Its target $\beta-\beta^{-1}=u$ is $6\pm2\sqrt5$ or $9\pm\sqrt5$. The discriminant $u^2+4$ is nonsquare in $\mathbb Q(\sqrt5)$, since its rational norm is either 720 or 6480, both nonsquares in $\mathbb Q$. Hence there is an involution fixing $\alpha$ and taking $\beta$ to $-1/\beta$. The units $\alpha,\beta$ are multiplicatively independent. Applying that involution to a putative relation would force a power of $\beta$ to be a root of unity, whereas $\beta$ is real with $|\beta|\ne1$. [Root fields](hall_pell_shared_divisors.md)

At a hit of $p^e\mid C_n$, simple lifting supplies a root $\beta$ in the local field with $\beta\equiv\alpha^n\bmod p^e$. The subgroup generated by the reductions of $\alpha,\beta$ has order at most $12R$ if $r_{p,e}\le R$, because it is generated by $\alpha$ and $q=\alpha^{12}$. Let $L=\lfloor\sqrt{12R}\rfloor$. Two of the $(L+1)^2$ residues $\alpha^a\beta^b$ with $0\le a,b\le L$ must coincide. Thus $p^e$ divides the absolute rational norm of some nonzero $\alpha^a\beta^b-1$ with $|a|,|b|\le L$ and $(a,b)\ne(0,0)$. The elements are algebraic integers even for negative exponents, since both bases are units.

Multiply these nonzero absolute norms over all such pairs and the finitely many quartic roots. There are $O(L^2)$ factors, each with logarithm $O(L)$ by bounding its conjugates. The product is a single positive integer divisible by the largest qualifying power of each prime across all the indices. Its logarithm is $O(L^3)=O(R^{3/2})$. This proves the required bound for $C_n$.

This argument also gives a stronger average statement for $C_n$. Summing the classes over a block, the weight for $r_{p,e}\le R$ is $O(J\sqrt R+R^{3/2})$, by partial summation of the weight bound and the count $8(J/r_{p,e}+1)$. On taking $R=J^{4/3}/\log(2J)$ these copies contribute $o(n)$ outside a set of density zero.

### The Fibonacci and Lucas factors

For $p\ge7$ no two of $t,z,A,B$ share $p$. Moreover at most one of $L_{(n+5)/2}$ and $L_{(n-5)/2}$ can contain $p$. Otherwise $g^{(n+5)/2}=g^{(n-5)/2}=-1\bmod p$ would give $g^5=1\bmod p$, contradicting the appearance of $-1$ in this group of odd order. The identity $F_{2m}=F_mL_m$ now shows that each $p^e\mid tz$ divides $F_k$ for one of $k=n,n+5,n-5$. [Factor separation](hall_pell_direction.md)

Write $\rho$ for the order of $g=\alpha/\bar\alpha$ modulo $p^e$. Binet's formula gives $\rho\mid k$ and $p^e\mid F_\rho$. Since $g^6=q$, we have $\rho\le6r_{p,e}$. All the qualifying prime powers in $tz$ are therefore accounted for by

$$\prod_{k\in\{n-5,n,n+5\}}\ \prod_{\substack{d\mid k\\d\le6R}}F_d.$$

Its logarithm is $O(R\sum_k\tau(k))$ because $\log F_d=O(d)$. This completes (3).

The mean bounds allow exceptional indices. The pointwise bound permits a linear contribution at long local periods. Either sufficiently many such copies or a single sufficiently large repeated prime could still produce a positive limiting excess along a sparse sequence.
