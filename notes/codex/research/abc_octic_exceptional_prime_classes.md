# Where the two observed exceptional primes occur in the full mixed orbit

Use the full odd index \(N\ge3\), the point \(A=(1,1)\) on \(v^2=u^3-8u^2+8u\), and \(Q=[(N+1)/2]A\). Write its signed reduced slope as \(s/t\), let \(Y=s^2+2t^2\), and use the remaining factors of \(T_N\) as in the whole-radical calculation. The following table is exhaustive. [Full slope map](abc_octic_full_mixed_orbit.md) · [Whole radical](abc_octic_whole_radical_tail.md)

| Prime | Order of \(A\) | Period for odd \(N\) with factor labels | Residues by factor | Least admissible \(N\) |
|---:|---:|---:|---|---:|
| 4871 | 2436 | 4872 | \(s\) at 2435, 2437. \(t\) at 1, 4871. | 2435, in \(s\) |
| 205883 | 34387 | 68774 | \(Y\) at 34387. \(t\) at 1, 68773. | 34387, in \(Y\) |

The least indices for the denominator factor \(t\) are 4871 and 68773, respectively. The residue 1 gives further admissible indices after adding a period. The index \(N=1\) itself gives an infinite slope and is omitted. For the first prime, ignoring the factor label leaves just \(N\equiv\pm1\bmod2436\). In particular 4871 never divides the triple at an original-seed index \(N=3m\).

For the finite check, traverse \([n]A\) modulo each prime until its first return to the identity; the odd labels are \(N=2n-1\bmod 2r\) for order \(r\). The slope is represented by \([u+v:2(u-1)]\) away from \(O,\pm A\). Both \(O,A\) map to infinity. The point \(-A\) maps to \(7/4\) since its other preimage is \(2A\). Checking the six homogeneous factors at every projective slope gives the table. For the \(Y\) residue at 205883 the reduced slope is 49823.

The two labeled periods have gcd two and lcm 167,533,464. All twelve pairings of the odd residues admit one solution modulo this lcm. In increasing order their least positive representatives are
\[
1,\ 15095893,\ 30191785,\ 53574947,\ 68670839,\ 83766731,\
83766733,\ 98862625,\ 113958517,\ 137341679,\ 152437571,\ 167533463 .
\]
The **first admissible simultaneous occurrence is \(N=15{,}095{,}893\)**. It is 2437 modulo 4872 and 34387 modulo 68774. Here \(4871^2\parallel s\) and \(205883^4\parallel Y\), so both primes occur to exponent two in \(T_N\). Direct modular multiplication gives \((s/t)/4871^2\equiv2886\bmod4871\) and \(((s/t)^2+2)/205883^4\equiv130407\bmod205883\). The denominator \(t\) is a unit at both primes. These checks use division polynomials modulo the third and fifth powers of the respective primes and no large rational slope. [Standard-library verifier](abc_octic_exceptional_prime_classes.py)
