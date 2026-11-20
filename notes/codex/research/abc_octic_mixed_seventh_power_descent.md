# The rational points of \(6y^2=1-x^7\)

The only affine rational point is \((1,0)\). Put \(X=-6x,\ Y=6^4y\), giving the odd-degree genus-three curve \(H:Y^2=X^7+6^7\). We prove that its Jacobian has just two rational points. The proof uses the same odd-degree two-descent on the Jacobian as in the [fifth-power calculation](abc_octic_mixed_fifth_power_chabauty.md).

## Global two-descent

The étale factors of \(X^7+6^7\) are \(\mathbb Q\) and \(K=\mathbb Q(\zeta)\), where \(\zeta\) is a primitive seventh root of unity. The norm-square condition determines the rational component from the \(K\)-component of the descent map. The \(K\)-component for an affine divisor point is \(X+6\zeta\); the nonzero rational two-torsion class \(T=[(-6,0)-\infty]\) maps to \(-6\pi\), \(\pi=1-\zeta\). There are two rational squarefree polynomial factors, so \(J[2](\mathbb Q)\) has order two. Away from \(2,3,7\) the degree-seven polynomial \(X^7+6^7\) has separable reduction, so descent classes have even valuations there by the local divisor evaluation.

The absolute discriminant is \(7^5\). The Minkowski bound \((4/\pi_{\rm real})^3(6!/6^6)\sqrt{7^5}<5\) gives class number one: 2 has residue degree three and 3 residue degree six, so no integral ideal has norm \(2,3,4\). Two prime ideals over 2 have generators \(\lambda=1+\zeta+\zeta^2+\zeta^4=(1+\sqrt{-7})/2\) and its conjugate. Their product is 2. The prime 7 is totally ramified.

Put \(\eta_1=\zeta+\zeta^{-1}\), \(\eta_2=\zeta^2+\zeta^{-2}\). The units \(-1,\eta_1,\eta_2\) generate the unit squareclasses. The last two are units, for example from the minimal polynomial \(Z^3+Z^2-2Z-1\). Their signs under the three embeddings of the real subfield give the two independent even-weight sign vectors, and \(-1\) gives the odd-weight all-negative vector. A real unit that becomes square in \(K=K^+(\sqrt{-7})\) was already square in \(K^+\), since the alternative squareclass \(-7\) has odd valuation at the prime over 7 in \(K^+\). The three classes are therefore independent, and they exhaust the unit squareclasses by Dirichlet's theorem. All possible global components are generated modulo squares by
\[
 -1,\quad \eta_1,\quad \eta_2,\quad \lambda,\quad\bar\lambda,\quad 3,\quad\pi.
\]

At 3 and at 7 the septimic has two local factors, so \(J[2](\mathbb Q_p)\) has order two. Since \(p\) is odd, \(J(\mathbb Q_p)/2J(\mathbb Q_p)\) has the same order. At both places \(T\) has a nonzero class by its odd valuation.

At 3 the rational and real-subfield units have square residues, since they lie in the cubic subfield of the degree-six residue field. The unit \(\pi\) has square residue because its norm to \(\mathbb F_3\) is \(7\bmod3\). Each of \(\lambda,\bar\lambda\) has nonsquare residue because its norm is \(8\bmod3\). The unit part of \(-6\pi\) is square. Thus the exponents of \(\lambda,\bar\lambda\) coincide and we can replace the pair by 2. At 7, both \(\eta_j\) reduce to 2, a square; 2 itself is also a square. The units \(-1,3\) are nonsquare and the unit part of \(T=-6\pi\) is square. The exponents of \(-1\) and 3 consequently coincide. The remaining basis to be tested is \(\eta_1,\eta_2,2,-3,\pi\).

## The local image at 2

Write \(F\) for the unramified cubic extension of \(\mathbb Q_2\). The algebra \(K\otimes\mathbb Q_2\) is \(F\times F\), with the two embeddings sending \(\zeta\) to \(z,z^{-1}\), respectively, where \(z\) is a primitive seventh root in \(F\). Choose the embedding for which \(t=z+z^2+z^4\) is the even root of \(t^2+t+2=0\). Then \(z^3=t z^2+(1+t)z+1\), and Frobenius acts on \(F\) via \(z\mapsto z^2\). The septimic has three local factors, hence the local two-torsion has order four. The local quotient by doubling has order \(4\cdot2^3=32\), using the dimension of the formal group.

Here are five independent classes in this local quotient. For the first three take \(T\) and the points above \(X=1,14\) over \(\mathbb Q_2\). For the last two take traces to \(\mathbb Q_2\) of the curve-point divisor above \(X=14z^2\) or \(X=6z+2z^2\) over \(F\). Their ordinates exist because \(X^7+6^7\) is locally square, as verified below. For a rational \(X\), squareness over the odd-degree extension \(F\) implies squareness over \(\mathbb Q_2\). For a traced point each component is the product of \(X'+6z^{\pm1}\) over the three conjugates \(X'\).

In the following table each entry is the valuation modulo two followed by the lexicographically least unit vector in its square coset modulo 8, in the ascending basis \(1,z,z^2\). Squareness of a unit modulo 8 is equivalent to local squareness by Hensel's lemma. The verifier uses modulus \(2^{15}\) to retain at least three unit digits after valuation removal.

| Local input | First component | Second component |
|---|---|---|
| \(T\) | \((1;0,1,3)\) | \((1;0,2,7)\) |
| \(1\) | \((0;0,1,1)\) | \((0;0,1,3)\) |
| \(14\) | \((1;0,3,2)\) | \((1;0,3,7)\) |
| \(14z^2\) | \((0;0,2,7)\) | \((1;1,0,3)\) |
| \(6z+2z^2\) | \((0;0,3,2)\) | \((1;0,3,7)\) |

These pairs generate 32 distinct squareclasses, so they exhaust the image. Testing the 32 global candidates generated by \(\eta_1,\eta_2,2,-3,\pi\) leaves only bit vectors \((0,0,0,0,0)\) and \((0,0,1,1,1)\). These are the identity and \(T=-6\pi\). The injection of \(J(\mathbb Q)/2J(\mathbb Q)\) now proves rank zero.

## Odd torsion

At 5 and 11 the curve has good reduction. At 5 the maps \(u\mapsto u^7\) on the extensions of degrees \(1,2,3\) are permutations, by the order of 5 modulo 7. The point counts are therefore \(5^i+1\) in each degree \(i\), and the Weil polynomial is \(Z^6+5^3\). At 11 the same reasoning works in degrees one and two. Direct enumeration in the cubic extension gives the third count \(1464\). Newton's identities and reciprocity give the Weil polynomial \(Z^6+44Z^3+11^3\). Consequently the two Jacobian orders are \(126,1376\), with gcd two; neither residue characteristic divides the other order. Reduction on prime-to-residue-characteristic torsion gives \(J(\mathbb Q)=\{0,T\}\). Both classes are accounted for by \(\infty,(-6,0)\) on the embedded curve, proving the claim. [Standard-library verifier](abc_octic_mixed_seventh_power_verify.py)
