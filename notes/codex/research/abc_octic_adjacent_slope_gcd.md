# Neighboring slope denominators and first-rank excess

On the full two-square orbit let \(E:v^2=u^3-8u^2+8u\), \(A=(1,1)\), \(J=(0,0)\), and \(x(P)=(v(P)+u(P))/(2(u(P)-1))\). At odd \(N=2n-1\ge3\), write the signed slope \(x([n]A)=s_N/t_N\) in lowest terms with positive denominator. There are positive coprime integers \(a_j,b_j\) with \(u([j]A)=a_j^2/b_j^2\) for every \(j\ge1\). Then
\[
 |s_{2n-1}|=a_{n-1}a_n,\qquad t_{2n-1}=2b_{n-1}b_n.
\]
In particular the adjacent slopes recover the elliptic abscissa by two gcds:
\[
 \gcd(|s_{2n-1}|,|s_{2n+1}|)=a_n,\qquad
 \gcd(t_{2n-1},t_{2n+1})=
 \begin{cases}2b_n,&2\mid n,\\4b_n,&2\nmid n.\end{cases}
\]

Indeed ordinary addition on \(E\) gives \(4x(P)^2=u(P)u(P-A)\). Starting from \(u(A)=1\), this gives the square assertion by induction at the nondegenerate multiples. At an odd prime, a prime divisor of \(a_j\) reduces \([j]A\) to \(J\) and a prime divisor of \(b_j\) reduces it to the identity. A cross cancellation between the abscissas at consecutive multiples would therefore force \(A=J\) modulo that prime, impossible. At 2 the even multiples lie in the formal group with \(v_2(b_j)=v_2(j)\), and the odd multiples reduce to the smooth point \((1,1)\) on the displayed integral model. Hence every \(a_j\) is odd. These facts give the reduced slope coordinates. If an odd prime divided both \(a_{n-1},a_{n+1}\), or both \(b_{n-1},b_{n+1}\), then \([2]A=O\) in its reduction group. This is impossible since the ordinate of \(A\) is 1. The indicated power of 2 follows from \(v_2(b_j)\). Exact rational addition checked the coordinate identities for all \(2\le n\le101\) and both gcds for \(2\le n\le100\). [Orbit, height and dyadic details](abc_octic_full_mixed_orbit.md)

## Exact first denominator and simultaneous quality gaps

For \(p>7\) let \(r_p\) be the order of \(A\) modulo \(p\), and \(d_p\) the formal depth of \([r_p]A\). Set
\[
 W_r=\sum_{p>7,\ r_p=r}(d_p-1)\log p,\qquad
 \mu=\limsup_{r\to\infty}W_r/r^2.
\]
An odd prime first occurs anywhere in the slope denominators at \(t_{2r_p-1}\), with exponent exactly \(d_p\). In fact \(p\mid t_N\) precisely when \(N\equiv\pm1\pmod{2r_p}\). At every \(t_{2jr_p-1}, t_{2jr_p+1}\) the exponent is \(d_p+v_p(j)\). These assertions follow from the coordinate formula and the unramified odd-prime formal logarithm. Thus \(W_r\) equals the entire excess at primes \(p>7\) appearing for the first time in the denominator sequence at \(2r-1\).

Let \(L_N^{\rm ord}\) sum \((d_p-1)\log p\) over \(p>7\) in the five ordinary factors \(s_N,t_N,D_N,\sqrt{Y_N},\sqrt{V_N}\). They have \(r_p\mid k\) for some \(k\in\{2N,N-1,N+1\}\). The three sums \(\sum_{r\mid k}r^2\le\zeta(2)k^2\) and the denominator at \(2r-1\) give the comparison
\[
 \frac{\mu}{4}\le\limsup_{N\to\infty,\ N\ {\rm odd}}\frac{L_N^{\rm ord}}{N^2}
 \le 6\zeta(2)\mu.
\]
The upper bound follows by discarding the bounded contribution of any fixed finite interval of ranks before taking the limsup.

There is a local-in-index version. The abscissa height gives \(W_r\le C r^2\) for a fixed \(C\). For any positive integer \(J_0\), the mass at ranks \(r<k/J_0\) in the divisors of a fixed \(k\) is at most \(Ck^2\sum_{j>J_0}j^{-2}\le Ck^2/J_0\). If \(L_N^{\rm ord}\ge\delta N^2\), choose \(J_0=\lceil 15C/\delta\rceil\). For large \(N\) at least \(\delta N^2/2\) survives the three truncations. As the sum of the remaining squared ranks is at most \((6N^2+2)\zeta(2)\), there is a single rank \(r\ge(N-1)/J_0\) at which the primes contributing to this very index have total excess at least \(\delta r^2/(13\zeta(2))\). They all divide both neighboring denominators at \(2jr\pm1\) for every \(j\ge1\).

In particular if \(\mu>0\), choose one sequence \(r_i\to\infty\) realizing the limsup. At all the indices \(2j r_i\pm1\), the same rank-\(r_i\) primes give at least \(W_{r_i}\) logarithmic excess in each triple, simultaneously for every fixed \(j\). With \(h=\widehat h(A)\) and \(q_N=\log c_N/\log\operatorname{rad}(a_N b_N c_N)\), this implies
\[
 \liminf_{i\to\infty}\big(1-q_{2j r_i\pm1}^{-1}\big)\ge \frac{\mu}{16h j^2}.
\]
Here the two signs may be chosen independently. Indeed \(T_N=2|s_Nt_ND_NU_N|\sqrt{Y_NV_N}\ll c_N\), its radical is that of the triple, and \(\log c_N=4hN^2+O(1)\). This proves simultaneous fixed quality gaps throughout every fixed finite collection of these adjacent pairs. [Valuations and whole radical](abc_octic_whole_radical_tail.md)

## First occurrences in the whole family

The first occurrence in the full triple can be earlier than the first slope denominator. Apart from the moving factor \(U\), it can be described exactly for large \(r=r_p\). At an odd prime the factors \(\sqrt Y\sqrt V,D\) correspond to \([N]A=O,J\), respectively. The numerator contains \(p\) only when \(r\) is even and \([r/2]A=J\), in which case \(N\equiv r\pm1\pmod{2r}\). The first ordinary occurrence is therefore as follows.

| Rank and reduction | First ordinary occurrence |
|---|---|
| \(r\) odd | \(\sqrt{Y_rV_r}\) |
| \(r\) even, \(J\notin\langle A\rangle\) | \(t_{2r-1}\) |
| \(4\mid r\), \(J\in\langle A\rangle\) | \(s_{r-1}\) |
| \(r\equiv2\pmod4\), \(J\in\langle A\rangle\) | \(D_{r/2}\) |

A prime dividing any moving \(U_M\) has odd rank and cyclic CM annihilator of norm \(r\). The total first-depth mass at *all* such primes of a given rank is \(O(2^{\omega(r)}r)\), by the CM height bound. Hence removing primes that might occur earlier in a moving factor costs \(o(r^2)\) for every one of the packets above. [First-occurrence argument](abc_octic_first_occurrence.md)

## Near-maximal ranks in the moving factor

The preceding ordinary contribution and the moving excess exhaust a fixed-exponent failure. Here is a uniform restriction on the latter. Write \(L=N^2+2\). The exact CM denominator packets on \(E'\) have ranks \(r\mid L\) (orders of \(S\) at these primes), and mass \(h\varphi(r)+O(2^{\omega(r)}\log(2L))\) at rank \(r\). The error summed over all \(r\mid L\) is \(L^{o(1)}\). All packets of rank exceeding \(2N\) make their first appearance in the whole triple at this \(N\). [CM packet formula and global first appearances](abc_octic_mixed_skew_denominator.md)

Let \(G=\gcd(a,L)\) for uniform \(a\bmod L\). The full main-term weight of packets with \(L/r\) in any given set is \(hL\) times the probability that \(G\) belongs to that set. For each fixed \(z>0\) and \(\ell=\log\log L\), one has
\[
 \limsup_{N\to\infty}\mathbb E\exp(z\log G/\ell)
 \ \le\ \exp\left(\tfrac12\int_0^1 (e^{zu}-1)\,du/u\right).
\]
Indeed at \(q^b\parallel L\) the local valuation of the gcd has tails \(q^{-j}\) up to \(b\), independently by CRT. Its moment factor at \(t=z/\ell\) is at most \(1+(q^t-1)/(q-q^t)\), by summing the infinite geometric tail. Primes \(q>\log L\) contribute \(O_z(1/\ell)\) to the log product, since their number is at most \(\log L/\ell\). All smaller primes are split in \(\mathbb Q(\sqrt{-2})\), and replacing \((q-q^t)^{-1}\) by \(q^{-1}\) costs \(o_z(1)\) by dominated convergence, using \(q^t\le e^z\) there. Partial summation with the prime number theorem in progressions gives the displayed integral for the sum over all split \(q\le\log L\): first restrict \(\log q/\ell\) to \([\epsilon,1]\), then bound the complementary sum by \(O_z(\epsilon)\) using \((q^t-1)\ll_z t\log q\).

Suppose \(\log(U_N/\operatorname{rad} U_N)\ge\delta h L\) along a sequence, with \(0<\delta<1\). Choose a constant \(b=b(\delta)\) such that
\[
 \inf_{z>0}\exp\left(-bz+\tfrac12\int_0^1(e^{zu}-1)\,du/u\right)<\delta/2.
\]
Then large indices in that sequence receive at least \((\delta/2)hL\) excess, up to \(o(L)\), from globally new primes with \(r\ge L/(\log L)^b\). Exceeding multiplicities coming from formal lifting after the first depth cost \(O(\log L)\) altogether. In particular one can take \(b=O(\log(1/\delta)/\log\log(1/\delta))\) as \(\delta\downarrow0\), by using \(z=\log b\). These conclusions decide where an excess must occur and leave open whether one occurs infinitely often.

The logarithmic scale is necessary for any bound based only on full packet mass. Let \(P_y\) be the product of odd split primes up to \(y\), prescribe one root of \(-2\) at each such prime, and choose an odd \(N\in[P_y,3P_y]\) by CRT. Then \(P_y\mid L\) and \(\log L\sim y\) by the prime number theorem in progressions. For any \(0<\epsilon<1\),
\[
 \Pr(G\le y^\epsilon)\le
 \prod_{y^\epsilon<q\le y,\ q\text{ split}}(1-1/q)\longrightarrow \sqrt\epsilon.
\]
For any \(b_N\to0^+\) it follows on this sequence that \(\Pr(G\le(\log L)^{b_N})\to0\), by sending \(\epsilon\) to zero. Thus ranks \(r\ge L/(\log L)^{o(1)}\) can account for a vanishing proportion of *all* logarithmic mass in \(U_N\). This sharpness assertion does not presume excess on the constructed indices.

## The second occurrence of a new moving prime

Every prime \(p\mid U_N\) of rank \(r>2N\) has its next occurrence anywhere in the entire triple sequence at precisely \(M=r\), in \(\sqrt{V_r}\). The third is at \(M=2r-N\), in the moving factor. In fact its complete support at positive odd indices is
\[
 \begin{array}{c|c}
 M\bmod 2r &\text{factor at }M\\\hline
 \pm N &U_M\\
 r &\sqrt{V_M}\\
 \pm1&t_M .
 \end{array}
\]
The table refers to admissible \(M\ge3\). The ranks in the moving factor are odd. At the chosen split place, \([N]S=[\tau]S\) in reduction for the point \(S=R+J'\) on the two-isogenous curve. Positive denominator valuation of \([M-\tau]S\) at one of the two places is equivalent to \([M]S=\pm[N]S\), hence to \(M\equiv\pm N\bmod r\); taking odd representatives gives the first row. As \(S\) has odd order \(r\), the point \(R=S+J'\) has order \(2r\) and its isogeny image \(A\) has order \(r\). The odd multiples have \(\sqrt V=B_M(S)\), \(\sqrt Y=B_M(R)\), proving the second row. For odd rank, the ordinary classification leaves only the third row. Thus the excess isolated by the preceding logarithmic cutoff has no second occurrence before \(L/(\log L)^b\).

## Overlap between different indices

For \(T_N=2|s_Nt_ND_NU_N|\sqrt{Y_NV_N}\), one has uniformly for \(d\ge2\)
\[
 \log\gcd(T_N,T_{N+2d})\ll d^2 .
\]
At any odd common prime, the exponent at an index is exactly the formal depth of \([N]A-X\) at a place of the CM field, for a choice of \(X\in\{O,J,A,-A,\tau A,-\tau A\}\). Choice of a fixed place above a split prime is harmless because both signs are available. The ordinary local identities apply at every odd prime. The moving factor has prime factors only \(1\bmod8\) and therefore never causes an exception to the local identity at 3, 5 or 7. At each prime shared with the second index, the smaller exponent is bounded by the formal depth of \([2d]A+X-Y\) for some pair of marks. For \(d\ge2\) all 36 differences are nonzero: a relation would kill a nonzero quadratic integer times the nontorsion point \(A\) up to rational two-torsion. The total finite denominator logarithms of these points are \(O(d^2)\) by the canonical abscissa height. Each selected odd place contributes at least its rational weighted depth to this bound. At 2 each individual exponent is \(1+\max(v_2(N-1),v_2(N+1))\). Their minimum is \(O(\log(2d))\) by subtracting the two selected arguments, which differ by a nonzero element of \(\{2d,2d-2,2d+2\}\).

For \(d=1\), the only identically zero difference has \(X=-A,Y=A\). Its assigned primes divide the slope numerators or denominators at both indices. Writing \(N=2n-1\), the reduction of \([n]A\) is a two-torsion point and belongs to \(\{O,J,A,A+J\}\) by slope support. Since \(A\) has nonzero ordinate in all odd characteristics, this leaves \(O,J\), giving exactly the odd depths of \(b_n,a_n\), respectively. The remaining pairs of marks contribute a bounded amount by the same height argument. The dyadic gcd formula above supplies a further factor of at most eight. Consequently
\[
 a_n b_n\mid\gcd(T_{2n-1},T_{2n+1}),\qquad
 \gcd(T_{2n-1},T_{2n+1})\ll a_n b_n
\]
with an absolute constant for this curve.

For \(4\le H\le N/2\), let \(E_N(H)\) be the sum of \((d_p-1)\log p\) over \(p>7\) dividing \(T_N\) and also \(T_M\) at any odd \(M\) with \(4\le|N-M|\le H\). There are two uniform bounds:
\[
 E_N(H)\ll H^3,\qquad E_N(H)\ll NH+N^{1+o(1)}.
\]
For the first, \(d_p\le v_p(T_N),v_p(T_M)\) at any shared prime. Sum the gcd bound over the shifts. For the second, if \(p\mid U_N\) and shares such an \(M\), its rank is \(O(N)\), by \(r\mid N\pm M\) at another moving factor or \(r\le2M\) at an ordinary occurrence. The total packet mass over small ranks dividing \(N^2+2\) is \(N^{1+o(1)}\). If \(p\) is ordinary at \(N\) and ever occurs in a moving factor, its rank divides one of \(k\in\{2N,N-1,N+1\}\) and these primes collectively contribute \(O(r^{1+o(1)})\) per rank, hence \(N^{1+o(1)}\) in total. For all remaining primes both occurrences are ordinary. At rank \(r\) they lie in pairs separated by two around \(0\) or \(r\) modulo \(2r\), or lie singly at \(r,r/2,3r/2\); which are possible depends on the parity and \(J\), as above. Any two indices separated by more than two therefore differ by at least \(r/2-2\). Thus \(r\le2H+4\). Summing the height bound \(Cr^2\) over these divisors of each \(k\) gives \(O(kH)\) by the reciprocal-square divisor tail.

In particular the excess at any high-quality index \(N\) is supported, up to \(o(N^2)\), on primes occurring at no other index in a window \(|M-N|\le H=o(N)\) apart from \(N\pm2\). If the excess is at least \(\delta N^2\), a sufficiently small constant multiple of \(\delta N\) gives a window retaining at least half of it. The two indices at distance two may share an entire first-rank packet, as the adjacent slope formula shows.

## Exact correction factors in the adjacent full gcd

For every \(n\ge2\), the bounded factor in the preceding adjacent gcd can in fact be evaluated:
\[
 \frac{\gcd(T_{2n-1},T_{2n+1})}{a_n b_n}
 =4\,14^{\mathbf1_{2\nmid n}}\,765^{\mathbf1_{3\nmid n}}\,
 137^{\mathbf1_{n\equiv\pm1\bmod 11}}.                                      \tag{1}
\]
The dyadic part is 4 for even \(n\), 8 for odd \(n\), from the slope gcd. For odd primes, a baseline collision means that \([n]A\) reduces to \(O\) or \(J\). At such a prime both slope factors have the identical depth of \([n]A\) at its reduced mark, namely \(v_p(a_n b_n)\). The six rational factors have pairwise coprime odd parts, so no other contribution occurs at that prime.

For an ordinary collision outside this baseline, use the residue classes in the first-occurrence table. At odd rank the only possible pair at distance two between different classes (other than the paired denominator poles around zero) joins \(r\) to a neighboring class \(\pm1\), requiring \(r=3\). At even rank, a transition between two distinct centers a distance two apart requires \(r=4\) with \([r/2]A=J\) (origin and middle pairs), or \(r=6\) with \([r/2]A=J\) (one pair and a half-rank singleton). Rank two is impossible at every odd prime. Now \(u(2A)=49/4\) and \(u(3A)=289/2025\). Thus rank three gives precisely 3 and 5 by \(b_3=45\), the rank-four case gives precisely 7 by \(a_2=7\), and the rank-six case gives precisely 17 by \(a_3=17\).

At \(p=3,5,17\), let \(T=O,O,J\), respectively. The point \([3]A-T\) has formal depth \(\lambda=2,1,1\), respectively. When \(3\mid n\) there is a baseline collision. When \(3\nmid n\), one neighboring index is divisible by three and gives the depth of \([3(2k\pm1)]A\) at \(T\); the other gives the slope depth of \([3k]A\) at \([k]T\), for \(k=(n-1)/3\) or \((n+1)/3\), whichever is integral. The depths are \(\lambda+v_p(2k\pm1)\) and \(\lambda+v_p(k)\), so their minimum is \(\lambda\). These primes give exactly \(3^2\cdot5\cdot17=765\) when \(3\nmid n\). At 7 it is \([2]A-J\) that has depth one. When \(n\) is even there is a baseline collision. For odd \(n\) the two slope factors use \([2k]A,[2(k+1)]A\) for \(k=(n-1)/2\); their depths have minimum one. This gives the extra 7 at odd \(n\).

For any prime in a moving factor at index \(M\), its rank \(r\) is odd and divides \(M^2+2\). An adjacent moving–moving collision requires \(r\mid2\) or \(r\mid2M\pm2\), hence \(r\mid3\) in the latter case. At an adjacent ordinary factor, \(r\) must divide \(M\pm2\) (an origin occurrence), or \(M\pm1,M\pm3\) (a denominator occurrence). Substitution in \(M^2+2\) leaves only ranks 3 or 11. The rank-three primes 3 and 5 do not divide any moving factor. At rank 11, necessarily \(M\equiv\pm3\bmod11\), so by the moving recurrence the prime divides \(U_3=137\). This prime has rank 11 by the CM relation and nontriviality of the reduction of \(A\). Its support table gives a nonbaseline adjacent collision just at \(n\equiv\pm1\bmod11\). There the smaller depth is always one: at the chosen place around \(M\equiv3\bmod22\), subtracting twice the ordinary slope parameter point \([n-1]A\) from the moving formal point gives \([3]A\mp[\tau]A\), of depth one since \(v_{137}(U_3)=1\). Negation gives the other residue class with \([n+1]A\). This proves (1). Exact rational coordinate computations checked (1) at all 127 centers \(2\le n\le128\).
