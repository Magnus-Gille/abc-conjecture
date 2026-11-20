# Simultaneous square primes on the Pell orbit

Write $F_n=|F_{11}(a_n,b_n)|$, where $b_n+a_n\sqrt2=(1+\sqrt2)^n$. At the good primes where $g=(1+\sqrt2)^4$ increases its order from $d_p$ modulo $p$ to $pd_p$ modulo $p^2$, mark $p$ whenever $p^2\mid F_n$. Let $K$ count the marks, $Q$ be their squarefree product, and $L=\log Q$. First regard the index as a Haar-random profinite integer. For ordinary integer indices these laws give the limiting distribution with any increasing cutoff $X(N)\to\infty$ for which $\pi(X(N))=o(N)$, including $N\log N/\log\log N$.

The number of simultaneous marks and their total logarithmic size satisfy
\[
 \limsup_{k\to\infty}\frac{\log\Pr(K\ge k)}{k\log k}\le-1,\qquad
 \limsup_{t\to\infty}\frac{\log\Pr(L\ge t)}{\sqrt{t\log t}}
       \le-\frac{2}{\sqrt3}.
\]
Consequently $K$ has exponential moments of all orders. Also $\mathbb E\exp(c\sqrt{L\log(2+L)})<\infty$ for $c<2/\sqrt3$. For the product $Q_k$ of the largest $k$ marks, including every mark if there are fewer than $k$, the ordinary power moment $\mathbb E Q_k^s$ is finite for every $0<s<2/(3k)$. These are bounds for the distribution of simultaneous primes rather than just the probability of at least one prime. The same proofs give these bounds when every good prime is considered and the marking condition is $v_p(F_n)>v_p(g^{d_p}-1)$. [Local square classes and summable order tail](abc_cm_pell_index_square_sieve.md)

## Free coordinates in joint prime conditions

A mark at $p$ occupies $h_p\le50$ classes modulo $p d_p$, with distinct images modulo $d_p$. The set of marks has finite expected cardinality because
\[
   \sum_{p>Y}\frac{h_p}{p d_p}\ll\frac{Y^{-\alpha}}{\log Y},
   \qquad \alpha=2/3 .
\]
In particular almost every profinite index has finitely many marks. For any finite collection $B$ of primes and nonnegative $w_p$,
\[
    \mathbb E\prod_{p\in B}(1+w_p\mathbf1_{p\text{ marked}})
       \le \prod_{p\in B}(1+w_p/p).                                    \tag{1}
\]
Indeed process the primes in increasing order. When $p$ is added, it divides neither any smaller prime's period nor $d_p$, because $d_q\mid q\pm1$. After additionally conditioning on the index modulo $d_p$, at most one of the $p$ possibilities for the independent coordinate modulo $p$ is marked. The same inequality holds conditional on a particular index class modulo $M$ provided each $p\in B$ is prime to $M$. In particular a specified finite set $B$ is marked with probability at most $1/\prod_{p\in B}p$.

For a prescribed collection $B$ one can retain the coprime part of each new order. Set $c_p=\gcd(d_p,\operatorname{lcm}_{q<p,\ q\in B}(q d_q))$, taking the empty least common multiple as 1. In an earlier residue class, refinement to $d_p$ gives $d_p/c_p$ equally likely classes. At most $h_p$ of them can hit a target. The new prime coordinate still costs $1/p$, so for $s>0$ the squarefree product over this collection satisfies
\[
 \mathbb E Q_B^s\le\prod_{p\in B}\left(1+(p^s-1)
             \min\left\{\frac1p,\frac{h_p c_p}{p d_p}\right\}\right).
\]
Monotone convergence extends the finite-product inequality to infinite collections. In particular, if $c_p\ll p^\kappa$ for some $0\le\kappa<2/3$, then the ordinary power moment is finite for $0<s<2/3-\kappa$. This follows by partial summation of the local tail. Bounded shared divisors give the full range $s<2/3$; the rank-stratified exponents apply when the collection has a larger local tail exponent. This condition concerns intersections of the actual periods, which can be checked before imposing specific residues.

For the count choose $Y=\exp(2k\log k)$. The probability of a larger mark is $O(Y^{-2/3})$. On $p\le Y$, (1) gives the exponential generating bound $\mathbb E z^{K_Y}\le \exp((z-1)\sum_{p\le Y}1/p)$ for $z\ge1$. The reciprocal prime sum is $O(\log\log Y)=O(\log k)$. Choosing $z=k/(C\log k)$ for a sufficiently large constant bounds the remaining probability by $\exp(-k\log k+O(k\log\log k))$. Also $\Pr(\max p>Y)\ll Y^{-\alpha}/\log Y$. Since $Q_k\le(\max p)^k$ with the empty maximum taken as 1, this proves the power moment claim.

## Conditioning on the largest mark

Group the possible largest mark $q$ into integer shells $y\le\log q<y+1$, $y\ge1$. The sum of the probabilities of the individual $q$ marks in this shell is $O(e^{-\alpha y})$. Given a specified square class at $q$ modulo $q d_q$, the product of all smaller primes dividing $d_q$ is at most $d_q\le q+1$. Hence on the event that $q$ is the largest mark, the logarithmic contribution from $q$ and those smaller primes is at most $2(y+1)+1$. All remaining primes $p<q$ have free $p$ coordinates under this conditioning. For an upper bound it suffices to condition on the $q$ class and drop the requirement that $q$ is largest after restricting this remaining sum to $p<q$.

Put $v=y+1$. For $s\ge0$ apply (1) with $w_p=p^s-1$. Convexity gives $p^s-1\le (e^{sv}-1)\log(p)/v$ for $p\le e^v$. The elementary bound $\sum_{p\le e^v}\log(p)/p\ll v$ then gives the conditional moment bound $\exp(C(e^{sv}-1))$. For $u=(t-2v-1)/v$ large take $sv=\log(u/C)$. The conditional probability of $L\ge t$ with this largest prime is bounded by $\exp(-u\log u+O(u))$. For bounded or negative $u$ use the bound 1.

Combining the two factors, a shell costs $\exp(-\alpha y-u\log u+O(u))$ when $u$ is large. Put $B=\sqrt{t\log t}$. Uniformly for $y/B$ in any compact subinterval of $(0,\infty)$, the negative logarithm divided by $B$ is at least
\[
             \alpha(y/B)+1/(2(y/B))+o(1)\ge\sqrt{2\alpha}+o(1).
\]
For $y/B<A$ the conditional $u\log u-O(u)$ bound alone has limiting coefficient at least $1/(2A)$, by monotonicity. For $y/B>B_0$ sum the geometric shell tail, with coefficient $\alpha B_0$. Choosing $A$ small and $B_0$ large covers the two outer ranges. There are $O(B)$ shells in the intervening range. This proves the stated coefficient $\sqrt{2\alpha}=2/\sqrt3$. Restricting marks to primes with exactly $h$ hit targets replaces $\alpha$ throughout by $s/(s+1)$, $s=\min(h+1,50)$.

## All repeated copies of a prime

The same upper tail and stretched-exponential moments hold for the larger variable
\[
                L_* = \sum_{p\ \mathrm{regular}}(v_p(F_n)-1)_+\log p .
\]
Here the mark still begins at depth two, and every further copy contributes another $\log p$. Given the root class at the largest mark $q$ modulo $q d_q$, let $a_p=v_p(q d_q)$ for $p\le q$. The contribution allowed by these fixed digits is at most $\sum_p a_p\log p=\log(qd_q)$. For the excess past those digits put $Z_p=(v_p(F_n)-1-a_p)_+$. Expose index coordinates prime by prime, including all digits of each smaller prime. Every divisor of $d_p$ is below $p$. Conditional on the earlier coordinates and on the fixed $a_p$ digits at $p$, the probability that $Z_p\ge j$ is at most $p^{-j}$, by the unique index lift at each precision. This also applies at $q$, where the first digit was fixed by its square class. Therefore
\[
  \mathbb E[p^{sZ_p}\mid\hbox{prior coordinates}]
       \le 1+\frac{p^s-1}{p(1-p^{s-1})},\qquad 0\le s<1 .
\]
For $s\le1/2$ this changes only the absolute constant in the bound $\exp(C(e^{sv}-1))$ for the shell. Choose $s=\min(1/2,\log(u/C)/v)$ when $u$ is large. If the cap at $1/2$ is active, the conditional bound is at most $\exp(-uv/2+u)$, which is $\exp(-c t)$ on these small shells since the first possible prime is 683. Else the previous optimization applies. The resulting limiting upper coefficient remains $-2/\sqrt3$. For the all-good-prime version replace $(v_p-1)_+$ by $(v_p-b_p)_+$, using the intrinsic initial depth in the index sieve. For each fixed threshold, the moving-cutoff distribution transfers as before: capping the finitely many retained valuations beyond that threshold suffices to test the event.

For a finite prescribed list the excess product has a finite ordinary power moment at every $s<1$, by the same conditional geometric calculation without an initial fixed modulus. Once the list includes any regular prime with a visited target, the moment diverges at $s\ge1$ because that single prime attains each further depth with geometric probability. The empirical moment bounds below are for the squarefree product $Q$.

## Sampling integer indices

For the moving cutoff, truncation at a fixed prime $Y$ gives a finite periodic joint law. Its discrepancy from the law with primes through $X(N)$ is at most the probability of any larger qualifying mark. The upper bound for this discrepancy is $O(Y^{-2/3}/\log Y+\pi(X(N))/N)$ apart from the vanishing discrepancy for the fixed finite period. Taking successive limits gives the asserted distribution. The same argument holds for the termwise cutoff $p\le X(n)$ by discarding its finite initial segment for each fixed $Y$.

Moment statements for the empirical index distribution can be proved for slower growing cutoffs. For any fixed positive integer $k$, expand $L_X^k$ into ordered prime tuples. Each joint event is a union of at most $50^k$ classes for the least common multiple of its periods. Each such class differs from its Haar density by at most $1/N$ in the sample $1\le n\le N$. Since $\sum_{p\le X}\log p\ll X$,
\[
   \left|\mathbb E_{n\le N}L_X^k-\mathbb E_{\rm Haar}L_X^k\right|
        \ll_k X^k/N .
\]
Thus all fixed $k$-th log moments converge for $X=o(N^{1/k})$ with $X\to\infty$. For $X=c_0\log N$ with sufficiently small fixed $c_0>0$, the full period is $\exp(O(X))\le N^{1/2}$. The sample error for the stretched-exponential moment is bounded by this period divided by $N$, times the supremum of the weight, which is $\exp(O(\sqrt{X\log X}))=N^{o(1)}$ because $L_X\le\sum_{p\le X}\log p\ll X$. Thus these moments converge on that cutoff as well. The near-$N\log N$ result above is convergence of the distributions.

## An explicit progression with 1,716 exact squares

There is one fixed progression on the **unmodified Pell orbit** on which 1,716 distinct primes, from 683 to 9,997,747, simultaneously satisfy $p^2\parallel F_n$. Their squarefree product has 36,848 bits. The progression modulus has 101,812 bits, so its density is greater than $2^{-101812}$. In particular $\Pr(K\ge1716,\ L>36847\log2)>2^{-101812}$. This statement marks a finite set of primes and imposes no conditions at the others.

The witness consists of triples $(p,d,r)$. For each one, $d$ is the exact order of $g$ modulo $p$, the order increases modulo $p^2$, and $F_r$ is zero modulo $p^2$ and nonzero modulo $p^3$. Since $g^{dp^2}=1$ modulo $p^3$, the Laurent identity shows that the entire congruence $n\equiv r\pmod{dp^2}$ preserves that valuation. Merging the congruences with the generalized Chinese remainder theorem produces a nonnegative representative of 101,811 bits. Its SHA-256 digest, on the shortest big-endian unsigned byte representation, is `a5eec969c7df01b24804213315bfb24e6d54513836a8667f2a401b70d728b5e3`. The conditions were found by trying compatible lifts of local orbit roots in increasing prime order. The verifier checks each witness directly from the division polynomial. [Modular witness](abc_cm_pell_simultaneous_square_witness.csv) · [Exact verifier](abc_cm_pell_simultaneous_square_verify.py)

Small simultaneous examples can also be certified as first visits. Starting with 683 and successively adjoining the primes in the first column, the table gives the least positive $n$ at which all their squares divide $F_n$. Each listed prime has exact depth two at that first visit, as verified modulo its cube. The verifier obtains the square classes in each local period using its first nonzero derivative and exhausts their compatible combinations.

| Prime adjoined | Number of joint classes in their least common period | Least positive index |
|---:|---:|---:|
| 683 | 14 | 1,213 |
| 1,409 | 14 | 4,196,890 |
| 2,179 | 348 | 5,274,743,585,530 |
| 2,267 | 340 | 97,751,649,103,127,879 |

## An exact atom for each of the $2^{1716}$ subsets

Every subset of the marked list is itself the **exact** set of regular square marks on a positive-measure set of profinite indices. The same pattern has positive limiting natural density with the moving cutoff above. One may even specify, independently, an arbitrary exact exponent $e_p\ge1$ at all 1,716 primes and exclude every additional regular square mark. This concerns the growing-cutoff law; squares beyond the cutoff at an individual integer index are unrestricted.

To check this, start with the period from the witness and close it under the periods of eligible prime divisors. Every possible good prime of the given full factor is $1$ or $67\bmod88$. At each prime $q$ in these classes dividing the current modulus, outside the marked list, adjoin $q d_q$ to the least common multiple. Any newly introduced prime factor of $d_q$ is smaller than $q$, so the procedure terminates. In this witness just 53 extra class-compatible primes arise. The verifier checks $q^2\nmid F_n$ at the retained index for each of these 53 primes. More importantly, **none** of the 1,716 selected primes divides any of the retained orders. The enlarged modulus has 101,887 bits. Dividing by the square of the selected prime product leaves a 28,192-bit modulus $B$ coprime to that entire product. [Exact closure and modular checks](abc_cm_pell_simultaneous_square_verify.py)

Keep the witness residue modulo $B$. This preserves every avoidance just checked and the visited orbit class modulo $d_p$ at each selected prime. On that orbit class $p\mid F_n$. Each extra precision selects one out of $p$ new index digits. Because the selected primes are distinct and prime to $B$, their digits are independent under this conditioning. The density of the prescribed valuation profile before sieving further primes is exactly
\[
       \lambda=\frac1B\prod_{p\text{ selected}}(1-1/p)p^{1-e_p}.
\]
Its defining period has the same prime factors as the closed modulus. Every remaining eligible prime has a free coordinate modulo itself while sieving in increasing order. The density surviving through $Y$ is consequently at least $c\lambda/\log Y$ for an absolute $c>0$, by (1)'s free-coordinate argument applied to avoidance. The loss from larger primes is $O(Y^{-2/3}/\log Y)$ unconditionally. Taking $Y$ a sufficiently large constant times $\lambda^{-3/2}$ proves a lower bound $\gg\lambda/\log(2/\lambda)$ for the exact profile with all other regular square marks excluded. This bound is uniform in the prescribed exponents. Setting $e_p=2$ on a chosen subset and $e_p=1$ on its complement gives the claim.
