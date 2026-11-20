# Perfect-power denominator indices have one large prime factor

Let \(E_6:y^2=x^3-36x\), \(G=(-3,9)\), and let \(B_n\) be the positive square root of the reduced abscissa denominator of \([n]G\). If \(n>1\) is odd and \(B_n\) is a perfect power, then
\[
          n=q^a,\qquad q\equiv3\pmod4\text{ prime},\qquad a\ge1.             \tag{1}
\]
For every prime \(\ell\) dividing the power exponent, \(\ell\equiv-1\pmod{48}\) and \(4q\mid\ell+1\). The integer \(q\) is the order of \(G+(0,0)\) modulo \(\ell\). These are necessary conditions. They do not establish the occurrence of a nontrivial perfect power.

More generally let \(S\) be a fixed finite set of rational primes, \(M=\max(\{3\}\cup S)\), and suppose \(k\ge2\) divides \(v_p(B_n)\) for every \(p\notin S\). Remove from \(n\) its full part supported on primes at most \(M\), and call the remaining positive integer \(m\). Then either \(m=1\), or \(m=q^a\) for a single prime \(q>M\) satisfying all the conditions in (1) and all the displayed restrictions on the prime divisors of \(k\). In the latter case \(B_{q^j}\) itself is a \(k\)-th power for every \(1\le j\le a\). The proof for \(S=\varnothing\) below allows every odd prime of \(n\), including 3, in the argument and gives (1) for the entire index.

## A small Gaussian factor at each split prime index

Write \(x([j]G)=A_j/B_j^2\) in lowest terms. For any prime \(s\equiv1\pmod4\), take \(s=a^2+b^2\) with \(a\) odd and \(b\) positive even, and put \(\lambda=a+bi\) in \(\mathbf Z[i]\). Define
\[
                   D_\lambda=A_aB_b^2+A_bB_a^2.
\]
The point \([a]G\) is on the bounded real component with \(-6<x([a]G)<0\), and \([b]G\) lies on the other component with \(x([b]G)>6\). Neither is torsion. Therefore
\[
 D_\lambda=(A_a+6B_a^2)B_b^2+(A_b-6B_b^2)B_a^2\ge B_b^2+B_a^2\ge5.
\]
Indeed \([2]G=(25/4,-35/8)\) lies in the formal subgroup at 2, so \(B_b\) is even and \(A_b\) is odd. The [quartic coordinates](abc_full_quartic_signature.md) give \(A_a=-3u_a^2\) and \((B_a,6)=1\). At 3 the reduction of \([2]G\) is nonsingular on \(y^2=x^3\). Every even multiple reduces either to the identity or to one of the two nonsingular affine points, both with abscissa 1. In the former case \(3\mid B_b\) and the reduced numerator is a unit; in the latter \(A_b\) is likewise a unit. Hence \(3\nmid A_b\). These facts show that \(D_\lambda\) is prime to 6, including when the multiplier \(b\) takes \([b]G\) into the formal group at 3.

The [Gaussian denominator identity](abc_congruent_six_cubic_packet_character.md) gives \(D_\lambda=N\mathfrak B([\lambda]G)\), where the ideal records the positive formal depths in \(\mathbf Q(i)\). Let \(h\mid D_\lambda\) and take a place \(\mathfrak h\mid h\) where \([\lambda]G\) is formal. The reduction of \(G\) is nonzero since it is integral, and its Gaussian annihilator contains the prime ideal \((\lambda)\); hence it equals \((\lambda)\). Its integer order is exactly \(s\), since \((\lambda)\cap\mathbf Z=(s)\). This odd order makes \(G\) a double over \(\mathbf F_h\). Applying the full rational two-descent to its abscissas \(-3,-9,3\) shows that \(-1\) and 3 are squares modulo \(h\), so \(h\equiv1\pmod{12}\). In particular \(h\) splits in \(\mathbf Q(i)\). At the conjugate place the annihilator is \((\bar\lambda)\ne(\lambda)\); hence precisely one place contributes to \(D_\lambda\). The full rational two-torsion and the odd-order point give \(4s\mid\#E_6(\mathbf F_h)\), so \(h\ge(2\sqrt s-1)^2>2s\). The multiplier \([\bar\lambda]\) on the formal subgroup has unit differential at \(\mathfrak h\), as \(N\lambda=s\ne h\). Thus it preserves the depth, and \([\bar\lambda][\lambda]G=[s]G\) gives
\[
                  e_h:=v_h(B_s)=v_\mathfrak h\mathfrak B([\lambda]G)
                              =v_h(D_\lambda)>0.                            \tag{2}
\]

For the explicit upper bound use \(H=\widehat h(G)<0.52\) and \(h(x([j]G))\le2Hj^2+\log(5184)/3\), following from the [rational duplication estimate](abc_full_quartic_prime_exponents.md). Each of the two terms defining \(D_\lambda\) has absolute value at most \(\exp(h(x([a]G))+h(x([b]G)))\). It follows that
\[
 e_h\log h\le\log D_\lambda\le 2Hs+\tfrac23\log5184+\log2 < 1.04s+6.40.
\]
For \(s\ge5\), \((1.04s+6.40)/s\le2.32<2\log10\le2\log(2s)\). We have proved that for every split prime index \(s\) there is a prime \(h\equiv1\bmod12\) of exact rank \(s\), with \(h>2s\) and \(0<e_h<2s\).

## Excluding split prime divisors of the index

For the version with exceptional support take \(m>1\) as above. For the pure-power case take \(m=n\) and \(S=\varnothing\). Set \(q=P^+(m)=P^+(n)\). Every prime \(h\mid B_q\) has exact order \(q\), since \(B_1=1\). It is \(1\bmod12\) and \(h>2q\) by the same two-descent and Hasse arguments. Consequently \(h\notin S\), \(h\nmid n\), and \(v_h(B_n)=v_h(B_q)\) by multiplication by a unit on the formal subgroup. Thus \(B_q\) is itself a \(k\)-th power. These prime-index denominators are greater than one, as follows for example from the [primitive divisor bound](abc_full_quartic_prime_exponents.md).

Fix a prime \(\ell\mid k\). The [square](abc_full_quartic_square_classification.md) and [cube](abc_full_quartic_cube_descent.md) classifications imply \(\ell\ge5\). The [Eisenstein descent](abc_full_quartic_prime_exponents.md) shows that any prime index \(s\) with \(B_s\) an \(\ell\)-th power must equal \(\mathrm{ord}(G+(0,0)\bmod\ell)\), and that \(4s\mid\#E_6(\mathbf F_\ell)\). In particular \(q\) is the unique candidate for this exponent and \(\ell\ge(2\sqrt q-1)^2>2q\).

Suppose \(m\) has a prime factor \(s\equiv1\bmod4\), and choose the largest such factor. The preceding Gaussian calculation supplies \(h\equiv1\bmod12\) of rank \(s\) with \(h>2s\) and \(0<e_h<2s\le2q<\ell\). In the support version \(h>M\), and in the pure case there is no exceptional support. Since \(\ell\mid v_h(B_n)\), the multiplier \(n/s\) cannot be a unit at \(h\), and thus \(h\mid n\). Either way \(h\) is a prime factor of \(m\), is \(1\bmod4\), and is strictly larger than the selected \(s\), a contradiction.

Every prime factor \(s\) of \(m\) is therefore \(3\bmod4\). Every prime \(h\mid B_s\) has exact odd order \(s\), is \(1\bmod12\), and is bigger than \(2s\). It cannot divide \(m\), the removed part of \(n\), or any prime in \(S\). Its valuation is unchanged in \(B_n\). Hence \(B_s\) is an \(\ell\)-th power, giving \(s=q\) by uniqueness. This proves \(m=q^a\). The same reasoning applies to \(B_{q^j}\) for \(1\le j\le a\): every prime in it has odd order a positive power of \(q\), and so is split and exceeds \(2q\). Its valuation is unchanged in \(B_n\), and is divisible by the full \(k\).

Finally the exponent descent requires \(\ell\equiv\pm1\bmod48\). For completeness the positive sign is incompatible with this inert \(q\). At \(\ell\equiv1\bmod48\) the Gaussian action and the Frobenius \(\pi\in\mathbf Z[i]\) are defined on the ordinary reduction. The order-\(q\) point \(G+(0,0)\) has Gaussian annihilator \((q)\), since \(q\equiv3\bmod4\) is inert. Frobenius is also the identity on the full two-torsion. Therefore \(\pi=1+2q(A+Bi)\), where \(B\ne0\) since \(N\pi=\ell\) is prime; this gives \(\ell\ge4q^2+1\). In contrast, choosing any \(h\mid B_q\) gives \(\ell\log(2q)<\ell\log h\le\log B_q\le 0.52q^2+1.5\) from the same height bounds. These inequalities contradict each other for \(q\ge3\). Hence \(\ell\equiv-1\bmod48\); the trace is zero at this prime, by cancellation under \(x\mapsto-x\), giving \(4q\mid\ell+1\).

## A congruent-number test on the exponent

Each surviving prime exponent \(\ell\) forces \(6\ell\) to be a congruent number. To see this, apply the Eisenstein descent at \(B_q\). It gives \(\gamma=(u+b\sqrt{-3})/2\) with \(u,b\) odd, \(v=N\gamma>1\), and \(\gamma^4+\bar\gamma^4=\ell s^2\) for a nonzero integer \(s\). The positive sign follows from \(\ell\equiv-1\bmod48\). Write \(t=(u^2-3b^2)/2\), \(d=ub\), and \(c=td\), all nonzero. Taking the sum and difference of \(\gamma^2,\bar\gamma^2\), and then of their squares, gives
\[
 t^2=2v^2+\ell s^2,\qquad 3d^2=2v^2-\ell s^2,\qquad
 \ell^2s^4+3c^2=4v^4.
\]
Consequently
\[
 (X,Y)=\left(-\frac{3\ell^2s^2}{v^2},\frac{9\ell^2sc}{v^3}\right)
 \quad\text{lies on}\quad Y^2=X^3-(6\ell)^2X.
\]
Its ordinate is nonzero. At 7 and 11 the curve has good reduction and trace zero, so its rational torsion has order dividing \(\gcd(8,12)=4\). Indeed reduction is injective on torsion over \(\mathbf Q_p\) at either of these odd primes, by the formal logarithm. The four rational two-torsion points exhaust the torsion, and the displayed point has infinite order. More precisely its two-descent squareclasses in the order \((X,X-6\ell,X+6\ell)\) are \((-3,-3\ell,\ell)\), since the last two coordinates are \(-3\ell t^2/v^2\) and \(9\ell d^2/v^2\).

For \(c_0=16,64\), let \(R_{c_0}(N)\) count all signed integral triples with \(8x^2+2y^2+c_0z^2=N\). The necessary direction of Tunnell's theorem for the even squarefree integer \(N=6\ell\) now gives the unconditional test
\[
                        R_{16}(6\ell)=2R_{64}(6\ell).
\]
For example, \(\ell=110927\) has \(\operatorname{ord}(G+(0,0))=2311\), but its representation counts are \(880,480\), excluding this exponent. At \(\ell=39503\) the order is \(823\) and the counts are \(512,256\), so this equality can hold at a prime satisfying the order requirement. Here \(G+(0,0)=(12,36)\), so both orders can be checked by a single prime-index multiplication. Both counts follow by enumerating \(0\le z\le\sqrt{N/c_0}\), \(0\le x\le\sqrt{(N-c_0z^2)/8}\) and testing whether \((N-c_0z^2-8x^2)/2\) is a square, with a factor of 2 for each nonzero coordinate. See J. B. Tunnell, *A classical Diophantine problem and modular forms of weight 3/2*, Invent. Math. 72 (1983), 323–334.
