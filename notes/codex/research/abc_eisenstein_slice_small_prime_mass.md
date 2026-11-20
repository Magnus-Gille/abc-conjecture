# Pointwise and first-occurrence bounds for the small-prime mass

Use the [fixed elliptic slice](abc_eisenstein_twelfth_elliptic_slice.md), the [marked divisor identities](abc_eisenstein_slice_marked_divisors.md), and the [paired-quartic gcd bound](abc_eisenstein_slice_quartic_lcm.md). For odd \(n\ge3\) write \(D_n\) for the integer with the same radical as the abc triple, \(J_n=|F_+F_-|\), and \(A_n\) for the part of \(D_n/J_n\) prime to 6. For \(m>0\) let \(V_{\le Y}(m)=\sum_{p\le Y}v_p(m)\log p\).

For any fixed \(\varepsilon>0\), the **entire valuation mass** from split primes \(p\equiv1\bmod4\), \(p\le n^{2-\varepsilon}\), in \(A_n\) is \(o(n^2)\) at every index. The contribution from inert primes in \(A_n\) through \(Y\le n\) is \(O(nY+\log n)\) at every index. On the independent quartic pair the elementary method gives a sparse exception set. For \(N/2\le n\le N\) and \(2\le Y\le N\), after excluding at most \(4\pi(Y)\) indices one has
\[
 V_{\le Y}(J_n)\ll 1+\frac{Y^2}{\log(2Y)}+\pi(Y)\log(2N).
                                                               \tag{1}
\]
Consequently, for \(Y=N^{1-\varepsilon}\), at all the remaining odd indices
\[
 V_{\le Y}(D_n)\ll_\varepsilon N^{2-\varepsilon}.
\]
Only \(O(N^{1-\varepsilon}/\log N)\) indices were omitted. In combination with the size estimate \(\log D_n=24\widehat h(P)n^2+o(n^2)\), this places all but \(o(n^2)\) logarithmic factor mass above \(Y\). The estimate retains prime exponents. An isolated repeated prime above the cutoff can still lower the radical.

## Dependent marks

Let \(Q=(-8,-64)\) on \(E':v^2=u^3-576u\); write \(r_p=\operatorname{ord}(Q\bmod p)\) and \(e_p=v_p(B'_{r_p})\). The good-prime dependent factors come from rational denominators at \(2n,n-1,n+1\) and a Gaussian denominator at \([n+i]Q+T_0\), using absolute ideal norm at the latter. Depth above \(e_p\) contributes in total \(O(\log n)\) by the ordinary lifting identity of the marked-divisors note. Distinct primes of fixed exact order \(r\) have weighted baseline sum \(\sum e_p\log p\le\log B'_r\ll 1+r^2\).

If \(p\equiv3\bmod4\) it can only hit the rational marks. For a hit at the rational index \(q\in\{2n,n-1,n+1\}\), one has \(r_p\mid q\), \(r_p\le Cp\). For \(p\le Y\le n\),
\[
 \sum_{r\mid q,\ r\le CY} r^2
    \le q^2\sum_{d\ge q/(CY)}d^{-2}\ll nY .
\]
This proves the inert bound. The same argument works on the rational factors irrespective of the splitting of \(p\).

For split \(p\ge5\), work at a Gaussian place \(\mathfrak p\mid p\). The CM ring \(\mathcal O=\mathbb Z[i]\) acts on reduction, the Frobenius belongs to it, and \(N(\pi_\mathfrak p-1)=\#E'(\mathbb F_p)\). Indeed this is good ordinary reduction of a curve with full Gaussian CM and the Frobenius commutes with its endomorphisms; the centralizer is \(\mathbb Q(i)\), Frobenius is integral, and its degree is its norm. The annihilator \(\mathfrak a=\{a\in\mathcal O:[a]\bar Q=O\}\) contains \(\pi_\mathfrak p-1\) and \(r_p\). In particular \(N\mathfrak a\le Cp\). Choose a generator \(\alpha\), once for each ideal. The point \([\alpha]Q\) has local formal depth exactly \(e_p\) because \(r_p/\alpha\) is a Gaussian integer prime to \(\mathfrak p\). Indeed \(r_p\mid\#E'(\mathbb F_p)\) and this group size is a multiple of four smaller than \(4p\), so it is prime to \(p\). Multiplication by the quotient therefore preserves formal depth.

At a rational marked factor, \(\mathfrak a\mid(q)\). At a Gaussian marked factor, doubling kills \(T_0\), giving \(\mathfrak a\mid(2(n+i))\) for the chosen ideal norm, or one may include both signs for a common orientation convention. Group by \(\mathfrak a\). For every such ideal, summing \(e_p\log p\) over all places with that annihilator costs at most
\[
 \log N\mathfrak B_{\mathbb Q(i)}([\alpha]Q)\ll1+N\mathfrak a
\]
by canonical height. The Gaussian ideals in this sum divide one of five principal ideals \((2n),(n-1),(n+1),(2(n+i)),(2(n-i))\), whose norms are \(O(n^2)\). Each has \(n^{o(1)}\) ideal divisors, for instance by the square of the ordinary divisor bound for its norm. Thus the total baseline of split primes \(p\le Y\) is \(\ll Y n^{o(1)}\), yielding the asserted near-quadratic cutoff.


This split-prime cutoff can be pushed much closer to \(n^2\). Write \(L_2=\log\log n\), \(L_3=\log L_2\), \(L_4=\log L_3\). For each fixed \(\delta>0\) the same pointwise \(o(n^2)\) bound holds through
\[
                 Y=n^2\exp(-(1+\delta)L_2L_3/L_4).                \tag{3}
\]
Here is a uniform divisor-tail proof. For any of the five Gaussian indices \(z\), put \(X=N(z)\asymp n^2\) and put \(\mathfrak b=(z)/\mathfrak a\). Then
\[
 \sum_{\mathfrak a\mid(z),\,N\mathfrak a\le CY}N\mathfrak a
  =X\sum_{\mathfrak b\mid(z),\,N\mathfrak b\ge X/(CY)}(N\mathfrak b)^{-1}.
\]
Define \(l_2=\log\log X,l_3=\log l_2,l_4=\log l_3\), fix small \(\epsilon>0\), and take \(\beta=(1-\epsilon)l_4/l_2\). Uniformly over \(z\) the shifted reciprocal divisor sum has logarithm at most \((1+o(1))l_3\). To see this, majorize it by the Euler product of \((1-(N\mathfrak q)^{-1+\beta})^{-1}\) over \(\mathfrak q\mid(z)\). For \(N\mathfrak q\le B=(\log X)^{1+\epsilon/2}\) the logarithm of the unshifted product is at most \(\log\log B+O(1)=l_3+O_\epsilon(1)\) by the prime ideal Mertens theorem. The increment upon shifting is
\[
 \ll \sum_{N\mathfrak q\le B}\frac{(N\mathfrak q)^\beta-1}{N\mathfrak q}
 \ll \beta B^\beta\log B=o(l_3),
\]
by partial summation of the prime ideal count and \((1-\epsilon)(1+\epsilon/2)<1\). For \(N\mathfrak q>B\) belonging to \((z)\) the whole contribution is \(\ll B^{-1+\beta}\log X/\log B=o(1)\), since the sum of their logarithms is at most \(\log X\). Rankin's bound for the tail of the unshifted divisor sum is therefore \(\exp((1+o(1))l_3-\beta\log(X/(CY)))\). In (3) we may take \(\epsilon\) sufficiently small in terms of \(\delta\), making this \(o(1)\). The constant factors between \(X\) and \(n^2\) do not change this conclusion.

## Independent mark and its unique high lift

The four possible marks \(S_i\) on \(E'\) are each CM-independent of \(Q\) modulo torsion. Fix a place over \(p\ge5\) in their Galois closure once for all. A hit localizes to exactly one mark, and the formal depth there equals \(v_p(J_n)\). At a hitting mark its coordinates belong to \(\mathbb Q_p\). Indeed the fixed residue of a rational point singles out exactly one of the four distinct reduced conjugates, so its decomposition group fixes the mark. The uniformizer is \(p\).

If \(v=v_p(J_n)>0\), then
\[
 \min(e_p,v)\log p\ll r_p,
 \qquad
 \min(e_p,v)\log p\ll\sqrt p\quad(p\equiv1\bmod4).               \tag{2}
\]
For the first bound reduce \(n\) modulo \(r_p\) to \(n_0\). At depth \(t=\min(e_p,v)\), both \([r_p]Q=O\) and \([n_0]Q=S_i\). Ordinary Dirichlet approximation gives integers \(s,a\) with \(s\equiv an_0\bmod r_p\), \(1\le a\ll\sqrt{r_p}\), \(|s|\ll\sqrt{r_p}\). Thus the nontorsion point \(sQ-aS_i\) is formal to depth \(t\) and has canonical height \(O(r_p)\). The fixed-field denominator norm bounds \(t\log p\).

For a split prime the congruences strengthen to \([\alpha]Q=O\) and \([n]Q=S_i\) at depth \(t\), with \(N\alpha\ll p\) as above. The kernel of \((a,b)\mapsto a+bn\bmod\alpha\) in \(\mathbb Z[i]^2\) has index \(N\alpha\). Pigeonholing a four-dimensional integer box gives a nonzero kernel vector of squared length \(O(\sqrt{N\alpha})\). The corresponding nontorsion point \(aQ+bS_i\) is formal to depth \(t\) and has height \(O(\sqrt p)\).

For each mod-\(p\) hitting residue \(h\in[0,r_p)\), set
\[
 L=\log_{E'}(r_pQ),\qquad C=\log_{E'}(S_i-hQ).
\]
The isometric formal logarithm gives \(v_p(L)=e_p\). If \(v_p(C)<e_p\), the depth is exactly \(v_p(C)\) all along this residue. Otherwise \(\alpha_{p,i}=C/L\in\mathbb Z_p\), and throughout the class
\[
             v_p(J_{h+kr_p})=e_p+v_p(k-\alpha_{p,i})
\]
at the indices for which the quartic pair is defined. This ratio cannot be rational: clearing an alleged rational denominator in the formal logarithm would give a nontrivial integer dependency of the two points \(Q,S_i\). By (2) the constant depth in the first case or the baseline \(e_p\) in the second costs at most \(O(p)\) after weighting by \(\log p\), even at the exceptional indices. For every \(k\) except at most one in this class and the entire prefix, \(v_p(k-\alpha_{p,i})\log p\le\log(2N)\). Two larger values would force \(0<|k-k'|\le N\) divisible by a power of \(p\) larger than \(N\). There are at most four classes. Summing \(p\) over the primes through \(Y\) proves (1). The baseline from split primes alone has upper bound \(O(Y^{3/2}/\log(2Y))\) by the stronger half of (2).

For a finite census the sole candidate index per class can be located by lifting \(\alpha_{p,i}\) to a precision \(p^j>N/r_p\): take the least nonnegative residue of the lift and check its index against the interval and parity. Each deeper valuation then needs at most this one index. An existing [square-level residue census](abc_eisenstein_slice_paired_quartic.md) implements the first digit.

At the bad primes the total in \(D_n\) is \(O(\log(2n))\). At 2 both parameters are odd, \(v_2(F_0)=3\) and thus \(v_2(z)=1\), while \(v_2(x^2-3y^2)=1\) and \(v_2(x^2+3y^2)=2\). The two forms \(x^2\pm6xy-3y^2\) have no projective \(\mathbb Q_2\)-root, as their discriminant has nonsquare class 3. Their valuations on primitive pairs are bounded by compactness, and \(v_2(J_n)=9\). Only \(x^2-y^2,x^2-9y^2\) can grow; their zeros correspond to \(nP=\pm P,\pm(P+(0,0))\). At 3, \(3\nmid x\) leaves only \(y\) and \(x^2-y^2\), corresponding to \(nP\) near the identity or \(\pm P\). At each fixed place, local parameter comparisons near the relevant rational sections have bounded additive errors in valuation, by the nonvanishing characteristic-zero derivative and compactness elsewhere. Doubling kills the two-torsion translate. The resulting rational denominators at \(2n,2(n\pm1)\) have valuation \(O(1+\log n/\log p)\), by restricting the formal group to a fixed isometric logarithm neighborhood.

## Effective elliptic logarithms

A proposed way to treat the single exceptional index at each place is a lower bound for a linear form in two \(p\)-adic elliptic logarithms. At any relevant \(p\ge5\) take \(M=\#E'(\mathbb F_p)\ll p\), prime to \(p\). The independent points \(MQ,MS_i\) belong to the formal group and have canonical heights \(O(p^2)\). Then
\[
 v_p(J_n)\log p
   =-\log|n\log_{E'}(MQ)-\log_{E'}(MS_i)|_p
\]
at all hitting indices. The linear form is nonzero by independence. An estimate \(O(p^A(\log(2n))^B)\) with fixed positive constants would give a uniform bound \(O(Y^{A+1}(\log(2n))^B)\) at every index. The directly relevant reference is Bosser and Surroca's work [*Upper bound for the height of S-integral points on elliptic curves*, arXiv:1208.2693](https://arxiv.org/abs/1208.2693). Its bibliographic record was checked; the underlying local theorem and its precise uniform dependence were not verified in the full text during this check. All preceding estimates are independent of this proposed additional input.

## A finite all-indices certificate

Starting from all 5,862 odd square progressions for the 2,777 visiting good primes through \(10^6\), the [higher-level verifier](abc_eisenstein_slice_high_lift_bound.py) exhausts them throughout the prefix of odd indices \(3\le n\le10^{18}\). If \(h\) is the least representative at depth \(j\), with period \(d\), two evaluations of \(A(k)=u(kQ)^2+336u(kQ)+576\) modulo \(p^{j+1}\), at \(h,h+d\), give the affine lifting digit. This is translation in the formal parameter at a smooth point with unit derivative. The program checks the unit slope at every stage. The lift representative never decreases, so the first representative to exceed the prefix ends the descent. The program also recomputes each of the 2,777 maximum-depth witnesses independently by a differential abscissa ladder, separate from the division-polynomial evaluation during lifting.

Of the visiting primes the numbers with maximum exponents \(3,4,5,6,7,8\) are respectively \(2495,246,27,5,2,2\). Only 167 and 191 reach depth eight. Witnesses are \(54\,385\,699\,776\,296\,631\) and \(48\,254\,830\,936\,505\,719\). The part of the prefix lcm supported on primes through \(10^6\), including 2, has 157,637 bits. For the excess \(J_n/\operatorname{rad}(J_n)\) the corresponding lcm has 106,665 bits. Thus through this finite rectangle \(V_{\le10^6}(J_n)<157637\log2\) at every odd index, with no exceptional set. [Exact census output](abc_eisenstein_slice_high_lift_bound.txt)
