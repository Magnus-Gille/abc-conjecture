# The first accessible norm range for inert prime indices on the congruent-number curve

On E:y²=x³−36x let G=(−3,9) and write Bₙ² for the reduced abscissa denominator of [n]G. For every prime r≡3 modulo 4, the only pair with ordₚ(G)=r and p≤10r² is **r=3, p=37**. It has B₃=37, of exponent one. The exclusion for r>3 is unconditional, with no bound on r.

At the larger cutoff p≤25r², a finite exhaustive scan for prime r≡3 modulo 4 up to one million finds **921 first-occurrence pairs and no repeated first denominator prime**. Among them 920 have r>3, so this range tests the first possible family beyond the single exceptional small rank. All valuations were checked both by division polynomials modulo p² and by abscissa multiplication modulo p³. [Complete order list](abc_gaussian_scalar_prime_orders25.csv) · [Verifier](abc_gaussian_scalar_prime_scan.py)

## Universal lower bound

Odd reduction order forces G to be a double. The rational two-torsion descent therefore makes −3,−9,3 quadratic residues modulo p, hence p≡1 modulo 12. In particular reduction is ordinary and split in ℤ[i]. If the rational order is the inert prime r, the Gaussian annihilator is (r), since ℤ[i]/r is a field. Thus the Frobenius π of norm p satisfies π−1∈(r). The same reasoning below applies with any odd g coprime to 3 for which π−1∈(g), independently of the exact annihilator. [Gaussian annihilator and odd-order conditions](abc_congruent_six_gaussian_first_primes.md)

Write π=1+ag+ibg with b≠0. Full rational two-torsion gives π−1∈(2), so a,b are even. Since p≡1 modulo 12 there are two cases.

* If p≡1 modulo 24, then −1,2,3 and 6 are all squares. Every nonzero rational two-torsion point has a rational half by the same full two-torsion descent, so all sixteen four-torsion points are rational. Also p≡1 modulo 8 implies 4|b by reducing the norm modulo 8. Since 16 divides #E(𝔽ₚ)=(a²+b²)g², we obtain 4|a.
* If p≡13 modulo 24, then −1,3 are squares and 6 is a nonsquare. Each nonzero two-torsion point has a nonsquare abscissa difference ±6, so none has a rational half. The 2-Sylow group therefore has order four. Here p≡5 modulo 8 gives b≡2 modulo 4; the equality v₂((a²+b²)g²)=2 now forces 4|a.

If a≠0, then |a|≥4 and |b|≥2. If a=0 and 3∤g, then p≡1 modulo 3 forces 3|b, hence |b|≥6. In either case
\[
 p\ge(4g-1)^2+4g^2=20g^2-8g+1.
\]
Taking g=r rules out p≤10r² for r>3 and r≡3 modulo 4. Equality in this stronger bound does occur, for example at r=271 and p=1,466,653. For r=3 direct rational arithmetic gives x([3]G)=−1587/1369.

## Finite check and the larger norm range

| Upper bound on p | Prime ranks tested | Distinct norm candidates per rank, summed | Prime candidates | Exact-order pairs | Pairs of depth at least two |
|---:|---:|---:|---:|---:|---:|
| 10r² | 39,322 | 98,302 | 8,831 | 1 | 0 |
| 25r² | 39,322 | 275,260 | 26,619 | 921 | 0 |

For each r, integer square-root bounds enumerate all p=(1+ar)²+(br)² in the range, using b>0 to identify conjugates and retaining p≡1 modulo 12. The primality test is deterministic on 64-bit inputs. The program tests [r]G over the prime field at every candidate, cross-checks with the division polynomial, and tests the valuation of ψᵣ(G), which equals vₚ(Bᵣ) at these good primes. Projective differential addition independently checks the valuation of the abscissa denominator. For p≤25r² all 920 nontrivial pairs have b=2; 460 have a=−4 and 460 have a=4. The first two are (r,p)=(131,344269) and (271,1466653). [10r² output](abc_gaussian_scalar_prime_scan.json) · [25r² output](abc_gaussian_scalar_prime_scan25.json)

The earlier exceptional prime 211 has [53]G=(6,0), [2]G≠O and [106]G=O, hence exact order 106. Here ψ₁₀₆(G)/211²≡2 modulo 211. Thus 211 has depth two on this curve at an even index.

~~~sh
python abc_gaussian_scalar_prime_scan.py 1000000 --orders /tmp/gaussian-orders-10.csv
python abc_gaussian_scalar_prime_scan.py 1000000 --window 25 --orders /tmp/gaussian-orders-25.csv
~~~
