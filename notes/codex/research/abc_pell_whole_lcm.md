# The lcm of the whole positive Pell geometric support

Let \(\varepsilon=1+\sqrt2\), \(b_j+a_j\sqrt2=\varepsilon^j\). Use the primitive degree-483 integer polynomial \(u(x)\) from the whole-triple trace construction, and put
\[
 s=b_{2n},\quad t=a_{2n},\quad x_+=-8(s+t)/s,\quad
 W_n=|s^{484}u(x_+)|=|sU_+| .
\]
Here \(W_n\) is the integer carrying the full geometric support of the positive-index primitive abc triple, with \(\log W_n=968n\log\varepsilon+O(1)\). Then
\[
 \boxed{\displaystyle
 \log\operatorname{lcm}(W_1,\ldots,W_N)
     =\left(482+\frac{16}{\pi^2}+o(1)\right)N^2\log\varepsilon .}          \tag{1}
\]
Thus the leading loss on passing from the product to the lcm is exactly \((2-16/\pi^2)N^2\log\varepsilon\). It comes entirely from two elementary Pell factors. The nonlinear factors keep their full leading product mass in the lcm. An lcm counts a prime power at its largest attained exponent, so squares at previously unused primes can still occur in that leading mass. [Definition of the geometric support and relation to abc quality](abc_pell_whole_trace.md)

## The 482 nonlinear targets

Write \(u(x)=x u_*(x)\), where \(u_*\) has degree 482; signs of integer polynomials are immaterial here. Then
\[
 T_n=|s^{482}u_*(x_+)|,\qquad W_n=8 b_{2n}\,a_{2n+1}\,T_n .
\]
Indeed \(a_{2n+1}=s+t\). The three factors come from distinct roots in the geometric support, and \((s,t)=1\), \(s\) is odd. The archimedean limit \(x_+\to-8-4\sqrt2\) avoids the zeros of \(u_*\), giving \(\log T_n=964n\log\varepsilon+O(1)\). Over \(K=\mathbf Q(\sqrt2)\), write \(g=\varepsilon^4\), \(\theta_\pm=-8\pm4\sqrt2\) and transform each root \(x\) of \(u_*\) into \(w=(\theta_+-x)/(x-\theta_-)\). Equivalently \(x_+=(\theta_-g^n+\theta_+)/(g^n+1)\). Hence \(T_n\), up to sign, a fixed constant and a power of the quadratic unit, is the product of \(g^n-w\) over these roots. The 482 targets are finite, nonzero and distinct.

The ten irreducible orbits over \(K\) have the following certified standardized third moments of \(\log|w|\) at the embedding \(\sqrt2>0\). For each orbit the variance is positive. Displayed values are rounded to six decimal places. The checker isolates all roots with complex interval arithmetic and verifies that all ten full skewness intervals are disjoint.

| Orbit degree | Signed standardized third moments |
|---:|---|
| 10 | \(0.514854,\ -0.514854,\ 0.133444,\ -0.133444\) |
| 50 | \(-0.271257,\ 0.271257,\ 0.292674,\ -0.292674\) |
| 121 | \(0.707312,\ 0.219184\) |

For the inference, take a Galois splitting field over \(K\) and apply all its automorphisms to a putative relation \(w^b=g^h z^a\) with \(b>0,a\ge0\); a root-of-unity factor makes no difference to the archimedean calculation. Each orbit's individual absolute logarithms occur equally often by orbit-stabilizer. With \(a=0\), positive variance excludes the relation. With \(a>0\), the two distributions would be carried to one another by a positive dilation and translation, preserving the signed standardized third moment. The disjoint intervals exclude this in different orbits, including those of opposite skew. Within one orbit its positive variance forces \(a=b\); its identical mean then gives \(h=0\). In particular every individual target is independent of \(g\). [Executable orbit and interval checks](abc_pell_whole_log_skew.py)

These are exactly the nonvanishing conditions in the proof of the [Pell lcm theorem](abc_cm_pell_lcm.md). For distinct indices \(n\le m\), two targets approximated to the same prime-power precision give a divisor of the numerator ideal of \(w^b-g^{bn-am}z^a\); the only potentially vanishing case \(a=b, bn=am\) is impossible. At a good prime each target gives at most one hit per multiplicative period. Individual independence supplies the total weighted bound \(O(R^{3/2})\) for visited layers of period at most \(R\), and the slope-cover argument bounds all remaining shared layers. The finitely many exceptional primes contribute \(O(N)\) over all indices by the fixed-prime spacing argument there. Therefore
\[
 \log\operatorname{lcm}(T_1,\ldots,T_N)=\sum_{n\le N}\log T_n+o(N^2)
                   =482N^2\log\varepsilon+o(N^2).                           \tag{2}
\]

## The two linear Pell factors

Let \(L_{\rm lin}(N)=\operatorname{lcm}_{1\le n\le N}\{a_{2n+1}, b_{2n}\}\). For \(d>1\) set \(C_d=|\Phi_d(\varepsilon,\bar\varepsilon)|\), the homogeneous cyclotomic polynomial evaluated at \(\varepsilon\) and \(\bar\varepsilon=1-\sqrt2\). This is a positive integer by reciprocality and conjugation. Then
\[
 a_m=\prod_{d\mid m,\ d>1} C_d,\qquad
 2b_{2n}=a_{4n}/a_{2n}
       =\prod_{d\mid4n,\ d\nmid2n} C_d .
\]
The union of all cyclotomic indices in this lcm consists precisely of odd \(3\le d\le2N+1\) and multiples of four \(4\le d\le4N\). Every odd \(d\) in range occurs by taking \(2n+1=d\). For the second sequence \(d\mid4n,\ d\nmid2n\) requires \(v_2(d)=v_2(n)+2\), and conversely choosing \(n=d/4\) realizes every multiple of four.

Replacing the product of the \(C_d\) in this union by the lcm changes its logarithm by \(O(N\log(2N))\), including the removal of the factor 2 above. To see this take an odd prime \(p\), a place of \(K\) above it, and \(r=\operatorname{ord}(\varepsilon/\bar\varepsilon\bmod p)\). Then \(p\nmid r\), and \(r>1\) since \(\varepsilon-\bar\varepsilon=2\sqrt2\) is a unit. For \(r\mid m\), binomial lifting in this unramified odd local field gives
\[
 v_p(a_m)=v_p(a_r)+v_p(m/r);
\]
for \(r\nmid m\) the valuation is zero. Equivalently by Möbius inversion, the positive valuations in the \(C_d\) are exactly the first value \(v_p(C_r)=v_p(a_r)\) and the values \(v_p(C_{r p^j})=1\), \(j\ge1\). If \(r\) belongs to the index union, its full initial valuation is present in an actual term of the lcm, since division by 2 is a unit at \(p\). If \(r\) is absent, all the contributing valuations are among the latter ones anyway. Thus the total logarithmic overcount over odd primes is bounded by \(\sum_{d\le4N}\sum_{p\mid d}\log p=O(N\log(2N))\). At 2 one has \(v_2(a_m)=v_2(m)\), by oddness of \(a_m\) at odd \(m\) and \(a_{2k}=2a_k b_k\) with \(b_k\) odd. It follows that \(C_{2^j}\) has valuation one for \(j\ge1\), and all other \(C_d\) are odd. The loss at 2 is at most \(O(\log(2N))\). Conversely every actual lcm term divides the full product of the \(C_d\) in the chosen union.

One has \(\log C_d=\varphi(d)\log\varepsilon+O(1)\), uniformly in \(d\). Indeed the Möbius expansion of \(\log\Phi_d\) has total error bounded by \(\sum_{k\ge1}|\log|1-(\bar\varepsilon/\varepsilon)^k||<\infty\). For the odd indices,
\[
 \sum_{d\le X,\ d\ {\rm odd}}\varphi(d)\sim\frac{2X^2}{\pi^2}.
\]
This follows from \(\varphi(d)=\sum_{k\mid d}\mu(k)d/k\), the sum of the odd positive integers up to \(Y\) being \(Y^2/4+O(Y+1)\), and \(\sum_{k\ {\rm odd}}\mu(k)/k^2=8/\pi^2\). For \(4\mid d\) write \(d=2^e k\) with \(k\) odd, \(e\ge2\); the corresponding constant is \((2/\pi^2)\sum_{e\ge2}2^{-e-1}=1/(2\pi^2)\). The tail in \(e\) is uniformly bounded by a convergent geometric sum, justifying the limiting constant. Substituting \(X=2N+1,4N\) respectively yields
\[
                    \log L_{\rm lin}(N)\sim (16/\pi^2) N^2\log\varepsilon.   \tag{3}
\]

## Combining the parts

Any odd prime power in \(L_{\rm lin}(N)\) has \(g\)-order at most \(2N+1\). Indeed \(p^j\mid b_{2n}\) makes \(g^n=-1\bmod p^j\), and \(p^j\mid a_{2n+1}\) makes \(g^{2n+1}=1\bmod p^j\). The first identity follows by multiplying \(2b_{2n}=\varepsilon^{2n}+\varepsilon^{-2n}\) by \(\varepsilon^{2n}\). For the second use \(\varepsilon^{2n+1}\equiv\bar\varepsilon^{2n+1}\bmod p^j\) and square their ratio. Thus the log gcd of the linear lcm and the nonlinear lcm in (2) is \(O(N^{3/2})\), by the nonlinear short-order estimate, with \(O(N)\) allowance for exceptional primes.

At an individual index \(\gcd(b_{2n},a_{2n+1})=1\) by the Pell norm and \(a_{2n+1}=s+t\). The nonlinear homogeneous form is coprime as a polynomial to the two linear factors \(s,s+t\), since \(u_*\) has nonzero leading coefficient and nonzero constant. Therefore their numerical common divisors at primitive \((s,t)\) are bounded by a fixed resultant. Alternatively their prime support lies in a fixed finite exceptional set, whose total log contribution to the lcm is \(O(N)\). Away from this set the lcm of the products has exactly the maximum of the two respective sequence valuations. This proves (1) from (2) and (3).
