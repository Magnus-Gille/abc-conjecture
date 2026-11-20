# Reducing squareful denominators to prime indices and prime powers

For \(R=(-8,16)\) on \(y^2=x^3+16x^2+32x\), let \(B_n^2\) be the reduced denominator of \(x([n]R)\). An integer is squareful if every prime divisor has exponent at least two.

If \(B_n\) is squareful at an odd \(n>3\), its largest index prime \(L=P^+(n)\) must itself have \(B_L\) squareful. In particular \(L\ge13\), every prime factor of \(B_L\) exceeds \(10^7\), and at least one of those primes has valuation at least three on its first occurrence, at exact order \(L\). Indeed every prime of \(B_L\) exceeds \(L\) for \(L\ge5\), as in the [largest-prime descent](abc_odd_rank_squareclass_support.md). Thus each valuation persists unchanged at \(n\). If \(L=3\), the depth-one factor 11 of \(B_9\) persists at each \(3^a\) with \(a\ge2\). The indices 5, 7 and 11 each have simple prime factors. For \(L\ge5\) the complete prime-order scan found that *every* \(p\le10^7\) dividing such a \(B_L\) occurs to exponent one. Finally each \(B_L\) with \(L\ge5\) is nonsquare by the [quartic point classification](abc_octic_mixed_elliptic_chabauty_11.md).

An infinite sequence of squareful denominators at odd indices would have one of two consequences. If the largest index primes are unbounded, there are infinitely many squareful denominators already at prime indices. If they are bounded, there exists a fixed odd prime \(q\) such that, for every sufficiently large \(j\), *every* primitive prime of \(B_{q^j}\) has first valuation at least two and at least one has first valuation at least three. To see this, the index supports are bounded by a finite set \(S\). Some \(q\in S\) occurs to unbounded exponent. Each \(q^j\) then divides an index with squareful denominator. A primitive prime at order \(q^j\) exceeds \(\max S\) for all large \(j\) by Hasse. Its depth is unchanged at the chosen multiple. The [fixed-support primitive-prime covering argument](abc_primitive_denominator_twists.md) supplies a prime of odd depth at each sufficiently large \(q^j\). Neither possibility has been established.

## A lower bound for the indices having a prime of exponent one

More than 75.4723 percent of odd indices, in lower relative natural density, have a prime of exponent exactly one in \(B_n\). A simpler estimate already gives more than 73.121 percent. Let \(\mathcal L\) be the 22,716 distinct prime orders \(L\ge5\) occurring in the [complete scan through ten million](abc_odd_rank_squareclass_support.md). For each one let \(W_L\) be the product of the scanned primes of exact order \(L\), all verified to have first depth one. At odd multiples \(n\) of \(L\), at least one stays simple unless \(W_L\mid n\). Similarly at multiples of nine the three primes with product \(W_9=11\cdot67\cdot13411\) supply a simple prime unless \(W_9\mid n\). Conditional on oddness, the density of indices divisible by none of the source moduli is \((8/9)\prod_{L\in\mathcal L}(1-1/L)\) by CRT. By the union bound the relative density with a simple prime is at least
\[
 1-\frac89\prod_{L\in\mathcal L}(1-1/L)
   -\frac1{9 W_9}-\sum_{L\in\mathcal L}\frac1{L W_L}
 >0.73121.
\]
Here \(W_L\) is coprime to \(L\). The union bound needs no independence between the losses at different ranks.

For the stronger bound, take the simple first occurrences through \(10^7\) of orders \(q,3q\) for primes \(q\ge5\), together with order 9. These give 51,057 prime witnesses in total. The calculation uses both possible CM group orders and division polynomials modulo \(p,p^2\), as in the prime-order scan. For each \(p\), possible orders are tested in increasing order, after excluding order 3. Thus if order \(3q\) is recorded, its proper divisors have already been excluded.

Split odd indices according as \(3\nmid n\) or \(3\mid n\). In the first case keep only orders \(q\). In the second, an order \(q\) or \(3q\) supplies an edge \(q\to p\), while an order 9 supplies an edge \(3\to p\). Node \(v\ge5\) denotes the event \(v\mid n\), and node 3 denotes \(9\mid n\) conditional on \(3\mid n\). These events are independent by CRT and have probabilities \(1/v\). A witness is simple exactly when its parent event occurs and its own event fails. No witness has two parents, and each edge increases numerically. Thus the graph in each branch is a finite forest.

To compute the probability of missing every witness, let \(T_v\) be the probability of no violation (parent present, child absent) in the subtree at \(v\), and \(I_v\) that probability with \(v\) also present. Independence gives
\[
 I_v=v^{-1}\prod_{w\ {\rm child\ of}\ v}I_w,\qquad
 T_v=I_v+(1-v^{-1})\prod_{w\ {\rm child\ of}\ v}T_w .
\]
The miss probability in each branch is the product of \(T_v\) at its roots. Weight these probabilities by \(2/3,1/3\) respectively and take the complement. Computing with outward integer rounding at scale \(10^{24}\) places the relative density of the union between \(0.75472364631571526040\) and \(0.75472364631571526046\). This is the density for the specified finite list, hence a lower bound for the full set of indices having a simple prime. [Density verifier](abc_odd_rank_squareful_descent.py)
