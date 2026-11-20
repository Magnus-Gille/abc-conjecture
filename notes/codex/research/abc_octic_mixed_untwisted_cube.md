# The mixed cube sextic has only its two points at infinity

The smooth projective curve \(C:y^2=x^6-6x^5+6x^4+40x^3+12x^2-24x+8\) has exactly its two rational points at infinity. Consequently there are no coprime positive \(s,t_0\) with \(s\) odd, \(t_0\) even, \(s^2+2t_0^2\) a cube, and either \((s-t_0)^2+t_0^2\) or \((s+t_0)^2+t_0^2\) a square. In particular there is no sixth power \(s^2+2t_0^2\) on the mixed two-square locus. The argument treats signed \(t_0\) and the minus norm, which covers both choices.

The factors \(s\pm t_0\sqrt{-2}\) are coprime in the Euclidean ring \(\mathbf Z[\sqrt{-2}]\). The odd norm excludes the ramified prime and common odd prime divisors would divide both coprime coordinates. Since \(-1\) is a cube, we may write
\[
 s+t_0\sqrt{-2}=(a+b\sqrt{-2})^3,qquad
 s=a^3-6ab^2,\quad t_0=3a^2b-2b^3 .
\]
Here \(a\) is odd and \(b\) is even. Nonzero \(t_0\) implies \(b\ne0\). Write \(x=a/b\). The square condition gives a point on
\[
 C:y^2=x^6-6x^5+6x^4+40x^3+12x^2-24x+8.
\]

## A rank-one elliptic quotient

Over \(K=\mathbf Q(d)\), \(d^2=2\), put \(c=2-2d\) and
\[
 E:Y^2=X^3+(6+6d)X^2+6X+c^2,\qquad P=(0,c).
\]
The morphism from \(C\) to \(E\) is given by
\[
 X=\frac{2cx}{(x+d)^2},\qquad Y=\frac{cy}{(x+d)^3}.
\]
Direct substitution verifies the formula. For a derivation, set \(v=(x^2+2)/(2x)\) and \(h=y(x+d)/(4x^2)\). Then \(h^2=(v+d)(v^3-3v^2+8)\), and \(X=c/(v+d),\ Y=ch/(v+d)^2\). The two infinities of \(C\) map to \(\pm P\).

The elliptic curve \(E(K)\) has rank one, with \(P\) spanning modulo torsion over \(\mathbf Q\). Denis Simon's number-field 2-descent returns lower bound one and 2-Selmer dimension one. The base field and every auxiliary number field used by the descent were unconditionally certified with PARI's \(\texttt{bnfcertify}\), including the sextic field of discriminant 373248. Setting \(\texttt{LIMBIGPRIME}=0\) chooses deterministic local solubility tests. The script verifies the input source hashes and the exact rank result. Independently, the two quotient maps from \(C\) to \(E\) and its conjugate have pullbacks of their invariant differentials equal to \((d-x)dx/y\) and \((-d-x)dx/y\). These span the holomorphic differential space, so \(\operatorname{Jac}(C)\) is rationally isogenous to \(\operatorname{Res}_{K/\mathbf Q}(E)\) and also has rank one. [Reproducible descent](abc_octic_mixed_untwisted_cube.py) · [Simon's Sage sources](https://github.com/sagemath/sage/tree/8de8dad7bcb38e1baa43508cbe944bf04a2d0401/src/sage/ext_data/pari/simon)

## The dyadic disk at infinity

Let \(r=1/x=b/a\in2\mathbf Z_2\) and \(w=y/x^3\). Then
\[
 w^2=1-6r+6r^2+40r^3+12r^4-24r^5+8r^6.
\]
For \(r\equiv2\pmod4\) the right-hand side is 5 modulo 8. Hence \(r\in4\mathbf Z_2\). Choose the sign of \(w\) giving \(w\equiv1\pmod4\). Both signs of \(y\) are available.

Write \(\mathcal O=\mathbf Z_2[d]\). For a point in the elliptic formal group with parameter \(z=-X/Y\in4\mathcal O\), the formal logarithm satisfies \(\log_E(z)/z\equiv1\pmod{2\mathcal O}\). Its coefficients in degree \(j\) belong to \((1/j)\mathcal O\) because the invariant differential is integral. The logarithm extends to \(E(K_2)\otimes\mathbf Q\), since the formal subgroup has finite index. The rank bound forces every global logarithm to lie on the \(\mathbf Q_2\)-line of \(\log_E(4P)\).

We identify that line modulo \(2\mathcal O\), with coordinates in the basis \(1,d\). Exact doubling gives
\[
 2P=(3/4-3d/2,(7d-43)/8),\qquad z(2P)=(90-474d)/1751.
\]
This point belongs to the formal subgroup. The doubling series is \(2z+O(z^3)\), since \(a_1=0\). Thus \(z(4P)\in4\mathcal O\) and
\[
 \log_E(4P)/4\equiv 1+d\pmod{2\mathcal O}.
\]
In particular \(P\) is nontorsion, and the global line has primitive residue vector \((1,1)\).

On the other hand, put \(h_0=1+dr\). The point \(Q\in E(K)\) coming from the finite parameter is
\[
 Q=(2cr/h_0^2,cw/h_0^3).
\]
For nonzero \(r\) the chord from \(-P\) to \(Q\) has slope
\[
 \lambda=(w+h_0^3)/(2rh_0),\qquad r\lambda\equiv1\pmod{2\mathcal O}.
\]
Writing \(X'=\lambda^2-(6+6d)-X(Q)\), one has \(r^2X'\equiv1\pmod{2\mathcal O}\). The ordinate of \(Q-P\) is \(-\lambda X'+c\), so its formal parameter is
\[
 z(Q-P)=1/(\lambda-c/X'),\qquad z(Q-P)/r\equiv1\pmod{2\mathcal O}.
\]
It follows that the primitive residue vector of \(\log_E(Q-P)/r\) is \((1,0)\). This vector and \((1,1)\) are distinct nonzero vectors modulo 2. Two vectors on the same \(\mathbf Q_2\)-line with primitive integral coefficient vectors must differ by a 2-adic unit and have the same nonzero residue. The contradiction rules out every nonzero \(r\) in the admissible disk.

## Integral dyadic slopes

The preceding argument already covers every finite rational point with \(v_2(x)<0\), since the square condition itself forced \(1/x\in4\mathbf Z_2\). If \(x\in2\mathbf Z_2\), the sextic is 8 modulo 16 and cannot be a square. It remains to treat odd \(x\), for which \(y\) is odd. In the quadratic ring \(\mathcal O/2\mathcal O\) one has \(d^2=0\). Thus the elliptic image \(Q=(X,Y)\) satisfies
\[
 X\in4\mathcal O,\qquad
 Y/2=(1-d)y/(x+d)^3\equiv (1+d)/(1+d)^3=1\pmod{2\mathcal O}.
\]
Let \(a_2=6+6d\). Its doubling tangent is
\[
 \lambda=(3X^2+2a_2X+6)/(2Y),\qquad 2\lambda\equiv1\pmod{2\mathcal O}.
\]
Writing \(X'=\lambda^2-a_2-2X\) for the abscissa of \(2Q\), we obtain \(4X'\equiv1\pmod{2\mathcal O}\). Its ordinate is \(-\lambda X'+\lambda X-Y\), so \(2Q\) lies in the formal group and
\[
    z(2Q)/2=1/\bigl(2\lambda-2(\lambda X-Y)/X'\bigr)
        \equiv1\pmod{2\mathcal O}.
\]
One more doubling as above gives \(\log_E(4Q)/4\equiv1\pmod{2\mathcal O}\), again incompatible with the global line \((1,1)\). This covers all rational affine \(x\). The monic, separable sextic has two rational points at infinity, completing the classification.
