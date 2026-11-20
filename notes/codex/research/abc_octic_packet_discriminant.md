# What torsion discriminants detect in a primitive packet

Let \(E:y^2=x^3-8x^2+8x\), \(A=(1,1)\), and let \(\psi_n\) denote its standard division polynomial. The discriminant of this integral Weierstrass model is \(2^{15}\). The argument below concerns primitive odd ranks and odd primes of good reduction.

## Simple roots and repeated integer values

Fix an odd integer \(r>1\). Over \(\mathbf Z[1/(2r)]\), the nonzero \(r\)-torsion points form a finite étale scheme. Two of their geometric abscissas coincide exactly when the points are equal up to sign. None of these points is a 2-torsion point, so the abscissa map is unramified there. Consequently \(\psi_r(X)\), whose leading coefficient is \(r\), has simple reductions at every odd \(p\nmid r\). Restricting to the abscissas of points of exact order \(r\) gives the same result. Equivalently, divide the monic normalization of \(\psi_r\) by the monic factors from proper divisors of \(r\). All the factors are integral after inverting \(2r\), and their pairwise resultants are units there. For a CM elliptic curve over a number field together with its endomorphisms, the same proof applies to abscissas of points of exact integral ideal annihilator \(I\) of odd norm, away from primes of bad reduction and those above \(2\operatorname N I\), in a local good integral model. Decomposition of torsion of exponent \(\operatorname N I\) into subsets of fixed annihilator commutes with reduction at these places.

For such a local monic factor \(F\) and integral abscissa \(a\) hitting a residue root, Hensel lifting gives a unique root \(\theta\) in the completed local ring with residue \(\bar a\). Then \(v(F(a))=v(a-\theta)\). Indeed, write \(F(X)=(X-\theta)G(X)\) and use \(G(a)\equiv F'(\theta)\ne0\) in the residue field. Separability controls collisions among distinct torsion points. The evaluation valuation measures the distance to the lifted torsion point. In particular \(p\mid F(a)\) implies \(p\nmid F'(a)\) at these primes, including when \(p^2\mid F(a)\).

Adding the evaluation point to the divisor produces
\[
   \operatorname{disc}((X-a)F(X))=\operatorname{disc}(F)\,F(a)^2 .
\]
This formula includes the original integer value as a factor.

## Numerical counterexample on the fixed point

Use \(r=34387=137\cdot251\) and \(p=205883\). This \(p\) is prime, splits in \(\mathbf Q(\sqrt{-2})\), and is prime to \(2r\). At \(A=(1,1)\), the division polynomial recurrence gives

| quantity | residue modulo \(p\) |
|---|---:|
| \(\psi_{137}(1)\) | 48637 |
| \(\psi_{251}(1)\) | 126586 |
| \(\psi_r(1)/p^2\) | 34977 |
| \(\psi'_r(1)\) | 132358 |
| \(\Phi_r(1)/p^2\) | 100540 |
| \(\Phi'_r(1)\) | 96176 |

Here \(\Phi_r=\psi_r/(\psi_{137}\psi_{251})\), a monic polynomial for this \(r\). The two smaller residues certify exact rank \(r\). Thus \(p^2\parallel\Phi_r(1)\) in the primitive packet of the fixed point, with \(p\nmid\operatorname{disc}(\Phi_r)\). The lifted torsion abscissa satisfies \(\theta\equiv1+106494p^2\bmod p^3\). For the derivative use \((x,y)=(1+p,1-5p/2)\) modulo \(p^2\), which satisfies the elliptic equation modulo \(p^2\). The finite difference divided by \(p\) gives the derivative of \(\psi_r(X)\) since \(r\) is odd. At either place above the split \(p\), exactly one factor in the decomposition by exact CM annihilator contains this contribution. Its root is the abscissa of the unique lifted \(r\)-torsion point reducing to \(A\). The example concerns the exact denominator packet of \(A\). The skew numerator \(U_N\) only has prime divisors that are \(1\bmod8\).

## Arbitrarily high first depth with one fixed CM kernel

The skew model has \(E':y^2=x^3+16x^2+32x\), \(S=(-4,-8)\), and \(\tau^2=-2\) acting by CM. At the seed \(N=3\), \(U_3=137\), and the odd denominator ideal of \([3-\tau]S\) has norm 137. Let \(\mathfrak p\) be the occupied place over 137. Since the ideal \(I=(3-\tau)\) has prime norm 11 and \(S\) remains affine modulo \(\mathfrak p\), its residue has exact annihilator \(I\). The initial formal depth is 1. [Skew denominator identity](abc_octic_mixed_skew_denominator.md)

For each \(j\ge0\) take an integer \(k\equiv1\bmod 11\) with \(v_{137}(k)=j\), possible by CRT, and set \(S_j=[k]S\). Its residue equals that of \(S\). Commutativity gives \([3-\tau]S_j=[k]([3-\tau]S)\). The formal logarithm is an isometry on the first formal group at this split odd good prime, so the new depth is \(j+1\). Since \([3-\tau]\) is étale and \(x\) is unramified at this nonzero odd-order torsion residue, this equals the valuation of the primitive monic kernel polynomial at \(x(S_j)\). Thus a single primitive CM kernel with fixed unit discriminant admits arbitrary valuations on a single rational cyclic subgroup as the evaluation point varies. Unbounded first depths for a fixed evaluation point as its annihilator varies remain unproved.

## A derivative that depends on the tested prime

At the abscissa \(a=1\), an arithmetic difference polynomial detects the second power. For \(F\in\mathbf Z[X]\) define
\[
       D_pF(X)=\frac{F(X^p)-F(X)^p}{p}\in\mathbf Z[X].
\]
Integrality follows from the Frobenius identity in characteristic \(p\). If \(p\mid F(1)\), then \(D_pF(1)\equiv F(1)/p\bmod p\). Therefore \(p^2\mid F(1)\) is equivalent to a common root at \(1\bmod p\) of \(F\) and \(D_pF\), giving the necessary condition \(p\mid\operatorname{Res}(F,D_pF)\). The polynomial and its resultant change with \(p\), and their evaluation at 1 reproduces the original test once \(p\) is specified.

## Exact factorization-free Fourier test on an odd packet

For any odd integer \(M>1\) the Jacobi symbol on all residues, including value zero at nonunits, gives a formula for the excess. Set
\[
     G(k)=\sum_{a=0}^{M-1}\left(\frac aM\right)\exp(2\pi i k a/M).
\]
Then
\[
    \frac{M}{\operatorname{rad}(M)}=\min\{k\ge1:G(k)\ne0\},
    \qquad
    |G(1)|=\begin{cases}\sqrt M& M\text{ squarefree},\\0&\text{otherwise}.\end{cases}
\]

To prove this take \(R=\operatorname{rad}(M)\) and \(c=M/R\). The Jacobi symbol has period \(R\) since each local factor \((a/p)^{v_p(M)}\) does. Summing \(c\) identical blocks with their additive phases gives \(G(k)=0\) unless \(c\mid k\). For \(k=c\) the sum is \(c\) times a primitive additive character sum on \(\mathbf Z/R\mathbf Z\). CRT factors the latter into sums on \(\mathbf F_p\) with nontrivial additive character. Each odd-exponent prime contributes a quadratic Gauss sum of modulus \(\sqrt p\). Each even-exponent prime contributes \(\sum_{a\ne0}e_p(ua)=-1\), \(u\ne0\). Hence \(G(c)\ne0\), giving both formulas. For arbitrary \(k\), any nonzero \(|G(k)|\) is at least 1 because each additional case of a trivial additive character contributes either 0 or \(p-1\). An approximation with rigorously bounded total absolute error below \(1/2\) therefore suffices for each zero test. Jacobi symbols are computable by Euclid's algorithm. Direct summation requires \(M\) terms per tested frequency. This yields an exact factorization-free criterion, with higher cost than trial division for deciding squarefreeness, and leaves growth of the fixed-seed primitive excess open.

Exact finite-field arithmetic also works. Choose a prime \(q\equiv1\bmod M\) and an element \(\zeta\) of order \(M\) in \(\mathbf F_q^\times\), and replace the additive phases by \(\zeta^{ka}\). The same block cancellations hold, and the factors at \(k=c\) remain nonzero: the square of a local quadratic Gauss sum is \(({-1}/p)p\), and \(q>M\). Searching for \(q,\zeta\) and verifying their properties can be done without factoring \(M\), for example by enumerating powers when checking the order. The verifier uses this variant for small packets.

## Exact radical with a cube-root sieve

An elementary bulk sieve gives a faster factorization-free algorithm for arbitrary positive \(M\). Take \(B=\lfloor M^{1/3}\rfloor\) and compute \(P=\prod_{p\le B}p\bmod M\) with a prime sieve. Form \(D=\gcd(M,P)\), and initialize \(L=M\). While \(g=\gcd(L,P)>1\), divide \(L\) by \(g\). Reduction of the product modulo \(M\) preserves all gcds used here, since \(L\mid M\). Then \(D\) is the product of the distinct small prime divisors and all prime factors of \(L\) exceed \(B\). There are at most two prime factors of \(L\), counted with multiplicity, since \((B+1)^3>M\). Consequently
\[
  \operatorname{rad}(M)=D
   \begin{cases}
      \sqrt L,&L\text{ is a perfect square},\\
      L,&\text{otherwise}.
   \end{cases}
\]

The algorithm never has to identify an individual prime dividing \(D\) or resolve a composite nonsquare residual \(L\). The gcd loop takes at most \(\log_2 M\) divisions. Sieving and modular products use \(M^{1/3+o(1)}\) bit operations, still exponential in the input bit length. When every prime divisor of the input belongs to a proven set of candidates, the primorial may omit ineligible primes. For an actual skew packet dividing \(U_N\), one may in particular retain only primes \(1\bmod8\).

[Standard-library check of the fixed-point example and small Fourier tests](abc_octic_packet_discriminant_verify.py)
