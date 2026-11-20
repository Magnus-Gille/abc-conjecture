# Large least prime divisors at inert prime ranks

Let \(E':y^2=x^3+16x^2+32x\), \(R=(-8,16)\), and let \(B_r\) be the positive square root of the abscissa denominator of \([r]R\). Let \(K=\mathbb Q(\tau)\), \(\tau^2=-2\), and \(\mathcal O=\mathbb Z[\tau]\). For a sufficiently large odd integer \(r\), denote by \(P_{(r)}\) the least rational prime at which the reduction of \(R\) has exact CM annihilator \((r)\) at a place of \(K\). Write \(P^-(m)\) for the least prime divisor of an integer \(m>1\). All logarithms are natural.

**Theorem.** Even among prime indices \(r\equiv5\pmod8\),
\[
        \limsup_{r\to\infty}\frac{P^-(B_r)}{r^2\log r}=\infty.
\]
At these indices \(P^-(B_r)=P_{(r)}\). There also exist odd composite indices with \(P_{(r)}/(r^2\log r)\to\infty\) for which the primes of exact annihilator \((r)\) carry \((1-o(1))\log B_r\), counting multiplicity. In particular, for every fixed \(C>0\), the fraction of the full logarithmic mass of \(B_r\) above \(C r^2\log r\) tends to one along the composite sequence, and equals one eventually along the prime sequence.

## From prime divisors to norms

All odd scalar denominator primes split in \(K\). At a place above \(p\mid B_r\), the annihilator \(I\) of \(R\) divides \((r)\), and the Frobenius is a CM multiplier \(\pi\in\mathcal O\) with \(\operatorname N\pi=p\) and \(\pi\equiv1\pmod I\). There is no dyadic denominator prime at an odd index. The exact-ideal formula ensures occurrence of \((r)\) for every sufficiently large odd \(r\). Thus a prime of this exact annihilator is of the form
\[
 p=\operatorname N(1+r\alpha)=(1+ra)^2+2r^2b^2,
 \qquad \alpha=a+b\tau,\quad a\in\mathbb Z,\quad b\ge1.
\]
Conjugation permits \(b\ge0\), and \(b=0\) would give an integer square. These facts also hold when the two places above \(p\) are interchanged. [CM and exact denominator formula](abc_octic_mixed_cm_prime_mass.md)

## Covering a disk in the norm lattice

Fix \(F\ge4\). A second parameter \(w=w(F)\) will be fixed before the real parameter \(A\) tends to infinity. We will construct a reduced residue class of integers \(r\) for which every \(\alpha=a+b\tau\) with \(b\ge1\) and \(\operatorname N\alpha\le A\) has \(\operatorname N(1+r\alpha)\) divisible by a prime at most \(6A\). Put \(Y=2A/F\). Choose the following compatible conditions, for \(A\) large enough that \(Y>w\).

* Take \(r\equiv5\pmod8\).
* At odd split rational primes \(q\le w\), take \(r\equiv-1\pmod q\).
* At split primes \(w<q\le Y\), and at odd inert primes \(q\le 2\sqrt A\), take \(r\equiv1\pmod q\).

Call \(\alpha\) a survivor if these conditions have supplied no divisor. Since \(b\ge1\), its integer \(n_+=\operatorname N(1+\alpha)\) is at least two and at most \((\sqrt A+1)^2\le2A\). The prime 2 cannot divide \(n_+\) for a survivor, since \(r\) is odd. An inert prime divisor of \(n_+\) has even exponent, hence would be at most \(\sqrt{2A}\) and was covered. Split prime divisors of \(n_+\) in \((w,Y]\) were covered as well. A survivor therefore has either a \(w\)-smooth value \(n_+\) or a factorization
\[
        n_+=mP,\qquad m<F,\qquad P>Y\text{ a split rational prime}.
\]
There can be only one prime factor above \(Y\), with exponent one, once \(Y^2>2A\).

For fixed \(w\), the number of possible \(1+\alpha\) with \(w\)-smooth norm \(\le2A\) is \((\log A)^{O_w(1)}\). Indeed its principal ideal factors over finitely many prime ideals, each exponent is \(O(\log A)\), and each ideal has two generators.

In the other case \(1+\alpha=\gamma\lambda\) with \(\operatorname N\gamma=m<F\) and \(\operatorname N\lambda=P\). One gets this factorization by dividing by a generator of the prime ideal over \(P\) that divides \(1+\alpha\). The ring \(\mathcal O\) is a PID. There are only finitely many \(\gamma\) for fixed \(F\). At every odd split \(q\le w\) with \(q\nmid m\), survival requires \(q\nmid\operatorname N(2-\gamma\lambda)\), since \(1-\alpha=2-\gamma\lambda\). Modulo each of the two prime ideals above \(q\), the unit \(\lambda\) must avoid the single nonzero residue \(2/\gamma\). The fraction of allowed units modulo \((q)\) is precisely \((1-1/(q-1))^2\).

Here the prime ideal theorem in ray classes is used only for a **fixed modulus**. For fixed \(w,\gamma\), let \(Q\) be the product of the split \(q\le w\) under consideration. Prime generators \(\lambda\), counted with both signs and norm at most \(X\), are equidistributed in \((\mathcal O/Q\mathcal O)^\times\). Indeed the ray class group in this class-number-one imaginary quadratic field is the unit residue group modulo the image of \(\{\pm1\}\). The two signed generators fill their two residues when these differ, and count twice when they coincide. The prime ideal theorem in each ray class supplies the desired equidistribution with total \((2+o_Q(1))X/\log X\). Prime ideals of residue degree two contribute \(O(\sqrt X)\). This is also the abelian Chebotarev theorem in the ray class field. No angular restriction is used.

Taking \(X=2A/m\) and summing over the finite list of \(\gamma\), the limsup of the number of nonsmooth survivors divided by \(A/\log A\) is at most
\[
 4\sum_{\substack{0<\operatorname N\gamma<F}}\frac1{\operatorname N\gamma}
 \prod_{\substack{q\le w\ \mathrm{split}\\q\nmid2\operatorname N\gamma}}
                  \left(1-\frac1{q-1}\right)^2 .
\]
Overcounting the factorizations can only increase this bound. For every fixed \(\gamma\) the product tends to zero, since the reciprocal sum over the two split prime classes \(1,3\bmod8\) diverges. Choose \(w=w(F)\) to make the displayed finite sum including its factor 4 smaller than \(1/(2F)\). For all sufficiently large \(A\), the number of all survivors, including the smooth ones, is then at most \(A/(F\log A)\).

Assign each survivor its own split prime \(q\in[3A,6A]\). The prime number theorem in the two split classes supplies \((3/2+o(1))A/\log A\) such primes. For \(A\) large these new moduli are distinct from the preceding ones. Choose a square root \(t\) of \(-2\) modulo \(q\) and impose \(r\equiv-(a+bt)^{-1}\pmod q\). The inverse exists, since \(q>\operatorname N\alpha>0\). This is a nonzero class and kills one factor of \(\operatorname N(1+r\alpha)\pmod q\). This completes the cover.

## Size of the index and the least prime

Let \(M\) be the complete modulus, including the factor 8. The CRT class is prime to \(M\). For each fixed \(F\) and all sufficiently large \(A\),
\[
       \frac{A}{2F}\le\log M\le\frac{3A}{F}.
\]
In fact the logarithm of the product of the split primes in \((w,Y]\) is \((1+o_F(1))A/F\). The inert block costs \(O(\sqrt A)\), the fixed factors cost \(O_F(1)\), and the new primes cost at most \((A/(F\log A))\log(6A)\). The numerical constants in the displayed inequality are absolute. Only the threshold for \(A\) depends on \(F\).

For an elementary choice of composite index, let \(x\in[1,M]\) be the CRT representative and take \(r=(x+M)(1+M)\). Then \(r\equiv x\pmod M\) and \(\log r\le2\log M+O(1)\). For a prime index take the least positive prime in the reduced CRT class. Linnik's theorem gives \(r\ll M^{L}\) with absolute constants. Every such prime satisfies \(r\equiv1\) modulo the product of all split primes in \((w,Y]\), so \(r>1\) implies \(\log r\ge A/(2F)\) for all sufficiently large \(A\). Both choices therefore satisfy
\[
       A/(2F)\le\log r\le C_0 A/F
\]
with an absolute \(C_0\), independent of \(F\). Since \(b\ge1\), every covered value is at least \(2r^2>6A\). Its divisor from the cover is consequently proper. Every prime norm of the displayed form must have \(\operatorname N\alpha>A\), hence
\[
 p=|1+r\alpha|^2\ge(r|\alpha|-1)^2>(r\sqrt A-1)^2\ge\tfrac12 A r^2.
\]
In particular \(P_{(r)}/(r^2\log r)\ge F/(2C_0)\). Taking \(F\to\infty\), with \(A\) sufficiently large at each stage, proves the unbounded normalized gaps. The construction asserts no specified rate for this divergence.

## Full denominator mass

Set \(h=\widehat h(R)>0\) and \(g(r)=\prod_{\mathfrak l\mid(r)}(1-1/\operatorname N\mathfrak l)\). The available scalar exact-ideal formula gives
\[
 \sum_{\substack{p\mid B_r\\ I_p=(r)}}v_p(B_r)\log p
   =h r^2 g(r)+O(r^{o(1)}),\qquad \log B_r=h r^2+O(1).
\]
Each split rational prime contributes twice in the place-counted formula and once here. [Exact mass, including its normalization](abc_odd_rank_quartic_logarithm.md)

All split primes dividing our \(r\) exceed \(Y=2A/F\), as every prescribed class for smaller split primes is a unit. There are at most \(\log r/\log Y\) such divisors. All inert prime divisors exceed \(2\sqrt A\), and 2 does not divide \(r\). Consequently
\[
  0\le1-g(r)\le \frac{2\log r}{Y\log Y}
           +\sum_{j>2\sqrt A}j^{-2}
       \ll\frac1{\log Y}+\frac1{\sqrt A}.
\]
The last constant is absolute since \(\log r\le C_0 A/F\). Choosing the diagonal sequence so \(A/F\to\infty\) proves the asserted full-mass fraction.

Finally every prime index constructed here is \(5\bmod8\), hence inert in \(K\). Its ideal \((r)\) is prime. The only proper divisor ideal is \(\mathcal O\), and the reduction of \(R=(-8,16)\) at an odd good prime is an affine point, so its annihilator cannot be \(\mathcal O\). Thus **every** rational prime dividing \(B_r\) belongs to this one exact ideal. The height formula ensures \(B_r>1\) for all sufficiently large \(r\), completing the prime-index statement.
