# Primitive solutions of \(a^4+3b^2=4z^{12}\)

With \(a,z>0\) and \(b\) a signed integer, the only primitive solutions are \((1,1,1)\) and \((1,-1,1)\). Equivalently, at a positive odd index the denominator \(B_n\) for \((-3,9)\) on \(y^2=x^3-36x\) is a cube precisely when \(n=1\).

The [Eisenstein descent and rank proof](abc_full_quartic_cube_descent.md) reduces this assertion to determining the rational slopes on the following quartic over the real cyclic cubic field \(F=\mathbf Q(\theta)\), where \(\theta^3-3\theta-1=0\). Put \(k=-3/(2\theta+1)\). The slope \(u\) must lie in \(\mathbf P^1(\mathbf Q)\), and its ordinate is in \(F\).
\[
 V^2=f(u)=1+4ku-18u^2-12ku^3+9u^4.
\]
The descent factors \((a^2+b\sqrt{-3})/2\) as a unit times a twelfth power. Its trace then splits into three pairwise coprime quartic factors over \(F\). Normalizing the signs of their real conjugates selects the one displayed quartic. The rank verifier bounds the ordinary two-isogeny descent images of its Jacobian by 8 and 1. [Rank verifier](abc_full_quartic_cube_rank.py)

On the model \(J:Y^2=X^3-36\theta^2X\), write \(P=(12,-12\theta k)\) and \(T=(0,0)\). The four known points at \(u=0,\infty\) are \(O,P,T,P+T\). The global group has rank one and torsion \(J[2]\). The following calculation proves that those four points exhaust the rational slopes.

## Simultaneous reduction at 17

The three roots of the defining cubic modulo 17 are 3, 4, and 10. Thus a global point reduces to a triple in elliptic groups of orders 16, 20, and 16. The orders of the three reductions of \(P\) are respectively 4, 10, and 4. We may use \(\langle P,J[2]\rangle\) for the full simultaneous reduction. In fact write \(P=mH+U\) for a free generator \(H\) and a torsion point \(U\). The abscissa squareclass of \(P\) is 3, whereas the four torsion images are \(1,-1,6\theta,-6\theta\). The class 3 differs from each of these. The real cubic field cannot contain \(\sqrt 3\); total reality excludes \(-3\) being a square, and \(\pm2\theta\) have odd valuation at the inert prime above 2. Since the abscissa map kills doubles, \(m\) is odd. Also \(5\nmid m\) since the middle reduction group has order 20 and the reduction of \(P\) has order divisible by 5. The only primes in the finite group orders are 2 and 5, proving the reduction assertion.

At each of the eighteen slopes in \(\mathbf P^1(\mathbf F_{17})\), enumerate the possible residues of \(V\) at the three places. For a finite nonzero slope transform them by the Weierstrass map in the descent proof. At zero and infinity the two local branches reduce to their indicated global seed points. The quartic is smooth at 17 (its four geometric roots are distinct, also from its diagonal trace form). The map and these branches have good reduction there, or equivalently one can use the displayed map at nonzero slopes and its integral local expansions at the seeds. Intersect the possible tuples with all \(jP+U\), \(0\le j<20\), \(U\in J[2]\). At slope zero the only tuples are the reductions of \(O,P\); at infinity they are those of \(T,P+T\). The intersection is empty at all other slopes. [Finite reduction and tangent verifier](abc_full_quartic_cube_split17.py) · [Independent enumeration allowing every possible generator](abc_full_quartic_cube_17_audit.py)

## A local uniqueness test

The map \((u,V)\mapsto(-1/(3u),V/(3u^2))\) is an involution because \(9u^4f(-1/(3u))=f(u)\). It interchanges the disks over infinity and zero and preserves rationality of the slope. Changing the sign of \(V\) then reduces the proof to the disk of \((u,V)=(0,1)\), where the corresponding point of \(J\) reduces to \(O\) at all three places. The uniformizer \(s=-X/Y\) satisfies
\[
                     u=-\theta s+O(s^2).
\]
Indeed the Weierstrass map has \(X=\theta^2/u^2+O(u^{-1})\) and \(Y=\theta^3/u^3+O(u^{-2})\), with integral coefficients at these places. The series for \(V\) is integral since \(2V\) is a unit at the seed.

Use the formal logarithm normalized by \(dX/(2Y)\). Its first term is \(s\), and it preserves the leading residue on \(17\mathbf Z_{17}\). For each root the following table gives the residue in the fourth column using a lift modulo \(17^2\).

| \(\theta\bmod17\) | \(\theta\bmod289\) | \(\operatorname{ord}(\bar P)\) | \(-\theta\log_J(20P)/17\bmod17\) |
|---:|---:|---:|---:|
| 3 | 207 | 4 | 11 |
| 4 | 157 | 10 | 13 |
| 10 | 214 | 4 | 7 |

For a quick check, write \(e=\operatorname{ord}(\bar P)\) and \(H=(e/2)P\). It reduces to a nonzero point of order two. Near its unique two-torsion lift the invariant differential is \(dY/(3X^2-36\theta^2)\), with unit denominator. Hence \(\log_J(eP)\equiv 2Y(H)/(3X(H)^2-36\theta^2)\pmod{289}\). Multiplying by \(20/e\) gives the table.

For a global point \(Q\) in all three identity disks, its triple of formal logarithms is a rational scalar multiple of that of \(20P\), since the global rank is one. For a nonzero scalar all three components have equal valuation. After division by that power of 17, the leading residues of the three slopes are a common nonzero scalar multiple of \((11,13,7)\). A rational \(u\) must have equal residues at this depth at every embedding. Therefore the scalar is zero; injectivity of the formal logarithm gives \(Q=O\). The involutions give exactly the two points over zero and the two over infinity. At zero the normalized Eisenstein integer \(\gamma\) is rational and coprimality forces \(\gamma=\pm1\). At infinity it is purely imaginary, forcing a factor above 3 into its norm, which is excluded. Substitution yields the two stated primitive solutions.
