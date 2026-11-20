# Prime divisors above the quartic cutoff at odd scalar indices

Let \(R=(-8,16)\) on \(E':y^2=x^3+16x^2+32x\), and let \(B_n\) be the positive square root of the reduced denominator of \(x([n]R)\). At **every odd index \(7\le n\le509\)** and **every prime index \(7\le n\le1009\)**, there is a prime \(p>n^4\) for which \(v_p(B_n)\) is odd and the exact CM annihilator of the reduction of \(R\) is \((n)\). In particular its ordinary reduction order is exactly \(n\). The lower endpoints matter. We have \(B_3=9\) and \(B_5=281\), whose prime factors all lie below the respective quartic cutoffs. The certification uses exact integer arithmetic and does not require factoring large residuals. [Verifier](abc_odd_rank_quartic_cutoff.py) · [All computed rows](abc_odd_rank_quartic_cutoff.csv)

## Removing the proper annihilators

Put \(K=\mathbb Q(\tau)\), \(\tau^2=-2\). Every prime of \(B_n\) is odd and splits in \(K\) for odd \(n\). Indeed \(R\) has odd order on reduction at such a prime, hence is a double. The duplication abscissa on this model is a square, so \(-8=x(R)\) is a square modulo \(p\). All primes concerned are of good reduction. At either prime above \(p\), let \(I\) be the annihilator in \(\mathbb Z[\tau]\) of the reduction of \(R\). It contains \((n)\). If \(I\ne(n)\) then some prime ideal \(\lambda\mid(n)\) has \((n)/\lambda\subseteq I\). A generator of \((n)/\lambda\) therefore kills the reduction, which is equivalent to divisibility by that place of its abscissa denominator. Conversely that divisibility rules out \(I=(n)\). The annihilators at conjugate places are conjugate, since \(R\) is rational. [CM action, reduction and Frobenius](abc_octic_mixed_cm_prime_mass.md)

For a prime \(q\mid n\) inert in \(K\), the required multiplier is the rational integer \(n/q\), so remove all powers of primes common with \(B_{n/q}\). For split \(q=a^2+2b^2\), it suffices to use the norm of the denominator ideal of \([(n/q)(a+b\tau)]R\). This norm already detects both conjugate annihilators. In either case repeated gcd removes all powers in \(B_n\) on the relevant support. Call the integer retained after all such removals \(C_n\).

The code evaluates \([i+j\tau]R\) in exact arithmetic. If \([j]R=(u,v)\), its CM image has coordinates \((-(u+16+32/u)/2,\ v(1-32/u^2)\tau/4)\). Add \([i]R\) by the chord formula. Write the resulting abscissa as \((m+j'\tau)/w\), where \(w>0\) and \(\gcd(w,m,j')=1\). The integral ideal \((w,m+j'\tau)\) has norm \(\gcd(w,m^2+2j'^2)\), by the determinants of pairs of its four lattice generators. Therefore the denominator ideal of the abscissa has norm \(w^2/\gcd(w,m^2+2j'^2)\). Its square root has the same odd prime support, and the verifier checks its integrality. [Formula for the CM endomorphism](abc_octic_mixed_skew_denominator.md)

## Removing the primes through \(n^4\)

For a prime of \(C_n\) the CM Frobenius has norm \(p\) and is congruent to \(1\) modulo \((n)\). Hence
\[
 p=(1+na)^2+2n^2b^2,\qquad a\in\mathbb Z,\ b\ge1.
\]
A zero value of \(b\) gives a square. Conjugation permits the choice \(b>0\). The exact range for \(p\le n^4\) is obtained with an integer square root in each row \(b\). The verifier first discards norms divisible by an odd sieve prime \(s\le97\), using only \(s\nmid n\) and \(s<2n^2+1\). This loses no prime value, since every enumerated norm is at least \(2n^2+1\). It multiplies the surviving norms row by row and removes all prime powers shared with \(C_n\). A composite surviving norm is harmless because every one of its factors lies below the cutoff. The result \(H_n\) is therefore the exact product of the prime powers in \(C_n\) at \(p>n^4\). Direct trial division by all rational primes through \(n^4\) independently checks this step at every odd \(n\le35\).

The complete run at odd indices from 3 through 509 and prime indices through 1009 enumerated 71,989,916 norm values, of which 17,617,002 remained after the small-prime sieve. Every one of the 324 distinct tested indices \(n\ge7\) gives \(H_n>1\) and \(\lfloor\sqrt{H_n}\rfloor^2\ne H_n\). In this finite set, \(H_n>B_n^{0.35}\) and \(H_n>C_n^{0.85}\). The CSV bit lengths certify these inequalities using only \(2^{b-1}\le H_n<2^b\) and the corresponding bounds for \(B_n,C_n\). The bit-length comparison is closest for the first inequality at \(n=165\) and for the second at \(n=39\). The computations do not bound the exponent of any individual large prime from above.

| \(n\) | \(B_n\) bits | \(C_n\) bits | \(H_n\) bits | \(C_n/H_n\) |
|---:|---:|---:|---:|---:|
| 7 | 17 | 17 | 17 | 1 |
| 9 | 28 | 14 | 14 | 1 |
| 19 | 126 | 113 | 102 | 2,243 |
| 165 | 9,430 | 3,324 | 3,304 | 926,971 |
| 509 | 89,729 | 89,729 | 89,678 | 3,096,336,983,455,057 |
| 1009 | 352,600 | 351,901 | 351,877 | 22,393,747 |

The first two successful odd indices have \(H_7=117041\) and \(H_9=13411\), both prime. To reproduce the full CSV, run `python abc_odd_rank_quartic_cutoff.py`. If python-flint is available the verifier uses its exact integer and rational arithmetic. With the Python standard library alone a smaller check such as `python abc_odd_rank_quartic_cutoff.py --odd-limit 39 --prime-limit 53 --direct-limit 27` is quick.
