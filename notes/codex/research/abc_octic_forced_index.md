# Forced index divisors on the orbit of (1,2)

Keep the slope signed until the end. Write its reduced form as \(x(P_m)=s/t\) and put \(U_\pm=(s\pm t)^2+t^2\). Use the odd-index orbit on \(65y^2=x^4+4\) with initial slope \(1/2\). All logarithms below are natural.

| Assumption | Necessary seed divisor of \(m\) | Further distinct prime divisors certified | Decimal digits in the certified divisor |
|---|---:|---:|---:|
| \(U_+\) cubeful | 13 | 105 | 607 |
| \(U_-\) cubeful | 5 | 240 | 1,425 |
| \(U_+\) cubeful, \(65\mid m\) | 65 | 1,510 | 9,400 |
| \(U_-\) cubeful, \(65\mid m\) | 65 | 762 | 4,677 |

Both norms are squareful exactly when \(65\mid m\), using admissible primitive coordinates. Their seed valuations force the divisibility, and all primes outside 5 and 13 have even valuations since the product is 65 times a square and the norms are coprime. Taking absolute values can interchange the two columns of norms. In particular, an odd index yielding two squareful norms and one cubeful norm has \(|m|\ge10^{4676}\) on this orbit.

## Local implication

Over \(\mathbf Q(\sqrt{65})\) write the seed as \(P=((1+\sqrt{65})/8,(1+\sqrt{65})/16)\) on \(E:V^2=X^3-X\), with elliptic origin at infinity. Its conjugate is \((0,0)-P\), so \(T=2P-(0,0)\). The point \(T\) corresponds to \(Q=(-16,-252)\) on \(E_{65}:Y^2=X^3-4225X\) by \((X,Y)\mapsto(X/65,Y/(65\sqrt{65}))\). We have \(P_r=P+[(r-1)/2]T\) for odd \(r\), and for any branch point \(W\), \(P_{rk}-W=[k](P_r-W)\) in the group with origin \(W\).

Suppose a good prime \(p>13\) has \(v_p(U_\pm(P_r))=2\). The reduction meets a unique branch of the indicated norm. It lifts to a branch \(W\) over \(\mathbf Q_p\) because \(p\equiv1\pmod4\). A branch parameter has square equal to the slope difference up to a unit. The point \(P_r-W\) is in the formal group and has parameter valuation one. In residue characteristic \(p>13\), multiplication by \(k\) changes this valuation by exactly \(v_p(k)\), as follows from the formal logarithm. Therefore for odd \(k\)
\[
 v_p(U_\pm(P_{rk}))=2+2v_p(k).
\]
For a prospective cubeful norm, whenever \(r\mid m\) this forces \(p\mid m/r\). The analogous seed valuation is \(1+2v_p(m)\), with \(p=13\) for \(U_+\) and \(p=5\) for \(U_-\).

The following verifier reads one list of witnesses, checks primality by trial division, checks earlier forced divisors include the current witness index, and directly computes the designated norm modulo \(p^3\) with an invertible slope denominator. Its elliptic additions take place first on \(E_{65}\) and then on \(E\) over the quadratic algebra obtained by adjoining \(\sqrt{65}\) to \(\mathbf Z/p^3\mathbf Z\). The verified layers for initial divisor 65 have sizes \(16,455,770,241,27,1\) on the plus side and \(16,243,351,139,13\) on the minus side. For an example of a single chain on the plus side, the table verifies forcing from \(13\) to \(41\), then \(149\), then \(5813\).

[Standard-library verifier](abc_octic_forced_index_verify.py) · [Witness list](abc_octic_forced_index_certificates.txt)

## An entire infinite subsequence can be excluded

At index \(5\) the signed slope is \(408328610689/25712328458\). For its primitive coordinates the plus norm has remainder \(2601=9\cdot17^2\bmod 17^3\), and the minus norm has remainder \(13456=16\cdot29^2\bmod29^3\). Therefore at every \(m=65^j,\ j\ge1\), the signed plus norm has valuation exactly two at 17 and the signed minus norm has valuation exactly two at 29. The lifting formula applies with \(r=5,\ k=65^j/5\), whose prime factors are 5 and 13. Thus neither norm on this particular infinite sequence is cubeful. This includes the index \(65\) previously used to exhibit simultaneous squarefulness.

More generally there is an exact divisibility test on this fixed orbit. Designate one signed norm to be cubeful and the other to be squareful, without swapping signs mid-test. Begin at index 1 and adjoin as factors of the current index all primes whose valuation is positive but below its designated threshold. Newly adjoined primes can be taken to the first power. Once a prime divides the index, if it occurs then its valuation is at least three (at least four at a good prime): the first odd rank is below the prime, and odd-index lifting adds at least two. The bad seed primes satisfy the displayed seed formula instead. By induction each index produced must divide every solution index, because preserving a deficient valuation at a divisor is impossible unless the new prime divides the quotient. Therefore the procedure either stops at a squarefree solution dividing every solution, or continues indefinitely and there is no solution on the orbit for that choice of sign. Taking absolute values can interchange signs, so both choices matter. The certificate above carries out finite implications within this procedure and leaves its eventual outcome open.

## Why this only proves lower bounds

For a good prime \(p\), an odd witness index reducing to a branch is a multiple of the order \(r_p\) of \(Q\) modulo \(p\), because \([r]T=2P_r-(0,0)\). The odd-order subgroup it generates is disjoint from the rational two-torsion of order four. Hasse's bound gives \(4r_p\le(\sqrt p+1)^2\), hence \(r_p<p\). When a branch is first encountered its necessary index factors are therefore all smaller than its prime. The finite good-prime implications can all be satisfied by including the primes in the index, and no finite cycle of these order conditions excludes every index. Excluding every index by this technique requires a theorem that the forcing continues without bound.

## An explicit slope height

Let \(h(u/v)=\log\max(|u|,v)\) for a reduced fraction \(u/v\), \(v>0\). On \(E_{65}\) the duplication fraction with \(B=4225\) is
\[
 \frac{(u^2+Bv^2)^2}{4uv(u^2-Bv^2)}.
\]
The gcd is at most \(4\cdot65^4\). Only primes dividing \(2B\) can occur. At 2 the numerator is odd or has valuation two. At \(p=5,13\), the numerator has valuation zero for \(p\nmid u\), and valuation four for \(p^2\mid u\). When \(v_p(u)=1\), a numerator valuation exceeding four forces the denominator valuation to be three. Consequently
\[
 4h(x(R))-\log(4\cdot65^4)\le h(x(2R))
 \le4h(x(R))+2\log4226.
\]
The reduced coordinate \(x(2Q)=4481^2/254016\) gives \(2\hat h(Q)\ge (2\log4481-\log(4\cdot65^4)/3)/4>2.69\) by the doubling limit. The other inequality then gives \(h(x([m]Q))\ge2.69m^2-(2/3)\log4226\). Finally \(x([m]Q)=-260s^2t^2/(s^4+4t^4)\), from \([m]T=2P_m-(0,0)\). With \(H=\max(|s|,t)\), this implies \(H>\exp(m^2/2)\) for \(|m|\ge5\).
