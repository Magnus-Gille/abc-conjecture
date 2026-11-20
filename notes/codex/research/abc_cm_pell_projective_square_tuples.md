# Simultaneous square divisors at small rational height

Fix \(r\ge1\). For all but \(O_{F,r}(\pi(2Y)^{r-1})\) ordered tuples of distinct compatible primes \(Y\le p_i\le2Y\), **every** choice of projective roots of \(F=F_{11}\) modulo their squares has a simultaneous primitive representative \((a,b)\) with
\[
           \max(|a|,|b|)\ll_r D,\qquad D=\prod_{i=1}^r p_i .
\]
Here the compatible primes are the good primes at which \(F\) has a projective root. They include the primes splitting completely in its splitting field outside a finite set, so the exceptional proportion tends to zero even within the compatible tuples by Chebotarev. This supplies \(r\) large, simultaneous square divisors of the same full rank-eleven form value. Their valuations can exceed two. For almost every such tuple an additional difficulty remains in the whole-radical estimate. At any fixed polynomial height the norm radical costs at least \(D^{1-\epsilon}\) for any prescribed \(\epsilon>0\), with an exceptional set depending on that height range and \(\epsilon\). [Complete radical and the norm charge](abc_cm_pell_whole_triple.md)

## The short representative and its possible coordinate gcd

A choice of roots modulo the \(p_i^2\) defines a lattice of determinant \(D^2\) in \(\mathbb Z^2\). At each prime its defining condition is one surjective linear congruence imposed by the projective line, and the local indices multiply. A shortest nonzero vector \(v\) in the sup norm satisfies \(\|v\|\ll D\) by Minkowski. If a prime outside the tuple divides both coordinates, dividing by it would give a shorter lattice vector. Write \(v=g u\) with \(u\) primitive. The good tuples are those for which such a vector can be taken with \(g=1\) for every choice of roots.

For a squarefree product \(M\) of at most \(r\) compatible primes, a fixed projective class modulo \(M^2\) contains only \(O_K(1)\) primitive pairs of height at most \(KM\). Indeed two distinct directions in it have integer determinant divisible by \(M^2\). Their projective angular separation is at least a positive constant depending only on \(K\), since their Euclidean norms are at most \(\sqrt2 KM\). Each direction has at most two primitive representatives. Summing over roots still gives \(O_{F,r,K}(1)\) possibilities since each prime has at most \(\deg F=100\) simple roots. This bound also holds for the empty product.

For a witness with \(g>1\), partition the tuple into untagged primes with product \(M\), \(s_1\) primes occurring once in \(g\), and \(s_2\) primes occurring at least twice in \(g\). Since \(\|v\|\ll D\),
\[
                  \|u\|\ll M Y^{-s_2}.
\]
At each untagged prime \(q\), \(u\) represents the chosen root modulo \(q^2\). At each once-tagged prime \(p\), division of the linear congruence by \(p\) shows that \(u\) represents the chosen root modulo \(p\). In particular \(p\mid F(u)\).

If \(s_1>0\), fix all the untagged primes. The spacing bound gives \(O_{F,r}(1)\) possibilities for \(u\). The nonzero integer \(F(u)\) has size \(O_{F,r}(Y^{100r})\), hence only \(O_{F,r}(1)\) possible prime divisors in the interval. This gives boundedly many choices for all once-tagged primes. Allow the twice-or-more-tagged primes arbitrary choices. If \(s_1=0\), then \(s_2>0\) and an untagged prime must exist for large \(Y\), since otherwise \(\|u\|<1\). Fix all those untagged primes except one, with fixed product \(M'\). Now \(\|u\|\ll M/Y\ll M'\), so again only boundedly many \(u\) occur. The omitted prime divides \(F(u)\). In either case at least one prime has only boundedly many choices once the others under consideration have been fixed. The finitely many partitions of the coordinate positions give the asserted exceptional count.

## How often the same divisors can cover the norm radical

Put \(X=Y^r\) and let \(0<\lambda<1\), \(\beta>1\) be fixed. The number of ordered tuples in this interval for which *any* primitive pair of height \(H\) satisfies
\[
 \log H\le(\log X)^\beta,\qquad
 \operatorname{rad}|b^2-2a^2|\le X^\lambda,\qquad
 D\mid F(a,b)
\]
is at most
\[
                  X^{\lambda\max(1,\beta-1)+o(1)} .
\]
Thus the proportion tends to zero as long as \(\beta<1+1/\lambda\), even allowing only first-power divisibility. In particular the same scarcity applies to every polynomial height \(H\le X^K\) for fixed \(K\). Charging just the marked squares in the full-radical inequality supplies the factor \(D/\operatorname{rad}|b^2-2a^2|\). Individual tuples and repetitions in other factors remain available.

Write \(L=\log X\) and \(n=|b^2-2a^2|\le3\exp(2L^\beta)\). For a given \(n\), primitive elements \(b+a\sqrt2\) generating an ideal of norm \(n\) admit at most two choices of prime ideals above each split prime dividing \(n\). Indeed, if both primes divide the element then their product, the rational prime, divides both coefficients. The exponents at a chosen place are determined by \(n\). At nonsplit primes there is at most one ideal choice. Each principal ideal has \(O(\log(2H))\) generators of height \(\le H\) by the two real embeddings and the rank-one unit group. The total multiplicity is therefore \(O(2^{\omega(n)}\log(2H))=X^{o(1)}\) when \(\operatorname{rad}(n)\le X^\lambda\). Also each nonzero \(F(a,b)\) contributes at most \(O_{F,r}((1+L^{\beta-1})^r)\) tuples by size.

To count possible \(n\), for fixed \(t>1\) and real \(0<v<1\) the two bounds on \(n\) give
\[
 \#\{n\}\le (3e^{2L^\beta})^v e^{t\lambda L}
           \prod_{\ell\text{ prime}}
              \left(1+\frac{\ell^{-t}}{\ell^v-1}\right).
\]
The product has logarithm \(O_t(v^{-1/t})\), by bounding \(\ell^v-1\ge v\log 2\), majorizing the sum by one over all integers, and splitting at \((v\log2)^{-1/t}\). For \(v=L^{1-\beta}/\log L\) and fixed \(t>\max(1,\beta-1)\) this logarithm and \(vL^\beta\) are \(o(L)\). Sending \(t\) down to the endpoint proves the claimed exponent. [Related count for two smooth endpoints](abc_every_prime_square_gain.md)
