# A quadratic character of Gaussian denominators on the congruent-six curve

Let \(E:y^2=x^3-36x\), \(G=(-3,9)\), \(K=\mathbf Q(i)\), and \([i](x,y)=(-x,iy)\). For \(S\in E(K)\setminus\{O\}\), write \(\mathfrak B(S)\) for the positive denominator ideal defined by \(v_{\mathfrak p}\mathfrak B(S)=\max(0,-v_{\mathfrak p}(x(S))/2)\). Define \(D_\alpha=N_{K/\mathbf Q}\mathfrak B([\alpha]G)\) for nonzero \(\alpha\in\mathbf Z[i]\). The positive integer \(D_\alpha\) depends only on \((\alpha)\) and is invariant under conjugation. For odd norm choose a generator \(\alpha=a+bi\) with \(a\) odd and \(b\) even. No coprimality of the coordinates is required. The rational point, its nontorsion property, and the odd-index coordinates follow from the [full quartic parametrization](abc_full_quartic_signature.md).

## Exact denominator identity

Write \(x([n]G)=A_n/B_n^2\) in lowest terms with \(B_n>0\) for \(n\ne0\). Set \((A_0,B_0)=(1,0)\). Then
\[
 D_{a+bi}=A_aB_b^2+A_bB_a^2.                                             \tag{1}
\]
In particular \(D_a=B_a^2\) at odd scalar indices. For even nonzero \(b\), \(A_b\) is a positive square by the duplication identity \(x(2S)=((x(S)^2+36)/(2y(S)))^2\). For odd \(a\) the real point \(aG\) lies in the bounded component, so \(-6<x(aG)<0\), whereas \(x(bG)>6\). This proves positivity of the right-hand side.

For a good place put \(d(S)=v_{\mathfrak p}\mathfrak B(S)\), \(P=aG\), \(Q=[i]bG\). For \(b\ne0\) the local addition identity is
\[
 v_{\mathfrak p}(x(P)-x(Q))+2d(P)+2d(Q)=d(P+Q)+d(P-Q).                    \tag{2}
\]
If both points are formal, write \(t=-x/y\) and \(u=-x(Q)/y(Q)\) for their parameters. The expansion \(x(t)=t^{-2}\) times an even unit series gives \(x(t)-x(u)=(u-t)(u+t)/(t^2u^2)\) times a unit. The formal group parameters of \(P\pm Q\) are \((t\pm u)\) times units, since inversion in this parameter is negation. If both points reduce to the same nonzero point of order two, translate by its rational two-torsion lift. The function \(x\) then has an even expansion with a unit quadratic coefficient, since \(x:E\to\mathbf P^1\) has simple ramification there in good odd residue characteristic. This gives the two factors \((u-t)(u+t)\) again. A common finite abscissa away from two-torsion is étale and gives just the one matching formal depth. With distinct finite reduced abscissas all terms vanish. With one formal point the negative abscissa valuation cancels its doubled depth. This proves (2) also when \(a,b\) have a common divisor. Now \(P+Q\) and \(P-Q\) are conjugate, so their denominator ideals multiply to \((D_{a+bi})\). Clearing the rational denominators on the left of (2) proves (1) away from 2 and 3.

At a place above 2 or 3 a formal \([\alpha]G\) would imply a formal \([N\alpha]G\), since \([i]\) preserves the integral formal subgroup. Every odd scalar index has denominator \(w\) prime to 6 by the quartic parametrization. Hence \(D_\alpha\) is a unit at both primes. In (1), \(B_a\) is prime to 6 and \(3\mid A_a\). The point \(2G=(25/4,-35/8)\) is formal at 2, hence \(B_b\) is even and \(A_b\) odd. At 3 the point \(2G\) has nonsingular reduction. Each multiple of it either is formal or reduces to one of the two smooth affine points with \(x=1\) on \(y^2=x^3\) over \(\mathbf F_3\). In both cases \(3\nmid A_b\). Thus the right-hand side is also prime to 6. For \(b=0\) the scalar identity is immediate from the ideal norm.

## A character modulo 193

Suppose \(13\nmid N\alpha\). As \(5^2=-1\bmod13\) and 2 generates \(\mathbf F_{13}^\times\), define
\[
 X=\operatorname{ind}_2(a+5b)\bmod3,\qquad Y=\operatorname{ind}_2(a-5b)\bmod3.
\]
With \(s(0)=s(2)=1\), \(s(1)=-1\), one has
\[
                          (D_\alpha/193)=s(X)s(Y).                          \tag{3}
\]
Here the left side is the Legendre symbol. Direct addition gives \(\operatorname{ord}_{193}G=26\). The odd index \(a\) always has a finite reduction. If \(26\nmid b\), (1) has the squareclass of \(x(aG)+x(bG)\bmod193\). If \(26\mid b\), (1) is a nonzero square modulo 193 because \(A_b\) is a unit square and \(B_a\) is a unit. This includes \(b=0\). These rules depend only on \(a,b\bmod26\). Each of the nine cubic-label pairs occurs at 16 of the 144 unit pairs with the specified parity. The signs by rows \(X=0,1,2\) and columns \(Y=0,1,2\) are

| \(X\backslash Y\) | 0 | 1 | 2 |
|---|---|---|---|
| 0 | + | − | + |
| 1 | − | + | − |
| 2 | + | − | + |

The [standard-library verifier](abc_congruent_six_cubic_packet_character.py) computes the 26 points, checks every residue pair, and verifies each cell and its size.

For a split prime \(q\), call its pair of cubic labels opposite and nonzero when it is \((1,2)\) or \((2,1)\) for a generator \(\lambda\mid q\) with the specified parity. This condition is independent of the generator sign since \(-1=2^6\bmod13\), and of the prime orientation since conjugation interchanges the labels. For \(\alpha=\lambda^j\bar\lambda^k\), the labels are \((u(j-k),-u(j-k))\) with \(u=1\) or \(-1\). Hence (3) is positive precisely when \(j-k\equiv0\pmod3\), independently of the orientation choice. The mixed ratio \(D_{j,k}D_{j-1,k-1}/(D_{j-1,k}D_{j,k-1})\) has the same character for \(j,k\ge1\). Here \(D_{j,k}=D_{\lambda^j\bar\lambda^k}\). The prime 5 qualifies since \(\lambda=1+2i\) has residues \(11,4\) and cubic labels \(1,2\).

For several such primes the raw character is positive precisely when the sum of their signed local exponents is zero in \(\mathbf F_3\). Replacing a chosen Gaussian prime by its conjugate interchanges the two local exponents and negates its label, leaving this sum invariant for a fixed ideal. Conjugating the entire ideal negates the sum and preserves its character.

## Density of the prime bases

The prime ideal theorem in fixed Gaussian ray classes gives uniformity on the units modulo 13 for the generators with \(a\) odd, \(b\) even. Indeed this choice fixes their residue to 1 modulo 2 up to sign; both signs give the same labels. In the split algebra \(\mathcal O/(13)=\mathbf F_{13}\times\mathbf F_{13}\) each cubic-index pair therefore has relative frequency \(1/9\). Imposing \(q\equiv5\bmod12\) on these split rational primes is the further condition \(N\lambda=2\bmod3\). It is independent by CRT at the fixed modulus \((2)(3)(13)\), and has probability \(1/2\) since the norm \(\mathbf F_9^\times\to\mathbf F_3^\times\) is surjective. The sign quotient acts trivially on these labels and norms. Inert rational primes contribute only degree-two ideals, of prime-ideal density zero, while each split rational prime contributes two conjugate degree-one ideals satisfying the same condition. The resulting absolute natural density among rational primes is \((1/2)(2/9)(1/2)=1/18\). Without the condition at 3, the absolute density is \(1/9\).

Every good prime dividing an odd scalar denominator has \(p\equiv1\bmod12\). In fact a point \(G\) of odd reduction order is a double, so the three two-descent characters require \(x(G)=-3\), \(x(G)-6=-9\), and \(x(G)+6=3\) all to be squares. Thus none of the prime bases selected with \(q\equiv5\bmod12\) can divide any \(D_\alpha\) of odd norm. This excludes ordinary lifting at any of these bases when applying Gaussian Möbius inversion.
