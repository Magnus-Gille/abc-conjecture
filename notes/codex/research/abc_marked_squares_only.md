# Positive abc excess paid for by prescribed primes of exact valuation two

For triples \(1+b=c\) with \(c>2\), mark distinct odd primes in a set \(S\), write \(D=\prod_{p\in S}p\), and require \(p^2\parallel b\) for each of them. If \(P=\operatorname{rad}(c)\), the exact identity is
\[
 \frac{c}{\operatorname{rad}(bc)}
 =\frac{c}{c-1}\frac{D}{P}\,
   \frac{b}{D\operatorname{rad}(b)}.
\]
The last factor is a positive integer. We use only the first two factors to certify the excess. Thus a large repeated prime hidden in the rest of \(b\) plays no role in these lower bounds.

## Independently twisted squares at any odd primes

For every nonempty \(S\), and for arbitrary integers \(j_p\ge1\) and units \(u_p\bmod p^{j_p}\), one can attain
\[
 b/p^2\equiv u_p\bmod p^{j_p}\quad(p\in S),\qquad
 \frac{c}{\operatorname{rad}(bc)}>\frac{2D}{D+1}>1.
\]
Set \(t=D-1\) if \(D\equiv1\bmod4\), and \(t=D+1\) otherwise. Then \(4\mid t\), so \(P=\operatorname{rad}(t)\le (D+1)/2\). Take \(c=t^{2Dm}\). For every odd \(p\mid D\), the factorization \(t^2-1=D(D\pm2)\) gives \(v_p(t^2-1)=1\). Therefore \(v_p(t^{2D}-1)=2\) by lifting the exponent. The powers of \(t^{2D}\) run through the whole subgroup \(1+p^2\mathbb Z\bmod p^{2+j_p}\), since the order is exactly \(p^{j_p}\) by the same lifting formula. Choose \(m\bmod p^{j_p}\) to obtain \(c\equiv1+p^2u_p\bmod p^{2+j_p}\), independently at each prime. CRT gives an \(m\) between 1 and \(\prod p^{j_p}\), as well as infinitely many positive choices. This proves the assertion with an explicit logarithmic height bound \(2D(\prod p^{j_p})\log(D+1)\) for the least positive choice.

## A single arbitrary large prime

For every odd prime \(p\) sufficiently large there is a prime \(r\le(\log p)^{2+o(1)}\) such that \(r^{p-1}\not\equiv1\bmod p^2\). For completeness, fix \(\epsilon>0\), take \(y=(\log p)^{2+\epsilon}\), and use the products of \(k=\lfloor(2\log p-\log2)/\log y\rfloor\) distinct primes at most \(y\). These products are distinct integers below \(p^2\), and none is divisible by \(p\). Their number is at least \((\pi(y)/k)^k\), whose logarithm is
\[
 \left(\frac{2(1+\epsilon)}{2+\epsilon}+o(1)\right)\log p>\log p
\]
by the prime number theorem (Chebyshev's lower estimate suffices). The solutions to \(x^{p-1}=1\bmod p^2\) form a subgroup of order \(p-1\), by simple-root lifting from \(\mathbb F_p^\times\). If every prime through \(y\) were in it, all the distinct products would lie in it as well. This contradiction proves the quoted bound in the sense of an exponent \(2+o(1)\). This elementary estimate suffices in place of stronger known bounds for the least nonzero Fermat quotient.

Take \(c=r^{p(p-1)m}\). Now \(v_p(r^{p(p-1)}-1)=2\). As before, \(m\) can realize any prescribed unit twist of \((c-1)/p^2\) to arbitrary finite precision. In every case the marked prime alone gives
\[
 \frac{c}{\operatorname{rad}(bc)}>\frac p r
   \ \ge\ \frac{p}{(\log p)^{2+o(1)}}.
\]
Within the family \(1+b=c\), the certificate paying \(b\) in full except at this single square equals \((c/(c-1))\,p/\operatorname{rad}(c)\le(c/(c-1))p/2\). The construction therefore attains the full power of the specified prime in this certificate, up to a polylogarithmic factor.

## Many independent twists with near-optimal joint gain

Let \(Y\to\infty\) and let \(S\) be **any nonempty subset** of the odd primes in \([Y,2Y]\). Uniformly in \(S\) and in all the twist precisions and target units, the construction can attain
\[
 \frac{c}{\operatorname{rad}(bc)}>D^{1-O(\log\log Y/\log Y)}
\]
using only the exact squares at the prescribed primes. Set \(L=\operatorname{lcm}_{p\in S}(p-1)\). No \(p\in S\) divides \(L\), since an even multiple of \(p\) is at least \(2p\), while \(q-1<2p\) for every \(q\in S\). For each \(p\in S\) choose a prime \(r_p\le(\log(2Y))^3\) with nonzero Fermat quotient at \(p\) by the previous count. For large \(Y\) these bases are all outside \(S\). Let \(T\) be the set of distinct chosen bases.

For every \(r\in T\) we have \(r^{LD}\equiv1\bmod p^2\) at all \(p\in S\). For \(r=r_p\), the valuation of \(r_p^{LD}-1\) is exactly two because \(p\nmid L\), \(v_p(D)=1\), and \(v_p(r_p^{p-1}-1)=1\). Take
\[
 c=\prod_{r\in T}r^{LD\,e_r}.
\]
At prime \(p\), impose \(e_r\equiv0\bmod p^{j_p}\) for each \(r\ne r_p\). The base \(r_p^{LD}\) generates the principal subgroup \(1+p^2\mathbb Z\bmod p^{2+j_p}\), so choose its exponent \(e_{r_p}\bmod p^{j_p}\) to hit \(1+p^2u_p\). CRT for each \(e_r\) imposes all these conditions, even if one base is selected for several primes. Set \(J=\prod p^{j_p}\); one may take \(1\le e_r\le J\). This gives
\[
 \log c\le LDJ\,|S|\,3\log\log(2Y),\qquad
 P=\prod_{r\in T}r\le ((\log(2Y))^3)^{|S|}.
\]
Since \(\log D\ge |S|\log Y\), the radical identity proves the claimed joint bound. In particular, for unit twists specified modulo \(p\) at each \(p\), \(J=D\) and \(L\le D\) give \(\log c\le D^{3+o(1)}\). Every marked prime may move, and their number may grow arbitrarily within the interval.

For a numerical check take \(p=1093,3511\). Both have zero Fermat quotient at base 2 and nonzero Fermat quotient at base 3. For \(D=3837523,\ L=49140\) and \(m=3554366\), take \(c=3^{LDm}=3^{670267697074040520}\). Modular exponentiation gives
\[
 \frac{c-1}{1093^2}\equiv37\bmod1093,\qquad
 \frac{c-1}{3511^2}\equiv59\bmod3511.
\]
Equivalently, verify \(\operatorname{pow}(3,670267697074040520,p^3)=1+p^2u_p\) for the two displayed pairs. Therefore \(c/\operatorname{rad}(bc)>3837523/3>1{,}279{,}174\), without factoring \(c-1\).

## The height scale for a dense marked set

Suppose \(\log D\gg Y\), for example when \(S\) contains all primes in \([Y,2Y]\). Then \(L=D^{o(1)}\). For a proof let \(K\ge2\) be fixed. Primes at most \(Y/K\) contribute \(O(Y/K)\) to the sum of distinct prime logarithms in \(L\) by Chebyshev's bound. All exponents after the first contribute \(O(\sqrt Y\log^2(2Y))\) since \(L\) divides \(\operatorname{lcm}(1,\ldots,\lfloor2Y\rfloor)\). Each remaining prime \(q\) divides some \(p-1\), so \(q,1+kq\) are prime for one integer \(k\le2K\). For each fixed \(k\) this is a density-zero condition among primes \(q\): impose \(kq+1\not\equiv0\bmod t\) for primes \(3\le t\le Z\) not dividing \(k\). The prime number theorem in fixed progressions gives an upper relative density \(\prod_t(1-1/(t-1))\) apart from finitely many equalities with those \(t\). The product tends to zero as \(Z\to\infty\). Hence these remaining \(q\) have total log weight \(o_K(Y)\). Let \(K\to\infty\) to obtain \(\log L=o(Y)\).

With arbitrary twists specified modulo \(p\) at every marked prime, the preceding construction now gives \(\log c\le D^{2+o(1)}\) and the joint certified gain is at least \((\log c)^{1/2-o(1)}\).

If only the exact valuation two is prescribed, every \(e_r\) may be taken at most \(2|S|\). Choose them independently and uniformly from \(1,\ldots,2|S|\). Modulo \(p^3\) the value of \((c-1)/p^2\bmod p\) is the linear form \(\sum_r e_r(r^{LD}-1)/p^2\bmod p\). Its coefficient at \(r_p\) is nonzero. Since \(2|S|<Y\) for large \(Y\), conditioning on the other variables gives probability at most \(1/(2|S|)\) that the form vanishes. A union bound leaves probability at least \(1/2\) of obtaining every exact square simultaneously. Exhaustive finite search thus finds a valid tuple. Now \(\log c=D^{1+o(1)}\), since \(D\log2\le\log c\le LD\,2|S|^2\,3\log\log(2Y)\). In particular the gain certified just by the marked squares is \((\log c)^{1-o(1)}\). Conversely, every output of the construction is a nontrivial \(D\)-th power, so \(D\le\log c/\log2\). This bounds the marked-square certificate itself by \(O(\log c)\), independently of further prime factors in \(c-1\).

For arbitrary assignments of squared primes to different terms and arbitrary compatible residues of all three entries, the [general congruence construction](abc_prescribed_crt_excess.md) supplies a separate positive gain and exact equality for the unfactored contribution. The bounds here are polynomial in the marked primes. They do not establish an infinite fixed-positive-power gain in \(c\).
