# A radical saving from a prescribed moving prime in the difference of two close integers

Fix \(\delta>0\) and \(s\ge0\). For **every sufficiently large prime** \(p\) there are coprime positive integers \(B<C\) and an integer \(k\ge2\) such that, on writing \(A=C-B\) and \(R=\operatorname{rad}(ABC)\), one has
\[
   p^k\mid A,\qquad A\le C p^{-s},\qquad
   \frac{p^{k-1}}{\operatorname{rad}(BC)}\ge p^\delta,\qquad
   \frac C R\ge p^{\delta+s}.
   \tag{1}
\]
The prime power in (1) alone pays for every prime divisor of the two endpoints and leaves the factor \(p^\delta\). One can take
\[
   k\sim\frac{1+\delta+s}{2}\log\log p,\qquad
   \log C\le\left(\frac{(1+\delta+s)^2}{8}+o(1)\right)
                  (\log p\,\log\log p)^2 .
   \tag{2}
\]
In particular the guaranteed saving satisfies
\[
  \log(C/R)\ge
  \left(4\sqrt2\,\frac{\delta+s}{1+\delta+s}-o(1)\right)
                   \frac{\sqrt{\log C}}{\log\log C}.
   \tag{3}
\]
The prime \(p\) can thus run through any prescribed infinite set. At \(s=0\), the sole specified prime power gives the whole stated gain without using an estimate on the relative difference.

There is also a **fixed-exponent** version. Prescribe any integer \(k\ge2\), choose \(0<\delta<k-1\), put \(\lambda=k-1-\delta\), and fix \(s\ge0\). For every sufficiently large prime \(p\), (1) holds at that \(k\) with
\[
 \log C\le \left(\frac{1}{2e^{1+(k+s)/\lambda}}+o(1)\right)
                       (\lambda\log p)^{1+(k+s)/\lambda}.
 \tag{4}
\]
For example every sufficiently large prime admits a triple with \(p^2\mid A\), \(A\le Cp^{-1/4}\), \(\operatorname{rad}(BC)\le p^{1/2}\) and \(C/R\ge p^{3/4}\), with \(\log C\ll(\log p)^{11/2}\). Divisibility by \(p^k\) is the only local information used; its actual valuation may be higher.

At \(p=1489\) one explicit pair is \(C=2^{352}\), \(B=3^{162}5^{41}\). Both are congruent to \(1{,}259{,}922\bmod p^2\), and \((C-B)/p^2\equiv511\bmod p\), so the valuation is exactly two. Integer comparison gives \(39(C-B)<C<40(C-B)\). Thus this single square certifies \(C/R>39\cdot1489/30>1935\) without factoring the remaining cofactor.

## Finding the two endpoints

Write \(L=\log p\), \(Y=(k-1-\delta)L\), and take the longest initial segment \(S\) of rational primes with \(\sum_{q\in S}\log q\le Y\). Both regimes have \(\max S\sim Y<p\), so every element is a unit modulo \(p^k\). Put \(m=|S|\) and \(w_q=\log q\). The integral vectors satisfying
\[
        \prod_{q\in S}q^{z_q}\equiv1\pmod {p^k}
\]
form a lattice in \(\mathbb R^m\) of index at most \(\varphi(p^k)<p^k\).

For \(H>1\) take the centrally symmetric convex body
\[
   \mathcal B_H=\{z:\;\sum_q w_q\max(z_q,0)\le H,\quad
                          \sum_q w_q\max(-z_q,0)\le H\}.
\]
In an orthant with \(j\) positive coordinates its volume is \(H^m/[j!(m-j)!\prod w_q]\), by the volumes of the two simplices. Summing gives \(\binom{2m}{m}H^m/(m!\prod w_q)\). Intersect with \(|\sum_q w_qz_q|\le p^{-s}\). This preserves at least the proportion \(p^{-s}/H\). Indeed the section areas perpendicular to this linear functional are even and nonincreasing on the positive half-axis by Brunn–Minkowski, and the functional is supported on \([-H,H]\).

Define
\[
 H_0=2p^{(k+s)/m}\left(\frac{m!\prod w_q}{\binom{2m}m}\right)^{1/m},
 \qquad H=(1+1/m)H_0^{m/(m-1)} .
\]
The volume of the intersection exceeds \(2^mp^k\). Minkowski's convex body theorem gives a nonzero vector of the stated lattice inside it. Split its positive and negative coordinates into the numerator and denominator of a reduced positive ratio \(U/V\). Unique factorization gives \(U\ne V\). Let \(B=\min(U,V)\), \(C=\max(U,V)\). The integer \(C-B\) is divisible by \(p^k\), and \(\log C\le H\). Also
\[
  (C-B)/C=1-\exp(-|\log(U/V)|)\le p^{-s},\qquad
  \operatorname{rad}(BC)\le\prod_{q\in S}q\le p^{k-1-\delta}.
\]
These inequalities give (1), since \(\operatorname{rad}(A)\le A/p^{k-1}\).

## The height calculation

The prime number theorem with its classical error term gives
\[
   Y/m=\log Y-1+o(1),\qquad
   (\prod_{q\in S}\log q)^{1/m}=(1+o(1))\log Y .
\]
For the first formula let \(x=\max S\). One has \(Y-\vartheta(x)=O(\log Y)\) from the next prime and \(x=Y+o(Y/\log^2Y)\) from the prime number theorem. Then use \(\pi(x)=x/\log x+x/\log^2x+O(x/\log^3x)\). The second formula follows by partial summation or by separating \(q\le x/(\log x)^2\), whose proportion is \(O(1/\log^2x)\). Stirling's estimate now gives
\[
  H=(1+o(1))\frac{Y}{2e}\,
       \exp\!\left(\frac{(k+s)L}{Y}[\log Y-1+o(1)]\right).
   \tag{5}
\]
Here \((k+s)L/Y\) stays bounded and \(\log H_0/m=o(1)\) in both regimes. At fixed \(k\) this is (4).

For varying \(k\), write \(\ell=\log L\), choose \(k\sim t\ell\) with \(t>0\), and use
\[
 \frac{(k+s)L}{Y}=1+\frac{1+\delta+s}{k-1-\delta},\qquad
 \log Y\sim\ell.
\]
Equation (5) becomes
\[
 H=(1+o(1))\frac{t^2}{2e^2}\exp((1+\delta+s)/t)\,(L\ell)^2 .
\]
The choice \(t=(1+\delta+s)/2\) minimizes this coefficient and gives (2). Since \(C>p^k\) tends to infinity and \(\sqrt{x}/\log x\) is eventually increasing, (1) and (2) give (3). The scale in (3) is sublinear in \(\log C\). Infinitely many triples with \(C/R\ge C^\epsilon\) for a fixed \(\epsilon>0\) remain unproved.

## A counting limit for the fixed exponent

If a common set of primes \(S'\) is charged at \(\prod_{q\in S'}q\le p^\lambda\), its size is at most \((\lambda+o(1))L/\log L\) by comparison with the initial segment. Suppose \(H=L^\beta\), \(\beta>1\). The number of distinct reduced \(S'\)-supported positive fractions whose numerator and denominator are at most \(e^H\) is at most
\[
  2^{|S'|}\binom{\lfloor2H/\log2\rfloor+|S'|}{|S'|}
   \le \exp\{(\lambda(\beta-1)+o(1))L\}.
\]
The first inequality counts the signs and the nonnegative absolute exponents with total at most \(2H/\log 2\). Consequently, for \(s=0\), forcing an equality by counting more than \(p^k\) fractions in the available residue classes requires \(\beta\ge1+k/\lambda\). This matches the exponent in (4) for that counting argument. Estimates exploiting a smaller actual image or unusually short individual congruences can behave differently.

The earlier optimized smooth-fraction count uses a power of two as modulus; Bright's larger published constant concerns unrestricted triples. [Earlier calculation and literature comparison](abc_smooth_congruences.md)

## How often a prescribed prime can work at smaller height

For \(\lambda>0,\ \beta>1\) let \(N_\lambda(L,\beta)\) count all coprime positive pairs \(B<C\) such that \(\operatorname{rad}(BC)\le e^{\lambda L}\) and \(\log C\le L^\beta\), allowing an arbitrary prime support for each pair. Then
\[
       \log N_\lambda(L,\beta)
          =\big(\lambda\max(1,\beta-1)+o(1)\big)L .
       \tag{6}
\]
Thus for \(0<\lambda<1\) and \(1<\beta<1+1/\lambda\), the primes \(p\in[P,2P]\) for which any such endpoints satisfy
\[
 \operatorname{rad}(BC)\le p^\lambda,\qquad
 \log C\le(\log p)^\beta,\qquad p\mid(C-B)
\]
number at most \(P^{\lambda\max(1,\beta-1)+o(1)}\). Their fraction among all primes tends to zero. This permits even divisibility by the first power of \(p\). In particular for almost every \(p\), the saving from a prescribed square alone under the budget \(\operatorname{rad}(BC)\le p^{1-\delta}\) requires superpolynomial height.

For the lower bound in (6), all pairs \((1,n)\) with \(2\le n\le e^{\lambda L}\) qualify for large \(L\). Also take the initial prime segment with \(\sum\log q\le\lambda L\), of size \((\lambda+o(1))L/\log L\). Every integer \(\prod q^{j_q}\) with \(0\le j_q\le\lfloor L^\beta/(\lambda L)\rfloor\) qualifies as \(C\) with \(B=1\), apart from the value 1. These two counts give both terms in the maximum.

For the upper bound, put \(H=L^\beta\) and take \(v>0,t>1\). A prime in a reduced pair occurs with positive exponent in one of the two entries. Consequently
\[
    N_\lambda(L,\beta)\le
    \exp(2vH+t\lambda L)
       \prod_q\left(1+\frac{2q^{-t}}{q^v-1}\right).
    \tag{7}
\]
Here \(\log(BC)\le2H\). For fixed \(t>1\) the logarithm of the product is \(O_t(v^{-1/t})\) for \(0<v<1\). Indeed use \(q^v-1\ge v\log2\), enlarge the sum to all positive integers and split it at \(M=(2/[v\log2])^{1/t}\). The initial part is \(O_t(M)\) by summing \(1+\log(M/n)\), and the tail is \(O_t(M)\) by integrating \(M^t n^{-t}\). Put \(v=L^{1-\beta}/\log L\) and \(t>\max(1,\beta-1)\). Both \(2vH\) and the logarithm of the product are \(o(L)\); send \(t\) down to the threshold. For the prime count use \(L=\log(2P)\); each nonzero difference \(C-B\) has at most \(L^\beta/\log P\) prime divisors in the interval.

The boundary exponent also gives density zero for a sufficiently small absolute height coefficient depending on \(\lambda\). More explicitly, let \(0<\lambda<1\), \(T=1/\lambda\), \(D_T=\pi/\sin(\pi/T)\), and
\[
       c_\lambda=\frac{\lambda}{4}\,e^{-1-T}D_T^{-T}.
\]
For each \(0<c<c_\lambda\), the number of primes \(p\in[P,2P]\) with \(\operatorname{rad}(BC)\le p^\lambda,\ p\mid C-B,\ \log C\le c(\log p)^{1+T}\) for some reduced pair is
\[
                 O_{\lambda,c}\!\left(P
                    \exp[-\epsilon_{\lambda,c}\log P/\log\log P]\right)
                 \quad\text{for some }\epsilon_{\lambda,c}>0 .
       \tag{8}
\]

To see the extra saving, apply (7) at \(H=cL^{1+T}\), \(t=T+u/\log L\), \(v=b/(L^T\log L)\), with fixed \(u\in\mathbb R\), \(b>0\). The prime number theorem gives
\[
 \sum_q\log\!\left(1+\frac{2q^{-t}}{q^v-1}\right)
   =\left[D_T(2e^{-u}/b)^{1/T}+o(1)\right]\frac{L}{\log L}.
\]
Indeed for \(q/L\) in a compact subinterval of \((0,\infty)\) the summand tends uniformly to \(\log(1+(2e^{-u}/b)(q/L)^{-T})\), and the rescaled prime sums converge to its integral. The terms \(q<\sqrt L\) contribute \(O(\sqrt L\log L)\). For \(\sqrt L\le q\le dL\) with \(0<d<1\) the summand is \(O_{b,T,u}(1+\log(L/q))\), from \(q^v-1\ge v\log q\); dyadic summation and Chebyshev's prime bound make this \(O(d(1+|\log d|)L/\log L)\). For \(q\ge DL,\ D>1\), the summand is \(O_{b,T,u}((q/L)^{-(T+1)/2})\) for large \(L\), and the dyadic tail costs \(O(D^{-(T-1)/2}L/\log L)\). This justifies both limits in the integral. Integration by parts and the beta integral give \(\int_0^\infty\log(1+x^{-T})\,dx=\pi/\sin(\pi/T)\).

The coefficient of \(L/\log L\) in the log upper bound (7), after its leading term \(L\), is therefore
\[
 \lambda u+2cb+D_T(2e^{-u}/b)^{1/T}.
\]
Set \(b=\lambda/(2c)\), \(u=\log(2D_T^T/b)\). The coefficient becomes \(1+\lambda+\lambda\log(4cD_T^T/\lambda)<0\). Counting prime divisors in each difference as above adds only \(O(\log L)\) to its logarithm. This proves (8). These scarcity statements allow individual primes to have much smaller witnesses.
