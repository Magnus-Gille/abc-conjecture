# Exact primitive-rank mass in the factor \(u_n^2+8v_n^2\)

Let \(E:y^2=x^3+16x^2+32x\), \(R=(-8,16)\), \(n=2^{j+1}\) with \(j\ge1\), and \(M=2^j\). Write \(x(MR)=u_n^2/v_n^2\) and \(s_n=u_n^2+8v_n^2\) as in the dyadic construction. For each positive odd integer \(d\), let \(B_d\) be the positive square root of the reduced denominator of \(x(dR)\), with \(B_1=1\). For \(d>1\) let \(F_d\) be the product of the prime powers in \(B_d\) whose prime has reduction order exactly \(d\) for \(R\). Put \(F_1=1\).

The factorization
\[
              s_n=B_{M-1}B_{M+1}
\]
is exact, and its two factors are coprime. Primes of respective first ranks \(M-1\) and \(M+1\) account for a sharp lower limiting fraction between \(0.90321\) and \(0.90323\) of \(\log s_n\), **with their full multiplicities**. Specifically, with \(v_2\) denoting the exponent of 2, put \(\nu(p)=v_2(\operatorname{ord}_p(2))\) for odd primes \(p\). Then
\[
 \liminf_{j\to\infty}\frac{\log(F_{2^j-1}F_{2^j+1})}{\log s_{2^{j+1}}}
 =\frac12\left(\prod_{\nu(p)\le1}(1-p^{-2})
                    +\prod_{\nu(p)=2}(1-p^{-2})\right).
\]
Here the primes in the Euler products divide the *indices* of the elliptic denominators, while primes in \(F_d\) divide the denominators themselves.

## The factorization and the elliptic height

At an odd prime \(p\), the curve has good reduction and \(R,-R\) reduce to distinct points with unit ordinate. A prime of \(s_n\) is a unit on \(v_n\), and \(MR\) then reduces to exactly one of \(R,-R\). Conversely these reductions force \(p\mid s_n\). The abscissa difference is a local parameter at each of these two points, since \(2y\) is a unit there. Translation is an isomorphism of the good model. Thus \(v_p(s_n)\) equals the formal depth of the unique point \((M\pm1)R\) reducing to the identity, namely \(v_p(B_{M\pm1})\). At 2 use the integral model \(Y^2=X^3+4X^2+2X\), with \(x=4X,\ y=8Y\). The point \(R\) has integral coordinates there and \(2R\) has \(X=1/4\), so \(2R\) belongs to the formal subgroup and \(R\) does not. Every odd multiple is outside this subgroup, hence has integral \(X\) at 2. Both odd-index denominators and \(s_n\) are odd, proving the identity and coprimality.

Write \(H=\widehat h(R)>0\) for the canonical height in the convention \(h(x(P))=2\widehat h(P)+O(1)\). All odd multiples of \(R\) lie on the bounded real component, since \(-8\) lies between the two negative roots \(-8\pm4\sqrt2\). Hence the ordinary absolute values of their abscissas are bounded above by a fixed constant. It follows uniformly at odd indices that
\[
                 \log B_d=H d^2+O(1).
\]
At good odd \(p\) of reduction order \(r\), the formal logarithm gives \(v_p(B_{rh})=v_p(B_r)+v_p(h)\). Apply Möbius inversion to \(\log B_d\) at an odd \(d>1\). The initial-depth term remaining is precisely \(\log F_d\). An additional \(\log p\) remains only when \(d/r\) is a positive power of \(p\), since the Möbius transform of \(v_p(h)\) is the indicator of the positive powers of \(p\). The sum of these additions is at most \(\log d\). Consequently
\[
 \log F_d=H J_2(d)+O(\tau(d)+\log d),\qquad
 J_2(d)=d^2\prod_{p\mid d}(1-p^{-2}),
\]
where \(\tau(d)\) counts positive divisors.

## Every odd rank at least three occurs

In fact \(F_d>1\) for **every odd \(d\ge3\)**. To bound the constants write \(x=P/Q\) in lowest terms and \(U=\max(|P|,|Q|)\). The duplication map is represented by
\[
 F=(P^2-32Q^2)^2,\qquad G=4PQ(P^2+16PQ+32Q^2).
\]
Their absolute values are at most \(1089 U^4\). No odd prime divides both, since a common divisor would force \(P/Q=-4\) and \((P/Q)^2=32\) modulo that prime. The dyadic gcd divides \(2^{10}\): when \(P\) is odd \(F\) is odd, and when \(P\) is even \(v_2(P^2-32Q^2)=\min(2v_2(P),5)\).

Over the reals, \(\max(|F|,|G|)\ge U^4/16\). If \(U=|Q|\), then \(|P^2-32Q^2|\ge31U^2\). Otherwise put \(z=Q/P\). If \(|1-32z^2|\ge1/4\), use \(F\). In the remaining case \(|z|>\sqrt{3/128}\) and \(1+32z^2<9/4\). For negative \(z\) this gives \(|1+16z+32z^2|>\sqrt6-9/4\), and for positive \(z\) it is greater than one. In both cases \(4|z(1+16z+32z^2)|>1/16\). Thus
\[
 \bigl| h(x(2P'))-4h(x(P'))\bigr|\le14\log2
\]
for points in the nontorsion orbit. Telescoping gives \(|h(x(P'))-2\widehat h(P')|\le(14/3)\log2\). At \(4R\), \(x=961/196\), so \(H\ge(\log961-(14/3)\log2)/32>1/10\). For odd \(d\), \(1<|x(dR)|<14\), giving \(|\log B_d-Hd^2|<3\). The preceding inversion now gives
\[
 \log F_d\ge \tfrac1{10}(8/\pi^2)d^2-3\tau(d)-\log d>0\quad(d\ge25,\ d\text{ odd}),
\]
where \(\tau(d)\le2\sqrt d\) suffices. The verifier computes \(B_d\) by rational addition for the remaining odd \(3\le d\le23\), and removes the complete prime support of all proper divisor indices by integer gcd. In each case the residue exceeds one.

Consequently, denoting the number of distinct primes by \(\omega\),
\[
 \omega(s_{2^{j+1}})\ge \tau(2^j-1)+\tau(2^j+1)-2.
\]
Each nontrivial divisor of either integer supplies a different reduction order. For \(j\ge4\), both integers exceed nine, and the one divisible by three must have at least four divisors (a larger multiple of three cannot be the square of a prime). Thus every \(s_n\) for \(n\ge32\) has at least four distinct prime factors. At \(n=16\), \(B_7=117041\) and \(B_9=3^3\cdot11\cdot67\cdot13411\) already give at least four. In particular \(s_n=3^a p^b q^c\) with two distinct non-3 primes is impossible at every dyadic \(n\ge16\), regardless of the exponents. At \(n=8\), \(s_8=3^2\cdot281\).

There is a size consequence independent of the multiplicities. At each nontrivial divisor rank \(d\), Hasse's bound gives \(p\ge(\sqrt d-1)^2\), hence \(\log p\ge\log d-O(1)\). Summing over the different ranks yields
\[
 \log\operatorname{rad}(s_n)\ge
 \tfrac12\sum_{\pm}\tau(M\pm1)\log(M\pm1)-O(\tau(M-1)+\tau(M+1)).
\]
The existence of a prime at each rank gives no lower bound on the fraction of its logarithmic size that survives taking the radical.

## Sharp constant

Write \(A_j,B_j'\) for the products \(\prod_{p\mid 2^j-1}(1-p^{-2})\) and \(\prod_{p\mid 2^j+1}(1-p^{-2})\). The preceding estimates show that the desired log fraction is \((A_j+B_j')/2+o(1)\). The factor \(2^j-1\) contributes only primes with \(\nu(p)\le h=v_2(j)\), and \(2^j+1\) only those with \(\nu(p)=h+1\). For fixed \(h\), the lower limit is exactly
\[
 C_h=\tfrac12\left(\prod_{\nu(p)\le h}(1-p^{-2})
                     +\prod_{\nu(p)=h+1}(1-p^{-2})\right).
\]
The products are lower bounds term by term. To attain them, take \(j\) of valuation \(h\) divisible by the odd parts of the orders of 2 at every odd prime up to a growing cutoff. The signs of \(2^j\bmod p\) then realize every eligible index prime. The Euler products converge absolutely, so larger primes have vanishing effect on the approximation.

The minimum is attained for \(h=1\). For \(h=0,1,2\) the interval verifier below uses all primes through \(200000\), bounding the unexamined product from below by \(1-1/200000\). It gives \(C_0>0.9263\), \(0.90321<C_1<0.90323\) and \(C_2>0.9050\). For \(h\ge3\) the first product is at least \(8/\pi^2\), the product over all odd primes. Every prime in the second product is \(1\bmod16\) and exceeds 17, since \(\operatorname{ord}_{17}(2)=8\). The second product therefore exceeds \(1-\sum_{a\ge2}(16a)^{-2}=1-(\pi^2/6-1)/256\). These uniform bounds give \(C_h>0.9039\). They also cover varying unbounded \(h\).

## Consequences for repeated primes

If \(s_n\) is squareful, all the primes in the two exact-rank parts already have exponent at least two at their *first* elliptic denominator. The same statement holds if only the part of \(s_n\) coprime to 3 is squareful, for \(2^j-1>3\). In particular, more than 90 percent of the log size then comes from repeated factors of those two first ranks, for all sufficiently large indices. If merely \(\log(s_n/\operatorname{rad}(s_n))/\log s_n>\delta\), the exact-rank parts contribute at least \((\delta-1+C_1-o(1))\log s_n\) in excess. These estimates say nothing about the multiplicities without a hypothesis of this kind.

For any fixed fractional excess \(\delta>0\) along an infinite subsequence one can still localize some of it to a rank \((2^j\pm1)/b\) with a fixed bounded odd \(b\). Indeed the log size in ranks \(r\mid d\) below \(d/K\) is bounded by \(H d^2\sum_{h>K}h^{-2}+o(d^2)\), using \(\log F_r\le\log B_r\) and the height bound. Total additional formal lifting at the index \(d\) contributes at most \(\log d\). Taking \(K>4/\delta\) and applying this at both \(d=2^j\pm1\) leaves a positive fraction of first-rank excess among finitely many possible cofactors \(b\le K\); one sign and cofactor recur infinitely often. Neither the existence nor the exclusion of such excess has been proved.

[Interval and denominator checks](abc_dyadic_shifted_rank_mass.py) · [Radical of the associated abc triple](abc_dyadic_direct_triple.md)
