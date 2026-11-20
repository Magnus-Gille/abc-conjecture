# Which prime powers can give an abc counterexample on the full octic orbit?

Take the full positive odd index \(N\ge3\) of the [two-square parametrization](abc_octic_full_mixed_orbit.md). Its primitive abc triples and their radicals are
\[
 (a_N,b_N,c_N)=((2st)^4,(s^4-4t^4)^2,(s^4+4t^4)^2),\qquad R_N=\operatorname{rad}(T_N),
\]
where \(Y=s^2+2t^2,\ V=(s-t)^2+t^2,\ U=(s+t)^2+t^2,\ D=s^2-2t^2\) and \(T_N=2|stDU|\sqrt{YV}\). Set \(e_p=v_p(T_N)\). Fix \(0<\eta<1\). Call a prime eligible at \(N\) if it meets both size bounds in the relevant row.

| Splitting in \(\mathbb Q(\sqrt{-2})\) | Prime size | Prime times exponent |
|---|---:|---:|
| Split | \(p>N^{2-\eta}\) | \(p e_p>N^{4-\eta}\) |
| Inert | \(p>N^{1-\eta}\) | \(p e_p>N^{3-\eta}\) |

Then, without assuming abc or any prime-counting conjecture,
\[
 \log c_N-\log R_N
   =\sum_{p\mid T_N,\ p\ {\rm eligible}}(e_p-1)\log p+o_\eta(N^2).
\]
Since \(\log c_N\asymp N^2\), this family disproves rational abc if and only if the displayed sum exceeds \(\delta N^2\) for some fixed \(\delta>0\) at infinitely many odd indices. The criterion permits arbitrary, different multiplicities at every prime.

## An equivalent criterion using a prime's first occurrence

For \(p\ge7\), let \(r_p\) be the order of \(A=(1,1)\) modulo \(p\), and let \(d_p\) be the formal depth of \([r_p]A\). Thus \(d_p\ge2\) means that this first multiple returning to the identity modulo \(p\) already returns to the identity modulo \(p^2\). Such primes are called elliptic Wieferich primes for this point. The formula above remains true after replacing \(e_p\) by \(d_p\) in both the sum and the eligibility table, and restricting to \(p>7\) with \(d_p\ge2\).

Indeed \(p\nmid r_p\), since the finite group has even order strictly less than \(2p\) by Hasse's bound. If \(p>7\) divides \(T_N\), select \(k\) as in the local calculation below. Then
\[
 d_p\le e_p\le d_p+v_p(k).
\]
For the first four multipliers equality holds at the right by the formal logarithm and the depth identities. For \(k=N^2+2\), the formal depth at \([k]A\) exceeds \(e_p\) by the valuation of the differential of a complementary endomorphism \([N\pm\sqrt{-2}]\). The two complementary differentials are integral and have product \(k\). At the unramified prime above \(p\) each valuation lies between zero and \(v_p(k)\). In particular \(\sum_{p\mid T_N,\ p>7}(e_p-d_p)\log p\le\sum_k\log k=O(\log N)\). To replace the cutoffs as well, use \(e_p\ll d_p\log(2N)\) and apply the excluded-mass estimate with \(\eta/2\) in place of \(\eta\). Thus the entire quadratic-size loss, if it occurs, must come from the *initial* excess depths of elliptic Wieferich primes actually dividing \(T_N\).

In particular, if the elliptic Wieferich primes for this point are finite, the qualities of this entire family tend to one. A search through all 78,495 primes \(7\le p\le 10^6\) found exactly two with \(d_p\ge2\). The pairs \((p,r_p)\) were \((4871,2436)\) and \((205883,34387)\), both with \(d_p=2\). The count uses division-polynomial values modulo \(p^2\) at \(\#E(\mathbb F_p)\), which has the same depth as \([r_p]A\). Independent elliptic multiplication over \(\mathbb Q_p\) gives abscissa valuation \(-4\) in both cases. [Reproducible count](abc_octic_prime_count_check.py)

Both primes occur in the actual triple family. At \(N=34387\), the abscissa \(D^2/(YV)\) has valuation \(-4\) at \(205883\), so the prime enters \(YV\) to exponent four. This prime is three modulo four and cannot divide the primitive sum of squares \(V\). Thus \(205883^4\parallel Y_{34387}\). At \(N=4873\) the point giving the slope is \([2437]A\), at distance of depth two from \(A\) at 4871. The slope function \((v+u)/(2(u-1))\) has a simple pole there with unit leading coefficient, so \(4871^2\parallel t_{4873}\). Each of these examples supplies a fixed logarithmic weight.

More generally, at \(N=2r_p+1\) this pole gives \(v_p(t_N)=d_p\) for every \(p>7\). Thus **one prime at a time** suffices if infinitely many distinct primes satisfy \((d_p-1)\log p\ge\delta r_p^2\) for a fixed \(\delta>0\). Indeed \(\log c_N\ll r_p^2\), while \(T_N\ll c_N\) and \(\log(T_N/R_N)\ge(d_p-1)\log p\). The ranks are unbounded on any infinite set because a fixed nonzero multiple of \(A\) has only finitely many denominator primes. In particular, this would follow from infinitely many elliptic Wieferich primes with \(r_p\le C\sqrt{\log p}\) for any fixed \(C\). A sequence with this property has not been established.

## Fixed places and the real size of the factors

Write \(n=(N+1)/2\). The slope \(s/t\) is a fixed rational function of \([n]A\) on \(E:v^2=u^3-8u^2+8u\), \(A=(1,1)\). For any fixed archimedean or nonarchimedean place and fixed algebraic point of this curve, logarithmic proximity of \([n]A\) to the point is \(o(n^2)\). Here proximity means the positive part of minus the log of a local-parameter distance, bounded away from the target. For a proof write \(n=Lm+r\) with fixed \(L\), \(0\le r<L\). Multiplication by \(L\) is unramified in characteristic zero. Near a target the proximity is bounded by the largest proximity of \([m]A\) to the finitely many division points of the target translated by \(-[r]A\), plus \(O_L(1)\). This follows by local parameters with nonzero linear term and compactness. Near a division point one can use its elliptic abscissa (or reciprocal abscissa at infinity) to bound proximity from above: that function differs from its value there to order at least one. The one-place Roth theorem, with its nonarchimedean version at a finite place, gives the bound \(3h(u([m]A))+O_L(1)\) for these rational abscissas approximating any of the finitely many fixed algebraic values. Rational targets satisfy the elementary height bound as well. Exact coincidences affect only finitely many indices for fixed \(L\). Since \(h(u([m]A))=2\widehat h(A)m^2+O(1)\), dividing by \(n^2\) and then letting \(L\) grow proves the claim. Orders of vanishing in the original, fixed slope map only change its constant factor.

Put \(H=\max(|s|,t)\). The positive definite forms \(U,Y,V\) have real sizes comparable to \(H^2\), and \(c_N\asymp H^8\). The three ratios \(|s|/H,\ t/H,\ |D|/H^2\) can approach zero only at the projective slopes \(0,\infty,\pm\sqrt 2\). Applying the proximity bound to the finitely many points over those slopes gives \(\log(c_N/T_N)=o(N^2)\). At any fixed prime the primitive coordinates have maximum local norm one. The valuations in \(T_N\) are consequently bounded by a constant plus finitely many proximities to the fibers over the zeros of its homogeneous factors, with their fixed multiplicities. Thus each fixed prime supplies \(o(N^2)\) even with its full exponent.

## Varying primes

For \(p>7\) dividing \(T_N\), its exponent \(e_p\) is at most the formal depth of \([k]A\) for one of the integers
\[
 k=N,\quad 2N,\quad N-1,\quad N+1,\quad N^2+2.
\]
The local identities proving this are in the [whole-triple calculation](abc_octic_mixed_quality_dichotomy.md). For \(p\mid U\) the complementary complex endomorphism can increase depth at \(p\mid N^2+2\), which suffices for this upper bound. Assign each prime to one such \(k\). All five are \(O(N^2)\), and each has \(N^{o(1)}\) rational or quadratic ideal divisors.

At a split prime choose one place above \(p\). The annihilator ideal \(\mathfrak a=(\gamma)\) of the reduction of \(A\) divides \((k)\) in \(\mathbb Z[\sqrt{-2}]\). Write \(m=\operatorname N\mathfrak a\). The sum of formal depths of \([\gamma]A\) weighted by \(\log p\) is \(O(m)\) by the global abscissa height. This upper bound holds for even and odd multipliers. Decompose \(e_p=f_p+(e_p-f_p)\), taking \(f_p\) to be the smaller of \(e_p\) and that first formal depth. At split places the formal logarithm shows that the sum of the second terms weighted by \(\log p\) is at most \(2\log k\) over all places assigned to that \(k\): the increase is at most the valuation of the differential of \([k/\gamma]\), which divides \(k\) in the integer ring. These properties use good reduction and the unramified odd-prime formal logarithm. [CM denominator estimates](abc_octic_mixed_cm_prime_mass.md)

Frobenius at this place is a complex multiplier \(\pi\) with norm \(p\) and \(\pi\equiv1\bmod\mathfrak a\). The lattice \(1+\mathfrak a\) therefore gives \(p\gg m\) and \(O(1+Z/m)\) possible primes up to \(Z\). Summing dyadically gives \(\sum_{p\le X}1/p\ll\log(2X)/m\) in this class. For \(p e_p\le X\) one has \(f_p\le X/p\), so the full first-depth mass subject to this cutoff is at most
\[
 O\big(\min(m,X\log^2(2X)/m)\big)=O(\sqrt X\log(2X)).
\]
For the cutoff \(p\le Z\), it is instead \(O(Z)\) since any occurring class has \(m\ll Z\).

At an inert prime the CM curve has trace zero, so the rational reduction order \(r\) of \(A\) divides \(p+1\) as well as \(k\). First formal depth is now taken at \([r]A\); its total mass at a fixed \(r\) is \(O(r^2)\) by the abscissa height. The sum of increases upon multiplying by \(k/r\) is at most \(\log k\) across the assigned rational primes. Within this rank, \(p\equiv-1\bmod r\), whence \(\sum_{p\le X}1/p\ll\log(2X)/r\) by summing reciprocals of positive terms of the progression (for \(r=1\) use the ordinary harmonic bound). The mass at \(p e_p\le X\) is bounded, up to the already counted increases, by
\[
 O\big(\min(r^2,X\log^2(2X)/r)\big)=O(X^{2/3}\log^{4/3}(2X)).
\]
For \(p\le Z\) the fixed-rank bound is \(O((Z+1)^2)\) since \(r\le p+1\).

Summing over the five choices of \(k\) and their \(N^{o(1)}\) possible classes, the excluded split primes, with their full exponents, give \(o(N^2)\) upon taking \(X=N^{4-\eta}\), \(Z=N^{2-\eta}\). For inert primes use \(X=N^{3-\eta}\), \(Z=N^{1-\eta}\). Fixed small primes were treated above. Finally \(\log(T_N/R_N)=\sum_{p\mid T_N}(e_p-1)\log p\). Together with the real-size estimate this proves the formula and the equivalence.
