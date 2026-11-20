# Primitive prime powers in the direct Pell abc triples

Let \(1+2P_{2n}^{\,2}=b_{2n}^{\,2}=C_n\), where
\((1+\sqrt2)^j=b_j+P_j\sqrt2\), and put \(h=\log(1+\sqrt2)\).
Write \(m=4n\). Since \(P_m=2P_{2n}b_{2n}\), the triple is primitive
and its radical is \(R_n=\operatorname{rad}(P_m)\). For \(D(t)=\log(t/\operatorname{rad}(t))\),

\[
 \frac{C_n}{R_n}=\frac{b_{2n}}{2P_{2n}}\exp D(P_m),\qquad
 \frac{b_{2n}}{2P_{2n}}\longrightarrow\frac1{\sqrt2},\qquad
 \log C_n=hm+O(1).
\]

## Exact quality and the rank weights

For odd primes \(p\), let \(r_p\) be the first index for which \(p\mid P_{r_p}\),
let \(w_p=v_p(P_{r_p})\), and set
\[
 E(r)=\sum_{r_p=r}(w_p-1)\log p.
\]
The standard rank and lifting formulas give \(r_p\mid p-(2/p)\) and
\(v_p(P_m)=w_p+v_p(m)\) whenever \(r_p\mid m\). At two,
\(v_2(P_m)=v_2(m)\). Thus for every positive integer \(m\),
\[
 D(P_m)=\log\gcd(m,P_m)-{\boldsymbol 1}_{2\mid m}\log2+
             \sum_{r\mid m}E(r).                                    \tag{1}
\]
For \(r\ge2\) the weight is exactly \(D(|\Phi_r(1+\sqrt2,1-\sqrt2)|)\).
Indeed, a primitive odd prime contributes its first-occurrence valuation
to the homogeneous cyclotomic factor. At an imprimitive odd prime, the
factor has valuation one if \(r/r_p\) is a positive power of \(p\),
and otherwise zero, by Möbius inversion on the lifting formula. At two
the valuation is at most one by inversion on \(v_2(m)\). In particular
\[
 0\le E(r)\le h\varphi(r)+O(1).
\]
The logarithmic Binet error here is bounded uniformly by the sum of
\(\lvert\log(1-((1-\sqrt2)/(1+\sqrt2))^j)\rvert\) over \(j\ge1\).

Set
\[
 H=\limsup_{\substack{m\to\infty\\4\mid m}}\frac1m\sum_{r\mid m}E(r).
\]
Then \(0\le H\le h\) and
\[
 \limsup_{n\to\infty}\frac{\log C_n}{\log R_n}
       =\frac{h}{h-H},
\]
with value \(+\infty\) when \(H=h\). Fixed positive abc exponents occur
infinitely often in the family exactly when \(H>0\). For this positivity
test one may also allow all \(m\), since \(m\mid4m\) and the weights are
nonnegative. The numerical value determining the quality uses \(4\mid m\).

The divisors of \(m\) carry the probability weights \(\varphi(r)/m\).
Equivalently, \(r=m/\gcd(k,m)\) for a uniformly chosen \(1\le k\le m\).
The normalized sum is the mean of \(E(r)/\varphi(r)\) for this law.
It follows that \(H>0\) exactly when there exist constants \(a,b>0\)
and infinitely many multiples of four \(m\) with
\[
  \frac1m \sum_{\substack{r\mid m\\E(r)\ge a\varphi(r)}}\varphi(r)\ \ge b.
\]
In particular \(E(r)=o(\varphi(r))\) suffices to rule out a fixed exponent.

## How small can individual contributions be?

Put \(T(r)=r/\log\log(10r)\). Uniformly as \(m\to\infty\),
\[
 \frac1m\sum_{r\mid m}T(r)
       =\frac{\sigma(m)}{m\log\log m}+o(1).                         \tag{2}
\]
Divisors \(r\le\sqrt m\) cost \(O(\tau(m)/\sqrt m)=o(1)\).
On larger divisors, \(\log\log(10r)=\log\log m+O(1)\), and
\(\sigma(m)/m\ll\log\log m\). Define \(L=\limsup_{r\to\infty}E(r)/T(r)\).
Equation (2) and Gronwall's theorem give the uniform bound
\[
 H\le\min(h,e^\gamma L).
\]
In particular \(E(r)=o(r/\log\log r)\) suffices.

The sharp constant in this bound can already be seen in
an abstract example. For any fixed \(A\ge0\) take
\[
 F_A(r)=\min\{h\varphi(r),\,A T(r)\}.
\]
The classical lower-order theorem for the totient states
\(\liminf \varphi(r)\log\log r/r=e^{-\gamma}\). For
\(A\le he^{-\gamma}\) this yields \(F_A(r)=A T(r)+o(T(r))\).
Its normalized divisor sum thus has limsup \(Ae^\gamma\). To obtain this
lower bound already at multiples of four, take
\(m_j=\mathrm{lcm}(1,\ldots,2j)\). The prime number theorem gives
\(\log m_j\sim2j\), and Mertens' product gives
\(\sigma(m_j)/m_j\sim e^\gamma\log(2j)\). The correction to the Mertens
product is \(\prod_{p\le 2j}(1-p^{-v_p(m_j)-1})\to1\), by dominated
convergence using \(\sum_p p^{-2}<\infty\). For \(A\ge he^{-\gamma}\),
monotonicity and \(\sum_{r\mid m}\varphi(r)=m\) give limsup exactly \(h\).
Hence for every \(A\) these modeled divisor sums attain
\(\min(h,e^\gamma A)\) under the pointwise bounds \(F_A\le AT\) and
\(F_A\le h\varphi\). For \(A=he^{-\gamma}\) every individual contribution
is \(o(r)\), while the aggregate reaches the full linear asymptotic scale.
These weights illustrate the scope of the cyclotomic bound. The analogous
behavior of the actual prime powers in Pell numbers is unknown.

One can additionally put the modeled weights on a set of \(X^{o(1)}\)
indices up to \(X\). Choose a subsequence of the \(m_j\), denoted by
\(M_i\), with \(M_i>M_{i-1}^4\). Keep \(F_A(r)\) only on divisors \(r\mid M_i\)
that exceed \(\sqrt{M_i}\). The small-divisor bound in (2) preserves the
limsup at \(M_i\). For any fixed \(\epsilon>0\), each block contains at
most \(\tau(M_i)\le M_i^{\epsilon/4}\) elements for all large \(i\).
If \(\sqrt{M_i}\le X<\sqrt{M_{i+1}}\), the preceding blocks and the
current one together contain \(O_\epsilon(X^\epsilon)\) elements by
the growth of \(M_i\).

## The exact gain on the logarithmic scale

The same multiples give a concrete unconditional lifting construction.
In the extended real numbers,
\[
 \boxed{\displaystyle
 \limsup_{n\to\infty}\frac{C_n}{R_n\log C_n}
       =\frac1{2\sqrt2\,h}
              \prod_{p\ {\rm odd}}p^{w_p-1}.}                         \tag{3}
\]
Equation (1) gives the upper bound. Along \(m_j=\mathrm{lcm}(1,\ldots,2j)\)
every odd \(p\mid m_j\) satisfies \(p\le2j-1\), hence \(r_p\mid p-(2/p)\mid m_j\).
By lifting, \(m_j\mid P_{m_j}\), also at two. The nested \(m_j\) eventually
contain every fixed rank as a divisor. The primitive products in (1)
therefore increase to the product in (3). This proves equality.
In addition \(\operatorname{rad}(m_j)^2\mid P_{m_j}\) for \(j\ge2\),
including at two. By \(\log\operatorname{rad}(m_j)=\vartheta(2j)\sim
\psi(2j)=\log m_j\), the construction forces a square divisor of size
at least \(m_j^{2-o(1)}\).

The verified weights at \(p=13,31,1546463\) alone multiply to
\(623224589\). The right side of (3) is infinite exactly when infinitely
many Pell–Wieferich primes exist. Even an unbounded gain on this
logarithmic scale would leave the fixed-exponent criterion in (1) open.

## Forcing a quadratic square divisor into either Pell coordinate

There are infinitely many odd squarefree \(n\) with \(n^2\mid b_{2n}\).
There are also infinitely many \(n\) of the form \(2s\), with \(s\) odd
and squarefree, such that \(n^2\mid P_{2n}\). Both assertions admit
deterministic recursive constructions.

For the trace start with \(n=1\) and \(p=3\mid b_2\). Given an odd
\(p\mid b_{2n}\) with \(p\nmid n\), put \(n'=np\) and take \(p'\) to
be the least prime divisor of
\[
 T=\frac{b_{2np}}{p b_{2n}}.
\]
For odd \(p\), the old trace divides the new trace. This follows from
the factorization of \(x^p+y^p\) by \(x+y\) and the Pell trace formula.
At every odd prime \(q\mid b_{2n}\), its valuation in \(b_{2np}\) is
\(v_q(b_{2n})+v_q(p)\), by applying Pell lifting to
\(P_{4n}=2P_{2n}b_{2n}\) and its multiple. Hence \(T\) is an odd integer
coprime to \(b_{2n}\). It is greater than one since
\(b_{2np}=\cosh(2nph)>p\cosh(2nh)\) for \(n\ge1,\ p\ge3\).
Since \(n^2\mid b_{2n}\) by induction, the fresh prime \(p'\)
divides neither \(n\) nor \(p\), and \((np)^2\mid b_{2np}\).
The first indices are \(1,3,33\). Furthermore, the order \(r_{p'}\)
divides \(4np\) and does not divide \(4n\). It is divisible by \(4p\),
so \(p'\equiv\pm1\pmod{4p}\).

For the coefficient start at \(n=2,\ p=3\mid P_4\) and replace the
trace quotient with \(P_{2np}/(pP_{2n})\). The same lifting argument,
including \(v_2(P_{2np})=v_2(P_{2n})\), gives a positive odd quotient
coprime to \(P_{2n}\). It exceeds one by
\(\sinh(2nph)>p\sinh(2nh)\). Since \(2^2\mid P_4\), induction
proves \(n^2\mid P_{2n}\).

More generally one may prescribe in advance a sequence of choices between
the two coordinates. Start at \(n=2,\ u=2,\ v=1\), with a fresh prime
\(3\mid P_4\) and another \(17\mid b_4\). Use a fresh prime from the
chosen coordinate to multiply \(n\) and the corresponding one of \(u,v\).
The quotient construction supplies a fresh prime on that side, while
the unused prime divides the same coordinate at its odd multiple. The
two coordinates are coprime at every stage by the Pell equation. By
induction \(uv=n\), \(u^2\mid P_{2n}\), \(v^2\mid b_{2n}\), and both
chosen factors remain squarefree. In particular \(n^2\mid P_{2n}b_{2n}\)
along every such schedule. Since \(\log C_n=4nh+O(1)\), these forced
squares have quadratic size in \(\log C_n\).

For each odd squarefree trace index \(s\) constructed above one may assign
arbitrary integer exponents \(e_p\ge1\) to the primes of \(s\). If
\(N=\prod_{p\mid s}p^{e_p}\), then
\[
    N\operatorname{rad}(N)=\prod_{p\mid s}p^{e_p+1}\mid b_{2N}.
\]
Indeed \(N/s\) is odd, and at each \(p\mid s\) the original valuation
of at least two increases by \(e_p-1\). The same statement holds in
\(P_{2N}\) for each squarefree coefficient index \(s\) constructed above.
At two it follows from \(v_2(P_{2N})=e_2+1\), and at odd primes from
ordinary lifting. Consequently, for each integer \(t\ge2\), setting
\(N=s^{t-1}\) forces the exact \(t\)-th power \(s^t=N^{t/(t-1)}\)
as a divisor of the chosen coordinate at infinitely many indices \(N\).
This exponent is the largest possible when using only the guaranteed
multiplicities \(e+1\) of primes with \(p^e\Vert N\). For every \(e\ge1\),
\[
 t\left\lfloor\frac{e+1}{t}\right\rfloor\le \frac{t}{t-1}e,
\]
with equality at \(e=t-1\). For \(e<t-1\) the left side is zero, and
for \(e\ge t-1\) one has \(e+1\le te/(t-1)\). Additional multiplicities
at first occurrence would supply separate gains.
