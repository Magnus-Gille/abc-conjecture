# An effective bound for the overlap of Pell values

Let \(b_n+a_n\sqrt2=(1+\sqrt2)^n\), \(F_n=|F_{11}(a_n,b_n)|\), and \(g=(1+\sqrt2)^4\). Then
\[
  0\le \log\frac{\prod_{n=1}^N F_n}{\operatorname{lcm}(F_1,\ldots,F_N)}
     \ll N^2\frac{(\log\log N)^2}{\log N}\qquad(N\ge 16).
\]
In particular \(\log\operatorname{lcm}(F_1,\ldots,F_N)\sim 50\log(1+\sqrt2)N^2\). The implied constant is allowed to depend on this fixed recurrence. The estimate bounds the total logarithmic overlap, including multiplicities. It allows a prime square to make its first appearance in one term.

## The local inputs

Outside finitely many primes, \(F_n\) has a factorization into 50 simple targets \(g^n-u\) at any chosen place in a fixed splitting field, up to units. Fix a place over each rational prime. For each \(p^j\mid F_n\), exactly one target at this place satisfies \(g^n\equiv u\pmod {p^j}\). The order \(r=r_{p,j}\) of \(g\) there is independent of the place, since quadratic conjugation inverts \(g\). The pair \((p,j)\) occurs at most \(50(1+N/r)\) times. Also the sum of \(\log p\) over all pairs that ever occur and have \(r\le R\) is \(O(R^{3/2})\). For the latter bound, products \(g^i u^k\) in a square of side \(\lfloor\sqrt R\rfloor+1\) give two identical residues. Their quotient differs from 1 globally by multiplicative independence. Numerator norms for all possible differences have log product \(O(R^{3/2})\). This captures the maximal qualifying power of each prime. A dyadic sum bounds the total occurrence weight from \(r\le N\) by \(O(N^{3/2})\). Fixed omitted primes cost \(O(N\log(2N))\) by fixed-place logarithmic forms, more than sufficient here. [Local factorization and valuation bounds](abc_pell_full11_small_prime_mass.md) · [Independence of targets](abc_cm_pell_target_rank.md)

Suppose \(1\le n<m\le N\) share a layer \((p,j)\), with respective targets \(u,v\). For integers \(b>0,a\ge0,h=bn-am\), the valuation of
\[
                          u^b-v^a g^h
\]
at the chosen place is at least \(j\), with \(v_p(p)=1\). The difference is nonzero. For distinct targets this follows from independence of \(u,v,g\). For equal targets, independence of \(u,g\) leaves only \(a=b,h=0\), impossible for \(m>n\). The absolute norm of its numerator ideal has logarithm \(O(1+a+b+|h|)\) by the height inequality. For fixed \((a,b,h)\), sum this bound over the finitely many target pairs, omitting any identically zero difference. The result bounds the logarithmic weight of the **union** of layers captured by all pairs of indices with these coefficients. Each prime need only be counted up to its highest captured power. For \(r>N\) there are at most 50 occurrences per layer even before restricting \((a,b,h)\), so a union bound suffices. [Target representation and gcd proof](abc_cm_pell_target_gcd.md)

## Covering all slopes effectively

Write \(x=n/m\in(0,1)\). For sufficiently large \(N\), set
\[
 K=\left\lfloor\frac{\log N}{200(\log\log N)^2}\right\rfloor,\quad
 L=\left\lfloor\frac{\log N}{8\log(K+2)}\right\rfloor,\quad B=N^{1/8}.
\]
It suffices to consider \(K\ge2\), adjusting the absolute bound for the finite initial range. Read the ordinary continued fraction of \(x\) up to its first \(L\) partial quotients. Take the canonical finite representation for rationals. Denominators of convergents through \(L\) digits of size at most \(K\) are at most \((K+1)^L\le B\).

If the first digit greater than \(K\) appears within these \(L\) digits, let \(a/b\) be the preceding convergent, taking \(0/1\) if it is the first digit. All slopes with this particular first-large-digit prefix form a one-sided interval whose closure has length \(1/[b((K+1)b+b')]\), where \(0\le b'\le b\) is the preceding denominator. This follows by letting the remaining complete quotient range from \(K+1\) to infinity in the fractional linear map for the prefix. Endpoints can be included for upper bounds. Interiors for different stopping prefixes are disjoint. Consequently \(\sum 1/b^2\ll K\) over these prefixes. There are \(O(B^2)\) such prefixes since a rational endpoint has at most two finite continued fraction expansions. On an interval,
\[
       |h|=|bn-am|\le N/(Kb).
\]
Summing \(O(1+a+b+|h|)\) over all these integers \(h\) for this prefix costs \(O(b+N/K+N^2/(K^2b^2))\). Summing over the prefixes costs \(O(B^3+NB^2+N^2/K)\). If the continued fraction ends before \(L\) digits with no large digit, take \(a/b=x\) and \(h=0\). All such endpoints together cost \(O(B^3)\).

The remaining slopes lie in the closures of the depth-\(L\) cylinders with all digits at most \(K\). Their number \(J\) is \(O(B^2)\). If a parent ends at \(a/b\), its interval has length \(1/[b(b+b')]\). The fraction of its length removed at the next step is therefore \((b+b')/((K+1)b+b')\ge 1/(K+2)\). Hence the total remaining length \(t\le (1-1/(K+2))^L\ll (\log N)^{-2}\). Dirichlet approximation with denominator cutoff \(Q=\lfloor\sqrt N\rfloor\) gives \(1\le b\le Q\), \(0\le a\le b\) and \( |bx-a|\le 1/Q\). Each candidate \(a/b\) lies in the \(1/Q\) neighborhood of these cylinders. For each fixed \(b\), this permits \(O(bt+bJ/Q+J)\) integer numerators. There are \(O(tN+J\sqrt N)\) candidate pairs in all. For each, \( |h|\le N/Q\), so the sum of the numerator-norm bounds over \(h\) is \(O(N)\). The remaining contribution is \(O(tN^2+JN^{3/2})\).

Combining the covers, the small-period bound and the finitely many bad primes proves the estimate. A layer dividing \(k\) terms contributes exactly \((k-1)\log p\) to log product minus log lcm. Finally \(\log F_n=100n\log(1+\sqrt2)+O(1)\), giving the leading constant.

## What this says about an abc counterexample

Writing \(L_0=1\), \(L_n=\operatorname{lcm}(F_1,\ldots,F_n)\), the logarithm of the part shared with earlier terms is \(\log\gcd(F_n,L_{n-1})\). Its sum through \(N\) is exactly the logarithmic overlap above. In particular, for any fixed \(\delta>0\), at most \(O_\delta(N(\log\log N)^2/\log N)\) indices in \([N,2N]\) inherit a product of previously observed prime-power layers of size at least \(e^{\delta n}\). One prime can occur at a greater exponent than before. Its new layers belong to \(F_n/\gcd(F_n,L_{n-1})\), which can itself contain squares. The estimate leaves their size open.
