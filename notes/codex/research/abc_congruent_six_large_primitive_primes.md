# A quartic threshold for first-appearance primes

Let \(G=(-3,9)\) on \(E:y^2=x^3-36x\), let \(B_r\) be the positive square root of the denominator of \(x([r]G)\), and let \(H=\widehat h(G)>0\). Write \(r_p\) for the reduction order of \(G\) at \(p\ge5\), and \(e_p=v_p(B_{r_p})\). The following bounds concern every sufficiently large odd \(r\).

1. **Unconditionally**, some first-appearance prime power satisfies
   \[
    \max_{r_p=r}p^{e_p}\gg_E r^4/(\log\log r)^2.
   \]
2. **Unconditionally**, for every fixed \(\eta>0\) there is a constant \(c_{E,\eta}>0\) such that
   \[
    \sum_{r_p=r}(e_p-1)\log p+
      \sum_{\substack{r_p=r\\p> r^4/(\log r)^\eta}}\log p
          \ \ge\ c_{E,\eta}r^2 .
   \]
   **If rational abc holds**, the first sum is \(o(r^2)\) and therefore
   \[
    \sum_{\substack{r_p=r\\p> r^4/(\log r)^\eta}}\log p
         \gg_{E,\eta} r^2.
   \]
   In particular an infinite sequence of odd \(r\) with every first-appearance prime at most \(r^4/(\log r)^\eta\), for one fixed \(\eta>0\), would disprove abc. The condition concerns distinct prime bases. The first assertion allows high powers of small bases.

This extends a [quartic bound for indices supported on inert primes](abc_full_quartic_signature.md) to general odd indices. It uses the [annihilator formula and abc triple](abc_congruent_six_gaussian_first_primes.md). It gives no infinite sequence satisfying the smoothness condition.

For a direct passage from an odd index to an abc triple, write \(x([r]G)=-3(a/w)^2\) as in the parametrization, so \(w=B_r\) and \(a^4+3b^2=4w^4\) is primitive. The inequalities \(a\le\sqrt2\,w\) and \(|b|\le 2w^2/\sqrt3\) give
\[
 \frac{4w^4}{\operatorname{rad}(6abw)}
   \gg \frac{w}{\operatorname{rad}(w)}\ge \exp(W_r),
 \qquad W_r=\sum_{r_p=r}(e_p-1)\log p .
\]
Here \(\log(4w^4)=4Hr^2+O(1)\) since odd multiples stay on the bounded real component. Thus \(W_r\ge c r^2\) at infinitely many odd indices supplies violations for one fixed positive abc exponent. This implication requires only the size of the largest term and the displayed radical inequality.

## Where a positive fraction of the logarithmic mass lies

Put \(\mathcal O=\mathbf Z[i]\). Let the ideal \(\mathfrak a\) range over all annihilators with \(\mathfrak a\cap\mathbf Z=(r)\). Write \(\mathfrak b=(r)/\mathfrak a\), and let \(\Phi(\mathfrak a)=|(\mathcal O/\mathfrak a)^\times|\). Assign \(\mathfrak a\) weight \(\Phi(\mathfrak a)\). These weights sum to \(J_2(r)=r^2\prod_{\ell\mid r}(1-\ell^{-2})\). Indeed a uniform element of the additive group \(\mathcal O/(r)\) has exact rational order \(r\) precisely when it is nonzero modulo \(\ell\) as a vector for every \(\ell\mid r\). Of those elements exactly \(\Phi(\mathfrak a)\) have Gaussian annihilator \(\mathfrak a\). The choices at distinct rational prime powers are independent under this conditioning.

For every fixed \(\delta>0\), the ideals with \(N\mathfrak b\le(\log r)^\delta\) have total weight at least \(c_\delta J_2(r)\), for some \(c_\delta>0\) independent of \(r\). Here are the details. An inert divisor \(\ell\) contributes nothing to \(\log N\mathfrak b\). At a split \(\ell^k\parallel r\), take the two coordinates in \(\mathcal O/(\ell^k)\simeq(\mathbf Z/\ell^k)^2\). At least one is a unit. The exponent of \(\ell\) in \(N\mathfrak b\) is the sum of the two truncated valuations, so for \(1\le j\le k\)
\[
 \Pr\big(v_\ell(N\mathfrak b)\ge j\big)
      =\frac{2\ell^{-j}}{1+1/\ell}.
\]
Choose a fixed small \(0<\theta<\delta/4\), and put \(y=(\log r)^\theta\). The probability that all split \(\ell>y\) dividing \(r\) contribute zero is bounded below in terms of \(\theta\). It is the product of \(1-2/(\ell+1)\); the reciprocal-prime sum from \(y\) to \(\log r\) is \(O_\theta(1)\) by Mertens, and for \(\ell>\log r\) dividing \(r\) it is \(O(1)\) since \(\sum_{\ell\mid r}\log\ell\le\log r\). The conditional expectation of the small-prime contribution is unchanged by independence and is bounded by
\[
 \sum_{\substack{\ell\le y\\\ell\equiv1\bmod4}}
       \frac{2\ell\log\ell}{\ell^2-1}
       \le (1+o(1))\log y
\]
by the prime number theorem in arithmetic progressions and partial summation. Markov's inequality proves the claim.

For each ideal the actual logarithmic first-depth mass over Gaussian places is
\[
 L(\mathfrak a)=2H\Phi(\mathfrak a)+
        O_E(2^{\omega(\mathfrak a)}\log(2N\mathfrak a)).
\]
There are \(r^{o(1)}\) ideals dividing \((r)\), each with \(r\le N\mathfrak a\le r^2\) if it contracts to \((r)\). The total error is \(r^{o(1)}\). Going back to rational primes divides the full sum by two: every prime of odd order splits, the two conjugate places have conjugate annihilators and the same initial depth \(e_p\). The sets \(N\mathfrak b\le L\) are conjugation-invariant. The depth assertion follows by multiplying a generator of the annihilator by the complementary factor to \(r\); at a good prime \(p\) of order \(r\), one has \(p\nmid r\) because \(4\mid\#E(\mathbf F_p)<4p\). Hence among these ideals for \(L=(\log r)^\delta\) there is rational first-depth mass \(\gg_{E,\delta}r^2\).

## A uniform count of small possible bases

All primes of odd order are \(1\bmod12\), and each relevant prime ideal of \(\mathbf Z[i]\) has Frobenius \(\pi\in\mathbf Z[i]\) with \(N\pi=p\) and \(\pi\equiv1\bmod\mathfrak a\). Indeed the Gaussian action is defined over \(\mathbf F_p\), the Frobenius commutes with this action and its centralizer in the rational endomorphism algebra is \(\mathbf Q(i)\). Integrality puts it in \(\mathbf Z[i]\), and Frobenius fixes \(G\bmod p\). Write \(\pi=1+\alpha (u+iv)\), where \((\alpha)=\mathfrak a\). For \(N\pi\le X\) the coordinates \(|u|,|v|\) lie in a box of side \(O(T)\), where \(T=2+\sqrt{X/N\mathfrak a}\).

Put \(D(r)=\prod_{\ell\mid r,\;\ell\equiv1\bmod4}(1-1/\ell)^{-2}\). The number of distinct candidate rational primes is
\[
 \ll \frac{T^2 D(r)}{\log T}.
 \tag{1}
\]
For clarity, use the dimension-one upper-bound sieve on the box. At \(\ell\equiv1\bmod4\) prime to \(r\), multiplication by \(\alpha\) is invertible on \(\mathcal O/(\ell)\). There are exactly \(2\ell-1\) residue pairs such that \(N(1+\alpha(u+iv))=0\bmod\ell\), the union of the two coordinate lines after an invertible affine change. For squarefree \(d\) composed of such primes, the predicted fraction is \(\prod_{\ell\mid d}(2\ell-1)/\ell^2\), with error \(O(2^{\omega(d)}(T+d))\) in the box count. This follows by counting each pair of residue classes with error \(O(T/d+1)\). Sieve up to \(T^{1/40}\) at level \(T^{1/4}\). The dimension-one sieve constant is uniform upon omitting primes; its product bound by Mertens in progressions is \(O(D(r)/\log T)\). The weighted remainders cost \(O(T^{5/4}(\log(2T))^5)\), and the small prime values excluded by sieving contribute at most \(T^{1/40}\) distinct primes. This proves (1), enlarging the constant for bounded \(T\). Finally \(1\le D(r)\ll\log\log(3r)\), by taking the product first over split primes up to \(\log r\), and bounding the remaining reciprocal sum over divisors of \(r\) as above.

For \(X=r^4/(\log r)^\eta\) and \(L=(\log r)^\delta\), the ideals \(N\mathfrak b\le L\) have \(N\mathfrak a\ge r^2/L\) and \(\log T\asymp\log r\). There are \(O(L)\) possible \(\mathfrak b\) by counting Gaussian integers in a disk. By (1) the logarithmic weight of the distinct prime bases at most \(X\) in all these ideals together is
\[
 \ll \frac{X L^2 D(r)}{r^2}=o(r^2),
\]
on taking \(0<2\delta<\eta\). The first-depth mass in the selected ideals is \(\gg_{E,\delta}r^2\). Subtract the small distinct bases; the remainder is bounded above by the sum of the excess \(W_r\) and the logarithmic weight of large distinct bases at that order. This proves the unconditional inequality in assertion 2. Rational abc implies \(W_r=o(r^2)\) by the explicit elliptic family of triples, giving its stated conditional consequence.

## The unconditional prime power

Use only the scalar annihilator \((r)\). Its rational first-depth mass is \(H\Phi((r))+r^{o(1)}\gg_E r^2/D(r)\), since the omitted inert Euler factors are bounded below by \(\prod_{\ell}(1-\ell^{-2})>0\). Let \(X\) be the largest \(p^{e_p}\) among its primes. If \(X>r^4\) there is nothing more to show. If \(X\le r^3\), the unsieved box count \(O(1+X/r^2)\) gives total mass \(O(r\log r)\), impossible for large \(r\). For \(r^3<X\le r^4\), formula (1) times \(\log X\) bounds the mass by \(O(XD(r)/r^2)\). Consequently \(X\gg_E r^4/D(r)^2\), proving assertion 1.

## An estimate in terms of the actual repetition

The constants in the argument also give, uniformly whenever \(W_r=o(r^2)\),
\[
 \max_{r_p=r}p\gg_E \frac{r^4}{(\log\log r)^2}
   \exp\!\left(-C_E\frac{W_r}{r^2}\log\log r\right).
\]
Here is the quantitative form of the weight argument. For \(3\le y\le\log r\), the probability of avoiding all contributions from split primes \(\ell>y\) is \(\gg\log y/\log\log r\): the product over all split primes in \((y,\log r]\) has this order by Mertens in progressions, since \(1-2/(\ell+1)=(1-1/\ell)/(1+1/\ell)\). The factors from divisors larger than \(\log r\) cost a bounded factor. There is an absolute \(K\) for which the expected small-prime contribution to \(\log N\mathfrak b\) is at most \((K/2)\log y\). The mass at \(N\mathfrak b\le y^K\) is consequently \(\gg_E r^2\log y/\log\log r\), uniformly over this interval. At \(X=c_0 r^4/[y^{2K}(\log\log r)^2]\) the small distinct bases in these ideals have log weight \(O_E(c_0r^2/\log\log r)\) by (1). Choose \(c_0>0\) small enough. The remaining sum \(W_r+\sum_{r_p=r,\;p>X}\log p\) is then at least \(c_1 r^2\log y/\log\log r\). Choose \(\log y=A(1+(W_r/r^2)\log\log r)\) with \(A>2/c_1\) and \(A\ge2\). This lies in the required interval for all sufficiently large \(r\) on the stated sequence, and the remaining sum exceeds \(W_r\). Some \(p>X\) exists, yielding the displayed estimate.
