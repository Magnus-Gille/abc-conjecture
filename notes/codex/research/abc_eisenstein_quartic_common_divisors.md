# A bound for common divisors of the two quartic factors at different indices

Use the fixed elliptic orbit \(E:Y^2=X^3+36X^2+36X\), \(P=(-2,8)\). At each odd \(n\ge3\), write \(X(nP)=-2(x/y)^2\) with \(x,y\) positive and coprime. Set
\[
 F_\pm(x,y)=x^4-18x^2y^2+9y^4\ \pm 12xy(x^2-3y^2),
 \qquad J_n=|F_+(x,y)F_-(x,y)|/512.
\]
The following bounds have absolute implied constants for this orbit.

* For distinct odd \(m,n\ge3\), \(\log\gcd(J_n,J_m)\ll n+m\).
* If \(p^e\mid J_n\) and \(p^e\mid J_m\) at two such indices, then \(e\log p\ll n+m\). In particular, a prime of size \(\exp(\delta n^2)\) at index \(n\) cannot occur again at any positive odd index below \(c_\delta n^2\), for sufficiently large \(n\).
* If \(B_j'\) denotes the square root of the abscissa denominator of \(jQ\), where \(Q=(-8,-64)\) on \(E':v^2=u^3-576u\), then \(\log\gcd(J_n,B_j')\ll j\) for every \(j\ge1\), uniformly in \(n\). In particular, \(p\mid J_n\) implies \(\operatorname{ord}(Q\bmod p)\gg\log p\).
* The log of the product of the \(J_n\) at odd indices up to \(N\) exceeds the log of their lcm by \(O(N^{5/2})\). In particular the log of that lcm is \(4\widehat h(P)N^3/3+O(N^{5/2})\). On intervals of length \(o(N)\) about \(N\), the log of the lcm is also asymptotic to the log of the product, provided the interval contains an eligible index.

The bounds allow large squares at a single index. They control recurrence across indices and overlap with ordinary elliptic denominators. [Connection to abc](abc_eisenstein_twelfth_elliptic_slice.md)

## The four points and their independence

Write \(h=\sqrt[4]3\), \(K=\mathbf Q(i,h)\), \(T=(0,0)\) on \(E'\), and
\[
        s=-168+96h^2,\qquad S=(s,8h^3s).
\]
The four conjugates of \(S\) are \(\pm S,\ \pm[i](S+T)\), where \([i](u,v)=(-u,iv)\). Indeed \(s'=-168-96h^2=576/s\), and translation by \(T\) sends \(u\) to \(-576/u\). Thus for any two conjugates \(S_a,S_b\) one can write \(S_b=[\epsilon]S_a+T_{ab}\), with \(\epsilon\in\{1,-1,i,-i\}\) and \([2]T_{ab}=O\).

The points \(Q,S_a\) are independent over \(\mathbf Z[i]\), also modulo torsion. The point \(Q\) is the 2-isogenous image of \(P\), which has infinite order. Duplication gives \(u(2S)=49\sqrt3\). Under \(u=h^2X,\ v=h^3Y\), the point \(2S\) corresponds to \((49,\pm329)\) on \(Y^2=X^3-192X\). Its ordinate is divisible by 47, whereas the discriminant has prime support in \(\{2,3\}\), so Nagell–Lutz proves it nontorsion. The automorphism of \(K\) fixing \(i\) and sending \(h\) to \(-h\) fixes \(Q\) and negates every \(S_a\). Subtracting conjugate relations proves the claimed independence.

All \(J_n\) are integers prime to 6. Indeed \(x,y\) are odd and \(3\nmid x\); reducing the quartics at the odd residue classes \(x/y\bmod64\) gives the valuations 4 and 5 at 2, in either order, and \(F_\pm\equiv x^4\bmod3\). By the 2-isogeny,
\[
       u(nQ)=-2(x^2-3y^2)^2/(xy)^2,\qquad
       u(nQ)^2+336u(nQ)+576=4F_+F_-/(xy)^4 .
\]
At any \(p\mid J_n\), both \(x,y\) are units. In \(K\) the two roots \(s,s'\) differ by the unit \(192\sqrt3\) at \(p\), and the four ordinates of the conjugate points are all units. The curve has good reduction there and \(K\) is unramified outside 2 and 3. For any chosen \(\mathfrak p\mid p\), exactly one conjugate \(S_a\) is congruent to \(nQ\) to depth \(v_p(J_n)\). Here congruence to depth \(e\) means equality in \(E'(\mathcal O_{K,\mathfrak p}/\mathfrak p^e)\). The abscissa is an étale coordinate at the target since \(2v(S_a)\) is a unit. [Factor identities](abc_eisenstein_slice_marked_divisors.md)

## The common-divisor estimate

Fix distinct positive \(n,m\) as above. For each \(p\mid\gcd(J_n,J_m)\) choose one place \(\mathfrak p\mid p\), put \(e=\min(v_p(J_n),v_p(J_m))\), and assign the prime to its ordered pair of conjugates \(S_a,S_b\). In the group modulo \(\mathfrak p^e\) one has
\[
 nQ=S_a,\qquad mQ=S_b=[\epsilon]S_a+T_{ab},
 \qquad [d]Q=O,\quad d=2(m-\epsilon n).
\]
The Gaussian integer \(d\) is nonzero. All primes assigned to the same pair share the same \(d\).

Choose Gaussian integers \(A,B\), not both zero, satisfying
\[
       A+nB\equiv0\bmod d,\qquad |A|^2+|B|^2\ll |d|.
\]
For example, allow the four integer coordinates of \(A,B\) to vary from zero to \(\lceil |d|^{1/2}\rceil\). The number of pairs exceeds the \(|d|^2\) residue classes modulo \(d\); subtract two with equal residue. This choice is simultaneous for all the primes in the assigned group.

The point \(Z=[A]Q+[B]S_a\) is nontorsion by independence. It reduces to the identity to depth at least \(e\) at every assigned place. All endomorphisms used here extend over these good primes. Write \(\mathfrak B(Z)\) for its good-prime abscissa denominator ideal with half the denominator valuations. The ordinary logarithmic height and its comparison with the canonical height give
\[
 \log N\mathfrak B(Z)\le [K:\mathbf Q]\big(\widehat h(Z)+O(1)\big)
      \ll |A|^2+|B|^2+1 \ll n+m .
\]
The middle bound uses the triangle inequality for the square root of canonical height and \(\widehat h([\alpha]D)=|\alpha|^2\widehat h(D)\) for Gaussian endomorphisms. Each assigned prime contributes at least \(e\log p\) to this same denominator norm. Summing over the at most sixteen pairs proves the bound on the whole gcd, including multiplicities.

For the mixed bound, assign primes of \(\gcd(J_n,B_j')\) to a single conjugate \(S_a\). Modulo the common depth one has \(nQ=S_a\), \(jQ=O\). Repeat the argument with \(d=j\). One may also use ordinary integer coefficients \(A,B\), choosing them of size \(O(\sqrt j)\) by the two-dimensional pigeonhole principle. Taking \(j=\operatorname{ord}(Q\bmod p)\) gives the asserted order bound. In particular any sequence with \(\log p\ge\delta r_p^2\), \(r_p=\operatorname{ord}(P\bmod p)\), eventually cannot divide any \(J_n\): the order of the isogenous image \(Q\) divides \(r_p\). This excludes overlap with the previously identified single-prime disproof criterion.

## The lcm and the remaining square question

The [fixed-orbit archimedean estimate](abc_eisenstein_twelfth_elliptic_slice.md) gives
\[
             \log J_n=8\,\widehat h(P)n^2+o(n^2).
\]
Indeed the homogeneous product has degree 8, has finitely many algebraic projective zero directions, and \(\log\max(x,y)=\widehat h(P)n^2+O(1)\). The logarithmic proximity of these directions at the archimedean place is \(o(n^2)\) by the division argument in that estimate.

For \(k\) odd indices in \([N,2N]\), the elementary product/lcm inequality gives
\[
  0\le \sum_n\log J_n-\log\operatorname{lcm}_n J_n
       \le \sum_{n<m}\log\gcd(J_n,J_m)\ll k(k-1)N .
\]
In particular, if \(k=o(N)\), the right side is \(o(kN^2)\).

For the full interval, count each prime power \(p^t\) with weight \(\log p\). Let \(k_{p,t}\) be the number of eligible indices up to \(N\) at which \(p^t\mid J_n\). The difference between log product and log lcm is exactly \(\sum_{p,t}(k_{p,t}-1)_+\log p\).

First, all distinct prime powers occurring at least twice have total weight \(O(N^{5/2})\). Given any two indices \(m\ne n\le N\) realizing the prime power, choose ordinary integers \(a,b\), not both zero, such that \(s=am+bn\) and \(|a|,|b|,|s|\ll\sqrt N\). To see this, take \(m\le n\) and apply Dirichlet approximation to \(m/n\) with denominator at most \(\lceil\sqrt N\rceil\). At a chosen place above the prime, the point
\[
                    Z=[s]Q-[a]S_b-[b]S_a
\]
is formal to depth at least \(t\); here \(S_b,S_a\) are the targets at \(m,n\), respectively. It is nontorsion. Otherwise independence would give \(s=0\) and \(a\epsilon+b=0\); with distinct positive \(m,n\) these force \(a=b=0\). Across all indices and primes there are only \(O(N^{3/2})\) candidate triples \((s,a,b)\) and a fixed number of choices of targets. Each nontorsion candidate has log denominator norm \(O(N)\). Summing their denominator norms logarithmically bounds the weights of all these distinct prime powers simultaneously. This argument also gives, for fixed gap \(g>0\), a single common multiple of all \(\gcd(J_n,J_{n+g})\) at eligible indices, with logarithm \(O(1+g^2)\): take \(a=1,b=-1,s=g\).

For the multiplicities, write \(r=\operatorname{ord}(Q\bmod p^t)\) in \(E'(\mathbf Z/p^t\mathbf Z)\). At a fixed place above \(p\) there are at most four target residue classes of indices modulo \(r\). Thus \(k_{p,t}\le4(N/r+1)\). All *distinct* prime powers that ever occur and have \(r\le R_0\) have total weight \(O(R_0^2)\), independently of \(N\). Indeed their first hitting index at this depth may be represented by \(0\le n_0<r\). Choose integers \(c,d\), not both zero, with \(c+d n_0\equiv0\bmod r\) and \(|c|,|d|\ll\sqrt{R_0}\), by pigeonhole. Then \([c]Q+[d]S_a\) is nontorsion and formal at the place to depth \(t\). There are \(O(R_0)\) choices of this point, each of log denominator norm \(O(R_0)\). Summing as above proves the weight bound. For \(R_0/2<r\le R_0\le 2N\), the contribution with multiplicities is consequently \(O(NR_0+R_0^2)\). Dyadic summation shows that all \(r\le N\) together contribute \(O(N^2)\).

For \(r>N\), there are at most four hits and the distinct-prime-power weight \(O(N^{5/2})\) already suffices. This proves the asserted product/lcm error. Finally the total archimedean loss in replacing \(\sum\log J_n\) by \(8\widehat h(P)\sum n^2\) is \(O(N^2)\). Near each real zero direction, the normalized quartic product is comparable to the distance from \(nQ\) to the corresponding real target; this follows from the two simple abscissa roots and nonzero ordinates. Away from these directions the loss per term is bounded. The maximum logarithmic proximity to a fixed target is \(O(N^2)\) by height separation. If \(k\ge2\) points are within distance \(d\) of the same target in an invariant metric on \(E'(\mathbf R)\), two of their indices differ by an integer \(a\le N/(k-1)\), with \(aQ\) within \(2d\) of the identity. The abscissa height of \(aQ\) bounds \(\log^+(1/d)\) by \(O(1+a^2)\). Summing these bounds for the ordered proximities gives \(O(N^2)\). Use \(\sum_{3\le n\le N,\ n\ {\rm odd}}n^2=N^3/6+O(N^2)\). [Independent detailed proof](abc_eisenstein_slice_quartic_lcm.md)

The fixed-gap estimate above also gives, for any finite set \(\mathcal S\) of primes,
\[
 \sum_{\substack{N<n\le2N\\n\ {\rm odd}}}\sum_{p\in\mathcal S}v_p(J_n)\log p
       \ll |\mathcal S| N^2 .
\]
For each prime order the weights \(v_p(J_n)\log p\) decreasingly. The first is \(O(N^2)\) by size; among the \(k\) largest two indices have gap at most \(N/(k-1)\), and the fixed-gap gcd bound applies. Summing the resulting \(O(1+N^2/(k-1)^2)\) estimates proves the claim.

An infinite sequence with \(p^2\mid J_n\) and \(\log p\ge\delta n^2\) would disprove abc by the pointwise radical comparison on the slice. The common-divisor bound forces each such prime to occur at most once even among all eligible indices up to a constant times \(\log p\). The lcm estimate supplies large prime powers across indices without bounding the exponent of each new prime at the index where it appears.

In particular, let \(L_N=\operatorname{lcm}_{3\le n\le N,\ n\ {\rm odd}}J_n\). A sufficient aggregate disproof criterion is
\[
 \liminf_{N\to\infty}\frac{\log\operatorname{rad}(L_N)}{N^3}
                  <\frac43\widehat h(P).
\]
Indeed \(\log(L_N/\operatorname{rad}L_N)\le\sum_n\log(J_n/\operatorname{rad}J_n)\). A fixed proportional deficit in the lcm radical therefore gives terms with \(\log(J_n/\operatorname{rad}J_n)\gg n^2\) at unbounded indices, using \(O(n^2)\) as a uniform upper bound. The height comparison then gives a fixed exponent violation. The converse implication from a single exceptional subsequence to this aggregate deficit need not follow.

## A finite check

At \(N=209\) the normalized \(L_N\) has bit length \(3{,}956{,}311\), and the product divided by the lcm has bit length 874. Exactly \(191\) is common to \(J_{209}\) and the entire earlier lcm. Direct evaluation gives \(191^2\parallel J_{209}\). This illustrates why recurrence of an entire power and recurrence of its base prime must be distinguished. The associated \(C=W^{12}\) has 101,144 decimal digits. For the full support integer \(D_{209}\) defined in the slice note, \(v_2=27\), \(v_{191}=2\), and \(\lfloor C\,2^{26}\cdot191/D_{209}\rfloor=50846\). Since \(\operatorname{rad}(D_{209})=\operatorname{rad}(3UVW)\), this certifies \(C/\operatorname{rad}(3UVW)>50846\). [Integer check](abc_eisenstein_quartic_lcm_check.py) · [Search bounds and square residues](abc_eisenstein_slice_paired_quartic.md)

Complete prime factorizations of both quartics at \(n=15\) are also certified in the integer check. Together with the factorizations at earlier indices, they rule out a squared prime above 3 at every odd \(n\le15\) without a prime cutoff.
