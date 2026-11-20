# Simultaneous exclusion of small primes from the entire octic abc triple

There is an absolute \(\delta>0\) and an infinite sequence of positive primitive abc triples
\[
 a=(2st)^4,\qquad b=(s^4-4t^4)^2,\qquad c=(s^4+4t^4)^2=a+b
\]
with the following properties. The only primes dividing \(abc\) below \((\log c)^\delta\) are \(2,3,5,7,17\). All five divide \(a\), with respective valuations \(12,8,4,4,4\). The two quadratic forms \(Y=s^2+2t^2\) and \(V=(s-t)^2+t^2\) are squares; every prime dividing \(Y\) is at least a positive constant times \(\log c\). Here \(s\) may be signed. The sign has no effect on the triple itself. In particular \(\operatorname{rad}(abc)\ll c\) on this family, by factoring both squares. A fixed-power saving would require additional control of their exponents or of other factors.

## Sieving the index

Use the full two-square parametrization with odd index \(N\), elliptic point \(Q=[(N+1)/2]A\), and reduction order \(r_p\) defined there. Recall that \(\log c\asymp N^2\). [Full group, slope, and local identities](abc_octic_full_mixed_orbit.md)

There is an absolute \(\gamma>0\) such that, in every sufficiently large dyadic interval \([X,2X]\), there are \(\gg X/(\log X)^5\) primes \(N\equiv29\pmod{72}\) for which
\[
 q\nmid (N-1)(N+1)(N^2+2)\qquad (5\le q\le z=X^\gamma,\ q\text{ prime}).
\]
Here are the distribution estimates needed to apply the fundamental lemma of the sieve. For \(q\ge5\) let \(\rho(q)\) be the number of roots of the displayed polynomial modulo \(q\). Its roots are all nonzero and \(\rho(q)\le4\); \(\rho(5)=2\). Extend \(\rho\) multiplicatively to squarefree \(d\) coprime to 6. The local sieve density among primes is \(g(q)=\rho(q)/(q-1)<1\). Mertens' formula gives the upper sieve-dimension bound four, namely \(\prod_{w\le q<z}(1-g(q))^{-1}\ll (\log z/\log w)^4\) for \(5\le w\le z\), with the usual \(1+O(1/\log w)\) multiplicative error relative to this upper bound. In particular \(\prod_{5\le q\le z}(1-g(q))\gg(\log z)^{-4}\).

For such \(d\le X^{1/3}\), the primes in the progression for which the polynomial vanishes modulo \(d\) form \(\rho(d)\) reduced classes modulo \(72d\). Write \(E(72d)\) for the maximum absolute error in a reduced class for the prime count on \([X,2X]\) against the logarithmic-integral main term. The remainder is at most \(4^{\omega(d)}E(72d)\). Bombieri–Vinogradov gives \(\sum_{d\le X^{1/3}}E(72d)\ll_B X/(\log X)^B\) for every fixed \(B\). Also \(E(72d)\ll X/d\) in this range. By Cauchy–Schwarz and \(\sum_{d\le X^{1/3}}16^{\omega(d)}/d\ll(\log X)^{16}\) over the squarefree moduli, the sum of the weighted errors is \(O_B(X/(\log X)^B)\) as well, on taking a larger exponent in Bombieri–Vinogradov. The dimension-four lower-bound fundamental lemma with level \(X^{1/3}\) now gives the stated count for any sufficiently small fixed \(\gamma>0\). Its sieve parameter \(\log(X^{1/3})/\log z=1/(3\gamma)\) can be fixed arbitrarily large. [Iwaniec and Kowalski, *Analytic Number Theory*, sieve methods and Bombieri–Vinogradov](https://bookstore.ams.org/coll-53)

## From a sieved index to the exact small-prime part

Take one of these primes \(N\). For odd \(p\), the order \(r_p\) exceeds two because \(A=(1,1)\) is integral and its ordinate is nonzero in odd characteristic. Hasse's bound gives \(r_p\le(\sqrt p+1)^2\). In particular \(p\le z/4\) implies \(r_p\le z\) for large \(X\).

* For \(p\mid YV\), the order divides \(N\), so \(r_p=N\). For \(p\mid D=s^2-2t^2\), it divides \(2N\) and exceeds two. Neither case is possible at \(p\le z/4\).
* For \(p\mid U=(s+t)^2+t^2\), the order divides \(N^2+2\). This odd integer has 3-adic valuation one because \(N\equiv2\bmod9\). Its other prime factors exceed \(z\), leaving only \(r_p=3\) for \(p\le z/4\). The denominator of \(u([3]A)=289/2025\) shows that only 3 and 5 have order three. At both primes \((N+1)/2\) is divisible by three, hence \(Q\) reduces to infinity on \(E\), where its slope has a pole. Thus \(p\mid t\) and \(U\equiv s^2\ne0\bmod p\).
* For \(p\mid st\), one has \(r_p\mid N-1\) or \(r_p\mid N+1\). The parts of \(N-1,N+1\) supported on \(2,3\) are exactly 4 and 6, respectively, by the class modulo 72. Thus \(r_p\mid4\) or \(r_p\mid6\) if \(p\le z/4\). In either case \((N+1)/2\equiv3\pmod{r_p}\), and \(Q\) reduces to \([3]A\) at \(p\). That point has signed slope \(-119/180\). The only possible odd small primes are consequently \(3,5,7,17\), and they do all occur. Indeed \(r_p=3\) at 3 and 5, \(r_7=4\), and \(r_{17}=6\), by direct reduction of \([2]A,[3]A\).

For exact valuations, at any odd \(p\mid st\) the identity
\[
 D^2-YV=2st(s^2-4st+2t^2)
\]
gives \(v_p(st)=v_p(u([N]A)-1)\). The abscissa minus one is a parameter at either of \(\pm A\) modulo \(p\), since their ordinates are \(\pm1\). At \(p=7\) one has \([N]A=A\bmod p\); its distance from \(A\) is the formal depth of \([N-1]A\). At \(p=3,5,17\) the depth is that of \([N+1]A\). Compare to index 5, which gives the slope \(-119/180\). The respective depth increments are \(v_p((N-1)/4)\) and \(v_p((N+1)/6)\) by the formal group law at an odd good prime. They vanish by the sieve and the congruence modulo 9. Thus the odd valuations of \(st\) at \(3,5,7,17\) are \(2,1,1,1\). At 2 the parity formula gives \(v_2(t)=2\), since \(N\equiv5\bmod8\). None of these five primes divides the other two entries, by primitivity. This proves the exact valuations in the statement.

Finally every \(p\mid Y\) splits in \(\mathbf Q(\sqrt{-2})\), while \(N\equiv5\bmod8\) is inert. The CM multiples of the point of order \(N\) give all of \(E[N]\) over \(\mathbf F_p\). The norm equation for Frobenius gives \(p\ge2N^2+1\). Here there are no inherited seed primes in \(Y\), since the reduction order of the generator is exactly \(N\) at every one of its prime divisors. Taking any fixed \(0<\delta<\gamma/2\) makes \((\log c)^\delta<z/4\) at sufficiently large \(X\). [CM norm equation](abc_octic_mixed_seed_prime_orbit.md)

## One explicit index

Take \(N=100000000000001166797\). This integer is \(29\bmod72\). The following integers are prime, as checked with PARI's unconditional `isprime` on each of the four integers.

| Expression | Value |
|---|---:|
| \(N\) | 100000000000001166797 |
| \((N-1)/4\) | 25000000000000291699 |
| \((N+1)/6\) | 16666666666666861133 |
| \((N^2+2)/3\) | 3333333333333411119800000000453805079737 |

Thus a reduction order outside the small cases in the proof is at least \(16666666666666861133\). Hasse's inequality gives that every prime of this primitive abc triple below \((4082482904-1)^2=16666666653287307409\) belongs to the five listed primes, with the stated exact valuations. The index and elliptic group law specify the triple without writing out its coordinates.
