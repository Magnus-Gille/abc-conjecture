# Repeated primes in a short interval for rational abc triples

For different coprime positive integers \(U,V\), put \(C=\max(U,V)\), \(D=|U-V|\), and \(G=C/(\operatorname{rad}(UV)D)\). The actual ratio of height to radical of the primitive triple is exactly
\[
 \frac C{\operatorname{rad}(UVD)}=G\frac D{\operatorname{rad}(D)} .
\]
Thus \(G\) measures how much gain remains when every prime in the difference is counted with full multiplicity.

For a finite example, take \(U=(13^{29}19^{19})^2\) and \(V=(17^{46})^2\). Direct integer exponentiation gives \(U>V\), 114 decimal digits in \(U\), and
\[
 2048(13\cdot17\cdot19)(U-V)<1000U<
 2049(13\cdot17\cdot19)(U-V).
\]
Thus \(2.048<G<2.049\) while the three supporting primes all lie between 13 and 19.

## Infinitely many localized examples

Fix \(0<\theta\le1\), \(0\le\gamma<1\), and a reduced residue class \(h\bmod d\). There are unbounded \(P,C\) and primitive triples as above with the following simultaneous properties.

* Every prime in \(UV\) lies in \( [P,P+P^\theta] \) and is \(h\bmod d\).
* When \(\gamma>0\), both \(U,V\) are \(m\)-th powers for a common prime \(m\gg_{\theta,\gamma,d}(\log C)^\gamma\).
* For a positive constant depending only on the fixed parameters,
\[
 \log G\gg_{\theta,\gamma,d}
 \frac{(\log C)^{\theta(1-\gamma)/(1+\theta)}}{\log\log C}.
\]

In particular, relative widths \(P^{\theta-1}\) tending to zero at any fixed \(\theta<1\) suffice for a gain exceeding every fixed power of \(\log C\), even after discarding every saving from the difference. The constructed \(P\) is \(\gg (\log C)^{(1-\gamma)/(1+\theta)}\).

Take \(T\to\infty\) and partition \( [T,2T] \) into intervals of length at most \(\lfloor T^\theta\rfloor\), using \(O(T^{1-\theta})\) intervals. The prime number theorem in the fixed progression gives \(\gg_d T/\log T\) eligible primes in total. One interval therefore contains a subset \(S\) of \(k\asymp_d T^\theta/\log T\) eligible primes. Let \(P\) be the left endpoint. Put \(E=\lceil8T\rceil\), and form the \((E+1)^k=N\) distinct numbers \(\prod_{p\in S}p^{e_p}\) with \(0\le e_p\le E\). Their logarithms lie in \( [0,H_0] \) for \(H_0=Ek\log(2T)\ll T^{1+\theta}\). Ordering them gives two distinct products \(A>B\) with
\[
 0<\log(A/B)\le H_0/(N-1).
\]
Write \(u=A/\gcd(A,B)\), \(v=B/\gcd(A,B)\). For \(\gamma=0\) take \(m=1\). Otherwise set \(\beta=\gamma(1+\theta)/(1-\gamma)\) and use Bertrand's postulate to choose a prime \(m\asymp T^\beta\). Write \(\beta=0\) also in the first case. Take \(U=u^m,V=v^m\). Since \(D/C=1-\exp(-m\log(u/v))\le m\log(u/v)\),
\[
 G\ge\frac{N-1}{mH_0(2T)^k}
 \ge\frac{4^k}{2mH_0}.
\]
It follows that \(\log G\gg k\), so the heights are unbounded. Also \(\log C\le mH_0\ll T^{1+\theta+\beta}\). Substitution into the eventually increasing function \(x^{\theta/(1+\theta+\beta)}/\log x\) proves the stated bound, since \(\theta/(1+\theta+\beta)=\theta(1-\gamma)/(1+\theta)\). The bounds on \(m,P\) follow from the same height inequality. This finite search can be defined deterministically by choosing the first eligible interval, the least eligible primes, and the closest pair with ties resolved by numerical order. It uses no hypothesis on primes in every short interval.

## Intervals of arbitrarily slowly growing absolute width

For every positive function \(w(P)\to\infty\) there are intervals \([P,P+w(P)]\), with \(P\to\infty\), and primitive triples for which all prime divisors of \(UV\) belong to that interval and
\[
 \frac{\log G}{\log\log C}\longrightarrow\infty.
\]
Simultaneously \(U,V\) are \(m\)-th powers with a common prime \(m\) satisfying \(\log m/\log\log C\to1\).

For each fixed integer \(k\ge9\), Maynard's theorem gives a constant \(B_k\) and infinitely many intervals \([P,P+B_k]\) containing at least \(k\) primes. Choose one with \(P>B_k\), with \(w(P)\ge B_k\), and with \(P\) larger than at all previous steps. Select \(k\) of those primes as \(S\). Make the same box of products with an integer \(E\) now tending to infinity *after* fixing \(k,P\). Choose a prime \(E^{\sqrt{k}}\le m\le 3E^{\sqrt{k}}\) by Bertrand's postulate. The same spacing inequality gives
\[
 G\ \ge\ \frac{(E+1)^k-1}{m E k\log(2P)(2P)^k}
 \ \ge\ E^{k-\sqrt{k}-2},
 \qquad
 H=\log C\le m E k\log(2P)\le E^{\sqrt{k}+2}
\]
once \(E\) is sufficiently large for this particular \(k,P\). Thus \(\log G/\log H\ge(k-\sqrt{k}-2)/(\sqrt{k}+2)\), which tends to infinity as \(k\) increases. Also \(m\ge H^{\sqrt{k}/(\sqrt{k}+2)}\) while \(m\le H/\log 2\), since \(C\) is a nontrivial \(m\)-th power. This proves the prime-exponent assertion. The cluster theorem is used separately for each fixed \(k\), so no uniform error term in Maynard's theorem is required. [Maynard, *Small gaps between primes*, Annals of Mathematics 181 (2015), Theorem 1.1](https://doi.org/10.4007/annals.2015.181.1.7)

### Which repeated primes could produce a fixed exponent?

For \(U=u^m>V=v^m\), the elementary inequality \(1-(v/u)^m\ge1-v/u\ge1/u\) gives \(G\le C^{1/m}\). Thus the logarithm of the certified gain in the unbounded-prime-exponent construction is \(o(\log C)\).

There is also a necessary condition for a genuine fixed-exponent exception. Put \(\Phi=(u^m-v^m)/(u-v)\) and let \(m\) be an odd prime. Since \(\Phi\ge u^{m-1}\) and \(\gcd(uv,\Phi)=1\),
\[
 \frac C{\operatorname{rad}(UVD)}\le
 \frac{C^{1/m}}{\operatorname{rad}(uv)}\cdot\frac{\Phi}{\operatorname{rad}(\Phi)}.
\]
If \(m\mid\Phi\), reduction modulo \(m\) first gives \(m\mid u-v\), and binomial expansion gives \(v_m(\Phi)=1\). For each other prime \(q\mid\Phi\), the residue \(u/v\bmod q\) has exact order \(m\). Indeed, \(q\mid u-v\) would give \(\Phi\equiv m v^{m-1}\not\equiv0\bmod q\). Consequently \(q\equiv1\bmod m\). If \(q^2\mid\Phi\), then \((u/v)^m\equiv1\bmod q^2\), hence \(u^{q-1}\equiv v^{q-1}\bmod q^2\). In particular a fixed-exponent exception \(C/\operatorname{rad}(UVD)\ge C^\eta\) on this family requires
\[
 \prod_{\substack{q^e\parallel\Phi\\e\ge2,\ q\equiv1\bmod m}}q^{e-1}
 \ \ge\ \operatorname{rad}(uv) C^{\eta-1/m}.
\]
In the arbitrarily slowly growing windows, every prime in this product is at least \((\log C)^{1-o(1)}\). No assertion about the factorization of the unfactored difference is needed for the construction or this implication.

## A uniform obstruction when the number of primes stays bounded

Suppose \(UV\) has exactly \(k\ge2\) prime divisors, all in \( [P,P+W] \), where \(P\ge2, W\ge1\). Put \(E=\sum_{p\mid UV}v_p(UV)\). If
\[
  2E W^{k-1}\le P ,
\]
then \(G\le 2+2^{k+1}k/P\), and in fact \(G<1\) for \(P\gg_k1\).

Write the primes \(p_i=P+d_i\), with \(P\) an integer and \(0\le d_i\le W\); one can take \(P\) to be the least prime and shorten the interval. Write \(a_i=v_{p_i}(U)-v_{p_i}(V)\), and \(M_j=\sum_i a_i d_i^j\), taking \(d_i^0=1\). The Vandermonde determinant is nonzero, so at least one \(M_j\) with \(0\le j\le k-1\) is a nonzero integer. Let \(j\) be the first. If \(j=0\) then
\[
 |\log(U/V)|\ge\log P-EW/P\ge\log P-1/2.
\]
In this case \(G\le (1-e^{1/2}/P)^{-1}P^{-k}\), which is already less than 2 for \(P\ge2\).

For \(1\le j\le k-2\), Taylor expansion of \(\log(1+x)\) gives the leading term \( (-1)^{j+1}M_j/(jP^j)\) in \(\log(U/V)\). The remainder has absolute value at most \(E(W/P)^{j+1}/(j+1)\le 1/(2(j+1)P^j)\). Hence \(|\log(U/V)|\ge 1/(2jP^j)\).

If \(j=k-1\), the evaluation weights \(a_i\) annihilate all polynomials in \(d_i\) of degree less than \(j\). The Lagrange interpolation formula shows
\[
  a_i=\frac{M_j}{\prod_{l\ne i}(d_i-d_l)}.
\]
Indeed the functional \(f\mapsto\sum_i a_i f(d_i)\) equals \(M_j\) times the leading coefficient on polynomials of degree at most \(j\). Applying the divided-difference mean-value theorem to \(f(t)=\log(P+t)\) gives some \(0\le\xi\le W\) with
\[
 |\log(U/V)|=\frac{|M_j|}{j(P+\xi)^j}\ge\frac{1}{j(2P)^j}.
\]
This last estimate uses \(W\le P\). In each positive-\(j\) case, \(C/D=(1-e^{-|\log(U/V)|})^{-1}\le 1+1/|\log(U/V)|\). Thus \(G\le P^{-k}(1+2^k k P^{k-1})\). Together these estimates prove the elementary obstruction.

Fix \(k\ge2\) and \(0<\delta<1/(k-1)\). Uniformly for
\[
 W\le P^{1/(k-1)-\delta}
\]
and arbitrary positive exponents, one has
\[
 \log^+ G\ll_{k,\delta}(1+\log\log(3C))^{k+1}.
\]
Here \(\log^+ G=\max(0,\log G)\). Indeed, unless the elementary bound applies we have \(2E>P/W^{k-1}\ge P^{(k-1)\delta}\). Matveev's theorem on a nonzero product of rational powers minus 1 gives
\[
 \log(C/D)\ll_k(1+\log E)\big(\log(2P)\big)^k.
\]
Apply it to \(\min(U,V)/C-1\ne0\), whose bases are the \(k\) positive rational primes, heights at most \(\log(2P)\), integral coefficients of absolute value at most \(E\), and ambient degree one. Now \(\log(2P)\ll_{k,\delta}1+\log E\) and \(E\le 2\log C/\log2\). This proves the stated uniform bound. [Matveev, Izvestiya Mathematics 64 (2000)](https://doi.org/10.1070/IM2000v064n06ABEH000314)

Consequently, any sequence of fixed-exponent abc exceptions \(C/\operatorname{rad}(UVD)\ge C^\eta\) in this bounded-\(k\) range must have \(D/\operatorname{rad}(D)\ge C^{\eta-o(1)}\). If \(D\) is squarefree, abc holds uniformly here with the explicit form of the subpower loss above. The unrestricted ordinary radical still depends on the repeated prime factors of \(D\). The localized lower bound also has a sublinear logarithm and gives no disproof of rational abc.

## Two primes whose ratio tends to one

When the two bases are primes \(p<q\), the interval may have any width \(o(p)\). More precisely, for \(U=p^a,V=q^b\), positive \(a,b\), and \(\rho=(q-p)/p\le1/2\),
\[
 \frac{\log^+ G}{\log C}
 \ll \rho\bigl(1+\log(1/\rho)\bigr)^2
\]
with an absolute implied constant. In particular, for \(q/p\to1\), fixed-exponent abc failures from these prime powers require \(D/\operatorname{rad}(D)\ge C^{\eta-o(1)}\).

If \(a=b\), the inequality \(C/D\le q/(q-p)\) gives \(G<1\). Otherwise put \(t=(a+b)/\log p\) and \(L=a\log p-b\log q\ne0\). If \(t<1/(2\rho)\), then \(|L|\ge\log p-b\log(1+\rho)\ge(\log p)/2\), again giving \(G<1\). For \(t\ge1/(2\rho)\), apply the two-logarithm estimate of Laurent, Mignotte and Nesterenko, *Formes linéaires en deux logarithmes et déterminants d'interpolation*, J. Number Theory **55** (1995), 285–321, Corollary 2. In degree one its bound is
\[
 -\log |L|\ll (\log A_1)(\log A_2)
  \left(1+\log^+\left(\frac a{\log A_2}+\frac b{\log A_1}\right)\right)^2.
\]
The bases \(p,q\) are positive and multiplicatively independent. Take \(\log A_1=\log A_2=\log(2q)>1\), which dominates their logarithmic heights and their real logarithms. The right side is \(O((\log p)^2(1+\log^+t)^2)\). Since \(C/D\le 1+1/|L|\) and \(\log C\ge t(\log p)^2/2\), it follows that \(\log^+G/\log C\ll (1+\log^+t)^2/t\). The supremum of the last expression on \(t\ge1/(2\rho)\) is \(O(\rho(1+\log(1/\rho))^2)\), by differentiation. This proves the claim.
