# Exact qualities of the first Pell triples and a trace cofactor at \(S=3\)

On the rank-eleven Pell family, the complete primitive triples at \(n=0,-1\) have the following qualities. The radical counts primes in all three entries. The certificate gives the full prime-power factorization of each entry and a Lucas or elliptic-curve primality proof for every prime too large for short trial division. [Factorizations and primality certificates](abc_pell11_whole_quality_cert.json) · [Arithmetic verifier](abc_pell11_whole_quality.py)

| \(n\) | Digits in \(C\) | Distinct primes in \(ABC\) | \(C/\operatorname{rad}(ABC)\) | \(\log C/\log\operatorname{rad}(ABC)\) |
|---:|---:|---:|---:|---:|
| 0 | 100 | 26 | 141.65645547470548 | 1.022081424521163 |
| \(-1\) | 223 | 25 | 4.45797560485738 | 1.002930066971272 |

For example the 223-digit triple has \(A=w^4,\ B=v^4-w^4,\ C=v^4\), with
\[
 w=7039593355723976257760439640541152670862292524544414321,\qquad
 v=35334029702162500235454380942279330650212743082681056883.
\]
Its odd geometric support is squarefree even though its quality exceeds one.

## Which repetitions in the trace come from opposite orientations?

For \(n=\pm1\), \(S=b_2=3\), and the initial abscissas are \(-40/3\) and \(-8/3\). Let \(U_+,U_-\) be the oriented evaluations of the degree-483 support polynomial \(u\), and \(P(3)=3U_+U_-\) the whole trace value. Write \(\mathrm{odd}(N)=|N|/2^{v_2(N)}\). The individual odd parts are coprime to 3, and
\[
 \gcd(\mathrm{odd}(U_+),\mathrm{odd}(U_-))=65.
\]
The prime factors 5 and 13 each occur exactly once in both orientations and hence exactly twice in the trace. The only unresolved odd prime multiplicities at this trace value are in the following composite 98-digit cofactor of the positive orientation:
\[
 K=28693400368939696245597515919279214199686829477449778222783333699417098176108317556906162484499677.
\]
In particular,
\[
 \frac{\mathrm{odd}(P(3))}{\operatorname{rad}(\mathrm{odd}(P(3)))}
   =65\,\frac K{\operatorname{rad}(K)},\qquad
 \frac{C_1}{\operatorname{rad}(A_1B_1C_1)}
   =\big(1.08257675457661035642868\ldots\big)\frac K{\operatorname{rad}(K)}.
\]
The decimal coefficient is the exact rational number \(C_1/(K\prod_{p\in S_1}p)\), where \(S_1\) is the set of certified prime factors recorded at \(n=1\). Multiplying the recorded prime powers accounts for all of \(A_1,C_1\), and for precisely \(B_1/K\). The verifier checks that \(K\) is coprime to every recorded prime and that it fails the base-two Fermat test. It also evaluates both \(U_\pm\) and independently measures the odd parts against these factorizations. The computations leave the squarefreeness of \(K\) open. [Trace polynomial](abc_pell_whole_trace.md) · [Certificate including the \(n=1\) cofactor](abc_pell11_whole_quality_cert.json)

## Direct lower bounds at exact square primes of the Pell form

The first positive Pell index for the prime 65099 gives a primitive triple with **5,078,831 digits** and \(C/\operatorname{rad}(ABC)\ge1\,657\,149.99654467\). Every entry in the following table is certified by exact integer multiplication, gcd, division and square roots. [First square indices](abc_pell11_early_squares.md) · [Verifier with the gains option](abc_pell11_whole_quality.py)

| \(n\) | Digits in \(C\) | Certified divisor of \(T/\operatorname{rad}(T)\) | Lower bound on \(C/\operatorname{rad}(ABC)\) |
|---:|---:|---:|---:|
| 36 | 13,358 | \(3\cdot19\cdot109\) | 12,780.37652803 |
| 1213 | 449,468 | \(683\) | 175.61961147 |
| \(-3031\) | 1,122,902 | \(683\) | 175.61961147 |
| 3706 | 1,373,191 | \(13\cdot17\cdot1409\) | 160,134.74435410 |
| 13707 | 5,078,831 | \(3^2\cdot11\cdot65099\) | 1,657,149.99654467 |

Here \(T\) is an explicit integer containing the full radical. Put \(D=SH\) as in the twist family, write \(U/V\) in lowest terms for the untwisted abscissa at \([11]P\), and put \(h=U^2+16UV+32V^2\). At the displayed indices the numerical gcd of \(h^2,1024V^4\) is 1024. The verifier finds exact integer square roots \(L,W\) with
\[
 L^2=-2DUV,\qquad 32W^2=-h.
\]
Take \(T=2\,\mathrm{odd}(LW(U+16V)(U+8V))\). Every odd prime dividing \(UV\) divides \(L\). Every odd prime dividing \(h\) divides \(W\). The remaining possible odd divisors of the triple occur in \(U+16V\) or \(U+8V\) by its defining formulas. Thus \(\operatorname{rad}(ABC)\mid\operatorname{rad}(T)\). The prescribed excess in each row is measured in \(T\), and multiplying that excess by \(C/T\) gives the lower bound. At \(n=36\) the saving comes entirely from primes outside the full rank-eleven form. [Triple formulas](abc_cm_pell_whole_triple.md)

Running the verifier with no arguments checks the two full factorizations and the positive-orientation partial factorization using the Python standard library. The option \(\texttt{--gains}\) also rebuilds the trace at 3 and checks all five large triples using python-flint.
