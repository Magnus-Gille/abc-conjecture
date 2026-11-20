# Many primitive triples at a single square height

There is a constant \(\kappa>0\) and there are arbitrarily large square integers \(C\) at which at least
\[
 H(C)=\exp\!\left(\kappa\frac{(\log C)^{1/3}}{\log\log C}\right)
\]
distinct primitive unordered pairs \(A+B=C\) satisfy \(C/\operatorname{rad}(ABC)\ge H(C)\). Every smaller addend \(A\) in this construction is a square. Its radical can depend on the pair.

Take the first \(k\) primes, write \(y=p_k,\ q=16y\), and form the \(q^{2k}\) distinct integers \(\prod p_i^{e_i}\) with \(0\le e_i<q^2\). Their logarithms lie in an interval of length \(L=(q^2-1)\sum_{i\le k}\log p_i\). Split the increasing list into disjoint blocks of \(T=(4q)^k\) entries. There are precisely \((4y)^k\) blocks. Their spans are disjoint, so one block has log-width \(w\le L/(4y)^k\). The elementary prime-size estimate \(p_k=O(k\log k)\) gives \(L=O(k^3(\log k)^3)\).

For each pair in that block, direct an edge from \(P\) to \(Q\) when the exponent vector of \(Q\) is strictly smaller in at most \(k/2\) coordinates than that of \(P\). At least one direction qualifies, since the counts of strictly smaller coordinates in the two directions sum to at most \(k\). Choose one direction per pair. A vertex \(P\) has at least \((T-1)/2\) outgoing edges. Among its neighbors there are at most \(2^k(q^2)^{k/2}=(2q)^k\) possible values for \(g=\gcd(P,Q)\), by choosing the coordinates lowered and their new values. Accordingly \(\gg 2^k\) neighbors have the same \(g\).

Put \(u=P/g,\ v=Q/g\). The integer \(u\) is fixed throughout this collection and \(\gcd(u,v)=1\). For large \(k\), \(w\) tends to zero and \(0<|u-v|\le 2wu\) since \(|\log(v/u)|\le w\). Each neighbor yields
\[
 A=(u-v)^2,\qquad B=v(2u-v),\qquad C=u^2 .
\]
Both addends are positive and \(A<C/2\). Also \(\gcd(A,C)=1\), and at most two \(v\)'s give any given square \(A\). Thus \(\gg 2^k\) unordered pairs survive at this exact \(C\). Only the first \(k\) primes can divide \(uv\), so
\[
 \operatorname{rad}(ABC)\le \operatorname{rad}(uv)\,|u-v|(2u-v)
 \le 4y^k w C,\qquad
 C/\operatorname{rad}(ABC)\ge 4^k/(4L).
\]
Finally \(\log C\le 2L\), and the increasing lower bound on the number of distinct pairs forces the constructed heights to escape every bounded interval. The function \(h^{1/3}/\log h\) is increasing for large \(h\). Its value at \(h=\log C\le O(k^3\log^3 k)\) is \(O(k)\). This proves both lower bounds with a single sufficiently small \(\kappa\).

The guaranteed exponent \(\log H(C)/\log C\) tends to zero. Whether infinitely many of these heights admit even one pair with savings \(C^\delta\) for a fixed positive \(\delta\) remains open.
