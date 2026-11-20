# An abc excess in every locally primitive congruence class

Let \(M\ge2\) and let \((a_0,b_0,c_0)\) modulo \(M\) satisfy \(a_0+b_0=c_0\) and \(\gcd(b_0,c_0,M)=1\). There are infinitely many primitive positive triples \(a+b=c\) in that exact class for which \(c/\operatorname{rad}(abc)\gg_M\log c\).

One may consequently specify any finite set of moving primes, assign each independently to any of the three terms with *exact* valuation two, and prescribe the residues of the remaining units to any finite precision compatible with the sum. To force \(p^2\parallel a\), for example, specify \(a\equiv p^2 u\bmod p^{2+j}\) for \(j\ge1,\ p\nmid u\), a unit residue for \(b\), and \(c=a+b\) at that modulus. Combine the specifications by CRT. The bound below is uniform in the identities and allocation of the primes.

An example at small height is \(11^2+2^2\cdot17^3=3^2\cdot13^3\), or \(121+19652=19773\). The marked primes \(11,2,3\) have exact valuation two in their respective entries. The full radical is \(2\cdot3\cdot11\cdot13\cdot17=14586\), giving \(c/R>1.35\).

## Construction and an exact identity

Choose \(B\) as the least positive representative of \(b_0\) mod \(M\). Choose a positive \(C_0\equiv c_0\bmod M\) coprime to \(B\). Take distinct primes \(r,s\nmid MBC_0\), and put \(L=\varphi(M)\). The output takes the form
\[
 c=C_0r^{Ln},\qquad b=Bs^{Lj},\qquad a=c-b>0.
\]
It automatically has the requested residues and \(\gcd(b,c)=1\). Set \(K=\operatorname{rad}(BC_0)rs\). For positive \(n,j\) its radical satisfies the equality
\[
 R=K\operatorname{rad}(a),\qquad
 \frac cR=\frac{c}{Ka}\;\frac{a}{\operatorname{rad}(a)}.
\]
Every unfactored prime in \(a\) may be counted at its full multiplicity in the first factor.

Write \(\alpha=\log r/\log s\), \(\Delta=\log(C_0/B)/(L\log s)\). For every sufficiently large continued-fraction denominator \(Q\) of \(\alpha\) there are \(Q\le n<2Q\) and \(j=\lfloor n\alpha+\Delta\rfloor>0\) with
\[
 \frac1Q\le n\alpha+\Delta-j\le\frac4Q .
\]
Indeed, if \(h/Q\) is the corresponding convergent then \(|\alpha-h/Q|<1/Q^2\). For \(0\le i<Q\), the residues of \(Q\alpha+\Delta+ih/Q\) form an equally spaced grid on the circle. Pick a grid point in \([2/Q,3/Q]\). Replacing \(ih/Q\) with \(i\alpha\) moves it by less than \(1/Q\). Set \(n=Q+i\). Irrationality follows from unique factorization, so convergent denominators are unbounded.

Now \(\log(c/b)=L\log s\,(n\alpha+\Delta-j)>0\) and, for \(Q\ge4L\log s\),
\[
 \frac{L\log s}{2Q}\le\frac ac=1-e^{-\log(c/b)}
       \le\frac{4L\log s}{Q}.
\]
Also \(LQ\log r\le\log c\le3LQ\log r\) once \(Q\) dominates the fixed \(\log C_0/(L\log r)\). Consequently the gain certified by closeness on this explicit sequence has two-sided bounds
\[
 \frac{\log c}{12 K L^2\log r\log s}
 \le \frac{c}{Ka}\le
 \frac{2\log c}{K L^2\log r\log s}.
\]
This isolates the contribution of the unfactored part of \(a\) exactly. A genuine fixed positive exponent on this sequence would require \(a/\operatorname{rad}(a)\ge c^{\eta-o(1)}\) for some \(\eta>0\) when \(M\) and the chosen bases are fixed.

## Uniform cost of the twists

Let \(\mathcal P\) be the set of marked primes and, more generally, allow exact valuations \(e_p\ge1\). The local data have precision at least \(p^{e_p+1}\). Write \(F_a,F_b,F_c\) for the products of \(p^{e_p-1}\) over the primes assigned to each term, and \(F=F_aF_bF_c\). Then \(a/\operatorname{rad}(a)\ge F_a\) and \(\operatorname{rad}(BC_0)\le BC_0/(F_bF_c)\). In particular the preceding lower bound for the full radical gives
\[
 \frac cR\ge
 \frac{F\log c}{12 BC_0\,rs\,L^2\log r\log s}.
\]
For the exact-square prescriptions \(F=\prod_{p\in\mathcal P}p\). The factor for each marked prime appears irrespective of which of the three entries contains it.

One can take \(B\le M,\ C_0\le M^{1+o(1)}\), uniformly as \(M\to\infty\). Write \(C_0=C_1+Mh\) with \(1\le C_1\le M\). Primes common to \(B,M\) automatically avoid \(C_0\). At each other prime dividing \(B\) exactly one class of \(h\) is forbidden. If \(D\) is their squarefree product, inclusion-exclusion counts admissible \(0\le h<X\) by \(X\varphi(D)/D+O(2^{\omega(D)})\), with absolute error at most \(2^{\omega(D)}\). Thus \(X=2\cdot4^{\omega(B)}\) suffices. The bound \(\omega(B)\ll \log M/\log\log(3M)\) follows from \(\omega(B)!\le B\).

Take \(r,s\) as the least two primes absent from \(MBC_0\). The Chebyshev lower bound for the sum of prime logarithms implies \(r,s\ll\log(3M)\), since \(MBC_0\le M^{3+o(1)}\). Finally \(L\le M\), so the displayed bound gives \(c/R\ge FM^{-4-o(1)}\log c\), uniformly for these choices and all sufficiently large convergents of each class. For any prescribed sequence of changing moduli, marked primes, and compatible residue triples, the height can be chosen large enough separately at each step to give \(c/R\ge(\log c)^{1-o(1)}\) while meeting all the specifications.

## A height bound for reaching a given gain

For each fixed \(A>0\), the construction attains \(c/R\ge M^A\) with
\[
 \log c\le M^{O_A((1+\log\log(3M))^2)} .
\]
When \(\gcd(M,6)=1\) it attains that gain with \(\log c\le M^{O_A(1)}\). The constants are effective.

To see the first assertion, take \(T=M^{A+C}\) for an absolute constant \(C\) sufficiently large, increasing its value to cover small \(M\). Then every convergent denominator at least \(T\) exceeds the thresholds used above, and \(F\ge1\) suffices for the indicated gain. Indeed \(Q\ge T\) gives \(c/R\ge FQ/(4BC_0rsL\log s)\), and \(BC_0rsL\log s\le M^{O(1)}\). Let \(Q\) be the first convergent denominator at least \(T\), and \(q<T\) its predecessor with numerator \(h\). Then
\[
 |q\log r-h\log s|<\log s/Q.
\]
Matveev's bound for two positive rational bases, applied to \(r^q/s^h-1\ne0\), gives
\[
 \log Q\ll (1+\log r)(1+\log s)\log(2+q+h)+\log(2+\log s).
\]
The conversion uses \(|e^z-1|\le2|z|\) for \(|z|\le1\); if the displayed form is larger than one the bound for \(Q\) is immediate. Here \(h\le q\log r/\log s+1\), so the right hand side is \(O_A((1+\log\log(3M))^2\log M)\). The height bound now follows from \(\log c\le3LQ\log r\). [Matveev (2000)](https://doi.org/10.1070/IM2000v064n06ABEH000314)

For the second assertion take \(r=2,s=3\). Since \(6\) is invertible modulo \(M\), a representative of \(b_0\) coprime to 6 can be selected below \(6M\). In choosing \(C_0\), add the primes 2 and 3 to the finite set to avoid. The same inclusion-exclusion proof yields \(C_0\le M^{1+o(1)}\). Now both base logarithms in Matveev's bound are absolute constants and the claimed polynomial bound for the logarithmic height follows.
