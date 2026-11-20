# Excess multiplicity from small primes in a binary power difference

Fix \(n\ge1\). For positive coprime integers \(B<A\le H\), put \(F=AB(A^n-B^n)\) and
\[
 D_Y(F)=\prod_{p\le Y}p^{\max(v_p(F)-1,0)} .
\]
For fixed \(\delta,\lambda>0\) and every \(\varepsilon>0\),
\[
 \#\{(A,B): D_{H^{2-\lambda}}(F)>H^\delta\}
 \ll_{n,\delta,\lambda,\varepsilon}
      H^{\,2-\min(\delta,\lambda,2/3)+\varepsilon}.                    \tag{1}
\]
Thus a fixed positive power of \(H\) in the repeated-prime contribution below the cutoff occurs on a power-saving exceptional set.

## Projective roots and spacing

For any modulus \(m\ge1\), the condition \(m\mid F\) on primitive pairs uses at most \(2(n+2)^{\omega(m)}\) projective residue classes modulo \(m\). At a prime power \(p^k\), if \(p\mid A\), both \(B\) and \(A^n-B^n\) are units, so \(p^k\mid F\) is exactly \(A\equiv0\bmod p^k\). This gives one class. The case \(p\mid B\) gives one more. Otherwise \(A/B\) is a unit and must be an \(n\)-th root of unity. At odd \(p\) the cyclic unit group has at most \(n\) such roots, including when \(p\mid n\). At \(p=2\), the unit group for \(k\ge3\) is \(C_2\times C_{2^{k-2}}\) and has at most \(2n\) such roots. The same bound covers \(k=1,2\). Combining the local lists by the Chinese remainder theorem gives the claimed class count, since the extra factor of at most two occurs only at the prime two.

Any two pairs in one projective class have \(m\mid AB'-A'B\). Different positive primitive pairs give different fractions \(B/A\), so their spacing in \((0,1)\) is at least \(m/H^2\). Consequently
\[
 \#\{(A,B):m\mid F\}\ll (n+2)^{\omega(m)}(1+H^2/m).                  \tag{2}
\]

## Extracting a divisor of the excess

Write \(s=\min(\delta,2/3)\) and \(Y=H^{2-\lambda}\). First count any pair for which \(p^2\mid F\) at a prime \(H^s<p\le Y\). Applying (2) with \(m=p^2\) costs altogether
\[
          \ll_n H^{2-s}+H^{2-\lambda}.
\]
Here \(\sum_{p>H^s}p^{-2}\ll H^{-s}\); if the interval is empty its contribution is zero.

For each remaining pair counted in (1), every prime of \(D_Y(F)\) is at most \(H^s\). Multiply its prime factors, including repetitions, until the running product first reaches \(H^s\). The resulting divisor \(d\mid D_Y(F)\) satisfies
\[
                 H^s\le d\le H^{2s},\qquad d\,\operatorname{rad}(d)\mid F.
\]
The last divisibility follows prime by prime from \(v_p(d)\le v_p(F)-1\). Applying (2) with \(m=d\operatorname{rad}(d)\) gives two sums. For any \(0<\theta<1\),
\[
  \sum_{d\ge1}\frac{(n+2)^{\omega(d)}d^\theta}{d\operatorname{rad}(d)}
  =\prod_p\left(1+\frac{(n+2)p^{\theta-2}}{1-p^{\theta-1}}\right)<\infty .
\]
Thus the terms containing \(H^2/m\) cost \(O_{n,\theta}(H^{2-s\theta})\). The terms containing \(1\) cost \(O_{n,\varepsilon}(H^{2s+\varepsilon})\), since \((n+2)^{\omega(d)}\ll_{n,\eta} d^\eta\) for each \(\eta>0\). Taking \(\theta\) sufficiently close to one and using \(2s\le2-s\) proves (1).

For \(0<\delta\le\min(\lambda,2/3)\) and \(\lambda<2\), the exponent \(2-\delta\) in (1) is sharp up to the displayed \(\varepsilon\). Choose \(2H^\delta<2^k\le4H^\delta\) and take \(A=2^k a\) in \([H/2,H]\), with odd \(B\in[H/8,H/4]\) coprime to \(a\). The prime two alone supplies excess at least \(2^{k-1}>H^\delta\) and eventually lies below the cutoff. These conditions yield \(\gg H^{2-\delta}\) pairs. Indeed \(a,B\) range over intervals of lengths comparable to \(U=H/2^k\) and \(H\); Möbius inversion over odd common divisors gives a positive constant times \(UH\) with error \(O(H\log(2U))=o(UH)\).

## An angular version on a dyadic height interval

Let \(H/2<A\le H\) and put \(\vartheta=\min(B,A-B)/H\). For fixed \(0<s\le\min(\lambda,2/3)\) and every \(\varepsilon>0\), all but \(O_{n,s,\lambda,\varepsilon}(H^{2-s+\varepsilon})\) primitive pairs satisfy
\[
        \vartheta\ge H^{-s},
        \qquad D_{H^{2-\lambda}}(F)\ll H^s\vartheta .                 \tag{3}
\]
The pairs with \(\vartheta<H^{-s}\) cost \(O(H^{2-s})\) by counting the smaller leg. Divide the others into \(O(\log H)\) strips \(u\le\vartheta<2u\) with \(H^{-s}\le u\le1\). The fractions \(B/A\) in one strip lie in two intervals of total length \(O(u)\), contained within distance \(4u\) of either endpoint of \([0,1]\). In (2) the bound on that strip consequently becomes
\[
           O((n+2)^{\omega(m)}(1+H^2u/m)).
\]
Put \(G=H^s u\). Strips with \(1\le G<2\) cost \(O(H^{2-s})\) each by counting the smaller leg. Otherwise summing over \(G<p\le H^{2-\lambda}\) with \(p^2\mid F\) costs \(O_n(H^2u/G+H^{2-\lambda})\). If all the repeated primes in the cutoff are at most \(G\) and their excess exceeds \(G\), the previous extraction gives \(G\le d\le G^2\) and \(d\operatorname{rad}(d)\mid F\). Its cost in the strip is
\[
        O_{n,\eta}\!\left(H^2u\,G^{-1+\eta}+G^{2+\eta}\right)
               \ll_{n,s,\varepsilon} H^{2-s+\varepsilon/2}
\]
for sufficiently small \(\eta>0\), since \(H^2u/G=H^{2-s}\) and \(2s\le2-s\). The logarithmic number of strips is absorbed in \(\varepsilon\). This proves (3).
