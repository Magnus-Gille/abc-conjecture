# A rank-one cubic-field elliptic curve for cubes on the quartic orbit

Let \(G=(-3,9)\) on \(E_6:y^2=x^3-36x\). At odd indices a cube denominator \(B_n=z^3\) gives a primitive solution
\[
                   a^4+3b^2=4z^{12}.
\]
Here \(a,z>0\), all three coordinates are odd and pairwise coprime, and \(3\nmid az\). [Full parametrization](abc_full_quartic_signature.md)

Write \(h=\sqrt{-3}\), \(K=\mathbf Q(h)\), \(\zeta=(1+h)/2\). The conjugate algebraic integers \(\alpha=(a^2+bh)/2\), \(\bar\alpha\) multiply to \(z^{12}\) and generate coprime ideals: a common prime would divide both their sum \(a^2\) and their product, contradicting \((a,z)=1\). The Eisenstein integers are a principal ideal domain. Thus \(\alpha=\eta\gamma^{12}\) with \(\gamma\in\mathbf Z[\zeta]\), \(\gamma\bar\gamma=z\), and \(\eta\in\mu_6\). Modulo the prime above 3 one has \(\eta=-1\) in the residue field, since \(\alpha\equiv a^2/2\), leaving \(-1,\zeta,\bar\zeta\) as units. Modulo 2, \(\gamma^{12}=1\) in \(\mathbf F_4\), whereas the coefficient of \(\zeta\) in \(\alpha\) is odd. Conjugation therefore permits \(\eta=\zeta\). In particular
\[
                 a^2=\zeta\gamma^{12}+\bar\zeta\bar\gamma^{12}.
\]

## Three coprime quartic factors

Let \(d=\exp(2\pi i/18)\), choose \(h\) with positive imaginary part, put \(M=\mathbf Q(d)\), and set \(F=M^+=\mathbf Q(\theta)\), \(\theta=d+d^{-1}\). Then \(d^3=\zeta\), \(\theta^3-3\theta-1=0\). Define \(\beta=d\gamma^4+d^{-1}\bar\gamma^4\in F\). Its three conjugates are obtained by multiplying \(d\) by the three cube roots of unity (extending the embeddings over \(K\)). The identity \(\prod_{j=0}^2 (\omega^j A+\omega^{-j}B)=A^3+B^3\) gives \(N_{F/\mathbf Q}(\beta)=a^2\); their sum is zero. A common prime of two conjugate factors would, after extension to \(M\), divide the two independent linear forms in \(\gamma^4,\bar\gamma^4\). Their determinant is a unit times \(\sqrt{-3}\). A prime above 3 is ruled out by \(3\nmid a\), while the two powers are relatively prime at every other prime. Hence \((\beta)\) is a square ideal.

The polynomial of \(\theta\) has discriminant 81 and \(\mathcal O_F=\mathbf Z[\theta]\): an index divisible by 3 would give field discriminant at most 9, contradicting the cubic Minkowski bound. The same bound with discriminant 81 is 2, and 2 is inert by reduction of the cubic, giving class number one. The signatures of \(-1,\theta,\theta'=2-\theta^2\) span all sign patterns. Indeed \(\theta,\theta'\) are conjugate units of norm one with distinct cyclic sign patterns, each having two negative entries. The unit group modulo squares has order eight by Dirichlet, so every totally positive unit is a square.

The signs of \(\beta\) comprise one positive and two negative signs by its positive norm and zero trace. Replacing \(\gamma\) by a sixth root of unity times \(\gamma\) cyclically permutes them. Therefore we may take \(\beta/\theta\) totally positive. Since \(\theta\) is a unit, principality and the unit signatures give \(\beta/\theta=v^2\) with \(v\in F\).

## Rational slopes on one quartic over the cubic field

Write \(\gamma=u+sh\) with rational \(u,s\). Put
\[
 \lambda=\frac{h(d-d^{-1})}{\theta}=-\frac{3}{2\theta+1},
 \qquad \lambda^2=12/\theta^2-3.
\]
Indeed \((d-d^{-1})(\theta^2-1)=d^3-d^{-3}=h\). For \(u\ne0\) set \(t=s/u\), \(V=v/u^2\). The fixed genus-one quartic and rational slope condition are
\[
            V^2=1+4\lambda t-18t^2-12\lambda t^3+9t^4,\qquad t\in\mathbf P^1(\mathbf Q).
\]
Finite \(t=0\) gives \(V=\pm1\); at \(t=\infty\) the values of \(V/t^2\) are \(\pm3\). A primitive solution of the original equation with \(t=0\) forces \(\gamma=\pm1\) by coprimality; \(t=\infty\) forces the prime above 3 into \(\gamma\), contrary to \(3\nmid z\) (the residue characteristic is odd, so half-integer coordinates cause no exception).

The quartic with base point \((0,1)\) is isomorphic to
\[
             J/F:\quad Y^2=X^3-36\theta^2 X.
\]
For finite nonzero \(t\), set
\[
 x_0=\frac{2(V+1)+4\lambda t}{t^2},\quad
 y_0=\frac{(x_0^2-36)t-4\lambda x_0+24\lambda}{2},\quad
 X=\frac{(x_0-6)\theta^2}{4},\quad Y=\frac{y_0\theta^3}{8}.
\]
Substitution gives the stated equation; the displayed formula for \(y_0\) recovers \(t\) rationally from the point away from the exceptional fibers. The four points at \(t=0,\infty\), in the order of the two positive and negative signs at each, map to \(O,P,T,P+T\) respectively, where \(P=(12,-12\theta\lambda)\) and \(T=(0,0)\). At \(t=0,V=-1\) this follows by Taylor expansion. At infinity, the positive leading coefficient gives \(x_0=6\), hence \(T\); the involution changing the sign of \(V\) sends each point \(Q\) to \(P-Q\), since the degree-two fibers are linearly equivalent. To use the isomorphic model \(Y'^2=X'^3-36X'/\theta^2\), put \(X'=X/\theta^2,Y'=Y/\theta^3\).

## Torsion and rank

At 19 and 71 the cubic field splits completely, and both primes are 3 modulo 4. The two group cardinalities are 20 and 72: in \(y^2=x^3+A x\) the summands of the quadratic-character sum at \(x\) and \(-x\) cancel. Reduction injectivity on prime-to-residue-characteristic torsion bounds the torsion by four. The full two-torsion is visible, proving \(J(F)_{\rm tors}=J[2]\); in particular \(P\) is nontorsion.

In the abscissa descent for \(Y^2=X^3+A X\) and its dual use \(A=-36\theta^2\) and \(A'=144\theta^2\). Valuations outside the primes over 2 and 3 are even in both abscissa images, by considering the valuations in the equation. The unique primes above 2 and 3 are generated respectively by 2 and \(\pi=\theta-1\) (its norm is 3 and the translate \(u^3+3u^2-3\) is Eisenstein at 3). Each candidate squareclass thus has a unique representative
\[
 e=(-1)^{s}\theta^i(2-\theta^2)^j2^k\pi^l,\qquad s,i,j,k,l\in\{0,1\}.
\]
On the dual all abscissas and the torsion class are totally positive. The signs of \(\pi\) equal those of \(\theta\), hence precisely the candidates \(s=j=0,i=l\) pass this dual test. At either remaining prime a necessary condition for \(e\) is local solubility of \(Z^2=eU^4+(A/e)W^4\) with at least one of \(U,W\) a unit. Normalizing that unit to 1 and reducing successively modulo \(16\mathcal O_F\) and \(9\mathcal O_F\) allows enumeration of the squares and fourth powers in rings of size \(16^3,9^3\). The two group sizes after the first test are at most 8 and 2, and after both tests they are at most 8 and 1. The script uses only the relation \(\theta^3=3\theta+1\) and exact integer arithmetic. Thus the usual two-isogeny rank formula gives
\[
           2^{\mathrm{rank}\,J(F)}\le 8\cdot1/4=2,
           \qquad \mathrm{rank}\,J(F)=1.
\]
[Standard-library rank verifier](abc_full_quartic_cube_rank.py) · [Output](abc_full_quartic_cube_rank.txt)

## All rational slopes and the cube classification

The roots of the cubic modulo 17 in the order \((3,4,10)\) give three reduction groups of orders \((16,20,16)\). Let \(\bar T\) denote the simultaneous image of the four global two-torsion points. The simultaneous image of \(J(F)\) lies in the union of the subgroups \(\langle U,\bar T\rangle\) that contain the simultaneous reduction of \(P\), with \(U\) ranging over all \(16\cdot20\cdot16=5120\) triples. Indeed one choice of \(U\) is the reduction of a generator of the free quotient. An exhaustive finite-group calculation finds 80 elements in this union. For each \(t\in\mathbf P^1(\mathbf F_{17})\), evaluate all three quartics and take every combination of square-root signs. The resulting points intersect the union only at \(O,P\) over zero and \(T,P+T\) over infinity. The signs agree across the three places on each surviving disk. Smooth reduction at 17 follows directly from the displayed elliptic equation and the separable quartic. [Independent exhaustive reduction and PARI local verification](abc_full_quartic_cube_17_audit.py) · [Output](abc_full_quartic_cube_17_audit.txt)

In the disk of \((0,1)\) write \(Q(t)\in J(F)\) for the image of a rational slope. At each of the three places the positively normalized square root is a convergent integral power series in \(t\), since its constant term is 1 and 2 is a unit. The displayed map has \(X=\theta^2 t^{-2}(1+O(t))\), \(Y=\theta^3 t^{-3}(1+O(t))\). Thus, for \(v_{17}(t)>0\), the formal parameter \(-X/Y\) has leading coefficient \(-1/\theta\). The elliptic logarithm has the same leading coefficient after composition. In detail, its derivative is an integral power series, and every term of degree \(j\ge2\) in the integral has valuation at least \(jv_{17}(t)-v_{17}(j)>v_{17}(t)\). In particular the three reductions of \(-\theta\log_J Q(t)/t\) all equal 1 when \(t\ne0\).

The reductions of \(P\) have orders \((4,10,4)\), so \(20P\) is simultaneously formal. The same PARI verifier over the three copies of \(\mathbf Q_{17}\) gives
\[
 \theta\bmod 289=(207,157,214),\qquad
 -\theta\log_J(20P)/17\bmod17=(11,13,7).
\]
For this computation the formal parameter agrees with the logarithm modulo \(17^2\). The rank-one result implies that the logarithm of any simultaneously formal global point belongs to the \(\mathbf Q_{17}\)-line through \(\log_J(20P)\), since an integer multiple of that global point is an integer multiple of \(20P\) modulo torsion. Multiplying the components by \(-\theta\), the reduction of this line has direction \((11,13,7)\), distinct from the direction \((1,1,1)\) forced by nonzero rational \(t\). Consequently the only point in that disk with rational slope has \(t=0\).

Changing the sign of \(V\) exchanges the two zero disks. The involution \((t,V)\mapsto(-1/(3t),V/(3t^2))\) preserves the quartic identity, preserves rational slopes, and exchanges the two infinity disks with the two zero disks. Thus the rational slopes on the cubic-field quartic are exactly 0 and infinity. The primitive restrictions proved above leave exactly
\[
              (a,b,z)=(1,\pm1,1),\qquad B_n\text{ a cube}\iff |n|=1
              \quad(n\text{ odd}).
\]
