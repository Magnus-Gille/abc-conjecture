# Perfect-power tests on all dyadic packets

For every \(n=2^k\), \(k\ge3\), the dyadic CM packet \(w_n\) is a quadratic nonresidue modulo 5. It is also a noncube modulo 7. A finite list of periodic modular tests excludes every perfect-power exponent \(2\le e\le150\) at **every** such index. For the ten packets \(16\le n\le8192\), the part supported on primes strictly greater than \(n^4\) is a non-perfect-power for **every** exponent. [Dyadic packet and ordinary first-depth identity](abc_dyadic_cm_largest_prime.md) · [Exact period and finite-exponent verifier](abc_dyadic_cm_power_characters.py)

## The square and cube tests

Write \(X=u^2,\ Y=v^2,\ W=X^2+16XY+32Y^2=w_n^2\). At \(n=8\), \((X,Y)=(961,196)\). Doubling sends
\[
(X,Y)\longmapsto\big((X^2-32Y^2)^2,\ 4XYW\big).
\]
Modulo 5 the pair \((1,1)\) is fixed and \(W=4\). Thus \(w_n\equiv\pm2\bmod5\) and at least one prime \(p\equiv2,3\bmod5\) occurs with **odd** first depth in each packet. Modulo 7 the pair \((2,0)\) is fixed and \(W=4\). Thus \(w_n\equiv\pm2\bmod7\), and some prime of each packet has first depth coprime to 3.

The same elementary orbit checks give \((w_n/13)=(w_n/17)=-1\) for all \(n\). The pairs modulo 13 cycle through \((12,1),(12,10),(1,1)\); modulo 17 the initial \((9,9)\) maps to the fixed \((8,8)\). At every listed state \(W^{(p-1)/4}=-1\bmod p\).

## All indices and exponents up to 150

For an odd prime exponent \(q\), choose auxiliary primes \(\ell\equiv1\bmod q\) and test the \(q\)-th power class of \(W=w_n^2\). To test \(q=2\), use the fourth power class of \(W\). Put \(d=q\) or \(d=4\), respectively, and \(\chi(z)=z^{(\ell-1)/d}\bmod\ell\). A permissible residue for a \(q\)-th power has \(\chi(W)\in\{0,1\}\).

For each \((q,\ell)\), the verifier iterates the finite state \((x,\chi(h))\), where \(x=X/Y,\ h=Y\) if \(Y\ne0\), or \(x=\infty,\ h=X\) otherwise. Homogeneity of the doubling polynomials of degree four and of \(W\) of degree two makes the next state and the tested character functions of the current state. Iteration stops at the **first repeated full state**, recording the initial segment and all allowed residue classes of \(j=k-3\) in the actual period. When two auxiliary places are needed, the generalized CRT tests all pairs of allowed classes for compatibility. Finite preperiods are checked directly. The sole permissible transient for the listed auxiliaries is \(n=8,\ q=71\), excluded by \(1<2273<2^{71}\). The verifier proves primality of each auxiliary and covers each prime \(q\le149\). Every exponent from 2 through 150 has such a prime divisor. The evidence for the infinite tails uses exact periods and the CRT, with no empirical cutoff.

## Unbounded exponents on the finite large-prime cofactors

Let \(S_n\) be the full part of \(w_n\) supported at \(p\le n^4\), and \(L_n=w_n/S_n\). The norm-disk certificate gives \(L_n>1\) and its number \(D\) of decimal digits for each tested \(16\le n\le8192\). If \(L_n=z^q\) for a prime exponent \(q\), then \(z>n^4=2^{4k}\), since any prime of \(z\) exceeds the cutoff. Therefore
\[
2^{4kq}<L_n<10^D<2^{10D/3},\qquad q<5D/(6k).
\]
For each prime exponent in this finite range the verifier finds a prime \(\ell\nmid S_n\) with a nontrivial power character on \(L_n^2\bmod\ell\), using at most \(k-3\) modular doublings. At \(n=8192\) this excludes all 19,959 prime exponents up to 224,250 with witnesses no greater than 27,534,907. The input cofactor has 3,498,307 digits and needs no factorization. [Small-support and digit certificates](abc_dyadic_cm_prime_support.md)

Consequently,
\[
\gcd\{v_p(w_n):p\mid w_n,\ p>n^4\}=1
\]
at every tested dyadic index from 16 through 8192. In particular one such valuation is odd; at each prime exponent \(q\) some such valuation is coprime to \(q\). If a tested cofactor has no prime of first depth one, its support must contain at least two distinct multiplicities, all at least two with gcd one. Exponents 2 and 3 illustrate why the gcd alone leaves that possibility open.

For all indices the square and cube tests carry the same limitation. If every depth in a packet exceeds one, its nonresidue modulo 5 forces some odd depth at least three. More generally, at all but finitely many indices the packet is coprime to any fixed auxiliary modulus \(M\), since different packets have disjoint prime support. The integer \(w_n^{1+\varphi(M)}\) then has exactly the same residue modulo \(M\) and the same prime support, while all its valuations exceed one. Also every unit modulo \(M\) is a \(q\)-th power for primes \(q\nmid\varphi(M)\). Thus a fixed set of residue tests alone cannot establish the existence of a first-depth-one prime or exclude all exponents at unbounded indices.

Finally there is a primitive quartic reformulation. The two integers \((u^2+8v^2\pm w_n)/2\) are positive, have opposite parity, and have product \(8v^4\). Any odd common prime would divide \(v\) and then \(u\), so the two integers are coprime. They are therefore \(a^4\) and \(8b^4\), with \(a\) odd, \(b\) even, \(\gcd(a,b)=1,\ ab=v\). In particular
\[
w_n=|a^4-8b^4|,\qquad u^2=a^4-8a^2b^2+8b^4.
\]
