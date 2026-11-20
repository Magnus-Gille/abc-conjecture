# Counting all indices with squarefree denominator cofactor up to a height

Let \(E:y^2=x^3-36x\), \(G=(-3,9)\), and \(B_n\) be the positive square root of the reduced denominator of \(x(nG)\). Set \(D_n=\prod_{v_p(B_n)\text{ odd}}p\), \(H=\widehat h(G)\), and
\[
                   N(Y)=\#\{n\ge1\text{ odd}:D_n\le Y\}.
\]
There is an absolute \(\delta>0\) such that \(N(Y)\ll Y^{1/2-\delta}\). This counts indices of unrestricted size. The proof uses the quadratic large sieve, the Bombieri–Vinogradov theorem, an elementary upper-bound sieve, and a bound for rational points on the genus-three curves associated to individual cofactors. The last section gives a separate effective enumeration in \(\exp(\exp(O((\log(2Y))^2)))\) bit operations.

## A supply of supersingular primes with smooth periods

Fix a reduced progression \(h\equiv b_0\pmod {m_0}\) contained in \(3\bmod4\). One may take \(m_0=4,b_0=3\) for the denominator alone, or \(m_0=24,b_0=7\). There is a fixed \(\theta<1/2\), depending only on this progression, such that \(\gg Z/\log Z\) primes \(h\le Z\) in the progression have **every full prime power dividing \(h+1\)** at most \(Z^\theta\).

First fix a parameter \(0<e<1/40\) and set
\[
          a=1/2-3e,\qquad b=1/2-2e,\qquad \theta=1/2-e.
\]
Count pairs of primes \(h\le Z\) and \(Z^a\le r\le Z^b\) with \(h\equiv b_0\bmod m_0\) and \(h\equiv-1\bmod r\). For large \(Z\), the two congruences specify a reduced class modulo \(m_0r\). The Bombieri–Vinogradov theorem, summed over these distinct moduli below \(m_0 Z^b\), gives
\[
 (1+o_e(1))\frac{Z}{\varphi(m_0)\log Z}
                 \sum_{Z^a\le r\le Z^b\atop r\text{ prime}}\frac1r.
\]
The reciprocal-prime sum tends to \(\log(b/a)>0\) for fixed \(e\).

Remove pairs for which a prime \(s>Z^\theta\) divides \(h+1\). It differs from \(r\), and \(h+1=urs\) with \(u\le2Z^{1-a-\theta}=2Z^{4e}\). For a fixed \(r,u\), write \(A=ur\), \(x=(Z+1)/A\); a nonempty contribution has \(x>Z^\theta\). The ordinary upper-bound sieve for the two linear forms \(s,As-1\) gives, with an absolute constant,
\[
       \#\{s\le x:s,As-1\text{ prime}\}
           \ll (A/\varphi(A))^2 x/(\log x)^2 .
\]
This estimate is uniform in \(A\). For an explicit route, sieve by primes through \(z=x^{1/10}\), omitting 2 and the primes of \(A\); each remaining prime omits two residue classes. The elementary Selberg upper sieve has error at most \(O(z^4(\log z)^{O(1)})\) and denominator at least \(\sum_{d\le z,(d,2A)=1}\mu^2(d)2^{\omega(d)}/d\). The Euler product over primes through \(z^{1/C}\) gives a lower bound \(\gg (\varphi(A)/A)^2(\log z)^2\) for this sum: under weights \(2^{\omega(d)}/d\) on their squarefree products the mean \(\log d\) is \(\le2\sum_{p\le z^{1/C}}\log p/p\), less than \((\log z)/2\) for a sufficiently large absolute \(C\). Thus at least half of the product's mass lies at \(d\le z\). The two prime-equals-sieving-prime exceptions cost \(O(z)\). In this argument one may enlarge the absolute constant to cover bounded \(x\).

Now \((ur/\varphi(ur))^2\ll (u/\varphi(u))^2\), and
\(\sum_{u\le V}(u/\varphi(u))^2/u\ll 1+\log V\) with an absolute constant. The latter follows by expanding the multiplicative weight as a divisor sum whose coefficients at primes are \((1-1/p)^{-2}-1=O(1/p)\), supported on squarefree integers. Summing first over \(u\) and then over \(r\), the removed pairs number at most
\[
        C_1(e+1/\log Z)\frac{Z}{\log Z}
                     \sum_{Z^a\le r\le Z^b\atop r\text{ prime}}\frac1r ,
\]
with \(C_1\) independent of \(e<1/40\). Choose \(e\) so small that \(C_1e<1/(4\varphi(m_0))\).

For \(m_0=4\) or 24, one explicit conservative choice is \(e=10^{-15}\). To track constants, apply the ordinary Montgomery large sieve for sifted sets with level \(Q=\lfloor\sqrt x\rfloor\), sieving at primes \(p\le w=x^{1/100}\), \(p\nmid 2A\). Its upper bound is \((x+Q^2+1)/G(Q)\), with the same squarefree lower sum for \(G(Q)\). In the full Euler product the complementary factors satisfy
\[
 \prod_{p\le w}(1+2/p)(1-1/p)^2
 \ge \tfrac12\prod_{n\ge3}(1-3/n^2)>1/25.
\]
The last inequality follows from \(\log(1-u)\ge-3u/2\) for \(0\le u\le1/3\) and \(\sum_{n\ge3}1/n^2\le1/2\). Also \(\prod_{p\le w}(1-1/p)^{-1}\ge\sum_{n\le w}1/n\ge\log w\). Removing the primes of \(2A\) retains a proportion at least \((\varphi(A)/(2A))^2\). Under the remaining Euler product distribution, \(\mathbb E\log d\le 2\sum_{p\le w}\log p/p\le4\log w\) eventually, so at least half its mass has \(d\le Q\). Thus \(G(Q)\ge (\varphi(A)/A)^2(\log x)^2/(2\cdot10^6)\). Including the at most \(2w\) prime-equals-sieving-prime cases, the twin-linear-form bound holds for large \(x\) with constant \(10^7\). Further,
\[
 \sum_{u\le V}\frac{(u/\varphi(u))^2}{u}\le e^6(1+\log V),
\]
since \((1-1/p)^{-2}-1\le6/p\) and \(\sum_{n\ge2}n^{-2}\le1\). Use \(x\le2Z/(ur)\), \((r/\varphi(r))^2\le4\), \(1/\theta^2<5\), and \(1+\log(2Z^{4e})\le5e\log Z\) eventually. The coefficient of \(e\) in the bad-pair count is then below \(10^{12}\), before division by the fixed progression density. With the displayed \(e\) its cost is less than \(1/(4\varphi(m_0))\) of \((Z/\log Z)\sum_r1/r\) for either modulus. The thresholds in this calculation are asymptotic.

There are also \(o_e(Z/\log Z)\) possible integers \(h\le Z\) with some \(p^j\mid(h+1)\), \(j\ge2\), \(Z^\theta<p^j\le Z+1\). Indeed the count is \(O(Z\sum_{p^j>Z^\theta,j\ge2}p^{-j}+\sqrt Z\log Z)=O(Z^{1-\theta/2}+\sqrt Z\log Z)\). For the reciprocal sum, split the prime bases at \(Z^{\theta/2}\) and sum geometric tails. Each \(h\) has at most \(O(1/a)\) choices for \(r\), since their product divides \(h+1\). Consequently removing the higher powers and then forgetting the marked divisor still leaves \(\gg_e Z/\log Z\) distinct primes. This proves the assertion. For the weaker conclusion at any fixed \(\theta>1/2\), Bombieri–Vinogradov alone supplies the probes by marking a prime divisor between \(Z^{1-\theta+\epsilon}\) and \(Z^{1/2-\epsilon}\) and removing the negligible higher powers.

## The quadratic large sieve in the cofactor variable

Let \(F=\log Y\), fix a small \(\eta>0\), and choose \(Z=(\eta F)^{1/\theta}\). For the primes just found, \(h+1\) divides \(t=\operatorname{lcm}(1,\ldots,\lfloor\eta F\rfloor)\). Chebyshev's bound gives \(\log t\le2\eta F\) for large \(Y\). At these primes the curve has trace zero by pairing \(x\) and \(-x\), and the two-isogenous curve \(E_0:y^2=x^3+36x^2+36x\) has the same group order \(h+1\). Thus the reduction of \(P=(-2,8)\) on \(E_0\) has order dividing \(t\).

For every odd \(n\), all prime divisors of \(B_n\) are \(1\bmod12\); this follows from rational two-descent on \(E\) because \(G\) has odd order at such a divisor. In particular none of the selected primes \(h\equiv3\bmod4\) divides \(B_n\). The [local denominator-squareclass test](abc_full_quartic_square_denominators.md) gives \((D_n/h)=(8(6-x([n]P))/h)\) at a finite reduction and \(+1\) at the identity. Every resulting symbol is nonzero. Hence the global vectors \(((D_n/h))_h\) are among at most \(t\) sign words.

Let \(m\gg Z/\log Z\) be the number of auxiliary primes, set \(k=\lfloor F/\log Z\rfloor\), and let \(\mathcal U\) contain all products of \(k\) distinct probes. Each is an odd squarefree integer at most \(Y\). Different subsets give distinct products. Since \(\log(m/k)\ge(1/\theta-1)\log F+O_\eta(1)\),
\[
               |\mathcal U|={m\choose k}\ge(m/k)^k
                               \ge Y^{1-\theta-o(1)} .
\]
For a prescribed word \((\sigma_h)_h\) use the coefficients \(a_u=\prod_{h\mid u}\sigma_h\) on \(\mathcal U\), zero elsewhere. Each occurring squarefree cofactor \(d\) for that word satisfies \(d\equiv1\bmod4\), so quadratic reciprocity gives \((u/d)=(d/u)=a_u\) for every \(u\in\mathcal U\). The amplification sum \(\sum_u a_u(u/d)\) therefore equals \(|\mathcal U|\). The quadratic large sieve at length \(Y\) in both variables gives
\[
 \sum_{d\le Y}^{\mathrm{odd\ squarefree}}\left|\sum_u a_u(u/d)\right|^2
                 \ll_\epsilon Y^{1+\epsilon}\sum_u |a_u|^2.
\]
Consequently at most \(Y^{\theta+\epsilon+o(1)}\) occurring cofactors give the prescribed word. Summing the at most \(Y^{2\eta}\) words and taking \(\eta\) arbitrarily small shows that the number of occurring squarefree \(d\le Y\) is \(O_\epsilon(Y^{\theta+\epsilon})\). [D. R. Heath-Brown, *A mean value estimate for real character sums*, Acta Arith. 72 (1995), 235–275](https://doi.org/10.4064/aa-72-3-235-275)

The [genus-three covering and uniform Mordell–Lang bound](abc_congruent_six_pointwise_cofactor_growth.md) bounds the number of positive odd indices with fixed kernel \(d\) by \(A^{1+\omega(d)}\), for an absolute \(A\). Uniformly for \(d\le Y\) this is \(Y^{o(1)}\), by \(d\ge(1+\omega(d))!\). Thus \(N(Y)\ll_\epsilon Y^{\theta+\epsilon}\); taking \(\epsilon<(1/2-\theta)/2\) proves the claimed strict improvement below \(1/2\). The same transfer holds for any fixed \(\theta<1\) for which \(Z^{1-o(1)}\) primes of the indicated type exist with all prime powers of \(h+1\) at most \(Z^\theta\).

## Independent bound from Gaussian auxiliary primes

The following argument uses elementary Chinese remaindering in place of the quadratic large sieve and does not use primes in progressions. It proves
\[
 \liminf_{Y\to\infty}\frac{\log(Y/N(Y))}{\sqrt{\log Y}}
         \ge (\log2)\sqrt{3\pi/(16H)}>0.73. \tag{1}
\]
It identifies three families of primes whose signs can be prescribed independently in the varying integer cofactor.

### Three families of auxiliary primes

Let \(T\) run over the three nonidentity rational two-torsion points, and write \(S_T=G+T\). In \(K=\mathbf Q(i)\) let \(I=(\alpha)\) be an odd ideal. The content of \(I\) is \(g=\gcd(|a|,|b|)\) for \(\alpha=a+bi\). Every ideal divisor of \(I\) has content dividing \(g\), since divisibility by the rational integer ideal \((c)\) is precisely divisibility of both coefficients by \(c\).

Fix \(K_1\ge1\). For every sufficiently large \(NI\) with content at most \(K_1\), there is a good place of \(K\) where \(S_T\) has exact Gaussian annihilator \(I\). Here is the adaptation of the [Gaussian height and inversion argument](abc_congruent_six_gaussian_first_primes.md). On the flat complex torus, if \([\alpha]S_T\) has distance \(\delta\) to the origin, complex conjugation shows that \([\bar\alpha]S_T\) has the same distance. By adding and subtracting, both \([2a]S_T\) and \([2b]S_T\) have distance at most \(2\delta\), using that multiplication by \(i\) is an isometry. Bezout coefficients for \(a,b\) of total absolute value \(O(1+|\alpha|/g)\) express \([2g]S_T=[2g]G\) as a combination of those points. The finitely many points \([2g]G\), \(1\le g\le K_1\), have positive distance from the origin. Hence \(\log^+|x([\alpha]S_T)|\le \log NI+O_{K_1}(1)\).

In particular the log norm of the denominator ideal of \([\alpha]S_T\) is \(2H NI+O_{K_1}(\log(2NI))\), and it is always at most \(2H NI+O(1)\), by the canonical height and \(\widehat h(S_T)=H\). Omit the places above 2 and 3 at a cost \(O(\log(2NI))\): for a fixed positive integer \(m\) taking \([m]S_T\) deep into the local formal group, \([\alpha][m]S_T\) has logarithmic formal depth \(v_{\mathfrak p}(\alpha)+O(1)\), and multiplication by \(m\) cannot reduce a positive depth. At all good places the excess above the initial depth sums to at most \(\log NI\), by the formal logarithm and the factorization of \((\alpha)\). Thus the sum of the exact-annihilator masses over \(J\mid I\) is \(2H NI+O_{K_1}(\log(2NI))\). Möbius inversion, with the same content bound at all divisors, gives primitive mass
\[
          2H\Phi_K(I)+O_{K_1}(2^{\omega_K(I)}\log(2NI)).
\]
This is positive for all sufficiently large \(NI\), since \(\Phi_K(I)=(NI)^{1-o(1)}\) and \(2^{\omega_K(I)}=(NI)^{o(1)}\). The three rational seeds form a fixed finite set throughout.

Assign to each such \((T,I)\), up to conjugating the ideal, one underlying rational prime \(h\) realizing its annihilator. Different classes for a given \(T\) have different \(h\), as the two places of a rational prime have conjugate annihilators. Across different \(T\) the primes are also disjoint. Indeed \(S_T\) modulo \(h\) has odd integer order dividing \(NI\), while the difference of two distinct \(S_T\) is a nonzero rational two-torsion point in good reduction. It follows in particular that \(G\) has even order at every selected \(h\). No such prime divides an odd \(B_n\), and
\[
                           \log h\le 2H NI+O(1).                          \tag{2}
\]

### Counting the auxiliary primes and the allowed character vectors

Choose \(Z\) large, \(L=\lfloor Z/\log Z\rfloor\), and \(t=\operatorname{lcm}(1,\ldots,L)\). Use odd ideals \(I\) of norm at most \(Z\) for which \(NI\mid t\) and with content at most \(K_1\). There are \(\pi Z/8+O(\sqrt Z+1)\) odd ideals of norm at most \(Z\) by counting Gaussian integers with coordinates of opposite parity in the disk and dividing by four units. Up to conjugation the leading constant is \(\alpha_0=\pi/16\), since self-conjugate odd ideals have a real generator and contribute \(O(\sqrt Z)\). By partial summation, the sum of the norms of all these conjugacy classes before the two restrictions is \((\alpha_0/2+o(1)) Z^2\).

At most \(O(Z/K_1)\) ideals have content exceeding \(K_1\), by summing \(O(Z/c^2)\) over \(K_1<c\le\sqrt Z\). Also only \(o(Z)\) ideals have \(NI\nmid t\). A rational prime \(p>L\) dividing \(NI\) then costs at most \(O(Z/p)\) ideals; from \(L\) to \(Z\) the reciprocal prime sum is \(O(\log\log Z/\log Z)\) by partial summation and the elementary prime upper bound. For \(L<p^e\le Z\) with \(e\ge2\), divisibility by \(p^e\) in the norm costs at most \(O((e+1)Z/p^e)\) ideals by prime-ideal factorization. There are \(O(\sqrt Z\log Z)\) candidate powers, with \(e=O(\log Z)\) and \(Z/p^e=O(\log Z)\). This also costs \(o(Z)\).

Discarding the finitely many classes below the annihilator threshold, we have \(b\ge (3\alpha_0-O(1/K_1)-o_{K_1}(1)) Z\) distinct primes in the three families. Their squarefree product \(M\) satisfies, by (2),
\[
                        \log M\le(3\alpha_0 H+o(1))Z^2.                 \tag{3}
\]
For each selected \(h\), \([2t]G=O\) modulo \(h\). On the curve \(E_0:y^2=x^3+36x^2+36x\), the rational two-isogeny to \(E\) sends \(P=(-2,8)\) to \(G+(6,0)\). Thus \([4t]P=O\) modulo \(h\). At odd indices, the [local denominator-squareclass test](abc_full_quartic_square_denominators.md) reads
\[
       (D_n/h)=(B_n/h)=(8(6-x([n]P))/h)
\]
on a finite reduction, and gives \(+1\) at the identity. The character is nonzero, since \(G\) has even order here. The entire sign vector on the \(b\) primes therefore takes at most \(4t\) possible values, and \(\log(4t)=O(L)=o(Z)\) by Chebyshev's bound.

Each individual word allows precisely \(\varphi(M)/2^b\) residue classes modulo \(M\). In particular for \(M\le Y\), at most \(2Y\cdot4t/2^b\) integers \(d\le Y\) pass. The [genus-three covering and uniform Mordell–Lang bound](abc_congruent_six_pointwise_cofactor_growth.md) bounds the number of positive odd indices with fixed kernel \(d\) by \(A^{1+\omega(d)}\) for an absolute \(A\). For every fixed integer \(j>1\) the \(j\)-th moment of this weight on \(d\le Y\) is \(O_j(Y(\log(2Y))^{O_j(1)})\). Indeed \(A^{j\omega(d)}\) is bounded by the ordinary \(k\)-fold divisor function for any integer \(k\ge A^j\), whose summatory function is \(O_k(Y(\log(2Y))^{k-1})\). Hölder's inequality transfers a fraction \(1-1/j\) of the logarithmic saving for admissible integers to \(N(Y)\), at a cost \(O_j(\log\log(2Y))\). Take \(Z=(1-\epsilon)\sqrt{\log Y/(3\alpha_0H)}\), so (3) guarantees \(M\le Y\). Let \(Y\) grow first and then \(K_1,j\) grow and \(\epsilon\) decrease to zero. This gives (1).

## A running-time bound for the exact census

Here is a deterministic bit bound using the odd-index square classification, elementary lifting, and Linnik's effective least-prime theorem. Write \(D=D_n\le Y\). For every odd prime \(q\) the square classification gives a prime \(p(q)\mid D_q\). It has exact rank \(q\) and satisfies \(p(q)>2q\) by full rational two-torsion and Hasse. On the primes of \(n\) the map \(q\mapsto p(q)\) is injective because the rank identifies \(q\). It partitions these vertices into increasing chains, with distinct terminal primes \(p\nmid n\) in \(D\); the terminal's odd depth survives multiplication from its preceding index. Along a chain ending at \(p\), the logs of the preceding vertices descend by at least \(\log2\) per step starting from \(\log p\). Their sum is at most \((\log p)^2/(2\log2)\). Summing the chains gives
\[
         P^+(n)< Y/2,\qquad
         \log\operatorname{rad}(n)\le (\log Y)^2/(2\log2) \quad(n>1).
\]
For every \(q\mid n\), any prime of \(D_q\) not in \(D\) must divide \(n\) by the formal valuation rule. Thus \(D_q\mid D\operatorname{rad}(n)\) and \(\log D_q\le\log Y+(\log Y)^2/(2\log2)\).

For each odd prime \(q<Y/2\) compute \(B_q\) exactly, strip its prime powers through \(Y\), and test whether the remainder is a square. Discard \(q\) if it is not, since any such larger prime would be prime to \(n\) and would persist. Otherwise the stripping gives \(D_q\); also discard \(q\) if its log exceeds the bound just proved. These comparisons can use relaxed integral thresholds, for example \(D_q\le (2Y)^{2\lceil\log_2(2Y)\rceil}\), to avoid real-arithmetic requirements.

For each remaining \(q\), choose by CRT a reduced class modulo \(4qD_q\) which is \(3\bmod4\), \(1\bmod q\), and is a nonsquare at one prime of \(D_q\) and 1 at all its other primes. These moduli are coprime, \(D_q>1\), and its primes are \(1\bmod12\). By Linnik a prime \(h\) in this class can be found with \(h\le\exp(O((\log(2Y))^2))\). Testing candidates by trial division suffices for this complexity bound. One can skip \(h=3\), which is already excluded by \(h\equiv1\bmod q\). The curve \(E_0\) has \(h+1\) points because it is isogenous to \(E\), whose trace vanishes at \(h\equiv3\bmod4\). Hence the sign of \((B_j/h)\) on odd indices is periodic modulo \(h+1\), and the signs at 1 and \(q\) differ by reciprocity. Set \(t_q=\operatorname{ord}_{h+1}(q)\le h+1\); this is defined since \(h+1\equiv2\bmod q\).

Take the first positive \(e_q\equiv1\bmod t_q\) for which \(2q^{e_q}>Y\). The [periodic prime-power witness](abc_full_quartic_effective_prime_support.md) gives a prime of odd depth at exact rank \(q^{e_q}\), larger than \(Y\), so \(v_q(n)<e_q\). Explicitly the characters at \(q^{e_q-1},q^{e_q}\) have opposite signs. The ratio of the denominators is therefore nonsquare, and no existing prime changes depth under multiplication by \(q\), since it has rank a power of \(q\) and is larger than \(2q\). Each \(e_q\) is at most \(h+2+\log(2Y)/\log q\). The log of the product \(N_0=\prod q^{e_q-1}\) over retained primes is therefore at most \(\exp(O((\log(2Y))^2))\). Enumerate its divisors, compute each required elliptic multiple by binary addition, strip all primes through \(Y\), and square-test the remaining integer; when it is square, check that the kernel computed in the stripping step is at most \(Y\). There are at most \(N_0\) divisors, and the abscissa and ordinate computations through index \(N_0\) use integers of \(O(N_0^2+1)\) bits by the canonical height. Ordinary integer arithmetic, powering, trial division through \(Y\), and exact square testing thus fit the claimed double-exponential bit bound. This algorithm does not require a numerical uniform Mordell–Lang constant.


The inverse estimate controls the absolute multiplicity of small cofactors across all indices. Even a bound of the shape \(N(Y)\ll_\epsilon Y^\epsilon\) would still permit exceptional isolated indices with \(\log D_n=o(n^2)\). A pointwise height comparison to \(\log B_n\asymp n^2\) requires additional information on prime valuations at each individual index.
