# First-occurrence square denominators through ten million

Let E be given by Y²=X³+36X²+36X and P=(−2,8). Write X(nP) in lowest terms with positive denominator Bₙ². For a good prime p let rₚ be the order of P modulo p and eₚ=vₚ(Bᵣₚ).

**Exactly one of the 664,577 primes 5≤p≤10,000,000 has eₚ≥2. It is p=211, with rₚ=53 and eₚ=2.** Direct rational computation gives a 271-digit B₅₃ and
\[
 B_{53}/211^2\equiv149\pmod{211},\qquad
 \psi_{53}(P)/211^2\equiv117\pmod{211}.
\]
The two residues differ because the reduced denominator and the integral division polynomial may have different unit factors. [Complete scan output](abc_eisenstein_slice_denominator_scan.txt) · [Exact rational verification](abc_eisenstein_slice_denominator_verify.py)

The translation x=X+12 gives y²=x³−396x+3024, P=(10,8), with discriminant 2¹⁵3⁶. Translation preserves all reduced square denominators. An Eratosthenes sieve enumerates primes and supplies factorizations. For p≡3 modulo 4 use p+1 as a candidate annihilator. For p≡1 modulo 4 write p=a²+b², a odd and b even, and test p+1±2a. These candidates come from the 2-isogenous CM curve y²=u³−576u. Each accepted candidate is explicitly checked by scalar multiplication in E over the field. This direct check proves it is an annihilator regardless of how it was chosen. Successively removing prime factors whenever the smaller multiple still kills P then gives the exact rₚ. [Compiled scan](abc_eisenstein_slice_denominator_scan.cpp)

The first lift test computes ψᵣ(P) modulo p². The even division polynomials are normalized by 2y(P)=16, which is a unit at every tested prime. The initial normalized values at n=1,2,3,4,5 are 1,1,−1536,229376,18656264192. A binary recurrence uses a signed window of eight consecutive division polynomials. In good reduction, ψᵣ is locally a denominator factor and its abscissa numerator is a unit when rP specializes to the identity. Thus its valuation is the denominator depth. Every computed division polynomial also passes the check that p divides it.

Independently for **every** good prime, the scanner computes [rₚ]P in Jacobian coordinates modulo p² and compares whether Z vanishes. All proper positive prefixes in left-to-right multiplication of rₚ are smaller than the order of the reduced point; hence their Z-coordinates are units. A final mixed addition reducing to infinity adds two distinct opposite points, since y(P)=8 is nonzero modulo p. The corresponding formula has a unit slope numerator. For a final doubling from a nonzero two-torsion point, smoothness makes the tangent numerator a unit. The scanner checks the resulting X,Y are units and Z is divisible by p, before checking that both lift tests agree. The ranks over all primes sum to 1,244,747,771,858.

For the neighboring denominators of the [elliptic slice](abc_eisenstein_twelfth_elliptic_slice.md), the exceptional first-depth contribution of these primes to the logarithm of the squarefull part of |x²−y²| is therefore exactly
\[
 (\log211)\,\mathbf1_{n\equiv\pm1\pmod {53}}.
\]
On positive odd indices n≥3, the first two occurrences are n=105 and 107. Direct rational arithmetic gives (x²−y²)/211²≡169,177 modulo 211 respectively. Ordinary lifting at higher multiples and primes above ten million are outside this first-depth sum.

~~~sh
g++ -O3 -std=c++17 abc_eisenstein_slice_denominator_scan.cpp -o /tmp/slice-first-depth
/tmp/slice-first-depth 10000000
python abc_eisenstein_slice_denominator_verify.py
~~~
