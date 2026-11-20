# The radical of the index and the odd-exponent support of its elliptic denominator

Let \(B_n\) and \(D_n=\operatorname{sf}(B_n)\) be the denominator and its squarefree kernel on \(E_6:y^2=x^3-36x\), \(G=(-3,9)\). At every positive odd \(n\),
\[
  2\log 2\,\log\operatorname{rad}(n)
       \le \sum_{p\mid D_n}(\log p)^2\le(\log D_n)^2 .
\]
Thus on all squarefree indices, or on indices with prime multiplicities at most a fixed \(h\), one has \(\log D_n\ge\sqrt{(2\log2/h)\log n}\). The proof gives a second bound with the rightmost term replaced by \((\log P^+(D_n))\log D_n\) when \(n>1\).

For each odd prime \(q\) choose any prime \(f(q)\mid D_q\), which exists by the [square classification](abc_full_quartic_square_classification.md). Its reduction order is exactly \(q\), so \(f\) is injective and \(f(q)>2q\) by Hasse and full rational two-torsion. Every value of \(f\) is \(1\bmod12\). For good \(p\mid B_m\), the formal logarithm gives \(v_p(B_{km})=v_p(B_m)+v_p(k)\). [Orbit and local formulas](abc_full_quartic_signature.md)

For each prime \(q\mid n\), follow \(q,f(q),f^2(q),\ldots\) until the first *strictly downstream* vertex \(t\mid D_n\). At each step, if the current vertex \(u\) divides \(n\), then \(w=f(u)\) has odd valuation at \(B_u\). Either it divides \(D_n\), or the lifting rule forces \(w\mid n\). Termination follows from strict increase and finiteness of the set of prime divisors of \(n\). For each terminal \(t\), at most one source can have distance \(j\) from \(t\) for any given \(j\ge1\), by injectivity. Its size is less than \(t/2^j\). Thus its sources contribute to \(\log\operatorname{rad}(n)\) at most
\[
   \sum_{j\ge1}(\log t-j\log2)_+
       \le\int_0^\infty(\log t-x\log2)_+\,dx
       =\frac{(\log t)^2}{2\log2}.
\]
Summing over terminals proves the claim, including the possibility that a terminal is itself a source at another step.

## Joint contribution from selected prime powers

Write \(e_q=v_q(n)\), and take the set of primes \(q\mid n\) for which \(q\not\equiv1\pmod{12}\) or \(e_q\) is even. Then
\[
 D_n\;\ge\prod_{q\text{ in this set}} D_{q^{e_q}}.
\]
Indeed, every prime \(p\mid D_{q^{e_q}}\) has exact order a positive power of \(q\), and all these starting primes are distinct. Starting at \(p\) itself, stop if \(p\mid D_n\), and otherwise follow the same increasing map \(f\). An absent starting prime divides \(n\) by lifting from \(q^{e_q}\). Distinct paths could only meet if one start \(p'\) were strictly downstream of another, by injectivity of \(f\). The predecessor of \(p'\) would have to be its exact reduction order, hence the associated prime \(q'\). This predecessor is \(1\bmod12\), as every vertex from the initial primes onward has that residue. Thus \(e_{q'}\) would be even. If the predecessor is the initial prime of its path, it has odd valuation in the corresponding prime-power denominator, and its valuation in \(B_n\) is still odd: it differs from that depth by \(e_{q'}\), since its own rank is smaller than \(q'\) and belongs to a power of a different prime. If the predecessor was reached as the value of \(f\) at an earlier prime \(u\), it has odd depth in \(B_u\), again retained in \(B_n\) because its valuation gain is \(e_{q'}\). In either case that path must already stop at \(q'\), before \(p'\). Distinct terminals in \(D_n\) therefore dominate the full product of initial primes.
