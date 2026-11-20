# Prime squares in the ninth cyclotomic value through the 32-bit prime range

Let \(A>B>0\) be coprime integers and let \(M=2^{32}-1\). Among all primes \(p\le M\) with \(p^2\mid\Phi_9(A,B)=A^6+A^3B^3+B^6\), the exact maximum of \(p/A^2\) is
\[
                     \frac{1549}{8100}=0.1912345679\ldots,
\]
attained only at \((A,B,p)=(90,67,1549)\). In particular, the scan found no positive example with \(p>A^2\). For \(\Phi_{18}(A,B)=A^6-A^3B^3+B^6\), the same search gives exactly one case with \(p>A^2\), namely \(\Phi_{18}(184,101)=2217\cdot122833^2\).

These conclusions include every base height for the specified prime range. They also give an unrestricted-prime result for \(A\le1353\) at index 9, since \(p^2\le\Phi_9(A,B)<3A^6\) and \(3\cdot1353^6<M^2\). At index 18 the analogous height cutoff is 1625, using \(\Phi_{18}(A,B)<A^6\) and \(1625^3<M\). [Earlier height-first census](abc_cyclotomic_large_square_twists.md)

## The nine positive cases in the wider search

The verifier searches the larger box \(A^2<16p\). Each row gives the exact factorization \(\Phi_9(A,B)=p^e m\) at the displayed prime. Every omitted pair has \(p/A^2\le1/16\), so comparing the nine rows proves the maximum.

| \(A\) | \(B\) | \(p\) | \(e\) | \(m\) |
|---:|---:|---:|---:|---:|
| 11 | 6 | 19 | 3 | 307 |
| 13 | 3 | 19 | 2 | 13,537 |
| 17 | 7 | 19 | 2 | 71,857 |
| 100 | 97 | 1,063 | 2 | 2,429,841 |
| 90 | 67 | 1,549 | 2 | 350,569 |
| 459 | 2 | 16,903 | 2 | 32,730,193 |
| 52,798 | 49,483 | 251,395,687 | 2 | 857,209,986,273 |
| 66,811 | 29,471 | 451,820,647 | 2 | 476,271,045,847 |
| 185,012 | 105,007 | 2,479,817,089 | 2 | 7,932,077,256,097 |

## Why the prime search is exhaustive

A prime dividing either form cannot divide \(AB\). The prime 2 divides neither form. At 3, put \(T=(\pm A)^3\), \(U=B^3\). If \(3\mid T^2+TU+U^2\), then \(T=U+3k\) with \(3\nmid U\), so \(T^2+TU+U^2=3(U^2+3kU+3k^2)\) has valuation one. At every other prime, \(p^2\mid\Phi_9(\pm A,B)\) holds exactly when \(\pm A/B\bmod p^2\) is a ninth root of unity of order 9 modulo \(p\). This follows from \((X^3-1)\Phi_9(X)=X^9-1\) and separability modulo \(p\). Thus the only eligible primes are \(p=1\bmod 18\).

For each such prime the code takes successive nonzero bases to the power \((p-1)/9\) until it obtains a residue \(y\) with \(y^3\ne1\). Cyclicity guarantees success. Put \(e=(y^9-1)/p\bmod p\). The unique ninth root above \(y\) is \(u=y+tp\), where \(t=-ey/9\bmod p\), by expansion to first order. The six primitive roots modulo \(p^2\) have exponents \(\pm1,\pm2,\pm4\) in \(u\). Interchanging \(A,B\) inverts either signed ratio, so only \(u,u^2,u^4\) need to be searched.

Write \(Q=p^2\), and let \(w\) be one of those three roots. For a signed numerator \(s\) and positive denominator \(t\) with \(s\equiv wt\bmod Q\), put \(j=(wt-s)/Q\). If \(s,t\) are coprime then \(j,t\) are coprime. Whenever \(s^2+t^2<Q\), the inequality \(2|s|t\le s^2+t^2\) gives
\[
             \left|\frac{w}{Q}-\frac{j}{t}\right|
               =\frac{|s|}{Qt}<\frac1{2t^2}.
\]
Legendre's continued-fraction criterion makes \(j/t\) a convergent for either sign of \(s\). Moreover, two candidate vectors of squared length less than \(Q\) have determinant divisible by \(Q\) and absolute determinant bounded by the product of their lengths, strictly less than \(Q\). Their determinant is zero, so they represent the same reduced signed fraction.

Take \(H=\lfloor\sqrt{16p-1}\rfloor\). For \(p>32\) every vector in the box satisfies \(s^2+t^2\le2H^2<32p<p^2\). The Euclidean algorithm on \((Q,w)\) produces signed errors of decreasing magnitude and convergent denominators of nondecreasing size. The first remainder at most \(H\) is the only possible candidate if its denominator is at most \(H\), and the search stops once the denominator exceeds \(H\). The only eligible prime below 33 is 19. The code enumerates all coprime pairs in its box directly.

## Reproduction

The segmented sieve enumerated **33,879,336** primes in the progression, an independently checked count. The default run emits all nine positive and twelve negative-sign cases in the wider box, with a flag for \(p>A^2\). It uses C++17 and includes a base-\(p\) multiplication fallback for compilers without 128-bit integers. [Prime-first verifier](abc_cyclotomic_ninth_prime_roots.cpp)

```sh
c++ -O3 -std=c++17 abc_cyclotomic_ninth_prime_roots.cpp -o ninth-roots
./ninth-roots
```
