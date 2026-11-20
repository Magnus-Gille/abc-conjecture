# Simple prime divisors above the quartic cutoff

For \(R=(-8,16)\) on \(y^2=x^3+16x^2+32x\), write \(B_n\) for the positive square root of the reduced denominator of \(x([n]R)\). **At 32 of the 35 odd indices from 7 through 75, an explicitly certified prime \(p>n^4\) divides \(B_n\) exactly once.** This includes every odd index from 7 through 35. The unresolved indices in this search are **37, 47 and 71**. At each of those three the exact part supported on primes above the cutoff is known to be nonsquare. [Odd-multiplicity census](abc_odd_rank_quartic_cutoff.md)

An explicit witness also exists at each of five larger prime indices. Each has ordinary first rank exactly \(n\).

| \(n\) | \(p\) with \(p>n^4\) and \(v_p(B_n)=1\) |
|---:|---:|
| 257 | 5,578,128,041 |
| 491 | 89,927,218,657 |
| 563 | 5,383,986,797,747 |
| 881 | 59,076,272,177,899 |
| 971 | 2,335,311,782,971 |

An independent check at \(n=971\) computed the reduced rational abscissa by the chord-and-tangent law over \(\mathbb Q\). Its denominator square root has 326,542 bits. For the stated \(p\) it gives \(B_{971}\bmod p=0\) and \((B_{971}/p)\bmod p=2{,}205{,}663{,}964{,}009\). Trial division through \(\lfloor\sqrt p\rfloor\) also confirms primality here.

Among the smaller 32 witnesses, 26 have ordinary first rank \(n\), including all certified prime indices. Exactly 24 witnesses have full CM annihilator \((n)\). The six inherited examples have index and first rank \((51,17),(57,19),(63,21),(65,13),(69,23),(75,15)\); direct verification gives valuation one at the stated index in every case. [All witnesses and primality certificates](abc_odd_rank_simple_large_cert.json)

## Verification

For each stored \(p\), the certificate proves primality by trial division through \(10^4\) for small leaves and a recursive Lucas criterion otherwise. For a larger node, it gives the complete prime factorization of \(p-1\) and a base \(g\) satisfying \(g^{p-1}\equiv1\pmod p\) and \(\gcd(g^{(p-1)/q}-1,p)=1\) for each prime factor \(q\mid p-1\). For any prime divisor \(s\mid p\), these conditions give \(g\) exact order \(p-1\) modulo \(s\), hence \(s\ge p\).

At the odd good prime \(p\), the fixed point \(R\) is integral. The division-polynomial formula for \(x([n]R)\) has denominator \(\psi_n(R)^2\). When \(\psi_n(R)\) vanishes modulo \(p\), the numerator \(x(R)\psi_n(R)^2-\psi_{n-1}(R)\psi_{n+1}(R)\) is a unit because the reduction order divides \(n\) and exceeds one. Consequently \(p\mid\psi_n(R)\), \(p^2\nmid\psi_n(R)\) certifies the exact exponent in \(B_n\). The verifier evaluates the standard division-polynomial recurrences modulo \(p^2\). To check first rank \(r\), it verifies \(p\mid\psi_r(R)\) and \(p\nmid\psi_{r/q}(R)\) for every prime \(q\mid r\). At \(n\le75\) it also recomputes the exact rational point \([n]R\) and tests the integer denominator directly. Run `python abc_odd_rank_simple_large.py` with the companion files in the same directory. [Standard-library verifier](abc_odd_rank_simple_large.py)

Candidate discovery used the earlier scalar-rank certificates, partial ECM or smooth-factor searches on individual denominator factors, and the smaller CM divisor at split prime index. For the last method, write \(n=a^2+2b^2\) and compute the odd norm of the denominator of \(x([a+b\sqrt{-2}]R)\), whose modulus is far smaller than \(B_n\). A prime found there can be verified against the original scalar point by the modular test above. This gave the five larger examples, all with annihilator norm \(n\). Complete factorization of a large scalar denominator is unnecessary for this certificate. [CM denominator calculation](abc_odd_rank_quartic_cutoff.md)
