# Odd-valuation primes in intervals on the elliptic slice

For each of the two individual quartic kernels, every interval of \(N\) consecutive positive odd indices contains at least
\[
               c\frac{(\log N)^2}{\log\log(3N)}
\]
distinct primes of odd valuation, with an absolute constant for the slice. The product of those distinct primes has logarithm at least \(c'(\log N)^2\). The starting index is arbitrary, subject to \(n\ge3\).

There is also a statement about separation between occurrences. Let \(L=L(N)\ge2\) and \(L=o((\log N)^{2/3})\). At all but \(o(N)\) indices of every such interval, **each** quartic kernel has a squarefree divisor exceeding \(N^{1-\varepsilon}\) whose prime divisors are absent from both quartics at every other odd index within distance \(L\). Here \(\varepsilon>0\) is fixed and the error is uniform in the starting index. For fixed \(L\), at every sufficiently large index the two such divisors exceed any preassigned constant. In particular every sufficiently late block of \(T\) consecutive odd indices, with \(T\) fixed, supplies at least \(2T\) mutually distinct odd-valuation primes.

## Inputs and occurrence rates

Use \(J_n=|F_+(x_n,y_n)F_-(x_n,y_n)|/512\) and its squarefree kernel \(b_n=d_4(n)d_5(n)\). The two factors \(d_i\) are coprime squarefree positive integers prime to six. For each \(i\), the global number of indices with \(d_i(n)=d\) is at most \(C^{1+\omega(d)}\), by uniform Mordell–Lang on the genus-three twists and a two-descent rank bound. [Definitions and fiber bound](abc_eisenstein_slice_squareclass_census.md)

Write \(Q=(-8,-64)\) on \(E':v^2=u^3-576u\) and \(r_p=\operatorname{ord}(Q\bmod p)\) for \(p\ge5\). At the primes over \(p\) in a fixed splitting field, \(p\mid J_n\) is equivalent to \(nQ\) reducing to one of four fixed distinct sections \(S_1,\ldots,S_4\). Thus at most four residues modulo \(r_p\) can contribute. Among all primes that occur anywhere on this orbit the following two properties hold. [Marked divisors](abc_eisenstein_slice_marked_divisors.md) · [Order and denominator bounds](abc_eisenstein_slice_quartic_lcm.md)

* The sum of \(\log p\) over occurring primes of order at most \(R\) is \(O(R^2)\). Indeed a hitting residue \(n_0\bmod r_p\) admits \(1\le a\ll\sqrt R\), \(|s|\ll\sqrt R\) with \(s\equiv an_0\bmod r_p\) by Dirichlet approximation. The point \(sQ-aS_j\) has denominator divisible at the place of contact. It is nontorsion by the independence of the marked point and \(Q\). There are \(O(R)\) candidate points, and each denominator has absolute norm of logarithm \(O(R)\) by the canonical height.
* All primes dividing two values \(J_n,J_m\) with \(0<|m-n|\le L\) divide a positive integer \(G_L\) with \(\log G_L\ll L^3\). Take the product of good-prime denominator norms of \(gQ-S_j+S_k\), for \(1\le g\le L\) and all 16 ordered pairs. These points are nontorsion by the CM independence proved in the marked-divisor calculation, including the case where the two marks differ by torsion. Each norm has logarithm \(O(1+g^2)\).

If any \(K\) occurring primes are ordered by increasing \(r_p\), then \(r_{p_j}\gg\sqrt{j\log(2j)}\). Indeed the product of the first \(j\) distinct primes in this list is at least \((j+1)!\), and its log is \(O(r_{p_j}^2)\). For uniform \(n\) in a block of \(N\) consecutive odd indices write \(\beta_p=\Pr(p\mid d_i(n))\). Each of the at most four hitting residues contains at most \(1+2N/r_p\) indices in the block. For the Bernoulli entropy \(h(t)=-t\log t-(1-t)\log(1-t)\) and any fixed \(c\ge0\), it follows that
\[
  \sum_{p\in B}\{h(\beta_p)+c\beta_p\}
     \ll_c \sqrt{K\log(2K)}+K\frac{\log(2N)}{N}
                                                        \tag{1}
\]
for every set \(B\) of \(K\ge1\) primes. Primes never occurring contribute zero. To check the estimate, bound the summand by a constant times \(t\log(e/t)\) at \(t=\beta_p\). This last function increases on \([0,1]\) and is subadditive there. Up to absolute constants and truncation at one, its arguments are bounded by \(1/N+1/\sqrt{j\log(2j)}\). Summing gives (1).

## The number of distinct primes

With \(D=d_i(n)\) and Shannon entropy in natural logarithms, the fiber estimate gives
\[
 \log N=H(D)+H(n\mid D)
       \le H(D)+(\log C)(1+\mathbb E\omega(D)).
\]
The random integer \(D\) is specified by its prime-support bits, so entropy subadditivity bounds the right side by \(\log C+\sum_p(h(\beta_p)+(\log C)\beta_p)\). Apply (1) to all \(K\) primes in the block. If \(K\ge\sqrt N\) the assertion is immediate. Otherwise the second term in (1) is bounded and \(K\log(2K)\gg(\log N)^2\). This yields the claimed prime count and lower bound on their product.

## Growth of the part supported away from nearby indices

Set \(u(n)=d_i(n)/\gcd(d_i(n),G_L)\), \(v(n)=\gcd(d_i(n),G_L)\), and fix \(Z\ge1\). For fixed \(L,Z\), the global number of indices with \(u(n)\le Z\) is at most
\[
 C(1+C)^{\omega(G_L)}\sum_{j\le Z} C^{\omega(j)}
     \ll \exp\!\left(O\left(\frac{L^3}{\log(2L)}\right)\right)
                 Z(\log(2Z))^A.                                      \tag{2}
\]
Indeed each candidate is a product of one divisor of \(\operatorname{rad}G_L\) and an integer at most \(Z\), and the fiber estimate applies. The divisor-function majorant of integer order at least \(C\) bounds the last sum. The estimate for \(\omega(G_L)\) follows by comparing its radical with a factorial. This proves the all-sufficiently-large-indices assertion for fixed \(L\).

For growing \(L\), let \(A_0=\{u(n)\le Z\}\), with fraction \(f>0\) in the block. Conditional on this event, the entropy of \(n\) is \(\log(fN)\). The pair \((u,v)\) determines \(d_i\), so the fiber bound and subadditivity give
\[
 \log(fN)\le \log C+ H(u\mid A_0)+(\log C)\mathbb E(\omega(u)\mid A_0)
               +H(v\mid A_0)+(\log C)\mathbb E(\omega(v)\mid A_0).
\]
The two \(u\)-terms sum to at most \(\log\sum_{j\le Z}C^{\omega(j)}\), by nonnegativity of relative entropy against the distribution proportional to \(C^{\omega(j)}\). Also \(fH(v\mid A_0)\le H(v)\) by conditioning on the event indicator and \(f\mathbb E(\omega(v)\mid A_0)\le\mathbb E\omega(v)\). Apply (1) to the support of \(G_L\) using \(\omega(G_L)\ll L^3/\log(2L)\). The result is
\[
 f\big[\log(fN)-\log Z-A\log\log(2Z)-O(1)\big]
   \ll L^{3/2}+\frac{L^3\log(2N)}{N\log(2L)}.                        \tag{3}
\]
For \(0<\varepsilon<1\) take \(Z=N^{1-\varepsilon}\). If \(f\ge N^{-\varepsilon/4}\), the bracket exceeds \(\tfrac12\varepsilon\log N\) for large \(N\). When \(L=o((\log N)^{2/3})\) the right side is \(o(\log N)\), proving the claimed uniform exceptional fraction. Apply this separately for \(i=4,5\) and omit the union of the two exceptional sets. A prime of either \(u(n)\) divides no other \(J_m\) within the radius, by the definition of \(G_L\), and the two individual supports at the same index are disjoint.

Writing \(J_n=b_n q_n^2\), this yields \(q_n<\sqrt{J_n}N^{-1+\varepsilon}\) outside the exceptional sets, with the entire displayed saving supplied by primes isolated in that radius. On this slice \(\log J_n=8\widehat h(P)n^2+o(n^2)\). The interval estimates give no pointwise lower bound for \(\log b_n\) of comparable size. In particular an exceptional sequence with a fixed fractional deficit in \(\log b_n\) is compatible with these results. [Pointwise height criterion](abc_eisenstein_slice_squareclass_descent.md)

## Independence and concentration in affine squareclass spaces

For each choice \(D(n)=d_4(n),d_5(n)\) or \(b_n\), any affine subspace \(V\subset\mathbf Q^\times/\mathbf Q^{\times2}\) of dimension \(k\) obeys the uniform estimate
\[
      \#\{n\in I:D(n)\in V\}\ll N\sqrt{\frac{k+1}{\log(2N)}}           \tag{4}
\]
in every block \(I\) of \(N\) consecutive odd indices. There is no height or support restriction on the generators of \(V\). For the product \(b_n\) the same fiber estimate follows by summing that for \(d_4\) over divisors of \(b_n\), giving \(C(1+C)^{\omega(b_n)}\).

For \(2\le R\le\log(2N)\), take \(B\) to be all visiting primes of order at most \(R\). It has \(K\ll R^2/\log(2R)\) members, and (1) bounds its total entropy and mean support cost by \(O(R)\). With fraction \(f\) of the block supported on this \(B\), the conditional argument leading to (3), with \(Z=1\), gives \(f\log(fN)\ll 1+R\). Consequently \(f\ll N^{-1/2}+R/\log(2N)\). Restrict now to the rows \(n\) for which \(D(n)\in V\). Their prime-incidence matrix over \(\mathbf F_2\) has row and column ranks at most \(k+1\), accounting for an affine translate. Among its columns indexed by primes of order exceeding \(R\), choose a basis of columns. Any row using a high-order prime must use at least one of the basis columns, since all the other high-order columns are linear combinations. Each such column is nonzero on at most \(4+8N/R\) rows, by the same contact bound used in (1). Thus the fraction in \(V\) is at most
\[
 O\left(N^{-1/2}+\frac R{\log(2N)}+(k+1)\left(\frac1N+\frac1R\right)\right).
\]
When \(k+1\le\log(2N)\) take \(R\asymp\sqrt{(k+1)\log(2N)}\); the other cases are immediate. This proves (4). In particular any subset comprising a fixed positive fraction of the block has squareclass span of dimension \(\gg\log N\).

One can choose synchronized pairs of independent individual factors. Fix \(0<\varepsilon<1\) and \(R=c_\varepsilon\log N\) for a sufficiently small positive constant. The proof of (3) with \(B\) the primes of order at most \(R\) and \(Z=N^{1-\varepsilon}\) shows that both individual parts on primes of larger order exceed \(N^{1-\varepsilon}\) on at least three quarters of the block. Choose a qualifying index and one high-order prime from each of its two disjoint supports. Delete from the remaining indices every contact of either prime with \(J\); this removes at most \(8+16N/R\) indices per chosen pair. Continue greedily to obtain \(\gg_\varepsilon\log N\) indices. The two selected primes in each pair are absent from all later selected pairs and separate the two factors of their own pair. The corresponding squareclasses \(d_4(n),d_5(n)\) are jointly independent by this triangular incidence matrix. The resulting \(b_n\) are independent as well.

There is a complementary assertion for entire consecutive blocks. If \(t=o((\log N)^{2/5})\), then for all but \(o(N)\) odd starting indices in any interval of \(N\) consecutive odd indices, all \(2t\) individual classes in the following \(t\) consecutive odd indices are independent. Each has a divisor exceeding \(N^{1-\varepsilon}\) that is coprime to the other \(2t-1\) factors. Indeed (3) with \(L=2t\) bounds the bad fraction by \(O_\varepsilon(N^{-\varepsilon/4}+t^{3/2}/\log N+t^3/(N\log(2t)))\). Apply the bound to the interval extended by \(t\) indices to cover the final starts. Each bad index spoils at most \(t\) starts, giving \(o(N)\) by the stated growth condition.

The primes supplying the separated divisors can also exceed a growing numerical cutoff. Exclude every prime \(p\le Y\) in addition to those dividing \(G_L\). In (1) the extra cost is \(O(\sqrt Y+Y\log(2N)/(N\log(2Y)))\) for \(Y\ge2\), using \(\pi(Y)\ll Y/\log(2Y)\). Thus for any \(Y=o((\log N)^2)\) and \(L=o((\log N)^{2/3})\), on all but \(o(N)\) indices of every block of length \(N\), each of the two separated squarefree divisors exceeds \(N^{1-\varepsilon}\) and has all its primes above \(Y\). The pointwise exceptional-sequence limitation remains the one described above.
