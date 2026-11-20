# The full radical distribution on the modulus-24 Eisenstein conic

Order the primitive positive triples
\[
 U^2+3V^2=W^{12},\qquad p\mid W\Longrightarrow p\equiv1\pmod{24}
\]
by \(W\le X\), giving equal weight to each triple. The condition on prime divisors of \(U\) in the [abc transfer](abc_eisenstein_power_conic.md) follows from the equation. In this population one always has \(144\mid V\). Write
\[
 D=\frac{3UVW}{\operatorname{rad}(3UVW)},\qquad
 Z=\frac{W^{13}}{\operatorname{rad}(3UVW)}.
\]

The number of triples is asymptotic to \(cX/(\log X)^{3/4}\) for an explicit \(c>0\). The integer \(D\) has a limiting distribution, in total variation on the positive integers, described by independent local variables. For \(p\ge5\) put \(\chi_p=(-3/p)\), and let \(J_p\) be the limiting valuation of \(UVW\). For \(j\ge1\),
\[
 \Pr(J_p\ge j)=
 \begin{cases}
 26/[p^{j-1}(p+1)] & p\equiv1\pmod{24},\\
 \gcd(24,p-\chi_p)/[p^{j-1}(p-\chi_p)] & p\not\equiv1\pmod{24}.
 \end{cases}                                                    \tag{1}
\]
At 2 and 3 let \(v_2(V)=4+G_2\), \(v_3(V)=2+G_3\) in distribution, with \(\Pr(G_p\ge k)=p^{-k}\) for \(k\ge0\). The limiting integer is
\[
 D_\infty=2^{3+G_2}3^{2+G_3}\prod_{p\ge5}p^{(J_p-1)_+}.
                                                               \tag{2}
\]
Only finitely many factors above 3 exceed 1 almost surely. In particular the limiting probability of squarefreeness of \(UVW\) away from 6 is the positive product \(\prod_{p\ge5}(1-\Pr(J_p\ge2))\). The proportion with the minimum possible defect \(D=72\) is one third of this product.

The same statements hold when one counts only prime \(W\equiv1\bmod24\). There is one triple per such prime. In (1) use \(\gcd(24,p-\chi_p)/[p^{j-1}(p-\chi_p)]\) at **all** \(p\ge5\). For either population,
\[
 Z\ \Longrightarrow\ Z_\infty=\frac{2D_\infty}{\sqrt3\,|\sin\Theta|},
 \qquad \Theta\text{ uniform on }[0,2\pi],\quad
 \Theta\text{ independent of }D_\infty.                       \tag{3}
\]
Its tail has the asymptotic
\[
 \lim_{T\to\infty}\sqrt{\frac{\log\log T}{\log T}},
    \log\!\left(T\Pr(Z_\infty>T)\right)=
    \begin{cases}7\sqrt2&\text{full population},\\
                  4\sqrt6&\text{prime }W.
    \end{cases}                                                \tag{4}
\]
These are iterated limits, first \(X\to\infty\) at fixed threshold. No uniformity at growing radical thresholds for the original family or the fourth-power transfer inputs is inferred.

## Counting the parameter ideals

Set \(K=\mathbb Q(\sqrt{-3})\), \(\mathcal O=\mathbb Z[(-1+\sqrt{-3})/2]\) and \(\mathcal P=\{p:p\equiv1\bmod24\}\). For each allowed \(W>1\), select one of the prime ideals above each \(p\mid W\) and give it exponent \(v_p(W)\). All resulting ideals \(I\) are principal, coprime to their conjugates, and determine primitive triples by \(U+V\sqrt{-3}=\beta^{12}\) followed by taking absolute values of both coefficients, where \((\beta)=I\). Units have twelfth power 1. Conversely, given a primitive triple the ideals of \(U\pm V\sqrt{-3}\) are coprime twelfth powers. To see this, \(W\equiv1\bmod24\), primitivity excludes common prime divisors, and neither prime above 2 or 3 divides the product. A twelfth root of the ideal has generator \(\beta\) whose twelfth power differs from \(U+V\sqrt{-3}\) by a unit. Reduction modulo 2 forces that unit to be \(\pm1\): \(U\) is odd and \(V\) even by reducing modulo 4 and 8, and every nonzero residue modulo \(2\mathcal O\) has cube 1. Thus the correspondence from ideals is exactly two-to-one, pairing the conjugates. The two coordinates cannot vanish since \(I\) is coprime and unequal to its conjugate.

The unweighted ideal count has Dirichlet series
\[
 F_1(s)=\prod_{p\in\mathcal P}\left(1+\frac{2}{p^s-1}\right),\qquad
 c=\frac{1}{2\Gamma(1/4)}
       \lim_{s\downarrow1}(s-1)^{1/4}F_1(s).
\]
Here and below finite congruence conditions and the angle may be kept simultaneously. We detail this use of the classical Selberg–Delange theorem. Take an integral modulus \(M\) divisible by 24, finite ray characters on ideals coprime to \(M\), and angle characters \(e^{6in\arg\beta}\), invariant under units. Their products \(\psi\) are Hecke characters. The weighted Dirichlet series excludes primes dividing \(M\), and one may also exclude any fixed finite set of rational primes. Its Euler factor at \(p\in\mathcal P\) outside these primes is
\[
 1+\sum_{e\ge1}\frac{u^e+v^e}{p^{es}}
   =\frac{1-uvp^{-2s}}{(1-up^{-s})(1-vp^{-s})},\quad
 u=\psi(\mathfrak p),\quad v=\psi(\overline{\mathfrak p}).
\]
Projecting onto the progression \(1\bmod24\) gives, for \(\Re s>1\),
\[
 \log F_\psi(s)=\frac18\sum_{\eta\bmod24}
       \log L_K(s,\psi\cdot(\eta\circ N))+A_\psi(s),           \tag{5}
\]
where the difference is holomorphic in \(\Re s>1/2\). This follows by comparing linear terms at degree-one prime ideals; the degree-two prime ideals and all terms of degree two and higher converge absolutely there. In (5) Euler factors at finitely many excluded places may be removed on both sides. Norms of units modulo \(24\mathcal O\) fill the four classes \(1,7,13,19\bmod24\). Indeed the norm modulo 3 of a unit is 1, while the norms \(x^2+3y^2\) of odd norm modulo 8 realize all four odd classes there. CRT applies. Thus exactly two of the eight characters \(\eta\) have \(\eta\circ N=1\).

For the trivial weight (5) has pole exponent \(1/4\). Otherwise the same pole occurs precisely when \(n=0\) and the finite weight is a character pulled back from the norm modulo 24. In that case the weight equals 1 on all admissible ideals. Every remaining weight has exponent zero, because none of the Hecke functions on the right has a pole. Fixed-character Hecke zero-free regions and Selberg–Delange give respectively \(C X(\log X)^{-3/4}(1+o(1))\) and \(o(X(\log X)^{-3/4})\). All characters and moduli are fixed in this use. More explicitly each Hecke function is holomorphic and nonzero in a standard logarithmic zero-free region at height at least one, after extracting a possible zeta pole at 1 and shrinking the region for the finitely many fixed small-height zeros. Their fixed fractional powers have polylogarithmic growth in a smaller such region. The classical Selberg–Delange expansion applies to the resulting Dirichlet series; its coefficients are bounded by the divisor function, and for exponent zero the first coefficient is proportional to \(1/\Gamma(0)=0\). [Selberg–Delange theorem, Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, II.5](https://doi.org/10.1090/gsm/163)

It follows by finite character orthogonality and the Weyl criterion that among ideals coprime to the fixed modulus the residue of a generator is uniform in the norm-one-modulo-24 subgroup of \((\mathcal O/M\mathcal O)^\times/\mathcal O^\times\), independently of its angle modulo \(\pi/3\). Omitting a fixed allowed \(p\) multiplies the unweighted asymptotic constant by \((p-1)/(p+1)\), the reciprocal of its Euler factor at 1. For prime \(W\), the same finite and angular equidistribution holds, by the fixed-character prime ideal theorem applied to (5)'s progression projector directly on prime ideals; degree-two ideals contribute \(O(\sqrt X)\). In this population omitting finitely many primes changes its count by \(O(1)\).

## Local laws

For \(p\ge5\) prime to \(W\), reduction of \(\beta\) runs uniformly over units modulo \(p^j\) for any unit-invariant test; equivalently use the uniform measure on raw unit residues before dividing by the diagonal six global units. CRT makes tests invariant at each place independent, including the norm condition at 2 and 3. The projective class of \(\beta\) maps by \(\beta\mapsto z=\beta/\bar\beta\) isomorphically onto the norm-one group of order \(p^{j-1}(p-\chi_p)\), by the kernel of this map and its cardinality. The prime-to-\(p\) torsion is cyclic of order \(p-\chi_p\) by reduction to the finite fields, with roots of unity lifting uniquely. Since \(U,V\) cannot both be divisible by \(p\),
\[
       p^j\mid UV\quad\Longleftrightarrow\quad z^{24}=1\bmod p^j.
\]
The factors \(z^{12}-1\) and \(z^{12}+1\) are coprime for odd \(p\). This gives \(d_p=\gcd(24,p-\chi_p)\) permissible projective classes at every level.

At \(p\in\mathcal P\) in the full population,
\[
 \Pr(p\nmid W)=\frac{p-1}{p+1},\qquad
 \Pr(v_p(W)=e)=\frac{2(p-1)}{(p+1)p^e}\quad(e\ge1).
\]
Remove the Euler factor and multiply the count by the ideal power of either orientation to see the second formula. Residues at other primes and angles remain uniform after multiplying by any such fixed power. In particular the unbounded exponents cause no dependence: the displayed probabilities sum to one, so finite truncation suffices. Adding the disjoint events \(p^j\mid UV\) and \(p^j\mid W\) proves (1). Simultaneous prime valuations follow by removing finitely many Euler factors and applying the same calculation and CRT.

Choose a generator \(\beta\equiv1\bmod2\mathcal O\) by multiplying by a sixth root of unity; this selects its integral-coordinate presentation \(\beta=x+y\sqrt{-3}\) uniquely up to sign. Indeed the unit group surjects onto \((\mathcal O/2\mathcal O)^\times\). The norm formula forces \(x\) odd and \(4\mid y\) from \(W\equiv1\bmod8\). Conversely these two 2-adic conditions imply the required norm and primary residue. At 3 the only condition is \(3\nmid x\). Uniform measure on these residues is therefore product additive Haar measure, restricted at 2 to odd \(x\) and \(y\in4\mathbb Z_2\), and at 3 to \(x\in\mathbb Z_3^\times\), \(y\in\mathbb Z_3\). Quotienting by the remaining simultaneous sign does not alter the tests. A direct factorization gives
\[
 V=\left|12xy(x-y)(x+y)(x-3y)(x+3y)
     (x^2-3y^2)(x^2-6xy-3y^2)(x^2+6xy-3y^2)\right|.
\]
Thus \(v_2(V)=2+v_2(y)\) and \(v_3(V)=1+v_3(y(x-y)(x+y))\). At 3 the three roots \(y=0,x,-x\) are distinct modulo 3 and exhaust its residues. These identities give the asserted local laws and the divisor 144.

## Uniform tail of the square-divisor sieve

Write \(H=\lceil\sqrt X\rceil\), so every primary parameter lies in the box \(|x|,|y|\le H\) and is primitive. Away from 6 the homogeneous polynomial for \(UVW\) is separable modulo every prime: the change \(z=(x+y\sqrt{-3})/(x-y\sqrt{-3})\) takes its 26 roots to \(\mu_{24}\cup\{0,\infty\}\). Every \(p^2\) therefore selects at most 26 projective classes modulo \(p^2\); it must square into one unique factor. The factors of \(U\) are the three quartics
\[
 F_0=x^4-18x^2y^2+9y^4,\qquad F_\pm=F_0\pm(12x^3y-36xy^3).
\]
Every other factor has degree at most two, including \(W=x^2+3y^2\). This also identifies a maximal degree four in the free prime-norm and general norm parameters, compared with degree sixteen after the fourth-power substitution.

For precision we prove
\[
 \lim_{L\to\infty}\limsup_{X\to\infty}
 \frac{\#\{\text{triples}: W\le X,\;\exists p>L,\ p^2\mid UVW\}}
      {\#\{\text{triples}: W\le X\}}=0                             \tag{6}
\]
in both populations. The following three ranges suffice.

* For \(L<p\le (\log H)^3\), impose the \(\le26\) projective root classes modulo \(p^2\) and sieve out disallowed prime divisors \(\ell\) of \(x^2+3y^2\). In the full population take \(\ell\equiv7,13,19\bmod24\); for prime norm take every \(\ell\equiv1\bmod3\), ignoring the possibility that the norm itself is a tiny sieving prime. Sieve only up to \(z=H^{1/10}\) and omit \(\ell=p\). At a sieving prime the forbidden proportion is \(g(\ell)=(2\ell-1)/\ell^2\) from two distinct lines. The Selberg upper-bound sieve gives
\[
 \ll \frac{H^2}{p^2(\log H)^\kappa}+H^{3/2},\qquad
 \kappa=3/4\text{ in the full population},\quad \kappa=1\text{ for prime }W.
\]
Here the initial root classes consist of \(O(p^2)\) individual residue pairs. The count with a squarefree sieving divisor \(d\) has main term \(g(d)\) times the initial box-area main term and error \(O(2^{\omega(d)}(H+p^2d))\): each of the \(O(p^2 2^{\omega(d)}d)\) classes modulo \(p^2d\) has box counting error \(O(1+H/(p^2d))\). Summing this error with the usual Selberg weights \(3^{\omega(d)}\) up to \(z^2\) is \(O(H^{3/2})\) uniformly. The sieve denominator \(\sum_{d\le z}\mu^2(d)\prod_{\ell\mid d}g(\ell)/(1-g(\ell))\) over the sieving primes is \(\gg(\log z)^\kappa\), uniformly after omitting one prime. Indeed restrict the Euler product to \(\ell\le z^\delta\): its total mass is \(\asymp_\delta(\log z)^\kappa\) by Mertens' theorem in progressions. Its normalized mass has expectation of \(\log d\) equal to \(\sum g(\ell)\log\ell=O(\delta\log z)\), so at least half lies below \(d=z\) for small fixed \(\delta\). Prime norms \(\le z\) contribute \(O(z)\) per tested \(p\). Summing and dividing by the population size gives \(O(1/L)+o(1)\).

* For \((\log H)^3<p\le H^2/(\log H)^2\), any two unequal primitive directions in the same projective class modulo \(p^2\) have determinant a nonzero multiple of \(p^2\), hence angular separation \(\gg p^2/H^2\). There are \(O(1+H^2/p^2)\) pairs per class. Summing over these primes gives \(O(H^2/(\log H)^2)\), negligible in both populations.

* For \(p>H^2/(\log H)^2\), only a quartic can be divisible by \(p^2\) when \(H\) is large. It then has the form \(F_i(x,y)=b p^2\ne0\) with signed \(0<|b|\ll(\log H)^4\). Here is a short uniform square sieve for the resulting twists. Choose \(Q=H^{1/3}\), and average the quadratic characters of \(bF_i(x,y)\) for primes \(q\in[Q,2Q]\) away from its fixed quartic discriminant and the prime factors of \(b\). At a nonzero square value all but \(O(1)\) of the characters equal 1 since \(|bF_i|\ll H^4(\log H)^4\). Squaring the average, the diagonal contributes \(O(H^2\log Q/Q)\). For distinct \(q,q'\), put \(m=qq'\). The full sum of \((bF_i/q)\) over residue pairs modulo \(q\) is \(O(q^{3/2})\): on each nonzero second coordinate scale by its fourth power, then use the Hasse–Weil bound for the squarefree quartic; the axis contributes \(O(q)\). CRT gives \(O(m^{3/2})\) for the full mixed sum. Tile the box by complete squares of side \(m\); discarded strips contain \(O(Hm+m^2)\) pairs. Thus the mixed sum is \(O(H^2/\sqrt m+Hm+m^2)\), and the number of pairs for any single \(b\) is \(O(H^{5/3}\log H)\). The polylogarithmically many twists still give \(o(H^2/\log H)\).

This proves (6). The calculation can also use the stronger uniform quartic-twist estimate obtained by [2-isogeny descent](abc_eisenstein_twelfth_large_squares.md). Combining (6) with fixed-prime convergence, and then cutting off the exponents at those finitely many primes, proves total-variation convergence in (2). Equidistribution of the angle survives the same truncations. Since \(2\sqrt3 UV=W^{12}|\sin(24\arg\beta)|\) and the absolute sine has the same law for uniform angle modulo \(\pi/3\) as on the whole circle, (3) follows.

## The limiting upper tail

Let \(M(s)=\mathbb E[D_\infty^{1-s}]\) for \(0<s<1\), \(r=1/s\). Denote the numerator and the final factor in (1) by \(k_p,B_p\), so \(\Pr(J_p\ge j)=k_p/(p^{j-1}B_p)\), \(B_p=p+O(1)\). Summation by parts in the local distribution gives
\[
 M_p(s)=1+\frac{k_p}{B_p}\frac{1-p^{s-1}}{p^s-1},\qquad p\ge5.
\]
The Euler product converges for every \(s>0\). The logarithms of the factors from 2 and 3 are \(O(\log r)\) near \(s=0\). In order of residue classes \(1,5,7,11,13,17,19,23\bmod24\), the numerators are \(26,6,6,12,12,6,6,24\) in the full population. For prime \(W\) replace the initial 26 by 24. Their prime average \(A\) is respectively \(49/4\) or 12. We claim
\[
                      \log M(s)\sim\frac{Ar}{\log r}.           \tag{7}
\]

For \(p\le r/(\log r)^2\) the bound \(\log M_p\ll\log(2r)\) and the prime count give \(O(r/(\log r)^2)\). For \(r/(\log r)^2<p\le r\), use \(\log M_p\ll r/(p\log p)\). The sum is \(O(r\log\log r/(\log r)^2)\) by partial summation from the prime upper bound, or by dyadic subdivision of this interval. For \(r<p\le r^B\) with fixed \(B>1\), each local logarithm is uniformly \((1+o(1))k_p r/(p\log p)\). Indeed \((\log p)/r\to0\) and the largest of these summands tends to zero. The prime number theorem in the eight fixed classes gives total
\[
 (A+o(1))\frac r{\log r}(1-1/B).
\]
The remaining tail is \(O(r/(B\log r))\), using \(p^s-1\ge s\log p\) and partial summation above \(r^B\). Letting \(B\to\infty\) proves (7).

For any \(T=e^t\) the sine distribution in (3) gives
\[
 e^t\Pr(Z_\infty>e^t)\asymp \mathbb E[\min(D_\infty,e^t)],
                                                               \tag{8}
\]
with absolute constants by the arcsine distribution on \([0,1]\). The upper bound for this expectation is \(e^{st}M(s)\). Setting \(s=\sqrt{2A/(t\log t)}\) and using (7) yields logarithmic upper bound \((2\sqrt{2A}+o(1))\sqrt{t/\log t}\).

For the lower bound, give each outcome tilted mass \(D_\infty^{1-s}/M(s)\) times its probability, and write \(L=\log D_\infty\), \(h_s=\log M(s)\). Under this tilted probability,
\[
                L/(h_s/s)\longrightarrow1\quad\text{in probability}.
\]
In fact for fixed \(0<\delta<1\) and small fixed \(a>0\), Markov's inequality bounds the logarithm of the probability of the upper failure by
\[
 h_{(1-a)s}-h_s-a(1+\delta)h_s
   =\big[(1-a)^{-1}-1-a(1+\delta)+o(1)\big]h_s.
\]
The coefficient is negative for small enough \(a\). For the lower failure the coefficient is \((1+a)^{-1}-1+a(1-\delta)+o(1)\), also negative. Fix \(0<\epsilon<1/3\) and now take \(s=\sqrt{2A/((1-\epsilon)t\log t)}\). Then \(h_s/s\sim(1-\epsilon)t\), so the interval \([(1-2\epsilon)t,t]\) has tilted probability tending to one. Consequently
\[
 \log\mathbb E[\min(D_\infty,e^t)]
    \ge h_s+s(1-2\epsilon)t+o(1).
\]
Let \(\epsilon\downarrow0\) to match the upper coefficient \(2\sqrt{2A}\). Equation (8) gives (4). In particular the limiting distribution has every positive moment of order less than one and has infinite first moment.

At cutoff \(10^6\), the two squarefreeness products are 0.4869956242 (full) and 0.4872886681 (prime norm). Their remaining absolute errors are below \(26/10^6\), by \(\sum_{n>N}26/(n(n-1))=26/N\). A finite enumeration through \(W\le120000\) gives 1,498 distinct triples in the full family and 1,384 with prime norm, agreeing with the independent orientation count and the progression prime count. All satisfy \(144\mid V\).
