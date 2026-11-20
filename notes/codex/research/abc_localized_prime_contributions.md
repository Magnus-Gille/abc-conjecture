# Counting square-addend triples in a short range

Put \(R(u,v)=\operatorname{rad}(uv(u-v)(u+v))\). A point is an integer \(1\le v\le u/2\) with \(\gcd(u,v)=1\), and it qualifies at \(\delta\) if \(R(u,v)\le u^{2-2\delta}\). It gives the primitive triple \(v^2+(u-v)(u+v)=u^2\).

**Localization.** Let \(\Lambda(u)>1\) tend to infinity, however slowly. If rational abc fails, there is an \(s'>3\) such that, for every sufficiently small fixed \(\delta>0\), infinitely many \(u\) each have \(\gg\delta^{-s'}\) qualifying points in one interval \([V,\Lambda(u)V]\). The interval is allowed to depend on \(u,\delta\). The implied constant can depend on the starting failure exponent.

**Four primes.** Take \(\Lambda(u)=\log u\). For each \(u\) choose any set \(S\) of at most four primes, even after seeing the qualifying points. Write \(Q(n)=n/\operatorname{rad}(n)\) and let \(T_{S^c}(u,v)\) be the factor of \(Q(v)Q(u-v)Q(u+v)\) supported on primes outside \(S\), retaining its full multiplicities. In any interval \([V,V\log u]\), at most \(O(\delta^{-3})\) qualifying points have
\[
 T_{S^c}(u,v)\le\operatorname{rad}(u)\,u^\delta.
\]
This upper bound is unconditional for \(0<\delta<1\) and all sufficiently large \(u\) depending on \(\delta\). The constant is absolute, independent of \(S,u,V,\delta\). It follows that, if abc fails, every such choice of four primes leaves \(\gg\delta^{-s'}\) points at each of infinitely many common heights with \(T_{S^c}(u,v)>\operatorname{rad}(u)u^\delta\), all in one interval. This concerns a set \(S\) shared by the points. The prime factors that account for repeated divisibility can differ from point to point.

## Localizing the previously constructed points

Use the [common-height transfer](abc_common_height_multiplicity.md). Its fixed finite alphabet consists of degree-\(D\) polynomials. In blocks of length \(\ell\) it supplies \(A^k\) distinct words of \(k\) blocks, all of degree \(q^k\), where \(s=\log_q A>3\). The proof chooses \(q^k\) within fixed constant factors of \(1/\delta\); its squaring step only requires a fixed rescaling of the input exponent. For each fixed \(k\) there are infinitely many seed fractions \(t\in(0,1)\) with increasing reduced denominators, giving distinct unordered pairs at an exact common height \(u\). The square-root addend after the squaring step is
\[
 v_f=u\,\min(f(t),1-f(t))
\]
for the word \(f\). Here \(u\) is the common output denominator before squaring. Endpoint hits and collisions occur at only finitely many seed ratios for fixed \(k\).

Pass to a subsequence of the seeds with \(t\to\tau\in[0,1]\). For any word with \(0<f(\tau)<1\), its smaller fraction has a positive finite limit. Otherwise, if its local degree at \(\tau\) is \(m\), the smaller fraction is asymptotic to \(c_f|t-\tau|^m\) with \(c_f>0\), by the polynomial Taylor expansion. Local degrees multiply under composition. Every \(m\) is a product of \(k\ell\) integers from 1 to \(D\). Its prime divisors are at most \(D\), each with exponent at most \(k\ell\log_2 D\). Including the interior case as one extra class, there are at most \(1+(1+\lfloor k\ell\log_2D\rfloor)^{\pi(D)}\) classes. A largest class has \(\gg A^k/(1+k)^{\pi(D)}\) words. For fixed \(k\), all ratios \(v_f/v_g\) in that class are bounded above by a finite constant as the seeds tend to \(\tau\). Since \(\Lambda(u)\to\infty\), one interval as stated contains the whole class at arbitrarily large heights. Choosing any fixed \(3<s'<s\) absorbs the polynomial in \(k=O(\log(1/\delta))\).

## Bounding the contribution captured by prescribed primes

The three integers \(Q(v),Q(u-v),Q(u+v)\) are pairwise coprime. For an odd prime this follows from primitivity. If \(u,v\) are odd, exactly one of \(u-v,u+v\) is divisible by 4, which gives the assertion at 2 as well. The product of the individual radicals of the three moving factors is at most \(2R(u,v)/\operatorname{rad}(u)\). Consequently at a qualifying point,
\[
 Q(v)Q(u-v)Q(u+v)
 \ \ge\ \tfrac38\operatorname{rad}(u)\,v\,u^{2\delta}.
\]
For a point satisfying the asserted upper bound on \(T_{S^c}\), the part supported on \(S\) is at least \(\tfrac38 v u^\delta\).

Write \(r=|S|\), and suppose \(1\le r\le4\). For each \(p_i\in S\), label it by the unique moving factor contributing to \(Q\), using an arbitrary fixed label when its contribution is zero. These data have at most \(3^r\) possibilities. For a single point let \(a_i=\log(p_i^{e_i})/\log u\), where \(e_i\) is its multiplicity in the moving \(Q\)-product. Assume \(1\le V\le u/2\); a window extending below 1 can be truncated with \(V=1\). For \(v\ge V\) and large \(u\), the last lower bound gives \(\sum a_i\ge L\), with
\[
 L=\log_u V+\delta/2 .
\]
Scale the nonnegative \(a_i\) down proportionally to coordinates \(x_i\le a_i\) summing to exactly \(L\). We have \(L<2\). Partition each of the first \(r-1\) coordinates into bins of width \(\delta/(8r)\), leaving the last coordinate determined by the sum. For two points with scaled vectors \(x,y\) in the same bins,
\[
 \sum_i\min(x_i,y_i)=L-\tfrac12\sum_i|x_i-y_i|\ \ge\ L-\delta/8.
\]
If the labels also agree, then \(\prod_i p_i^{\min(e_i(v),e_i(w))}\) divides \(v-w\), by subtracting the corresponding linear forms. This divisor is at least \(u^{L-\delta/8}=Vu^{3\delta/8}\), greater than \(V\log u\) for sufficiently large \(u\). Thus each cell contains at most one point in the interval. There are \(O_r(\delta^{-(r-1)})\) cells including labels. If \(S\) is empty the lower bound \(\tfrac38vu^\delta>1\) already excludes every such point.

The exponent \(r-1\) comes from the fixed sum in the window. It also applies to any fixed \(r\), with a constant depending on \(r\), and to \(\Lambda(u)=u^{o(1)}\) tending to infinity. With four primes it is strictly below the exponent forced by abc failure. An upper bound of cubic order for the remaining points with large contributions outside \(S\) would settle the conjecture.

## How often a square height has any qualifying point

Without a restriction on the repeated factors one still has an average bound specific to square heights. If \(N_\delta(u)\) counts all qualifying \(v\), then for fixed \(0<\delta<1\)
\[
 \sum_{u\le X}N_\delta(u)\le X^{1-\delta+o(1)} .
\]
The four radicals of \(u,v,u-v,u+v\) have product at most \(2R(u,v)\). The two smallest therefore have product at most \(\sqrt2 X^{1-\delta}\). Their two integer values determine \((u,v)\) uniquely once the pair of linear forms is named, since all six pairs of forms are linearly independent. For any prescribed radical \(d\), the number of integers \(n\le2X\) with radical \(d\) is \(X^{o(1)}\), uniformly: writing \(r=\omega(d)=O(\log X/\log\log X)\), the exponent vectors number at most \(\binom{\lfloor\log_2(2X)\rfloor}{r}=X^{o(1)}\). Finally there are \(O(Y\log(2Y))\) pairs of candidate radicals with product at most \(Y=\sqrt2 X^{1-\delta}\). This proves the average estimate, which allows the remaining points to concentrate at sparse individual heights.
