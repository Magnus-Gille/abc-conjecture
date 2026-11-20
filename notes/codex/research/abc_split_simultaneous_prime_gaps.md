# Simultaneous gaps in the two elliptic denominator factors at split prime indices

On \(E:y^2=x^3+16x^2+32x\), take \(R=(-8,16)\) and let \(B_q^2\) be the reduced denominator of \(x([q]R)\). For a prime \(q>3\) split in \(K=\mathbb Q(\sqrt{-2})\), write \(B_q=M_q C_q\). The coprime factor \(M_q\) contains the primes where the annihilator of \(R\) under complex multiplication has norm \(q\). Those of \(C_q\) have annihilator \((q)\), of norm \(q^2\). Valuations in these factors are the original valuations in \(B_q\).

There is an infinite sequence of split primes \(q\equiv11\bmod24,\ q\equiv-1\bmod7\) along which
\[
 \min\left\{\frac{P^-(M_q)}{q\log q},\
             \frac{P^-(C_q)}{q^2\log q}\right\}\longrightarrow\infty ,
\]
where \(P^-\) denotes the least prime factor. Both integers have a prime of odd exponent along this sequence. The proper factor \(M_q\) in fact has two distinct odd-exponent primes for all sufficiently large split indices, by a covering argument. The result controls where prime factors can occur. Their total contribution without multiplicities remains undetermined. [CM factorization](abc_odd_rank_quartic_cutoff.md) · [Congruences giving odd exponents](abc_odd_rank_split_packet_characters.md) · [Covering argument](abc_odd_rank_primitive_cm_norm.md)

## Two simultaneous norm conditions

There is a simpler conclusion on a whole rational progression. For every sufficiently large prime \(q\equiv11\bmod24\), \(M_q\) supplies two distinct primes of odd exponent, each exceeding \(q\). Also \(C_q\equiv3\bmod7\), a quadratic nonresidue. Thus a third odd-exponent prime belongs to \(C_q\), and is at least \(2q^2+1\) by the Frobenius norm form. For example at \(q=59=3^2+2\cdot5^2\), one has \(M_{59}=524939\cdot1436441\), and \(1637428889\mid C_{59}\). Trial division confirms primality of all three. Exact rational multiplication gives \(B_{59}\bmod p=0\) and \((B_{59}/p)\bmod p=152299,\ 754422,\ 1544704660\) respectively. Thus all three exponents are one in this example. [Exact formula modulo seven](abc_split_packet_cubic.md) · [Large-prime certificate](abc_odd_rank_simple_large.md)

Put \(\mathcal O=\mathbb Z[\sqrt{-2}]\) and write \(q=\gamma\bar\gamma\). Every rational prime of \(M_q\) has the form \(N(1+\gamma\alpha)\) for a nonzero \(\alpha\in\mathcal O\): conjugate the Frobenius and the ideal together if its annihilator is \((\bar\gamma)\). Every prime of \(C_q\) has the form \(N(1+q\alpha)\). These statements follow since Frobenius fixes \(R\) and its norm is the rational prime. We construct \(\gamma\) making every value of both forms composite when \(0<N\alpha\le A\), including the real shifts.

Fix \(F\ge4\). We choose \(w=w(F)\) before sending \(A\) to infinity, and put \(Y=2A/F\). Fix \(\gamma\equiv3+\sqrt{-2}\bmod24\mathcal O\) and \(\gamma\equiv2+\sqrt{-2}\bmod7\mathcal O\). These are unit residue classes of norms \(11\bmod24\) and \(6\bmod7\). Omit \(2,3,7\) from the following prime moduli.

* For split \(p\le w\) put \(\gamma\equiv(2,-1/2)\) in \(\mathcal O/(p)\simeq\mathbb F_p\times\mathbb F_p\), choosing either ordering of the factors. Both entries are units different from 1, and \(N\gamma\equiv-1\bmod p\).
* For split \(w<p\le Y\) and inert \(p\le2\sqrt A\), put \(\gamma\equiv1\bmod p\mathcal O\). Then \(N\gamma\equiv1\bmod p\) as well.

First count the \(\alpha\) for which a given norm condition still needs a divisor. Set aside all \(O(\sqrt A)\) real \(\alpha\). For nonreal \(\alpha\) the integer \(n=N(1+\alpha)\) is between 2 and \(2A\). If it has a split divisor in \((w,Y]\), that divisor works for both conditions. An inert prime factor of \(n\) has square dividing \(n\), hence is at most \(\sqrt{2A}\) and already works unless it belongs to the fixed exceptions. Taking \(w>7\), the survivors therefore have either \(w\)-smooth \(n\), or \(n=mP\) with \(m<F\) and \(P>Y\) a split rational prime of exponent one. There are only \((\log A)^{O_w(1)}\) elements with \(w\)-smooth \(n\), by factorization into finitely many prime ideals and the two choices of unit.

Write \(1+\alpha=\eta\lambda\) in the latter case, \(N\eta=m,\ N\lambda=P\). The ring is a PID, and only finitely many \(\eta\) occur at fixed \(F\). At a split \(p\le w\) away from \(2,3,7,m\), a component \(t\) of the multiplier is nonzero and different from 1. It is \(2\) or \(-1/2\) for the \(\gamma\) condition, and is \(-1\) for both components of the \(q=N\gamma\) condition. To survive in both components of this prime, the unit \(\lambda\) must avoid \((1-t^{-1})/\eta\) in each. Thus the allowed fraction of unit residues is \((1-1/(p-1))^2\) for each condition separately.

For fixed \(w\), prime generators \(\lambda\) of norm at most \(X\), counted with both signs, are equidistributed in the units of the residue ring modulo the product of these \(p\). This is the prime ideal theorem in the finitely many fixed ray classes, since the ordinary class number is one and the signs fill each unit orbit. Their total is \((2+o_w(1))X/\log X\). With \(X=2A/m\) the limsup of the number of survivors at one condition divided by \(A/\log A\) is bounded by
\[
 4\sum_{0<N\eta<F}\frac1{N\eta}
 \prod_{\substack{p\le w\ {\rm split}\\p\nmid42N\eta}}
                 (1-1/(p-1))^2.
\]
For each of the finitely many \(\eta\) the product tends to zero with \(w\). Choose \(w\) so the sum is less than \(1/(4F)\). The union of the survivors at the two conditions, together with all the real shifts, then has size at most \(A/(F\log A)\) for all sufficiently large \(A\). This argument allows the threshold for \(A\) to depend on \(F\). [Single-condition counting argument](abc_odd_rank_quadratic_large_gaps.md)

Give each remaining \(\alpha\) its own split prime \(p\) in \([3A,6A]\). There are enough by the prime number theorem in progressions. Write \(\alpha=(\alpha_+,\alpha_-)\bmod p\); both coordinates are nonzero since \(0<N\alpha\le A<p\). Impose \(\gamma=(-1/\alpha_+,1)\bmod p\). This kills the first component of \(1+\gamma\alpha\), and also of \(1+(N\gamma)\alpha\). All prescriptions are units, so CRT gives a unit residue \(x\bmod M\mathcal O\) for a rational integer \(M\). The split primes in \((w,Y]\) cost \((1+o_F(1))A/F\) in \(\log M\), the assigned primes cost at most \(A\log(6A)/(F\log A)\), the inert primes cost \(O(\sqrt A)\), and the remaining fixed moduli cost \(O_F(1)\). Thus \(\log M\le3A/F\) eventually for each \(F\).

## Taking a prime generator

Use the least-prime-ideal bound in a ray class of a fixed number field: a prime ideal coprime to the modulus in the class can be taken with norm bounded by a fixed power of the norm of the modulus (up to a field-dependent constant). This is the number-field Linnik theorem. [Weiss, *The least prime ideal*](https://doi.org/10.1515/crll.1983.338.56) · [Thorner and Zaman, *An explicit bound for the least prime ideal in the Chebotarev density theorem*](https://doi.org/10.2140/ant.2017.11.1135)

Apply the bound to the ray class of \((x)\). A generator \(\gamma\) of the prime ideal may be chosen congruent to \(x\bmod M\mathcal O\), by the definition of ray equivalence. Its norm is \(6\bmod7\), a nonsquare; hence it cannot be an inert rational prime ideal of degree two. Ramified primes have been excluded by the modulus, so \(q=N\gamma\) is an ordinary split prime. There is an absolute \(C_0\) with \(\log q\le C_0 A/F\) since \(N(M\mathcal O)=M^2\). Also \(q\equiv1\) modulo the product of the split primes in \((w,Y]\), so \(\log q\ge A/(2F)\) eventually and both covered norms exceed \(6A\) at every nonzero \(\alpha\). Every assigned divisor is proper.

For every prime in \(M_q\) we now have \(N\alpha>A\), so \(p\ge(\sqrt{qA}-1)^2\); for those in \(C_q\) we have \(p\ge(q\sqrt A-1)^2\). Their respective normalized lower bounds are at least \(F/(2C_0)\) for sufficiently large \(A\). Taking \(F\to\infty\) and choosing \(A\) sufficiently large at each stage proves the theorem.

## Quantitative gaps

Write \(\log_j\) for the \(j\)-fold iterated natural logarithm. The construction gives an infinite sequence where both ratios in the theorem are
\[
 \gg \frac{\log_2 q\,\log_4 q}{(\log_3 q)^2}.
\]
This uses a sieve in place of prime-generator equidistribution at the auxiliary parameter \(w\). Put \(H=\log A,\ H_2=\log H,\ H_3=\log H_2\), and take
\[
 u=K_0H_2/H_3,\quad w=\exp(H/u),\quad
 F=c\, H H_3/H_2^2,\quad Y=2A/F .
\]
Here \(K_0\) is a sufficiently large absolute constant and \(c>0\) is sufficiently small after \(K_0\) is fixed. Then \(w=o(A/F)\). Chebyshev's upper bound controls the cost of the small split-prime block by \(O(w)\); all the bounds on \(\log M,\log q\) above remain uniform for this choice.

The count of elements \(1+\alpha\) with \(w\)-smooth norm up to \(2A\) is \(O(A/H^5)\). To check this, sum over their principal ideals, with two signs per ideal. Rankin's bound at \(s=1-\delta,\ \delta=(\log u)/(2\log w)\) gives an upper bound \(2(2A)^s\) times the Euler product of \((1-(N\mathfrak l)^{-s})^{-1}\) over prime ideals above rational primes \(\le w\). Its logarithm is \(O(H_2+\sqrt u)\): inert terms and higher powers are bounded since \(s\to1\), while at split primes the extra sum \(\sum_{p\le w}(p^\delta-1)/p\) is \(O(1+\sqrt u)\). For the latter, use partial summation with the Chebyshev bound or dyadic intervals to majorize by a constant times \(1+\int_0^{\delta\log(2w)}(e^v-1)\,dv/v\). The initial sum \(\sum_{p\le w}1/p\) is \(O(\log\log w)\). Now \(\delta\log A=u\log u/2=(K_0/2+o(1))H_2\). This proves the claimed smooth count once \(K_0\) is fixed large enough.

For the remaining survivors \(1+\alpha=\eta\lambda\), \(N\eta=m<F,\ N\lambda=P>Y\). Bound the number of \(\lambda\) in the disk \(N\lambda\le X=2A/m\) by a lattice sieve. At all split primes \(5\le p\le z=A^{c_0}\) require both coordinates of \(\lambda\bmod p\) to be nonzero, since \(P>Y>z\). At split \(p\le w\) with \(p\nmid42m\), also forbid the one nonzero residue in each coordinate from the relevant screen. Take \(A\) large enough that \(w<z\). The density retained is therefore \((1-1/p)^2\) or \((1-2/p)^2\), respectively. By Mertens' theorem for the two split classes modulo eight, its product up to \(z\) is
\[
 \ll \frac{g(m)}{\log z\,\log w},\qquad
 g(m)=\prod_{p\mid m}(1-1/p)^{-2}.
\]
Indeed \((1-2/p)^2\le (1-1/p)^4\), and removing the additional screen at each divisor of \(m\) costs at most the factor in \(g(m)\) against this upper bound. The finitely many fixed primes cost an absolute constant.

Here are uniform error bounds for the upper sieve. Let \(\rho(p)\) be the fraction of forbidden classes at \(p\), so \(\rho(p)\le4/p\). At squarefree \(d\) the number of forbidden CRT classes is at most \(4^{\omega(d)}d\). A single class in the disk contributes its area main term with error \(O(\sqrt X/d+1)\) by the elementary lattice-point bound for a translated ellipse. Thus the remainder is \(O(4^{\omega(d)}(\sqrt X+d))\). Use Selberg weights supported on divisors at most \(D=A^{1/100}\), of magnitude at most one. The standard Selberg denominator is the sum for \(d\le D,\ d\mid\prod_{p\le z}p\) with multiplicative weights \(\prod_{p\mid d}\rho(p)/(1-\rho(p))\). Its unrestricted sum is the reciprocal retained product. Under the normalized unrestricted weights, the events \(p\mid d\) are independent with probabilities \(\rho(p)\), so \(\mathbb E\log d\ll\log z\) uniformly. Choose \(c_0>0\) sufficiently small; Markov puts at least half the weight below \(D\). The sum of the remainder terms over pairs of sieve divisors up to \(D\) is \(O(D^{2+o(1)}(\sqrt A+D^2))=O(A^{0.54})\) for all sufficiently large \(A\). The upper bound per \(\eta\) is consequently
\[
 \ll \frac{A g(m)}{m\log A\,\log w}+O(A^{0.54}).
\]

One has \(\sum_{0<N\eta\le F}g(N\eta)/(N\eta)\ll\log(2F)\). To see this expand \(g(n)=\sum_{d\mid n}h(d)\) with squarefree support and \(h(p)=(1-1/p)^{-2}-1=O(1/p)\). Whenever \(d\mid N\eta\), the element \(\eta\) belongs to at least one of \(2^{\omega(d)}\) ideals of norm at least \(d\) obtained by choosing a prime ideal over each \(p\mid d\). In this principal ring, an ideal of norm \(j\) contains \(O(T/j)\) nonzero elements of norm at most \(T\) for \(j\le T\), and none otherwise. Therefore \(\sum_{0<N\eta\le T}g(N\eta)\ll T\sum_d2^{\omega(d)}h(d)/d\ll T\). Partial summation gives the assertion.

Summing the sieve now bounds survivors at each screen by \(O(Au\log(2F)/H^2)+O(F A^{0.54})\). The smooth and real shifts add \(O(A/H^5+\sqrt A)\). With \(c\) sufficiently small these estimates for both screens total at most \(A/(F H)\), as required by the large-prime assignment. The resulting \(\log q\asymp A/F\) gives \(\log_2 q\sim H,\ \log_3 q\sim H_2,\ \log_4 q\sim H_3\), proving the quantitative assertion.

In particular, write \(\operatorname{sf}(n)=\prod_{v_p(n)\ {\rm odd}}p\). Take the two odd-exponent primes in \(M_q\) from the covering theorem and one in \(C_q\) from the congruence certificate. They are distinct. On this sequence,
\[
 \operatorname{sf}(B_q)\gg q^4(\log q)^3
       \left(\frac{\log_2 q\,\log_4 q}{(\log_3 q)^2}\right)^3.
\]
The power \(q^4\) here bounds a product of primes. The full logarithmic size \(\log B_q\) is asymptotic to \(\widehat h(R)q^2\).

## Density among all split prime indices

Fix any \(L(x)>0\) with \(L(x)=o(\log x)\). Except on a relative density-zero set of split primes \(q\), **both**
\[
 P^-(M_q)>q L(q),\qquad P^-(C_q)>q^2 L(q).
\]
For the full factor this is the prime-index sieve in the [quadratic prime-size bound](abc_odd_rank_quadratic_prime_barrier.md), applied to the exact annihilator \((q)\): at a small full prime one must have \(p=(1+aq)^2+2b^2q^2\), with \(b\ne0\). In \(T\le q\le2T\) that sieve gives \(O(BT/(\log T)^2)\) exceptional prime indices when \(B=O(1+\sup_{T\le x\le2T}L(x))=o(\log T)\) bounds \(a^2+2b^2\) up to an absolute factor. Its density-zero conclusion relative to all primes also holds relative to the split primes, of natural prime density one half.

For the proper factor, a small \(p\) requires \(p=N(1+\gamma\alpha)\), where \(q=N\gamma\in[T,2T]\) is itself prime and \(0<N\alpha\ll B\). Fix \(\alpha\). Sieve the lattice disk \(N\gamma\le2T\) by split primes up to \(z=T^{c_0}\), with \(c_0\) sufficiently small. At \(s\nmid N\alpha\) forbid each component of \(\gamma\) to be zero or \(-1/\alpha\) in that component; at every other split prime only forbid zero. Both prime norms exceed \(z\): \(p\ge(\sqrt q-1)^2\) since \(\alpha\ne0\). This is the disk sieve just proved with both cutoffs equal to \(z\) and omission multiplier \(g(N\alpha)\). It gives \(O(Tg(N\alpha)/(\log T)^2+T^{0.54})\) values of \(\gamma\). The mean bound for \(g(N\alpha)\) over the coefficient disk gives \(O(BT/(\log T)^2+BT^{0.54})=o(T/\log T)\) generating pairs. This proves the second density estimate required. Nontriviality of both factors at all sufficiently large split primes follows for \(M_q\) from the covering argument and for \(C_q\) from its positive logarithmic mass.

At all sufficiently large split primes, at least two different odd-valuation primes come from \(M_q\). On a set of split primes of relative density greater than \(0.9999999747549\), a third comes from \(C_q\). Intersecting the latter certified set with the preceding density-one set shows
\[
 \operatorname{sf}(B_q)>q^4 L(q)^3
\]
on a set of split prime indices of relative density greater than \(0.9999999747549\). One can also restrict to \(q\equiv 11\bmod24\), on which the third prime is guaranteed at every index, leaving relative density one *within this progression*. In particular \(L(q)=\log q/\log\log q\) is allowed. [Complementary nonpower test](abc_split_packet_cubic.md)

## Simultaneously excluding any fixed set of power exponents

For a fixed finite set of prime exponents, the [division-polynomial ray condition](abc_split_packet_cubic.md) gives a fixed unit residue for \(\gamma\) in which no listed exponent divides every valuation in \(C_q\). Its norm is \(11\bmod24\). The same conclusion holds in each of the two coprime pieces of \(M_q\) for all sufficiently large split primes by applying the covering argument at each listed exponent. The quantitative gap construction may be made inside this ray: include its modulus in the initial congruences in place of the conditions modulo 24 and 7, and omit its prime factors from all sieves. They change the estimates only by constants, and \(N\gamma\equiv 2\bmod3\) still rules out degree-two prime ideals. Constants in the gap bound can now depend on the list. Thus, along the resulting sequence, each exponent has two prime witnesses past the \(M_q\) cutoff and another past the \(C_q\) cutoff. A single witness need not serve all the exponents, and an exponent relatively prime to a fixed list need not be one.

## Consequence if the full factor is squareful infinitely often

Write \(h=\widehat h(R)\). The height calculations give \(\log B_q=hq^2+O(1)\) and \(\log M_q=2hq+O(\log q)\). If every prime of \(C_q\) occurs at least twice, then
\[
 \log(B_q/\operatorname{rad}B_q)\ge\tfrac12\log C_q
               \ge \tfrac12 hq^2-O(q).
\]
The [primitive-triple construction](abc_odd_rank_truncated_radical.md) has \(\log c=8 hq^2+O(q)\) and \(\log(c/\operatorname{rad}(abc))\ge\log(B_q/\operatorname{rad}B_q)-O(1)\). Infinitely many squareful \(C_q\) would therefore give triples with lower limiting quality at least \(16/15\). The prime-size and power-residue results leave this existence question open.

One can weaken the hypothesis quantitatively. Put \(S_q=\prod_{p\parallel C_q}p\), the product of primes occurring exactly once. Suppose that for some fixed \(0<\eta\le1\), infinitely many split prime indices have \(\log S_q\le(1-\eta)\log C_q\). The prime powers of exponent \(e\ge2\) then contribute at least \(\eta\log C_q\) in logarithmic size. Since \(e-1\ge e/2\), their contribution to \(\log(B_q/\operatorname{rad} B_q)\) is at least \((\eta/2)\log C_q\). As \(\log C_q=hq^2+O(q)\), the resulting primitive triples have
\[
 \liminf\frac{\log c}{\log\operatorname{rad}(abc)}\ \ge\ \frac{16}{16-\eta}.
\]
For example, a fixed ten percent of the logarithmic size in repeated prime powers along an infinite subsequence would guarantee limiting lower quality at least \(160/159\). Establishing any fixed positive proportion on an infinite subsequence would suffice here.
