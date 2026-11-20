# Effective bounds on the prime support of near-square denominators

Let \(E:y^2=x^3-36x\), \(G=(-3,9)\), and write the reduced denominator of \(x([n]G)\) as \(B_n^2\), with \(B_n>0\). At positive odd indices write \(B_n=D_n z_n^2\), with \(D_n\) squarefree. For each odd prime \(q\) there is a computable integer \(t_q\ge1\) such that at every level \(h\equiv1\pmod{t_q}\) there is a prime of odd valuation that first divides the sequence at \(B_{q^h}\). In particular, for **any** finite set of allowed prime factors of \(D_n\), one can compute the complete list of eligible indices. The termination argument below uses the exact square classification and Dirichlet's theorem on primes in progressions.

## A periodic test for each prime base

The [square classification](abc_full_quartic_square_classification.md) gives \(D_q>1\). All primes dividing \(B_q\) are \(1\bmod12\) by the [quartic parametrization](abc_full_quartic_signature.md). At such a prime \(p\) the reduction of \(G\) has order exactly \(q\), since \(G\) is integral. Its cyclic group and the rational two-torsion generate a subgroup of order \(4q\). Consequently \(p\ge(2\sqrt q-1)^2>2q\), and \(D_q\) is prime to \(2q\).

Choose a prime \(\ell>3\) satisfying
\[
 \ell\equiv3\pmod4,\qquad \ell\equiv1\pmod q,\qquad
 \left(\frac{D_q}{\ell}\right)=-1.
\]
For existence, choose a nonresidue modulo one prime of \(D_q\) and choose 1 modulo its other primes. The Chinese remainder theorem combines those choices with the two congruences above. Quadratic reciprocity applies without a sign since the primes of \(D_q\) are \(1\bmod4\). Dirichlet's theorem gives primes in this reduced progression. In practice one may simply test successive primes in the first two congruences using the following elliptic test, without factoring \(B_q\).

On \(E_0:y^2=x^3+36x^2+36x\) take \(P=(-2,8)\). If \(j\) is odd and \([j]P\) has finite reduction at \(\ell\), the [slope formula](abc_full_quartic_square_denominators.md) gives
\[
 \left(\frac{B_j}{\ell}\right)
 =\left(\frac{8(6-x([j]P))}{\ell}\right).
\]
At identity reduction the sign is \(+1\). No odd \(B_j\) is divisible by \(\ell\), since its prime factors are \(1\bmod12\). Thus the sign depends only on \(j\) modulo \(T=\operatorname{ord}_\ell(P)\). The curve \(E_0\) is two-isogenous to \(E\) over \(\mathbf Q\). Indeed its two-isogenous equation has cubic \(x(x-24)(x-48)\), which scales to \(E\) by \(x=4(X+6),\ y=8Y\). Since \(\ell\equiv3\pmod4\), pairing \(x\) with \(-x\) in the character sum on \(E\) gives \(\#E_0(\mathbf F_\ell)=\ell+1\). In particular \(q\nmid T\), because \(\ell+1\equiv2\pmod q\). Set \(t_q=\operatorname{ord}_T(q)\). The signs at indices 1 and \(q\) differ, so \(T>1\).

For \(h\ge1\) with \(h\equiv1\pmod{t_q}\), the signs at \(q^{h-1}\) and \(q^h\) are the signs at 1 and \(q\), respectively. Divisibility of elliptic denominators makes \(B_{q^h}/B_{q^{h-1}}\) an integer, and its sign at \(\ell\) is negative. It therefore has a prime \(p_h\) of odd valuation. Every prime already in \(B_{q^{h-1}}\) has exact reduction order a nontrivial power of \(q\) and is greater than \(q\) by Hasse. Its exponent is unchanged on multiplication of the index by \(q\), by the elliptic formal group. Therefore \(p_h\) is new, of exact order \(q^h\), and
\[
 p_h\ge(2\sqrt{q^h}-1)^2>2q^h.
\]
These witnesses are distinct and their odd valuations persist at every higher \(q\)-power. For \(e\ge1\), put \(J=1+\lfloor(e-1)/t_q\rfloor\). Their product gives the explicit inequality
\[
 D_{q^e}>2^J q^{J+t_q J(J-1)/2}.
\]
Any auxiliary prime with nonzero signs at all odd indices and with \(q\nmid T\) works if its signs at 1 and \(q\) differ. The imposed progression is a way to guarantee finding one.

## Computing all indices over a specified prime support

Let \(S\) be the finite set and set \(Y=\max(\{2\}\cup S)\). Any eligible odd index \(n>1\) has largest prime divisor \(q_0\) with \(2q_0<Y\). Indeed every prime dividing \(D_{q_0}\) exceeds \(2q_0\), and hence cannot divide \(n\). Its odd exponent survives in \(B_n\), by formal lifting. For each odd prime \(q<Y/2\), perform the preceding search for \(t_q\). Take the smallest positive \(h_q\equiv1\pmod{t_q}\) with \(2q^{h_q}>Y\). If \(q^{h_q}\mid n\), the prime \(p_{h_q}>Y\) constructed above cannot divide \(n\) and its odd exponent survives in \(B_n\). Thus every eligible \(n\) divides the computable integer
\[
 N(S)=\prod_{q<Y/2,\ q\ {\rm odd\ prime}}q^{h_q-1}.
\]
Test its divisors by computing \(B_n\), dividing out all powers of primes in \(S\), and checking whether the remaining integer is a square. This returns exactly the eligible indices, including 1. There is no claimed practical running-time bound as \(Y\) grows.

## What the cofactor measures for abc

At the primitive triple \(a^4+3b^2=4w^4\), let \(C=4w^4\) and \(R=\operatorname{rad}(6abw)\). Here \(w=B_n\) for some odd \(n\). Since \(a\le\sqrt2\,w\) and \(|b|\le2w^2/\sqrt3\),
\[
 R\le6a|b|\operatorname{rad}(w)\ll w^3\operatorname{rad}(w)
 \le w^3\sqrt{D_n w}\cdot O(1).
\]
The last bound follows from \(w=D_n z_n^2\) and \(\operatorname{rad}(w)\le D_nz_n\). Thus if \(D_n\le w^{1-\delta}\) along infinitely many indices for some fixed \(0<\delta\le1\), those triples violate rational abc for each \(0<\varepsilon<\delta/(8-\delta)\). Indeed \(R^{1+\varepsilon}\ll w^{(4-\delta/2)(1+\varepsilon)}\), whose exponent is strictly below 4. Only finitely many primitive triples have bounded \(w\). The exact square classification settles the possibility \(D_n=1\); the [pointwise cofactor bound](abc_congruent_six_pointwise_cofactor_growth.md) still permits a fixed fractional deficit in \(\log D_n\) relative to \(\log w\).
