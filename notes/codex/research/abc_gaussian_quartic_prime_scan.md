# Testing the quartic prime cutoff on the congruent-number curve

Let G=(−3,9) on E:y²=x³−36x, and let Bᵣ be the positive square root of the reduced denominator of x([r]G). Among the 87 primes r≤1,000 with r≡3 modulo 4, **r=3 is the only one for which every first-occurrence prime is at most r⁴**. It has B₃=37. For every other tested rank, more than 99.4% of log Bᵣ comes from prime bases greater than r⁴, counting their multiplicities. [Rank-by-rank certificates](abc_gaussian_quartic_prime_scan.csv) · [Summary](abc_gaussian_quartic_prime_scan.json) · [Verifier](abc_gaussian_quartic_prime_scan.py)

| Upper bound on r | Prime ranks | Candidate norm representations | Prime candidates (summed by rank) | First-occurrence primes ≤r⁴ | Ranks having such a prime |
|---:|---:|---:|---:|---:|---:|
| 200 | 24 | 25,139 | 3,867 | 11 | 9 |
| 400 | 40 | 152,051 | 20,380 | 21 | 16 |
| 1,000 | 87 | 2,240,207 | 254,696 | 43 | 34 |

All 43 in-window primes have exact exponent one. 53 ranks had no in-window primes, 27 had one, five had two and two had three. The largest in-window prime was 213,767,642,113 at r=839. At r=131 the three primes are 344,269, 1,164,853 and 114,202,657, and the remaining cofactor has 10,935 bits. At r=7, the complete factorization B₇=14,281·140,449 independently illustrates the case with no in-window primes. The conclusion for factors above the cutoff uses no factorization of the remaining integers.

## Why this exhausts the prime bases

At a good prime of odd order the point is a double. Its abscissa differences −3,−9,3 are therefore quadratic residues, which forces p≡1 modulo 12. When r is inert in ℤ[i], ordₚ(G)=r forces the Gaussian annihilator to be (r). In particular the Gaussian Frobenius π has π−1∈(r). At odd reduction order the two-torsion conditions further imply that π=1+ar+ibr with 4 dividing a and 2 dividing b. Thus every possible prime p≤r⁴ can be found by enumerating integer a,b in the disk (1+ar)²+(br)²≤r⁴. Use b>0 to identify conjugates; b=0 gives a rational square. At r=3 the finite computation also admits all a,b and checks the unfiltered case. Each retained norm is submitted to FLINT's proven primality test. [Frobenius coefficient restriction](abc_gaussian_scalar_prime_scan.md)

## Exact denominator and mass comparison

The isomorphism over ℚ(√3) given by (x,y)↦(3x,3√3y) carries T=(−1,√3) on y²=x³−4x to G. Let fᵢ=ψᵢ(T) at odd i and fᵢ=ψᵢ(T)/(2√3) at even i. The first five values are 0,1,1,−37,−70. The standard division-polynomial recurrence runs over integers in this normalization, with (2√3)⁴=144. For odd r,
\[
 x([r]G)=-3-\frac{36 f_{r-1}f_{r+1}}{f_r^2}.
\]
The verifier computes the integer terms and checks gcd(fᵣ,36fᵣ₋₁fᵣ₊₁)=1 at every tested rank, proving Bᵣ=|fᵣ| and (Bᵣ,6)=1. For every tested r≤400 it independently reconstructs [r]G by exact affine arithmetic and checks the reduced denominator is Bᵣ². Every divisor prime of Bᵣ has first index r, since r is prime and G is integral.

For each rank, take the gcd of Bᵣ with the product of all enumerated prime candidates. For each hit, independently check [r]G=O over the field. Repeated computation of ψᵣ(G) modulo powers of p yields e=vₚ(Bᵣ). Direct divisibility of Bᵣ and the abscissa ladder modulo p²ᵉ⁺¹ verify that exponent. Writing Sᵣ for the product of these pᵉ, the exact quotient Bᵣ/Sᵣ equals 1 only at r=3. For each r>3 the integer inequality
\[
                       S_r^{500}<B_r^3
\]
gives log(Bᵣ/Sᵣ)>(497/500)log Bᵣ. This bounds logarithmic mass with multiplicities. The smallest measured fraction is approximately 0.99404648 at r=67.

The earlier [quadratic-cutoff search](abc_gaussian_scalar_prime_scan.md) found at most one in-window prime at each of the 39,321 inert prime ranks 3<r≤10⁶, always of exponent one. Since log Bᵣ>0.35r²−2.2>log(25r²) for r≥7, each of those ranks has a primitive prime greater than 25r² as well.

~~~sh
python abc_gaussian_quartic_prime_scan.py 1000 --rows /tmp/gaussian-quartic-primes.csv
~~~
